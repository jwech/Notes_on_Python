class Settings():
    '''Store all settings of Alien Invasion'''

    def __init__(self):
        '''Initialize settings'''
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 650
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 2
        self.ship_limit = 2

        self.bullet_speed_factor = 1.5
        self.bullet_width = 300
        self.bullet_height = 10
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        self.alien_speed_factor = 0.5
        self.fleet_drop_speed = 30
        # 1 means right, -1 means left
        self.fleet_direction = 1

        self.speed_scale = 1.1
        self.initialize_dymatic_settings()

        self.alien_points = 50
    
    def initialize_dymatic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        # 1 means move right
        self.fleet_direction = 1
    
    def increase_speed(self):
        self.ship_speed_factor *= self.speed_scale
        self.bullet_speed_factor *= self.speed_scale
        self.alien_speed_factor *= self.speed_scale
        