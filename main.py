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
        map_layer.zoom = 2

        #generer un joueur
        player_position = tmx_data.get_object_by_name("player")
        self.player = Player(player_position.x, player_position.y)
        
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


    def events(self):
        # gérer les événements, tels que les mouvements du personnage, les collisions, etc.
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.player.moving_up = True
                elif event.key == pygame.K_DOWN:
                    self.player.moving_down = True
                elif event.key == pygame.K_LEFT:
                    self.player.moving_left = True
                elif event.key == pygame.K_RIGHT:
                    self.player.moving_right = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.player.moving_up = False
                elif event.key == pygame.K_DOWN:
                    self.player.moving_down = False
                elif event.key == pygame.K_LEFT:
                    self.player.moving_left = False
                elif event.key == pygame.K_RIGHT:
                    self.player.moving_right = False

    def draw(self):
        # dessiner les objets du jeu sur l'écran
        self.group.update()
        self.group.center(self.player.rect.center)
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
