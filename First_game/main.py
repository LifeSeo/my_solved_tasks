import pygame

pygame.init()
screen = pygame.display.set_mode((600, 300))
pygame.display.set_caption("Моя первая игрушка на Python")
icon = pygame.image.load("First_game/images/icon.png")
pygame.display.set_icon(icon)

running = True
while running:
    # screen.fill((22, 177, 247))
    pygame.display.update()
    for even in pygame.event.get():
        if even.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif even.type == pygame.KEYDOWN:
            if even.key == pygame.K_F1:
                screen.fill((52, 134, 235)) 