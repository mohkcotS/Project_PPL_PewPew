import math

def CheckCollision(Entity1, Entity2):
    for bullet in Entity1.bullets:
        dx = bullet.x - Entity2.x
        dy = bullet.y - Entity2.y
        distance = math.hypot(dx, dy)  # tính khoảng cách giữa 2 điểm

        if distance < (bullet.radius + Entity2.radius):
            Entity1.bullets.remove(bullet)
            return True  # Có va chạm
    return False  # Không có va chạm