import pygame

image_path = "/data/data/org.test.myapp/files/app/"

clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((618, 359))
pygame.display.set_caption("Моя первая игрушка на Python")
icon = pygame.image.load(image_path + "images/icon.png").convert_alpha()
pygame.display.set_icon(icon)

# squire = pygame.Surface((50, 170))
# squire.fill("Red")

# my_font = pygame.font.Font("First_game/fonts/Oswald.ttf", 40)
# text_surface = my_font.render("Game", True, "Green")

# player = pygame.image.load("First_game/images/golf.png")
back_ground = pygame.image.load(image_path + 
                                "images/fon_background.jpg").convert_alpha()

# player = pygame.image.load('First_game/images/animation/left_person/left_1.png')

walk_left = [
    pygame.image.load(image_path + 
                      'images/animation/left_person/left_1.png').convert_alpha(),
    pygame.image.load(image_path + 
                      'images/animation/left_person/left_2.png').convert_alpha(),
    pygame.image.load(image_path + 
                      'images/animation/left_person/left_3.png').convert_alpha(),
    pygame.image.load(image_path + 
                      'images/animation/left_person/left_4.png').convert_alpha()
]

walk_right = [
    pygame.image.load(image_path + 
                      'images/animation/right_person/right_1.png').convert_alpha(),
    pygame.image.load(image_path + 
                      'images/animation/right_person/right_2.png').convert_alpha(),
    pygame.image.load(image_path + 
                      'images/animation/right_person/right_3.png').convert_alpha(),
    pygame.image.load(image_path + 
                      'images/animation/right_person/right_4.png').convert_alpha()
]

ghost = pygame.image.load(image_path + "images/ghost.png").convert_alpha()
# ghost_x = 620
player_anime_count = 0
bg_second = 0

bg_sound = pygame.mixer.Sound(image_path + 'sounds/bg.mp3')
bg_sound.play(loops=-1)
volume = 1.0

ghost_timer = pygame.USEREVENT + 1
pygame.time.set_timer(ghost_timer, 2500)
ghost_list_in_game = []

label = pygame.font.Font(image_path + "fonts/Oswald.ttf", 40)
lose_label = label.render("Вы проиграли (:- !", True, (193, 196, 199))
restart_label = label.render("Играть заного", True, (115, 132, 148))
restart_label_rect = restart_label.get_rect(topleft=(180, 200))

bullet = pygame.image.load(image_path + "images/bullet.png").convert_alpha()
bullets = []
bullets_max = 5

player_speed = 5
player_x = 150
player_y = 220
is_jump = False
jump_count = 8
running = True
gameplay = True

while running:

    # screen.blit(squire, (0, 0))
    # screen.blit(text_surface, (250, 50))
    # screen.blit(back_ground, (0, 0))
    screen.blit(back_ground, (bg_second, 0))
    screen.blit(back_ground, (bg_second + 618, 0))
    # screen.blit(ghost, (ghost_x, 220))

    if gameplay:

        player_rest = walk_left[0].get_rect(topleft=(player_x, player_y))
        # ghos_rect = ghost.get_rect(topleft =(ghost_x, 220))

        if ghost_list_in_game:
            for (i, el) in enumerate(ghost_list_in_game):
                screen.blit(ghost, el)
                el.x -= 10

                if el.x < -10:
                    ghost_list_in_game.pop(i)

                if player_rest.colliderect(el):
                    gameplay = False

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
            
        if bullets:
            for (i, el) in enumerate(bullets):
                screen.blit(bullet, (el.x, el.y))
                el.x += 4
                
                if el.x > 630:
                    bullets.pop(i)
                    
                if ghost_list_in_game:
                    for (index, ghost_el) in enumerate(ghost_list_in_game):
                        if el.colliderect(ghost_el):
                            ghost_list_in_game.pop(index)
                            bullets.pop(i)

    else:
        screen.fill((87, 88, 89))
        screen.blit(lose_label, (180, 100))
        screen.blit(restart_label, restart_label_rect)
        
        mouse = pygame.mouse.get_pos()
        if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            gameplay = True
            player_x = 150
            ghost_list_in_game.clear()
            bullets.clear()
            bullets_max = 5
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
            ghost_list_in_game.append(ghost.get_rect(topleft=(620, 230)))
            
        if gameplay and even.type == pygame.KEYUP and even.key == pygame.K_RSHIFT and bullets_max > 0:
                bullets.append(bullet.get_rect(topleft=(player_x + 30, player_y + 10)))
                bullets_max -= 1
            
        elif even.type == pygame.KEYDOWN:
            if even.key == pygame.K_F1:
                screen.fill((52, 134, 235))

            elif even.key == pygame.K_F2:
                volume -= 0.1
                bg_sound.set_volume(volume)
                print(bg_sound.get_volume())

            elif even.key == pygame.K_F3:
                volume += 0.1
                bg_sound.set_volume(volume)
                print(bg_sound.get_volume())
    

    clock.tick(15)
