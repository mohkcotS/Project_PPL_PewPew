import pygame

class StatsBox:
    def __init__(self, screen, width, height, y_position, command_box_width, player):
        self.screen = screen
        self.width = width
        self.height = height
        self.y_position = y_position
        self.player = player

        # Kích thước khung StatsBox (giảm chiều cao)
        self.STATS_WIDTH = width // 5 + 50
        self.STATS_HEIGHT = 120

        # Vị trí khung
        command_box_left = (width - command_box_width) // 2
        self.stats_frame = pygame.Rect(command_box_left - self.STATS_WIDTH - 70, self.y_position - 37, self.STATS_WIDTH, self.STATS_HEIGHT)

        # Màu sắc và font chữ
        self.stats_color = (24, 45, 47)
        self.border_color = (80, 140, 150)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.Font(None, 28)

        # Tải hình ảnh cho chiêu thức
        self.heal_image = pygame.image.load("src/assets/Buffs/Heal.png")
        self.laser_image = pygame.image.load("src/assets/Buffs/Laser.png")
        self.freeze_image = pygame.image.load("src/assets/Buffs/Freeze.png")

        # Điều chỉnh kích thước hình ảnh
        self.heal_image = pygame.transform.scale(self.heal_image, (40, 40))
        self.laser_image = pygame.transform.scale(self.laser_image, (40, 40))
        self.freeze_image = pygame.transform.scale(self.freeze_image, (40, 40))

    def draw(self):
        # Vẽ viền
        shadow_rect = self.stats_frame.inflate(8, 8)
        pygame.draw.rect(self.screen, self.border_color, shadow_rect)

        # Vẽ nền
        pygame.draw.rect(self.screen, self.stats_color, self.stats_frame)

        # Vẽ điểm số từ player
        points_text = f"Score: {self.player.score}"
        text_surface = self.font.render(points_text, True, self.text_color)
        self.screen.blit(text_surface, (self.stats_frame.x + 20, self.stats_frame.y + 12))

        # Khoảng cách ngang giữa các chiêu
        skill_spacing = self.STATS_WIDTH // 3
        skill_y_offset = self.stats_frame.y + 65

        # Heal (bố cục ngang)
        heal_opacity = 1.0 if self.player.heal_buff >= 3 else 0.5
        heal_surface = self.heal_image.copy()
        heal_surface.set_alpha(int(heal_opacity * 255))
        self.screen.blit(heal_surface, (self.stats_frame.x + 25, skill_y_offset))
        self._draw_usage_circle(self.stats_frame.x + 50, skill_y_offset, self.player.heal_buff)

        # Laser
        laser_opacity = 1.0 if self.player.laser_buff >= 3 else 0.5
        laser_surface = self.laser_image.copy()
        laser_surface.set_alpha(int(laser_opacity * 255))
        self.screen.blit(laser_surface, (self.stats_frame.x + 25 + skill_spacing, skill_y_offset))
        self._draw_usage_circle(self.stats_frame.x + 50 + skill_spacing, skill_y_offset, self.player.laser_buff)

        # Freeze
        freeze_opacity = 1.0 if self.player.freeze_buff >= 3 else 0.5
        freeze_surface = self.freeze_image.copy()
        freeze_surface.set_alpha(int(freeze_opacity * 255))
        self.screen.blit(freeze_surface, (self.stats_frame.x + 25 + 2 * skill_spacing, skill_y_offset))
        self._draw_usage_circle(self.stats_frame.x + 50 + 2 * skill_spacing, skill_y_offset, self.player.freeze_buff)

    def _draw_usage_circle(self, x, y, count):
        # Tính số lần sử dụng dựa trên số lượng thu thập
        usage = 0
        if count >= 6:
            usage = 2
        elif count >= 3:
            usage = 1

        # Vẽ khung tròn đỏ
        pygame.draw.circle(self.screen, (255, 0, 0), (x + 20, y), 10)
        # Vẽ số lần sử dụng trong khung tròn
        usage_text = self.font.render(str(usage), True, (255, 255, 255))
        text_rect = usage_text.get_rect(center=(x + 20, y))
        self.screen.blit(usage_text, text_rect)