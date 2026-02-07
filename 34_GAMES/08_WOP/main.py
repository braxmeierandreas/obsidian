import pygame
import sys
import os
import random

# --- PATH SETUP ---
try:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    shared_dir = os.path.join(os.path.dirname(script_dir), 'SHARED')
    sys.path.append(shared_dir)
    from sound_manager import SoundManager
except Exception as e:
    class SoundManager:
        def __init__(self): self.enabled = False
        def play(self, n): pass
        def start_jazz(self, f): pass
        def toggle(self): pass

# --- CONSTANTS ---
COLORS = {
    'BLACK': (20, 20, 20),
    'WHITE': (235, 235, 235),
    'RED': (220, 50, 50),
    'GREEN': (50, 220, 50),
    'BLUE': (50, 50, 220),
    'GOLD': (255, 215, 0),
    'DARK_BG': (35, 38, 45),
    'GREY': (120, 120, 120),
    'PURPLE': (150, 50, 220),
    'ORANGE': (255, 140, 0)
}

PROMPT_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "prompts.txt")
PUNISH_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "punishments.txt")
JAZZ_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "jazz.mp3")

def load_list(path):
    data = {}
    current_cat = None
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith("# "):
                    current_cat = line[2:]
                    if current_cat not in data: data[current_cat] = []
                elif line and current_cat:
                    data[current_cat].append(line)
    return data

class Button:
    def __init__(self, text, x, y, w, h, func, param=None, color=None):
        self.text = text
        self.rect = pygame.Rect(x, y, w, h)
        self.func = func
        self.param = param
        self.base_color = color if color else (50, 50, 50)
    
    def draw(self, win, font):
        m = pygame.mouse.get_pos()
        c = tuple(min(255, val + 30) for val in self.base_color) if self.rect.collidepoint(m) else self.base_color
        pygame.draw.rect(win, c, self.rect, border_radius=12)
        pygame.draw.rect(win, COLORS['WHITE'], self.rect, 2, border_radius=12)
        t = font.render(self.text, True, COLORS['WHITE'])
        win.blit(t, (self.rect.centerx - t.get_width()//2, self.rect.centery - t.get_height()//2))
    
    def click(self, pos):
        return self.rect.collidepoint(pos)

class VirtualKeyboard:
    def __init__(self, x, y, w, h, callback):
        self.rect = pygame.Rect(x, y, w, h)
        self.callback = callback
        self.keys = "QWERTZUIOPÜASDFGHJKLÖYXCVBNM"
        self.buttons = []
        self.create_keys()
        
    def create_keys(self):
        rows = 3
        cols = 10
        margin = 5
        key_w = (self.rect.width - (cols+1)*margin) // cols
        key_h = (self.rect.height - (rows+1)*margin) // rows
        
        # Row 1
        for i, char in enumerate("QWERTZUIOPÜ"):
            bx = self.rect.x + margin + i*(key_w+margin)
            by = self.rect.y + margin
            self.buttons.append(Button(char, bx, by, key_w, key_h, self.callback, char, (60,60,60)))
            
        # Row 2
        for i, char in enumerate("ASDFGHJKLÖÄ"):
            bx = self.rect.x + margin + (key_w//2) + i*(key_w+margin)
            by = self.rect.y + margin + key_h + margin
            self.buttons.append(Button(char, bx, by, key_w, key_h, self.callback, char, (60,60,60)))
            
        # Row 3
        for i, char in enumerate("YXCVBNM"):
            bx = self.rect.x + margin + (key_w*1.5) + i*(key_w+margin)
            by = self.rect.y + margin + 2*(key_h + margin)
            self.buttons.append(Button(char, bx, by, key_w, key_h, self.callback, char, (60,60,60)))
            
        # Backspace
        self.buttons.append(Button("<", self.rect.right - key_w*1.5 - margin, self.rect.bottom - key_h - margin, key_w*1.5, key_h, self.callback, "BACK", (100,50,50)))

    def draw(self, win, font):
        pygame.draw.rect(win, (30,30,30), self.rect)
        for b in self.buttons:
            b.draw(win, font)

    def click(self, pos):
        if not self.rect.collidepoint(pos): return False
        for b in self.buttons:
            if b.click(pos):
                b.func(b.param)
                return True
        return False

class WoPGame:
    def __init__(self):
        pygame.init()
        # Enable text input for reliable typing
        pygame.key.start_text_input()
        
        self.fullscreen = False
        self.sw, self.sh = 1000, 800
        self.win = pygame.display.set_mode((self.sw, self.sh), pygame.RESIZABLE)
        pygame.display.set_caption("Wahrheit oder Pflicht - Ultimate")
        
        self.sounds = SoundManager()
        self.sounds.start_jazz(JAZZ_FILE)
        
        self.font = pygame.font.SysFont("arial", 22)
        self.big_font = pygame.font.SysFont("arial", 44, bold=True)
        self.text_font = pygame.font.SysFont("arial", 30)
        
        self.all_prompts = load_list(PROMPT_FILE)
        self.all_punishments = []
        if os.path.exists(PUNISH_FILE):
            with open(PUNISH_FILE, "r", encoding="utf-8") as f:
                self.all_punishments = [l.strip() for l in f if l.strip()]
        
        self.categories = list(set([c.split(' | ')[0] for c in self.all_prompts.keys()])) + ["ZUFALL MIX"]
        self.current_cat = "Lustig"
        
        self.players = []
        self.current_player_idx = 0
        self.input_text = ""
        
        self.state = "MENU"
        self.current_prompt = ""
        self.current_type = ""
        
        self.recalc_geometry()

    def recalc_geometry(self):
        if self.fullscreen:
            info = pygame.display.Info()
            self.sw, self.sh = info.current_w, info.current_h
        else:
            self.sw, self.sh = self.win.get_size()
            
        cx, cy = self.sw // 2, self.sh // 2
        bw, bh = 300, 55
        
        self.menu_btns = [
            Button("SPIELER BEARBEITEN", cx - bw//2, cy - 150, bw, bh, self.set_state, "PLAYERS", color=COLORS['BLUE']),
            Button("STARTEN", cx - bw//2, cy - 80, bw, bh, self.start_game, color=COLORS['GREEN']),
            Button(f"KATEGORIE: {self.current_cat}", cx - bw//2, cy - 10, bw, bh, self.toggle_cat, color=COLORS['PURPLE']),
            Button("VOLLBILD", cx - bw//2, cy + 60, bw, bh, self.toggle_fs),
            Button("BEENDEN", cx - bw//2, cy + 130, bw, bh, sys.exit, color=COLORS['RED'])
        ]
        
        self.btn_back = Button("ZURÜCK", 20, 20, 120, 40, self.set_state, "MENU")
        self.btn_start_now = Button("LOS GEHT'S", self.sw - 220, 20, 200, 40, self.start_game, color=COLORS['GREEN'])
        self.btn_add_player = Button("HINZUFÜGEN", cx + 110, 130, 140, 50, self.add_player_from_input, color=COLORS['GREEN'])
        
        # Virtual Keyboard (Bottom 30% of screen)
        kb_h = int(self.sh * 0.3)
        self.vk = VirtualKeyboard(0, self.sh - kb_h, self.sw, kb_h, self.vk_callback)

    def vk_callback(self, char):
        if char == "BACK":
            self.input_text = self.input_text[:-1]
        elif len(self.input_text) < 20:
            self.input_text += char

    def set_state(self, s):
        self.state = s
        self.input_text = ""
        self.sounds.play('select')
        self.recalc_geometry()

    def toggle_cat(self):
        idx = (self.categories.index(self.current_cat) + 1) % len(self.categories)
        self.current_cat = self.categories[idx]
        self.sounds.play('select')
        self.recalc_geometry()

    def toggle_fs(self):
        self.fullscreen = not self.fullscreen
        if self.fullscreen: self.win = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        else: self.win = pygame.display.set_mode((1000, 800), pygame.RESIZABLE)
        self.recalc_geometry()

    def add_player_from_input(self):
        if self.input_text.strip():
            self.players.append(self.input_text.strip())
            self.input_text = ""
            self.sounds.play('select')

    def start_game(self):
        if not self.players: self.players = ["Spieler 1"]
        self.current_player_idx = 0
        self.state = "CHOICE"
        self.sounds.play('select')

    def draw(self):
        self.win.fill(COLORS['DARK_BG'])
        if self.state == "MENU": self.draw_menu()
        elif self.state == "PLAYERS": self.draw_players()
        elif self.state == "CHOICE": self.draw_choice()
        elif self.state == "DISPLAY": self.draw_display()
        elif self.state == "PUNISH": self.draw_punish()
        pygame.display.flip()

    def draw_menu(self):
        t = self.big_font.render("WAHRHEIT ODER PFLICHT", True, COLORS['GOLD'])
        self.win.blit(t, (self.sw//2 - t.get_width()//2, self.sh//8))
        for b in self.menu_btns: b.draw(self.win, self.font)

    def draw_players(self):
        t = self.big_font.render("WER SPIELT MIT?", True, COLORS['WHITE'])
        self.win.blit(t, (self.sw//2 - t.get_width()//2, 50))
        
        # Input Box
        pygame.draw.rect(self.win, COLORS['BLACK'], (self.sw//2 - 250, 130, 350, 50), border_radius=5)
        pygame.draw.rect(self.win, COLORS['WHITE'], (self.sw//2 - 250, 130, 350, 50), 2, border_radius=5)
        
        it = self.font.render(self.input_text + "|", True, COLORS['WHITE'])
        self.win.blit(it, (self.sw//2 - 240, 140))
        
        self.btn_add_player.draw(self.win, self.font)
        self.btn_back.draw(self.win, self.font)
        if self.players: self.btn_start_now.draw(self.win, self.font)

        # List Players
        y = 220
        self.player_delete_rects = []
        for i, p in enumerate(self.players):
            if y > self.sh - self.vk.rect.height - 50: break # Stop if overlapping keyboard
            row_rect = pygame.Rect(self.sw//2 - 250, y, 500, 40)
            pygame.draw.rect(self.win, (60, 60, 70), row_rect, border_radius=5)
            txt = self.font.render(f"{i+1}. {p}", True, COLORS['GOLD'])
            self.win.blit(txt, (self.sw//2 - 230, y + 8))
            del_rect = pygame.Rect(self.sw//2 + 150, y + 8, 80, 25)
            pygame.draw.rect(self.win, (150, 50, 50), del_rect, border_radius=5)
            del_t = self.font.render("Löschen", True, COLORS['WHITE'])
            self.win.blit(del_t, (del_rect.centerx - del_t.get_width()//2, del_rect.centery - del_t.get_height()//2))
            self.player_delete_rects.append((i, del_rect))
            y += 50
            
        # Draw Virtual Keyboard
        self.vk.draw(self.win, self.font)

    def draw_choice(self):
        p_name = self.players[self.current_player_idx]
        t = self.big_font.render(f"{p_name.upper()}, WÄHLE!", True, COLORS['GOLD'])
        self.win.blit(t, (self.sw//2 - t.get_width()//2, self.sh//6))
        bw, bh = 400, 140
        self.choice_btns = [
            Button("WAHRHEIT", self.sw//2 - bw - 20, self.sh//2 - bh//2, bw, bh, self.get_prompt, "Wahrheit", color=COLORS['PURPLE']),
            Button("PFLICHT", self.sw//2 + 20, self.sh//2 - bh//2, bw, bh, self.get_prompt, "Pflicht", color=COLORS['ORANGE'])
        ]
        for b in self.choice_btns: b.draw(self.win, self.big_font)
        self.btn_back.draw(self.win, self.font)

    def draw_display(self):
        p_name = self.players[self.current_player_idx]
        cat_t = self.font.render(f"{p_name} | {self.current_type} ({self.current_cat})", True, COLORS['GREY'])
        self.win.blit(cat_t, (self.sw//2 - cat_t.get_width()//2, 50))
        self.render_wrapped_text(self.current_prompt, self.text_font, COLORS['WHITE'], self.sh//2)
        self.btn_done = Button("ERLEDIGT", self.sw//2 - 220, self.sh - 120, 200, 60, self.next_turn, color=COLORS['GREEN'])
        self.btn_fail = Button("TRAUE MICH NICHT", self.sw//2 + 20, self.sh - 120, 200, 60, self.to_punish, color=COLORS['RED'])
        self.btn_done.draw(self.win, self.font)
        self.btn_fail.draw(self.win, self.font)

    def draw_punish(self):
        t = self.big_font.render("STRAFE!", True, COLORS['RED'])
        self.win.blit(t, (self.sw//2 - t.get_width()//2, 100))
        self.render_wrapped_text(self.current_prompt, self.text_font, COLORS['ORANGE'], self.sh//2)
        self.btn_punish_done = Button("STRAFE ERLEDIGT", self.sw//2 - 100, self.sh - 120, 200, 60, self.next_turn, color=COLORS['BLUE'])
        self.btn_punish_done.draw(self.win, self.font)

    def render_wrapped_text(self, text, font, color, y_center):
        words = text.split(' ')
        lines, cur = [], ""
        for w in words:
            if font.size(cur + w)[0] < self.sw - 120: cur += w + " "
            else: lines.append(cur); cur = w + " "
        lines.append(cur)
        y = y_center - (len(lines) * 35) // 2
        for l in lines:
            s = font.render(l, True, color)
            self.win.blit(s, (self.sw//2 - s.get_width()//2, y))
            y += 40

    def next_turn(self):
        self.current_player_idx = (self.current_player_idx + 1) % len(self.players)
        self.state = "CHOICE"
        self.sounds.play('win')

    def to_punish(self):
        self.current_prompt = random.choice(self.all_punishments) if self.all_punishments else "10 Liegestütze!"
        self.state = "PUNISH"
        self.sounds.play('punish')

    def get_prompt(self, p_type):
        if self.current_cat == "ZUFALL MIX":
            valid_keys = [k for k in self.all_prompts.keys() if p_type in k]
            key = random.choice(valid_keys) if valid_keys else None
        else:
            key = f"{self.current_cat} | {p_type}"
        
        if key and key in self.all_prompts:
            self.current_prompt = random.choice(self.all_prompts[key])
            self.current_type = p_type
            self.state = "DISPLAY"
            self.sounds.play('move')
        else:
            self.current_prompt = "Nichts gefunden."
            self.state = "DISPLAY"
            self.sounds.play('error')

    def run(self):
        clock = pygame.time.Clock()
        while True:
            for e in pygame.event.get():
                if e.type == pygame.QUIT: pygame.quit(); sys.exit()
                if e.type == pygame.VIDEORESIZE: self.recalc_geometry()
                if e.type == pygame.TEXTINPUT and self.state == "PLAYERS":
                    if len(self.input_text) < 20: self.input_text += e.text
                if e.type == pygame.MOUSEBUTTONDOWN:
                    m = e.pos
                    if self.state == "MENU":
                        for b in self.menu_btns:
                            if b.click(m): b.func(b.param) if b.param else b.func()
                    elif self.state == "PLAYERS":
                        if self.btn_back.click(m): self.btn_back.func(self.btn_back.param)
                        if self.btn_add_player.click(m): self.btn_add_player.func()
                        if self.players and self.btn_start_now.click(m): self.btn_start_now.func()
                        if self.vk.click(m): pass # Handled inside vk
                        for i, r in self.player_delete_rects:
                            if r.collidepoint(m):
                                self.players.pop(i)
                                self.sounds.play('error')
                                break
                    elif self.state == "CHOICE":
                        for b in self.choice_btns:
                            if b.click(m): b.func(b.param)
                        if self.btn_back.click(m): self.btn_back.func(self.btn_back.param)
                    elif self.state == "DISPLAY":
                        if self.btn_done.click(m): self.btn_done.func()
                        if self.btn_fail.click(m): self.btn_fail.func()
                    elif self.state == "PUNISH":
                        if self.btn_punish_done.click(m): self.btn_punish_done.func()
                
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE: self.set_state("MENU")
                    if self.state == "PLAYERS":
                        if e.key == pygame.K_RETURN: self.add_player_from_input()
                        elif e.key == pygame.K_BACKSPACE: self.input_text = self.input_text[:-1]

            self.draw()
            clock.tick(30)

if __name__ == "__main__":
    WoPGame().run()
