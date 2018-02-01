# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 22:43:24 2018

@author: mzbor
"""

import time
import sys
from psychopy import visual,event,core

my_num=1
win = visual.Window([400,400],color="black", units="pix")
square = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100])

square.draw()
win.flip()
core.wait(.05)
while my_num>0:
    keys = event.getKeys(['left', 'right'])
    if 'right' in keys:
        square.size *= [.9,1]
        square.draw()
        win.flip()
        core.wait(.05)
    if 'left' in keys:
        square.size *= [1.1,1]
        square.draw()
        win.flip()
        core.wait(.05)
win.close()
sys.exit()