# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 13:43:54 2018

@author: mzbor
"""

import time
import sys
from psychopy import visual,event,core
 
win = visual.Window([400,400],color="black", units='pix')
square = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100])
square.draw()
win.flip()
core.wait(1) #pause for 500 ms (half a second)
square = visual.Rect(win,lineColor="black",fillColor="blue",size=[100,100])
square.draw()
win.flip()
core.wait(1) #pause for 500 ms (half a second)
win.close()
sys.exit()