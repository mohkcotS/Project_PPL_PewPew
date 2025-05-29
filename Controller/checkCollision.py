import math
from Entity.Shield.shield import Shield
from Entity.Player.player import Player
from Entity.Monster.monster import Monster

def CheckCollision(Entity1, Entity2):
    if(isinstance(Entity1,Monster) and isinstance(Entity2,Player)):
        dx = Entity1.x - Entity2.x
        dy = Entity1.y - Entity2.y
        distance = math.hypot(dx, dy)
        if distance < (Entity1.radius + Entity2.radius):
            return True

    for bullet in Entity1.bullets[:]:  
        dx = bullet.x - Entity2.x
        dy = bullet.y - Entity2.y
        distance = math.hypot(dx, dy)

        if distance < (bullet.radius + Entity2.radius):
            if Entity1.isPlayer == "true":
                if bullet.name == Entity2.name and bullet.direction.value == Entity2.direction:
                    Entity1.bullets.remove(bullet)
                    return True
            elif isinstance(Entity2, Shield):
                if Entity1.direction == Entity2.direction:
                    Entity1.bullets.remove(bullet)
                    return True
            else:
                if Entity2.health > 0:
                    Entity2.health -= 1
                    Entity1.bullets.remove(bullet)

    return False