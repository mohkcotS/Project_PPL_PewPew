import pygame

class HealthBar:
    def __init__(self, screen, width, height, x, y, player):
        self.screen = screen
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.player = player
        self.max_health = 3
        self.health = self.max_health
        self.health_bar_width = 150
        self.health_bar_height = 20

    def draw(self):
        # Draw the health bar background (gray)
        pygame.draw.rect(self.screen, (100, 100, 100), (self.x, self.y, self.health_bar_width, self.health_bar_height))
        # Calculate the width of the health bar based on current health
        health_width = (self.health / self.max_health) * self.health_bar_width
        # Draw the health bar (green if health > 1, red if health <= 1)
        health_color = (0, 255, 0) if self.health > 1 else (255, 0, 0)
        pygame.draw.rect(self.screen, health_color, (self.x, self.y, health_width, self.health_bar_height))
        # Draw border
        pygame.draw.rect(self.screen, (255, 255, 255), (self.x, self.y, self.health_bar_width, self.health_bar_height), 2)

    def take_damage(self):
        self.health -= 1
        if self.health < 0:
            self.health = 0

    def heal(self):
        self.health += 1
        if self.health > self.max_health:
            self.health = self.max_health