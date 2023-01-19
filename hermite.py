import numpy as np
import matplotlib.pyplot as plt
import util

#----------------------------------------------------- ALL SPLINE GLOBALS

#array of points
xpoints = []
ypoints = []
cxpoints = []
cypoints = []

xar = []
yar = []
car = [] #curvature array
t = 0.0

#----------------------------------------------------- ALL SPLINE CLASSES
class point:
    x = 0.0
    y = 0.0
    cx = 0.0
    cy = 0.0
    end = False
    
#----------------------------------------------------- ALL SPLINE FUNCS
def clearAll():
    global v, omega, xpoints, ypoints, cxpoints, cypoints, xar, yar, t
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

def loadUserPos(poses): #loads the x and y coordinates into respective arrays (pos is a tuple, pygame format)
    for pos in poses: xpoints.append(pos[0]); ypoints.append(pos[1])
    
def loadCtrlPos(poses):
    for pos in poses: cxpoints.append(pos[0]); cypoints.append(pos[1])

def findX(point1, point2, t): #given 2 points, generate x values for the spline along the two points
    a1 = (2 * point1.x) + (-2 * point2.x) + (point1.cx) + (point2.cx)
    b1 = (-3 * point1.x) + (3 * point2.x) + (-2 * point1.cx) + (-1 * point2.cx)
    c1 = point1.cx
    d1 = point1.x
    return a1*(t**3) + b1*(t**2) + c1*(t) + d1

def findXDer(point1, point2, t, degree): #derivatives
    a1 = (2 * point1.x) + (-2 * point2.x) + (point1.cx) + (point2.cx)
    b1 = (-3 * point1.x) + (3 * point2.x) + (-2 * point1.cx) + (-1 * point2.cx)
    c1 = point1.cx
    d1 = point1.x
    
    if degree == 1:
        return 3*a1*(t**2) + 2*b1*t + c1
    elif degree == 2:
        return 6*a1*t + 2*b1

def findY(point1, point2, t): #given 2 points, generate x values for the spline along the two points
    a2 = (2 * point1.y) + (-2 * point2.y) + (point1.cy) + (point2.cy) 
    b2 = (-3 * point1.y) + (3 * point2.y) + (-2 * point1.cy) + (-1 * point2.cy)
    c2 = point1.cy
    d2 = point1.y
    
    return a2*(t**3) + b2*(t**2) + c2*(t) + d2

def findYDer(point1, point2, t, degree): #given 2 points, generate x values for the spline along the two points
    a2 = (2 * point1.y) + (-2 * point2.y) + (point1.cy) + (point2.cy) 
    b2 = (-3 * point1.y) + (3 * point2.y) + (-2 * point1.cy) + (-1 * point2.cy)
    c2 = point1.cy
    d2 = point1.y
    
    if degree == 1:
        return 3*a2*(t**2) + 2*b2*t + c2
    elif degree == 2:
        return 6*a2*t + 2*b2

def shiftCtrlPoints(): #only for visual stuff. Adds the ctrl vector to it's related point for a better visualisation.
    for i in range(len(cxpoints)):
        cxpoints[i] = xpoints[i] + cxpoints[i]
        cypoints[i] = ypoints[i] + cypoints[i]

def drawMPL(res): #draw matplotlib spline
    plt.figure(figsize=(10, 10))
    point1 = point()
    point2 = point()
    
    for i in range(len(xpoints)-1):
        
        t = np.linspace(0,1,num=res)
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
        # for j in range(len(xar)):
        #     print("[",xar[j],yar[j],end="]")
        plt.plot(xar,yar,'k',linewidth=2.0)
    
    plt.plot(xpoints,ypoints, 'b.', markersize = 10.0)
    plt.plot(cxpoints,cypoints, 'm.', markersize = 6.0)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

def calcPts(res):
    global car
    car = []
    newPoses = []
    returnPoses = []
    point1 = point()
    point2 = point()
    for i in range(len(xpoints)-1):
        t = 0
        while t < 1:
            t += 0.01
            point1.x = xpoints[i]
            point2.x = xpoints[i+1]
            point1.y = ypoints[i]
            point2.y = ypoints[i+1]
            point1.cx = cxpoints[i]
            point2.cx = cxpoints[i+1]
            point1.cy = cypoints[i]
            point2.cy = cypoints[i+1]
            xar.append(findX(point1, point2, t))
            yar.append(findY(point1, point2, t))
            
            xFirstDer = findXDer(point1, point2, t, 1)
            xSecondDer = findXDer(point1, point2, t, 2)
            yFirstDer = findYDer(point1, point2, t, 1)
            ySecondDer = findYDer(point1, point2, t, 2)
            
            # a = util.ar_times(xFirstDer, ySecondDer)
            # b = util.ar_times(yFirstDer, xSecondDer)
            # c = util.ar_power_const(xFirstDer, 2.0)
            # d = util.ar_power_const(yFirstDer, 2.0)
            # e = util.ar_minus(a, b)
            # f = util.ar_power_const(util.ar_add(d, e), 1.5)
            
            kappa = (xFirstDer * ySecondDer - yFirstDer * xSecondDer) / (xFirstDer ** 2.0 + yFirstDer ** 2.0) ** 0.5
        
        # kappa = util.ar_divide(e, f)
        
            car.append(kappa)
    # print("\n\n\n\n\n hhHhHh")
    
    newPoses = util.arToPos(xar, yar)
    for pos in newPoses:
        returnPoses.append(pos)
            
    clearAll()
    return returnPoses

def writeToTxt():
    txt = open('paths/path.txt', 'w')
    n = 0
    for pos in calcPts(50):
        entry = str(pos[0]) + " " + str(pos[1]) + " " + str(car[n]) + "\n"
        txt.write(entry)
        n += 1
    txt.close()
    
# def calcVelocities():
    
#     v = 0.0
#     omega = 0.0 
#     #angular vel
#     #tangential vel
    
#     v_max = 100;
#     a_t_max = 20;
#     a_omega_max = 20;
#     omega_max = 100;
#     f_max = 3
#     #consts
    
#     txt = open('paths/path.txt', 'r')
#     read = txt.readlines()
    
#     pts = []
#     vel = []
    
#     for line in read:
#         linecoords = line.split()
#         for i in range(2):
#             linecoords[i] = float(linecoords[i])
#         pts.append(linecoords)
        
#     vel = [None] * len(pts)
    
#     #parse data from path 
    
#     print(pts)
    
#     dt = v_i = ds = a_t = c_i = 0
    
#     #dt = delta t, v_t is velocity (tangential) at i, ds is delta s (arc length), a_t is tangential accel, c_i is curvature at i
    
#     startv = 0
#     endv = 0
    
#     vel[0] = startv
    
#     arcl_i = 0
    
#     for i in range(1, len(pts) - 1):
#         c_i = pts[i][2]
        
#         vel_t_max = (vel[i-1]**2.0 + 2*ds*a_t_max)
        
#         dt = (2 * util.distance((pts[i][0], pts[i][1]), (pts[i-1][0], pts[i-1][1]))) / (vel[i] + vel[i-1])
        
        
#         v_max_omega = 0.0;
        
#         v_max_omega = omega_max / abs(c_i)
        
#         v_min_a_t = v[i-1] - a_t_max * dt
#         v_max_a_t = v[i-1] + a_t_max * dt
        
#         v_hat = (2 * ds * a_omega_max) / c_i * v[i-1]

def calcVelocities(v_start: float, v_end: float) -> tuple[float, float]:
    
    #CONSTS
    a_rad_max = 2; #ms^-2
    a_tan_max = 1.5; #ms^-2
    v_max = 4
    
    txt = open('paths/path.txt', 'r')
    read = txt.readlines()
    
    pts = []
    c = [] #curvatures
    omega = [] #omegalul
    
    for line in read:
        linecoords = line.split()
        for i in range(3):
            linecoords[i] = float(linecoords[i])
        pts.append(linecoords)
        
    for x in pts:
        c.append(x[2])
        
    v = [None] * len(pts) #velocities
    
    # plotPointsWithT(c)
        
    v[0] = v_start #set first vel to userinput start value
    v[len(pts) - 1] = v_end #and same here but for end

    t = 0
    d = 0
    A = a_tan_max ** 2 # max tangential accel ^ 2 just for naming
    B = a_rad_max ** 2 # max radial accel ^ 2 just for naming
    
    for i in range(len(pts) - 1):
    
        
        #just for naming, _i means current point, _ii means i+1 or next pt
        
        v_i = v_ii = c_i = 0
        
        v_i = v[i]
        c_i = c[i]
        
        dt = ds = 0
        
        pt_i = pts[i]
        pt_ii = pts[i+1]
        
        ds = util.distance(pt_i, pt_ii)
        
        # v_ii = (B * v[0] + (A * (B ** 2.0) * (t ** 2.0) - A * B * (((v_i ** 2.0) * c_i) ** 2.0)) ** 0.5) / B
        
        v_ii = (v_i ** 2 + 2 * a_tan_max * ds) ** 0.5
        
        # print(v_ii)
        a_tan = a_rad = 0
        
        dt = (2 * ds) / (v_i + v_ii)
        
        # print(dt)
        
        t += dt
        d += ds
        v[i+1] = v_ii
        
    v = correctPlotBackwards(pts, v, c, a_tan_max, a_rad_max, v_max, v_end)
    fixTimePlot(pts, v)
    print(d)
    # print(v)
    
    # plotPointsWithT(v)
        
    #plt.show()
    
    



def plotPointsWithT(x): #this is garbage so probably don't use it
    t = 0
    plt.figure(figsize=(10, 10))
    for i in range(len(x)):
        plt.plot(t, x[i], '.b', markersize = 6.0)
        t += 0.1
        
    plt.show()
    
def correctPlotBackwards(pts, v, c, a_tan_max, a_rad_max, v_max, end):
    v[len(v) - 1] = end
    # print(v)
    for i in range((len(v) - 1), 0, -1):
        v_i = v_ii = c_i = 0
        v_i = v[i]
        v_ii_a = v[i-1]
        c_i = c[i]
        
        dt = ds = 0
        
        pt_i = pts[i]
        pt_ii = pts[i-1]
        
        ds = util.distance(pt_i, pt_ii)    
        
        v_ii = (v_i ** 2 + 2 * a_tan_max * ds) ** 0.5
        
        v_ii = min(v_ii_a, v_ii)
        v_ii = min(v_max, v_ii)
        
        # print(v_ii)
        
        v[i-1] = v_ii
        
    return v
        
def min(a, b):
    if a > b:
        return b
    elif b > a:
        return a
    else:
        print("it didnt work lmao")
    
def fixTimePlot(pts, v):
    t_ar = []
    t = 0
    for i in range(len(pts) - 1):
        
        v_i = v_ii = 0
        
        v_i = v[i]
        v_ii = v[i+1]
        
        dt = ds = 0
        
        pt_i = pts[i]
        pt_ii = pts[i+1]
        
        ds = util.distance(pt_i, pt_ii)
        
        dt = (2 * ds) / (v_i + v_ii)
        # print(dt)
        
        t += dt
        
        t_ar.append(t)
        
    t += dt
    t_ar.append(t)
        
    print(t_ar)
    
    plt.plot(t_ar, v, ".k", linewidth = 2)
    
    plt.show()
    
    
    return t