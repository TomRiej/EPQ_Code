import numpy as np

# TODO: make it look pretty with images

DEBUG = True

class Bird:
    def __init__(self, canvas, size, jumpStrength, gravity):
        self.__coords = np.array([150.0, 400.0])
        self.__canvas = canvas
        self.__jumpStrength = jumpStrength
        self.__yVel = 0
        self.__gravity = gravity
        self.__width = size
        
        self.__score = 0
        self.__render()

    def __render(self):
        self.__canvasObj = self.__canvas.create_oval(*self.__coords-self.__width,
                                                     *self.__coords+self.__width,
                                                     fill="yellow")  
        
    def checkCollision(self, pipe):
        if self.__coords[1] < pipe.getGapTopY() or self.__coords[1] > pipe.getGapBotY():
            print("crashed at top or bot")
            return True
        x1, y1, x2, y2 = self.__findClosestPointsToPipe(pipe)
        if DEBUG:
            self.__canvas.create_line(*self.__coords, x1, y1, tag="line")
            self.__canvas.create_line(*self.__coords, x2, y2, tag="line")
        if self.__checkPointCollideWithBird(x1, y1):
            return True
        return self.__checkPointCollideWithBird(x2, y2)
        # ^ this returns false if no collisions
        
        
    def __findClosestPointsToPipe(self, pipe):
        top, bot= pipe.getGapTopY(), pipe.getGapBotY()
        if self.__coords[0] < pipe.getLeftMostX():
            return pipe.getLeftMostX(), top, pipe.getLeftMostX(), bot
            
        elif self.__coords[0] > pipe.getRightMostX():
            return pipe.getRightMostX(), top, pipe.getRightMostX(), bot
        
        else:
            return self.__coords[0], top, self.__coords[0], bot
        
    def __checkPointCollideWithBird(self, x, y):
        distSquared = ((self.__coords[0] - x)**2) + ((self.__coords[1] - y)**2)
        return True if distSquared < (self.__width**2) else False
        
    def getLeftMostX(self):
        return self.__coords[0]-self.__width
        
    def getRightMostX(self):
        return self.__coords[0]+self.__width
    
    def getX(self):
        return self.__coords[0]
    
    def move(self):
        self.__yVel += self.__gravity
        self.__coords[1] += self.__yVel
        self.__canvas.move(self.__canvasObj, 0, self.__yVel)
    
    def jump(self):
        self.__yVel = self.__jumpStrength
        
    def getScore(self):
        return self.__score
        
    def incrementScore(self):
        self.__score += 1
        
    