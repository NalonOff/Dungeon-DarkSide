import pygame

class Map:
    def __init__(self):
        texture_Path = 'assets/textures/block/'

        self.floor1 = pygame.image.load(f'{texture_Path}floor_1.png')
        self.floor2 = pygame.image.load(f'{texture_Path}floor_2.png')
        self.wallMid = pygame.image.load(f'{texture_Path}wall_mid.png')
        self.wallSideMidRight = pygame.image.load(f'{texture_Path}wall_side_mid_right.png')
        self.wallSideMidLeft = pygame.image.load(f'{texture_Path}wall_side_mid_left.png')
        self.wallInnerCornerMidLeft = pygame.image.load(f'{texture_Path}wall_inner_corner_mid_left.png')
        self.wallInnerCornerMidRight = pygame.image.load(f'{texture_Path}wall_inner_corner_mid_rigth.png')
        self.wallTopMid = pygame.image.load(f'{texture_Path}wall_top_mid.png')

    def loadLevel(self, file, numberOfLayers):

        game_map = []

        for layer in range(0, numberOfLayers):
            game_layer = []

            filePath = f'assets/maps/{file}{layer}.txt'
            f = open(filePath, 'r')
            data = f.read()
            f.close()
            data = data.split('\n')

            for row in data:
                game_layer.append(list(row))

            game_map.append(game_layer)

        return game_map



    def renderLevel(self, level, screen):

        for layers in level:
            y = 0
            for layer in layers:
                x = 0
                for tile in layer:
                    if tile == '1':
                        screen.blit(self.floor1, (x * 16, y * 16))
                    if tile == '2':
                        screen.blit(self.floor2, (x * 16, y * 16))
                    if tile == '3':
                        screen.blit(self.wallMid, (x * 16, y * 16))
                    if tile == '4':
                        screen.blit(self.wallSideMidRight, (x * 16, y * 16))
                    if tile == '5':
                        screen.blit(self.wallSideMidLeft, (x * 16, y * 16))
                    if tile == '6':
                        screen.blit(self.wallInnerCornerMidLeft, (x * 16, y * 16))
                    if tile == '7':
                        screen.blit(self.wallInnerCornerMidRight, (x * 16, y * 16))
                    if tile == '8':
                        screen.blit(self.wallTopMid, (x * 16, y * 16))
                    x += 1
                y += 1
