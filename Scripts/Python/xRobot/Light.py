# -*- coding: utf-8 -*-
# == Script pour generer un clone de Yeesha Glow Light ==
# Mirphak 2018-06-17 version 1

from Plasma import *
import math
from . import CloneObject

#
def Light0(objectName="RTGlowLight", ageName="CustomAvatars", av=None, bLoadShowOn=True, bAttachOn=False):
    bOn = bLoadShowOn
    if av is None:
        av = PtGetLocalAvatar()
    pos = av.getLocalToWorld()
    CloneObject.Clone2(objName=objectName, age=ageName, bShow=bOn, bLoad=bOn, matPos=pos, bAttach=bAttachOn, soAvatar=av)
    return PtFindSceneobject(objectName, ageName)

#
def Light1(objectName="RTGlowLight", ageName="CustomAvatars", av=None, bLoadShowOn=True, bAttachOn=False, dx=0, dy=0, dz=4, rx=0, ry=0, rz=0):
    bOn = bLoadShowOn
    if av is None:
        av = PtGetLocalAvatar()
    pos = av.getLocalToWorld()
    pos1 = pos
    pos1.translate(ptVector3(dx, dy, dz))
    mRotX = ptMatrix44()
    mRotY = ptMatrix44()
    mRotZ = ptMatrix44()
    mRotX.rotate(0, (math.pi * rx) / 180)
    mRotY.rotate(1, (math.pi * ry) / 180)
    mRotZ.rotate(2, (math.pi * rz) / 180)
    pos1 = pos1 * mRotZ * mRotY * mRotX
    CloneObject.Clone2(objName=objectName, age=ageName, bShow=bOn, bLoad=bOn, matPos=pos1, bAttach=bAttachOn, soAvatar=av)
    return PtFindSceneobject(objectName, ageName)

#
def SetLight(mso, cr=10, cg=10, cb=10, ca=10):
    cloneKeys = PtFindClones(mso.getKey())
    if len(cloneKeys) > 0:
        ck = cloneKeys[0]
        so = ck.getSceneObject()
        soName = so.getName()
        so.netForce(1)
        PtSetLightValue(ck, soName, cr, cg, cb, ca)

#
def SetLight2(objectName, ageName, cr=10, cg=10, cb=10, ca=10):
    try:
        objKey = PtFindSceneobject(objectName, ageName).getKey()
    except:
        print("{} not found in {}".format(objectName, ageName))
        return
    so = objKey.getSceneObject()
    so.netForce(1)
    PtSetLightValue(objKey, objectName, cr, cg, cb, ca)

#
def Light(objectName="RTGlowLight", ageName="CustomAvatars", av=None, bLoadShowOn=True, bAttachOn=False, dx=0, dy=0, dz=4, rx=0, ry=0, rz=0, cr=1, cg=1, cb=1, ca=1):
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
    CloneObject.Clone2(objName=objectName, age=ageName, bShow=bOn, bLoad=bOn, matPos=pos1, bAttach=bAttachOn, soAvatar=av)
    mso = PtFindSceneobject(objectName, ageName)
    cloneKeys = PtFindClones(mso.getKey())
    if len(cloneKeys) > 0:
        ck = cloneKeys[0]
        so = ck.getSceneObject()
        so.netForce(1)
        PtSetLightValue(ck, objectName, cr, cg, cb, ca)

#
def YeeshaGlowLight(av=None, bLoadShowOn=True, bAttachOn=False, dx=0, dy=0, dz=4, rx=0, ry=0, rz=0, cr=1, cg=1, cb=1, ca=1):
    objName="RTGlowLight"
    age="CustomAvatars"
    Light(objName, age, av, bLoadShowOn, bAttachOn, dx, dy, dz, rx, ry, rz, cr, cg, cb, ca)

#
def PelletLight(av=None, bLoadShowOn=True, bAttachOn=False, dx=0, dy=0, dz=4, rx=0, ry=0, rz=0, cr=1, cg=1, cb=1, ca=1):
    objName="RTOmniLight01"
    age="PelletBahroCave"
    Light(objName, age, av, bLoadShowOn, bAttachOn, dx, dy, dz, rx, ry, rz, cr, cg, cb, ca)

#"RTProjDirLight02", "Payiferen"
#"RTProjDirLight03", "Payiferen"

#
def PayLight2(av=None, bLoadShowOn=True, bAttachOn=False, dx=0, dy=0, dz=4, rx=0, ry=0, rz=0, cr=1, cg=1, cb=1, ca=1):
    objName="RTProjDirLight02"
    age="Payiferen"
    Light(objName, age, av, bLoadShowOn, bAttachOn, dx, dy, dz, rx, ry, rz, cr, cg, cb, ca)

#
def PayLight3(av=None, bLoadShowOn=True, bAttachOn=False, dx=0, dy=0, dz=4, rx=0, ry=0, rz=0, cr=1, cg=1, cb=1, ca=1):
    objName="RTProjDirLight03"
    age="Payiferen"
    Light(objName, age, av, bLoadShowOn, bAttachOn, dx, dy, dz, rx, ry, rz, cr, cg, cb, ca)

#
def PayLight3b(av=None, bLoadShowOn=True, bAttachOn=False, dx=0, dy=0, dz=10, rx=0, ry=0, rz=0):
    objName="RTProjDirLight03"
    age="Payiferen"
    return Light1(objName, age, av, bLoadShowOn, bAttachOn, dx, dy, dz, rx, ry, rz)

#
def GlowWhite(av=None, bLoadShowOn=True, bAttachOn=False, dx=0, dy=0, dz=0, rx=0, ry=0, rz=0):
    objName="RT-GlowWhite"
    age="PelletBahroCave"
    return Light1(objName, age, av, bLoadShowOn, bAttachOn, dx, dy, dz, rx, ry, rz)

"""
Ligths

* Tetsonot tetsoPod
= Omni Light Info
- RTBlinkingOmni : A,D,S:(0, 0, 0, 1), kLPMovable   +
- RTSpiralLight01 : A,D,S:(0, 0, 0, 1), kLPMovable
- RTSpiralLight02 : A,D,S:(0, 0, 0, 1), kLPMovable
- RTWindowOmni02 : A,D,S:(0, 0, 0, 1), kDisable kLPMovable  ++
- RTWindowOmni03 : A,D,S:(0, 0, 0, 1), kDisable kLPMovable  ++
= Spot Light Info
- RTSpotLight01 : A,D,S:(0, 0, 0, 1), kDisable kLPMovable

* city KahloPub
= Omni Light Info
- GZRTLight01 : A,S:(0, 0, 0, 1), D:(1, 0.2352941334, 0, 1), kLPMovable kLPHasIncludes kLPIncludesChars
- kpRTOmniLight01 : A,S:(0, 0, 0, 1), D:(0.6941176653, 0.5333333611, 0.250980407, 1), X
- kpRTOmniLight02 : A,S:(0, 0, 0, 1), D:(0.3098039329, 0.5333333611, 0.5960784554, 1), X
- kpRTOmniLight03 : A,S:(0, 0, 0, 1), D:(0.3098039329, 0.5333333611, 0.5960784554, 1), kDisable
- kpRTOmniLight04 : A,S:(0, 0, 0, 1), D:(0.3098039329, 0.5333333611, 0.5960784554, 1), kLPMovable ++

* Personal
- RTBugLight (fixe)

* EderTsogal
= Directional
- RTDirLight01Anim L.Light1("RTDirLight01Anim","EderTsogal",None,1,0,0,0,-10,45,0,0)

* Jalak
= Omni
- RTOmniLightBluAmbient
- RTOmniLightBluAmbient01
- RTOmniLightBluAmbient02
- RTOmniLightBluAmbient03
- RTOmniLightBluAmbient04
- RTOmniLightBluAmbient05

"""