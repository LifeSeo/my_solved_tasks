import pygame

pygame.init()
screen = pygame.display.set_mode((600, 300))
pygame.display.set_caption("Моя первая игрушка на Python")
icon = pygame.image.load("First_game/images/icon.png")
pygame.display.set_icon(icon)

squire = pygame.Surface((50, 170))
squire.fill("Red")

my_font = pygame.font.Font("First_game/fonts/Oswald.ttf", 40)
text_surface = my_font.render("Game", True, "Green")

player = pygame.image.load("First_game/images/golf.png")

running = True
while running:
    
    screen.blit(squire, (0, 0))
    screen.blit(text_surface, (250, 50))
    screen.blit(player, (50, 100))
    pygame.draw.circle(screen, "Blue", (250, 150), 30)
    # pygame.draw.circle(squire, "Blue", (10, 7), 5)
    # screen.fill((22, 177, 247))
    pygame.display.update()
    for even in pygame.event.get():
        if even.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif even.type == pygame.KEYDOWN:
            if even.key == pygame.K_F1:
                screen.fill((52, 134, 235)) 