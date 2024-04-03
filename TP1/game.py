from cmu_graphics import *
import random
import copy



class Platform:
    def __init__(self):
        self.platform = []
        cols = 10
        begin = 0
        self.platform = [0]* cols
        # ind = 1
        ind = random.randint(0, cols-1)
        self.platform[ind] = 1
        self.y = 70
        self.constant = 70
        
    def draw(self, count):
        #have the platforms drawn here
        for j in range(5):
            if self.platform[j] ==0:
                color = 'blue'
            elif self.platform[j] == 2:
                color = 'green'
            else:
                color = 'red'
            
            self.y = self.constant +count*80 
            drawRect(200 +(j*20), self.y , 20, 20, fill = color)
            
            
    def move(self, direction):
        if direction == 'right':
            self.platform = [self.platform[len(self.platform)-1]] + self.platform[:len(self.platform)-1]
        if direction == 'left':
            self.platform = self.platform[1:] + [self.platform[0]]
    
    def empty(self):
        for i in range(len(self.platform)):
            self.platform[i] = 2
    
    def shift(self, key):
        if self.y >=self.constant: 
            self.constant -= key
        else:
            return True
        
            
        
class Ball():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = 7
    
        #velocity
        self.dy =-1
        
        #acceleration
        self.ddy = 0.1
    
    def draw(self):
        drawCircle(self.x, self.y, self.r, fill = 'purple')
        
    def step(self, direction):
        self.dy *= direction
        if direction == -1:
            self.dy = -5
            self.ddy = 0.3
        self.y += self.dy
        self.dy += self.ddy
        



def onAppStart(app):
    app.width = 500
    app.height = 500
    app.cols =5
    app.start = 0
    app.end = app.start + app.cols
    app.platList = []
    for i in range(8):
        app.platList.append(Platform())
    app.copy = copy.deepcopy(app.platList)
    app.currPlat = app.platList[0]
    app.platY = app.currPlat.y
    app.ballList = [Ball(212,24)]
    app.currNum =0
    app.gameOver = False
    
def redrawAll(app):
    # print(app.gameOver)
    if not app.gameOver:
        count = 0
        for platform in app.platList:
            platform.draw(count)
            count+=1
    
        for ball in app.ballList:
            ball.draw()
    else:
        gameOverScreen(app)

def onKeyPress(app, key):
    if key == 'right':
        for platform in app.platList:
            platform.move(key)
            
    if key =='left':
        for platform in app.platList:
            platform.move(key)

def onStep(app):
    
    for ball in app.ballList:
        app.gameOver = gameOver(ball.y)
        if not app.gameOver:
            if collided(app, ball.x, ball.y, ball.r)[0]:
                ball.step(-1)
            else:
                ball.step(1)
            
            
            #updates the level the ball is on
            for i in range(len(app.platList)):
                if i == len(app.platList):
                    continue
                elif i == 0:
                    if ball.y <= app.platList[i].y:
                        app.currPlat = app.platList[i]
                        app.currNum = i
                else:
                    if ball.y <= app.platList[i].y and  ball.y >= app.platList[i-1].y:
                        app.currPlat = app.platList[i]
                        app.currNum = i
        if app.currNum !=0:
            # app.platList = app.platList[app.currNum -1:]
            for i in range(len(app.platList)):
                if i > len(app.platList): continue
                print(i, len(app.platList))
                platform = app.platList[i]
                if i < app.currNum:
                    for j in range(len(platform.platform)):
                        platform.platform[j] = 2
                        
                if app.platList[app.currNum].y != 70:
                    platform.shift(1)
                if platform.y < 0:
                    # app.platList = app.platList[i:]
                    count2 = False
                

                
                if app.currPlat.y == 70:
                    print('hi')
                    app.platList = app.platList[app.currNum:]
                    for i in range (app.currNum):
                        app.platList.append(Platform())

                # print(len(app.platList))
            
    


def collided(app, x, y, r):
    platform = app.platList[app.currNum]
    if platform.platform[0] == 1:
        return [False, 'red']
        
    elif ( y + r > platform.y):
        return [True, 'blue']
    return [False, None] #idk if i ever use none... or the colors honestly

def gameOver(y):
    if y < 0:
        return True
    return False

def gameOverScreen(app):
    drawRect(0, 0, app.height, app.width, fill = 'black')
        
def main():
    runApp()
    
main()