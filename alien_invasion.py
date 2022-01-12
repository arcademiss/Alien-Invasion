import pygame
from ship import Ship
import sys
from bullet import Bullet
from settings import Settings
from alien import Alien
from time import sleep
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


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
        # Create stats and scoreboard
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        # Create button
        self.button = Button(self, "Play")

    def run_game(self):
        """Start the game loop"""
        while True:
            self._check_events()
            if self.stats.active_game:
                self.ship.update()
                self.bullets.update()
                self._update_bullet(self.bullets.copy())
                self._update_alien()
            else:
                self.stats.active_game = False
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
        elif event.key == pygame.K_p and not self.stats.active_game:
            self._start_game()
            self.sb.prep_score()
            self.sb.prep_ships()

    def _check_keyup_events(self, event):
        """Checks for releasing buttons"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Creating a bullet and firing it"""
        if len(self.bullets) < self.settings.bullets_allowed and self.stats.active_game:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _create_fleet(self):
        """Create a fleet of aliens"""
        # Make an alien
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        # Determine the number of available columns
        available_space_x = self.settings.screen_width - (2 * alien_width)
        alien_number_x = available_space_x // (2 * alien_width)
        # Determine the number of available rows
        ship_height = self.ship.rect.height
        available_space_y = self.settings.screen_height - (3 * alien_width) - ship_height
        number_rows = available_space_y // (2 * alien_height)
        # Create the alien fleet
        for row_number in range(number_rows):
            for alien_number in range(alien_number_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Create an alien"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """Respond to the fleet reaching an edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the fleet and change the moving direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_alien_bottom(self):
        """Checks if any aliens have reached the bottom of the screen"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # We treat this event as if the ship got hit
                self._ship_hit()
                break

    def _update_alien(self):
        """Move alien to the right"""
        self._check_fleet_edges()
        self.aliens.update()
        # Detect if an alien hits player ship
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        self._check_alien_bottom()

    def _ship_hit(self):
        """Respond to an alien hitting the ship"""
        # Decrement the number of ships left
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.sb.prep_ships()
        elif self.stats.ships_left <= 0:
            self.stats.active_game = False
            pygame.mouse.set_visible(True)
        # Delete aliens and bullets
        self.aliens.empty()
        self.bullets.empty()
        # Create a new fleet and recenter ship
        self._create_fleet()
        self.ship.ship_center()
        # Pause
        sleep(0.5)

    def _update_screen(self):
        """Updates the screen"""
        # Colors the screen with self.bgcolor for each iteration
        self.screen.fill(self.settings.bg_color)
        # Display ship
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # Draw score information
        self.sb.show_score()
        # Draw the button
        if not self.stats.active_game:
            self.button.draw_button()
        # Displays the last drawn screen
        pygame.display.flip()

    def _update_bullet(self, bullets):
        """Deletes an old bullet and removes the bullet+alien collision"""
        for bullet in bullets:
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collision()
        # If we have no aliens we spawn more
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            self.stats.level += 1
            self.sb.prep_level()

    def _check_bullet_alien_collision(self):
        """Check for collisions and if one is found delete bullet and alien"""
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True
        )
        if collisions:
            for alien in collisions.values():
                self.stats.score += (self.settings.alien_points * len(alien))
            self.sb.prep_score()
            self.sb.check_high_score()

    def _start_game(self):
        """Starts the game"""
        # Reset dynamic settings
        self.settings.initialize_dynamic_settings()
        # Hide mouse
        pygame.mouse.set_visible(False)
        # Reset game stats
        self.stats.reset_stats()
        self.stats.active_game = True
        # Remove any remaining aliens and bullets
        self.aliens.empty()
        self.bullets.empty()
        # Create new fleet and recenter ship
        self._create_fleet()
        self.ship.ship_center()


if __name__ == '__main__':
    # Make an instance of a game
    ai = AlienInvasion()
    ai.run_game()
