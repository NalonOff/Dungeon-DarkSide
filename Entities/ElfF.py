import Entity
import pygame

class ElfF(Entity.Entity):

    def __init__(self):
        super().__init__('elf_f')

        self.health = 20
        self.attack = 2

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount

    def update_animation(self, action, way):
        self.animate(action, way)

    def update(self):
        if self.moving_left:
            self.pos[0] -= self.velocity
            self.update_animation('run', 'left')
            self.lastWay = 'left'
        if self.moving_right:
            self.pos[0] += self.velocity
            self.update_animation('run', 'right')
            self.lastWay = 'right'
        if self.moving_down:
            self.pos[1] += self.velocity
            self.update_animation('run', self.lastWay)
        if self.moving_up:
            self.pos[1] -= self.velocity
            self.update_animation('run', self.lastWay)






        if self.moving_left == False and self.moving_right == False and self.moving_up == False and self.moving_down == False:
            self.update_animation('idle', self.lastWay)

        self.rect = pygame.Rect(self.pos, self.image.get_size())
