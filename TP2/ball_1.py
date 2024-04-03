from cmu_graphics import *

class Ball():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = 8
    
        #velocity
        self.dy =-1
        
        #acceleration
        self.ddy = 0.1
    
    def draw(self):
        drawCircle(self.x, self.y, self.r, fill = 'purple')
        
    def step(self, direction, num):
        self.dy *= direction


        if direction == -1 and num != 0:
            self.dy = -7
            self.ddy = 0.4
        elif direction == -1:
            self.dy = -5
            self.ddy = 0.3
        self.y += self.dy
        self.dy += self.ddy