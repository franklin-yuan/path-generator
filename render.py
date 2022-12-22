import os
import pygame as pg 
import hermite as hm
import util 

pg.font.init()

#----------------------------------------------------- ALL GUI GLOBALS
WIDTH, HEIGHT = 876, 900
WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Spline Tool")

BLACK      = (   0,   0,   0)
WHITE      = ( 255, 255, 255)
BLUE       = (  0,   0, 255)
GREEN      = (  0, 255,   0)
RED        = (255,   0,   0)
DUSTYBLUE  = (136, 155, 174)
PASTELBLUE = (174, 198, 207)
PASTELRED  = (255, 105,  97)
GRAY       = (100, 100, 100)
GRAINSBORO = (220, 220, 220)

userPoints = []
ctrlPoints = []

clicked = False

FPS = 60
FIELD_WIDTH, FIELD_HEIGHT = 876, 594
ROBOT_WIDTH, ROBOT_HEIGHT = 60, 60
USER_POINT_WIDTH, USER_POINT_HEIGHT = 8, 8
CTRL_POINT_WIDTH, CTRL_POINT_HEIGHT = 6, 6
BORDER_WIDTH, BORDER_HEIGHT = 550, 550

BORDER = pg.Rect((FIELD_WIDTH- BORDER_WIDTH) / 2, (FIELD_HEIGHT - BORDER_HEIGHT) / 2, BORDER_WIDTH, BORDER_HEIGHT)

ACTIVE_RANGE_X = (200, 680) #from what pixel to what pixel in the x direction can user create point
ACTIVE_RANGE_Y = (80, 560) # ^ but with y direction
ACTIVE_RANGE_X_N = ACTIVE_RANGE_X[1] - ACTIVE_RANGE_X[0] #exact numerical range of respective directions
ACTIVE_RANGE_Y_N = ACTIVE_RANGE_Y[1] - ACTIVE_RANGE_Y[0]

FIELD_IMAGE = pg.image.load(os.path.join('assets','vex_field.png'))
FIELD_IMAGE = pg.transform.scale(FIELD_IMAGE, (FIELD_WIDTH, FIELD_HEIGHT))
ROBOT_IMAGE = pg.image.load(os.path.join('assets','robot_square.png'))
ROBOT_IMAGE = pg.transform.scale(ROBOT_IMAGE, (ROBOT_WIDTH, ROBOT_HEIGHT))

INSTRUC_FONT = pg.font.SysFont('arial', 20)

SCALING_CONST = 10 #Arbitrary units for how tall / wide the field should be
CONTROL_SHIFT_HEIGHT = (1 / SCALING_CONST) * ACTIVE_RANGE_Y_N


#----------------------------------------------------- ALL GUI FUNCS

def drawWindow(robot):
    WIN.fill(WHITE)
    renderImages(robot)
    renderText()
    updateUserPoint()
    updateCtrlPoint()
    
    pg.display.update()
    
def renderText():
    INSTRUC_TEXT = INSTRUC_FONT.render("INSTRUCTIONS: PRESS F TO CREATE TARGET POINT", 1, BLACK)
    WIN.blit(INSTRUC_TEXT, (10, FIELD_HEIGHT))
    
def renderImages(robot):
    WIN.blit(FIELD_IMAGE, (0,0))
    WIN.blit(ROBOT_IMAGE, (robot.x, robot.y))
    
def getMousePos(): #gets coordinates of mouse pointer
    pos = pg.mouse.get_pos()
    return pos

def scaleCoords(pos): #scales coordinates selected to 10 x 10
    x = pos[0]
    y = pos[1]
    x -= ACTIVE_RANGE_X[0]; x /= ACTIVE_RANGE_X_N; x *= SCALING_CONST
    y -= ACTIVE_RANGE_Y[0]; y /= ACTIVE_RANGE_Y_N; y *= SCALING_CONST
    return (x,y)
    
def drawUserPoint(): #draws the user point when f is pushed
    pos = getMousePos()
    if pos[0] >= ACTIVE_RANGE_X[0] and pos[0] <= ACTIVE_RANGE_X[1] and pos[1] >= ACTIVE_RANGE_Y[0] and pos[1] <= ACTIVE_RANGE_Y[1]: #check if mouse pointer is within the field image
        userPoint = pg.Rect(pos[0], pos[1], USER_POINT_WIDTH, USER_POINT_HEIGHT)
        drawCtrlPoint(pos)
        userPoints.append(userPoint)
        hm.loadXY(scaleCoords(pos)) 
        
def updateUserPoint():
    for userPoint in userPoints:
        pg.draw.circle(WIN, DUSTYBLUE, (userPoint.x, userPoint.y), USER_POINT_HEIGHT, 3)
    
def drawCtrlPoint(pos): #draws the control point for tge point created when f is pushed
    if pos[1] >= ACTIVE_RANGE_Y[0] + CONTROL_SHIFT_HEIGHT: #if at top of the screen
        newPos = (pos[0], pos[1] - CONTROL_SHIFT_HEIGHT)
        top = True
    else:
        newPos = (pos[0], pos[1] + CONTROL_SHIFT_HEIGHT) #moves the control point a bit higher
        top = False
    
    ctrlPoint = pg.Rect(newPos[0], newPos[1], CTRL_POINT_WIDTH, CTRL_POINT_HEIGHT)
    ctrlPoints.append(ctrlPoint)

def updateCtrlPoint(): #updates the control point's pos as well as draw the line between the user point and the ctrl point
    i = 0
    for ctrlPoint in ctrlPoints:
        pg.draw.circle(WIN, PASTELBLUE, (ctrlPoint.x, ctrlPoint.y), CTRL_POINT_HEIGHT, 3) 
        util.drawDashedLine(WIN, GRAINSBORO, (userPoints[i].x, userPoints[i].y), (ctrlPoint.x, ctrlPoint.y), 3, 3)
        i += 1
    
    
    

def main():
    
    robot = pg.Rect(200, 200, ROBOT_WIDTH, ROBOT_HEIGHT)
    
    run = True
    while run:
        for event in pg.event.get():
            
            util.drag(event, userPoints, ctrlPoints)
            
            if event.type == pg.QUIT:
                run = False
                
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_f:
                    drawUserPoint() #CREATE POINT ON KEY F PRESS          
        
        drawWindow(robot)
            
    pg.quit()
    
    print(hm.xpoints)
    print(hm.ypoints)


if __name__ == "__main__":
    main()
