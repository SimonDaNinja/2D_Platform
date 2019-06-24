import pygame
import movement_constants

class Character:
    def __init__(self, surface, startX, startY, color, radius, velocityX = 0, velocityY = 0, accelerationX = 0, accelerationY = 0, maxRunSpeed = 800, stoppingRateVel = 1500, xBounciness = 0.5, yBounciness = .0):
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
        self.xBounciness = xBounciness
        self.yBounciness = yBounciness
        self.stageWidth, self.stageHeight = surface.get_size()
        self.surface = surface

    def Draw(self):
        screenX = int(self.x)
        screenY = int(self.stageHeight - self.y)
        pygame.draw.circle(self.surface, self.color, (screenX, screenY), self.radius)

    def Gravitate(self, gravAccX, gravAccY):
        self.accelerationX += gravAccX
        self.accelerationY += gravAccY

    def Step(self, dT, isPeriodic):
        if isPeriodic:
            self.x += self.velocityX*dT
            self.y += self.velocityY*dT
            if self.x<0:
                self.x = self.stageWidth
            if self.x > self.stageWidth:
                self.x = 0
        else:
            if self.x<0 or self.x > self.stageWidth:
                pass
            else:
                self.x += self.velocityX*dT
                self.y += self.velocityY*dT
        self.velocityX += self.accelerationX*dT
        self.velocityY += self.accelerationY*dT

    def Run(self,direction):
        # if going too fast to the left
        if self.velocityX < 0 and direction == movement_constants.LEFT and abs(self.velocityX)>self.maxRunSpeed:
            pass
        # if going to fast to the right
        elif self.velocityX > 0 and direction == movement_constants.RIGHT and abs(self.velocityX)>self.maxRunSpeed:
            pass
        elif direction == movement_constants.RIGHT:
            self.accelerationX += 2600
        elif direction == movement_constants.LEFT:
            self.accelerationX -= 2600

    def SlowDown(self, dT):
        if abs(self.velocityX)>0:
            velocitySign = self.velocityX/abs(self.velocityX)
            speedX = max(velocitySign*self.velocityX-self.stoppingRateVel*dT,0)
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
                        if shortestYMoveOut>0 and self.velocityY>0:
                            signMove = abs(shortestYMoveOut)/shortestYMoveOut
                            signVel = abs(self.velocityY)/self.velocityY
                        else:
                            signMove = 1
                            signVel = 1
                        if signMove == signVel:
                            if abs(self.velocityY)>300:
                                self.velocityY = -self.velocityY*self.yBounciness
                            else:
                                self.velocityY = 0
                    else:
                        self.x += shortestXMoveOut
                        if shortestXMoveOut>0 and self.velocityX>0:
                            signMove = abs(shortestXMoveOut)/shortestXMoveOut
                            signVel = abs(self.velocityX)/self.velocityX
                        else:
                            signMove = 1
                            signVel = 1
                        if signMove == signVel:
                            if abs(self.velocityX)>300:
                                self.velocityX = -self.velocityX*self.xBounciness
                            else:
                                self.velocityX = 0
        return onTopOfSolid