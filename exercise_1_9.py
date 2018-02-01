# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 21:51:38 2018

@author: mzbor
"""

import time
import sys
from psychopy import visual,event,core

my_num=1
win = visual.Window([400,400],color="black", units="pix")
square = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100])
while my_num > 0:
    keys = event.getKeys(['s'])
    if 's' in keys:
        square.ori
        square.draw()
        win.flip()
        core.wait(2)
        my_num2=1
        while my_num2 > 0:
            keys = event.getKeys(['i'])
            if 'i' in keys:
                my_num2=0
                core.wait(.01)
    else:
        square.ori += 9
        square.draw()
        win.flip()
        core.wait(.025)          
win.close()
sys.exit()