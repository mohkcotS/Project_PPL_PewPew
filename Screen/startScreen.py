import pygame

def show_start_screen(screen,width,height,clock):
    font = pygame.font.SysFont(None, 55)
    instruction_font = pygame.font.SysFont(None, 30)

    title_text = font.render("Pew Pew", True, (255, 255, 255))
    start_text = font.render("Press ENTER to Start", True, (255, 255, 255))
    instruction_text = font.render("Game Instructions", True, (255, 255, 255))
    
    instructions = [
        "1. Use 'attack <direction> <ID>' to shoot enemy ships.",
        "   - Example: 'attack left Sco92' to strike a ship on the left.",
        "   - Use when an enemy is in range and poses a threat.",
        "2. Use 'defend <direction>' to shield player from incoming attacks.",
        "   - Example: 'defend mid' to protect the center.",
        "   - Deploy when enemy projectiles approach player.",
        "3. Use 'use heal' to restore player's health.",
        "   - Activate when player's health is low to survive longer.",
        "4. Use 'use <skill> <direction>' to unleash special abilities.",
        "   - Example: 'use laser right' to clear enemies on the right.",
        "   - Use 'laser' or 'freeze' when facing multiple foes.",
        "5. Use 'collect <buff>' to gain power-ups.",
        "   - Example: 'collect laserP' to enhance your laser.",
        "   - Collect when buffs (laserP, freezeP) appear on screen."
    ]
    while True:
        screen.fill((0, 0, 0))  # nền đen
        screen.blit(title_text, ((width - title_text.get_width()) // 2, height // 8))
        screen.blit(start_text, ((width - start_text.get_width()) // 2, height // 4.3))
        screen.blit(instruction_text, ((width - instruction_text.get_width()) // 2, height // 2.7))

        # Render and blit instructions
        y_offset = height // 2.3  # Start below "Press ENTER to Start" with spacing
        left_margin = 320  # Left margin for instructions
        for line in instructions:
            instruction_surface = instruction_font.render(line, True, (255, 255, 255))
            screen.blit(instruction_surface, (left_margin, y_offset))
            y_offset += 30 # Increase line spacing to 40px for better readability
        
        pygame.display.flip()
        clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return  # Thoát khỏi màn hình start