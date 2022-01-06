import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class describing an alien"""
    def __init__(self, ai_game):
        """Initialises an instance of alien"""
        super().__init__()
        self.screen = ai_game.screen

        # Load the image of alien
        self.image = pygame.image.load('image/alien.bmp')
        self.rect = self.image.get_rect()

        # Spawn an alien at the top of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the aliens horizontal position with precision
        self.x = float(self.rect.x)
