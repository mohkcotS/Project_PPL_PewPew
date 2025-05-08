import pygame
from Entity.Player.player import Player
from Entity.Monster.monster import Monster
pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Quái vật hướng đối tượng")

clock = pygame.time.Clock()

player = Player(320, 450)
monster = Monster(320,0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0, 0, 0))  # nền đen
    player.draw(screen)
    monster.draw(screen)
    monster.move()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
