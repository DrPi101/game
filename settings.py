class Settings():
    """a class to store all settings"""
    def __init__(self):
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (230,230,230)

        #ship settings
        self.ship_speed_factor = 1.5

        # bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 4
        self.bullet_height = 15
        self.bullet_color = 60,60,60
