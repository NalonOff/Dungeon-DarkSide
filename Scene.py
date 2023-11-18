import pygame

class Scene:

    def __init__(self, screen):
        self.screen = screen
        self.display = pygame.Surface((426, 240))
        self.running = True
        self.clock = pygame.time.Clock()
        self.windowSize = screen.get_size()
        self.mousePos = pygame.mouse.get_pos()[0] / 4.5, pygame.mouse.get_pos()[1] / 4.5

    def display_flip(self):
        self.surf = pygame.transform.scale(self.display, self.windowSize)
        self.screen.blit(self.surf, (0, 0))
        pygame.display.flip()

        self.mousePos = pygame.mouse.get_pos()[0] / 4.5, pygame.mouse.get_pos()[1] / 4.5

    def zoom(self, image, zoomlevel):
        zoomed_image = image
        for zoom in range(1, zoomlevel):
            zoomed_image = pygame.transform.scale2x(zoomed_image)
        return zoomed_image

    def rect_calculator(self, x, y, width, height):

        newX = (x * self.windowSize[0]) / 1920
        newY = (y * self.windowSize[0]) / 1920
        newWidth = (width * self.windowSize[0]) / 1920
        newHeight = (height * self.windowSize[0]) / 1920

        rect = pygame.Rect(newX, newY, newWidth, newHeight)

        return rect