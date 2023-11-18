import pygame
import Scene

class PauseMenu(Scene.Scene):

    def __init__(self, screen):
        super().__init__(screen)
        self.back = pygame.image.load('assets/textures/gui/menus/pauseSceenBack.png')

        self.started = False

    def handling_event(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False


        self.clock.tick(120)

    def update(self):
        pass

    def run(self):
        self.running = True

        while self.running:

            self.handling_event()
            self.update()

            self.display.fill((0, 0, 0))
            self.display.blit(self.back, (0, 0))


            self.display_flip()
