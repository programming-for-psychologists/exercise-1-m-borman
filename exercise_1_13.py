# -*- coding: utf-8 -*-
"""
Created on Thu Feb 01 00:14:30 2018

@author: mzbor
"""


import time
import sys
from psychopy import visual,event,core

my_num=1
win = visual.Window([400,400],colorSpace='rgb',color=[0,0,1],units="pix") #trying to set rgb colorspace and assign color to window.  Appears to work.
square = visual.Rect(win,color=[1,0,1],size=[100,100]) #trying to set starting color of square.  Doesn't seem to work.
while my_num > 0:
    square.ori += 9
    square.color += [.1,.1,.1] #trying to change color each time through loop
    square.draw()
    win.flip()
    core.wait(.025)
win.close()
sys.exit()