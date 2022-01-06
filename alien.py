import pygame
from pygame.sprite import Sprite
from settings import Settings


class Alien(Sprite):
    """A class describing an alien"""
    def __init__(self, ai_game):
        """Initialises an instance of alien"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        # Load the image of alien
        self.image = pygame.image.load('image/alien.bmp')
        self.rect = self.image.get_rect()

        # Spawn an alien at the top of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the aliens horizontal position with precision
        self.x = float(self.rect.x)

    def update(self):
        """Move them to the right"""
        self.x += (self.settings.fleet_direction * self.settings.alien_speed)
        self.rect.x = self.x

    def check_edges(self):
        """Checks if alien is inside the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
