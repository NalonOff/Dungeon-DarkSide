import pygame
import Animation


class Entity(Animation.AnimateSprite):

    def __init__(self, sprite_name):
        super().__init__(sprite_name)

        self.velocity = 0.75
        self.pos = [10, 10]
        self.momentum = 0
        self.lastWay = 'right'
        self.moving_left = False
        self.moving_right = False
        self.moving_down = False
        self.moving_up = False

        self.rect = pygame.Rect(self.pos, self.image.get_size())
