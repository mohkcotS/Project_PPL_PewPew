import pygame
import math


def show_syntax_screen(screen, width, height, clock):
    text_font = pygame.font.Font("src/assets/font/SpaceMonoB.ttf", 28)
    text_font1 = pygame.font.Font("src/assets/font/SpaceMonoB.ttf", 20)
    text_font2 = pygame.font.Font("src/assets/font/SpaceMonoB.ttf", 16)

    background = pygame.image.load("src/assets/Space_Background.png")
    background = pygame.transform.scale(background, (width, height))

    color1 = (103, 232, 249)
    colorText = (255,255,255)
    colorTitle = (255,255,0)

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

    monster = pygame.image.load("src/assets/Ship1.png")
    monster = pygame.transform.scale(monster, (75, 75))
    monster = pygame.transform.rotate(monster, 180)
    monster_id = text_font2.render("Leo000", True, (255,255,255))

    shield = pygame.image.load("src/assets/Shield/shield.png")
    shield = pygame.transform.scale(shield, (75, 75))

    attack_Title = text_font1.render("ATTACK", True, colorTitle)
    attackInstruction = [
    "Syntax: attack <direction> <id>",
    "Ex: attack mid Leo000",
    "Kill enemy in specified direction"
    ]

    defend_Title = text_font1.render("DEFEND", True, colorTitle)
    defendInstruction = [
    "Syntax: defend <direction>",
    "Ex: defend mid",
    "Block a single enemy bullet from a",
    "specified direction."
    ]

    heal_Title = text_font1.render("HEAL", True, colorTitle)
    healInstruction = [
    "Syntax: use heal",
    "Recover 1 HP",
    ]

    buff_Title = text_font1.render("BUFF", True, colorTitle)
    buffInstruction = [
    "Syntax: collect <buff>",
    "Ex: collect laserP",
    "Pick up buffs dropped after",
    "defeating enemies."
    ]

    skill_Title = text_font1.render("SKILL", True, colorTitle)
    skillInstruction = [
    "Syntax: use <skill>  <direction>",
    "Ex: use laser mid",
    "Activate skill in specified",
    "direction."
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
        screen.blit(monster, ((50, y)))
        screen.blit(monster_id, ((50 + (75 - monster_id.get_width())// 2, y+80)))
        screen.blit(attack_Title, (150, 200))
        screen.blit(shield, ((650, y)))
        screen.blit(defend_Title, (750, 200))


        y = 225
        for line in attackInstruction:
            line_surface = text_font1.render(line, True, (colorText))
            screen.blit(line_surface, (150, y))
            y += 25
         
        y = 225
        for line in defendInstruction:
            line_surface = text_font1.render(line, True, (colorText))
            screen.blit(line_surface, (750, y))
            y += 25 
        

        y = 375
        screen.blit(laserP, ((50, y)))
        screen.blit(freezeP, ((50, y+100)))
        screen.blit(laserSkill, ((650, y)))
        screen.blit(freezeSkill, ((650, y+100)))

        y = 400
        screen.blit(buff_Title, (150, y))
        screen.blit(skill_Title, (750, y))
       
        y = 425
        for line in buffInstruction:
            line_surface = text_font1.render(line, True, (colorText))
            screen.blit(line_surface, (150, y))
            y += 25 

        y= 425
        for line in skillInstruction:
            line_surface = text_font1.render(line, True, (colorText))
            screen.blit(line_surface, (750, y))
            y += 25 

        y = 600 
        screen.blit(heal, ((50, y)))
        screen.blit(heal_Title, (150, y))

        y = 625
        for line in healInstruction:
            line_surface = text_font1.render(line, True, (colorText))
            screen.blit(line_surface, (150, y))
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