#---------------
#MIT License

#Copyright (c) 2019 Simon Liljestrand

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.
#----------------


# If this file is run, an overview of the stage will be displayed
import pygame
import math
from character import Character
from solid import Solid
from stage import Stage
from solid import Goal
from solid import Trap
from solid import MovingSolidX
import color_palette

WIDTH = 800
HEIGHT = 600

STAGE_WIDTH = 1200*3
STAGE_HEIGHT = 1000


pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
solids = []

underWaterCatcher = Solid((0,0,0),[(0, -500, STAGE_WIDTH, 50)])
solids.append(underWaterCatcher)

waterLevel = 100
water = Trap(color_palette.TEAL, [(0,waterLevel,STAGE_WIDTH,waterLevel)])
solids.append(water)

plankThickness = 50
plankLength = 300
correctionTerm1 = 50
correctionTerm2 = correctionTerm1+150
plank = Solid(color_palette.BROWN, [(plankThickness, waterLevel+plankThickness, plankLength, plankThickness),
    (plankThickness+6*plankLength, waterLevel+plankThickness, plankLength, plankThickness),
    (correctionTerm1+plankThickness+7*plankLength+plankThickness*2, waterLevel + plankThickness*5, plankThickness*2, plankThickness*2),
    (correctionTerm2+plankThickness+7*plankLength+plankThickness*2+plankThickness*3, waterLevel + plankThickness*7, plankLength*2, plankThickness)])
solids.append(plank)

startX = 2*plankThickness+plankLength +plankLength
startY = plankThickness+waterLevel
xEnds = (4*plankThickness+plankLength, plankThickness+5*plankLength-3*plankThickness)
solids.append(plank)

movingPlank = MovingSolidX(color_palette.BROWN,startX, startY, plankLength, plankThickness, xEnds, False)
solids.append(movingPlank)

goalWidth = 100
goalHeight = 150
goal = Goal(color_palette.WHITE, [(correctionTerm2+plankThickness+7*plankLength+plankThickness*2+plankThickness*3+plankLength, waterLevel + plankThickness*7+goalHeight, goalWidth, goalHeight)])
solids.append(goal)

startX = plankThickness + plankLength/2
startY = int(HEIGHT/2)
character = Character(screen, startX, startY, (255,215,0), 50)
isPeriodic = False
stage = Stage(screen, character, isPeriodic, STAGE_WIDTH, STAGE_HEIGHT, solids)

if __name__ == '__main__':
    stage.DrawStage(1200)
    input('press anything to exit')
