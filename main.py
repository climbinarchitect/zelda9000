import pygame
import os
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Zelda Inspired Adventure")
        self.clock = pygame.time.Clock()
        self.running = True

    def new(self):
        # initialiser et lancer un nouveau jeu
        pass

    def run(self):
        # boucle principale du jeu
        self.clock.tick(FPS)
        self.events()
        self.draw()
        pygame.display.flip()


    def events(self):
        # gérer les événements, tels que les mouvements du personnage, les collisions, etc.
        for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    self.running = False


    def draw(self):
        # dessiner les objets du jeu sur l'écran
        self.screen.fill(WHITE)

    def game_over(self):
        # afficher l'écran de fin de partie
        pass

    def victory(self):
        # afficher l'écran de victoire
        pass


if __name__ == "__main__":
    game = Game()
    game.new()
    while game.running:
        game.run()
    pygame.quit()
    sys.exit()
