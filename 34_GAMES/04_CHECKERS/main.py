import pygame
import sys

# Farben
RED_COLOR = (255, 0, 0)
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
GREY_COLOR = (128, 128, 128)
BLUE_COLOR = (0, 0, 255)
DARK_RED_COLOR = (150, 0, 0)
GOLD_COLOR = (255, 215, 0)

# Spielfeld
ROWS, COLS = 8, 8

class Piece:
    PADDING = 15
    OUTLINE = 2

    def __init__(self, row, col, color, square_size):
        self.row = row
        self.col = col
        self.color = color
        self.square_size = square_size
        self.king = False
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = self.square_size * self.col + self.square_size // 2
        self.y = self.square_size * self.row + self.square_size // 2

    def make_king(self):
        self.king = True

    def draw(self, win):
        radius = self.square_size // 2 - self.PADDING
        pygame.draw.circle(win, GREY_COLOR, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        if self.king:
            font = pygame.font.SysFont("arial", int(self.square_size * 0.4), bold=True)
            text = font.render("K", True, GOLD_COLOR)
            win.blit(text, (self.x - text.get_width()//2, self.y - text.get_height()//2))

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

class Board:
    def __init__(self, square_size, offset_x, offset_y):
        self.board = []
        self.square_size = square_size
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.red_left = self.white_left = 12
        self.red_kings = self.white_kings = 0
        self.create_board()

    def draw_squares(self, win, screen_width, screen_height):
        win.fill(BLACK_COLOR)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, (40, 40, 40), (self.offset_x + row * self.square_size, self.offset_y + col * self.square_size, self.square_size, self.square_size))
            for col in range((row + 1) % 2, COLS, 2):
                pygame.draw.rect(win, (80, 80, 80), (self.offset_x + row * self.square_size, self.offset_y + col * self.square_size, self.square_size, self.square_size))

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, WHITE_COLOR, self.square_size))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, DARK_RED_COLOR, self.square_size))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw(self, win, screen_width, screen_height):
        self.draw_squares(win, screen_width, screen_height)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    # Adjust piece position for drawing
                    original_x, original_y = piece.x, piece.y
                    piece.x += self.offset_x
                    piece.y += self.offset_y
                    piece.draw(win)
                    piece.x, piece.y = original_x, original_y

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

        if row == ROWS - 1 and piece.color == WHITE_COLOR:
            piece.make_king()
            self.white_kings += 1
        if row == 0 and piece.color == DARK_RED_COLOR:
            piece.make_king()
            self.red_kings += 1

    def get_piece(self, row, col):
        return self.board[row][col]

    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece.color == DARK_RED_COLOR:
                self.red_left -= 1
            else:
                self.white_left -= 1

    def winner(self):
        if self.red_left <= 0: return "Weiß gewinnt!"
        if self.white_left <= 0: return "Rot gewinnt!"
        return None

    def get_valid_moves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        if piece.color == DARK_RED_COLOR or piece.king:
            moves.update(self._traverse_left(row - 1, max(row - 3, -1), -1, piece.color, left))
            moves.update(self._traverse_right(row - 1, max(row - 3, -1), -1, piece.color, right))
        if piece.color == WHITE_COLOR or piece.king:
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

class Game:
    def __init__(self, win, square_size, offset_x, offset_y):
        self.win = win
        self.square_size = square_size
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.selected = None
        self.board = Board(square_size, offset_x, offset_y)
        self.turn = DARK_RED_COLOR
        self.valid_moves = {}

    def update(self, screen_width, screen_height):
        self.board.draw(self.win, screen_width, screen_height)
        self.draw_valid_moves(self.valid_moves)
        
        # Turn indicator
        font = pygame.font.SysFont("arial", 30)
        txt = "Roter Spieler ist dran" if self.turn == DARK_RED_COLOR else "Weißer Spieler ist dran"
        color = DARK_RED_COLOR if self.turn == DARK_RED_COLOR else WHITE_COLOR
        label = font.render(txt, True, color)
        self.win.blit(label, (screen_width // 2 - label.get_width() // 2, 20))
        
        winner = self.board.winner()
        if winner:
            over_font = pygame.font.SysFont("arial", 60, bold=True)
            over_label = over_font.render(winner, True, GOLD_COLOR)
            self.win.blit(over_label, (screen_width // 2 - over_label.get_width() // 2, screen_height // 2))

        pygame.display.update()

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
            return True
        return False

    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False
        return True

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, BLUE_COLOR, (self.offset_x + col * self.square_size + self.square_size // 2, self.offset_y + row * self.square_size + self.square_size // 2), 15)

    def change_turn(self):
        self.valid_moves = {}
        self.turn = WHITE_COLOR if self.turn == DARK_RED_COLOR else DARK_RED_COLOR

def main():
    pygame.init()
    info = pygame.display.Info()
    SW, SH = info.current_w, info.current_h
    win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption('Dame - Vollbild')
    
    square_size = min(SW, SH) // 10
    offset_x = (SW - square_size * COLS) // 2
    offset_y = (SH - square_size * ROWS) // 2
    
    clock = pygame.time.Clock()
    game = Game(win, square_size, offset_x, offset_y)

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_r:
                    game = Game(win, square_size, offset_x, offset_y)
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row = (pos[1] - offset_y) // square_size
                col = (pos[0] - offset_x) // square_size
                if 0 <= row < ROWS and 0 <= col < COLS:
                    game.select(row, col)
        game.update(SW, SH)

if __name__ == "__main__":
    main()