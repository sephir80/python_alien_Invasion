import sys

import pygame


class AlienInvasion:
    """Classe generale per gestire le risorse e il comportamento del gioco """

    def __init__(self):
        """Inizializza il gioco, e crea le risorse del gioco """
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Controlla eventi della tastiera ed del mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Aggiorna lo schermo
            pygame.display.flip()


if __name__ == '__main__':
    # Crea una instanza del gioco, e avvia il gioco.
    ai = AlienInvasion()
    ai.run_game()
