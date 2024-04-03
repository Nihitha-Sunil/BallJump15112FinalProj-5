from cmu_graphics import *
import random
from PIL import Image
import os, pathlib

class Platform:
    def __init__(self, count):
        self.platform = []
        self.cols = 5
        begin = 0
        self.count = count

        #create shield
        self.shield = False
        self.shieldNum = -1
        if self.count!= 0:
            p = random.randint(0, 101)
            if p < 10:
                self.shield = True
                self.shieldNum = random.randint(0, 5)
            else:
                self.shield = False
        
        #create Skip
        self.skip = False
        self.skipNum = -1
        if self.count!= 0:
            p2 = random.randint(0, 101)
            if p2 < 5:
                self.skip = True
                self.skipNum = random.randint(0, 5)
                if self.skipNum == self.shieldNum:
                    self.skip = False
                    self.skipNum = -1
            else:
                self.skip = False
    
        
        self.platform = self.createPlatform()
        self.y = 80
        self.constant = 80
        

        
        

    def createPlatform(self):
        platform = [0]* self.cols
        #choose a random index of this list and set it ecual to 1, 
        # this will be the empty cell
        ind = random.randint(1, self.cols-1)
        platform[ind] = 1

        #randomly choose spot for 'obstacle'/ red box
        num = random.randint(0, self.cols//2 +1)
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
                color = gradient( 'indigo','darkMagenta', rgb(210, 145, 188), start='right-bottom')
                borderC = 'indigo'
            elif self.platform[j] == 2:
                color = gradient( 'fireBrick','crimson', 'lightCoral', start='right-bottom')
                borderC = 'darkRed'
            else:
                color = None
                borderC = None
            
            self.y = self.constant + self.count *80 
            drawRect(200 +(j*20), self.y , 20, 20, fill = color, border = borderC, borderWidth = 1.5)
            
            #draw Shield Icon and Skip Icon
            if self.shield == True and j == self.shieldNum:
                image = openImage("image/shield2.png")
                image = CMUImage(image)
                drawImage(image, 200 +(j*20), self.y-20,width = 20, height =20)
            if self.skip == True and j == self.skipNum:
                image2 = openImage("image/skip3.png")
                image2 = CMUImage(image2)
                drawImage(image2, 196 +(j*20), self.y-30,width = 30, height =30)
                # drawCircle(200 +(j*20), self.y-10,5, fill = 'red')
                
            
            
    def move(self, direction):
        # moves the platform and powerups right or left based on user input
        if direction == 'right':
            self.platform = [self.platform[len(self.platform)-1]] + self.platform[:len(self.platform)-1]
            if self.shield:
                if self.shieldNum == 4:
                    self.shieldNum = 0
                else:
                    self.shieldNum +=1
            if self.skip:
                if self.skipNum == 4:
                        self.skipNum = 0
                else:
                    self.skipNum +=1
        if direction == 'left':
            self.platform = self.platform[1:] + [self.platform[0]]
            if self.shield:
                if self.shieldNum == 0:
                        self.shieldNum = 4
                else:
                    self.shieldNum -=1
            if self.skip:
                if self.skipNum == 0:
                        self.skipNum = 4
                else:
                    self.skipNum -=1
    def move2(self):
        pass
    
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
        
def openImage(fileName):
        return Image.open(os.path.join(pathlib.Path(__file__).parent,fileName))
    
    