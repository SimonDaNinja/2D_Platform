import pygame
import math
from character import Character
from solid import Solid
from stage import Stage

WIDTH = 800
HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
character = Character(screen, int(WIDTH/2), int(HEIGHT/2), (255,215,0), 50)
solids = []
solids.append(Solid((int(255/2),0,0),[(0,200,math.floor(WIDTH/3),200),(math.floor(WIDTH/3),100,math.floor(WIDTH/3),100),(math.floor(WIDTH/3)*2,200,(WIDTH-1+math.floor(WIDTH/3)*2),200)]))
solids.append(Solid((0,int(255/3*2),0),[(0,int(HEIGHT*2/3),250,50)]))
stage = Stage(screen, character, solids)