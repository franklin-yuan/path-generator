import pygame as pg 
import numpy as np

clicked = False
objClicked = False

class utils:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
    
def runOnce(f):
    def wrapper(*args, **kwargs):
        if not wrapper.has_run:
            wrapper.has_run = True
            return f(*args, **kwargs)
    wrapper.has_run = False
    return wrapper
    
def half(a): 
    return a / 2

def getMousePos(): #gets coordinates of mouse pointer
    pos = pg.mouse.get_pos()
    return pos

def arToPos(Xar, Yar): #turns arrays (x and y) into array of poses
    poses = []
    for i in range(len(Xar)):
        poses.append((Xar[i], Yar[i])) 
    
    return poses   

def scalePos(pos, scaleVal):
    return (pos[0] * scaleVal, pos[1] * scaleVal)

def turnToVector(pos, pos1): 
    newPos = (pos[0] - pos1[0], pos[1] - pos1[1])
    return newPos

def addVector(pos, vec):
    return (pos[0] + vec[0], pos[1] + vec[1]) 

def drawDashedLine(surface, color, start_pos, end_pos, width = 1, dash_length = 10, exclude_corners = True):
    
    # convert tuples to numpy arrays
    start_pos = np.array(start_pos)
    end_pos   = np.array(end_pos)

    # get euclidian distance between start_pos and end_pos
    length = np.linalg.norm(end_pos - start_pos)

    # get amount of pieces that line will be split up in (half of it are amount of dashes)
    dash_amount = int(length / dash_length)

    # x-y-value-pairs of where dashes start (and on next, will end)
    dash_knots = np.array([np.linspace(start_pos[i], end_pos[i], dash_amount) for i in range(2)]).transpose()

    return [pg.draw.line(surface, color, tuple(dash_knots[n]), tuple(dash_knots[n+1]), width)
            for n in range(int(exclude_corners), dash_amount - int(exclude_corners), 2)]

def drag(event, ar1 = [], ar2 = []): #ar1 and ar2 are arrays of objects that can be clicked
    global clicked, objClicked
    if event.type == pg.MOUSEBUTTONDOWN:
        if event.button == 1:
            clicked = True
    elif event.type == pg.MOUSEBUTTONUP:
        clicked = False
    
    if clicked == True:
        pos = pg.mouse.get_pos()
        x = pos[0]
        y = pos[1]
        for object in ar1:
            if object.collidepoint(pos):
                object.x = x - (object.width / 2)
                object.y = y - (object.height / 2)
        for object in ar2:
            if object.collidepoint(pos):
                object.x = x - (object.width / 2)
                object.y = y - (object.height / 2)
            
                
def delPoint(event, ar1, ar2): #ar1 and ar2 are arrays of objects that can be clicked
    if event.type == pg.MOUSEBUTTONDOWN:
        pos = pg.mouse.get_pos()
        if event.button == 3:
            for object in ar1:
                if object.collidepoint(pos):
                    ar2.pop(ar1.index(object))
                    ar1.remove(object)
                    
    

