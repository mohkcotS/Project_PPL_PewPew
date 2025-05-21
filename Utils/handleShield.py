from Entity.Shield.shield import Shield

def HandleShield(command, ingame_shield_list ):
    """Handle commands entered through the command box."""
    if not command:
        return  # Không xử lý nếu lệnh rỗng

    if "defend" in command:
        if "mleft" in command:
            ingame_shield_list.append(Shield(direction = 'mleft'))
        elif "mright" in command:
            ingame_shield_list.append(Shield(direction = 'mright'))       
        elif "right" in command:
            ingame_shield_list.append(Shield(direction = 'right'))
        elif "left" in command:
            ingame_shield_list.append(Shield(direction = 'left'))
        elif "mid" in command:
            ingame_shield_list.append(Shield(direction = 'mid'))

    
    