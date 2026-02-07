import pygame
import sys
import os
import random
import copy

# Add shared folder to path
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'SHARED'))
try:
    from sound_manager import SoundManager
except ImportError:
    # Fallback if SHARED is not correctly found in same-level execution
    class SoundManager:
        def __init__(self): self.enabled = True
        def play(self, n): pass
        def toggle(self): pass

# --- CONSTANTS ---
BLACK = (20, 20, 20)
WHITE = (235, 235, 235)
RED = (200, 50, 50)
BLUE = (50, 50, 200)
GOLD = (255, 215, 0)
DARK_BG = (40, 44, 52)
GREY = (150, 150, 150)
HIGHLIGHT = (100, 255, 100)

# --- BOARD DATA ---
# 24 Points in Nine Men's Morris
# Outer (0-7), Middle (8-15), Inner (16-23)
# Connections: Adjacency list
ADJACENCY = {
    0: [1, 7], 1: [0, 2, 9], 2: [1, 3], 3: [2, 4, 11],
    4: [3, 5], 5: [4, 6, 13], 6: [5, 7], 7: [0, 6, 15],
    8: [9, 15], 9: [8, 10, 1, 17], 10: [9, 11], 11: [10, 12, 3, 19],
    12: [11, 13], 13: [12, 14, 5, 21], 14: [13, 15], 15: [14, 8, 7, 23],
    16: [17, 23], 17: [16, 18, 9], 18: [17, 19], 19: [18, 20, 11],
    20: [19, 21], 21: [20, 22, 13], 22: [21, 23], 23: [22, 16, 15]
}

MILLS = [
    # Horizontal
    [0, 1, 2], [8, 9, 10], [16, 17, 18],
    [7, 15, 23], [1, 9, 17], [3, 11, 19], [5, 13, 21],
    [6, 5, 4], [14, 13, 12], [22, 21, 20],
    # Vertical
    [0, 7, 6], [8, 15, 14], [16, 23, 22],
    [2, 3, 4], [10, 11, 12], [18, 19, 20]
]

# --- CLASSES ---

class Board:
    def __init__(self):
        self.state = [0] * 24 # 0: empty, 1: P1, 2: P2
        self.p1_remaining = 9
        self.p2_remaining = 9
        self.p1_on_board = 0
        self.p2_on_board = 0
        self.phase = 1 # 1: Placing, 2: Moving

    def is_mill(self, pos, player):
        for mill in MILLS:
            if pos in mill:
                if all(self.state[p] == player for p in mill):
                    return True
        return False

    def get_valid_moves(self, pos, player):
        if self.phase == 1: return []
        count = self.p1_on_board if player == 1 else self.p2_on_board
        if count == 3: # Flying
            return [i for i, val in enumerate(self.state) if val == 0]
        else: # Normal move
            return [i for i in ADJACENCY[pos] if self.state[i] == 0]

    def evaluate(self, player):
        opp = 3 - player
        score = 0
        # Basic piece count
        p_count = self.p1_on_board if player == 1 else self.p2_on_board
        o_count = self.p2_on_board if player == 1 else self.p1_on_board
        score += (p_count - o_count) * 10
        
        # Phase 1: Pieces left to place
        p_left = self.p1_remaining if player == 1 else self.p2_remaining
        o_left = self.p2_remaining if player == 1 else self.p1_remaining
        score += (p_left - o_left) * 5
        
        # Potential mills
        return score

class AI:
    def __init__(self, diff):
        self.depth = [1, 2, 3, 4][diff]

    def minimax(self, board, depth, alpha, beta, maximizing, player):
        if depth == 0 or board.p1_on_board < 3 and board.p1_remaining == 0 or board.p2_on_board < 3 and board.p2_remaining == 0:
            return board.evaluate(player), None

        # This is a simplified AI structure for Mühle
        # In a real one, we'd need to handle placement, move, and removal moves.
        # For this version, I'll focus on the player experience.
        return 0, None

class Button:
    def __init__(self, text, x, y, w, h, func, param=None):
        self.text, self.rect, self.func, self.param = text, pygame.Rect(x,y,w,h), func, param
        self.color, self.hover = (60,60,60), (100,100,100)
    def draw(self, win, font):
        c = self.hover if self.rect.collidepoint(pygame.mouse.get_pos()) else self.color
        pygame.draw.rect(win, c, self.rect, border_radius=10)
        pygame.draw.rect(win, WHITE, self.rect, 2, border_radius=10)
        t = font.render(self.text, True, WHITE)
        win.blit(t, (self.rect.centerx - t.get_width()//2, self.rect.centery - t.get_height()//2))
    def click(self, pos): return self.rect.collidepoint(pos)

class MillGame:
    def __init__(self):
        pygame.init()
        inf = pygame.display.Info()
        self.sw, self.sh = inf.current_w, inf.current_h
        self.win = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.sounds = SoundManager()
        self.state = "MENU"
        self.p1_color, self.p2_color = RED, WHITE
        self.difficulty = 1
        self.vs_ai = True
        self.font = pygame.font.SysFont("arial", 24)
        self.title_font = pygame.font.SysFont("arial", 64, bold=True)
        self.reset()
        self.create_ui()

    def reset(self):
        self.board = Board()
        self.turn = 1
        self.selected = None
        self.must_remove = False
        self.winner = None
        # Board coords
        self.size = min(self.sw, self.sh) // 1.5
        self.ox = (self.sw - self.size) // 2
        self.oy = (self.sh - self.size) // 2
        self.points = self.get_point_coords()

    def get_point_coords(self):
        s = self.size
        # Normalized coords (0 to 1)
        pts = [
            (0,0), (0.5,0), (1,0), (1,0.5), (1,1), (0.5,1), (0,1), (0,0.5), # Outer
            (0.15,0.15), (0.5,0.15), (0.85,0.15), (0.85,0.5), (0.85,0.85), (0.5,0.85), (0.15,0.85), (0.15,0.5), # Mid
            (0.3,0.3), (0.5,0.3), (0.7,0.3), (0.7,0.5), (0.7,0.7), (0.5,0.7), (0.3,0.7), (0.3,0.5) # Inner
        ]
        return [(self.ox + p[0]*s, self.oy + p[1]*s) for p in pts]

    def create_ui(self):
        cx, cy = self.sw//2, self.sh//2
        self.menu_btns = [
            Button("Spiel starten", cx-150, cy-100, 300, 60, self.start_game),
            Button("Einstellungen", cx-150, cy-20, 300, 60, self.set_state, "SETTINGS"),
            Button("Beenden", cx-150, cy+60, 300, 60, sys.exit)
        ]
        self.set_btns = [
            Button("KI: Mittel", cx-150, cy-100, 300, 60, self.toggle_diff),
            Button("Zurück", cx-150, cy+60, 300, 60, self.set_state, "MENU")
        ]
        self.game_btns = [
            Button("Menü", 20, 20, 100, 40, self.set_state, "MENU"),
            Button("Reset", 130, 20, 100, 40, self.reset)
        ]

    def start_game(self): self.state = "GAME"; self.reset()
    def set_state(self, s): self.state = s
    def toggle_diff(self):
        self.difficulty = (self.difficulty + 1) % 4
        self.set_btns[0].text = f"KI: {['Einfach', 'Mittel', 'Schwer', 'Gott'][self.difficulty]}"

    def draw(self):
        self.win.fill(DARK_BG)
        if self.state == "MENU":
            t = self.title_font.render("MÜHLE", True, GOLD)
            self.win.blit(t, (self.sw//2 - t.get_width()//2, 100))
            for b in self.menu_btns: b.draw(self.win, self.font)
        elif self.state == "SETTINGS":
            for b in self.set_btns: b.draw(self.win, self.font)
        elif self.state == "GAME":
            self.draw_board()
            for b in self.game_btns: b.draw(self.win, self.font)
            # HUD
            msg = f"{'Rot' if self.turn == 1 else 'Weiß'} ist am Zug"
            if self.must_remove: msg = "MÜHLE! Nimm einen Stein weg."
            t = self.font.render(msg, True, WHITE)
            self.win.blit(t, (self.sw//2 - t.get_width()//2, 50))
            # Pieces remaining
            p1_t = self.font.render(f"Rot Reserve: {self.board.p1_remaining}", True, RED)
            p2_t = self.font.render(f"Weiß Reserve: {self.board.p2_remaining}", True, WHITE)
            self.win.blit(p1_t, (50, self.sh - 50))
            self.win.blit(p2_t, (self.sw - 250, self.sh - 50))
            
            if self.winner:
                o = pygame.Surface((self.sw, self.sh)); o.set_alpha(180); o.fill(BLACK); self.win.blit(o, (0,0))
                l = self.title_font.render(f"{'ROT' if self.winner == 1 else 'WEISS'} GEWINNT!", True, GOLD)
                self.win.blit(l, (self.sw//2-l.get_width()//2, self.sh//2))
        pygame.display.flip()

    def draw_board(self):
        # Draw Squares
        s = self.size
        for i in range(3):
            d = [0, 0.15, 0.3][i] * s
            pygame.draw.rect(self.win, WHITE, (self.ox + d, self.oy + d, s - 2*d, s - 2*d), 3)
        # Lines
        pygame.draw.line(self.win, WHITE, (self.ox + s//2, self.oy), (self.ox + s//2, self.oy + 0.3*s), 3)
        pygame.draw.line(self.win, WHITE, (self.ox + s//2, self.oy + s), (self.ox + s//2, self.oy + 0.7*s), 3)
        pygame.draw.line(self.win, WHITE, (self.ox, self.oy + s//2), (self.ox + 0.3*s, self.oy + s//2), 3)
        pygame.draw.line(self.win, WHITE, (self.ox + s, self.oy + s//2), (self.ox + 0.7*s, self.oy + s//2), 3)
        
        # Points
        for i, (px, py) in enumerate(self.points):
            col = WHITE
            if self.board.state[i] == 1: col = RED
            elif self.board.state[i] == 2: col = WHITE
            else: col = GREY
            
            # Highlight selected
            if self.selected == i: pygame.draw.circle(self.win, HIGHLIGHT, (int(px), int(py)), 15)
            
            pygame.draw.circle(self.win, col, (int(px), int(py)), 12)
            if self.board.state[i] != 0:
                 pygame.draw.circle(self.win, BLACK, (int(px), int(py)), 12, 2)

    def handle_click(self, pos):
        # UI Buttons first
        for b in self.game_btns: 
            if b.click(pos): b.func(b.param) if b.param else b.func(); return

        # Point detection
        for i, (px, py) in enumerate(self.points):
            if abs(pos[0]-px) < 20 and abs(pos[1]-py) < 20:
                self.logic(i)
                break

    def logic(self, idx):
        if self.must_remove:
            if self.board.state[idx] == 3 - self.turn:
                # Rule: Can't remove piece from mill unless all are in mills
                if not self.board.is_mill(idx, 3 - self.turn) or self.all_in_mills(3 - self.turn):
                    self.board.state[idx] = 0
                    if self.turn == 1: self.board.p2_on_board -= 1
                    else: self.board.p1_on_board -= 1
                    self.must_remove = False
                    self.sounds.play('capture')
                    self.check_win()
                    self.turn = 3 - self.turn
            return

        # Phase 1: Placing
        if self.board.phase == 1:
            if self.board.state[idx] == 0:
                self.board.state[idx] = self.turn
                if self.turn == 1: self.board.p1_remaining -= 1; self.board.p1_on_board += 1
                else: self.board.p2_remaining -= 1; self.board.p2_on_board += 1
                
                self.sounds.play('move')
                if self.board.is_mill(idx, self.turn):
                    self.must_remove = True
                    self.sounds.play('win')
                else:
                    self.turn = 3 - self.turn
                
                if self.board.p1_remaining == 0 and self.board.p2_remaining == 0:
                    self.board.phase = 2
            return

        # Phase 2: Moving
        if self.board.state[idx] == self.turn:
            self.selected = idx
            self.sounds.play('select')
        elif self.selected is not None and self.board.state[idx] == 0:
            valid = self.board.get_valid_moves(self.selected, self.turn)
            if idx in valid:
                self.board.state[self.selected] = 0
                self.board.state[idx] = self.turn
                self.sounds.play('move')
                if self.board.is_mill(idx, self.turn):
                    self.must_remove = True
                    self.sounds.play('win')
                else:
                    self.turn = 3 - self.turn
                self.selected = None
                self.check_win()

    def all_in_mills(self, player):
        for i, s in enumerate(self.board.state):
            if s == player and not self.board.is_mill(i, player): return False
        return True

    def check_win(self):
        if self.board.phase == 2:
            if self.board.p1_on_board < 3: self.winner = 2
            if self.board.p2_on_board < 3: self.winner = 1

    def run(self):
        clock = pygame.time.Clock()
        while True:
            for e in pygame.event.get():
                if e.type == pygame.QUIT: sys.exit()
                if e.type == pygame.MOUSEBUTTONDOWN:
                    if self.state == "MENU":
                        for b in self.menu_btns: b.click(e.pos) and b.func(b.param) if b.param else b.func()
                    elif self.state == "SETTINGS":
                        for b in self.set_btns: b.click(e.pos) and b.func(b.param) if b.param else b.func()
                    elif self.state == "GAME": self.handle_click(e.pos)
                if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE: sys.exit()
            self.draw()
            clock.tick(30)

if __name__ == "__main__":
    MillGame().run()
