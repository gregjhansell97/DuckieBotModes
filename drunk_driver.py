#external modules
from collections import namedtuple
import cv2

#local modules
from DuckieBotModes import Driver

class DrunkDriver(Driver):
    '''
    '''
    def __init__(self, camera=None, car=None):
        '''
        '''
        Driver.__init__(self, camera=camera, car=car)

    def drag(self, speed, drag):
        if speed < -drag:
            speed += drag
        elif speed < 0:
            speed = 0
        if speed > drag:
            speed -= drag
        elif speed > 0:
            speed = 0
        #puts a cap limit on max speed
        if abs(speed - 0) < 0.0001:
            speed = 0
        if speed < 0:
            return max(speed, -1)
        else:
            return min(speed, 1)
