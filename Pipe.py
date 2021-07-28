from random import randint

DEBUG = True


class Pipe:
    def __init__(self, canvas, pipeGap, pipeVel, windowSize):
        self.__canvas = canvas
        self.__x = windowSize[0]
        self.__width = 60
        self.__gap = pipeGap
        self.__pipeVel = pipeVel
        self.__gapStartY = randint(100,windowSize[1]-200)
        self.__windowSize = windowSize
        self.render()
        
    def getTopRect(self):
        x0 = self.__x
        y0 = 0
        x1 = self.__x + self.__width
        y1 = self.__gapStartY
        return x0,y0,x1,y1

    def getBotRect(self):
        x0 = self.__x
        y0 = self.__gapStartY + self.__gap
        x1 = self.__x + self.__width
        y1 = self.__windowSize[1]
        return x0,y0,x1,y1
    
    def render(self):
        self.__topRect = self.__canvas.create_rectangle(self.getTopRect(), fill="lightgreen")
        self.__botRect = self.__canvas.create_rectangle(self.getBotRect(), fill="lightgreen")
        self.__canvas.tag_lower(self.__topRect)
        self.__canvas.tag_lower(self.__botRect) # makes sure text it at front
        
        
        
    def move(self):
        self.__canvas.move(self.__topRect, self.__pipeVel, 0)
        self.__canvas.move(self.__botRect, self.__pipeVel, 0)
        self.__x += self.__pipeVel
        return False if self.__x + self.__width < 0 else True
            
    def getRightMostX(self):
        return self.__x + self.__width 
    
    def getLeftMostX(self):
        return self.__x
    
    def getGapTopY(self):
        return self.__gapStartY

    def getGapBotY(self):
        return self.__gapStartY + self.__gap
        
        