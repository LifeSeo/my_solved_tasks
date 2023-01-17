import pygame

clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((618, 359))
pygame.display.set_caption("Моя первая игрушка на Python")
icon = pygame.image.load("First_game/images/icon.png").convert_alpha()
pygame.display.set_icon(icon)

# squire = pygame.Surface((50, 170))
# squire.fill("Red")

# my_font = pygame.font.Font("First_game/fonts/Oswald.ttf", 40)
# text_surface = my_font.render("Game", True, "Green")

# player = pygame.image.load("First_game/images/golf.png")
back_ground = pygame.image.load("First_game/images/fon_background.jpg").convert_alpha()

# player = pygame.image.load('First_game/images/animation/left_person/left_1.png')

walk_left = [
    pygame.image.load('First_game/images/animation/left_person/left_1.png').convert_alpha(),
    pygame.image.load('First_game/images/animation/left_person/left_2.png').convert_alpha(),
    pygame.image.load('First_game/images/animation/left_person/left_3.png').convert_alpha(),
    pygame.image.load('First_game/images/animation/left_person/left_4.png').convert_alpha()
]

walk_right = [
    pygame.image.load('First_game/images/animation/right_person/right_1.png').convert_alpha(),
    pygame.image.load('First_game/images/animation/right_person/right_2.png').convert_alpha(),
    pygame.image.load('First_game/images/animation/right_person/right_3.png').convert_alpha(),
    pygame.image.load('First_game/images/animation/right_person/right_4.png').convert_alpha()
]

ghost = pygame.image.load("First_game/images/ghost.png").convert_alpha()
# ghost_x = 620
player_anime_count = 0
bg_second = 0

bg_sound = pygame.mixer.Sound('First_game/sounds/bg.mp3')
bg_sound.play(loops= -1)
volume = 1.0

ghost_timer = pygame.USEREVENT +1
pygame.time.set_timer(ghost_timer, 2500)
ghost_list_in_game = []

player_speed = 5
player_x = 150
player_y = 220
is_jump = False
jump_count = 8
running = True
while running:
    
    # screen.blit(squire, (0, 0))
    # screen.blit(text_surface, (250, 50))
    # screen.blit(back_ground, (0, 0))
    screen.blit(back_ground, (bg_second, 0))
    screen.blit(back_ground, (bg_second + 618, 0))
    # screen.blit(ghost, (ghost_x, 220))
    
    player_rest = walk_left[0].get_rect(topleft =(player_x, player_y))
    # ghos_rect = ghost.get_rect(topleft =(ghost_x, 220))
    
    if ghost_list_in_game:
        for el in ghost_list_in_game:
            screen.blit(ghost, el)
            el.x -= 10
    
            if player_rest.colliderect(el):
                print("Вы проиграли")
    
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
        if jump_count >= -8:
            if jump_count > 0:
                player_y -= (jump_count ** 2) / 2
            else:
                player_y += (jump_count ** 2) / 2
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 8
            
    # ghost_x -= 10
    
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
        if even.type == ghost_timer:
                ghost_list_in_game.append(ghost.get_rect(topleft =(620, 230)))
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