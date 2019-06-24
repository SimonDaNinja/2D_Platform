import pygame
import math
import numpy as np

GRAVITY_CONSTANT_Y = -5000
GRAVITY_CONSTANT_X = 0
WIDTH = 800
HEIGHT = 600
FPS = 60
D_T = 1/FPS

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

class Character:
    def __init__(self, startX, startY, color, radius, velocityX = 0, velocityY = 0, accelerationX = 0, accelerationY = 0, maxRunSpeed = 800, stoppingRateVel = 1500):
        self.x = startX
        self.y = startY
        self.color = color
        self.radius = radius
        self.accelerationX = accelerationX
        self.accelerationY = accelerationY
        self.velocityX = velocityX
        self.velocityY = velocityY
        self.maxRunSpeed = maxRunSpeed
        self.onTheGround = False
        self.stoppingRateVel = stoppingRateVel

    def Draw(self, screen):
        screenX = int(self.x)
        screenY = int(HEIGHT - self.y)
        pygame.draw.circle(screen, self.color, (screenX, screenY), self.radius)

    def Gravitate(self):
        self.accelerationY += GRAVITY_CONSTANT_Y
        self.accelerationX += GRAVITY_CONSTANT_X

    def Step(self):
        self.x += self.velocityX*D_T
        self.y += self.velocityY*D_T
        if self.x<0:
            self.x = WIDTH
        if self.x>WIDTH:
            self.x = 0
        self.velocityX += self.accelerationX*D_T
        self.velocityY += self.accelerationY*D_T

    def Run(self,direction):
        # if going too fast to the left
        if self.velocityX < 0 and direction == LEFT and abs(self.velocityX)>self.maxRunSpeed:
            pass
        # if going to fast to the right
        elif self.velocityX > 0 and direction == RIGHT and abs(self.velocityX)>self.maxRunSpeed:
            pass
        elif direction == RIGHT:
            self.accelerationX += 2600
        elif direction == LEFT:
            self.accelerationX -= 2600

    def SlowDown(self):
        if abs(self.velocityX)>0:
            velocitySign = self.velocityX/abs(self.velocityX)
            speedX = max(velocitySign*self.velocityX-self.stoppingRateVel*D_T,0)
            self.velocityX = velocitySign*speedX

    def Jump(self):
        if self.onTheGround:
            self.velocityY += 1500
            self.onTheGround = False

    def CollideWithSolid(self, solid):
        onTopOfSolid = False
        for seg in solid.segments:
            leftX = self.x-self.radius
            rightX = self.x+self.radius
            topY = self.y+self.radius
            bottomY = self.y-self.radius
            if((seg[0] < leftX) and (leftX < (seg[0]+seg[2])))or((seg[0] < rightX) and (rightX < (seg[0]+seg[2])))or((seg[0] > leftX) and (rightX > (seg[0]+seg[2]))):
                if abs(seg[0]-rightX)>abs(seg[0]+seg[2]-leftX):
                    shortestXMoveOut = seg[0]+seg[2]-leftX
                else:
                    shortestXMoveOut = seg[0]-rightX

                if((seg[1] >= bottomY) and (bottomY > (seg[1]-seg[3]))) or ((seg[1] >= topY) and (topY > (seg[1]-seg[3]))) or ((seg[1] <= topY) and (bottomY < (seg[1]-seg[3]))):
                    if abs(seg[1]-bottomY)>abs(seg[1]-seg[3]-topY):
                        shortestYMoveOut = seg[1]-seg[3]-topY
                    else:
                        shortestYMoveOut = seg[1]-bottomY
                    if abs(shortestXMoveOut)>abs(shortestYMoveOut):
                        self.y += shortestYMoveOut
                        onTopOfSolid = True
                        self.velocityY = 0
                    else:
                        self.x += shortestXMoveOut
                        self.velocityX = 0
        return onTopOfSolid


class Solid:
    def __init__(self, color, segments = [(0, 200, WIDTH, 200)]):
        self.segments = segments
        self.color = color
    def Draw(self, surface):
        for seg in self.segments:
            pygame.draw.rect(surface, self.color, pygame.Rect(int(seg[0]), int(HEIGHT-seg[1]), seg[2], seg[3]))


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    solids = []
    solids.append(Solid((int(255/2),0,0),[(0,200,math.floor(WIDTH/3),200),(math.floor(WIDTH/3),100,math.floor(WIDTH/3),100),(math.floor(WIDTH/3)*2,200,(WIDTH-1+math.floor(WIDTH/3)*2),200)]))
    solids.append(Solid((0,int(255/3*2),0),[(0,int(HEIGHT*2/3),250,50)]))
    clock = pygame.time.Clock()
    character = Character(int(WIDTH/2), int(HEIGHT/2), (255,215,0), 50)
    playing = True

    while playing:
        screen.fill((0,128,255))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                character.Jump()
            if event.type == pygame.QUIT:
                playing = False
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            character.Run(LEFT)
        if pressed[pygame.K_RIGHT]:
            character.Run(RIGHT)
        character.Gravitate()
        character.Step()
        isOnTheGround = False
        for solid in solids:
            isOnTheGround = bool(isOnTheGround + character.CollideWithSolid(solid))
        character.onTheGround = isOnTheGround

        if character.onTheGround:
            character.SlowDown()
        character.Draw(screen)
        for solid in solids:
            solid.Draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
        character.accelerationX = 0
        character.accelerationY = 0
