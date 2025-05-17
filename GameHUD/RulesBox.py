import pygame

class RulesBox:
    def __init__(self, screen, width, height, y_position, command_box_width):
        self.screen = screen
        self.width = width
        self.height = height
        self.y_position = y_position

        self.RULES_WIDTH = width // 3.6
        self.RULES_HEIGHT = 225

        # Position to the right of CommandBox
        command_box_right = (width - command_box_width) // 2 + command_box_width
        self.rules_frame = pygame.Rect(command_box_right + 70, self.y_position, self.RULES_WIDTH, self.RULES_HEIGHT)

        # Colors and font
        self.rules_color = (24, 45, 47)  # BACKGROUND FRAME
        self.border_color = (80, 140, 150)  # BORDER COLOR
        self.text_color = (64, 255, 209)  # TEXT COLOR
        self.font = pygame.font.Font(None, 24)

        # Game rules
        self.rules = [
            "Game Rules:",
            "1. attack <direction> <ID>",
            "   Directions: left, mleft, mid, mright, right",
            "   ID: e.g., Cap254",
            "2. defend <direction>",
            "3. use heal",
            "4. use <skill> <direction>",
            "   Skills: laser, freeze",
            "5. collect <buff>",
            "   Buffs: laserP, freezeP",
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
                (self.rules_frame.x + 12, self.rules_frame.y + 12 + i * 21),
            )
