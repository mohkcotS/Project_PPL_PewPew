import pygame
pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Quái vật hướng đối tượng")

clock = pygame.time.Clock()

# Định nghĩa lớp Monster
class Monster:
    def __init__(self, x, y, color=(0, 255, 0), radius=30, speed=2):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.speed = speed

    def move(self):
        self.x += self.speed  # Di chuyển sang phải

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)

# Tạo một con quái
monster = Monster(50, 200)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    monster.move()

    screen.fill((0, 0, 0))  # nền đen
    monster.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
