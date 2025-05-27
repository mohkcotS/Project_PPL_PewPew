from Entity.Buffs.buff_Freeze import BuffFreeze
from Entity.Buffs.buff_Lazer import BuffLazer
from Controller.direction import Direction 
import pygame
import random

def HandleBuff (command,ingame_buff_list, ingame_monster_list, player) :
    if(not command):
        return
    if "collect" in command:
        if "laserp" in command:
            player.laser_buff += 1
            for buff in ingame_buff_list:
                if isinstance(buff, BuffLazer):
                    ingame_buff_list.remove(buff)
                    break
        else:
            player.freeze_buff += 1
            for buff in ingame_buff_list:
                if isinstance(buff, BuffFreeze):
                    ingame_buff_list.remove(buff)
                    break
    elif "use" in command:
        if "heal" in command:
            if player.health < 3:
                player.health += 1
                player.heal_buff -= 3
        else:
            if "laser" in command:
                # if player.laser_buff < 3:
                #     return
                
                target_direction = None
                if "mleft" in command:
                    target_direction = "mleft"
                elif "mright" in command:
                    target_direction = "mright"
                elif "right" in command:
                    target_direction = "right"
                elif "left" in command:
                    target_direction = "left"
                elif "mid" in command:
                    target_direction = "mid"
                
                if target_direction:
                    player.laser_buff -= 3
                    
                    monsters_to_remove = [m for m in ingame_monster_list if m.direction == target_direction]
                    monster_killed = len(monsters_to_remove)
                    player.heal_buff += monster_killed
                    player.score += monster_killed

                    for monster in monsters_to_remove:
                        # if random.random() < 0.3: 
                            new_buff = random.choice([
                                BuffLazer(monster.x, monster.y, monster.direction),
                                BuffFreeze(monster.x, monster.y, monster.direction)
                            ])
                            ingame_buff_list.append(new_buff)

                    ingame_monster_list[:] = [m for m in ingame_monster_list if m.direction != target_direction]

                    laser_effect = BuffLazer(player.x, player.y, target_direction, is_effect=True)
                    ingame_buff_list.append(laser_effect)

            elif "freeze" in command:
                if player.freeze_buff <= 0:
                    return
                target_direction = None

                if "mleft" in command:
                    target_direction = "mleft"
                elif "mright" in command:
                    target_direction = "mright"
                elif "right" in command:
                    target_direction = "right"
                elif "left" in command:
                    target_direction = "left"
                elif "mid" in command:
                    target_direction = "mid"
                
                if target_direction:
                    player.freeze_buff -= 1

                    freeze_effect = BuffFreeze(player.x, player.y, target_direction, is_effect=True)
                    ingame_buff_list.append(freeze_effect)

                    freeze_duration = freeze_effect.freeze_duration
                    now = pygame.time.get_ticks()

                    for monster in ingame_monster_list:
                        if monster.direction == target_direction:
                            monster.freeze_until = now + freeze_duration
                            for bullet in getattr(monster, "bullets", []):
                                bullet.freeze_until = now + freeze_duration
    
    print(player.laser_buff, player.freeze_buff)
