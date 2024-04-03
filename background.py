from cmu_graphics import *
import random
import copy
from PIL import Image
#citations: https://en.wikipedia.org/wiki/Voronoi_diagram, https://www.youtube.com/watch?v=vcfIJ5Uu6Qw, 
# https://www.ronja-tutorials.com/post/028-voronoi-noise/#summary

#additionally took help from Pat's 11/21 lecture on Images

def backgroundStart(app):
    app.setMaxShapeCount(300000)
    app.width = 500
    app.height = 500
    app.row = 5
    app.col = 5
    app.side = 500 //5 #app.width
    app.board = [([None] * app.col) for row in range(app.row)]
    app.pointList = []
    # p = [[0]*5 for row in range(5) ]
    app.pixelList =[ [0]*500 for row in range(500) ]
    app.colorList = [(255, 223, 211),  (254, 200, 216), (210, 145, 188), (149, 125, 173),(224, 187, 228)]*5
    app.img = Image.new(mode = "RGB", size =(500,500), color= 'white')
    app.pixel_map = app.img.load()
    
    

    class Point():
        def __init__(self, row, col, side):
            self.x = random.randint((row*app.side)+1, (row+1)*app.side)
            self.y = random.randint((col*app.side)+1, (col+1)*app.side)

        
        def __eq__(self, other):
            return self.x == other.x and self.y == other.y
        
# this basically creates random points in different regions of the screen
# by creating a grid, I can make sure the points are spread out
    for i in range(len(app.board)):
        for j in range(len(app.board)):
            point = Point(i, j, app.side)
            app.pointList.append(point)
            app.board[i][j] = (point.x, point.y)
    
    update(app, app.pixelList)
    for i in range(500):
        for j in range(500):
            color = app.pixelList[i][j]
            app.pixel_map[i, j] = app.colorList[color]
    app.img.save("output", format="png")
    app.imCMU = CMUImage(app.img)

def background2(app):
    return app.imCMU


#the update function basically updates the pixelList so that it keeps track of the point closest to it
def update(app, L):
    pointCopy =copy.deepcopy(app.pointList)
    for i in range(500):
        for j in range(500):
            x = findClosestPoint(L[i][j], i ,j, pointCopy)
            index = app.pointList.index(x[1])
            L[i][j] = index


#this uses backtracking to find which point is the closest
def findClosestPoint(A, i, j, L):
    if len(L) == 1:
        return [distance(i, j, L[0]), L[0]]
    else:
        currPoint = L[0]
        rest = L[1:]
        currDist = distance(i, j, currPoint)
        restDist = findClosestPoint(A, i, j, rest)
        if currDist <  restDist[0]:
            return [currDist, currPoint]
        else:
            return restDist

#distance formula from what we learned in CS academy
def distance(x0, y0, currPoint):
    (x1, y1) = currPoint.x, currPoint.y
    return ((x1 - x0)**2 + (y1 - y0)**2)**0.5

