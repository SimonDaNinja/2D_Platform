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

class Solid:
    INSTRUCTIONS = []
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

    def CollideWithCharacter(self, character):
        onTopOfSolid = False
        gameOver = False
        win = False
        for seg in self.segments:
            leftX = character.x-character.radius
            rightX = character.x+character.radius
            topY = character.y+character.radius
            bottomY = character.y-character.radius
            leftEndSurrounded = ((seg[0] < leftX) and (leftX < (seg[0]+seg[2])))
            rightEndSurrounded = ((seg[0] < rightX) and (rightX < (seg[0]+seg[2])))
            segmentSurroundedX = ((seg[0] >= leftX) and (rightX >= (seg[0]+seg[2])))
            if leftEndSurrounded or rightEndSurrounded or segmentSurroundedX:
                if abs(seg[0]-rightX)>abs(seg[0]+seg[2]-leftX):
                    shortestXMoveOut = seg[0]+seg[2]-leftX
                else:
                    shortestXMoveOut = seg[0]-rightX
                bottomSurrounded = ((seg[1] >= bottomY) and (bottomY > (seg[1]-seg[3])))
                topSurrounded = ((seg[1] >= topY) and (topY > (seg[1]-seg[3])))
                segmentSurroundedY = ((seg[1] <= topY) and (bottomY < (seg[1]-seg[3])))
                if bottomSurrounded or topSurrounded or segmentSurroundedY:
                    if abs(seg[1]-bottomY)>abs(seg[1]-seg[3]-topY):
                        shortestYMoveOut = seg[1]-seg[3]-topY
                    else:
                        shortestYMoveOut = seg[1]-bottomY
                    if abs(shortestXMoveOut)>abs(shortestYMoveOut):
                        character.y += shortestYMoveOut
                        if character.velocityY<0:
                            onTopOfSolid = True
                        if shortestYMoveOut>0 and character.velocityY>0:
                            signMove = abs(shortestYMoveOut)/shortestYMoveOut
                            signVel = abs(character.velocityY)/character.velocityY
                        else:
                            signMove = 1
                            signVel = 1
                        if signMove == signVel:
                            if abs(character.velocityY)>300:
                                character.velocityY = -character.velocityY*character.yBounciness
                            else:
                                character.velocityY = 0
                    else:
                        character.x += shortestXMoveOut
                        if shortestXMoveOut>0 and character.velocityX>0:
                            signMove = abs(shortestXMoveOut)/shortestXMoveOut
                            signVel = abs(character.velocityX)/character.velocityX
                        else:
                            signMove = 1
                            signVel = 1
                        if signMove == signVel:
                            if abs(character.velocityX)>300:
                                character.velocityX = -character.velocityX*character.xBounciness
                            else:
                                character.velocityX = 0
        return onTopOfSolid, gameOver, win

class Goal(Solid):

    def CollideWithCharacter(self, character):
        onTopOfSolid = False
        gameOver = False
        win = False
        onTopOfSolid = False
        for seg in self.segments:
            leftX = character.x-character.radius
            rightX = character.x+character.radius
            topY = character.y+character.radius
            bottomY = character.y-character.radius
            leftEndSurrounded = ((seg[0] < leftX) and (leftX < (seg[0]+seg[2])))
            rightEndSurrounded = ((seg[0] < rightX) and (rightX < (seg[0]+seg[2])))
            segmentSurroundedX = ((seg[0] >= leftX) and (rightX >= (seg[0]+seg[2])))
            if leftEndSurrounded or rightEndSurrounded or segmentSurroundedX:
                if abs(seg[0]-rightX)>abs(seg[0]+seg[2]-leftX):
                    shortestXMoveOut = seg[0]+seg[2]-leftX
                else:
                    shortestXMoveOut = seg[0]-rightX
                bottomSurrounded = ((seg[1] >= bottomY) and (bottomY > (seg[1]-seg[3])))
                topSurrounded = ((seg[1] >= topY) and (topY > (seg[1]-seg[3])))
                segmentSurroundedY = ((seg[1] <= topY) and (bottomY < (seg[1]-seg[3])))
                if bottomSurrounded or topSurrounded or segmentSurroundedY:
                    gameOver = True
                    win = True
        return onTopOfSolid, gameOver, win

class Trap(Solid):
    def CollideWithCharacter(self, character):
        onTopOfSolid = False
        gameOver = False
        win = False
        onTopOfSolid = False
        for seg in self.segments:
            leftX = character.x-character.radius
            rightX = character.x+character.radius
            topY = character.y+character.radius
            bottomY = character.y-character.radius
            leftEndSurrounded = ((seg[0] < leftX) and (leftX < (seg[0]+seg[2])))
            rightEndSurrounded = ((seg[0] < rightX) and (rightX < (seg[0]+seg[2])))
            segmentSurroundedX = ((seg[0] >= leftX) and (rightX >= (seg[0]+seg[2])))
            if leftEndSurrounded or rightEndSurrounded or segmentSurroundedX:
                if abs(seg[0]-rightX)>abs(seg[0]+seg[2]-leftX):
                    shortestXMoveOut = seg[0]+seg[2]-leftX
                else:
                    shortestXMoveOut = seg[0]-rightX
                bottomSurrounded = ((seg[1] >= bottomY) and (bottomY > (seg[1]-seg[3])))
                topSurrounded = ((seg[1] >= topY) and (topY > (seg[1]-seg[3])))
                segmentSurroundedY = ((seg[1] <= topY) and (bottomY < (seg[1]-seg[3])))
                if bottomSurrounded or topSurrounded or segmentSurroundedY:
                    gameOver = True
                    win = False
        return onTopOfSolid, gameOver, win

class MovingSolidX(Solid):
    INSTRUCTIONS=['solid.Move(D_T)']
    SPEED = 300
    def __init__(self,
            color,
            startX,
            startY,
            width,
            height,
            xEnds,
            goingRight = True):
        startSegment = [startX, startY, width, height]
        self.segments = [startSegment]
        self.xLeft = min(xEnds)
        self.xRight = max(xEnds)
        self.color = color
        self.goingRight = goingRight
        self.character = None

    def Move(self, dT):
        x = self.segments[0][0]
        if self.goingRight:
            x += dT*self.SPEED
            self.segments[0][0] = x
            if not (self.character is None):
                self.character.x += dT*self.SPEED
            if x>self.xRight:
                self.goingRight = False
        else:
            x -= dT*self.SPEED
            self.segments[0][0] = x
            if not (self.character is None):
                self.character.x -= dT*self.SPEED
            if x<self.xLeft:
                self.goingRight = True

    def CollideWithCharacter(self, character):
        onTopOfSolid = False
        gameOver = False
        win = False
        for seg in self.segments:
            leftX = character.x-character.radius
            rightX = character.x+character.radius
            topY = character.y+character.radius
            bottomY = character.y-character.radius
            leftEndSurrounded = ((seg[0] < leftX) and (leftX < (seg[0]+seg[2])))
            rightEndSurrounded = ((seg[0] < rightX) and (rightX < (seg[0]+seg[2])))
            segmentSurroundedX = ((seg[0] >= leftX) and (rightX >= (seg[0]+seg[2])))
            if leftEndSurrounded or rightEndSurrounded or segmentSurroundedX:
                if abs(seg[0]-rightX)>abs(seg[0]+seg[2]-leftX):
                    shortestXMoveOut = seg[0]+seg[2]-leftX
                else:
                    shortestXMoveOut = seg[0]-rightX
                bottomSurrounded = ((seg[1] >= bottomY) and (bottomY > (seg[1]-seg[3])))
                topSurrounded = ((seg[1] >= topY) and (topY > (seg[1]-seg[3])))
                segmentSurroundedY = ((seg[1] <= topY) and (bottomY < (seg[1]-seg[3])))
                if bottomSurrounded or topSurrounded or segmentSurroundedY:
                    if abs(seg[1]-bottomY)>abs(seg[1]-seg[3]-topY):
                        shortestYMoveOut = seg[1]-seg[3]-topY
                    else:
                        shortestYMoveOut = seg[1]-bottomY
                    if abs(shortestXMoveOut)>abs(shortestYMoveOut):
                        character.y += shortestYMoveOut
                        if character.velocityY<0:
                            onTopOfSolid = True
                        if shortestYMoveOut>0 and character.velocityY>0:
                            signMove = abs(shortestYMoveOut)/shortestYMoveOut
                            signVel = abs(character.velocityY)/character.velocityY
                        else:
                            signMove = 1
                            signVel = 1
                        if signMove == signVel:
                            if abs(character.velocityY)>300:
                                character.velocityY = -character.velocityY*character.yBounciness
                            else:
                                character.velocityY = 0
                    else:
                        character.x += shortestXMoveOut
                        if shortestXMoveOut>0 and character.velocityX>0:
                            signMove = abs(shortestXMoveOut)/shortestXMoveOut
                            signVel = abs(character.velocityX)/character.velocityX
                        else:
                            signMove = 1
                            signVel = 1
                        if signMove == signVel:
                            if abs(character.velocityX)>300:
                                character.velocityX = -character.velocityX*character.xBounciness
                            else:
                                character.velocityX = 0
            if onTopOfSolid:
                self.character = character
            else:
                self.character = None
        return onTopOfSolid, gameOver, win
