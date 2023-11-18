import pygame
import Scene
from Map import Map
from Menus.PauseScreen import PauseMenu

class Game(Scene.Scene):
    def __init__(self, screen, hero):
        super().__init__(screen)

        self.hero = hero

        self.map = Map()
        self.pauseMenu = PauseMenu(screen)

        self.running = True


    def handling_event(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.hero.moving_left = True
                if event.key == pygame.K_d:
                    self.hero.moving_right = True
                if event.key == pygame.K_s:
                    self.hero.moving_down = True
                if event.key == pygame.K_w:
                    self.hero.moving_up = True

                if event.key == pygame.K_ESCAPE:
                    self.pauseMenu.run()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.hero.moving_left = False
                if event.key == pygame.K_d:
                    self.hero.moving_right = False
                if event.key == pygame.K_s:
                    self.hero.moving_down = False
                if event.key == pygame.K_w:
                    self.hero.moving_up = False

        self.clock.tick(120)


    def run(self):
        pygame.mixer.init()
        while self.running:
            self.handling_event()
            self.hero.update()

            self.screen.fill((34, 34, 34))
            self.display.fill((0, 0, 0))

            self.map.renderLevel(self.map.loadLevel('map', 3), self.display)
            self.display.blit(self.hero.image, self.hero.pos)

            self.display_flip()
