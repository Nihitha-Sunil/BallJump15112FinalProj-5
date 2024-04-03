from cmu_graphics import *
import random
import copy
import platform_1
import platform_2
import ball_1
import drawScreen
import background
import json 

def onAppStart(app):
    app.width = 500
    app.height = 500
    app.cols =5
    app.splash = True
    app.instruction = False
    app.leaderboard = False
    loadScores(app)

    app.count=0
    reset(app)

    #creates the background using voronoi noise algorithm
    background.backgroundStart(app)

    

    
def reset(app):  
    app.difficulty = 0
    #create a list that contains all the platforms
    app.platList = []
    for i in range(8):
        p = random.randint(0,101)
        if p<=5 + app.difficulty and i!=0:
            #appends a harder platform --> as score increases, difficulty increases, thus 
            #higher chance to get a harder platform
            app.platList.append(platform_2.Platform(i))
        else:
            app.platList.append(platform_1.Platform(i))

    app.currPlat = app.platList[0]
    app.ballList = [ball_1.Ball(212,24)]
    app.currNum =0
    app.gameOver = False
    app.pause = False
    app.score = 0
    app.shield = False
    app.shieldSec = 0
    app.skip = False
    app.imageX = 0
    app.imageY = 0
    app.skipTrue = False
    app.skipSec = 0

    
def redrawAll(app):
    drawImage(app.imCMU,0,0)
    if not app.splash:
        if not app.leaderboard:
            
            drawScreen.displayScore(app)
            drawScreen.drawInstructionButton(app)
            drawScreen.drawResetButton(app)
            drawScreen.drawPauseButton(app)
            drawScreen.drawLeaderBoardButton(app)
            drawScreen.drawHighScore(app)
            
            if app.gameOver:
                drawScreen.gameOverScreen(app)
                app.scoresSet.add(app.score)
            elif app.pause:
                drawScreen.pauseScreen(app)
            else:
                if app.shield:
                    drawScreen.drawShield(app)
                if app.skipTrue:
                    drawScreen.drawSkip(app)
                #draws ball
                for ball in app.ballList:
                    ball.draw()
                for platform in app.platList:
                    platform.draw()
        else:
            drawScreen.drawLeaderBoard(app)
        
    else:
        drawScreen.drawSplash(app)
    

def onKeyPress(app, key):
    
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
    app.splash = False
    app.leaderboard = False


def onStep(app):
    app.count+=1

    #increases difficulty based on score
    app.difficulty = app.count//100

    if not app.splash:
        #check shield and skip
        checkShield(app)
        checkSkip(app)
        
        if not app.gameOver:
            if not app.pause:
                if app.count%20 ==0:
                    for platform in app.platList:
                        platform.move2()      
                #continuously check on step if the ball has hit the platform or not
                for ball in app.ballList:
                    collision = collided(app, ball.x, ball.y, ball.r)
                    if collision[0]:
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
                                    p = random.randint(0,101)
                                    if p<=10 + app.difficulty:
                                        app.platList.append(platform_2.Platform(len(app.platList)))
                                    else:
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
                                    #also makes the powerups dissapear
                                    platform.shield = False
                                    platform.skip = False
                            
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
        if platform.shieldNum==0:
            platform.shield = False
        if platform.skipNum == 0:
            platform.skip = False
        return [False, None]
    
    elif (y + r > platform.y 
        and platform.platform[0] == 2):
        #the ball has collided with the red box, so game over
        if app.shield:
            return [True, 'red']
        app.gameOver = True
        app.scoresSet.add(app.score)
        if app.score > app.highScore:
            app.highScore = app.score
        #update highscore
        app.scoresSet.add(app.score)
        if app.score > app.highScore:
            app.highScore = app.score
        createHighScore(app)
        app.shield = False
        app.skipTrue = False
    
    elif ( y + r >= platform.y):
        #the ball colided with a blue box
        if platform.shieldNum ==0:
            platform.shield = False
        if platform.skipNum == 0:
            platform.skip = False
        return [True, 'blue']
    
    return [False, 'red'] 

def checkShield(app):
    #checks whether the shield is True
    if app.currPlat.shieldNum == 0 and app.shield != True:
            app.shield = True
            app.shieldSec = 0
    if app.shield:
        app.shieldSec +=1
        if app.shieldSec >= 200:
            app.shield = False
    else:
        app.shieldSec = 0

def checkSkip(app):
    #need seperate variables that keeps track of when the skip background runs
    if app.skipTrue:
        app.skipSec +=1
        if app.skipSec >=100:
            app.skipTrue = False
            app.skipSec = 0
    if app.currPlat.skipNum == 0 and app.skip != True:
            app.skip = True
            app.skipTrue = True
    if app.skip:
        for i in range(len(app.currPlat.platform)):
            app.currPlat.shield = False
            app.currPlat.skip = False
            app.currPlat.platform[i] = 1
            app.platList[app.currNum+1].platform[i] = 1
        app.skip = False
   

def onMousePress(app, mouseX, mouseY):
    if inInstructionButton(mouseX, mouseY):
        app.splash = True
    
    if inResetButton(mouseX, mouseY):
        reset(app)
        
    if inPauseButton(mouseX, mouseY):
        app.pause = not app.pause

    if inLeaderboardButton(mouseX, mouseY):
        app.leaderboard = True

#buttons
def inInstructionButton(x, y):
    if x >10 and x < 110 and y >30 and y < 50:
        return True
    return False
    
def inLeaderboardButton(x, y):
    if x >10 and x < 110 and y >60 and y < 80:
        return True
    return False

def inPauseButton(x, y):
    if x >10 and x < 80 and y >90 and y < 110:
        return True
    return False

def inResetButton(x, y):
    if x >10 and x < 80 and y >120 and y < 140:
        return True
    return False



    

def gameOver(y):
    if y < 0:
        return True
    return False

def createHighScore(app):
    with open("scores.json", "w") as f:
        app.scoresList = list(app.scoresSet)
        app.scoresList.sort(reverse = True)
        app.scoresList = app.scoresList[:5]
        json.dump(app.scoresList, f)
    

def loadScores(app):
    try:
        with open("scores.json", "r") as f:
            app.scoresList = json.load(f)
            app.scoresList.sort(reverse = True)
            if len(app.scoresList)!= 0:
                app.highScore = app.scoresList[0]
            else: app.highScore = 0

    except FileNotFoundError:
        app.scoresList = []
        app.highScore = 0
    
    app.scoresSet = set(app.scoresList)



def main():
    runApp()
    
main()
