# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 20:05:23 2017

@author: william_r_sommers
"""

__author__ = 'william_r_sommers'

from math import sin, cos, pi
from random import random
import matplotlib.pyplot as mplt

DAY_SEC=1440
WORK_DAY=8*60

def baseline():
    return 10+random()*10
    
phase_shift = pi/WORK_DAY/2

def first_term(x):
    return 50*abs(sin(x*( (2/3)* pi/WORK_DAY)+phase_shift))

def second_term(x,magnitude):
    return magnitude * abs(sin(x*pi/WORK_DAY))

cpu_util = [baseline() + first_term(x) + second_term(x,20) for x in range(DAY_SEC)]
sec_term = [second_term(x,20) for x in range(DAY_SEC)]

print(cpu_util)
mplt.plot(cpu_util)
mplt.axis([0, 1440, 0, 100])
mplt.plot(sec_term)
mplt.show()