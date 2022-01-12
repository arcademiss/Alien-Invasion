import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """This clas will handle the behavior of a ship"""
    def __init__(self, ai_game):
        """Initialise the ship and its starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Load ship image by rect
        self.image = pygame.image.load('image/ship.bmp')
        self.rect = self.image.get_rect()

        # Set ship init position at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Set a flag for moving right/left
        self.moving_right = False
        self.moving_left = False

        # Store the x and y atributes
        self.x = float(self.rect.x)

    def ship_center(self):
        """Centers the ship"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def update(self):
        """Update the ship's position based on the movement of flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        # Update the position of the rectangle
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its last known location"""
        self.screen.blit(self.image, self.rect)
