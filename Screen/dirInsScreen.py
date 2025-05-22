import pygame
from PIL import Image
import math

def load_gif_frames(gif_path, target_size=(150, 150)):
    pil_gif = Image.open(gif_path)
    frames = []
    try:
        while True:
            frame = pil_gif.convert("RGBA")
            frame = frame.resize(target_size, Image.Resampling.LANCZOS)
            mode = frame.mode
            size = frame.size
            data = frame.tobytes()
            pygame_image = pygame.image.fromstring(data, size, mode)
            frames.append(pygame_image)
            pil_gif.seek(pil_gif.tell() + 1)
    except EOFError:
        pass
    return frames

def show_direction_screen(screen, width, height, clock):
    font = pygame.font.SysFont(None, 55)
    title_font = pygame.font.SysFont(None, 40)
    text_font = pygame.font.Font("src/assets/font/SpaceMonoB.ttf", 28)

    background = pygame.image.load("src/assets/Space_Background.png")
    background = pygame.transform.scale(background, (width, height))

    color1 = (103, 232, 249)

    instruction_text = pygame.image.load("src/assets/InstructionScreen/instruction.png")
    instruction_text = pygame.transform.scale(instruction_text, (500,500))

    #Direction
    leftDirText = text_font.render("left", True, (color1))
    mleftDirText = text_font.render("mleft", True, (color1))
    rightDirText = text_font.render("right", True, (color1))
    mrightDirText = text_font.render("mright", True, (color1))
    midDirText = text_font.render("mid", True, (color1))
    playerText = text_font.render("Player",True,(255,255,255))

    # Load GIF frames
    player_frames = load_gif_frames("src/assets/Player.gif", target_size=(150, 150))
    player_frame_count = len(player_frames)
    player_frame_idx = 0
    player_frame_delay = 4 
    player_frame_counter = 0

    #Bullet
    bullet = pygame.image.load("src/assets/Bullet/02.png")
    bulletLeft = pygame.transform.rotate(bullet,46)
    bulletMLeft = pygame.transform.rotate(bullet,33)
    bulletMid = pygame.transform.rotate(bullet, 0)
    bulletMRight = pygame.transform.rotate(bullet, -33)
    bulletRight = pygame.transform.rotate(bullet, -46)

    #Enter to continue
    enterText = text_font.render("ENTER", True, (color1))
    arrow_color = color1
    arrow_size = 22 
    arrow_gap = 8  

    while True:
        screen.blit(background, (0, 0)) # nền đen

        #Instruction
        y = 40
        screen.blit(instruction_text, ((width - instruction_text.get_width()) // 2, -150))

        #Direction
        y = 200
        screen.blit(leftDirText, (40, y))
        screen.blit(mleftDirText, ((600-mleftDirText.get_width())//2, y))
        screen.blit(midDirText, ((width-midDirText.get_width())//2, y))
        screen.blit(mrightDirText, (600 + (600-mrightDirText.get_width())//2, y))
        screen.blit(rightDirText, (1090, y))

        #Player
        player_frame_counter += 1
        if player_frame_counter >= player_frame_delay:
            player_frame_idx = (player_frame_idx + 1) % player_frame_count
            player_frame_counter = 0
        player_img = player_frames[player_frame_idx]
        screen.blit(player_img, ((width- player_img.get_width())// 2 ,560 ))

        screen.blit(playerText, ((width- playerText.get_width())// 2 , 720 ))

        #Bullet
        screen.blit(bulletLeft, (150 ,300))
        screen.blit(bulletMLeft, (380 ,375))
        screen.blit(bulletMid, (580 ,450))
        screen.blit(bulletMRight, (720 ,375))
        screen.blit(bulletRight, (1000 ,300))

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