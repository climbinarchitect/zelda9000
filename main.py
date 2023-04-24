import pygame
import os
import sys
import pytmx
import pyscroll
from player import Player

pygame.init()

        
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
FPS = 60

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Zelda Inspired Adventure")
        self.clock = pygame.time.Clock()
        self.running = True
        
        # charger la carte (tmx)
        tmx_data = pytmx.util_pygame.load_pygame('monde.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 1

        #generer un joueur
        self.player = Player(100, 80)

        # dessiner le groupe de calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=3)
        self.group.add(self.player)

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
        self.group.draw(self.screen)
        pygame.display.flip()


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
