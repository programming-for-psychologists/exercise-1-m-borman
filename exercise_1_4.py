# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 11:05:44 2018

@author: mzbor
"""

import time
import sys
from psychopy import visual,event,core
 
win = visual.Window([400,400],color="black", units='pix')
square_red = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100])
square_red.draw()
win.flip()
core.wait(1.5) #pause for 500 ms (half a second)
win.flip()
core.wait(1)
win.flip()
for x in range(0,3):
    square_red.draw()
    win.flip()
    core.wait(.03)
    win.flip() #pause for 500 ms (half a second)
win.close()
sys.exit()