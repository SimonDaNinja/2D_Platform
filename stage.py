import pygame
import math
from character import Character
from solid import Solid
import movement_constants

GRAVITY_CONSTANT_Y = -5000
GRAVITY_CONSTANT_X = 0
WIDTH = 800
HEIGHT = 600
FPS = 60
D_T = 1/FPS

EXAMPLE_SOLIDS = []
EXAMPLE_SOLIDS.append(Solid((int(255/2),0,0),[(0,200,math.floor(WIDTH/3),200),(math.floor(WIDTH/3),100,math.floor(WIDTH/3),100),(math.floor(WIDTH/3)*2,200,(WIDTH-1+math.floor(WIDTH/3)*2),200)]))
EXAMPLE_SOLIDS.append(Solid((0,int(255/3*2),0),[(0,int(HEIGHT*2/3),250,50)]))

class Stage:
    def __init__(self,
            screen,
            character,
            isPeriodic,
            stageWidth,
            stageHeight,
            solids = EXAMPLE_SOLIDS):

        self.screen = screen
        self.solids = solids
        self.clock = pygame.time.Clock()
        self.character = character
        self.isPeriodic = isPeriodic
        self.stageWidth = stageWidth
        self.stageHeight = stageHeight
        self.character.stageWidth = stageWidth
        self.character.stageHeight = stageHeight
        self.screenWidth, self.screenHeight = screen.get_size()

    def SetStageWidth(self, stageWidth):
        self.stageWidth = stageWidth
        self.character.stageWidth = stageWidth

    def SetStageHeight(self, stageHeight):
        self.stageHeight = stageHeight
        self.character.stageHeight = stageHeight

    def DrawStage(self, maxDim):
        # This method is only meant to be used for getting an overview of the stage during development!
        if self.stageWidth > self.stageHeight:
            stageToScreenFactor = maxDim/self.stageWidth
        else:
            stageToScreenFactor = maxDim/self.stageHeight
        screenWidth = int(stageToScreenFactor*self.stageWidth)
        screenHeight = int(stageToScreenFactor*self.stageHeight)

        screen = pygame.display.set_mode((screenWidth,screenHeight))

        screen.fill((0,128,255))
        drawSolids = [Solid(solid.color,[tuple(val*stageToScreenFactor for val in seg) for seg in solid.segments]) for solid in self.solids]
        for solid in drawSolids:
            solid.Draw(screen, screenWidth, screenHeight, 0, screenHeight)
        character = Character(screen, int(self.character.x*stageToScreenFactor), int(self.character.y*stageToScreenFactor), self.character.color, int(self.character.radius*stageToScreenFactor), screenWidth, screenHeight)
        character.Draw()
        pygame.display.flip()
        

    def Run(self):
        playing = True
        while playing:
            self.screen.fill((0,128,255))
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    self.character.Jump()
                if event.type == pygame.QUIT:
                    playing = False
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_LEFT]:
                self.character.Run(movement_constants.LEFT)
            if pressed[pygame.K_RIGHT]:
                self.character.Run(movement_constants.RIGHT)
            self.character.Gravitate(GRAVITY_CONSTANT_X, GRAVITY_CONSTANT_Y)
            self.character.Step(D_T, self.isPeriodic)
            isOnTheGround = False
            for solid in self.solids:
                isOnTheGround = bool(isOnTheGround + self.character.CollideWithSolid(solid))
            self.character.onTheGround = isOnTheGround

            if self.character.onTheGround:
                self.character.SlowDown(D_T)
            self.character.Draw()
            topLeftX, topLeftY = self.character.GetUpperLeftCorner()
            for solid in self.solids:
                solid.Draw(self.screen, self.stageWidth, self.stageHeight, topLeftX, topLeftY)
            pygame.display.flip()
            self.clock.tick(FPS)
            self.character.accelerationX = 0
            self.character.accelerationY = 0

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    character = Character(screen, int(WIDTH/2), int(HEIGHT/2), (255,215,0), 50)
    stage = Stage(screen, character, True)
    stage.Run()
