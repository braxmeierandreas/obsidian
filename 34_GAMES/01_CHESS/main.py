import pygame
import chess
import sys

# Farben
COLOR_LIGHT = (232, 235, 239)
COLOR_DARK = (125, 135, 150)
COLOR_HIGHLIGHT = (186, 202, 68)
COLOR_MOVES = (214, 214, 105)
COLOR_CHECK = (255, 100, 100)
WHITE_PIECE = (255, 255, 255)
BLACK_PIECE = (0, 0, 0)

class ChessGame:
    def __init__(self):
        pygame.init()
        info = pygame.display.Info()
        self.sw, self.sh = info.current_w, info.current_h
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption('Obsidian Chess - Fullscreen')
        
        self.dim = 8
        self.sq_size = min(self.sw, self.sh) // 10
        self.board_width = self.dim * self.sq_size
        self.offset_x = (self.sw - self.board_width) // 2
        self.offset_y = (self.sh - self.board_width) // 2
        
        # Font for pieces
        try:
            self.font = pygame.font.SysFont("segoeuisymbol", int(self.sq_size * 0.8))
        except:
            self.font = pygame.font.SysFont("arial", int(self.sq_size * 0.8))
            
        self.board = chess.Board()
        self.selected_sq = None
        self.clock = pygame.time.Clock()

    def draw_board(self):
        self.screen.fill((30, 30, 30))
        colors = [COLOR_LIGHT, COLOR_DARK]
        for r in range(self.dim):
            for c in range(self.dim):
                color = colors[((r + c) % 2)]
                pygame.draw.rect(self.screen, color, 
                                 (self.offset_x + c*self.sq_size, self.offset_y + r*self.sq_size, 
                                  self.sq_size, self.sq_size))

    def draw_pieces(self):
        piece_map = {
            'K': '♔', 'Q': '♕', 'R': '♖', 'B': '♗', 'N': '♘', 'P': '♙',
            'k': '♚', 'q': '♛', 'r': '♜', 'b': '♝', 'n': '♞', 'p': '♟'
        }
        for r in range(self.dim):
            for c in range(self.dim):
                sq_idx = chess.square(c, 7-r)
                piece = self.board.piece_at(sq_idx)
                if piece:
                    symbol = piece_map[piece.symbol()]
                    color = WHITE_PIECE if piece.color == chess.WHITE else BLACK_PIECE
                    
                    if piece.color == chess.WHITE:
                        shadow = self.font.render(symbol, True, (0,0,0))
                        self.screen.blit(shadow, (self.offset_x + c*self.sq_size + self.sq_size//2 - shadow.get_width()//2 + 2, 
                                                 self.offset_y + r*self.sq_size + self.sq_size//2 - shadow.get_height()//2 + 2))

                    text = self.font.render(symbol, True, color)
                    self.screen.blit(text, (self.offset_x + c*self.sq_size + self.sq_size//2 - text.get_width()//2, 
                                           self.offset_y + r*self.sq_size + self.sq_size//2 - text.get_height()//2))

    def highlight(self):
        if self.selected_sq:
            r, c = self.selected_sq
            s = pygame.Surface((self.sq_size, self.sq_size))
            s.set_alpha(100)
            s.fill(COLOR_HIGHLIGHT)
            self.screen.blit(s, (self.offset_x + c*self.sq_size, self.offset_y + r*self.sq_size))
            
            sq_idx = chess.square(c, 7-r)
            for move in self.board.legal_moves:
                if move.from_square == sq_idx:
                    to_sq = move.to_square
                    to_c = chess.square_file(to_sq)
                    to_r = 7 - chess.square_rank(to_sq)
                    pygame.draw.circle(self.screen, COLOR_MOVES, 
                                     (self.offset_x + to_c*self.sq_size + self.sq_size//2, 
                                      self.offset_y + to_r*self.sq_size + self.sq_size//2), 
                                     self.sq_size//6)

    def run(self):
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
                        self.board = chess.Board()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    c = (pos[0] - self.offset_x) // self.sq_size
                    r = (pos[1] - self.offset_y) // self.sq_size
                    
                    if 0 <= r < 8 and 0 <= c < 8:
                        clicked_sq = chess.square(c, 7-r)
                        if self.selected_sq:
                            prev_r, prev_c = self.selected_sq
                            move = chess.Move(chess.square(prev_c, 7-prev_r), clicked_sq)
                            
                            # Handle promotion
                            if move in self.board.legal_moves:
                                self.board.push(move)
                                self.selected_sq = None
                            else:
                                move_prom = chess.Move(chess.square(prev_c, 7-prev_r), clicked_sq, promotion=chess.QUEEN)
                                if move_prom in self.board.legal_moves:
                                    self.board.push(move_prom)
                                    self.selected_sq = None
                                else:
                                    piece = self.board.piece_at(clicked_sq)
                                    if piece and piece.color == self.board.turn:
                                        self.selected_sq = (r, c)
                                    else:
                                        self.selected_sq = None
                        else:
                            piece = self.board.piece_at(clicked_sq)
                            if piece and piece.color == self.board.turn:
                                self.selected_sq = (r, c)

            self.draw_board()
            self.highlight()
            self.draw_pieces()
            
            if self.board.is_check():
                king_sq = self.board.king(self.board.turn)
                k_c, k_r = chess.square_file(king_sq), 7 - chess.square_rank(king_sq)
                s = pygame.Surface((self.sq_size, self.sq_size))
                s.set_alpha(150)
                s.fill(COLOR_CHECK)
                self.screen.blit(s, (self.offset_x + k_c*self.sq_size, self.offset_y + k_r*self.sq_size))

            if self.board.is_game_over():
                font = pygame.font.SysFont("arial", 60, bold=True)
                txt = font.render(f"Spiel vorbei: {self.board.result()}", True, (255, 255, 255))
                self.screen.blit(txt, (self.sw//2 - txt.get_width()//2, 50))

            pygame.display.flip()
            self.clock.tick(30)

if __name__ == "__main__":
    game = ChessGame()
    game.run()