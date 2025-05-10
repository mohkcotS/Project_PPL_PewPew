import pygame

class CommandBox:
    def __init__(self, screen, width, height, y_position):
        self.screen = screen
        self.width = width
        self.height = height
        self.y_position = y_position

        self.CHAT_HEIGHT = 48
        self.CHAT_WIDTH = width // 2.5

        self.chat_frame = pygame.Rect((width - self.CHAT_WIDTH) // 2, self.y_position, self.CHAT_WIDTH, self.CHAT_HEIGHT)

        self.chat_color = (24, 45, 47)          #BACKGROUND FRAME
        self.border_color = (80, 140, 150)       #BORDER COLOR
        self.text_color = (64, 255, 209)         #TEXT COLOR

        self.font = pygame.font.Font(None, 28) 

        self.input_text = ""
        self.cursor_visible = True
        self.last_cursor_toggle = pygame.time.get_ticks()
        
        # CURSOR TEXT TIME
        self.cursor_interval = 500  # ms

    def handle_input(self, event):
        # HANDLE INPUT FROM KEYBOARD
        if event.type == pygame.TEXTINPUT:
            self.input_text += event.text
        # HANDLE 'ENTER' AND 'BACKSPACE'
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                command = self.input_text.strip()
                self.input_text = ""
                return command
            elif event.key == pygame.K_BACKSPACE:
                self.input_text = self.input_text[:-1]
        return None

    def draw(self):
        now = pygame.time.get_ticks()
        if now - self.last_cursor_toggle >= self.cursor_interval:
            self.cursor_visible = not self.cursor_visible
            self.last_cursor_toggle = now

        # BORDER
        shadow_rect = self.chat_frame.inflate(8, 8)
        pygame.draw.rect(self.screen, self.border_color, shadow_rect)

        # BACKGROUND
        pygame.draw.rect(self.screen, self.chat_color, self.chat_frame)

        # TEXT
        display_text = self.input_text + ("|" if self.cursor_visible else "")
        text_surface = self.font.render(display_text, True, self.text_color)
        self.screen.blit(text_surface, (self.chat_frame.x + 12, self.chat_frame.y + 12))