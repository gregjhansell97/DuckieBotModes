#external modules
from collections import namedtuple
import cv2
import numpy as np
import os
from pathlib import Path
import random


#local modules
from DuckieBotModes.driver import Driver

class Squid(Driver):
    '''
    '''
    def __init__(self, camera=None, car=None):
        '''
        '''
        Driver.__init__(self, camera=camera, car=car)
        image_path = Path(os.path.realpath(__file__))/".."/"ink.png"
        self.ink = cv2.imread(str(image_path.resolve()), cv2.IMREAD_UNCHANGED)
        self.ink.reshape(self.ink.shape[0]*self.ink.shape[1], 4)

    def frame(self, frame):
        '''
        '''
        ink_pixels = cv2.resize(self.ink, (frame.shape[1], frame.shape[0]))
        ink_pixels = ink_pixels.reshape(frame.shape[0]*frame.shape[1], 4)
        frame_pixels = frame.reshape(frame.shape[0]*frame.shape[1], 3)

        # handles the blending of the two images
        is_zero = (ink_pixels[:,3] == 0)
        is_zero = np.array([is_zero, is_zero, is_zero]).transpose()
        frame_pixels = frame_pixels*(is_zero) + ink_pixels[:, 0:3]*(is_zero != True)

        frame = frame_pixels.reshape(frame.shape[0], frame.shape[1], 3)

        return frame
