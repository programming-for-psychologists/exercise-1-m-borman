# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 23:36:52 2018

@author: mzbor
"""


import time
import sys
from psychopy import visual,event,core

my_num=1
win = visual.Window([400,400],color="black", units="pix")
square = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100])
square2 = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100])

while my_num > 0:
    square.pos = [-100,0]
    square.ori += 9
    square.draw()
    square2.pos = [100,0]
    square2.ori += -9
    square2.draw()
    win.flip()
    core.wait(.025)
win.close()
sys.exit()