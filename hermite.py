import numpy as np
import matplotlib.pyplot as plt
import util

#----------------------------------------------------- ALL SPLINE CLASSES
class point:
    x = 0.0
    y = 0.0
    cx = 0.0
    cy = 0.0
    end = False
    
class segment:
    concluded = False
    userPoints = []
    ctrlPoints = []
    def __init__(self):
        self.clearAll()
    #----------------------------------------------------- ALL SPLINE FUNCS
    def clearAll(self):
        self.v = 0.0 #tangential vel
        self.omega = 0.0 #angular vel

        #array of points
        self.xpoints = []
        self.ypoints = []
        self.cxpoints = []
        self.cypoints = []

        self.xar = []
        self.yar = []
        self.t = 0.0

    def loadUserPos(self, poses): #loads the x and y coordinates into respective arrays (pos is a tuple, pygame format)
        for pos in poses: self.xpoints.append(pos[0]); self.ypoints.append(pos[1])
        
    def loadCtrlPos(self, poses):
        for pos in poses: self.cxpoints.append(pos[0]); self.cypoints.append(pos[1])

    @staticmethod
    def findX(point1,point2,t): #given 2 points, generate x values for the spline along the two points
        a1 = (2 * point1.x) + (-2 * point2.x) + (point1.cx) + (point2.cx)
        b1 = (-3 * point1.x) + (3 * point2.x) + (-2 * point1.cx) + (-1 * point2.cx)
        c1 = point1.cx
        d1 = point1.x
        return a1*(t**3) + b1*(t**2) + c1*(t) + d1

    @staticmethod
    def findY(point1,point2,t): #given 2 points, generate x values for the spline along the two points
        a2 = (2 * point1.y) + (-2 * point2.y) + (point1.cy) + (point2.cy) 
        b2 = (-3 * point1.y) + (3 * point2.y) + (-2 * point1.cy) + (-1 * point2.cy)
        c2 = point1.cy
        d2 = point1.y
        
        return a2*(t**3) + b2*(t**2) + c2*(t) + d2

    
    def shiftCtrlPoints(self): #only for visual stuff. Adds the ctrl vector to it's related point for a better visualisation.
        for i in range(len(self.cxpoints)):
            self.cxpoints[i] = self.xpoints[i] + self.cxpoints[i]
            self.cypoints[i] = self.ypoints[i] + self.cypoints[i]

    def calcPts(self, res): #returns array of poses, no drawing
        newPoses = []
        returnPoses = []
        point1 = point()
        point2 = point()
        for i in range(len(self.xpoints)-1):
            self.t = np.linspace(0,1,num=res)
            point1.x = self.xpoints[i]
            point2.x = self.xpoints[i+1]
            point1.y = self.ypoints[i]
            point2.y = self.ypoints[i+1]
            point1.cx = self.cxpoints[i]
            point2.cx = self.cxpoints[i+1]
            point1.cy = self.cypoints[i]
            point2.cy = self.cypoints[i+1]
            self.xar.append(self.findX(point1, point2, self.t))
            self.yar.append(self.findY(point1, point2, self.t))
        # print("\n\n\n\n\n hhHhHh")
        
        for i in range(len(self.xar)):
            newPoses = util.arToPos(self.xar[i], self.yar[i])
            for pos in newPoses:
                returnPoses.append(pos)
                
        self.clearAll()
        return returnPoses

def writeToTxt(segments): #run at end of program. Takes the calculated points and crams into a txt file
    txt = open('paths/path.txt', 'w')
    for pos in calcAllPts(50, segments):
        entry = str(pos[0]) + " " + str(pos[1]) + "\n"
        txt.write(entry)
    txt.close()
        
def clearAllAll(segments):
    for seg in segments:
        seg.v = 0.0 #tangential vel
        seg.omega = 0.0 #angular vel

        #array of points
        seg.xpoints = []
        seg.ypoints = []
        seg.cxpoints = []
        seg.cypoints = []

        seg.xar = []
        seg.yar = []
        seg.t = 0.0
        
def drawMPL(res, segments): #draw matplotlib spline
    plt.figure(figsize=(10, 10))
    
    for seg in segments:
    
        point1 = point()
        point2 = point()
        
        for i in range(len(seg.xpoints)-1):
            
            t = np.linspace(0,1,num=res)
            point1.x = seg.xpoints[i]
            point2.x = seg.xpoints[i+1]
            point1.y = seg.ypoints[i]
            point2.y = seg.ypoints[i+1]
            point1.cx = seg.cxpoints[i]
            point2.cx = seg.cxpoints[i+1]
            point1.cy = seg.cypoints[i]
            point2.cy = seg.cypoints[i+1]
            xar = seg.findX(point1, point2, t)
            yar = seg.findY(point1, point2, t)
            # for j in range(len(xar)):
            #     print("[",xar[j],yar[j],end="]")
            plt.plot(xar,yar,'k',linewidth=2.0)
    
    plt.plot(seg.xpoints,seg.ypoints, 'b.', markersize = 10.0)
    plt.plot(seg.cxpoints,seg.cypoints, 'm.', markersize = 6.0)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
    
def calcAllPts(res, segments): #returns array of poses, no drawing
    
    for seg in segments:
        newPoses = []
        returnPoses = []
        point1 = point()
        point2 = point()
        for i in range(len(seg.xpoints)-1):
            seg.t = np.linspace(0,1,num=res)
            point1.x = seg.xpoints[i]
            point2.x = seg.xpoints[i+1]
            point1.y = seg.ypoints[i]
            point2.y = seg.ypoints[i+1]
            point1.cx = seg.cxpoints[i]
            point2.cx = seg.cxpoints[i+1]
            point1.cy = seg.cypoints[i]
            point2.cy = seg.cypoints[i+1]
            seg.xar.append(seg.findX(point1, point2, seg.t))
            seg.yar.append(seg.findY(point1, point2, seg.t))
        # print("\n\n\n\n\n hhHhHh")
        
        for i in range(len(seg.xar)):
            newPoses = util.arToPos(seg.xar[i], seg.yar[i])
            for pos in newPoses:
                returnPoses.append(pos)
            
    seg.clearAll()
    return returnPoses