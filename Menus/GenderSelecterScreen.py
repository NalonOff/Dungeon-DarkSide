import pygame
import Scene
from Game import Game
from Entities.ElfM import ElfM
from Entities.WizzardM import WizzardM
from Entities.KnightM import KnightM
from Entities.ElfF import ElfF
from Entities.WizzardF import WizzardF
from Entities.KnightF import KnightF

class GenderSelecterScreen(Scene.Scene):

    def __init__(self, screen):
        super().__init__(screen)
        self.screen = screen

        self.selectButtonLeft = pygame.image.load('assets/textures/gui/menus/selectButtonBlack.png')
        self.selectButtonRight = pygame.image.load('assets/textures/gui/menus/selectButtonBlack.png')

        self.selectButtonLeftRect = self.rect_calculator(16, 90, 112, 112)
        self.selectButtonRightRect = self.rect_calculator(308, 90, 112, 112)

        self.back = pygame.image.load('assets/textures/gui/menus/selectTypeScreenBack.png')
        self.back2 = pygame.image.load('assets/textures/gui/menus/selectTypeScreenBack2.png')

        self.elf_m = ElfM()
        self.elf_f = ElfF()
        self.wizzard_m = WizzardM()
        self.wizzard_f = WizzardF()
        self.knight_m = KnightM()
        self.knight_f = KnightF()
        self.hero_past_string = None
        self.hero_string = None

        self.xPos = [40, 330]
        self.yPos = [75, 75]


        self.started = False
        self.stats = False


    def handling_event(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if self.selectButtonLeftRect.collidepoint(self.mousePos):
                self.selectButtonLeft = pygame.image.load('assets/textures/gui/menus/selectButtonWhite.png')
                self.hero_string = f'{self.hero_past_string}_f'
                self.stats = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.started = True
            elif self.selectButtonRightRect.collidepoint(self.mousePos):
                self.selectButtonRight = pygame.image.load('assets/textures/gui/menus/selectButtonWhite.png')
                self.hero_string = f'{self.hero_past_string}_m'
                self.stats = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.started = True
            else:
                self.selectButtonLeft = pygame.image.load('assets/textures/gui/menus/selectButtonBlack.png')
                self.selectButtonRight = pygame.image.load('assets/textures/gui/menus/selectButtonBlack.png')
                self.stats = False


        self.clock.tick(120)


    def update(self):
        self.elf_m.update()
        self.elf_f.update()
        self.wizzard_m.update()
        self.wizzard_f.update()
        self.knight_m.update()
        self.knight_f.update()

        if self.started:
            self.start()

    def start(self):
        start_Rect = pygame.Rect(0, 215, 426, 16)
        down_rect = pygame.Rect(0, 0, 426, 15)

        if self.hero_string == 'elf_m':
            hero = self.elf_m
            if down_rect.collidepoint(self.xPos[1], self.yPos[1]):
                hero.momentum = -hero.momentum - 3
            else:
                hero.momentum += 0.08
            self.yPos[1] -= hero.momentum

            if start_Rect.collidepoint(self.xPos[1], self.yPos[1]):
                self.running = False
                hero.momentum = 0
                Game(self.screen, hero).run()
        if self.hero_string == 'elf_f':
            hero = self.elf_f
            if down_rect.collidepoint(self.xPos[0], self.yPos[0]):
                hero.momentum = -hero.momentum - 3
            else:
                hero.momentum += 0.08
            self.yPos[0] -= hero.momentum

            if start_Rect.collidepoint(self.xPos[0], self.yPos[0]):
                self.running = False
                hero.momentum = 0
                Game(self.screen, hero).run()
        if self.hero_string == 'wizzard_m':
            hero = self.wizzard_m
            if down_rect.collidepoint(self.xPos[1], self.yPos[1]):
                hero.momentum = -hero.momentum - 3
            else:
                hero.momentum += 0.08
            self.yPos[1] -= hero.momentum

            if start_Rect.collidepoint(self.xPos[1], self.yPos[1]):
                self.running = False
                hero.momentum = 0
                Game(self.screen, hero).run()
        if self.hero_string == 'wizzard_f':
            hero = self.wizzard_f
            if down_rect.collidepoint(self.xPos[0], self.yPos[0]):
                hero.momentum = -hero.momentum - 3
            else:
                hero.momentum += 0.08
            self.yPos[0] -= hero.momentum

            if start_Rect.collidepoint(self.xPos[0], self.yPos[0]):
                self.running = False
                hero.momentum = 0
                Game(self.screen, hero).run()
        if self.hero_string == 'knight_m':
            hero = self.knight_m
            if down_rect.collidepoint(self.xPos[1], self.yPos[1]):
                hero.momentum = -hero.momentum - 3
            else:
                hero.momentum += 0.08
            self.yPos[1] -= hero.momentum

            if start_Rect.collidepoint(self.xPos[1], self.yPos[1]):
                self.running = False
                hero.momentum = 0
                Game(self.screen, hero).run()
        if self.hero_string == 'knight_f':
            hero = self.knight_f
            if down_rect.collidepoint(self.xPos[0], self.yPos[0]):
                hero.momentum = -hero.momentum - 3
            else:
                hero.momentum += 0.08
            self.yPos[0] -= hero.momentum

            if start_Rect.collidepoint(self.xPos[0], self.yPos[0]):
                self.running = False
                hero.momentum = 0
                Game(self.screen, hero).run()


    def load_hero(self, hero):
        if hero == 'elf':
            self.display.blit(self.zoom(self.elf_f.image, 3), (self.xPos[0], self.yPos[0]))
            self.display.blit(self.zoom(self.elf_m.image, 3), (self.xPos[1], self.yPos[1]))
            self.hero_past_string = 'elf'
        elif hero == 'wizzard':
            self.display.blit(self.zoom(self.wizzard_f.image, 3), (self.xPos[0], self.yPos[0]))
            self.display.blit(self.zoom(self.wizzard_m.image, 3), (self.xPos[1], self.yPos[1]))
            self.hero_past_string = 'wizzard'
        elif hero == 'knight':
            self.display.blit(self.zoom(self.knight_f.image, 3), (self.xPos[0], self.yPos[0]))
            self.display.blit(self.zoom(self.knight_m.image, 3), (self.xPos[1], self.yPos[1]))
            self.hero_past_string = 'knight'


    def show_stats(self):
        self.display.blit(pygame.image.load(f'assets/textures/gui/menus/stats/{self.hero_string}.png'), (0, 0))


    def run(self, hero):
        while self.running:
            self.handling_event()
            self.update()

            self.screen.fill((34, 34, 34))
            self.display.fill((0, 0, 0))

            self.display.blit(self.back, (0, 0))
            self.display.blit(self.selectButtonLeft, (16, 90))
            self.display.blit(self.selectButtonRight, (308, 90))

            if self.stats:
                self.show_stats()
            else:
                self.display.blit(self.back2, (0, 0))


            self.load_hero(hero)


            self.display_flip()
