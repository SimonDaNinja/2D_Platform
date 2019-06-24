import pygame

class Solid:
    def __init__(self,
            color,
            segments):

        self.segments = segments
        self.color = color

    def Draw(self, surface, stageWidth, stageHeight, topLeftX, topLeftY):
        screenHeight = surface.get_height()
        for seg in self.segments:
            relativeX = seg[0] - topLeftX
            relativeY = seg[1] - topLeftY + stageHeight
            screenX = int(relativeX)
            screenY = int(stageHeight - relativeY)
            pygame.draw.rect(surface, self.color, pygame.Rect(screenX, screenY, seg[2], seg[3]))
