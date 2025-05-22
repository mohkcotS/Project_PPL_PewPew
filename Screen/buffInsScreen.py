import pygame
import math


def show_buff_screen(screen, width, height, clock):
    text_font = pygame.font.Font("src/assets/font/SpaceMonoB.ttf", 28)
    text_font1 = pygame.font.Font("src/assets/font/SpaceMonoB.ttf", 20)

    background = pygame.image.load("src/assets/Space_Background.png")
    background = pygame.transform.scale(background, (width, height))

    color1 = (103, 232, 249)

    instruction_text = pygame.image.load("src/assets/InstructionScreen/instruction.png")
    instruction_text = pygame.transform.scale(instruction_text, (500,500))

    laserP = pygame.image.load("src/assets/Buffs/Laser.png")
    laserP = pygame.transform.scale(laserP, (75, 75))

    freezeP = pygame.image.load("src/assets/Buffs/Freeze.png")
    freezeP = pygame.transform.scale(freezeP, (75, 75))

    heal = pygame.image.load("src/assets/Buffs/Heal.png")
    heal = pygame.transform.scale(heal, (75, 75))

    laserSkill = pygame.image.load("src/assets/Buffs/LaserEffect.png")
    laserSkill = pygame.transform.scale(laserSkill, (75, 75))

    freezeSkill = pygame.Surface((75, 75), pygame.SRCALPHA)
    freezeSkill.fill((0, 255, 255, 80))

    laserP_Title = text_font1.render("LASER PIECE", True, (218,48,0))
    laserPInstruction = [
    "Collect 3 pieces to unlock",
    "the Laser Skill.",
    ]

    freezeP_Title = text_font1.render("FREEZE PIECE", True, (47,177,187))
    freezePInstruction = [
    "Collect 3 pieces to unlock",
    "the Freeze Skill.",
    ]

    heal_Title = text_font1.render("HEAL", True, (73,201,3))
    healInstruction = [
    "Kill enemies to gather",
    "Collect 5 pieces to recover 1 HP.",
    ]

    laser_Title = text_font1.render("LASER SKILL", True, (255,188,34))
    laserInstruction = [
    "Kills all enemies in a",
    "specified direction.",
    ]

    freeze_Title = text_font1.render("FREEZE SKILL", True, (0,255,255))
    freezeInstruction = [
    "Freezes all enemies in a",
    "specified direction.",
    ]


    #Enter to continue
    enterText = text_font.render("ENTER", True, (color1))
    arrow_color = color1
    arrow_size = 22 
    arrow_gap = 8  

    while True:
        screen.blit(background, (0, 0)) # nền đen

        #Instruction
        screen.blit(instruction_text, ((width - instruction_text.get_width()) // 2, -150))

        #Buff
        y = 200
        screen.blit(laserP, ((100, y)))
        screen.blit(laserP_Title, ((200, y)))
        screen.blit(laserSkill, ((700, y)))
        screen.blit(laser_Title, ((800, y)))
        
        y = 225
        for line in laserPInstruction:
            line_surface = text_font1.render(line, True, (255, 255, 255))
            screen.blit(line_surface, (200, y))
            y += 25 

        y = 225
        for line in laserInstruction:
            line_surface = text_font1.render(line, True, (255, 255, 255))
            screen.blit(line_surface, (800, y))
            y += 25 

        y = 350
        screen.blit(freezeP, ((100, y)))
        screen.blit(freezeP_Title, ((200, y)))
        screen.blit(freezeSkill, (700, y))
        screen.blit(freeze_Title, (800, y))

        y = 375
        for line in freezePInstruction:
            line_surface = text_font1.render(line, True, (255, 255, 255))
            screen.blit(line_surface, (200, y))
            y += 25 
        
        y= 375
        for line in freezeInstruction:
            line_surface = text_font1.render(line, True, (255, 255, 255))
            screen.blit(line_surface, (800, y))
            y += 25 

        y = 500 
        screen.blit(heal, ((100, y)))
        screen.blit(heal_Title, ((200, y)))

        y = 525
        for line in healInstruction:
            line_surface = text_font1.render(line, True, (255, 255, 255))
            screen.blit(line_surface, (200, y))
            y += 25 

        #Enter to continue
        t = pygame.time.get_ticks() / 200  # speed of oscillation
        dx = int(10 * math.sin(t))         # oscillation distance

        enter_x = width - enterText.get_width() - 2 * arrow_size - arrow_gap - 50 + dx
        enter_y = 720
        screen.blit(enterText, (enter_x, enter_y))

        arrow_y = enter_y + enterText.get_height() // 2
        arrow1 = [
            (enter_x + enterText.get_width() + 10, arrow_y - arrow_size // 2),
            (enter_x + enterText.get_width() + 10, arrow_y + arrow_size // 2),
            (enter_x + enterText.get_width() + 10 + arrow_size, arrow_y)
        ]
        pygame.draw.polygon(screen, arrow_color, arrow1)
        arrow2 = [
            (enter_x + enterText.get_width() + 10 + arrow_size + arrow_gap, arrow_y - arrow_size // 2),
            (enter_x + enterText.get_width() + 10 + arrow_size + arrow_gap, arrow_y + arrow_size // 2),
            (enter_x + enterText.get_width() + 10 + 2 * arrow_size + arrow_gap, arrow_y)
        ]
        pygame.draw.polygon(screen, arrow_color, arrow2)

        pygame.display.flip()
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return