#external modules
from collections import namedtuple
import cv2
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

    def frame(self, frame):
        '''
        '''
        # background = frame
        # self.imgpath='ink9.png'
        # print(self.imgpath)
        # overlay = cv2.imread('gui/static/ink_img/'+self.imgpath)
        # overlay = cv2.resize(overlay, (background.shape[1], background.shape[0]))
        # background = cv2.imread('gui/static/ink_img/ink8.png')
        # background = cv2.flip( background, 1 )
        # cv2.imshow('image',background)

        # print(os.getcwd())
        # print (Path('.'))
        # added_image = cv2.addWeighted(background,0.7,overlay,0.3,0)

        return frame
