# If this file is run, an overview of the stage will be displayed
import pygame
import math
from character import Character
from solid import Solid
from stage import Stage

WIDTH = 800
HEIGHT = 600
GREEN = (0,200,0)
RED = (200,0,0)

STAGE_X_SHIFT = 600

STAGE_WIDTH = 4300 + STAGE_X_SHIFT
STAGE_HEIGHT = 3500 + STAGE_X_SHIFT

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
character = Character(screen, int(WIDTH/2), int(HEIGHT/2), (255,215,0), 50)

solids = []

groundLevel = 100
ground = Solid(GREEN, [(0,groundLevel,STAGE_WIDTH,groundLevel)])
solids.append(ground)

platformSpacing = 200
platformWidth = 200
startPlatforms = Solid(RED, [(STAGE_X_SHIFT+0,groundLevel+platformSpacing,platformWidth,50),
        (STAGE_X_SHIFT+400,groundLevel+platformSpacing*2,platformWidth,50),
        (STAGE_X_SHIFT+0,groundLevel+platformSpacing*3,platformWidth,50),
        (STAGE_X_SHIFT+400,groundLevel+platformSpacing*4,platformWidth,50)])
solids.append(startPlatforms)

pipeThickness = 70
pipeWidth = 300
pipeBottom = Solid(RED, [(STAGE_X_SHIFT+400+450, groundLevel+platformSpacing*4, pipeThickness, platformSpacing*3),
    (STAGE_X_SHIFT+400+450, groundLevel+platformSpacing, 800, pipeThickness),
    (STAGE_X_SHIFT+400+450+800,groundLevel+platformSpacing*6,pipeThickness,platformSpacing*5+pipeThickness)])
solids.append(pipeBottom)

separatorHeight = 500
pipeTop = Solid(RED, [(STAGE_X_SHIFT+400+450+pipeWidth, groundLevel+platformSpacing*3, pipeThickness, platformSpacing*2-pipeWidth),
    (STAGE_X_SHIFT+400+450+pipeWidth, pipeWidth+groundLevel+platformSpacing, 800-pipeWidth*2, pipeThickness),
    (STAGE_X_SHIFT+400+450+800-pipeWidth, separatorHeight+groundLevel+platformSpacing*6, pipeThickness, separatorHeight+platformSpacing*5+pipeThickness-pipeWidth)])
solids.append(pipeTop)

pipePlatformWidth = 70
pipePlatformThickness = 50
pipePlatformsRight = Solid(RED, [(STAGE_X_SHIFT+400+450+800-pipePlatformWidth, groundLevel+platformSpacing*2, pipePlatformWidth, pipePlatformThickness),
    (STAGE_X_SHIFT+400+450+800-pipePlatformWidth, groundLevel+platformSpacing*4, pipePlatformWidth, pipePlatformThickness)])
solids.append(pipePlatformsRight)

pipePlatformsLeft = Solid(RED, [(STAGE_X_SHIFT+400+450+800-pipeWidth+pipeThickness, groundLevel+platformSpacing*3, pipePlatformWidth, pipePlatformThickness),
    (STAGE_X_SHIFT+400+450+800-pipeWidth+pipeThickness, groundLevel+platformSpacing*5, pipePlatformWidth, pipePlatformThickness)])
solids.append(pipePlatformsLeft)

connectingPlatform = Solid(RED, [(STAGE_X_SHIFT+400+450+800+300, groundLevel+platformSpacing*7, platformWidth, 50)])
solids.append(connectingPlatform)

stairs = Solid(RED, [(STAGE_X_SHIFT+platformSpacing+400+450+800+600, groundLevel+platformSpacing*8, platformWidth,platformSpacing*8),
    (STAGE_X_SHIFT+platformSpacing+400+450+800+600+platformWidth*1, groundLevel+platformSpacing*7, platformWidth,platformSpacing*7),
    (STAGE_X_SHIFT+platformSpacing+400+450+800+600+platformWidth*2, groundLevel+platformSpacing*6, platformWidth,platformSpacing*6),
    (STAGE_X_SHIFT+platformSpacing+400+450+800+600+platformWidth*3, groundLevel+platformSpacing*5, platformWidth,platformSpacing*5),
    (STAGE_X_SHIFT+platformSpacing+400+450+800+600+platformWidth*4, groundLevel+platformSpacing*4, platformWidth,platformSpacing*4),
    (STAGE_X_SHIFT+platformSpacing+400+450+800+600+platformWidth*5, groundLevel+platformSpacing*3, platformWidth,platformSpacing*3),
    (STAGE_X_SHIFT+platformSpacing+400+450+800+600+platformWidth*6, groundLevel+platformSpacing*2, platformWidth,platformSpacing*2),
    (STAGE_X_SHIFT+platformSpacing+400+450+800+600+platformWidth*7, groundLevel+platformSpacing*1, platformWidth,platformSpacing*1)])
solids.append(stairs)

isPeriodic = False
stage = Stage(screen, character, isPeriodic, STAGE_WIDTH, STAGE_HEIGHT, solids)

if __name__ == '__main__':
    stage.DrawStage(800)
    input('press anything to exit')
