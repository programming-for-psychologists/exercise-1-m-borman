# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 14:03:13 2018

@author: mzbor
"""

import time
import sys
from psychopy import visual,event,core

my_num=1
win = visual.Window([400,400],color="black", units="pix")
square = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100])
while my_num > 0:
    square.ori += 9
    square.draw()
    win.flip()
    core.wait(.025)
win.close()
sys.exit()