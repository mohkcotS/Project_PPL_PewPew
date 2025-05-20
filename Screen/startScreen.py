import pygame
import math

def show_start_screen(screen, width, height, clock):
    font = pygame.font.Font("src/assets/font/m6x11plus.ttf", 55) 

    title_text = pygame.image.load("src/assets/startScreen/title.png")
    title_text = pygame.transform.scale(title_text, (title_text.get_width() // 3, title_text.get_height() // 3))
    
    background = pygame.image.load("src/assets/bg.gif")
    background = pygame.transform.scale(background, (width, height))

    blink_surface = pygame.Surface((width, 100), pygame.SRCALPHA)

    while True:
        screen.blit(background, (0, 0))
        screen.blit(title_text, ((width - title_text.get_width()) // 2, height // 6))

        t = pygame.time.get_ticks() / 200  # tốc độ nhấp nháy
        alpha = int(128 + 127 * math.sin(t)) 

        start_text = font.render("Press ENTER to Start", True, (0, 0, 0)) 
        start_text.set_alpha(alpha)

        text_x = (width - start_text.get_width()) // 2
        text_y = height // 2 + 40
        screen.blit(start_text, (text_x, text_y))

        pygame.display.flip()
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return  