import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.sprite_sheet = pygame.image.load('player.jpg')
        self.image = self.get_image(0, 0)
        self.image.set_colorkey([255, 255, 255])
        self.rect = self.image.get_rect()
        self.position = [x, y]
        self.animations = {
            'down': self.get_image(0, 0),
            'left': self.get_image(0, 64),
            'right': self.get_image(0, 130),
            'up': self.get_image(0, 192)
        }
        
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False


    def update(self):
        if self.moving_up:
            self.position[1] -= 1
        if self.moving_down:
            self.position[1] += 1
        if self.moving_left:
            self.position[0] -= 1
        if self.moving_right:
            self.position[0] += 1

        self.rect.topleft = self.position

    def get_image(self, x, y):
        image = pygame.Surface([64, 64])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 64, 64))
        return image
     
    
    def change_animation(self, name):
        self.image = self.animations[name]