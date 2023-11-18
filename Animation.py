import pygame

class AnimateSprite(pygame.sprite.Sprite):

    def __init__(self, sprite_name):
        super().__init__()
        self.image = pygame.image.load(f'assets/textures/entity/{sprite_name}/{sprite_name}_idle_anim_f0.png')
        self.idleFrame = 0
        self.runFrame = 5
        self.images = animations.get(sprite_name)
        self.clock = 0

    def animate(self, action, way):
        if self.clock == 20:

            if action == 'idle':
                self.idleFrame += 1
                if self.idleFrame >= 4:
                    self.idleFrame = 0
                if way == 'right':
                    self.image = self.images[self.idleFrame]
                elif way == 'left':
                    self.image = pygame.transform.flip(self.images[self.idleFrame], True, False)

            elif action == 'run':
                self.runFrame += 1
                if self.runFrame >= 8:
                    self.runFrame = 4
                if way == 'right':
                    self.image = self.images[self.runFrame]
                elif way == 'left':
                    self.image = pygame.transform.flip(self.images[self.runFrame], True, False)

            self.clock = 0

        self.clock += 1

def load_animation_images(sprite_name, action):
    images = []
    path = f'assets/textures/entity/{sprite_name}/{sprite_name}_'
    actions = action

    for actionNumber in range(0, len(actions)):
        for frameNumber in range(0, 4):
            image_path = path + actions[actionNumber] + '_' + 'anim_f' + str(frameNumber) + '.png'
            images.append(pygame.image.load(image_path))

    return images

animations = {

    'elf_m': load_animation_images('elf_m', ['idle', 'run']),
    'wizzard_m': load_animation_images('wizzard_m', ['idle', 'run']),
    'knight_m': load_animation_images('knight_m', ['idle', 'run']),

    'elf_f': load_animation_images('elf_f', ['idle', 'run']),
    'wizzard_f': load_animation_images('wizzard_f', ['idle', 'run']),
    'knight_f': load_animation_images('knight_f', ['idle', 'run']),


    'skelet': load_animation_images('skelet', ['idle', 'run']),
    'wogol': load_animation_images('wogol', ['idle', 'run']),
    'goblin': load_animation_images('goblin', ['idle', 'run']),
    'zombie': load_animation_images('zombie', ['idle', 'run']),
    'chort': load_animation_images('chort', ['idle', 'run']),
    'masked_orc': load_animation_images('masked_orc', ['idle', 'run'])
}
