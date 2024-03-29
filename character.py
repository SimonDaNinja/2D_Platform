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
import pygame
import math
import movement_constants
import random

class Character:
    MAX_SPEED = 8000
    def __init__(self,
            surface,
            startX,
            startY,
            color,
            radius,
            stageWidth = None,
            stageHeight = None,
            velocityX = 0,
            velocityY = 0,
            accelerationX = 0,
            accelerationY = 0,
            maxRunSpeed = 800,
            stoppingRateVel = 1500,
            xBounciness = 0.5,
            yBounciness = .0):

        self.x = startX
        self.y = startY
        self.color = color
        self.radius = radius
        self.stageWidth = stageWidth
        self.stageHeight = stageHeight
        self.accelerationX = accelerationX
        self.accelerationY = accelerationY
        self.velocityX = velocityX
        self.velocityY = velocityY
        self.maxRunSpeed = maxRunSpeed
        self.onTheGround = False
        self.stoppingRateVel = stoppingRateVel
        self.xBounciness = xBounciness
        self.yBounciness = yBounciness
        self.screenWidth, self.screenHeight = surface.get_size()
        self.surface = surface

    def GetUpperLeftCorner(self):
            upperLeftXA = max(int(self.x - self.screenWidth/2),0)
            upperLeftX = min(upperLeftXA, int(self.stageWidth - self.screenWidth))
            upperLeftYA = min(int(self.y + self.screenHeight/2), self.stageHeight)
            upperLeftY = max(upperLeftYA, int(self.screenHeight))
            upperLeft = (upperLeftX, upperLeftY)
            return upperLeft

    def Draw(self):
        upperLeftX, upperLeftY = self.GetUpperLeftCorner()
        relativeX = self.x - upperLeftX
        relativeY = self.y - upperLeftY + self.stageHeight
        screenX = int(relativeX)
        screenY = int(self.stageHeight - relativeY)
        pygame.draw.circle(self.surface, self.color, (screenX, screenY), self.radius)

    def Gravitate(self, gravAccX, gravAccY):
        self.accelerationX += gravAccX
        self.accelerationY += gravAccY

    def Step(self, dT, isPeriodic):
        speed = math.sqrt(self.velocityX**2 + self.velocityY**2)
        if speed>self.MAX_SPEED:
            rescaleFactor = self.MAX_SPEED/speed
            self.velocityX *= rescaleFactor
            self.velocityY *= rescaleFactor
        if isPeriodic:
            self.x += self.velocityX*dT
            self.y += self.velocityY*dT
            if self.x<0:
                self.x = self.stageWidth
            if self.x > self.stageWidth:
                self.x = 0
        else:
            if self.x<0:
                self.x = 0
                self.velocityX = 0
            elif self.x > self.stageWidth:
                self.x = self.stageWidth
                self.velocityX = 0
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

    def ShiftColorRandomly(self):
        if self.onTheGround:
            r = random.randint(0,255)
            g = random.randint(0,255)
            b = random.randint(0,255)
            randomColor = (r,g,b)
            self.color = randomColor

    def Jump(self):
        if self.onTheGround:
            self.velocityY += 1500
