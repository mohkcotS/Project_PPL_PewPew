import pygame

def show_direction_screen(screen, width, height, clock):
    font = pygame.font.SysFont(None, 55)
    title_font = pygame.font.SysFont(None, 40)
    text_font = pygame.font.Font("src/assets/font/m6x11plus.ttf", 40)

    background = pygame.image.load("src/assets/Space_Background.png")
    
    radius = 150
    player = pygame.image.load("src/assets/Player.gif")
    player = pygame.transform.scale(player, (radius, radius))

    bullet = pygame.image.load("src/assets/Bullet/02.png")
    bulletLeft = pygame.transform.rotate(bullet,46)
    bulletMLeft = pygame.transform.rotate(bullet,33)
    bulletMid = pygame.transform.rotate(bullet, 0)
    bulletMRight = pygame.transform.rotate(bullet, -33)
    bulletRight = pygame.transform.rotate(bullet, -46)

    background = pygame.transform.scale(background, (width, height))

    color1 = (103, 232, 249)


    instruction_text = font.render("Game Instructions", True, (color1))
    direction_text = font.render("Direction", True, (color1))

    leftDirText = text_font.render("left", True, (color1))
    mleftDirText = text_font.render("mleft", True, (color1))
    rightDirText = text_font.render("right", True, (color1))
    mrightDirText = text_font.render("mright", True, (color1))
    midDirText = text_font.render("mid", True, (color1))
    playerText = text_font.render("Player",True,(255,255,255))

    while True:
        screen.blit(background, (0, 0)) # nền đen

        # === Section: Instruction Title ===
        y = 40
        screen.blit(instruction_text, ((width - instruction_text.get_width()) // 2, y))

        y=100
        screen.blit(direction_text, ((width - direction_text.get_width()) // 2, y))

        y = 200
        screen.blit(leftDirText, (40, y))
        screen.blit(mleftDirText, ((600-mleftDirText.get_width())//2, y))
        screen.blit(midDirText, ((width-midDirText.get_width())//2, y))
        screen.blit(mrightDirText, (600 + (600-mrightDirText.get_width())//2, y))
        screen.blit(rightDirText, (1090, y))

        screen.blit(player, ((width- player.get_width())// 2 ,560 ))
        screen.blit(playerText, ((width- playerText.get_width())// 2 , 720 ))

        screen.blit(bulletLeft, (150 ,300))
        screen.blit(bulletMLeft, (380 ,375))
        screen.blit(bulletMid, (580 ,450))
        screen.blit(bulletMRight, (720 ,375))
        screen.blit(bulletRight, (1000 ,300))



        pygame.display.flip()
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return
