import pygame

pygame.init()

screen_width = 525
screen_height = 300
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Русский рыцарь")
icon = pygame.image.load('icon/icon.knight.png')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
running = True
floor = 1
bg_x = 0
player_x = 20
player_y = 180
player_speed = 4
jump = False
jumpCount = 8
player_anim_count = 0

phon = pygame.image.load('image/Images/1.jpg')
thon = pygame.image.load('image/Images/2.jpg')
player = pygame.image.load('imageknight/1.png')
walk_right = [
    pygame.image.load('imageknight/2.png'),
    pygame.image.load('imageknight/3.png'),
    pygame.image.load('imageknight/6.png'),
    pygame.image.load('imageknight/7.png'),
    pygame.image.load('imageknight/8.png'),
]
monster = pygame.image.load('monster/monster.png')
font = pygame.font.SysFont('Arial', 12)
monster_x = 500
monster_y = 55
monster_speed = 2
monster_alive = True
transition = False
game_over = False
text = font.render('Убейте монстра, чтобы одержать победу', True, (255, 255, 255))
game_over_text = font.render('Вы прошли игру', True, (255, 255, 255))
restart_text = font.render('Нажмите SPACE для начала заново', True, (255, 255, 255))
exit_text = font.render('Нажмите ENTER для выхода', True, (255, 255, 255))


while running:
    clock.tick(23)
    screen.blit(phon if not transition else thon, (bg_x, 0))
    screen.blit(phon if not transition else thon, (bg_x + 540, 0))
    keys = pygame.key.get_pressed()
    screen.blit(walk_right[player_anim_count], (player_x, player_y))
    screen.blit(text, (10, 10))

    if game_over:
        screen.blit(game_over_text, (230,150))
        screen.blit(restart_text, (230,170))
        screen.blit(exit_text, (230,190))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_over = False
                    floor = 1
                    monster_x = 500
                    monster_alive = True

                elif event.key == pygame.K_RETURN:
                    running = False
    else:
        if keys[pygame.K_a] and player_x > 20:
            player_x -= player_speed
        elif keys[pygame.K_d] and player_x < 240:
            player_x += player_speed
        if not jump:
            if keys[pygame.K_w]:
                jump = True
        else:
            if jumpCount >= -8:
                neg = 1
                if jumpCount < 0:
                    neg = -1
                player_y -= (jumpCount ** 2) / 2 * neg
                jumpCount -= 1
            else:
                jump = False
                jumpCount = 8

        if player_anim_count == 3:
            player_anim_count = 0
        else:
            player_anim_count += 1

        bg_x -= 2
        if bg_x == -530:
            bg_x = 0

        if monster_alive:
            screen.blit(monster, (monster_x, monster_y))
            if monster_x > player_x:
                monster_x -= monster_speed
            elif monster_x < player_x:
                monster_x += monster_speed

        if player_x < monster_x + monster.get_width() and player_x + player.get_width() > monster_x and player_y < monster_y + monster.get_height() and player_y + player.get_height() > monster_y:
            monster_alive = False

        if bg_x == -450 and not monster_alive:
            transition = True
            floor = 2
            bg_x = 0
            keys = pygame.key.get_pressed()
            screen.blit(walk_right[player_anim_count], (player_x, player_y))
            monster_alive = True
            monster_x = 400


        if not monster_alive and floor == 2:
            game_over = True

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
