import math

def CheckCollision(Entity1, Entity2):
    for bullet in Entity1.bullets[:]:  # duyệt bản sao để tránh lỗi khi remove
        dx = bullet.x - Entity2.x
        dy = bullet.y - Entity2.y
        distance = math.hypot(dx, dy)

        if distance < (bullet.radius + Entity2.radius):
            if Entity1.isPlayer == "true":
                if bullet.name == Entity2.name:
                    Entity1.bullets.remove(bullet)
                    return True
            else:
                return True

    return False
