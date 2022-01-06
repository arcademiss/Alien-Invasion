import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Class to manage bullets fired from the ship"""
    def __init__(self, ai_game):
        """Initializes a bullet"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = ai_game.settings.bullet_color
        self.rect = pygame.Rect(0, 0, ai_game.settings.bullet_width, ai_game.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        """Moves the bullet up the screen"""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Draws the bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
