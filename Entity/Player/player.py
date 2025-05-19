import pygame
from PIL import Image
from Entity.entity import Entity

class Player(Entity):
    def __init__(self, x=600, y=560, gif_path="src/assets/Player.gif", speed=5, score=0, direction="mid_player"):
        super().__init__(x, y, "true", (0, 0, 255), 30, speed, direction)
        self.score = score
        self.frames = self.load_gif_frames(gif_path)
        self.current_frame = 0
        self.frame_delay = 5  # Delay between frames (adjust as needed)
        self.frame_counter = 0
        self.laser_buff = 0
        self.freeze_buff = 0
        self.heal_buff = 0

    def load_gif_frames(self, gif_path):
        pil_gif = Image.open(gif_path)
        frames = []
        target_size = (150, 150)
        try:
            while True:
                frame = pil_gif.convert("RGBA")
                frame = frame.resize(target_size, Image.Resampling.LANCZOS)
                mode = frame.mode
                size = frame.size
                data = frame.tobytes()
                pygame_image = pygame.image.fromstring(data, size, mode)
                frames.append(pygame_image)
                pil_gif.seek(pil_gif.tell() + 1)
        except EOFError:
            pass
        return frames

    def update_animation(self):
        self.frame_counter += 1
        if self.frame_counter >= self.frame_delay:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.frame_counter = 0

    def draw(self, surface):
        self.update_animation()
        frame = self.frames[self.current_frame]
        rect = frame.get_rect(center=(self.x, self.y))
        surface.blit(frame, rect)
        self.draw_bullets(surface)