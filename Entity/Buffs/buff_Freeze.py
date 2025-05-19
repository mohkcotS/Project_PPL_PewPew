import pygame
from Entity.Buffs.buff import Buff

class BuffFreeze(Buff):
    def __init__(self, x, y, direction):
        super().__init__(x, y, direction, buff_type="freeze", image_path="src/assets/Buffs/Freeze.png")