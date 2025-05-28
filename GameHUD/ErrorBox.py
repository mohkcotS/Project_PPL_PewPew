import pygame

class ErrorBox:
    def __init__(self, screen, width, height, y_position, stats_box_width):
        self.screen = screen
        self.width = width
        self.height = height
        self.y_position = y_position
        self.error_message = ""
        self.show_error = False
        self.error_duration = 2000  # Thời gian hiển thị lỗi (ms)
        self.last_error_time = 0

        # Kích thước và vị trí của ErrorBox
        self.ERROR_WIDTH = stats_box_width
        self.ERROR_HEIGHT = 30

        # Căn chỉnh ErrorBox dựa trên vị trí của StatsBox
        command_box_left = (width - stats_box_width) // 2
        self.error_frame = pygame.Rect(command_box_left - self.ERROR_WIDTH - 84, y_position - self.ERROR_HEIGHT - 50, self.ERROR_WIDTH, self.ERROR_HEIGHT)
        
        # Màu sắc và font chữ
        self.error_color = (255, 0, 0)  # Màu đỏ cho lỗi
        self.border_color = (150, 0, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.Font("src/assets/font/SpaceMonoB.ttf", 20)

    def set_error(self, message):
        self.error_message = message
        self.show_error = True
        self.last_error_time = pygame.time.get_ticks()

    def draw(self):
        if self.show_error:
            current_time = pygame.time.get_ticks()
            if current_time - self.last_error_time > self.error_duration:
                self.show_error = False
            else:
                # Vẽ viền
                shadow_rect = self.error_frame.inflate(4, 4)
                pygame.draw.rect(self.screen, self.border_color, shadow_rect)

                # Vẽ nền
                pygame.draw.rect(self.screen, self.error_color, self.error_frame)

                # Vẽ thông báo lỗi
                text_surface = self.font.render(self.error_message, True, self.text_color)
                text_rect = text_surface.get_rect()
                
                y_position = self.error_frame.centery - (text_rect.height // 2) - 3  # Nâng văn bản lên 3px từ bottom
                x_position = self.error_frame.left + (self.ERROR_WIDTH - text_rect.width) // 2  # Căn giữa theo chiều ngang
                self.screen.blit(text_surface, (x_position, y_position))