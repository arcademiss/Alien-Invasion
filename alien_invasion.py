import pygame
from ship import Ship
import sys
from bullet import Bullet
from settings import Settings


class AlienInvasion:
    """Overall class to manage behavior of game"""
    def __init__(self):
        """Initialize the game and create resources"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (0, 0), pygame.FULLSCREEN
        )
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Start the game loop"""
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._delete_bullet(self.bullets.copy())
            self._update_screen()

    def _check_events(self):
        """Listens for mouse and keyboard inputs"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Checks for button presses"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Checks for releasing buttons"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Creating a bullet and firing it"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_screen(self):
        """Updates the screen"""
        # Colors the screen with self.bgcolor for each iteration
        self.screen.fill(self.settings.bg_color)
        # Display ship
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # Displays the last drawn screen
        pygame.display.flip()

    def _delete_bullet(self, bullets):
        """Deletes a bullet"""
        for bullet in bullets:
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)


if __name__ == '__main__':
    # Make an instance of a game
    ai = AlienInvasion()
    ai.run_game()
