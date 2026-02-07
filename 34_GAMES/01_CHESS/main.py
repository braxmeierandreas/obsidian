import pygame
import chess
import sys

# Configuration
WIDTH, HEIGHT = 640, 640
DIMENSION = 8
SQ_SIZE = WIDTH // DIMENSION
MAX_FPS = 15
IMAGES = {}

# Colors
COLOR_LIGHT = (232, 235, 239)
COLOR_DARK = (125, 135, 150)
COLOR_HIGHLIGHT = (186, 202, 68)  # Yellow-ish for selected
COLOR_MOVES = (214, 214, 105)     # Lighter yellow for legal moves
COLOR_CHECK = (255, 100, 100)     # Red for check

def load_images():
    """
    We will use pygame.font to render unicode chess pieces instead of loading images
    to keep this self-contained and 'perfect' without missing asset issues.
    """
    pass

def draw_board(screen):
    colors = [COLOR_LIGHT, COLOR_DARK]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r + c) % 2)]
            pygame.draw.rect(screen, color, pygame.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

def draw_pieces(screen, board, font):
    # Unicode pieces
    # White: ♔♕♖♗♘♙
    # Black: ♚♛♜♝♞♟
    piece_map = {
        'K': '♔', 'Q': '♕', 'R': '♖', 'B': '♗', 'N': '♘', 'P': '♙',
        'k': '♚', 'q': '♛', 'r': '♜', 'b': '♝', 'n': '♞', 'p': '♟'
    }
    
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            # python-chess board.piece_at uses 0-63 squares, but rank 0 is bottom.
            # Pygame (0,0) is top-left.
            # chess.A1 (0) is bottom-left.
            # Matrix: r=0 -> rank 8, r=7 -> rank 1
            # File: c=0 -> a, c=7 -> h
            
            square_index = chess.square(c, 7-r)
            piece = board.piece_at(square_index)
            
            if piece:
                symbol = piece_map[piece.symbol()]
                # Color logic: The unicode pieces are black/white glyphs, 
                # but we can color them Black and White for visibility.
                if piece.color == chess.WHITE:
                    text_color = (0, 0, 0) # Outline/Glyph
                    # Actually standard fonts just draw the glyph. 
                    # Let's render them in Black for Black pieces and White for White pieces
                    # regardless of the specific glyph to be clear, OR stick to black ink.
                    # Better: White pieces = White color with black outline effect?
                    # Simple: Black pieces = Black, White pieces = White.
                    render_color = (255, 255, 255)
                    # Add a slight shadow/outline for visibility on light squares?
                else:
                    render_color = (0, 0, 0)
                
                # Render text
                text_surface = font.render(symbol, True, render_color)
                text_rect = text_surface.get_rect(center=(c*SQ_SIZE + SQ_SIZE//2, r*SQ_SIZE + SQ_SIZE//2))
                
                # Simple shadow for white pieces on light squares
                if piece.color == chess.WHITE:
                     shadow_surface = font.render(symbol, True, (0,0,0))
                     shadow_rect = shadow_surface.get_rect(center=(c*SQ_SIZE + SQ_SIZE//2 + 2, r*SQ_SIZE + SQ_SIZE//2 + 2))
                     screen.blit(shadow_surface, shadow_rect)
                     
                screen.blit(text_surface, text_rect)

def highlight_squares(screen, board, selected_square, legal_moves):
    if selected_square is not None:
        r, c = selected_square
        # Highlight selected square
        s = pygame.Surface((SQ_SIZE, SQ_SIZE))
        s.set_alpha(100) # transparency
        s.fill(COLOR_HIGHLIGHT)
        screen.blit(s, (c*SQ_SIZE, r*SQ_SIZE))
        
        # Highlight legal moves from this square
        # Convert (r, c) to chess.Square
        sq_index = chess.square(c, 7-r)
        
        for move in legal_moves:
            if move.from_square == sq_index:
                # To square
                to_sq = move.to_square
                to_c = chess.square_file(to_sq)
                to_r = 7 - chess.square_rank(to_sq)
                
                # Draw a circle or highlight
                pygame.draw.circle(screen, COLOR_MOVES, 
                                 (to_c*SQ_SIZE + SQ_SIZE//2, to_r*SQ_SIZE + SQ_SIZE//2), 
                                 SQ_SIZE//6)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Obsidian Chess')
    clock = pygame.time.Clock()
    
    # Try to find a good font that supports chess symbols
    font_name = "segoeuisymbol" # Standard on Windows 10/11
    try:
        font = pygame.font.SysFont(font_name, int(SQ_SIZE * 0.8))
    except:
        font = pygame.font.SysFont("arial", int(SQ_SIZE * 0.8))

    board = chess.Board()
    
    selected_square = None # Tuple (row, col)
    running = True
    
    while running:
        legal_moves = list(board.legal_moves)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos() # (x, y)
                col = location[0] // SQ_SIZE
                row = location[1] // SQ_SIZE
                
                clicked_sq_index = chess.square(col, 7-row)
                
                if selected_square == (row, col):
                    # Deselect
                    selected_square = None
                else:
                    # If we already have a selection, check if this is a valid move
                    move_made = False
                    if selected_square is not None:
                        prev_r, prev_c = selected_square
                        prev_sq_index = chess.square(prev_c, 7-prev_r)
                        
                        # Check for promotion (auto-promote to Queen for simplicity in this version)
                        # A robust version would ask, but for "one click start" simplicity we default Queen.
                        # We construct a move. If it's a promotion rank, we try adding promotion.
                        move = chess.Move(prev_sq_index, clicked_sq_index)
                        
                        if move in board.legal_moves:
                            board.push(move)
                            move_made = True
                        else:
                            # Try promotion
                            move_prom = chess.Move(prev_sq_index, clicked_sq_index, promotion=chess.QUEEN)
                            if move_prom in board.legal_moves:
                                board.push(move_prom)
                                move_made = True
                    
                    if move_made:
                        selected_square = None
                        # Check game over state
                        if board.is_game_over():
                            print("Game Over:", board.result())
                    else:
                        # Select new piece if it belongs to turn player
                        piece = board.piece_at(clicked_sq_index)
                        if piece and piece.color == board.turn:
                            selected_square = (row, col)
                        else:
                            selected_square = None

        draw_board(screen)
        highlight_squares(screen, board, selected_square, legal_moves)
        draw_pieces(screen, board, font)
        
        # Draw checkmate/check indication
        if board.is_check():
            # Find king
            king_sq = board.king(board.turn)
            k_c = chess.square_file(king_sq)
            k_r = 7 - chess.square_rank(king_sq)
            s = pygame.Surface((SQ_SIZE, SQ_SIZE))
            s.set_alpha(100)
            s.fill(COLOR_CHECK)
            screen.blit(s, (k_c*SQ_SIZE, k_r*SQ_SIZE))

        if board.is_game_over():
            # Simple text overlay
            outcome = board.result()
            overlay = pygame.Surface((WIDTH, HEIGHT))
            overlay.set_alpha(150)
            overlay.fill((0,0,0))
            screen.blit(overlay, (0,0))
            
            msg = f"Game Over: {outcome}"
            text = font.render(msg, True, (255, 255, 255))
            text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//2))
            screen.blit(text, text_rect)

        pygame.display.flip()
        clock.tick(MAX_FPS)

if __name__ == "__main__":
    main()
