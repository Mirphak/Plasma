# -*- coding: utf-8 -*-

# == Script pour Ahnonay ==

from Plasma import *
import math
import CloneObject

"""
* Objets du ciel a retourner:
    SkyDome
    SkyDomeBeneath
"""

"""
                soTop = dicClones["FissureStarField"][nbClonesFound - 2].getSceneObject()
                soBottom = dicClones["FissureStarField"][nbClonesFound - 1].getSceneObject()
                pos = soMaster.getLocalToWorld()
                mrot = ptMatrix44()
                mrot.rotate(0, math.pi)
                mscale = ptMatrix44()
                mscale.makeScaleMat(ptVector3(self._scale, self._scale, self._scale))
                mtransUp = ptMatrix44()
                mtransUp.translate(ptVector3(.0, .0, 30))
                mtransDown = ptMatrix44()
                mtransDown.translate(ptVector3(.0, .0, -30))
                soTop.draw.netForce(1)
                soTop.physics.netForce(1)
                soBottom.draw.netForce(1)
                soBottom.physics.netForce(1)
                soTop.physics.warp(pos * mtransUp * mscale * mrot)
                soBottom.physics.warp(pos * mtransDown * mscale)
                soTop.draw.enable(1)
                soBottom.draw.enable(1)
"""


bAlreadyScaled = False
#
def RotateSceneObjects(name = "SkyDome", strAxis = "x", angle = 0, scale = 1):
    global bAlreadyScaled
    pf = PtFindSceneobjects(name)
    mrot = ptMatrix44()
    axis = 0
    if strAxis == 'x':
        axis = 0
    elif strAxis == 'y':
        axis = 1
    elif strAxis == 'z':
        axis = 2
    else:
        return 0
    try:
        mrot.rotate(axis, (math.pi * float(angle)) / 180)
    except ValueError:
        return 0
    mscale = ptMatrix44()
    if bAlreadyScaled:
        mscale.makeScaleMat(ptVector3(1./scale, 1./scale, 1./scale))
        bAlreadyScaled = False
    else:
        mscale.makeScaleMat(ptVector3(scale, scale, scale))
        bAlreadyScaled = True
    for so in pf:
        try:
            pos = so.getLocalToWorld()
            so.netForce(1)
            so.physics.warp(pos * mscale * mrot)
        except RuntimeError:
            pass
    return 1

#
def CleftSky(bOn=True):
    CloneObject.co3("skyDome", "Cleft", bShow=bOn, bLoad=bOn)

#
def Desert(bOn=True):
    CloneObject.co3("DesertPlane", "Cleft", bShow=bOn, bLoad=bOn)

#
def Clone(objName="SkyDome", bLoadOn=True, bShowOn=True):
    CloneObject.co3(objName, "Minkata", bShow=bShowOn, bLoad=bLoadOn)

#
def Cloud(bLoadOn=True, bShowOn=True, fscale=1):
    CloneObject.co3("SkyHighStormy", "Personal", bShow=bShowOn, bLoad=bLoadOn, scale=fscale, matPos=None)

#

"""
!toggle Wheel  0 0
!toggle Horizon  0 0

//nosky
//skycolor 10 75 85
//fogshape 400 1000 10
//fogcolor 10 75 85

A tester, objets de Personal avec coordonnees:
SkyHighStormy
SkyLow
"""