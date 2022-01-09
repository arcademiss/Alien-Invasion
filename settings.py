class Settings:
    """This is a class for game settings"""

    def __init__(self):
        """Initialise the game's settings"""
        # Static settings
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # Ship settings
        self.ship_limit = 3
        # Bullet settings
        self.bullet_width = 12
        self.bullet_height = 20
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        # Alien settings
        self.fleet_drop_speed = 10
        # How quickly the game speeds up
        self.speedup_scale = 1.1
        # Rate at wich alien hit gives more points
        self.score_increase = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialized dynamic settings"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        # 1 means fleet moves to the right -1 to the left
        self.fleet_direction = 1
        self.alien_points = 10

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_increase)
