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

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Controlla eventi della tastiera ed del mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Ricolora lo schermo durante ogni loop.
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # Aggiorna lo schermo
            pygame.display.flip()


if __name__ == '__main__':
    # Crea una istanza del gioco, e avvia il gioco.
    ai = AlienInvasion()
    ai.run_game()
