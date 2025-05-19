from Entity.Buffs.buff_Freeze import BuffFreeze
from Entity.Buffs.buff_Lazer import BuffLazer

def HandleBuff (command,ingame_buff_list,player) :
    if(not command):
        return laser_buff,freeze_buff
    if "collect" in command:
        if "laserP" in command:
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
    
    print(player.laser_buff, player.freeze_buff)
