from abc import ABC, abstractmethod

class Entity(ABC):  # Kế thừa từ ABC để thành lớp trừu tượng
    def __init__(self, x, y, color=(0, 255, 0)):
        self.x = x
        self.y = y
        self.color = color 

    @abstractmethod
    def draw(self, surface):
        pass  # Lớp con bắt buộc phải override