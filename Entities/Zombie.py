import Entity

class Zombie(Entity.Entity):

    def __init__(self):
        super().__init__('zombie')

        self.health = 20
        self.attack = 3

        self.pos = [20, 30]

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount

    def update_animation(self, action, way):
        self.animate(action, way)

    def update(self):
        if self.moving_left and self.moving_up:
            self.pos[0] -= self.velocity / 1.5
            self.pos[1] -= self.velocity / 1.5
            self.lastWay = 'left'
            self.update_animation('run', self.lastWay)
        elif self.moving_right and self.moving_up:
            self.pos[0] += self.velocity / 1.5
            self.pos[1] -= self.velocity / 1.5
            self.lastWay = 'right'
            self.update_animation('run', self.lastWay)
        elif self.moving_left and self.moving_down:
            self.pos[0] -= self.velocity / 1.5
            self.pos[1] += self.velocity / 1.5
            self.lastWay = 'left'
            self.update_animation('run', self.lastWay)
        elif self.moving_right and self.moving_down:
            self.pos[0] += self.velocity / 1.5
            self.pos[1] += self.velocity / 1.5
            self.lastWay = 'right'
            self.update_animation('run', self.lastWay)
        elif self.moving_left:
            self.pos[0] -= self.velocity
            self.update_animation('run', 'left')
            self.lastWay = 'left'
        elif self.moving_right:
            self.pos[0] += self.velocity
            self.update_animation('run', 'right')
            self.lastWay = 'right'
        elif self.moving_down:
            self.pos[1] += self.velocity
            self.update_animation('run', self.lastWay)
        elif self.moving_up:
            self.pos[1] -= self.velocity
            self.update_animation('run', self.lastWay)


        elif self.moving_left == False and self.moving_right == False and self.moving_up == False and self.moving_down == False:
            self.update_animation('idle', self.lastWay)

        self.rect = pygame.Rect(self.pos, self.image.get_size())
