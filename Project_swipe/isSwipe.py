import numpy as np
import time
import serial

ser = serial.Serial('COM6',9600)
time.sleep(2)

def swipeVel():
    pullData = open('swipeData.txt','r').read()
    dataArray=pullData.split('\n')
    xar=[]
    yar=[]
    zar=[]
    xVelar=[]
    yVelar=[]
    zVelar=[]
    for eachline in dataArray:
        if len(eachline)>1:
            x,y,z,xVel,yVel,zVel=eachline.split(',')
            xar.append(int(x))
            yar.append(int(y))
            zar.append(int(z))
            xVelar.append(int(xVel))
            yVelar.append(int(yVel))
            zVelar.append(int(zVel))
    xVelMean = np.mean(xVelar[-29:])
    yVelMean = np.mean(yVelar[-29:])
    zVelMean = np.mean(zVelar[-29:])
##    if ~np.isnan(xVelMean):
##        print "%4d %4d %4d" % (xVelMean,yVelMean,zVelMean)
        
    if xVelMean > 8:
        print "Swipe left"
        ser.write("L")
    elif xVelMean < -8:
        print "Swipe right"
        ser.write("R")
    elif yVelMean > 8:
        print "Swipe down"
        ser.write("S")
    elif yVelMean < -8:
        print "Swipe up"
        ser.write("S")
    elif zVelMean > 8:
        print "Swipe front"
        ser.write("F")
    elif zVelMean < -8:
        print "Swipe back"
        ser.write("B")

try:
    while 1:
        swipeVel()
        time.sleep(.02)
except KeyboardInterrupt:
    print 'Interrupted'
