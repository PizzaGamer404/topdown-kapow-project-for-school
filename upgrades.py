from character import Character, UpgradeBaseClase

class SidewaysDefense:
    def __init__(self, screen, player):
        super().__init__(screen, player)
    
    def update(self, room, x_input, y_input, is_pewing, delta_time):
