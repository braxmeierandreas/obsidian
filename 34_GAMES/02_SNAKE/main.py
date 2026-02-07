import pygame
import time
import random

# Initialisierung
pygame.init()

# Farben
WHITE = (255, 255, 255)
YELLOW = (255, 255, 102)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)
DARK_GREY = (40, 40, 40)

# Display Einstellungen
DIS_WIDTH = 800
DIS_HEIGHT = 600
SNAKE_BLOCK = 20
SNAKE_SPEED = 15

dis = pygame.display.set_mode((DIS_WIDTH, DIS_HEIGHT))
pygame.display.set_caption('Obsidian Snake')

clock = pygame.time.Clock()

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, GREEN, [x[0], x[1], snake_block, snake_block])
        # Kleiner Rand für Segmente
        pygame.draw.rect(dis, BLACK, [x[0], x[1], snake_block, snake_block], 1)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [DIS_WIDTH / 6, DIS_HEIGHT / 3])

def show_score(score):
    value = score_font.render("Score: " + str(score), True, YELLOW)
    dis.blit(value, [0, 0])

def gameLoop():
    game_over = False
    game_close = False

    x1 = DIS_WIDTH / 2
    y1 = DIS_HEIGHT / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    # Zufällige Position für Essen (auf Raster ausgerichtet)
    foodx = round(random.randrange(0, DIS_WIDTH - SNAKE_BLOCK) / 20.0) * 20.0
    foody = round(random.randrange(0, DIS_HEIGHT - SNAKE_BLOCK) / 20.0) * 20.0

    while not game_over:

        while game_close == True:
            dis.fill(DARK_GREY)
            message("Verloren! Drücke C zum Weiterspielen oder Q zum Beenden", RED)
            show_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -SNAKE_BLOCK
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = SNAKE_BLOCK
                    x1_change = 0

        # Wand-Kollision
        if x1 >= DIS_WIDTH or x1 < 0 or y1 >= DIS_HEIGHT or y1 < 0:
            game_close = True
        
        x1 += x1_change
        y1 += y1_change
        dis.fill(BLACK)
        
        # Hintergrund-Gitter (optional, für Optik)
        for x in range(0, DIS_WIDTH, SNAKE_BLOCK):
            pygame.draw.line(dis, DARK_GREY, (x, 0), (x, DIS_HEIGHT))
        for y in range(0, DIS_HEIGHT, SNAKE_BLOCK):
            pygame.draw.line(dis, DARK_GREY, (0, y), (DIS_WIDTH, y))

        pygame.draw.rect(dis, RED, [foodx, foody, SNAKE_BLOCK, SNAKE_BLOCK])
        
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Selbst-Kollision
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(SNAKE_BLOCK, snake_List)
        show_score(Length_of_snake - 1)

        pygame.display.update()

        # Essen finden
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, DIS_WIDTH - SNAKE_BLOCK) / 20.0) * 20.0
            foody = round(random.randrange(0, DIS_HEIGHT - SNAKE_BLOCK) / 20.0) * 20.0
            Length_of_snake += 1

        clock.tick(SNAKE_SPEED)

    pygame.quit()
    quit()

if __name__ == "__main__":
    gameLoop()
