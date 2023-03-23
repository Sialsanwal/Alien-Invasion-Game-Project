class Settings:
    """ A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game statics setting"""
        # screen setting
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Ship setting

        self.ship_limit = 3

        # Bullet Settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullet_allowed = 3

        # Alien Settings

        self.fleet_drop_speed = 10


        # How fast the game speed up
        self.speedup_scale = 1.1
        self.initialize_dynamic_setting()

    def initialize_dynamic_setting(self):
        """Initialize setting that change throughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 1.5
        self.alien_speed = 1.0

        # fleet_direction of 1 represent right and -1 represent left
        self.fleet_direction = 1
        #Scoring
        self.alien_points = 50


    def increased_speed(self):
        """Increased speed setting."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale


