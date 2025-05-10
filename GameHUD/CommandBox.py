import pygame

class CommandBox:
    def __init__(self, screen, width, height, y_position):
        self.screen = screen
        self.width = width
        self.height = height
        self.y_position = y_position  # Vị trí y của khung chat (dưới đường kẻ ngang)

        self.CHAT_HEIGHT = 50
        self.CHAT_WIDTH = width // 3  # Chiếm 1/3 chiều rộng màn hình (chính giữa)
        self.chat_frame = pygame.Rect((width - self.CHAT_WIDTH) // 2, self.y_position, self.CHAT_WIDTH, self.CHAT_HEIGHT)
        print(f"y_position: {self.y_position}, chat_frame: {self.chat_frame}")
        self.chat_color = (100, 100, 100)  # Màu xám
        self.font = pygame.font.Font(None, 36)
        self.input_text = ""

    def handle_input(self, event):
        """Handle keyboard input for the command box."""
        if event.type == pygame.TEXTINPUT:
                self.input_text += event.text  # Thêm ký tự vào input_text
                print("Text input:", event.text)
                return None

        if event.type == pygame.KEYDOWN:
            print("Key pressed:", pygame.key.name(event.key))
            if event.key == pygame.K_RETURN:
                command = self.input_text.strip()  # Lấy lệnh và loại bỏ khoảng trắng thừa
                self.input_text = ""  # Xóa nội dung sau khi nhấn Enter
                return command 
            elif event.key == pygame.K_BACKSPACE:
                self.input_text = self.input_text[:-1]  # Xóa ký tự cuối cùng
            return None

    def draw(self):
        """Draw the command box and its text on the screen."""
        pygame.draw.rect(self.screen, self.chat_color, self.chat_frame)
        # text_surface = self.font.render(self.input_text, True, (255, 255, 255))
        # text_position = (self.chat_frame.x + 5, self.chat_frame.y + 5)
        # self.screen.blit(text_surface, text_position)
        if self.input_text:
            text_surface = self.font.render(self.input_text, True, (255, 255, 255))
            text_position = (self.chat_frame.x + 5, self.chat_frame.y + 5)
            self.screen.blit(text_surface, text_position)
            print(f"Drawing text '{self.input_text}' at {text_position}")
        else:
            print("No text to draw")