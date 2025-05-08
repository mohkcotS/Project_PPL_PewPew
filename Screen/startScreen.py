import pygame

def show_start_screen(screen,width,height,clock):
    font = pygame.font.SysFont(None, 60)
    title_text = font.render("Pew Pew", True, (255, 255, 255))
    start_text = font.render("Press ENTER to Start", True, (255, 255, 255))
    
    while True:
        screen.fill((0, 0, 0))  # nền đen
        screen.blit(title_text, ((width - title_text.get_width()) // 2, height // 3))
        screen.blit(start_text, ((width - start_text.get_width()) // 2, height // 2))

        pygame.display.flip()
        clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return  # Thoát khỏi màn hình start