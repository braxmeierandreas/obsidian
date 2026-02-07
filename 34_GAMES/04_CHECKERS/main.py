import pygame
import sys
import copy
import random
import os

# Add shared folder to path
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'SHARED'))
from sound_manager import SoundManager

# --- CONFIGURATION & CONSTANTS ---
ROWS, COLS = 8, 8
DEFAULT_WIDTH, DEFAULT_HEIGHT = 800, 800

# Colors
RED = (200, 50, 50)
WHITE = (230, 230, 230)
BLACK = (20, 20, 20)
BLUE = (50, 50, 200)
GREY = (128, 128, 128)
GOLD = (255, 215, 0)
GREEN = (50, 200, 50)
DARK_BG = (40, 44, 52)

# --- CLASSES ---

class Piece:
    PADDING = 15
    OUTLINE = 3

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0

    def calc_pos(self, square_size, offset_x, offset_y):
        self.x = offset_x + self.col * square_size + square_size // 2
        self.y = offset_y + self.row * square_size + square_size // 2

    def make_king(self):
        self.king = True

    def draw(self, win, square_size):
        radius = square_size // 2 - self.PADDING
        pygame.draw.circle(win, (50, 50, 50), (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        if self.king:
            font = pygame.font.SysFont("arial", int(square_size * 0.4), bold=True)
            text = font.render("K", True, GOLD)
            win.blit(text, (self.x - text.get_width()//2, self.y - text.get_height()//2))

    def move(self, row, col):
        self.row = row
        self.col = col

class Board:
    def __init__(self):
        self.board = []
        self.red_left = self.white_left = 12
        self.red_kings = self.white_kings = 0
        self.create_board()

    def create_board(self):
        self.board = []
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, WHITE))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, RED))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw(self, win, square_size, offset_x, offset_y, p1_color, p2_color):
        # Update colors based on settings
        current_red = p1_color
        current_white = p2_color
        
        # Draw squares
        win.fill(DARK_BG)
        board_rect = (offset_x, offset_y, square_size*COLS, square_size*ROWS)
        pygame.draw.rect(win, BLACK, board_rect, 5) # Border
        
        for row in range(ROWS):
            for col in range(COLS):
                rect = (offset_x + col*square_size, offset_y + row*square_size, square_size, square_size)
                if col % 2 == ((row + 1) % 2):
                    pygame.draw.rect(win, (80, 80, 80), rect)
                else:
                    pygame.draw.rect(win, (40, 40, 40), rect)
        
        # Draw pieces
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    # Update piece color dynamically for display
                    draw_color = current_white if piece.color == WHITE else current_red
                    piece.color = draw_color # Hacky but works for display update
                    piece.calc_pos(square_size, offset_x, offset_y)
                    piece.draw(win, square_size)
                    # Restore logical color for logic checks (optional, but safer to keep consistency)
                    if draw_color != piece.color:
                        piece.color = WHITE if piece.color == current_white else RED

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)
        
        # Promotion
        if row == ROWS - 1 and piece.color == WHITE:
            piece.make_king()
            self.white_kings += 1
        if row == 0 and piece.color == RED:
            piece.make_king()
            self.red_kings += 1

    def get_piece(self, row, col):
        return self.board[row][col]

    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece.color == RED:
                self.red_left -= 1
            else:
                self.white_left -= 1

    def winner(self):
        if self.red_left <= 0: return WHITE
        if self.white_left <= 0: return RED
        return None

    def get_valid_moves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row
        
        # Determine direction based on color identity (RED is usually bottom, moves UP)
        # Note: In my logic RED moves UP (-1), WHITE moves DOWN (+1)
        
        if piece.color == RED or piece.king:
            moves.update(self._traverse_left(row - 1, max(row - 3, -1), -1, piece.color, left))
            moves.update(self._traverse_right(row - 1, max(row - 3, -1), -1, piece.color, right))
        if piece.color == WHITE or piece.king:
            moves.update(self._traverse_left(row + 1, min(row + 3, ROWS), 1, piece.color, left))
            moves.update(self._traverse_right(row + 1, min(row + 3, ROWS), 1, piece.color, right))
        return moves

    def _traverse_left(self, start, stop, step, color, left, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0: break
            current = self.board[r][left]
            if current == 0:
                if skipped and not last: break
                elif skipped: moves[(r, left)] = last + skipped
                else: moves[(r, left)] = last
                if last:
                    if step == -1: row = max(r - 3, -1)
                    else: row = min(r + 3, ROWS)
                    moves.update(self._traverse_left(r + step, row, step, color, left - 1, skipped=last))
                    moves.update(self._traverse_right(r + step, row, step, color, left + 1, skipped=last))
                break
            elif current.color == color: break
            else: last = [current]
            left -= 1
        return moves

    def _traverse_right(self, start, stop, step, color, right, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLS: break
            current = self.board[r][right]
            if current == 0:
                if skipped and not last: break
                elif skipped: moves[(r, right)] = last + skipped
                else: moves[(r, right)] = last
                if last:
                    if step == -1: row = max(r - 3, -1)
                    else: row = min(r + 3, ROWS)
                    moves.update(self._traverse_left(r + step, row, step, color, right - 1, skipped=last))
                    moves.update(self._traverse_right(r + step, row, step, color, right + 1, skipped=last))
                break
            elif current.color == color: break
            else: last = [current]
            right += 1
        return moves
        
    def evaluate(self):
        # AI Heuristic
        return self.white_left - self.red_left + (self.white_kings * 0.5 - self.red_kings * 0.5)

    def get_all_moves(self, color):
        moves = []
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0 and piece.color == color:
                    valid_moves = self.get_valid_moves(piece)
                    for move, skip in valid_moves.items():
                        # Create a temp board state (simulated)
                        temp_board = copy.deepcopy(self)
                        temp_piece = temp_board.get_piece(row, col)
                        new_board = temp_board.simulate_move(temp_piece, move, skip)
                        moves.append(new_board)
        return moves

    def simulate_move(self, piece, move, skip):
        self.move(piece, move[0], move[1])
        if skip:
            self.remove(skip)
        return self

# --- AI ---

class AI:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.depth_map = {0: 1, 1: 2, 2: 4, 3: 5} # Easy, Medium, Hard, "Unbeatable"
        
    def minimax(self, position, depth, max_player, game):
        if depth == 0 or position.winner() != None:
            return position.evaluate(), position
        
        if max_player: # WHITE (AI)
            max_eval = float('-inf')
            best_move = None
            for move in position.get_all_moves(WHITE):
                evaluation = self.minimax(move, depth-1, False, game)[0]
                max_eval = max(max_eval, evaluation)
                if max_eval == evaluation:
                    best_move = move
            return max_eval, best_move
        else: # RED (Player)
            min_eval = float('inf')
            best_move = None
            for move in position.get_all_moves(RED):
                evaluation = self.minimax(move, depth-1, True, game)[0]
                min_eval = min(min_eval, evaluation)
                if min_eval == evaluation:
                    best_move = move
            return min_eval, best_move

    def get_move(self, board, game):
        depth = self.depth_map.get(self.difficulty, 2)
        value, new_board = self.minimax(board, depth, True, game)
        return new_board

# --- MENU & UI ---

class Button:
    def __init__(self, text, x, y, w, h, func, param=None):
        self.text = text
        self.rect = pygame.Rect(x, y, w, h)
        self.func = func
        self.param = param
        self.color = (60, 60, 60)
        self.hover_color = (100, 100, 100)
        
    def draw(self, win, font):
        mouse_pos = pygame.mouse.get_pos()
        color = self.hover_color if self.rect.collidepoint(mouse_pos) else self.color
        pygame.draw.rect(win, color, self.rect, border_radius=10)
        pygame.draw.rect(win, WHITE, self.rect, 2, border_radius=10)
        
        txt_surf = font.render(self.text, True, WHITE)
        win.blit(txt_surf, (self.rect.centerx - txt_surf.get_width()//2, self.rect.centery - txt_surf.get_height()//2))
        
    def check_click(self, pos, sounds):
        if self.rect.collidepoint(pos):
            sounds.play('select')
            if self.param is not None:
                self.func(self.param)
            else:
                self.func()
            return True
        return False

class Game:
    def __init__(self):
        pygame.init()
        self.info = pygame.display.Info()
        self.w, self.h = self.info.current_w, self.info.current_h
        self.win = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        pygame.display.set_caption("Checkers Ultimate")
        
        self.sounds = SoundManager()
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("arial", 24)
        self.title_font = pygame.font.SysFont("arial", 60, bold=True)
        
        # State
        self.state = "MENU" # MENU, GAME, SETTINGS, GAMEOVER
        self.p1_color = RED
        self.p2_color = WHITE
        self.difficulty = 1 # 0=Easy, 1=Med, 2=Hard, 3=God
        self.fullscreen = True
        self.vs_ai = True
        
        self.reset_game()
        self.create_menu()

    def reset_game(self):
        self.board = Board()
        self.turn = RED
        self.valid_moves = {}
        self.selected = None
        self.ai = AI(self.difficulty)
        
        # Board geometry
        self.sq_size = min(self.w, self.h) // 10
        self.offset_x = (self.w - self.sq_size*COLS) // 2
        self.offset_y = (self.h - self.sq_size*ROWS) // 2

    def create_menu(self):
        cx, cy = self.w // 2, self.h // 2
        bw, bh = 300, 60
        self.menu_buttons = [
            Button("Spielen (vs AI)", cx - bw//2, cy - 100, bw, bh, self.start_game, True),
            Button("Spielen (2 Spieler)", cx - bw//2, cy - 20, bw, bh, self.start_game, False),
            Button("Einstellungen", cx - bw//2, cy + 60, bw, bh, self.set_state, "SETTINGS"),
            Button("Beenden", cx - bw//2, cy + 140, bw, bh, self.quit_game)
        ]
        
        self.settings_buttons = [
            Button("Schwierigkeit: Mittel", cx - bw//2, cy - 100, bw, bh, self.toggle_diff),
            Button("Farbe P1: Rot", cx - bw//2, cy - 20, bw, bh, self.toggle_color),
            Button("Ton: An", cx - bw//2, cy + 60, bw, bh, self.toggle_sound),
            Button("Zurück", cx - bw//2, cy + 140, bw, bh, self.set_state, "MENU")
        ]
        
        self.game_ui_buttons = [
             Button("Menü", 20, 20, 100, 40, self.set_state, "MENU"),
             Button("Reset", 130, 20, 100, 40, self.reset_game)
        ]

    def set_state(self, state):
        self.state = state

    def start_game(self, vs_ai):
        self.vs_ai = vs_ai
        self.reset_game()
        self.state = "GAME"

    def quit_game(self):
        pygame.quit()
        sys.exit()

    def toggle_diff(self):
        self.difficulty = (self.difficulty + 1) % 4
        labels = ["Einfach", "Mittel", "Schwer", "Unbesiegbar"]
        self.settings_buttons[0].text = f"Schwierigkeit: {labels[self.difficulty]}"

    def toggle_color(self):
        # Cycle RED -> BLUE -> GREEN -> RED
        if self.p1_color == RED: 
            self.p1_color = BLUE
            self.settings_buttons[1].text = "Farbe P1: Blau"
        elif self.p1_color == BLUE: 
            self.p1_color = GREEN
            self.settings_buttons[1].text = "Farbe P1: Grün"
        else: 
            self.p1_color = RED
            self.settings_buttons[1].text = "Farbe P1: Rot"

    def toggle_sound(self):
        self.sounds.toggle()
        txt = "An" if self.sounds.enabled else "Aus"
        self.settings_buttons[2].text = f"Ton: {txt}"

    def run(self):
        while True:
            self.clock.tick(60)
            self.events()
            self.draw()
            
            # AI Move
            if self.state == "GAME" and self.turn == WHITE and self.vs_ai:
                pygame.display.update() # Force redraw before thinking
                # Simple delay for feel
                pygame.time.wait(500)
                new_board = self.ai.get_move(self.board, self)
                if new_board:
                    self.board = new_board
                    self.sounds.play('move')
                    self.change_turn()
                else:
                    print("AI cannot move!")

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.state == "MENU":
                    for b in self.menu_buttons: b.check_click(event.pos, self.sounds)
                elif self.state == "SETTINGS":
                    for b in self.settings_buttons: b.check_click(event.pos, self.sounds)
                elif self.state == "GAME":
                    # UI Buttons
                    for b in self.game_ui_buttons: b.check_click(event.pos, self.sounds)
                    
                    # Game Click
                    if self.turn == RED or not self.vs_ai:
                        row = (event.pos[1] - self.offset_y) // self.sq_size
                        col = (event.pos[0] - self.offset_x) // self.sq_size
                        if 0 <= row < ROWS and 0 <= col < COLS:
                            self.select(row, col)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if self.state == "GAME": self.state = "MENU"
                    else: self.quit_game()

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        
        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            self.sounds.play('select')
            return True
        return False

    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            self.sounds.play('move')
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
                self.sounds.play('capture')
            self.change_turn()
        else:
            return False
        return True

    def change_turn(self):
        self.valid_moves = {}
        if self.turn == RED:
            self.turn = WHITE
        else:
            self.turn = RED
            
        winner = self.board.winner()
        if winner:
            self.sounds.play('win')
            print("WINNER")

    def draw(self):
        self.win.fill(DARK_BG)
        
        if self.state == "MENU":
            title = self.title_font.render("DAME ULTIMATE", True, GOLD)
            self.win.blit(title, (self.w//2 - title.get_width()//2, 100))
            for b in self.menu_buttons: b.draw(self.win, self.font)
            
        elif self.state == "SETTINGS":
            title = self.title_font.render("EINSTELLUNGEN", True, WHITE)
            self.win.blit(title, (self.w//2 - title.get_width()//2, 100))
            for b in self.settings_buttons: b.draw(self.win, self.font)
            
        elif self.state == "GAME":
            self.board.draw(self.win, self.sq_size, self.offset_x, self.offset_y, self.p1_color, self.p2_color)
            self.draw_valid_moves(self.valid_moves)
            for b in self.game_ui_buttons: b.draw(self.win, self.font)
            
            # Info
            diff_txt = ["Einfach", "Mittel", "Schwer", "Unbesiegbar"][self.difficulty]
            info = self.font.render(f"Modus: {'vs AI' if self.vs_ai else 'PvP'} | Diff: {diff_txt}", True, GREY)
            self.win.blit(info, (self.w - info.get_width() - 20, 20))
            
            turn_txt = "Dein Zug (Rot)" if self.turn == RED else "Gegner Zug (Weiß)"
            col = self.p1_color if self.turn == RED else self.p2_color
            turn_lbl = self.font.render(turn_txt, True, col)
            self.win.blit(turn_lbl, (self.w//2 - turn_lbl.get_width()//2, 50))

            winner = self.board.winner()
            if winner:
                txt = "ROT GEWINNT" if winner == RED else "WEISS GEWINNT"
                overlay = pygame.Surface((self.w, self.h))
                overlay.set_alpha(200)
                overlay.fill(BLACK)
                self.win.blit(overlay, (0,0))
                lbl = self.title_font.render(txt, True, GOLD)
                self.win.blit(lbl, (self.w//2 - lbl.get_width()//2, self.h//2))
                
                # Rematch btn hint
                hint = self.font.render("Drücke RESET für Rematch", True, WHITE)
                self.win.blit(hint, (self.w//2 - hint.get_width()//2, self.h//2 + 100))

        pygame.display.flip()

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            cx = self.offset_x + col * self.sq_size + self.sq_size // 2
            cy = self.offset_y + row * self.sq_size + self.sq_size // 2
            pygame.draw.circle(self.win, BLUE, (cx, cy), 15)

if __name__ == "__main__":
    game = Game()
    game.run()
