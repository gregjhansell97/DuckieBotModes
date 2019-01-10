#external modules
import random

#local modules
from DuckieBotModes import Driver

class DrunkDriver(Driver):
    '''
    varies the drag of the wheel and distorts the image for each frame to emulate a drunk driver
    '''
    def drag(self, speed, drag):
        '''
        implementation of method in parent (overriding)
        '''
        drag = random.random()
        if speed < -drag:
            speed += drag
        elif speed < 0:
            speed = 0
        if speed > drag:
            speed -= drag
        elif speed > 0:
            speed = 0
        #puts a cap limit on max speed
        if abs(speed) < 0.0001:
            speed = 0
        if speed < 0:
            return max(speed, -1)
        else:
            return min(speed, 1)

    def frame(self, frame):
        '''
        implementation of method in parent (overriding)
        '''
        #TODO distort frame
        return frame
