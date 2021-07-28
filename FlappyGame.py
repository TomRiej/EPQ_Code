# built in imports
import tkinter as tk
import numpy as np

# my imports
from Bird import Bird
from Pipe import Pipe

# Bird constants
GRAVITY = 0.5
JUMP_STRENGTH = -10
BIRD_SIZE = 20

# Game constants
WINDOW_SIZE = (800,800)
PIPE_GAP = 180
PIPE_VEL = -5
PIPE_SPAWN_RATE = 85
DEFAULT_REFRESH_DELAY = 10

DEBUG = True




# The Game Class
class FlappyBirdGame:
    def __init__(self, master):
        self.__master = master
        self.__master.title("Flappy Bird")
        self.__master.minsize(*WINDOW_SIZE)
        
        self.__frame = tk.Frame(self.__master, 
                              width=WINDOW_SIZE[0],
                              height=WINDOW_SIZE[1])
        
        self.__canvas = tk.Canvas(self.__frame,
                                  width=WINDOW_SIZE[0],
                                  height=WINDOW_SIZE[1],
                                  bg="lightblue")
        self.__canvas.bind("<space>", self.onSpace)
        
        self.__refreshCounter = 0
        self.__refeshAgain = True
        
        self.__pipes = []
        
        
    def onSpace(self, event):
        self.__bird.jump()
    
    def render(self):
        self.__frame.pack()
        self.__canvas.pack()
        self.__canvas.focus_set()
        self.__spawnBird()
        self.__spawnPipe()
        self.__closestPipeIndex = 0
        self.__scoreText = self.__canvas.create_text(WINDOW_SIZE[0]/2, 50,
                                                     text="0",
                                                     font="Verdana 30")
        
        
    def __spawnBird(self):
        self.__bird = Bird(self.__canvas, BIRD_SIZE, JUMP_STRENGTH, GRAVITY)
        
    def __spawnPipe(self):
        self.__pipes.append(Pipe(self.__canvas, PIPE_GAP, PIPE_VEL, WINDOW_SIZE))
        
    def __findClosestPipeIndex(self):
        if self.__pipes[0].getRightMostX() > self.__bird.getLeftMostX():
            return 0
        else:
            return 1
        
    def __moveBirds(self):
        self.__bird.move()
        
    def __movePipes(self):
        for pipe in self.__pipes:
            if not pipe.move():
                self.__pipes.remove(pipe)
                del pipe
    
    def __detectCollisions(self, closestPipe):
        if (closestPipe.getLeftMostX()-BIRD_SIZE) <= self.__bird.getX() <= (closestPipe.getRightMostX()+BIRD_SIZE):
            if self.__bird.checkCollision(closestPipe):
                self.__refeshAgain = False
        
    def update(self):
        if DEBUG:
            self.__canvas.delete("line")
        
        # movement
        self.__moveBirds()
        self.__movePipes()
        newClosestPipeIndex = self.__findClosestPipeIndex()
        closestPipe = self.__pipes[newClosestPipeIndex]
        
        # Collision detection
        self.__detectCollisions(closestPipe)
            
        # Update Score if needed
        if newClosestPipeIndex > self.__closestPipeIndex:
            self.__bird.incrementScore()
            self.__canvas.itemconfig(self.__scoreText,
                                     text=str(self.__bird.getScore()))
        self.__closestPipeIndex = newClosestPipeIndex
        
        # Spawn new pipes
        if self.__refreshCounter > PIPE_SPAWN_RATE:
            self.__spawnPipe()
            self.__refreshCounter = 0
        
        
        
        # refresh
        if self.__refeshAgain:
            self.__refreshCounter += 1
            self.__master.after(DEFAULT_REFRESH_DELAY, self.update)
        else:
            return True
    
    

if __name__ == '__main__':
    root = tk.Tk()
    
    game = FlappyBirdGame(root)
    game.render()
    game.update()
    
    
    root.mainloop()

