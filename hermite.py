import numpy as np
import matplotlib as plt

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
def loadXY(pos): #loads the x and y coordinates into respective arrays (pos is a tuple, pygame format)
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