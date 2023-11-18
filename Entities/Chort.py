import Entity

class Chort(Entity.Entity):

    def __init__(self):
        super().__init__('chort')

        self.health = 8
        self.attack = 1.5

        self.pos = [30, 40]

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount

    def update_animation(self, action, way):
        self.animate(action, way)
    def update(self):
        if self.moving_left == False and self.moving_right == False and self.moving_left == False and self.moving_right == False:
            self.update_animation('idle', self.lastWay)
