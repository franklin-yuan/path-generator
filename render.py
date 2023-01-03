import os
import pygame as pg 
import hermite as hm
import util 

pg.font.init()

#----------------------------------------------------- ALL GUI GLOBALS
WIDTH, HEIGHT = 876, 900
WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Spline Tool")

BLACK      = (  0,   0,   0)
WHITE      = (255, 255, 255)
BLUE       = (  0,   0, 255)
GREEN      = (  0, 255,   0)
RED        = (255,   0,   0)
DUSTYBLUE  = (136, 155, 174)
PASTELBLUE = (174, 198, 207)
DARKBLUE   = ( 25,  69, 105)
PASTELRED  = (255, 105,  97)
GRAY       = (100, 100, 100)
GRAINSBORO = (220, 220, 220)

segments = []
currentSegment = 0 #index number of the current segment we are editing
update = False

FPS = 144

FIELD_WIDTH, FIELD_HEIGHT = 876, 594
ROBOT_WIDTH, ROBOT_HEIGHT = 60, 60
PATH_DOT_WIDTH, PATH_DOT_HEIGHT = 2, 2
USER_POINT_WIDTH, USER_POINT_HEIGHT = 22, 22
CTRL_POINT_WIDTH, CTRL_POINT_HEIGHT = 16, 16
USER_CIRCLE_RAD = (USER_POINT_WIDTH - 2) / 2 
CTRL_CIRCLE_RAD = (CTRL_POINT_WIDTH - 2) / 2 
CENTER_CIRCLE_RAD = 1
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
PATH_DOT_IMAGE = pg.image.load(os.path.join('assets','spline_path_dot.png'))
PATH_DOT_IMAGE = pg.transform.scale(PATH_DOT_IMAGE, (PATH_DOT_WIDTH, PATH_DOT_HEIGHT))

INSTRUC_FONT = pg.font.SysFont('arial', 20)

SCALING_CONST = 10 #Arbitrary units for how tall / wide the field should be
CONTROL_SHIFT_HEIGHT = (1 / SCALING_CONST) * ACTIVE_RANGE_Y_N

CTRL_VEC_SCALING_CONST = 3

SPLINE_RESOLUTION_WIN = 15 #how many line segments that will be rendered between 2 target points (well how many points calculated but pretty much same thing), this one is for the draggable window, lower to improve performance
SPLINE_RESOLUTION_MPL = 25 #this one is for the graph that pops up


TARGET_POINT_CLR = DUSTYBLUE
CTRL_POINT_CLR = PASTELBLUE
TARGET_TO_CTRL_LINE_CLR = GRAINSBORO
SPLINE_LINE_CLR = DARKBLUE

#----------------------------------------------------- ALL GUI FUNCS
def drawWindow(robot):
    WIN.fill(WHITE)
    renderImages(robot)
    renderText()
    updateUserPoint()
    updateCtrlPoint()
    
    if len(segments[currentSegment].userPoints) >= 2:
        parseAllCoords()
        for i in range(len(segments)):
            updateSpline(segments[i].calcPts(SPLINE_RESOLUTION_WIN))
        
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
    y = SCALING_CONST - y
    
    return (x,y)

def unscaleCoords(pos):
    # print("i run")
    x = pos[0]
    y = pos[1]
    x /= SCALING_CONST; x *= ACTIVE_RANGE_X_N; x += ACTIVE_RANGE_X[0]
    y = SCALING_CONST - y
    y /= SCALING_CONST; y *= ACTIVE_RANGE_Y_N; y += ACTIVE_RANGE_Y[0]
    # print(x,y)
    
    return (x,y)
    
def inRangeOfField(pos):
    if pos[0] >= ACTIVE_RANGE_X[0] and pos[0] <= ACTIVE_RANGE_X[1] and pos[1] >= ACTIVE_RANGE_Y[0] and pos[1] <= ACTIVE_RANGE_Y[1]:
        return True
    else:
        return False
    
def drawUserPoint(): #draws the user point when f is pushed
    pos = getMousePos()
    corner = (pos[0] - (USER_POINT_WIDTH / 2), pos[1] - (USER_POINT_HEIGHT / 2))
    if inRangeOfField(pos) == True: #check if mouse pointer is within the field image
        userPoint = pg.Rect(corner[0], corner[1], USER_POINT_WIDTH, USER_POINT_HEIGHT)
        drawCtrlPoint(corner, pos)
        segments[currentSegment].userPoints.append(userPoint)
        
def updateUserPoint():
    for userPoint in collateSegPoints("user"):
        pg.draw.circle(WIN, TARGET_POINT_CLR, (userPoint.x + (userPoint.width / 2), userPoint.y + (userPoint.height / 2)), USER_CIRCLE_RAD, 3)
        pg.draw.circle(WIN, TARGET_POINT_CLR, (userPoint.x + (userPoint.width / 2), userPoint.y + (userPoint.height / 2)), CENTER_CIRCLE_RAD, 1)
        
def drawCtrlPoint(pos, pos1): #draws the control point for tge point created when f is pushed #pos is corner, pos1 is actual
    if pos[1] >= ACTIVE_RANGE_Y[0] + CONTROL_SHIFT_HEIGHT: #if at top of the screen
        newPos = (pos[0], pos[1] - CONTROL_SHIFT_HEIGHT)
        top = True
    else:
        newPos = (pos[0], pos[1] + CONTROL_SHIFT_HEIGHT) #moves the control point a bit higher
        top = False
    
    ctrlPoint = pg.Rect(newPos[0], newPos[1], CTRL_POINT_WIDTH, CTRL_POINT_HEIGHT)
    segments[currentSegment].ctrlPoints.append(ctrlPoint)
    
def updateCtrlPoint(): #updates the control point's pos as well as draw the line between the user point and the ctrl point
    i = 0
    for ctrlPoint in collateSegPoints("ctrl"):
        pg.draw.circle(WIN, CTRL_POINT_CLR, (ctrlPoint.x + (ctrlPoint.width / 2), ctrlPoint.y + (ctrlPoint.height / 2)), CTRL_CIRCLE_RAD, 3) 
        pg.draw.circle(WIN, CTRL_POINT_CLR, (ctrlPoint.x + (ctrlPoint.width / 2), ctrlPoint.y + (ctrlPoint.height / 2)), CENTER_CIRCLE_RAD, 1) 
        util.drawDashedLine(WIN, TARGET_TO_CTRL_LINE_CLR, (collateSegPoints("user")[i].x + (collateSegPoints("user")[i].width / 2), collateSegPoints("user")[i].y + (collateSegPoints("user")[i].height / 2)), (ctrlPoint.x + (ctrlPoint.width / 2), ctrlPoint.y + (ctrlPoint.height / 2)), 3, 3)
        i += 1

def drawEndPoint():
    global currentSegment
    currentSegment += 1
    segments.append(hm.segment())

def parseAllCoords():
    cornerUX = [] #coords of the corner of target points
    cornerUY = []
    cornerCX = [] #coords of the corner of the control points
    cornerCY = []
    adjUX = [] #adjusted coords of target points
    adjUY = []
    adjCX = [] #adjusted coords of control points
    adjCY = []
    
    for j in range(len(segments)):
    
        for userPoint in segments[j].userPoints:
            cornerUX.append(userPoint.x)
            cornerUY.append(userPoint.y)
        
        for ctrlPoint in segments[j].ctrlPoints:
            cornerCX.append(ctrlPoint.x)
            cornerCY.append(ctrlPoint.y)
        
        for x in cornerUX: adjUX.append(x + (USER_POINT_WIDTH / 2))
        for y in cornerUY: adjUY.append(y + (USER_POINT_HEIGHT / 2))
        for x in cornerCX: adjCX.append(x + (CTRL_POINT_WIDTH / 2))
        for y in cornerCY: adjCY.append(y + (CTRL_POINT_HEIGHT / 2))
        
        userPoses = util.arToPos(adjUX, adjUY)
        ctrlPoses = util.arToPos(adjCX, adjCY)
        
        for i in range(len(userPoses)): userPoses[i] = scaleCoords(userPoses[i]) 
        for i in range(len(ctrlPoses)): ctrlPoses[i] = scaleCoords(ctrlPoses[i])
        
        # print(ctrlPoses[0])
        # print(userPoses[0])
        
        for i in range(len(ctrlPoses)): ctrlPoses[i] = util.turnToVector(ctrlPoses[i], userPoses[i]); ctrlPoses[i] = util.scalePos(ctrlPoses[i], CTRL_VEC_SCALING_CONST)
        
        # print(ctrlPoses[0])
        # print(userPoses[0])
        
        segments[j].loadUserPos(userPoses)
        segments[j].loadCtrlPos(ctrlPoses)
    #run this at the end to loop thorugh all points and control points, currently the thing is being fed only where they pressed k, not the final pos
        
def updateSpline(poses):#this needes to be in real time
    newPoses = [] #unscaled stuff
    for pos in poses:
        newPos = unscaleCoords(pos)
        newPoses.append(newPos)
    
    for i in range(len(newPoses) - 1):
        # print(poses[i], poses[i+1])
        pg.draw.line(WIN, SPLINE_LINE_CLR, newPoses[i], newPoses[i+1], 2)
    
    
    # for pos in newPoses:
    #     pg.draw.circle(WIN, GREEN, pos, 1, 0)

def collateSegPoints(choice):
    userPts = []
    ctrlPts = []
    for seg in segments:
        for i in range(len(seg.userPoints)):
            userPts.append(seg.userPoints[i])
            ctrlPts.append(seg.ctrlPoints[i])
    
    if choice.lower() == "user":
        return userPts
    elif choice.lower() == "ctrl":
        return ctrlPts
        

#----------------------------------------------------- MAIN
def main():
    segments.append(hm.segment()) #create initial segment
    
    robot = pg.Rect(200, 200, ROBOT_WIDTH, ROBOT_HEIGHT)
    clock = pg.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pg.event.get():
            if inRangeOfField(getMousePos()) == True:
                util.drag(event, collateSegPoints("user"), collateSegPoints("ctrl"),)
                util.delPoint(event, collateSegPoints("user"), collateSegPoints("ctrl"))
            
            if event.type == pg.QUIT:
                run = False
                
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_f:
                    drawUserPoint() #CREATE POINT ON KEY F PRESS      
                if event.key == pg.K_g:
                    drawEndPoint() #CREATE THE ENDING POINT FOR THE SEGMMENT
                    
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    update = True    
                elif event.type == pg.MOUSEBUTTONUP:
                    update = False
        
        drawWindow(robot)
            
    pg.quit()
    hm.clearAllAll(segments)
    parseAllCoords()
    hm.drawMPL(SPLINE_RESOLUTION_MPL, segments)
    hm.writeToTxt(segments)
    
if __name__ == "__main__":
    main()
    