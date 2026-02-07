import pygame
import random
import sys

# Farben
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 50, 50)
GREEN = (50, 255, 50)
BLUE = (50, 50, 255)
YELLOW = (255, 255, 50)
GRAY = (180, 180, 180)
DARK_GRAY = (50, 50, 50)

PLAYER_COLORS = [RED, BLUE, YELLOW, GREEN]
PLAYER_NAMES = ["Rot", "Blau", "Gelb", "Grün"]

class LudoGame:
    def __init__(self, win, sw, sh):
        self.win = win
        self.sw = sw
        self.sh = sh
        
        # Grid Size calculation
        self.grid_size = min(sw, sh) // 13
        self.offset_x = (sw - self.grid_size * 11) // 2
        self.offset_y = (sh - self.grid_size * 11) // 2
        
        self.turn = 0
        self.dice_value = 0
        self.waiting_for_dice = True
        self.waiting_for_move = False
        self.pieces = [[-1, -1, -1, -1] for _ in range(4)]
        self.message = "Rot ist am Zug. Klicke zum Würfeln."
        
        self.path_coords = self.generate_path_coords()
        self.base_coords = self.generate_base_coords()
        self.target_coords = self.generate_target_coords()

    def generate_path_coords(self):
        coords = []
        # Top arm down (right side)
        for y in range(4, -1, -1): coords.append((6, y))
        coords.append((5, 0)) # top mid
        for y in range(0, 5): coords.append((4, y)) # top arm up (left side)
        # Left arm left
        for x in range(3, -1, -1): coords.append((x, 4))
        coords.append((0, 5)) # left mid
        for x in range(0, 4): coords.append((x, 6))
        # Bottom arm down
        for y in range(7, 11): coords.append((4, y))
        coords.append((5, 10)) # bottom mid
        for y in range(10, 6, -1): coords.append((6, y))
        # Right arm right
        for x in range(7, 11): coords.append((x, 6))
        coords.append((10, 5)) # right mid
        for x in range(10, 6, -1): coords.append((x, 4))
        return coords

    def generate_base_coords(self):
        return [
            [(0,0), (1,0), (0,1), (1,1)], # Red (Top Left)
            [(9,0), (10,0), (9,1), (10,1)], # Blue (Top Right)
            [(9,9), (10,9), (9,10), (10,10)], # Yellow (Bottom Right)
            [(0,9), (1,9), (0,10), (1,10)]  # Green (Bottom Left)
        ]
    
    def generate_target_coords(self):
        return [
            [(5, 1), (5, 2), (5, 3), (5, 4)], # Red
            [(9, 5), (8, 5), (7, 5), (6, 5)], # Blue
            [(5, 9), (5, 8), (5, 7), (5, 6)], # Yellow
            [(1, 5), (2, 5), (3, 5), (4, 5)]  # Green
        ]

    def draw(self):
        self.win.fill((30, 30, 30))
        
        # Draw path
        for i, (x, y) in enumerate(self.path_coords):
            color = GRAY
            if i == 0: color = RED
            if i == 10: color = BLUE
            if i == 20: color = YELLOW
            if i == 30: color = GREEN
            rect = (self.offset_x + x*self.grid_size, self.offset_y + y*self.grid_size, self.grid_size-2, self.grid_size-2)
            pygame.draw.rect(self.win, color, rect, border_radius=5)
            
        # Draw bases and targets
        for p in range(4):
            for x, y in self.base_coords[p]:
                rect = (self.offset_x + x*self.grid_size, self.offset_y + y*self.grid_size, self.grid_size-2, self.grid_size-2)
                pygame.draw.rect(self.win, PLAYER_COLORS[p], rect, 2, border_radius=5)
            for x, y in self.target_coords[p]:
                rect = (self.offset_x + x*self.grid_size, self.offset_y + y*self.grid_size, self.grid_size-2, self.grid_size-2)
                pygame.draw.rect(self.win, PLAYER_COLORS[p], rect, 1, border_radius=5)

        # Draw pieces
        for p in range(4):
            for i, pos in enumerate(self.pieces[p]):
                if pos == -100: continue # Finished
                if pos == -1: x, y = self.base_coords[p][i]
                elif pos >= 40: x, y = self.target_coords[p][pos-40]
                else: x, y = self.path_coords[pos]
                
                center = (self.offset_x + x*self.grid_size + self.grid_size//2, self.offset_y + y*self.grid_size + self.grid_size//2)
                pygame.draw.circle(self.win, PLAYER_COLORS[p], center, self.grid_size//2 - 5)
                pygame.draw.circle(self.win, WHITE, center, self.grid_size//2 - 5, 2)

        # UI
        font = pygame.font.SysFont("arial", 36, bold=True)
        txt = font.render(self.message, True, WHITE)
        self.win.blit(txt, (self.sw // 2 - txt.get_width() // 2, self.sh - 80))
        
        if self.dice_value > 0:
            dice_font = pygame.font.SysFont("arial", 60, bold=True)
            dice_txt = dice_font.render(str(self.dice_value), True, PLAYER_COLORS[self.turn])
            self.win.blit(dice_txt, (self.sw - 150, self.sh // 2))

        pygame.display.update()

    def roll_dice(self):
        self.dice_value = random.randint(1, 6)
        can_move = False
        start_idx = [0, 10, 20, 30][self.turn]
        
        for i, pos in enumerate(self.pieces[self.turn]):
            if pos == -100: continue
            if pos == -1:
                if self.dice_value == 6: can_move = True
            elif pos < 40:
                can_move = True
            elif pos < 44:
                if pos + self.dice_value <= 43: can_move = True
                elif pos + self.dice_value == 44: can_move = True # Finish
        
        if not can_move:
            self.message = f"Kein Zug möglich. {PLAYER_NAMES[(self.turn+1)%4]} ist dran."
            pygame.time.wait(1000)
            self.turn = (self.turn + 1) % 4
            self.dice_value = 0
            self.waiting_for_dice = True
        else:
            self.message = f"Gewürfelt: {self.dice_value}. Wähle eine Figur."
            self.waiting_for_dice = False
            self.waiting_for_move = True

    def move_piece(self, piece_idx):
        pos = self.pieces[self.turn][piece_idx]
        start_idx = [0, 10, 20, 30][self.turn]
        
        if pos == -1:
            if self.dice_value == 6:
                self.pieces[self.turn][piece_idx] = start_idx
                self.check_kickout(start_idx)
            else: return
        elif pos < 40:
            dist_from_start = (pos - start_idx) % 40
            if dist_from_start + self.dice_value >= 40:
                new_pos = 40 + (dist_from_start + self.dice_value - 40)
                if new_pos <= 43: self.pieces[self.turn][piece_idx] = new_pos
                elif new_pos == 44: self.pieces[self.turn][piece_idx] = -100
                else: return
            else:
                new_pos = (pos + self.dice_value) % 40
                self.pieces[self.turn][piece_idx] = new_pos
                self.check_kickout(new_pos)
        elif pos < 44:
            new_pos = pos + self.dice_value
            if new_pos <= 43: self.pieces[self.turn][piece_idx] = new_pos
            elif new_pos == 44: self.pieces[self.turn][piece_idx] = -100
            else: return
            
        if self.dice_value != 6:
            self.turn = (self.turn + 1) % 4
        
        self.dice_value = 0
        self.waiting_for_move = False
        self.waiting_for_dice = True
        self.message = f"{PLAYER_NAMES[self.turn]} ist am Zug. Klicke zum Würfeln."
        
        if all(p == -100 for p in self.pieces[self.turn-1 if self.turn > 0 else 3]):
             self.message = f"{PLAYER_NAMES[self.turn-1 if self.turn > 0 else 3]} GEWINNT!"

    def check_kickout(self, path_pos):
        # Safe spots (start positions)
        if path_pos in [0, 10, 20, 30]: return
        for p in range(4):
            if p == self.turn: continue
            for i, pos in enumerate(self.pieces[p]):
                if pos == path_pos:
                    self.pieces[p][i] = -1

    def handle_click(self, pos):
        if self.waiting_for_dice:
            self.roll_dice()
        elif self.waiting_for_move:
            for i in range(4):
                curr_pos = self.pieces[self.turn][i]
                if curr_pos == -100: continue
                if curr_pos == -1: x, y = self.base_coords[self.turn][i]
                elif curr_pos >= 40: x, y = self.target_coords[self.turn][curr_pos-40]
                else: x, y = self.path_coords[curr_pos]
                
                rect = pygame.Rect(self.offset_x + x*self.grid_size, self.offset_y + y*self.grid_size, self.grid_size, self.grid_size)
                if rect.collidepoint(pos):
                    self.move_piece(i)
                    break

def main():
    pygame.init()
    info = pygame.display.Info()
    SW, SH = info.current_w, info.current_h
    win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Mensch ärgere dich nicht - Vollbild")
    clock = pygame.time.Clock()
    game = LudoGame(win, SW, SH)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_r:
                    game = LudoGame(win, SW, SH)
            if event.type == pygame.MOUSEBUTTONDOWN:
                game.handle_click(event.pos)
        
        game.draw()
        clock.tick(60)

if __name__ == "__main__":
    main()