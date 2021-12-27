# -*- coding: utf-8 -*-

from Plasma import *
from . import CloneObject
import math


#attacher so1 a so2 : attacher(obj, av) ou l'inverse    
def Attacher(so1, so2):
    """attacher so1 à so2 : attacher(obj, av) ou l'inverse"""
    so1.physics.netForce(1)
    so1.draw.netForce(1)
    PtAttachObject(so1, so2, 1)

# detacher so1 de so2 : detach(obj, av) ou l'inverse    
def Detacher(so1, so2):
    so1.physics.netForce(1)
    so1.draw.netForce(1)
    PtDetachObject(so1, so2, 1)

# Il doit falloir attacher un objet qui ne bouge pas a un objet qui peut bouger

# attache ou detache le sol a/de moi
def groundtome(bAttachOn=True):
    av = PtGetLocalAvatar()
    #avpos = PtGetLocalAvatar().getLocalToWorld()
    so = PtFindSceneobject("GroundPlaneVis", "Minkata")
    #sopos = so.getLocalToWorld()

    if bAttachOn:
        Attacher(so1=so, so2=av)
    else:
        Detacher(so1=so, so2=av)

# attache ou detache le ballon a/de moi
def soccertome(bAttachOn=True):
    av = PtGetLocalAvatar()
    #avpos = PtGetLocalAvatar().getLocalToWorld()
    so = PtFindSceneobject("SoccerBall", "Minkata")
    #sopos = so.getLocalToWorld()

    if bAttachOn:
        Attacher(so1=so, so2=av)
    else:
        Detacher(so1=so, so2=av)

# attache ou detache le sol a/de moi
def groundtosoccer(bAttachOn=True):
    av = PtGetLocalAvatar()
    #avpos = PtGetLocalAvatar().getLocalToWorld()
    soGround = PtFindSceneobject("GroundPlaneVis", "Minkata")
    #sopos = so.getLocalToWorld()
    soSoccer = PtFindSceneobject("SoccerBall", "Minkata")

    if bAttachOn:
        Attacher(so1=soGround, so2=soSoccer)
    else:
        Detacher(so1=soGround, so2=soSoccer)

#-----------------------------------------------------------------------

def PrepareClones(bOn=True):
    #soAvatar = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
    soAvatar = PtGetLocalAvatar()
    mPos = soAvatar.getLocalToWorld()
    #
    CloneObject.co3("LinkOutPOS", "spyroom", bShow=bOn, bLoad=bOn, scale=1, matPos=mPos)
    CloneObject.co3("GroundFloorProxy", "Minkata", bShow=bOn, bLoad=bOn, scale=1, matPos=mPos)

def GetClonesPos():
    soGround = PtFindSceneobject("GroundFloorProxy", "Minkata")
    soMovable = PtFindSceneobject("LinkOutPOS", "spyroom")
    ckGround = PtFindClones(soGround.getKey())
    ckMovable = PtFindClones(soMovable.getKey())
    print("nb ckGround: {}".format(len(ckGround)))
    print("nb ckMovable: {}".format(len(ckMovable)))
    i = 0
    for k in ckGround:
        so = k.getSceneObject()
        try:
            pos = so.position()
            print("Clone #{} of {} is at {}, {}, {}".format(i, so.getName(), pos.getX(), pos.getY(), pos.getZ()))
        except RuntimeError:
            print("Clone #{} of {} has no position".format(i, so.getName()))
        i += 1
    i = 0
    for k in ckMovable:
        so = k.getSceneObject()
        pos = so.position()
        print("Clone #{} of {} is at {}, {}, {}".format(i, so.getName(), pos.getX(), pos.getY(), pos.getZ()))
        i += 1

def Move000():
    soMovable = PtFindSceneobject("LinkOutPOS", "spyroom")
    ckMovable = PtFindClones(soMovable.getKey())
    if len(ckMovable) < 1:
        return 0
    so = ckMovable[0].getSceneObject()
    # = ptMatrix44()
    so.netForce(1)
    so.physics.warp(ptMatrix44())

def AttachGroundToMovable(bAttachOn=True):
    soGround = PtFindSceneobject("GroundFloorProxy", "Minkata")
    soMovable = PtFindSceneobject("LinkOutPOS", "spyroom")
    ckGround = PtFindClones(soGround.getKey())
    ckMovable = PtFindClones(soMovable.getKey())
    if len(ckGround) < 1:
        return 0
    if len(ckMovable) < 1:
        return 0
    sog = ckGround[0].getSceneObject()
    som = ckMovable[0].getSceneObject()
    if bAttachOn:
        Attacher(so1=sog, so2=som)
    else:
        Detacher(so1=sog, so2=som)

def AttachMovableToGround(bAttachOn=True):
    soGround = PtFindSceneobject("GroundFloorProxy", "Minkata")
    soMovable = PtFindSceneobject("LinkOutPOS", "spyroom")
    ckGround = PtFindClones(soGround.getKey())
    ckMovable = PtFindClones(soMovable.getKey())
    if len(ckGround) < 1:
        return 0
    if len(ckMovable) < 1:
        return 0
    sog = ckGround[0].getSceneObject()
    som = ckMovable[0].getSceneObject()
    if bAttachOn:
        Attacher(so1=som, so2=sog)
    else:
        Detacher(so1=som, so2=sog)

def MoveToMe():
    soMovable = PtFindSceneobject("LinkOutPOS", "spyroom")
    ckMovable = PtFindClones(soMovable.getKey())
    if len(ckMovable) < 1:
        return 0
    so = ckMovable[0].getSceneObject()
    soAvatar = PtGetLocalAvatar()
    mPosAvatar = soAvatar.getLocalToWorld()
    so.netForce(1)
    so.physics.warp(mPosAvatar)

#