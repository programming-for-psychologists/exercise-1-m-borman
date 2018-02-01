# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 12:19:55 2018

@author: mzbor
"""

import time
import sys
from psychopy import visual,event,core
 
win = visual.Window([400,400],color="black", units='pix')
square = visual.Rect(win,lineColor="black",fillColor="blue",size=[100,100])
square_one = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100])
for x in range(0,3):
    square.draw()
    win.flip()
    core.wait(1) #pause for 500 ms (half a second)
    win.flip()
    core.wait(.05)
    square_one.draw()
    win.flip()
    core.wait(1)
    win.flip()
    if x !=2:
        core.wait(.05)
win.close()
sys.exit()