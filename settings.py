class Settings:
    """This is a class for game settings"""

    def __init__(self):
        """Initialise the game's settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # Ship settings
        # Speed setting
        self.ship_speed = 1.4999999
        # Bullet settings
        self.bullet_speed = 0.9999999
        self.bullet_width = 12
        self.bullet_height = 20
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # 1 means the fleet is moving to the right -1 means left
        self.fleet_direction = 1
