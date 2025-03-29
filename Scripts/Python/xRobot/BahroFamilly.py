# -*- coding: utf-8 -*-

from Plasma import *

import math
#import datetime
import random

from . import CloneObjects

"""
In Kadish Vista
z= -63.84
x   y
551 -212 
545 -237
519 -230
518 -204
"""

def Load():
    bahroShow = True
    z = -63.84
    for bahroNumber in range(1, 10):
        bahroScale = random.uniform(0.3, 1.3)
        x = random.uniform(519.0, 545.0)
        y = random.uniform(-230.0, -212.0)
        bahroPos = ptMatrix44()
        bahroPos.translate(ptVector3(x, y, z))
        mrot = ptMatrix44()
        mrot.rotate(2, (math.pi * random.uniform(0.0, 90.0)) / 180)
        bahroPos = bahroPos * mrot
        CloneObjects.PutBahroHere(show=bahroShow, load=True, nb=9, num=bahroNumber, scale=bahroScale, pos=bahroPos, attach=False)
