class GameStats:
    """Track statistics for alien invasion"""
    def __init__(self, ai_game):
        """Initialises statistics"""
        self.settings = ai_game.settings
        self.reset_stats()
        self.active_game = True

    def reset_stats(self):
        """Initialises statistics that can change during game"""
        self.ships_left = self.settings.ship_limit
