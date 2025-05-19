import pygame

class RulesBox:
    def __init__(self, screen, width, height, y_position, command_box_width):
        self.screen = screen
        self.width = width
        self.height = height
        self.y_position = y_position

        self.RULES_WIDTH = width // 4
        self.RULES_HEIGHT = 275

        # Position to the right of CommandBox
        command_box_right = (width - command_box_width) // 2 + command_box_width
        self.rules_frame = pygame.Rect(command_box_right + 70, self.y_position-50, self.RULES_WIDTH, self.RULES_HEIGHT)

        # Colors and font
        self.rules_color = (24, 45, 47)  # BACKGROUND FRAME
        self.border_color = (80, 140, 150)  # BORDER COLOR
        self.text_color = (255,255,255)  # TEXT COLOR
        self.font = pygame.font.Font(None, 24)

        # Game rules
        self.rules = [
            "Available direction:",
            "• left,  mleft,  mid,  mright,  right",
            "",
            "Available buff and buff piece:",
            "• laser,  freeze,  laserP,  freezeP",
            "",
            "Available commands:",
            "• attack <direction> <ID>",
            "• defend <direction>",
            "• use heal",
            "• use <skill> <direction>",
            "• collect <buff>",
        ]

    def draw(self):
        # Draw border
        shadow_rect = self.rules_frame.inflate(8, 8)
        pygame.draw.rect(self.screen, self.border_color, shadow_rect)

        # Draw background
        pygame.draw.rect(self.screen, self.rules_color, self.rules_frame)

        # Draw rules text (multi-line)
        for i, line in enumerate(self.rules):
            text_surface = self.font.render(line, True, self.text_color)
            self.screen.blit(
                text_surface,
                (self.rules_frame.x + 20, self.rules_frame.y + 12 + i * 21),
            )
