import pygame
import Scene
from Menus.HeroSelecterScreen import HeroSelecterScreen
from Entities.MaskedOrc import MaskedOrc

class TitleScreen(Scene.Scene):

    def __init__(self, screen):
        super().__init__(screen)
        self.heroselecter = HeroSelecterScreen(screen)

        self.masked_orc = MaskedOrc()
        self.masked_orc.pos = [300, 120]

        self.playButton = pygame.image.load('assets/textures/gui/menus/selectButtonBlack.png')
        self.playButtonRect = self.rect_calculator(442, 721, 555, 245)
        self.back = pygame.image.load('assets/textures/gui/menus/titleScreenBack.png')

        self.started = False

    def handling_event(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if self.playButtonRect.collidepoint(pygame.mouse.get_pos()):
                self.playButton = pygame.image.load('assets/textures/gui/menus/startButtonWhite.png')
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.started = True
            else:
                self.playButton = self.playButton = pygame.image.load('assets/textures/gui/menus/startButtonBlack.png')

        self.clock.tick(120)

    def start(self):
        self.masked_orc.moving_right = True
        start_Rect = pygame.Rect(430, 120, 16, 27)

        if self.masked_orc.rect.colliderect(start_Rect):
            self.masked_orc.moving_right = False
            self.running = False
            self.heroselecter.run()

    def update(self):
        self.masked_orc.update()

        if self.started:
            self.start()

    def run(self):
        while self.running:
            self.handling_event()
            self.update()

            self.display.fill((0, 0, 0))

            self.display.blit(self.back, (0, 0))

            self.display.blit(self.masked_orc.image, self.masked_orc.pos)


            self.display.blit(self.playButton, (98, 160))
            self.display_flip()
