from cmu_graphics import *
import random
import copy
import platform_1
import ball_1
import drawScreen

def onAppStart(app):
    app.width = 500
    app.height = 500
    app.cols =5
    app.splash = True
    app.instruction = False
    app.highScore = 0
    reset(app)

    
def reset(app):  

    #create a list that contains all the platforms
    app.platList = []
    for i in range(8):
        app.platList.append(platform_1.Platform(i))

    app.currPlat = app.platList[0]
    app.ballList = [ball_1.Ball(212,24)]
    app.currNum =0
    app.gameOver = False
    app.pause = False
    app.score = 0

    
def redrawAll(app):
    if not app.splash:
        for platform in app.platList:
            platform.draw()
    
        for ball in app.ballList:
            ball.draw()
        drawScreen.displayScore(app)
        drawScreen.drawInstructionButton(app)
        drawScreen.drawResetButton(app)
        drawScreen.drawPauseButton(app)
        drawScreen.drawHighScore(app)
        
        if app.gameOver:
            drawScreen.gameOverScreen(app)
        if app.pause:
            drawScreen.pauseScreen(app)
        
    else:
        drawScreen.drawSplash(app)
    

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
        else:
            reset(app)


def onStep(app):
    if not app.splash:
        if not app.gameOver:
            if not app.pause:

                #continuously check on step if the ball has hit the platform or not
                for ball in app.ballList:
                    collision = collided(app, ball.x, ball.y, ball.r)
                    if collision[0]:
                        if collision[1] != 'red':
                            #the ball collided with platform so we make it go in the other direction
                            ball.step(-1, app.currNum)
                    else:
                        ball.step(1, app.currNum)
                    
                    
                    #updates the level the ball is on
                    for i in range(len(app.platList)):
                        if i == len(app.platList):
                            continue
                        elif i == 0:
                            #this updates the currNum if the ball passes the first platform
                            if ball.y <= app.platList[i].y:
                                app.currPlat = app.platList[i]
                                app.currNum = i
                        else:
                            #this updates the currNum by checking if the ball is between 2 platforms
                            if ball.y <= app.platList[i].y and  ball.y >= app.platList[i-1].y:
                                app.currPlat = app.platList[i]
                                
                                #By checking if app.currNum is not equal to i, we make sure 
                                #that the platform has just been changed. By doing this we can append
                                #the right amount of platforms to the end of our platList
                                if app.currNum != i:
                                    app.platList.append(platform_1.Platform(len(app.platList)))
                                    if collided(app, ball.x, ball.y, ball.r)[0]:
                                        ball.step(-1, app.currNum)
                                    else:
                                        ball.step(1, app.currNum)
                                app.currNum = i

                    #checks if the platform has been passed and then makes it dissapear    
                    if app.currNum !=0:
                        for i in range(len(app.platList)):
                            platform = app.platList[i]
                            if i < app.currNum:
                                for j in range(len(platform.platform)):
                                    platform.platform[j] = 1
                            
                            #if the current platform is not on top, it shifts it upward       
                            if app.platList[app.currNum].y != 80:
                                platform.shift(2)
                                
                        #recreate the platform list to take away the platforms from before
                        if app.currPlat.y == 80:
                            app.platList = app.platList[app.currNum:] 
                            if len(app.platList) > 10:
                                app.platList = app.platList[:11]
                            app.currNum =0

                        #this is to make sure the distance between the platforms is consistent
                            for i in range(len(app.platList)):
                                platform = app.platList[i]
                                platform.constant = 80
                                platform.count = i

                            app.currPlat = app.platList[0]


#this function return if the ball has collided with the platform, 
#and the color of the box it has collided with
def collided(app, x, y, r):
    platform = app.platList[app.currNum]
    
    if (platform.platform[0] == 1 
        and y + r > platform.y):
        #increase the score since the ball passed a platform
        app.score +=10
        return [False, 'red']
    
    elif (y + r > platform.y 
        and platform.platform[0] == 2):
        #the ball has collided with the red box, so game over
        app.gameOver = True
        #update highscore
        if app.score > app.highScore:
            app.highScore = app.score
    
    elif ( y + r >= platform.y):
        return [True, 'blue']
    
    return [False, None] 

                   
    
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

    

def gameOver(y):
    if y < 0:
        return True
    return False


def main():
    runApp()
    
main()