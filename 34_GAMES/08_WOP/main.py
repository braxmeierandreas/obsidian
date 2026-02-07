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

def load_prompts():
    data = {}
    current_cat = None
    if os.path.exists(PROMPT_FILE):
        with open(PROMPT_FILE, "r", encoding="utf-8") as f:
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
        self.text, self.rect, self.func, self.param = text, pygame.Rect(x,y,w,h), func, param
        self.base_color = color if color else (50, 50, 50)
    def draw(self, win, font):
        color = tuple(min(255, c + 30) for c in self.base_color) if self.rect.collidepoint(pygame.mouse.get_pos()) else self.base_color
        pygame.draw.rect(win, color, self.rect, border_radius=12)
        pygame.draw.rect(win, COLORS['WHITE'], self.rect, 2, border_radius=12)
        t = font.render(self.text, True, COLORS['WHITE'])
        win.blit(t, (self.rect.centerx - t.get_width()//2, self.rect.centery - t.get_height()//2))
    def click(self, pos): return self.rect.collidepoint(pos)

class WoPGame:
    def __init__(self):
        pygame.init()
        self.fullscreen = False
        self.sw, self.sh = 1000, 800
        self.win = pygame.display.set_mode((self.sw, self.sh), pygame.RESIZABLE)
        pygame.display.set_caption("Wahrheit oder Pflicht - Ultimate")
        
        self.sounds = SoundManager()
        self.font = pygame.font.SysFont("arial", 24)
        self.big_font = pygame.font.SysFont("arial", 48, bold=True)
        self.text_font = pygame.font.SysFont("arial", 32)
        
        self.all_prompts = load_prompts()
        self.categories = ["Sex", "Party", "Lustig", "Peinlich"]
        self.current_category = "Lustig"
        
        self.state = "MENU" # MENU, CHOICE, DISPLAY, SETTINGS
        self.current_prompt = ""
        self.current_type = "" # Wahrheit / Pflicht
        self.recalc_geometry()

    def recalc_geometry(self):
        self.sw, self.sh = self.win.get_size()

    def draw(self):
        self.win.fill(COLORS['DARK_BG'])
        if self.state == "MENU": self.draw_menu()
        elif self.state == "CHOICE": self.draw_choice()
        elif self.state == "DISPLAY": self.draw_display()
        elif self.state == "SETTINGS": self.draw_settings()
        pygame.display.flip()

    def draw_menu(self):
        t = self.big_font.render("WAHRHEIT ODER PFLICHT", True, COLORS['GOLD'])
        self.win.blit(t, (self.sw//2 - t.get_width()//2, self.sh//6))
        
        bw, bh = 300, 60
        cx = self.sw//2 - bw//2
        cy = self.sh//2 - 120
        
        self.menu_btns = [
            Button("SPIEL STARTEN", cx, cy, bw, bh, self.to_choice, color=COLORS['GREEN']),
            Button(f"KATEGORIE: {self.current_category}", cx, cy + 80, bw, bh, self.toggle_cat, color=COLORS['BLUE']),
            Button("VOLLBILD UMSCHALTEN", cx, cy + 160, bw, bh, self.toggle_fs),
            Button("BEENDEN", cx, cy + 240, bw, bh, sys.exit, color=COLORS['RED'])
        ]
        for b in self.menu_btns: b.draw(self.win, self.font)

    def draw_choice(self):
        t = self.big_font.render(f"KATEGORIE: {self.current_category.upper()}", True, COLORS['WHITE'])
        self.win.blit(t, (self.sw//2 - t.get_width()//2, self.sh//4))
        
        bw, bh = 400, 150
        self.choice_btns = [
            Button("WAHRHEIT", self.sw//2 - bw - 20, self.sh//2 - bh//2, bw, bh, self.get_prompt, "Wahrheit", color=COLORS['PURPLE']),
            Button("PFLICHT", self.sw//2 + 20, self.sh//2 - bh//2, bw, bh, self.get_prompt, "Pflicht", color=COLORS['ORANGE'])
        ]
        for b in self.choice_btns: b.draw(self.win, self.big_font)
        
        self.back_btn = Button("ZURÜCK", 20, 20, 120, 40, self.to_menu)
        self.back_btn.draw(self.win, self.font)

    def draw_display(self):
        # Category header
        cat_t = self.font.render(f"Kategorie: {self.current_category} | {self.current_type}", True, COLORS['GREY'])
        self.win.blit(cat_t, (self.sw//2 - cat_t.get_width()//2, 50))
        
        # The Prompt
        words = self.current_prompt.split(' ')
        lines = []
        current_line = ""
        for w in words:
            if self.text_font.size(current_line + w)[0] < self.sw - 100:
                current_line += w + " "
            else:
                lines.append(current_line)
                current_line = w + " "
        lines.append(current_line)
        
        y_off = self.sh // 2 - (len(lines) * 40) // 2
        for line in lines:
            txt = self.text_font.render(line, True, COLORS['WHITE'])
            self.win.blit(txt, (self.sw//2 - txt.get_width()//2, y_off))
            y_off += 45
            
        self.next_btn = Button("NÄCHSTER SPIELER", self.sw//2 - 150, self.sh - 120, 300, 60, self.to_choice, color=COLORS['GREEN'])
        self.next_btn.draw(self.win, self.font)
        
        self.back_btn = Button("MENÜ", 20, 20, 120, 40, self.to_menu)
        self.back_btn.draw(self.win, self.font)

    def to_menu(self): self.state = "MENU"
    def to_choice(self): self.state = "CHOICE"

    def toggle_cat(self):
        idx = (self.categories.index(self.current_category) + 1) % len(self.categories)
        self.current_category = self.categories[idx]
        self.sounds.play('select')

    def toggle_fs(self):
        self.fullscreen = not self.fullscreen
        if self.fullscreen: self.win = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        else: self.win = pygame.display.set_mode((1000, 800), pygame.RESIZABLE)
        self.recalc_geometry()

    def get_prompt(self, p_type):
        key = f"{self.current_category} | {p_type}"
        if key in self.all_prompts and self.all_prompts[key]:
            self.current_prompt = random.choice(self.all_prompts[key])
            self.current_type = p_type
            self.state = "DISPLAY"
            self.sounds.play('move')
        else:
            self.current_prompt = "Keine Fragen in dieser Kategorie gefunden!"
            self.state = "DISPLAY"
            self.sounds.play('error')

    def run(self):
        clock = pygame.time.Clock()
        while True:
            for e in pygame.event.get():
                if e.type == pygame.QUIT: pygame.quit(); sys.exit()
                if e.type == pygame.VIDEORESIZE and not self.fullscreen: self.recalc_geometry()
                if e.type == pygame.MOUSEBUTTONDOWN:
                    if self.state == "MENU":
                        for b in self.menu_btns: b.click(e.pos) and b.func()
                    elif self.state == "CHOICE":
                        for b in self.choice_btns: b.click(e.pos) and b.func(b.param)
                        if self.back_btn.click(e.pos): self.back_btn.func()
                    elif self.state == "DISPLAY":
                        if self.next_btn.click(e.pos): self.next_btn.func()
                        if self.back_btn.click(e.pos): self.back_btn.func()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        if self.state == "MENU": pygame.quit(); sys.exit()
                        else: self.state = "MENU"
            self.draw()
            clock.tick(30)

if __name__ == "__main__":
    WoPGame().run()
