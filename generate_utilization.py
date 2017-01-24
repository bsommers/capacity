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
WORK_DAY=9*60
PRE_WORK = 8*60
POST_WORK = 7*60

def baseline():
    return 10+random()*10
    
phase_shift = pi/WORK_DAY/2

def first_term(x, magnitude):
    return magnitude*abs(sin(x*(2* pi/WORK_DAY)+phase_shift))

def second_term(x,magnitude):
    return magnitude * abs(cos(x*2*pi/WORK_DAY))

def backup(i):
    if i < POST_WORK*.30 or i > POST_WORK*0.6:
        return 5+random()*10
    else:
        return 30+random()*60

a_cpu_util = [baseline() + backup(_) for _ in range(PRE_WORK)]
prime_cpu_util = [baseline() + first_term(x,50) + second_term(x,20) 
                    for x in range(WORK_DAY)]
sec_term = [second_term(x,20) for x in range(DAY_SEC)]
b_cpu_util = [baseline() for _ in range(POST_WORK)]

day_workload= a_cpu_util + prime_cpu_util + b_cpu_util

print(day_workload)
#mplt.plot(cpu_util)
mplt.axis([0, 1440, 0, 100])
#mplt.plot(sec_term)
#mplt.plot(a_cpu_util)
#mplt.plot(b_cpu_util)
mplt.plot(day_workload)
mplt.show()