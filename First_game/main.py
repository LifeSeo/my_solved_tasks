import pygame

clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((618, 359))
pygame.display.set_caption("Моя первая игрушка на Python")
icon = pygame.image.load("First_game/images/icon.png")
pygame.display.set_icon(icon)

# squire = pygame.Surface((50, 170))
# squire.fill("Red")

# my_font = pygame.font.Font("First_game/fonts/Oswald.ttf", 40)
# text_surface = my_font.render("Game", True, "Green")

# player = pygame.image.load("First_game/images/golf.png")
back_ground = pygame.image.load("First_game/images/fon_background.jpg")

# player = pygame.image.load('First_game/images/animation/left_person/left_1.png')

walk_left = [
    pygame.image.load('First_game/images/animation/left_person/left_1.png'),
    pygame.image.load('First_game/images/animation/left_person/left_2.png'),
    pygame.image.load('First_game/images/animation/left_person/left_3.png'),
    pygame.image.load('First_game/images/animation/left_person/left_4.png')
]

walk_right = [
    pygame.image.load('First_game/images/animation/right_person/right_1.png'),
    pygame.image.load('First_game/images/animation/right_person/right_2.png'),
    pygame.image.load('First_game/images/animation/right_person/right_3.png'),
    pygame.image.load('First_game/images/animation/right_person/right_4.png')
]

player_anime_count = 0
bg_second = 0

bg_sound = pygame.mixer.Sound('First_game/sounds/bg.mp3')
bg_sound.play(loops= -1)
volume = 1.0

player_speed = 5
player_x = 150
player_y = 220
is_jump = False
jump_count = 7
running = True
while running:
    
    # screen.blit(squire, (0, 0))
    # screen.blit(text_surface, (250, 50))
    # screen.blit(back_ground, (0, 0))
    screen.blit(back_ground, (bg_second, 0))
    screen.blit(back_ground, (bg_second + 618, 0))
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        screen.blit(walk_left[player_anime_count], (player_x, player_y))
    else:
        screen.blit(walk_right[player_anime_count], (player_x, player_y))
        
    if keys[pygame.K_LEFT] and player_x > 50:
        player_x -= player_speed
    elif keys[pygame.K_RIGHT] and player_x < 200:
        player_x += player_speed
    
    if not is_jump:
        if keys[pygame.K_SPACE]:
            is_jump = True
    else:
        if jump_count >= -7:
            if jump_count > 0:
                player_y -= (jump_count ** 2) / 2
            else:
                player_y += (jump_count ** 2) / 2
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 7
    
    if player_anime_count == 3:
        player_anime_count = 0
    else:
        player_anime_count += 1
        
    bg_second -= 2
    if bg_second == -618:
            bg_second = 0
    # screen.blit(player, (300, 220))
    # pygame.draw.circle(screen, "Blue", (250, 150), 30)
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
        
            elif even.key == pygame.K_F2:
                volume -= 0.1
                bg_sound.set_volume(volume)
                print(bg_sound.get_volume() )
            
            elif even.key == pygame.K_F3:
                volume += 0.1
                bg_sound.set_volume(volume)
                print(bg_sound.get_volume() )
                
                
    clock.tick(15)