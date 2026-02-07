import pygame

pygame.init()
surf = pygame.Surface((512, 512))
surf.fill((220, 50, 50)) # Red Background

# Draw Border
pygame.draw.rect(surf, (255, 215, 0), (0,0,512,512), 20)

# Draw Text
font = pygame.font.SysFont("arial", 250, bold=True)
text = font.render("W|P", True, (255, 215, 0)) # Gold Text
surf.blit(text, (256 - text.get_width()//2, 256 - text.get_height()//2))

pygame.image.save(surf, "icon.png")
pygame.quit()
