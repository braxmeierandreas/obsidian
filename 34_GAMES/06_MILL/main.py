import pygame
import sys
import os
import random

# --- PATH SETUP ---
try:
    # Ensure we can find the SHARED folder
    script_dir = os.path.dirname(os.path.abspath(__file__))
    shared_dir = os.path.join(os.path.dirname(script_dir), 'SHARED')
    sys.path.append(shared_dir)
    from sound_manager import SoundManager
    print(f"Shared directory found at: {shared_dir}")
except Exception as e:
    print(f"Warning: Could not load SoundManager: {e}")
    class SoundManager:
        def __init__(self): self.enabled = False
        def play(self, n): pass
        def toggle(self): pass

# --- CONSTANTS ---
COLORS = {
    'BLACK': (20, 20, 20),
    'WHITE': (235, 235, 235),
    'RED': (220, 50, 50),
    'BLUE': (50, 50, 220),
    'GOLD': (255, 215, 0),
    'DARK_BG': (35, 38, 45),
    'GREY': (120, 120, 120),
    'HIGHLIGHT': (0, 255, 0),
    'LINE': (200, 200, 200)
}

ADJACENCY = {
    0: [1, 7], 1: [0, 2, 9], 2: [1, 3], 3: [2, 4, 11],
    4: [3, 5], 5: [4, 6, 13], 6: [5, 7], 7: [0, 6, 15],
    8: [9, 15], 9: [8, 10, 1, 17], 10: [9, 11], 11: [10, 12, 3, 19],
    12: [11, 13], 13: [12, 14, 5, 21], 14: [13, 15], 15: [14, 8, 7, 23],
    16: [17, 23], 17: [16, 18, 9], 18: [17, 19], 19: [18, 20, 11],
    20: [19, 21], 21: [20, 22, 13], 22: [21, 23], 23: [22, 16, 15]
}

MILLS = [
    [0, 1, 2], [8, 9, 10], [16, 17, 18], [7, 15, 23], [1, 9, 17], [3, 11, 19], [5, 13, 21],
    [6, 5, 4], [14, 13, 12], [22, 21, 20], [0, 7, 6], [8, 15, 14], [16, 23, 22],
    [2, 3, 4], [10, 11, 12], [18, 19, 20]
]

class Board:
    def __init__(self):
        self.state = [0] * 24
        self.p1_res = 9
        self.p2_res = 9
        self.p1_on = 0
        self.p2_on = 0
        self.phase = 1

    def is_mill(self, pos, player):
        for mill in MILLS:
            if pos in mill:
                if all(self.state[p] == player for p in mill):
                    return True
        return False

class Button:
    def __init__(self, text, x, y, w, h, func, param=None):
        self.text, self.rect, self.func, self.param = text, pygame.Rect(x,y,w,h), func, param
    def draw(self, win, font):
        color = (80,80,80) if self.rect.collidepoint(pygame.mouse.get_pos()) else (50,50,50)
        pygame.draw.rect(win, color, self.rect, border_radius=8)
        pygame.draw.rect(win, COLORS['WHITE'], self.rect, 2, border_radius=8)
        t = font.render(self.text, True, COLORS['WHITE'])
        win.blit(t, (self.rect.centerx - t.get_width()//2, self.rect.centery - t.get_height()//2))
    def click(self, pos): return self.rect.collidepoint(pos)

class MillGame:
    def __init__(self):
        pygame.init()
        self.fullscreen = False
        self.sw, self.sh = 1000, 800
        self.win = pygame.display.set_mode((self.sw, self.sh), pygame.RESIZABLE)
        pygame.display.set_caption("Mühle Ultimate")
        
        self.sounds = SoundManager()
        self.font = pygame.font.SysFont("arial", 22)
        self.big_font = pygame.font.SysFont("arial", 48, bold=True)
        self.state = "MENU"
        self.reset()

    def reset(self):
        self.board = Board()
        self.turn = 1
        self.selected = None
        self.must_remove = False
        self.winner = None
        self.recalc_geometry()

    def recalc_geometry(self):
        self.sw, self.sh = self.win.get_size()
        self.size = min(self.sw, self.sh) * 0.7
        self.ox = (self.sw - self.size) // 2
        self.oy = (self.sh - self.size) // 2
        s = self.size
        pts = [
            (0,0), (0.5,0), (1,0), (1,0.5), (1,1), (0.5,1), (0,1), (0,0.5),
            (0.15,0.15), (0.5,0.15), (0.85,0.15), (0.85,0.5), (0.85,0.85), (0.5,0.85), (0.15,0.85), (0.15,0.5),
            (0.3,0.3), (0.5,0.3), (0.7,0.3), (0.7,0.5), (0.7,0.7), (0.5,0.7), (0.3,0.7), (0.3,0.5)
        ]
        self.point_coords = [(self.ox + p[0]*s, self.oy + p[1]*s) for p in pts]

    def draw(self):
        self.win.fill(COLORS['DARK_BG'])
        if self.state == "MENU":
            self.draw_menu()
        elif self.state == "GAME":
            self.draw_game()
        pygame.display.flip()

    def draw_menu(self):
        t = self.big_font.render("MÜHLE", True, COLORS['GOLD'])
        self.win.blit(t, (self.sw//2 - t.get_width()//2, self.sh//3))
        self.start_btn = Button("Spiel starten", self.sw//2-100, self.sh//2, 200, 50, self.start_game)
        self.fs_btn = Button("Vollbild Umschalten", self.sw//2-100, self.sh//2 + 70, 200, 50, self.toggle_fs)
        self.start_btn.draw(self.win, self.font)
        self.fs_btn.draw(self.win, self.font)

    def draw_game(self):
        s = self.size
        # Board lines
        for i in range(3):
            d = [0, 0.15, 0.3][i] * s
            pygame.draw.rect(self.win, COLORS['LINE'], (self.ox + d, self.oy + d, s - 2*d, s - 2*d), 3)
        pygame.draw.line(self.win, COLORS['LINE'], (self.ox + s//2, self.oy), (self.ox + s//2, self.oy + 0.3*s), 3)
        pygame.draw.line(self.win, COLORS['LINE'], (self.ox + s//2, self.oy + s), (self.ox + s//2, self.oy + 0.7*s), 3)
        pygame.draw.line(self.win, COLORS['LINE'], (self.ox, self.oy + s//2), (self.ox + 0.3*s, self.oy + s//2), 3)
        pygame.draw.line(self.win, COLORS['LINE'], (self.ox + s, self.oy + s//2), (self.ox + 0.7*s, self.oy + s//2), 3)

        # Points
        for i, (px, py) in enumerate(self.point_coords):
            col = COLORS['GREY']
            if self.board.state[i] == 1: col = COLORS['RED']
            elif self.board.state[i] == 2: col = COLORS['WHITE']
            
            if self.selected == i:
                pygame.draw.circle(self.win, COLORS['HIGHLIGHT'], (int(px), int(py)), 18, 3)
            
            pygame.draw.circle(self.win, col, (int(px), int(py)), 14)
            pygame.draw.circle(self.win, COLORS['BLACK'], (int(px), int(py)), 14, 2)

        # UI
        status = f"{'Rot' if self.turn == 1 else 'Weiß'} ist am Zug"
        if self.must_remove: status = "MÜHLE! Nimm einen Stein weg."
        st_t = self.font.render(status, True, COLORS['WHITE'])
        self.win.blit(st_t, (self.sw//2 - st_t.get_width()//2, 20))
        
        p1_info = self.font.render(f"Rot: {self.board.p1_res} Res, {self.board.p1_on} Feld", True, COLORS['RED'])
        p2_info = self.font.render(f"Weiß: {self.board.p2_res} Res, {self.board.p2_on} Feld", True, COLORS['WHITE'])
        self.win.blit(p1_info, (20, self.sh - 40))
        self.win.blit(p2_info, (self.sw - p2_info.get_width() - 20, self.sh - 40))
        
        self.back_btn = Button("Menü", 20, 20, 80, 35, self.to_menu)
        self.back_btn.draw(self.win, self.font)

        if self.winner:
            ov = pygame.Surface((self.sw, self.sh), pygame.SRCALPHA)
            ov.fill((0,0,0,180))
            self.win.blit(ov, (0,0))
            wt = self.big_font.render(f"{'ROT' if self.winner == 1 else 'WEISS'} GEWINNT!", True, COLORS['GOLD'])
            self.win.blit(wt, (self.sw//2-wt.get_width()//2, self.sh//2-50))
            self.rem_btn = Button("Nochmal spielen", self.sw//2-100, self.sh//2+50, 200, 50, self.reset)
            self.rem_btn.draw(self.win, self.font)

    def start_game(self): self.state = "GAME"; self.reset()
    def to_menu(self): self.state = "MENU"
    def toggle_fs(self):
        self.fullscreen = not self.fullscreen
        if self.fullscreen: self.win = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        else: self.win = pygame.display.set_mode((1000, 800), pygame.RESIZABLE)
        self.recalc_geometry()

    def run(self):
        clock = pygame.time.Clock()
        while True:
            for e in pygame.event.get():
                if e.type == pygame.QUIT: pygame.quit(); sys.exit()
                if e.type == pygame.VIDEORESIZE and not self.fullscreen: self.recalc_geometry()
                if e.type == pygame.MOUSEBUTTONDOWN:
                    if self.state == "MENU":
                        if self.start_btn.click(e.pos): self.start_btn.func()
                        if self.fs_btn.click(e.pos): self.fs_btn.func()
                    elif self.state == "GAME":
                        if self.back_btn.click(e.pos): self.back_btn.func()
                        elif self.winner and self.rem_btn.click(e.pos): self.rem_btn.func()
                        else: self.game_click(e.pos)
                if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE: pygame.quit(); sys.exit()
            self.draw()
            clock.tick(30)

    def game_click(self, pos):
        for i, (px, py) in enumerate(self.point_coords):
            if abs(pos[0]-px) < 20 and abs(pos[1]-py) < 20:
                self.handle_logic(i)
                break

    def handle_logic(self, idx):
        if self.winner: return
        if self.must_remove:
            if self.board.state[idx] == 3 - self.turn:
                # Rule: Can't take from mill unless all are in mills
                if not self.board.is_mill(idx, 3-self.turn) or self.all_in_mills(3-self.turn):
                    self.board.state[idx] = 0
                    if self.turn == 1: self.board.p2_on -= 1
                    else: self.board.p1_on -= 1
                    self.must_remove = False
                    self.sounds.play('capture')
                    self.turn = 3 - self.turn
                    self.check_game_over()
            return

        if self.board.phase == 1:
            if self.board.state[idx] == 0:
                self.board.state[idx] = self.turn
                if self.turn == 1: self.board.p1_res -= 1; self.board.p1_on += 1
                else: self.board.p2_res -= 1; self.board.p2_on += 1
                self.sounds.play('move')
                if self.board.is_mill(idx, self.turn):
                    self.must_remove = True
                    self.sounds.play('win')
                else: self.turn = 3 - self.turn
                if self.board.p1_res == 0 and self.board.p2_res == 0: self.board.phase = 2
            return

        if self.board.state[idx] == self.turn:
            self.selected = idx
            self.sounds.play('select')
        elif self.selected is not None and self.board.state[idx] == 0:
            # Check move validity
            can_jump = (self.board.p1_on == 3 if self.turn == 1 else self.board.p2_on == 3)
            if can_jump or idx in ADJACENCY[self.selected]:
                self.board.state[self.selected] = 0
                self.board.state[idx] = self.turn
                self.sounds.play('move')
                if self.board.is_mill(idx, self.turn):
                    self.must_remove = True
                    self.sounds.play('win')
                else: self.turn = 3 - self.turn
                self.selected = None
                self.check_game_over()

    def all_in_mills(self, p):
        for i in range(24):
            if self.board.state[i] == p and not self.board.is_mill(i, p): return False
        return True

    def check_game_over(self):
        if self.board.phase == 2:
            if self.board.p1_on < 3: self.winner = 2
            elif self.board.p2_on < 3: self.winner = 1
            # Also check if blocked (simplified check)
            # ...

if __name__ == "__main__":
    try:
        MillGame().run()
    except Exception as e:
        import traceback
        with open("crash_log.txt", "w") as f:
            f.write(str(e) + "\n" + traceback.format_exc())
        print(f"CRASH! Error saved to crash_log.txt: {e}")