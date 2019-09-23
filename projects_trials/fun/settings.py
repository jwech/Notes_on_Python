class Settings:

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.speed_factor = 2
        self.ship_limit = 2

        self.bullet_width = 300
        self.bullet_height = 10
        self.bullet_color = 60, 60, 60
        self.bullet_speed_factor = 1.5
        self.bullets_allowed = 100

        self.fleet_speed_factor = 1
        self.fleet_direction = 1
        self.fleet_drop_speed_factor = 100