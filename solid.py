import pygame

WIDTH = 800

class Solid:
    def __init__(self, color, segments = [(0, 200, WIDTH, 200)]):
        self.segments = segments
        self.color = color
    def Draw(self, surface):
        height = surface.get_height()
        for seg in self.segments:
            pygame.draw.rect(surface, self.color, pygame.Rect(int(seg[0]), int(height-seg[1]), seg[2], seg[3]))
