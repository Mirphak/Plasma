# -*- coding: utf-8 -*-
# == Script pour generer un clone de Yeesha Glow Light ==
# Mirphak 2018-06-17 version 1

from Plasma import *
import math
from . import CloneObject

#
def YeeshaGlowLight(av=None, bLoadShowOn=True, bAttachOn=False, dx=0, dy=0, dz=4, rx=0, ry=0, rz=0, cr=1, cg=1, cb=1, ca=1):
    bOn = bLoadShowOn
    if av is None:
        av = PtGetLocalAvatar()
    pos = av.getLocalToWorld()
    pos1 = pos
    pos1.translate(ptVector3(dx, dy, dz))
    mRot = ptMatrix44()
    mRot.rotate(0, (math.pi * rx) / 180)
    mRot.rotate(1, (math.pi * ry) / 180)
    mRot.rotate(2, (math.pi * rz) / 180)
    pos1 = pos1 * mRot
    CloneObject.Clone2(objName="RTGlowLight", age="CustomAvatars", bShow=bOn, bLoad=bOn, matPos=pos1, bAttach=bAttachOn, soAvatar=av)
    mso = PtFindSceneobject("RTGlowLight", "CustomAvatars")
    cloneKeys = PtFindClones(mso.getKey())
    if len(cloneKeys) > 0:
        ck = cloneKeys[0]
        PtSetLightValue(ck, "RTGlowLight", cr, cg, cb, ca)
