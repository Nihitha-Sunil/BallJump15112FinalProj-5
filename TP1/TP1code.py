from cmu_graphics import *
import random
import copy


#create a platform class
class Platform:
    def __init__(self, count):
        self.platform = []
        self.cols = 5
        begin = 0
        self.platform = self.createPlatform()
        self.y = 70
        self.constant = 70
        self.count = count

    def createPlatform(self):
        platform = [0]* self.cols
        ind = 1
        # ind = random.randint(0, self.cols-1)
        platform[ind] = 1
        num = self.cols//2
        prev = -1
        for i in range(num):
            x =(random.randint(0, self.cols-1))
            if x != ind and x != prev and x !=0:
                platform[x] = 2
            prev = x
        
        return platform
        
        
    def draw(self):
        #have the platforms drawn here
        for j in range(5):
            if self.platform[j] ==0:
                color = 'blue'
                borderC = 'black'
            elif self.platform[j] == 2:
                color = 'red'
                borderC = 'black'
            else:
                color = None
                borderC = None
            
            self.y = self.constant + self.count *80 
            drawRect(200 +(j*20), self.y , 20, 20, fill = color, border = borderC)
            
            
    def move(self, direction):
        # moves the platform right or left based on user input
        if direction == 'right':
            self.platform = [self.platform[len(self.platform)-1]] + self.platform[:len(self.platform)-1]
        if direction == 'left':
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
        


class Coin():
    def __init__(self, y):
        self.x = random.randint(200, 300)
        self.y = y
        self.r = 3
    
    def draw(self):
        drawCircle(self.x, self.y, 10, fill = 'yellow')
        
    def shift(self, key):
        self.y -= key
        
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
    app.splash = True
    reset(app)
    app.pause = False
    app.instruction = False
    app.highScore = 0

    
def reset(app):  
    app.platList = []
    for i in range(8):
        app.platList.append(Platform(i))
    app.copy = copy.deepcopy(app.platList)
    app.currPlat = app.platList[0]
    app.platY = app.currPlat.y
    app.ballList = [Ball(212,24)]
    app.currNum =0
    app.gameOver = False
    app.score = 0
    app.step = 0
    
def redrawAll(app):
    # print(app.gameOver)
    if not app.splash:
        # count = 0
        for platform in app.platList:
            platform.draw()
            # count+=1
    
        for ball in app.ballList:
            ball.draw()
        displayScore(app)
        drawInstructionButton(app)
        drawResetButton(app)
        drawPauseButton(app)
        drawHighScore(app)
        
        if app.gameOver:
            gameOverScreen(app)
        if app.pause:
            pauseScreen(app)
        
    else:
        drawSplash(app)
    

def onKeyPress(app, key):
    app.splash = False
    if not app.splash:

        if not app.gameOver:
            if key == 'right':
                for platform in app.platList:
                    platform.move(key)
                    
            elif key =='left':
                for platform in app.platList:
                    platform.move(key)
            elif key == 'p':
                    app.pause = not app.pause
            # elif key == 's':
            #     takeStep(app)
        else:
            reset(app)




def onStep(app):
    print(len(app.platList))
    if not app.splash:
        if not app.gameOver:
            if not app.pause:
                for ball in app.ballList:
                    if collided(app, ball.x, ball.y, ball.r)[0]:
                        ball.step(-1)
                    else:
                        ball.step(1)
                    
                    
                    #updates the level the ball is on
                    for i in range(len(app.platList)):
                        # print(ball.y, app.platList[i].y, 'sheeeeeee')
                        if i == len(app.platList):
                            continue
                        elif i == 0:
                            if ball.y <= app.platList[i].y:
                                app.currPlat = app.platList[i]
                                app.currNum = i
                        else:
                            if ball.y <= app.platList[i].y and  ball.y >= app.platList[i-1].y:
                                app.currPlat = app.platList[i]
                                if app.currNum != i:
                                    print('yo')
                                    app.platList.append(Platform(len(app.platList)))
                                app.currNum = i
                                # print('changed currNum')

                    #checks if the platform has been passed and then makes it dissapear    
                    if app.currNum !=0:
                        for i in range(len(app.platList)):
                            platform = app.platList[i]
                            if i < app.currNum:
                                for j in range(len(platform.platform)):
                                    platform.platform[j] = 1
                            
                            #if the current platform is not on top, it shifts it upward       
                            if app.platList[app.currNum].y != 70:
                                # print('shifted')
                                platform.shift(2)
                                
                        createP = app.currNum
                            #recreate the platform list to take away the platforms from before
                        if app.currPlat.y == 70:
                            # print(app.currNum)
                            # print(app.platList[app.currNum].y)
                            # print(len(app.platList), app.platList[0].y)
                            app.platList = app.platList[app.currNum:] 
                            # print(len(app.platList), app.platList[0].y,'hehe')
                            app.currNum =0

                            
                            
                            app.currPlat = app.platList[0]
                            # print(app.currNum, 'newlist')
                            # for i in range (createP):
                            #     app.platList.append(Platform(len(app.platList)))
                    #     print(app.platList[0].y, '------')
                    #     print(app.platList[app.currNum].y, '------')
                    # print('ooooo')
                            
                   
    
def onMousePress(app, mouseX, mouseY):
    if inInstructionButton(mouseX, mouseY):
        app.splash = True
    
    if inResetButton(mouseX, mouseY):
        reset(app)
        
    if inPauseButton(mouseX, mouseY):
        app.pause = not app.pause

def inInstructionButton(x, y):
    if x >10 and x < 110 and y >30 and y < 50:
        return True
    return False
    
def inPauseButton(x, y):
    if x >10 and x < 80 and y >60 and y < 80:
        return True
    return False

def inResetButton(x, y):
    if x >10 and x < 80 and y >90 and y < 110:
        return True
    return False

    
def collided(app, x, y, r):
    platform = app.platList[app.currNum]
    if (platform.platform[0] == 1 
        and y + r > platform.y):
        app.score +=10
        return [False, 'red']
    elif (y + r > platform.y 
        and platform.platform[0] == 2):
        app.gameOver = True
        if app.score > app.highScore:
            app.highScore = app.score
    elif ( y + r > platform.y):
        return [True, 'blue']
    return [False, None] 

def gameOver(y):
    if y < 0:
        return True
    return False
    
def drawInstructionButton(app):
    drawRect(10, 30, 100, 20, fill = 'black')
    drawLabel('Instructions', 60, 40, fill = 'white', font = 'orbitron', align = 'center', bold = True)

def drawPauseButton(app):
    drawRect(10, 60, 70, 20, fill = 'black')
    drawLabel('Pause', 45, 70, fill = 'white', font = 'orbitron', align = 'center', bold = True)

def drawResetButton(app):
    drawRect(10, 90, 70, 20, fill = 'black')
    drawLabel('Reset', 45, 100, fill = 'white', font = 'orbitron', align = 'center', bold = True)
    
def drawSplash(app):
    drawRect(0,0, app.width, app.height, fill = 'black', opacity = 100)
    drawRect(app.width//2, 50, 350, 80, align = 'center', fill = None, border = 'white', borderWidth = 5)
    drawLabel('Ball Jump', app.width//2, 50, size = 60, font='orbitron', fill = 'white', bold = True)
    drawLabel('(press any key to continue)', app.width//2, 105, size = 16, font='orbitron', fill = RGB(192,234,255), bold = True)
    drawLabel(' Instructions:', app.width//2, 130, size = 20, font='orbitron', fill = RGB(192,234,255), bold = True)
    drawLabel('Use right arrow to move the platform right', app.width//2, 160, size = 16, font='orbitron', fill = RGB(192,234,255))
    drawLabel('Use left arrow to mover the platform left',app.width//2, 190, size = 16, font='orbitron', fill = RGB(192,234,255))
    drawLabel('if you land on green you lose', app.width//2, 220, size = 16, font='orbitron', fill = RGB(192,234,255))
    drawLabel('P to Pause',app.width//2, 250, size = 16, font='orbitron', fill = RGB(192,234,255))
    drawLabel('Each row you pass, you gain 10 points', app.width//2, 280, size = 16, font='orbitron', fill = RGB(192,234,255))
    drawLabel('Avoid obstacles', app.width//2, 300, size = 16, font='orbitron', fill = RGB(192,234,255))

def gameOverScreen(app):
    drawRect(0, 0, app.width, app.height, fill = 'black', opacity = 75)
    drawLabel('Game Over!', app.width//2, app.height//2, size = 40, fill = 'white', bold = True, font='orbitron')
    drawLabel('Press any key to start a new game', app.width//2, app.height//2 + 40, size = 15, fill = 'white', bold = True, font='orbitron')

def pauseScreen(app):
    drawRect(0, 0, app.width, app.height, fill = 'black', opacity = 75)
    drawLabel(chr(0x23f8), app.width//2, app.height//2 - 60, size=100, font='symbols', fill = 'white')
    drawLabel('Paused', app.width//2, app.height//2, size = 40, fill = 'white', bold = True, font='orbitron')
    drawLabel('Press p to unpause', app.width//2, app.height//2 + 40, size = 15, fill = 'white', bold = True, font='orbitron')

def displayScore(app):
    drawLabel(f'score: {app.score}', 10, 15, size = 16, font='orbitron', fill = 'black', bold = True, align = 'left')
    
def drawHighScore(app):
    drawLabel(f'Highest Score: {app.highScore}', 10, 480, size = 16, font='orbitron', fill = 'black', bold = True, align = 'left')
    
    
def main():
    runApp()
    
main()