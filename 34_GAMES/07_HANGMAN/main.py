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
    'DARK_BG': (40, 44, 52),
    'GREY': (120, 120, 120)
}

WORD_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "words.txt")

def load_words():
    lists = {"Einfach": [], "Mittel": [], "Schwer": []}
    current_cat = "Mittel"
    if os.path.exists(WORD_FILE):
        with open(WORD_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith("# "):
                    cat = line[2:]
                    if cat in lists: current_cat = cat
                elif line and not line.startswith("#"):
                    lists[current_cat].append(line.upper())
    # Fallback if empty
    for k in lists:
        if not lists[k]: lists[k] = ["TEST"]
    return lists

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

class HangmanGame:
    def __init__(self):
        pygame.init()
        self.fullscreen = False
        self.sw, self.sh = 1000, 800
        self.win = pygame.display.set_mode((self.sw, self.sh), pygame.RESIZABLE)
        pygame.display.set_caption("Galgenmännchen Ultimate")
        
        self.sounds = SoundManager()
        self.font = pygame.font.SysFont("arial", 22)
        self.big_font = pygame.font.SysFont("arial", 48, bold=True)
        self.letter_font = pygame.font.SysFont("arial", 32, bold=True)
        
        self.all_words = load_words()
        self.difficulty = "Mittel"
        self.state = "MENU"
        self.input_text = ""
        self.multiplayer = False
        self.reset()

    def reset(self):
        if not self.multiplayer:
            self.word = random.choice(self.all_words[self.difficulty]).upper()
        # if multiplayer, word is set in ENTRY state
        self.guessed = []
        self.errors = 0
        self.max_errors = 10
        self.game_over = False
        self.win_status = False
        self.recalc_geometry()

    def recalc_geometry(self):
        self.sw, self.sh = self.win.get_size()

    def draw(self):
        self.win.fill(COLORS['DARK_BG'])
        if self.state == "MENU":
            self.draw_menu()
        elif self.state == "ENTRY":
            self.draw_entry()
        elif self.state == "ADD_WORD":
            self.draw_add_word()
        elif self.state == "GAME":
            self.draw_game()
        pygame.display.flip()

    def draw_menu(self):
        t = self.big_font.render("GALGENMÄNNCHEN", True, COLORS['GOLD'])
        self.win.blit(t, (self.sw//2 - t.get_width()//2, self.sh//6))
        
        bw, bh = 250, 45
        cx = self.sw//2 - bw//2
        cy = self.sh//2 - 100
        
        self.menu_buttons = [
            Button("Singleplayer", cx, cy, bw, bh, self.start_singleplayer),
            Button("Multiplayer (Lokal)", cx, cy + 60, bw, bh, self.to_entry),
            Button("Wort hinzufügen", cx, cy + 120, bw, bh, self.to_add_word),
            Button(f"Schwierigkeit: {self.difficulty}", cx, cy + 180, bw, bh, self.toggle_diff),
            Button("Vollbild Umschalten", cx, cy + 240, bw, bh, self.toggle_fs)
        ]
        
        for b in self.menu_buttons: b.draw(self.win, self.font)

    def draw_entry(self):
        t = self.big_font.render("GEHEIMES WORT EINGEBEN", True, COLORS['WHITE'])
        self.win.blit(t, (self.sw//2 - t.get_width()//2, self.sh//4))
        
        # Hidden typing
        display = "*" * len(self.input_text)
        txt = self.big_font.render(display, True, COLORS['GOLD'])
        pygame.draw.rect(self.win, COLORS['BLACK'], (self.sw//2-200, self.sh//2, 400, 60))
        self.win.blit(txt, (self.sw//2 - txt.get_width()//2, self.sh//2 + 5))
        
        hint = self.font.render("Drücke ENTER zum Starten oder ESC zum Abbrechen", True, COLORS['GREY'])
        self.win.blit(hint, (self.sw//2 - hint.get_width()//2, self.sh//2 + 80))

    def draw_add_word(self):
        t = self.big_font.render("NEUES WORT HINZUFÜGEN", True, COLORS['WHITE'])
        self.win.blit(t, (self.sw//2 - t.get_width()//2, self.sh//4))
        
        txt = self.big_font.render(self.input_text, True, COLORS['GOLD'])
        pygame.draw.rect(self.win, COLORS['BLACK'], (self.sw//2-200, self.sh//2, 400, 60))
        self.win.blit(txt, (self.sw//2 - txt.get_width()//2, self.sh//2 + 5))
        
        hint = self.font.render(f"Kategorie: {self.difficulty} | ENTER: Speichern | ESC: Abbruch", True, COLORS['GREY'])
        self.win.blit(hint, (self.sw//2 - hint.get_width()//2, self.sh//2 + 80))

    def draw_game(self):
        self.draw_hangman()
        
        display_word = ""
        for char in self.word:
            if char in self.guessed or char == " ":
                display_word += char + " "
            else:
                display_word += "_ "
        
        w_surf = self.big_font.render(display_word, True, COLORS['WHITE'])
        self.win.blit(w_surf, (self.sw//2 - w_surf.get_width()//2, self.sh * 0.6))
        
        self.draw_alphabet()
        
        self.back_btn = Button("Menü", 20, 20, 80, 35, self.to_menu)
        self.back_btn.draw(self.win, self.font)
        
        if self.game_over:
            ov = pygame.Surface((self.sw, self.sh), pygame.SRCALPHA)
            ov.fill((0,0,0,180))
            self.win.blit(ov, (0,0))
            
            if self.win_status:
                msg = "GEWONNEN!"
                col = COLORS['GREEN']
            else:
                msg = f"VERLOREN! Wort war: {self.word}"
                col = COLORS['RED']
                
            wt = self.big_font.render(msg, True, col)
            self.win.blit(wt, (self.sw//2-wt.get_width()//2, self.sh//2-50))
            self.rem_btn = Button("Nochmal spielen", self.sw//2-100, self.sh//2+50, 200, 50, self.reset_game)
            self.rem_btn.draw(self.win, self.font)

    def draw_hangman(self):
        cx, cy = self.sw * 0.3, self.sh * 0.3
        s = 100
        color = COLORS['WHITE']
        th = 5
        if self.errors >= 1: pygame.draw.line(self.win, color, (cx-s, cy+s), (cx+s, cy+s), th)
        if self.errors >= 2: pygame.draw.line(self.win, color, (cx-s//2, cy+s), (cx-s//2, cy-s), th)
        if self.errors >= 3: pygame.draw.line(self.win, color, (cx-s//2, cy-s), (cx+s//2, cy-s), th)
        if self.errors >= 4: pygame.draw.line(self.win, color, (cx+s//2, cy-s), (cx+s//2, cy-s//2), th)
        if self.errors >= 5: pygame.draw.circle(self.win, color, (int(cx+s//2), int(cy-s//2+20)), 20, th)
        if self.errors >= 6: pygame.draw.line(self.win, color, (cx+s//2, cy-s//2+40), (cx+s//2, cy+20), th)
        if self.errors >= 7: pygame.draw.line(self.win, color, (cx+s//2, cy-s//2+50), (cx+s//2-30, cy-s//2+80), th)
        if self.errors >= 8: pygame.draw.line(self.win, color, (cx+s//2, cy-s//2+50), (cx+s//2+30, cy-s//2+80), th)
        if self.errors >= 9: pygame.draw.line(self.win, color, (cx+s//2, cy+20), (cx+s//2-30, cy+70), th)
        if self.errors >= 10: pygame.draw.line(self.win, color, (cx+s//2, cy+20), (cx+s//2+30, cy+70), th)

    def draw_alphabet(self):
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜ"
        cols = 10
        start_x = (self.sw - (cols * 50)) // 2
        start_y = self.sh * 0.75
        self.letter_rects = []
        for i, char in enumerate(letters):
            x = start_x + (i % cols) * 50
            y = start_y + (i // cols) * 50
            rect = pygame.Rect(x, y, 40, 40)
            self.letter_rects.append((char, rect))
            color = COLORS['GREY']
            if char in self.guessed:
                color = COLORS['GREEN'] if char in self.word else COLORS['RED']
            pygame.draw.rect(self.win, color, rect, border_radius=5)
            t = self.letter_font.render(char, True, COLORS['WHITE'])
            self.win.blit(t, (x + 20 - t.get_width()//2, y + 20 - t.get_height()//2))

    def start_singleplayer(self):
        self.multiplayer = False
        self.state = "GAME"
        self.reset()

    def reset_game(self):
        if self.multiplayer: self.state = "ENTRY"; self.input_text = ""
        else: self.reset()

    def to_entry(self):
        self.state = "ENTRY"
        self.input_text = ""
        self.multiplayer = True

    def to_add_word(self):
        self.state = "ADD_WORD"
        self.input_text = ""

    def save_word(self):
        if self.input_text.strip():
            # Append to file
            with open(WORD_FILE, "a", encoding="utf-8") as f:
                f.write(f"\n{self.input_text.strip().upper()}")
            self.all_words = load_words() # Reload
        self.state = "MENU"

    def start_multi(self):
        if self.input_text.strip():
            self.word = self.input_text.strip().upper()
            self.state = "GAME"
            self.reset()

    def to_menu(self): self.state = "MENU"
    def toggle_fs(self):
        self.fullscreen = not self.fullscreen
        if self.fullscreen: self.win = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        else: self.win = pygame.display.set_mode((1000, 800), pygame.RESIZABLE)
        self.recalc_geometry()

    def toggle_diff(self):
        diffs = list(self.all_words.keys())
        idx = (diffs.index(self.difficulty) + 1) % len(diffs)
        self.difficulty = diffs[idx]

    def run(self):
        clock = pygame.time.Clock()
        while True:
            for e in pygame.event.get():
                if e.type == pygame.QUIT: pygame.quit(); sys.exit()
                if e.type == pygame.VIDEORESIZE and not self.fullscreen: self.recalc_geometry()
                if e.type == pygame.MOUSEBUTTONDOWN:
                    if self.state == "MENU":
                        for b in self.menu_buttons: b.click(e.pos) and b.func()
                    elif self.state == "GAME":
                        if self.back_btn.click(e.pos): self.to_menu()
                        elif self.game_over:
                            if self.rem_btn.click(e.pos): self.reset_game()
                        else:
                            for char, rect in self.letter_rects:
                                if rect.collidepoint(e.pos) and char not in self.guessed:
                                    self.handle_guess(char)
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE: 
                        if self.state == "MENU": pygame.quit(); sys.exit()
                        else: self.state = "MENU"
                    elif self.state == "ENTRY":
                        if e.key == pygame.K_RETURN: self.start_multi()
                        elif e.key == pygame.K_BACKSPACE: self.input_text = self.input_text[:-1]
                        else: self.input_text += e.unicode.upper()
                    elif self.state == "ADD_WORD":
                        if e.key == pygame.K_RETURN: self.save_word()
                        elif e.key == pygame.K_BACKSPACE: self.input_text = self.input_text[:-1]
                        else: self.input_text += e.unicode.upper()
                    elif self.state == "GAME" and not self.game_over:
                        key_char = e.unicode.upper()
                        if key_char in "ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜ" and key_char != "":
                            if key_char not in self.guessed:
                                self.handle_guess(key_char)

            self.draw()
            clock.tick(30)

    def handle_guess(self, char):
        self.guessed.append(char)
        if char not in self.word:
            self.errors += 1
            self.sounds.play('error')
        else:
            self.sounds.play('move')
        self.check_status()

    def check_status(self):
        win = True
        for char in self.word:
            if char != " " and char not in self.guessed:
                win = False
                break
        if win:
            self.game_over = True
            self.win_status = True
            self.sounds.play('win')
        if self.errors >= self.max_errors:
            self.game_over = True
            self.win_status = False
            self.sounds.play('lose')

if __name__ == "__main__":
    HangmanGame().run()