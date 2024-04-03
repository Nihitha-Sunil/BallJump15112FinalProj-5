from cmu_graphics import *
import random

class Platform:
    def __init__(self, count):
        self.platform = []
        self.cols = 5
        begin = 0
        self.shieldNum = -1
        self.skipNum = -1
        self.platform = self.createPlatform()
        self.y = 80
        self.constant = 80
        self.count = count
        

    def createPlatform(self):
        platform = [0]* self.cols
        #choose a random index of this list and set it equal to 1, 
        # this will be the empty cell
        ind = random.randint(1, self.cols-1)
        platform[ind] = 1
        

        #randomly choose spot for 'obstacle'/ red box
        num = self.cols//2
        prev = {0, -1}
        for i in range(num):
            x =(random.randint(0, self.cols-1))
            if x != ind and x not in prev:
                platform[x] = 2
            prev.add(x)
        
        return platform
        
        
    def draw(self):
        #have the platforms drawn here
        for j in range(5):
            if self.platform[j] ==0:
                # color = gradient( RGB(156, 37, 71),RGB(240, 163, 185), RGB(232, 179, 194), start='right-bottom')
                color = gradient( 'mediumVioletRed', rgb(227, 109, 184), rgb(255, 182, 193), start='right-bottom')
                borderC = rgb(156, 20, 105)
            elif self.platform[j] == 2:
                color = gradient( 'fireBrick','crimson', 'lightCoral', start='right-bottom')
                borderC = 'darkRed'
            else:
                color = None
                borderC = None
            
            self.y = self.constant + self.count *80 
            drawRect(200 +(j*20), self.y , 20, 20, fill = color, border = borderC, borderWidth = 1.5)
            
            
    def move(self, direction):
        #don't do anything since it cannot be controlled by clicks
        pass

    def move2(self):
        self.platform = self.platform[1:] + [self.platform[0]]
    
    def empty(self):
        #makes the platform dissapear
        for i in range(len(self.platform)):
            self.platform[i] = 1
    
    def shift(self, key):
        #shifts the platform upwards when the platforms before dissapears
        if self.y >=self.constant: 
            self.constant -= key
        else:
            return True