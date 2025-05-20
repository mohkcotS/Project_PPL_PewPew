import pygame

def show_instruction_screen(screen, width, height, clock):
    font = pygame.font.SysFont(None, 55)
    title_font = pygame.font.SysFont(None, 40)
    instruction_font = pygame.font.SysFont(None, 30)
    background = pygame.image.load("src/assets/Space_Background.png")
    background = pygame.transform.scale(background, (width, height))

    color1 = (255, 105, 97)
    color2 = (255, 255, 153)
    color3 = (144, 238, 144)

    instruction_text = font.render("Game Instructions", True, (color2))
    command_text = title_font.render("Command Instruction", True, (color1))
    direction_text = title_font.render("Available Directions", True, (color1))
    buff_text = title_font.render("Available Buffs", True, (color1))
    start_text = font.render("Press ENTER to Start", True, (color3))

    leftTopIns = [
        "• left : Targets to the left",
        "",
        "• mleft : Targets in the middle left",
        "",
        "• mid : Targets to the middle",
        "",
        "• mright : Targets to the middle right",
        "",
        "•right : Targets to the right",
    ]

    rightTopIns = [
        "• laser : Clear all enemies power",
        "",
        "• laserP : Lazer buff fraction",
        "",
        "• freeze : Freezes enemies movement",
        "",
        "• freezeP : Freeze buff fraction",
    ]

    botLeftIns = [
        "• attack <direction> <ID> – Fire at enemy ships.",
        "   Example: attack left Sco921",
        "",
        "• defend <direction> – Block incoming attacks.",
        "   Example: defend mid",
        "",
        "• use heal - Restore player’s health.",
    ]
    botRightIns = [
        "• use <skill> <direction> – Activate special abilities.",
        "   Example: use laser right",
        "",
        "• collect <buff> – Pick up piece of skill",
        "   Example: collect laserP",
    ]

    while True:
        screen.blit(background, (0, 0)) # nền đen

        # === Section: Instruction Title ===
        y = 40
        screen.blit(instruction_text, ((width - instruction_text.get_width()) // 2, y))

        # === Section: Directions & Buffs Titles ===
        y += 70
        screen.blit(direction_text, (100, y))
        screen.blit(buff_text, (700, y))

        # === Section: Directions Content ===
        y_offset = y + 40
        for line in leftTopIns:
            line_surface = instruction_font.render(line, True, (255, 255, 255))
            screen.blit(line_surface, (100, y_offset))
            y_offset += 25  # Line spacing

        # === Section: Buffs Content ===
        y_offset = y + 40
        for line in rightTopIns:
            line_surface = instruction_font.render(line, True, (255, 255, 255))
            screen.blit(line_surface, (700, y_offset))
            y_offset += 25

        # === Section: Command Instruction Title ===
        y = y_offset + 80
        screen.blit(command_text, ((width - command_text.get_width()) // 2, y))

        # === Section: Commands Content ===
        y_offset = y + 50
        for line in botLeftIns:
            line_surface = instruction_font.render(line, True, (255, 255, 255))
            screen.blit(line_surface, (50, y_offset))
            y_offset += 25

        y_offset = y + 50
        for line in botRightIns:
            line_surface = instruction_font.render(line, True, (255, 255, 255))
            screen.blit(line_surface, (650, y_offset))
            y_offset += 25

        # === Section: Start Prompt ===
        y = y_offset + 90
        screen.blit(start_text, ((width - start_text.get_width()) // 2, y))

        pygame.display.flip()
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return
