import sys

import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Classe generale per gestire le risorse e il comportamento del gioco """

    def __init__(self):
        """Inizializza il gioco, e crea le risorse del gioco """
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

    def _check_events(self):
        """Respond to keypress and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False


    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Ricolora lo schermo durante ogni loop.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # Aggiorna lo schermo
        pygame.display.flip()


    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Controlla eventi della tastiera ed del mouse
            self._check_events()
            self.ship.update()
            self._update_screen()



if __name__ == '__main__':
    # Crea una istanza del gioco, e avvia il gioco.
    ai = AlienInvasion()
    ai.run_game()
