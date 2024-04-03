from cmu_graphics import *
    
def drawInstructionButton(app):
    color = gradient('darkMagenta','indigo')
    drawRect(10, 30, 100, 20, fill = color, border = 'indigo')
    drawLabel('Instructions', 60, 40, fill = rgb(254, 200, 216), font = 'monospace', align = 'center', bold = True)

def drawLeaderBoardButton(app):
    color = gradient('darkMagenta','indigo')
    drawRect(10, 60, 100, 20, fill = color, border = 'indigo')
    drawLabel('Leaderboard', 60, 70, fill = rgb(254, 200, 216), font = 'monospace', align = 'center', bold = True)

def drawPauseButton(app):
    color = gradient('darkMagenta','indigo')
    drawRect(10, 90, 70, 20, fill = color, border = 'indigo')
    drawLabel('Pause', 45, 100, fill = rgb(254, 200, 216), font = 'monospace', align = 'center', bold = True)

def drawResetButton(app):
    color = gradient('darkMagenta','indigo')
    drawRect(10, 120, 70, 20, fill = color, border = 'indigo')
    drawLabel('Reset', 45, 130, fill = rgb(254, 200, 216), font = 'monospace', align = 'center', bold = True)


def drawShield(app):
    drawRect(10,10, 480, 480, fill = 'lightBlue', opacity = 40, border = 'blue', borderWidth = 4)
    drawLabel('Shield',app.width//2, 22, size = 19, fill = 'blue', bold = True, font='monospace')
def drawSkip(app):
    drawRect(10,10, 480, 480, fill = 'lightGreen', opacity = 40, border = 'green', borderWidth = 4)
    drawLabel('Skip',app.width//2, 22, size = 19, fill = 'green', bold = True, font='monospace')

def drawSplash(app):
    drawRect(0,0, app.width, app.height, fill = 'indigo', opacity = 20)
    drawRect(app.width//2, 80, 350, 80, align = 'center', fill = None, border = 'indigo', borderWidth = 5)
    drawLabel('Ball Jump', app.width//2, 80, size = 60, font='monospace', fill = 'indigo', bold = True)
    drawLabel('(press any key to continue)', app.width//2, 135, size = 16, font='monospace', fill = 'indigo', bold = True)
    drawLabel(' Instructions:', app.width//2, 170, size = 20, font='monospace', fill = 'indigo', bold = True)
    drawLabel('Use right arrow to move the platform right', app.width//2, 200, size = 16, font='monospace', fill = 'indigo', bold = True)
    drawLabel('Use left arrow to mover the platform left',app.width//2, 230, size = 16, font='monospace', fill = 'indigo', bold = True)
    drawLabel('if you land on red you lose', app.width//2, 260, size = 16, font='monospace', fill = 'indigo', bold = True)
    drawLabel('P to Pause',app.width//2, 290, size = 16, font='monospace', fill = 'indigo', bold = True)
    drawLabel('Shield protects you from dying ', app.width//2, 320, size = 16, font='monospace', fill = 'indigo', bold = True)
    drawLabel('Skip lets you skip 2 platforms', app.width//2, 350, size = 16, font='monospace', fill = 'indigo', bold = True)

def gameOverScreen(app):
    drawRect(0, 0, app.width, app.height, fill = 'indigo', opacity = 30)
    drawLabel('Game Over!', app.width//2, app.height//2, size = 40, fill = 'indigo', bold = True, font='monospace')
    drawLabel('Press any key to start a new game', app.width//2, app.height//2 + 40, size = 15, fill = 'indigo', bold = True, font='monospace')

def pauseScreen(app):
    drawRect(0, 0, app.width, app.height, fill = 'indigo', opacity = 30)
    # drawLabel(chr(0x23f8), app.width//2, app.height//2 - 60, size=100, font='symbols', fill = 'indigo')
    drawLabel('Paused', app.width//2, app.height//2, size = 60, fill = 'indigo', bold = True, font='monospace')
    drawLabel('Press p to unpause', app.width//2, app.height//2 + 60, size = 15, fill = 'indigo', bold = True, font='monospace')

def drawLeaderBoard(app):
    drawRect(0, 0, app.width, app.height, fill = 'black', opacity = 25)
    drawLabel('Leaderboard', app.width//2, 100, size = 40, fill = 'indigo', bold = True, font = 'monospace')
    scoresList = list(app.scoresSet)
    scoresList.sort(reverse = True)
    scoresList = app.scoresList[:5]
    if len(scoresList) == 0:
        drawLabel('No High scores', app.width//2, 200, size = 20, fill = 'indigo',font = 'monospace', bold = True)
    else:
        for i in range(len(scoresList)):
            drawLabel(f'{i+1}: {scoresList[i]}', app.width//2, 200+(i*20), size = 20, fill = 'indigo', bold = True, font = 'monospace')
    drawLabel('(press any key to continue)', app.width//2, 350, size = 16, font='monospace', fill = 'indigo', bold = True)

def displayScore(app):
    drawLabel(f'score: {app.score}', 10, 15, size = 16, font='monospace', fill = 'indigo', bold = True, align = 'left')
    
def drawHighScore(app):
    drawLabel(f'Highest Score: {app.highScore}', 10, 480, size = 16, font='monospace', fill = 'indigo', bold = True, align = 'left')
    
    