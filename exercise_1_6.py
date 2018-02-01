# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 12:52:19 2018

@author: mzbor
"""

import time
import sys
from psychopy import visual,event,core

win = visual.Window([400,400],color="black", units="pix")
square = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100])
square.draw()
win.flip()
core.wait(1)
square.setOri(45)
square.draw()
win.flip()
core.wait(1)
win.close()
sys.exit()