import pygame
import Scene
from Menus.GenderSelecterScreen import GenderSelecterScreen
from Entities.ElfM import ElfM
from Entities.WizzardM import WizzardM
from Entities.KnightM import KnightM

class HeroSelecterScreen(Scene.Scene):

    def __init__(self, screen):
        super().__init__(screen)
        self.genderSelecterScreen = GenderSelecterScreen(screen)

        self.selectButtonLeft = pygame.image.load('assets/textures/gui/menus/selectButtonBlack.png')
        self.selectButtonMid = pygame.image.load('assets/textures/gui/menus/selectButtonBlack.png')
        self.selectButtonRight = pygame.image.load('assets/textures/gui/menus/selectButtonBlack.png')

        self.selectButtonLeftRect = self.rect_calculator(17, 110, 112, 112)
        self.selectButtonMidRect = self.rect_calculator(157, 110, 112, 112)
        self.selectButtonRightRect = self.rect_calculator(297, 110, 112, 112)

        self.back = pygame.image.load('assets/textures/gui/menus/selectHeroSceenBack.png')

        self.elf = ElfM()
        self.wizzard = WizzardM()
        self.knight = KnightM()
        self.hero_string = None

        self.xPos = [40, 180, 320]
        self.yPos = [95, 95, 95]

        self.started = False


    def handling_event(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if self.selectButtonLeftRect.collidepoint(self.mousePos):
                self.selectButtonLeft = pygame.image.load(
                    'assets/textures/gui/menus/selectButtonWhite.png')
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.hero_string = 'elf'
                    self.started = True
            elif self.selectButtonMidRect.collidepoint(self.mousePos):
                self.selectButtonMid = pygame.image.load(
                    'assets/textures/gui/menus/selectButtonWhite.png')
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.hero_string = 'wizzard'
                    self.started = True
            elif self.selectButtonRightRect.collidepoint(self.mousePos):
                self.selectButtonRight = pygame.image.load(
                    'assets/textures/gui/menus/selectButtonWhite.png')
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.hero_string = 'knight'
                    self.started = True
            else:
                self.selectButtonLeft = pygame.image.load(
                    'assets/textures/gui/menus/selectButtonBlack.png')
                self.selectButtonMid = pygame.image.load(
                    'assets/textures/gui/menus/selectButtonBlack.png')
                self.selectButtonRight = pygame.image.load(
                    'assets/textures/gui/menus/selectButtonBlack.png')

        self.clock.tick(120)


    def update(self):
        self.elf.update()
        self.wizzard.update()
        self.knight.update()

        if self.started:
            self.start(self.hero_string)

    def start(self, heroName):
        start_Rect = pygame.Rect(0, 215, 426, 16)
        down_rect = pygame.Rect(0, 0, 426, 15)

        if heroName == 'elf':
            if down_rect.collidepoint(self.xPos[0],self.yPos[0]):
                self.elf.momentum = -self.elf.momentum - 2.5
            else:
                self.elf.momentum += 0.08
            self.yPos[0] -= self.elf.momentum
            if start_Rect.collidepoint(self.xPos[0], self.yPos[0]):
                self.running = False
                self.elf.momentum = 0
                self.genderSelecterScreen.run(heroName)

        if heroName == 'wizzard':
            if down_rect.collidepoint(self.xPos[1],self.yPos[1]):
                self.wizzard.momentum = -self.wizzard.momentum - 2.5
            else:
                self.wizzard.momentum += 0.08
            self.yPos[1] -= self.wizzard.momentum
            if start_Rect.collidepoint(self.xPos[1], self.yPos[1]):
                self.running = False
                self.wizzard.momentum = 0
                self.genderSelecterScreen.run(heroName)

        if heroName == 'knight':
            if down_rect.collidepoint(self.xPos[2],self.yPos[2]):
                self.knight.momentum = -self.knight.momentum - 2.5
            else:
                self.knight.momentum += 0.08
            self.yPos[2] -= self.knight.momentum

            if start_Rect.collidepoint(self.xPos[2], self.yPos[2]):
                self.running = False
                self.knight.momentum = 0
                self.genderSelecterScreen.run(heroName)


    def run(self):
        while self.running:
            self.handling_event()
            self.update()

            self.screen.fill((34, 34, 34))
            self.display.fill((0, 0, 0))

            self.display.blit(self.back, (0, 0))
            self.display.blit(self.selectButtonLeft, (17, 110))
            self.display.blit(self.selectButtonMid, (157, 110))
            self.display.blit(self.selectButtonRight, (297, 110))

            self.display.blit(self.zoom(self.elf.image, 3), (self.xPos[0], self.yPos[0]))
            self.display.blit(self.zoom(self.wizzard.image, 3), (self.xPos[1], self.yPos[1]))
            self.display.blit(self.zoom(self.knight.image, 3), (self.xPos[2], self.yPos[2]))


            self.display_flip()
