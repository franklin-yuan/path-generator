import os
import numpy as np
from matplotlib import pyplot as plt
import pygame as pg 

pg.font.init()

#----------------------------------------------------- ALL GUI GLOBALS
WIDTH, HEIGHT = 876, 900
WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Spline Tool")

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
BLUE =      (  0,   0, 255)
GREEN =     (  0, 255,   0)
RED =       (255,   0,   0)

userPoints = []

FPS = 60
FIELD_WIDTH, FIELD_HEIGHT = 876, 594
ROBOT_WIDTH, ROBOT_HEIGHT = 60, 60
USER_POINT_WIDTH, USER_POINT_HEIGHT = 5, 5
BORDER_WIDTH, BORDER_HEIGHT = 550, 550

BORDER = pg.Rect((FIELD_WIDTH- BORDER_WIDTH) / 2, (FIELD_HEIGHT - BORDER_HEIGHT) / 2, BORDER_WIDTH, BORDER_HEIGHT)

ACTIVE_RANGE_X = (200, 680)
ACTIVE_RANGE_Y = (80, 560)
FIELD_IMAGE = pg.image.load(os.path.join('assets','vex_field.png'))
FIELD_IMAGE = pg.transform.scale(FIELD_IMAGE, (FIELD_WIDTH, FIELD_HEIGHT))
ROBOT_IMAGE = pg.image.load(os.path.join('assets','robot_square.png'))
ROBOT_IMAGE = pg.transform.scale(ROBOT_IMAGE, (ROBOT_WIDTH, ROBOT_HEIGHT))

INSTRUC_FONT = pg.font.SysFont('comicsans', 30)

#----------------------------------------------------- ALL SPLINE GLOBALS
v = 0.0 #tangential vel
omega = 0.0 #angular vel

#array of points
xpoints = []
ypoints = []
cxpoints = []
cypoints = []

xar = []
yar = []
t = 0.0

class point:
    x = 0.0
    y = 0.0
    cx = 0.0
    cy = 0.0
    end = False

#----------------------------------------------------- ALL SPLINE FUNCS
def loadXY(pos):
    xpoints.append(pos[0])
    ypoints.append(pos[1])

def findX(point1,point2,t): #given 2 points, generate x values for the spline along the two points
    a1 = (2 * point1.x) + (-2 * point2.x) + (point1.cx) + (point2.cx)
    b1 = (-3 * point1.x) + (3 * point2.x) + (-2 * point1.cx) + (-1 * point2.cx)
    c1 = point1.cx
    d1 = point1.x
    return a1*(t**3) + b1*(t**2) + c1*(t) + d1

def findY(point1,point2,t): #given 2 points, generate x values for the spline along the two points
    a2 = (2 * point1.y) + (-2 * point2.y) + (point1.cy) + (point2.cy) 
    b2 = (-3 * point1.y) + (3 * point2.y) + (-2 * point1.cy) + (-1 * point2.cy)
    c2 = point1.cy
    d2 = point1.y
    
    return a2*(t**3) + b2*(t**2) + c2*(t) + d2

def drawMPL(): #draw matplotlib spline
    plt.figure(figsize=(10, 10))
    point1 = point()
    point2 = point()
    
    for i in range(len(xpoints)-1):
        
        t = np.linspace(0,1,num=100)
        point1.x = xpoints[i]
        point2.x = xpoints[i+1]
        point1.y = ypoints[i]
        point2.y = ypoints[i+1]
        point1.cx = cxpoints[i]
        point2.cx = cxpoints[i+1]
        point1.cy = cypoints[i]
        point2.cy = cypoints[i+1]
        xar = findX(point1, point2, t)
        yar = findY(point1, point2, t)
        for j in range(len(xar)):
            print("[",xar[j],yar[j],end="]")
        plt.plot(xar,yar,'k',linewidth=2.0)
    
    plt.plot(xpoints,ypoints, 'b.', markersize = 10.0)
    plt.plot(cxpoints,cypoints, 'm.', markersize = 6.0)
    plt.xlabel('x')
    plt.ylabel('y')
        
    plt.show()

#----------------------------------------------------- ALL GUI FUNCS

def drawWindow(robot):
    WIN.fill(WHITE)
    WIN.blit(FIELD_IMAGE, (0,0))
    WIN.blit(ROBOT_IMAGE, (robot.x, robot.y))
    
    for userPoint in userPoints:
        pg.draw.circle(WIN, RED, (userPoint.x, userPoint.y) , USER_POINT_HEIGHT)
    
    INSTRUC_TEXT = INSTRUC_FONT.render("INSTRUCTIONS: PRESS F TO CREATE TARGET POINT", 1, BLACK)
    WIN.blit(INSTRUC_TEXT, (10, FIELD_HEIGHT))
    
    pg.display.update()
    
def getMousePos():
    pos = pg.mouse.get_pos()
    return pos

def drawUserPoint():
    pos = getMousePos()
    if pos[0] >= ACTIVE_RANGE_X[0] and pos[0] <= ACTIVE_RANGE_X[1] and pos[1] >= ACTIVE_RANGE_Y[0] and pos[1] <= ACTIVE_RANGE_Y[1]: #check if mouse pointer is within the field image
        userPoint = pg.Rect(pos[0], pos[1], USER_POINT_WIDTH, USER_POINT_HEIGHT)
        userPoints.append(userPoint)
        loadXY(pos)
    
def main():
    
    robot = pg.Rect(200, 200, ROBOT_WIDTH, ROBOT_HEIGHT)
    
    clock = pg.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_f:
                    drawUserPoint()
    
            # CREATE POINT
            
        
        drawWindow(robot)
            
    pg.quit()
    
    print(xpoints)
    print(ypoints)


if __name__ == "__main__":
    main()
