import math
from Entity.Shield.shield import Shield
from Entity.Player.player import Player
from Entity.Monster.monster import Monster

def CheckCollision(Entity1, Entity2):
    # Case 1: Collision between Monster and Player (direct collision only)
    if isinstance(Entity1, Monster) and isinstance(Entity2, Player):
        dx = Entity1.x - Entity2.x
        dy = Entity1.y - Entity2.y
        distance = math.hypot(dx, dy)
        if distance < (Entity1.radius + Entity2.radius):
            return True
        return False

    # Case 2: Collision between Bullet and Player or Shield
    if hasattr(Entity1, 'is_bullet'):  # Check if Entity1 has is_bullet attribute
        if Entity1.is_bullet:  # Check if Entity1 is a bullet
            dx = Entity1.x - Entity2.x
            dy = Entity1.y - Entity2.y
            distance = math.hypot(dx, dy)

            if distance < (Entity1.radius + Entity2.radius):
                # Bullet from player hitting a monster
                if Entity1.isPlayer == "true" and isinstance(Entity2, Monster):
                    if Entity1.name == Entity2.name:
                        return True
                # Bullet hitting a shield
                elif isinstance(Entity2, Shield):
                    if Entity1.direction == Entity2.direction:
                        return True
                # Bullet from monster hitting player
                elif isinstance(Entity2, Player) and Entity1.isPlayer != "true":
                    return True

    return False