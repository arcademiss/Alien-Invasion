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
        self.ship_speed = 1.00000005
        # Bullet settings
        self.bullet_speed = 0.999995
        self.bullet_width = 5
        self.bullet_height = 20
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
