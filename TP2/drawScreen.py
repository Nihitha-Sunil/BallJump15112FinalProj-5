from cmu_graphics import *
    
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
    
    