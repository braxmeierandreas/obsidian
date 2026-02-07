import pygame
import random
import sys

# Farben
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
DARK_GREY = (30, 30, 30)

class SnakeGame:
    def __init__(self):
        pygame.init()
        info = pygame.display.Info()
        self.sw, self.sh = info.current_w, info.current_h
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("Snake - Fullscreen")
        
        self.block_size = 30
        self.speed = 12
        
        # Center the grid
        self.cols = (self.sw // self.block_size) - 2
        self.rows = (self.sh // self.block_size) - 4
        self.offset_x = (self.sw - self.cols * self.block_size) // 2
        self.offset_y = (self.sh - self.rows * self.block_size) // 2
        
        self.reset()
        self.font = pygame.font.SysFont("arial", 36, bold=True)

    def reset(self):
        self.snake = [[self.cols // 2, self.rows // 2]]
        self.dir = [1, 0]
        self.food = self.new_food()
        self.score = 0
        self.game_over = False

    def new_food(self):
        while True:
            food = [random.randint(0, self.cols - 1), random.randint(0, self.rows - 1)]
            if food not in self.snake:
                return food

    def run(self):
        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if self.game_over and event.key == pygame.K_r:
                        self.reset()
                    
                    if not self.game_over:
                        if event.key == pygame.K_UP and self.dir != [0, 1]: self.dir = [0, -1]
                        if event.key == pygame.K_DOWN and self.dir != [0, -1]: self.dir = [0, 1]
                        if event.key == pygame.K_LEFT and self.dir != [1, 0]: self.dir = [-1, 0]
                        if event.key == pygame.K_RIGHT and self.dir != [-1, 0]: self.dir = [1, 0]

            if not self.game_over:
                # Move
                head = [self.snake[0][0] + self.dir[0], self.snake[0][1] + self.dir[1]]
                
                # Check collision
                if (head[0] < 0 or head[0] >= self.cols or 
                    head[1] < 0 or head[1] >= self.rows or 
                    head in self.snake):
                    self.game_over = True
                else:
                    self.snake.insert(0, head)
                    if head == self.food:
                        self.score += 1
                        self.food = self.new_food()
                    else:
                        self.snake.pop()

            # Draw
            self.screen.fill(DARK_GREY)
            
            # Border
            pygame.draw.rect(self.screen, (100, 100, 100), 
                             (self.offset_x - 5, self.offset_y - 5, 
                              self.cols * self.block_size + 10, self.rows * self.block_size + 10), 2)
            
            # Food
            pygame.draw.rect(self.screen, RED, 
                             (self.offset_x + self.food[0] * self.block_size, 
                              self.offset_y + self.food[1] * self.block_size, 
                              self.block_size, self.block_size), border_radius=5)
            
            # Snake
            for i, part in enumerate(self.snake):
                color = GREEN if i == 0 else (0, 200, 0)
                pygame.draw.rect(self.screen, color, 
                                 (self.offset_x + part[0] * self.block_size, 
                                  self.offset_y + part[1] * self.block_size, 
                                  self.block_size - 1, self.block_size - 1), border_radius=3)

            # Score
            score_txt = self.font.render(f"Score: {self.score}", True, YELLOW)
            self.screen.blit(score_txt, (self.sw // 2 - score_txt.get_width() // 2, 20))

            if self.game_over:
                over_txt = self.font.render("GAME OVER! Drücke 'R' zum Neustart", True, RED)
                self.screen.blit(over_txt, (self.sw // 2 - over_txt.get_width() // 2, self.sh // 2))

            pygame.display.flip()
            clock.tick(self.speed)

if __name__ == "__main__":
    game = SnakeGame()
    game.run()