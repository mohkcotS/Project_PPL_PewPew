import pygame
from Entity.Player.player import Player
from Entity.Monster.rightMonster import RightMonster
from Entity.Monster.midRightMonster import MidRightMonster
from Entity.Monster.midMonster import MidMonster
pygame.init()
pygame.display.set_caption("Quái vật hướng đối tượng")
clock = pygame.time.Clock()

width = 800
height = 600

start_pos = (0, (4/5)*height)  # Vị trí bắt đầu (x, y)
end_pos = (width, (4/5) *height)    # Vị trí kết thúc (x, y)
line_color = (255, 255, 255)  # white
line_width = 3 

screen = pygame.display.set_mode((width, height))
        

player = Player()
monster1 = RightMonster()
monster2 = MidRightMonster()
monster3 = MidMonster()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0, 0, 0))  # nền đen


    pygame.draw.line(screen, line_color, start_pos, end_pos, line_width)
    player.draw(screen)
    monster1.draw(screen)
    monster1.move()
    monster2.draw(screen)
    monster2.move()
    monster3.draw(screen)
    monster3.move()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
