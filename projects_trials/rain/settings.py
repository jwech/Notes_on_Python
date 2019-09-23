class Settings:
    '''Store settings of the game'''
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = 0, 0, 0

        self.fleet_direction = 1
        self.fleet_speed_factor = 1
        self.fleet_drop_factor = 10