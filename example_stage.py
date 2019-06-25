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

WIDTH = 800
HEIGHT = 600
BROWN = (0,200,math.floor(WIDTH/3),200)
GREEN = (0,int(255/3*2),0)

STAGE_WIDTH = WIDTH
STAGE_HEIGHT = HEIGHT

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
character = Character(screen, int(WIDTH/2), int(HEIGHT/2), (255,215,0), 50)
solids = []
ground = Solid((int(255/2),0,0),
        [BROWN,
            (math.floor(WIDTH/3),100,math.floor(WIDTH/3),100),
            (math.floor(WIDTH/3)*2,200,(WIDTH-1-math.floor(WIDTH/3)*2),200)])
platform =Solid(GREEN,[(0,int(HEIGHT*2/3),250,50)])

solids.append(ground)
solids.append(platform)
isPeriodic = True
stage = Stage(screen, character, isPeriodic, STAGE_WIDTH, STAGE_HEIGHT, solids)
if __name__ == '__main__':
    stage.DrawStage(800)
    input('press anything to exit')
