import Leap, sys, thread, time
#import numpy as np

class SampleListener(Leap.Listener):
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']

    xLast = 0
    yLast = 0
    zLast = 0
    
    def on_init(self, controller):
        print ("Initialized")

    def on_connect(self, controller):
        print ("Connected")

        # Enable gestures
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);

    def on_disconnect(self, controller):
        print ("Disconnected")

    def on_exit(self, controller):
        print ("Exited")

    def on_frame(self, controller):
        frame = controller.frame()
        
        open("swipeData.txt", "w")
        # Get hands
        for hand in frame.hands:
            
            x=hand.palm_position[0]
            y=hand.palm_position[1]
            z=hand.palm_position[2]
            
            xVel = (self.xLast - x)
            yVel = (self.yLast - y)
            zVel = (self.zLast - z)

##            print "Velocity:  x: %d z: %d " % (xVel,zVel)
            print (" xLast: %f zLast: %f \t  x: %f z: %f \t Velocity:  x: %f z: %f" % (self.xLast,self.zLast,x,z,xVel,zVel))
            self.xLast=x
            self.yLast=y 
            self.zLast=z            

            outF = open("swipeData.txt", "a")
            outF.write(str(int(x))+','+str(int(y))+','+str(int(z))+','+str(int(xVel))+','+str(int(yVel))+','+str(int(zVel))+'\n')  



def main():
    # Create a sample listener and controller
    listener = SampleListener()
    controller = Leap.Controller()

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)

    # Keep this process running until Enter is pressed
    print ("Press Enter to quit...")
    try:
        sys.stdin.readline()
        
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)


if __name__ == "__main__":
    main()
