import pygame

class Map:

    def __init__(self, background_color,  rectangle_color, screen):
        self.background_color = background_color
        self.rectangle_color = rectangle_color
        self.screen = screen
        self.coordinates = []

    def build(self):
        self.screen.fill(self.background_color)

        x = 40
        y = 40
        while y < 560:
            while x < 560:
                pygame.draw.rect(self.screen, self.rectangle_color, pygame.Rect(x, y, 100, 100), 2, 3)
                self.coordinates.append((x, y))
                x += 105
            
            x = 40
            y += 105

    def get_coordinates(self):
        return self.coordinates
