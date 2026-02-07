import pygame
import sys
import math

# Farben
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

# Board Konfiguration
ROWS = 6
COLS = 7

class ConnectFour:
    def __init__(self):
        pygame.init()
        
        # Monitor Auflösung holen für Vollbild
        info = pygame.display.Info()
        self.screen_width = info.current_w
        self.screen_height = info.current_h
        
        # Vollbild-Modus
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("Vier Gewinnt - Vollbild")
        
        # Dynamische Berechnung der Größe
        self.square_size = min(self.screen_width // COLS, (self.screen_height - 100) // (ROWS + 1))
        self.width = COLS * self.square_size
        self.height = (ROWS + 1) * self.square_size
        self.radius = int(self.square_size / 2 - 5)
        
        # Zentrierung des Spielfelds
        self.offset_x = (self.screen_width - self.width) // 2
        self.offset_y = (self.screen_height - self.height) // 2
        
        self.board = self.create_board()
        self.game_over = False
        self.turn = 0 # 0 für Rot, 1 für Gelb
        self.font = pygame.font.SysFont("arial", 48, bold=True)
        self.small_font = pygame.font.SysFont("arial", 24)

    def create_board(self):
        return [[0 for _ in range(COLS)] for _ in range(ROWS)]

    def drop_piece(self, row, col, piece):
        self.board[row][col] = piece

    def is_valid_location(self, col):
        return self.board[ROWS-1][col] == 0

    def get_next_open_row(self, col):
        for r in range(ROWS):
            if self.board[r][col] == 0:
                return r

    def winning_move(self, piece):
        # Horizontal
        for c in range(COLS - 3):
            for r in range(ROWS):
                if self.board[r][c] == piece and self.board[r][c+1] == piece and self.board[r][c+2] == piece and self.board[r][c+3] == piece:
                    return True
        # Vertikal
        for c in range(COLS):
            for r in range(ROWS - 3):
                if self.board[r][c] == piece and self.board[r+1][c] == piece and self.board[r+2][c] == piece and self.board[r+3][c] == piece:
                    return True
        # Diagonale (positiv)
        for c in range(COLS - 3):
            for r in range(ROWS - 3):
                if self.board[r][c] == piece and self.board[r+1][c+1] == piece and self.board[r+2][c+2] == piece and self.board[r+3][c+3] == piece:
                    return True
        # Diagonale (negativ)
        for c in range(COLS - 3):
            for r in range(3, ROWS):
                if self.board[r][c] == piece and self.board[r-1][c+1] == piece and self.board[r-2][c+2] == piece and self.board[r-3][c+3] == piece:
                    return True
        return False

    def draw_board(self, mouse_pos=None):
        self.screen.fill(BLACK)
        
        # Hintergrund für das Board
        pygame.draw.rect(self.screen, BLUE, (self.offset_x, self.offset_y + self.square_size, self.width, self.height - self.square_size), border_radius=15)

        for c in range(COLS):
            for r in range(ROWS):
                # Löcher im Board
                color = BLACK
                if self.board[r][c] == 1:
                    color = RED
                elif self.board[r][c] == 2:
                    color = YELLOW
                
                pos_x = self.offset_x + int(c * self.square_size + self.square_size / 2)
                pos_y = self.offset_y + self.height - int(r * self.square_size + self.square_size / 2)
                pygame.draw.circle(self.screen, color, (pos_x, pos_y), self.radius)

        # Vorschau-Stein
        if not self.game_over and mouse_pos:
            posx = mouse_pos[0]
            if self.offset_x < posx < self.offset_x + self.width:
                color = RED if self.turn == 0 else YELLOW
                pygame.draw.circle(self.screen, color, (posx, self.offset_y + int(self.square_size / 2)), self.radius)

        # Text-Anzeige
        if self.game_over:
            winner = "Spieler 1 (Rot)" if self.turn == 1 else "Spieler 2 (Gelb)" # Turn wurde schon gewechselt
            msg = f"{winner} gewinnt!"
            color = RED if self.turn == 1 else YELLOW
            label = self.font.render(msg, True, color)
            self.screen.blit(label, (self.screen_width // 2 - label.get_width() // 2, 20))
            
            hint = self.small_font.render("Drücke 'R' für Neustart oder 'ESC' zum Beenden", True, WHITE)
            self.screen.blit(hint, (self.screen_width // 2 - hint.get_width() // 2, self.screen_height - 50))
        else:
            msg = f"Spieler {'1' if self.turn == 0 else '2'} ist dran"
            color = RED if self.turn == 0 else YELLOW
            label = self.font.render(msg, True, color)
            self.screen.blit(label, (self.screen_width // 2 - label.get_width() // 2, 20))

        pygame.display.update()

    def run(self):
        clock = pygame.time.Clock()
        while True:
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_r:
                        self.__init__() # Neustart

                if event.type == pygame.MOUSEBUTTONDOWN and not self.game_over:
                    posx = event.pos[0]
                    if self.offset_x < posx < self.offset_x + self.width:
                        col = int((posx - self.offset_x) // self.square_size)

                        if self.is_valid_location(col):
                            row = self.get_next_open_row(col)
                            self.drop_piece(row, col, self.turn + 1)

                            if self.winning_move(self.turn + 1):
                                self.game_over = True

                            self.turn = (self.turn + 1) % 2

            self.draw_board(mouse_pos)
            clock.tick(60)

if __name__ == "__main__":
    game = ConnectFour()
    game.run()