#external modules
import random

#local modules
from DuckieBotModes import Driver

class DrunkDriver(Driver):
    '''
    '''
    def drag(self, speed, drag):
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
        #TODO distort frame
        return frame
