# -*- coding: utf-8 -*-

from Plasma import *
import CloneObject
import math

#
def TreeSphere(en=True, clouds=True):
    for item in ('SphereEnviron', 'SphereEnvironDARK', 'SphereClouds')[:2+clouds]:
        d = PtFindSceneobject(item, 'GreatTreePub').draw
        d.netForce(1)
        d.enable(en)
        en = not en;

#
def Add(item=1, bOn=True):
    #CloneObject.co3("ConstellationDummyCave01", "Minkata", bShow=bOn, bLoad=bOn, scale=1, matPos=None)
    #CloneObject.co3("ConstellationDummyCave02", "Minkata", bShow=bOn, bLoad=bOn, scale=1, matPos=None)
    #CloneObject.co3("ConstellationDummyCave03", "Minkata", bShow=bOn, bLoad=bOn, scale=1, matPos=None)
    #CloneObject.co3("ConstellationDummyCave04", "Minkata", bShow=bOn, bLoad=bOn, scale=1, matPos=None)
    #CloneObject.co3("ConstellationDummyCave05", "Minkata", bShow=bOn, bLoad=bOn, scale=1, matPos=None)
    """
    if item == 1 :
        CloneObject.co3("StarGlobe", "Minkata", bShow=bOn, bLoad=bOn, scale=1, matPos=None)
    elif item == 2 :
        CloneObject.co3("GalaxyDecal", "Minkata", bShow=bOn, bLoad=bOn, scale=1, matPos=None)
    elif item == 3 :
        CloneObject.co3("GalaxyDecalSmall", "Minkata", bShow=bOn, bLoad=bOn, scale=1, matPos=None)
    elif item == 4 :
        CloneObject.co3("RTDirLightSunshine", "Minkata", bShow=bOn, bLoad=bOn, scale=1, matPos=None)
    elif item == 5 :
        CloneObject.co3("RTDirLightCoolDesertFill", "Minkata", bShow=bOn, bLoad=bOn, scale=1, matPos=None)
    elif item == 6 :
        CloneObject.co3("RTDirLightWarmDesertFill", "Minkata", bShow=bOn, bLoad=bOn, scale=1, matPos=None)
    elif item == 7 :
        CloneObject.co3("RTDirLightWarmDesertFill01", "Minkata", bShow=bOn, bLoad=bOn, scale=1, matPos=None)
    else :
        pass
    """
    if item == 1 :
        CloneObject.co3("RTDirLightSunshine", "Minkata", bShow=bOn, bLoad=bOn, scale=1, matPos=None)
        CloneObject.co3("RTDirLightCoolDesertFill", "Minkata", bShow=bOn, bLoad=bOn, scale=1, matPos=None)
        CloneObject.co3("RTDirLightWarmDesertFill", "Minkata", bShow=bOn, bLoad=bOn, scale=1, matPos=None)
        CloneObject.co3("RTDirLightWarmDesertFill01", "Minkata", bShow=bOn, bLoad=bOn, scale=1, matPos=None)
    elif item == 2 :
        #Directional
        CloneObject.co3("RTDirLight01Anim", "EderTsogal", bShow=bOn, bLoad=bOn, scale=1, matPos=None)
        #Omni
        CloneObject.co3("RTOmniLight03", "EderTsogal", bShow=bOn, bLoad=bOn, scale=1, matPos=None)
        CloneObject.co3("RTOmniLight04", "EderTsogal", bShow=bOn, bLoad=bOn, scale=1, matPos=None)
        CloneObject.co3("RTOmniLight05", "EderTsogal", bShow=bOn, bLoad=bOn, scale=1, matPos=None)
        CloneObject.co3("RTOmniLight06", "EderTsogal", bShow=bOn, bLoad=bOn, scale=1, matPos=None)
        CloneObject.co3("RTOmniLight07", "EderTsogal", bShow=bOn, bLoad=bOn, scale=1, matPos=None)
        CloneObject.co3("RTOmniLight09", "EderTsogal", bShow=bOn, bLoad=bOn, scale=1, matPos=None)
        CloneObject.co3("RTOmniLightFountain", "EderTsogal", bShow=bOn, bLoad=bOn, scale=1, matPos=None)
    elif item == 3 :
        CloneObject.co3("RTOmniLightFliker", "Ahnonay", bShow=bOn, bLoad=bOn, scale=1, matPos=None)
    elif item == 4 :
        CloneObject.co3("RTProjDirLight03", "Payiferen", bShow=bOn, bLoad=bOn, scale=1, matPos=None)
    else :
        pass

#
def LightForTiwah(bOn=True):
    pos1 = ptMatrix44()
    pos2 = ptMatrix44()
    pos3 = ptMatrix44()
    pos4 = ptMatrix44()

    tuplePos1 = ((-0.0914004445076, -0.704146981239, -0.704146981239, 783.95513916), (0.995814204216, -0.0646298527718, -0.0646299123764, -578.580627441), (0.0, -0.707106769085, 0.70710682869, 1151.59057617), (0.0, 0.0, 0.0, 1.0))
    tuplePos2 = ((0.626261711121, 0.551269590855, -0.55126953125, 782.68145752), (0.779612958431, -0.442833811045, 0.442833840847, -567.865478516), (-2.98023223877e-08, -0.707106769085, -0.70710670948, 1151.59057617), (0.0, 0.0, 0.0, 1.0))
    tuplePos3 = ((-0.762868046761, 0.4571826756, -0.457182705402, 785.506896973), (0.64655393362, 0.539429306984, -0.539429247379, -593.303527832), (0.0, -0.707106769085, -0.707106590271, 1151.85327148), (0.0, 0.0, 0.0, 1.0))
    tuplePos4 = ((0.131729483604, -0.858478546143, -0.495642840862, 766.657470703), (0.991285681725, 0.114081077278, 0.0658647418022, -578.623840332), (0.0, -0.5, 0.866025388241, 1167.91870117), (0.0, 0.0, 0.0, 1.0))

    pos1.setData(tuplePos1)
    pos2.setData(tuplePos2)
    pos3.setData(tuplePos3)
    pos4.setData(tuplePos4)

    CloneObject.co3("RTOmniLight03", "EderTsogal", bShow=bOn, bLoad=bOn, scale=1, matPos=pos1)
    CloneObject.co3("RTOmniLight04", "EderTsogal", bShow=bOn, bLoad=bOn, scale=1, matPos=pos1)
    CloneObject.co3("RTOmniLight05", "EderTsogal", bShow=bOn, bLoad=bOn, scale=1, matPos=pos1)
    CloneObject.co3("RTOmniLight06", "EderTsogal", bShow=bOn, bLoad=bOn, scale=1, matPos=pos2)
    CloneObject.co3("RTOmniLight07", "EderTsogal", bShow=bOn, bLoad=bOn, scale=1, matPos=pos2)
    CloneObject.co3("RTOmniLight09", "EderTsogal", bShow=bOn, bLoad=bOn, scale=1, matPos=pos3)
    #CloneObject.co3("RTDirLightCoolDesertFill", "Minkata", bShow=bOn, bLoad=bOn, scale=1, matPos=pos2)
    #CloneObject.co3("RTDirLightWarmDesertFill", "Minkata", bShow=bOn, bLoad=bOn, scale=1, matPos=pos3)
    #CloneObject.co3("RTDirLightWarmDesertFill01", "Minkata", bShow=bOn, bLoad=bOn, scale=1, matPos=pos3)
    #CloneObject.co3("RTDirLightSunshine", "Minkata", bShow=bOn, bLoad=bOn, scale=1, matPos=None)
    CloneObject.co3("RTDirLight01Anim", "EderTsogal", bShow=bOn, bLoad=bOn, scale=1, matPos=pos1)
    CloneObject.co3("RTOmniLightFountain", "EderTsogal", bShow=bOn, bLoad=bOn, scale=1, matPos=pos1)
    CloneObject.co3("RTProjDirLight03", "Payiferen", bShow=bOn, bLoad=bOn, scale=1, matPos=pos4)

# COOL :
# Pour Tiwah
# Pour MobKveer : ws 8, (1, 90.0); ws 7, (2, 45.0) 
def test1(nObj=1, bOn=True, bAttachOn=True, fAngleX=90.0, fAngleY=0.0, fAngleZ=0.0):
    av = PtGetLocalAvatar()
    pos = PtGetLocalAvatar().getLocalToWorld()
    mRot = ptMatrix44()
    # rotation selon X : axis = 0
    mRot.rotate(0, (math.pi * float(fAngleX)) / 180)
    mRot.rotate(1, (math.pi * float(fAngleY)) / 180)
    mRot.rotate(2, (math.pi * float(fAngleZ)) / 180)
    mPos = pos * mRot
    if nObj == 1 :
        CloneObject.Clone2("RTProjDirLight03", "Payiferen", bShow=bOn, bLoad=bOn, matPos=mPos, bAttach=bAttachOn, soAvatar=av)
    elif nObj == 2 :
        CloneObject.Clone2("RTProjDirLight02", "Payiferen", bShow=bOn, bLoad=bOn, matPos=mPos, bAttach=bAttachOn, soAvatar=av)
    else :
        pass

# Pour MobKveer : ws 8, (1, 90.0); ws 7, (2, 45.0) 
def jalak(nObj=1, bOn=True, bAttachOn=True, fAngleX=0.0, fAngleY=0.0, fAngleZ=0.0):
    av = PtGetLocalAvatar()
    pos = PtGetLocalAvatar().getLocalToWorld()
    mRot = ptMatrix44()
    # rotation selon X : axis = 0
    mRot.rotate(0, (math.pi * float(fAngleX)) / 180)
    mRot.rotate(1, (math.pi * float(fAngleY)) / 180)
    mRot.rotate(2, (math.pi * float(fAngleZ)) / 180)
    mPos = pos * mRot
    if nObj == 1 :
        CloneObject.Clone2("RTOmniLight02", "Jalak", bShow=bOn, bLoad=bOn, matPos=mPos, bAttach=bAttachOn, soAvatar=av)
    elif nObj == 2 :
        CloneObject.Clone2("RTOmniLight04", "Jalak", bShow=bOn, bLoad=bOn, matPos=mPos, bAttach=bAttachOn, soAvatar=av)
    elif nObj == 3 :
        CloneObject.Clone2("RTOmniLight06NEW", "Jalak", bShow=bOn, bLoad=bOn, matPos=mPos, bAttach=bAttachOn, soAvatar=av)
    elif nObj == 4 :
        CloneObject.Clone2("RTOmniLight07", "Jalak", bShow=bOn, bLoad=bOn, matPos=mPos, bAttach=bAttachOn, soAvatar=av)
    elif nObj == 5 :
        CloneObject.Clone2("RTOmniLight08", "Jalak", bShow=bOn, bLoad=bOn, matPos=mPos, bAttach=bAttachOn, soAvatar=av)
    elif nObj == 6 :
        CloneObject.Clone2("RTOmniLightBluAmbient", "Jalak", bShow=bOn, bLoad=bOn, matPos=mPos, bAttach=bAttachOn, soAvatar=av)
    elif nObj == 7 :
        CloneObject.Clone2("RTOmniLightBluAmbient01", "Jalak", bShow=bOn, bLoad=bOn, matPos=mPos, bAttach=bAttachOn, soAvatar=av)
    elif nObj == 8 :
        CloneObject.Clone2("RTOmniLightBluAmbient02", "Jalak", bShow=bOn, bLoad=bOn, matPos=mPos, bAttach=bAttachOn, soAvatar=av)
    elif nObj == 9 :
        CloneObject.Clone2("RTOmniLightBluAmbient03", "Jalak", bShow=bOn, bLoad=bOn, matPos=mPos, bAttach=bAttachOn, soAvatar=av)
    elif nObj == 10 :
        CloneObject.Clone2("RTOmniLightBluAmbient04", "Jalak", bShow=bOn, bLoad=bOn, matPos=mPos, bAttach=bAttachOn, soAvatar=av)
    elif nObj == 11 :
        CloneObject.Clone2("RTOmniLightBluAmbient05", "Jalak", bShow=bOn, bLoad=bOn, matPos=mPos, bAttach=bAttachOn, soAvatar=av)
    elif nObj == 12 :
        CloneObject.Clone2("RTProjDirLight01", "Jalak", bShow=bOn, bLoad=bOn, matPos=mPos, bAttach=bAttachOn, soAvatar=av)
    elif nObj == 13 :
        CloneObject.Clone2("SunShadowtRTDirLight04", "Jalak", bShow=bOn, bLoad=bOn, matPos=mPos, bAttach=bAttachOn, soAvatar=av)
    else :
        pass

#
def LightForKveer(bOn=True, bAttachOn=False):
    pos1 = ptMatrix44()
    pos2 = ptMatrix44()
    pos3 = ptMatrix44()
    pos4 = ptMatrix44()
    
    tuplePos1 = ((-0.999985933304, -0.00528157455847, 0.0, -0.273455888033), (0.00528157455847, -0.999985933304, 0.0, -47.5185241699), (0.0, 0.0, 1.0, 9.40436553955), (0.0, 0.0, 0.0, 1.0))
    tuplePos2 = ((-0.999986410141, -0.00528157642111, 0.0, -0.273455888033), (0.00528157642111, -0.999986410141, 0.0, -47.5185241699), (0.0, 0.0, 1.0, 48.0664749146), (0.0, 0.0, 0.0, 1.0))
    tuplePos3 = ((0.999998033047, 0.00198203604668, 0.0, 0.119770005345), (-0.00198203604668, 0.999998033047, 0.0, 3.88968443871), (0.0, 0.0, 1.0, 49.4459877014), (0.0, 0.0, 0.0, 1.0))
    tuplePos4 = ((-0.999917268753, -0.0128562794998, 0.0, -0.539468109608), (0.0128562794998, -0.999917268753, 0.0, -71.0015563965), (0.0, 0.0, 1.0, 9.40436553955), (0.0, 0.0, 0.0, 1.0))
    
    pos1.setData(tuplePos1)
    pos2.setData(tuplePos2)
    pos3.setData(tuplePos3)
    pos4.setData(tuplePos4)
    
    av = PtGetLocalAvatar()
    #pos = PtGetLocalAvatar().getLocalToWorld()
    mRot = ptMatrix44()
    mRot.rotate(0, (math.pi * float(90.0)) / 180)
    pos6 = pos4 * mRot
    
    mRot = ptMatrix44()
    mRot.rotate(0, (math.pi * float(45.0)) / 180)
    pos5 = pos3 * mRot
    
    #CloneObject.co3("RTOmniLight03", "EderTsogal", bShow=bOn, bLoad=bOn, scale=1, matPos=pos1)
    #CloneObject.co3("RTOmniLight04", "EderTsogal", bShow=bOn, bLoad=bOn, scale=1, matPos=pos1)
    #CloneObject.co3("RTOmniLight05", "EderTsogal", bShow=bOn, bLoad=bOn, scale=1, matPos=pos1)
    #CloneObject.co3("RTOmniLight06", "EderTsogal", bShow=bOn, bLoad=bOn, scale=1, matPos=pos2)
    #CloneObject.co3("RTOmniLight07", "EderTsogal", bShow=bOn, bLoad=bOn, scale=1, matPos=pos2)
    #CloneObject.co3("RTOmniLight09", "EderTsogal", bShow=bOn, bLoad=bOn, scale=1, matPos=pos3)
    #CloneObject.co3("RTDirLight01Anim", "EderTsogal", bShow=bOn, bLoad=bOn, scale=1, matPos=pos3)
    #CloneObject.co3("RTOmniLightFountain", "EderTsogal", bShow=bOn, bLoad=bOn, scale=1, matPos=pos4)
    #CloneObject.co3("RTProjDirLight03", "Payiferen", bShow=bOn, bLoad=bOn, scale=1, matPos=pos4)
    """
    CloneObject.Clone2("RTOmniLight03", "EderTsogal", bShow=bOn, bLoad=bOn, matPos=pos1, bAttach=bAttachOn, soAvatar=av)
    #CloneObject.Clone2("RTOmniLight04", "EderTsogal", bShow=bOn, bLoad=bOn, matPos=pos1, bAttach=bAttachOn, soAvatar=av)
    #CloneObject.Clone2("RTOmniLight05", "EderTsogal", bShow=bOn, bLoad=bOn, matPos=pos1, bAttach=bAttachOn, soAvatar=av)
    CloneObject.Clone2("RTOmniLight06", "EderTsogal", bShow=bOn, bLoad=bOn, matPos=pos2, bAttach=bAttachOn, soAvatar=av)
    #CloneObject.Clone2("RTOmniLight07", "EderTsogal", bShow=bOn, bLoad=bOn, matPos=pos2, bAttach=bAttachOn, soAvatar=av)
    CloneObject.Clone2("RTOmniLight09", "EderTsogal", bShow=bOn, bLoad=bOn, matPos=pos3, bAttach=bAttachOn, soAvatar=av)
    #CloneObject.Clone2("RTDirLight01Anim", "EderTsogal", bShow=bOn, bLoad=bOn, matPos=pos3, bAttach=bAttachOn, soAvatar=av)
    CloneObject.Clone2("RTOmniLightFountain", "EderTsogal", bShow=bOn, bLoad=bOn, matPos=pos4, bAttach=bAttachOn, soAvatar=av)
    CloneObject.Clone2("RTProjDirLight03", "Payiferen", bShow=bOn, bLoad=bOn, matPos=pos5, bAttach=bAttachOn, soAvatar=av)
    #CloneObject.Clone2("RTDirLight01Anim", "EderTsogal", bShow=bOn, bLoad=bOn, matPos=pos6, bAttach=bAttachOn, soAvatar=av)
    #CloneObject.Clone2("RTProjDirLight02", "Payiferen", bShow=bOn, bLoad=bOn, matPos=pos6, bAttach=bAttachOn, soAvatar=av)
    """
    CloneObject.Clone2("RTOmniLight03", "EderTsogal", bShow=bOn, bLoad=bOn, matPos=pos1, bAttach=bAttachOn, soAvatar=av)
    CloneObject.Clone2("RTOmniLight04", "EderTsogal", bShow=bOn, bLoad=bOn, matPos=pos5, bAttach=bAttachOn, soAvatar=av)
    CloneObject.Clone2("RTOmniLight05", "EderTsogal", bShow=bOn, bLoad=bOn, matPos=pos6, bAttach=bAttachOn, soAvatar=av)
    CloneObject.Clone2("RTOmniLight06", "EderTsogal", bShow=bOn, bLoad=bOn, matPos=pos2, bAttach=bAttachOn, soAvatar=av)
    CloneObject.Clone2("RTOmniLight07", "EderTsogal", bShow=bOn, bLoad=bOn, matPos=pos6, bAttach=bAttachOn, soAvatar=av)
    CloneObject.Clone2("RTOmniLight09", "EderTsogal", bShow=bOn, bLoad=bOn, matPos=pos3, bAttach=bAttachOn, soAvatar=av)
    #CloneObject.Clone2("RTDirLight01Anim", "EderTsogal", bShow=bOn, bLoad=bOn, matPos=pos3, bAttach=bAttachOn, soAvatar=av)
    CloneObject.Clone2("RTOmniLightFountain", "EderTsogal", bShow=bOn, bLoad=bOn, matPos=pos4, bAttach=bAttachOn, soAvatar=av)
    CloneObject.Clone2("RTProjDirLight03", "Payiferen", bShow=bOn, bLoad=bOn, matPos=pos5, bAttach=bAttachOn, soAvatar=av)
    #CloneObject.Clone2("RTDirLight01Anim", "EderTsogal", bShow=bOn, bLoad=bOn, matPos=pos6, bAttach=bAttachOn, soAvatar=av)
    CloneObject.Clone2("RTProjDirLight02", "Payiferen", bShow=bOn, bLoad=bOn, matPos=pos6, bAttach=bAttachOn, soAvatar=av)

#
#def LightForKveer2(av, num=1, bLoadShowOn=True, bAttachOn=False):
def LightForKveer2(av, num=1, bLoadShowOn=True, bAttachOn=False, dx=0, dy=0, dz=0, rx=0, ry=0, rz=0):
    bOn = bLoadShowOn
    """
    pos1 = ptMatrix44()
    pos2 = ptMatrix44()
    pos3 = ptMatrix44()
    pos4 = ptMatrix44()
    """
    """
    tuplePos1 = ((-0.999985933304, -0.00528157455847, 0.0, -0.273455888033), (0.00528157455847, -0.999985933304, 0.0, -47.5185241699), (0.0, 0.0, 1.0, 9.40436553955), (0.0, 0.0, 0.0, 1.0))
    tuplePos2 = ((-0.999986410141, -0.00528157642111, 0.0, -0.273455888033), (0.00528157642111, -0.999986410141, 0.0, -47.5185241699), (0.0, 0.0, 1.0, 48.0664749146), (0.0, 0.0, 0.0, 1.0))
    tuplePos3 = ((0.999998033047, 0.00198203604668, 0.0, 0.119770005345), (-0.00198203604668, 0.999998033047, 0.0, 3.88968443871), (0.0, 0.0, 1.0, 49.4459877014), (0.0, 0.0, 0.0, 1.0))
    tuplePos4 = ((-0.999917268753, -0.0128562794998, 0.0, -0.539468109608), (0.0128562794998, -0.999917268753, 0.0, -71.0015563965), (0.0, 0.0, 1.0, 9.40436553955), (0.0, 0.0, 0.0, 1.0))
    """
    """
    tuplePos1 = ((-1.0, 0.0, 0.0, 0.0), (0.0, -1.0, 0.0, -50.0), (0.0, 0.0, 1.0, 10.0), (0.0, 0.0, 0.0, 1.0))
    tuplePos2 = ((-1.0, 0.0, 0.0, 0.0), (0.0, -1.0, 0.0, -50.0), (0.0, 0.0, 1.0, 50.0), (0.0, 0.0, 0.0, 1.0))
    tuplePos3 = ((1.0, 0.0, 0.0, 0.0), (0.0, 1.0, 0.0, 5.0), (0.0, 0.0, 1.0, 50.0), (0.0, 0.0, 0.0, 1.0))
    tuplePos4 = ((-1.0, 0.0, 0.0, 0.0), (0.0, -1.0, 0.0, -70.0), (0.0, 0.0, 1.0, 10.0), (0.0, 0.0, 0.0, 1.0))
    
    pos1.setData(tuplePos1)
    pos2.setData(tuplePos2)
    pos3.setData(tuplePos3)
    pos4.setData(tuplePos4)
    """
    
    #av = PtGetLocalAvatar()
    #pos = PtGetLocalAvatar().getLocalToWorld()
    pos = av.getLocalToWorld()
    
    pos1 = pos
    pos2 = pos
    pos3 = pos
    pos4 = pos
    """
    pos2.translate(ptVector3(0.0, 0.0, 40.0))
    pos3.translate(ptVector3(0.0, 55.0, 40.0))
    pos4.translate(ptVector3(0.0, -20.0, 0.0))
    
    mRot = ptMatrix44()
    mRot.rotate(2, (math.pi * float(180.0)) / 180)
    pos1 = pos1 * mRot
    pos2 = pos2 * mRot
    pos4 = pos4 * mRot
    """
    
    pos1.translate(ptVector3(dx, dy, dz))
    
    mRot = ptMatrix44()
    mRot.rotate(0, (math.pi * rx) / 180)
    mRot.rotate(1, (math.pi * ry) / 180)
    mRot.rotate(2, (math.pi * rz) / 180)
    
    pos1 = pos1 * mRot
    
    mRot = ptMatrix44()
    mRot.rotate(0, (math.pi * float(90.0)) / 180)
    pos6 = pos4 * mRot
    
    mRot = ptMatrix44()
    mRot.rotate(0, (math.pi * float(45.0)) / 180)
    pos5 = pos3 * mRot
    
    if num == 1:
        CloneObject.Clone2("RTOmniLight03", "EderTsogal", bShow=bOn, bLoad=bOn, matPos=pos1, bAttach=bAttachOn, soAvatar=av)
    elif num == 2:
        #CloneObject.Clone2("RTOmniLight04", "EderTsogal", bShow=bOn, bLoad=bOn, matPos=pos5, bAttach=bAttachOn, soAvatar=av)
        CloneObject.Clone2("RTOmniLight04", "EderTsogal", bShow=bOn, bLoad=bOn, matPos=pos1, bAttach=bAttachOn, soAvatar=av)
    elif num == 3:
        #CloneObject.Clone2("RTOmniLight05", "EderTsogal", bShow=bOn, bLoad=bOn, matPos=pos6, bAttach=bAttachOn, soAvatar=av)
        CloneObject.Clone2("RTOmniLight05", "EderTsogal", bShow=bOn, bLoad=bOn, matPos=pos1, bAttach=bAttachOn, soAvatar=av)
    elif num == 4:
        #CloneObject.Clone2("RTOmniLight06", "EderTsogal", bShow=bOn, bLoad=bOn, matPos=pos2, bAttach=bAttachOn, soAvatar=av)
        CloneObject.Clone2("RTOmniLight06", "EderTsogal", bShow=bOn, bLoad=bOn, matPos=pos1, bAttach=bAttachOn, soAvatar=av)
    elif num == 5:
        #CloneObject.Clone2("RTOmniLight07", "EderTsogal", bShow=bOn, bLoad=bOn, matPos=pos6, bAttach=bAttachOn, soAvatar=av)
        CloneObject.Clone2("RTOmniLight07", "EderTsogal", bShow=bOn, bLoad=bOn, matPos=pos1, bAttach=bAttachOn, soAvatar=av)
    elif num == 6:
        #CloneObject.Clone2("RTOmniLight09", "EderTsogal", bShow=bOn, bLoad=bOn, matPos=pos3, bAttach=bAttachOn, soAvatar=av)
        CloneObject.Clone2("RTOmniLight09", "EderTsogal", bShow=bOn, bLoad=bOn, matPos=pos1, bAttach=bAttachOn, soAvatar=av)
    elif num == 7:
        #CloneObject.Clone2("RTOmniLightFountain", "EderTsogal", bShow=bOn, bLoad=bOn, matPos=pos4, bAttach=bAttachOn, soAvatar=av)
        CloneObject.Clone2("RTOmniLightFountain", "EderTsogal", bShow=bOn, bLoad=bOn, matPos=pos1, bAttach=bAttachOn, soAvatar=av)
    elif num == 8:
        CloneObject.Clone2("RTProjDirLight03", "Payiferen", bShow=bOn, bLoad=bOn, matPos=pos5, bAttach=bAttachOn, soAvatar=av)
    elif num == 9:
        CloneObject.Clone2("RTProjDirLight02", "Payiferen", bShow=bOn, bLoad=bOn, matPos=pos6, bAttach=bAttachOn, soAvatar=av)

#
def LightForJalak(av, num=1, bLoadShowOn=True, bAttachOn=False, dx=0, dy=0, dz=0, rx=0, ry=0, rz=0):
    bOn = bLoadShowOn
    pos = av.getLocalToWorld()
    
    pos1 = pos
    pos2 = pos
    pos3 = pos
    pos4 = pos
    
    pos1.translate(ptVector3(dx, dy, dz))
    
    mRot = ptMatrix44()
    mRot.rotate(0, (math.pi * rx) / 180)
    mRot.rotate(1, (math.pi * ry) / 180)
    mRot.rotate(2, (math.pi * rz) / 180)
    
    pos1 = pos1 * mRot
    
    if num == 1:
        CloneObject.Clone2("RTOmniLight03", "EderTsogal", bShow=bOn, bLoad=bOn, matPos=pos1, bAttach=bAttachOn, soAvatar=av)
    elif num == 2:
        CloneObject.Clone2("RTOmniLight04", "EderTsogal", bShow=bOn, bLoad=bOn, matPos=pos1, bAttach=bAttachOn, soAvatar=av)
    elif num == 3:
        CloneObject.Clone2("RTOmniLight09", "EderTsogal", bShow=bOn, bLoad=bOn, matPos=pos1, bAttach=bAttachOn, soAvatar=av)
    elif num == 4:
        CloneObject.Clone2("RTOmniLightFountain", "EderTsogal", bShow=bOn, bLoad=bOn, matPos=pos1, bAttach=bAttachOn, soAvatar=av)
    elif num == 5:
        CloneObject.Clone2("RTProjDirLight01", "Jalak", bShow=bOn, bLoad=bOn, matPos=pos1, bAttach=bAttachOn, soAvatar=av)
    elif num == 6:
        CloneObject.Clone2("RTOmniLightBluAmbient", "Jalak", bShow=bOn, bLoad=bOn, matPos=pos1, bAttach=bAttachOn, soAvatar=av)


# RIEN
"""
    CloneObject.Clone2("kpRTOmniLight02", "City", bShow=bOn, bLoad=bOn, matPos=mPos, bAttach=bOn, soAvatar=av)
    CloneObject.Clone2("Omni06LAntern", "City", bShow=bOn, bLoad=bOn, matPos=mPos, bAttach=bOn, soAvatar=av)
    CloneObject.Clone2("MT-PodiumSpot01", "City", bShow=bOn, bLoad=bOn, matPos=mPos, bAttach=bOn, soAvatar=av)
    CloneObject.Clone2("LIBWorkLight02a", "City", bShow=bOn, bLoad=bOn, matPos=mPos, bAttach=bOn, soAvatar=av)
    CloneObject.Clone2("RTPathLight15", "City", bShow=bOn, bLoad=bOn, matPos=mPos, bAttach=bOn, soAvatar=av)
    CloneObject.Clone2("RTSpotLight01", "City", bShow=bOn, bLoad=bOn, matPos=mPos, bAttach=bOn, soAvatar=av)
    CloneObject.Clone2("RTPrisonRmLight", "Kveer", bShow=bOn, bLoad=bOn, matPos=mPos, bAttach=bOn, soAvatar=av)
"""

# ?
def test2(bOn=True, fAngleX=90.0, fAngleY=0.0, fAngleZ=0.0):
    av = PtGetLocalAvatar()
    pos = PtGetLocalAvatar().getLocalToWorld()
    mRot = ptMatrix44()
    # rotation selon X : axis = 0
    mRot.rotate(0, (math.pi * float(fAngleX)) / 180)
    mRot.rotate(1, (math.pi * float(fAngleY)) / 180)
    mRot.rotate(2, (math.pi * float(fAngleZ)) / 180)
    mPos = pos * mRot
    CloneObject.Clone2("RTProjDirLight01", "Jalak", bShow=bOn, bLoad=bOn, matPos=mPos, bAttach=bOn, soAvatar=av)


# ?
def test3(bOn=True, fAngleX=90.0, fAngleY=0.0, fAngleZ=0.0):
    av = PtGetLocalAvatar()
    pos = PtGetLocalAvatar().getLocalToWorld()
    mRot = ptMatrix44()
    # rotation selon X : axis = 0
    mRot.rotate(0, (math.pi * float(fAngleX)) / 180)
    mRot.rotate(1, (math.pi * float(fAngleY)) / 180)
    mRot.rotate(2, (math.pi * float(fAngleZ)) / 180)
    mPos = pos * mRot
    CloneObject.co3("SunShadowtRTDirLight04", "Jalak", bShow=bOn, bLoad=bOn, scale=1, matPos=None)

# ?
def test4(bOn=True, fAngleX=90.0, fAngleY=0.0, fAngleZ=0.0):
    av = PtGetLocalAvatar()
    pos = PtGetLocalAvatar().getLocalToWorld()
    mRot = ptMatrix44()
    # rotation selon X : axis = 0
    mRot.rotate(0, (math.pi * float(fAngleX)) / 180)
    mRot.rotate(1, (math.pi * float(fAngleY)) / 180)
    mRot.rotate(2, (math.pi * float(fAngleZ)) / 180)
    mPos = pos * mRot
    CloneObject.co3("RTOmniLightBluAmbient", "Jalak", bShow=bOn, bLoad=bOn, scale=1, matPos=None)

# ?
def spark(bOn=True, fAngleX=90.0, fAngleY=0.0, fAngleZ=0.0):
    av = PtGetLocalAvatar()
    pos = PtGetLocalAvatar().getLocalToWorld()
    mRot = ptMatrix44()
    # rotation selon X : axis = 0
    mRot.rotate(0, (math.pi * float(fAngleX)) / 180)
    mRot.rotate(1, (math.pi * float(fAngleY)) / 180)
    mRot.rotate(2, (math.pi * float(fAngleZ)) / 180)
    mPos = pos * mRot
    CloneObject.co3("SparkEmitter", "Ahnonay", bShow=bOn, bLoad=bOn, scale=1, matPos=None)

# ?
def pellet(bOn=True, fAngleX=0.0, fAngleY=0.0, fAngleZ=0.0):
    av = PtGetLocalAvatar()
    pos = PtGetLocalAvatar().getLocalToWorld()
    mRot = ptMatrix44()
    # rotation selon X : axis = 0
    mRot.rotate(0, (math.pi * float(fAngleX)) / 180)
    mRot.rotate(1, (math.pi * float(fAngleY)) / 180)
    mRot.rotate(2, (math.pi * float(fAngleZ)) / 180)
    mPos = pos * mRot
    CloneObject.co3("MachineCamRespDummy", "PelletBahroCave", bShow=bOn, bLoad=bOn, scale=1, matPos=None)

# Objets tournants du relto (feux d'artifice)
def rotators(bOn=True, bAttachOn=True, fAngleX=90.0, fAngleY=0.0, fAngleZ=0.0):
    av = PtGetLocalAvatar()
    pos = PtGetLocalAvatar().getLocalToWorld()
    mRot = ptMatrix44()
    # rotation selon X : axis = 0
    mRot.rotate(0, (math.pi * float(fAngleX)) / 180)
    mRot.rotate(1, (math.pi * float(fAngleY)) / 180)
    mRot.rotate(2, (math.pi * float(fAngleZ)) / 180)
    mPos = pos * mRot
    CloneObject.Clone2("CalStoneFireMaster", "Personal", bShow=bOn, bLoad=bOn, matPos=mPos, bAttach=bAttachOn, soAvatar=av)

# Objets tournants du Nexus mainColumnRotatingDummy
def nexus(bOn=True, bAttachOn=True, fAngleX=90.0, fAngleY=0.0, fAngleZ=0.0):
    av = PtGetLocalAvatar()
    pos = PtGetLocalAvatar().getLocalToWorld()
    mRot = ptMatrix44()
    # rotation selon X : axis = 0
    mRot.rotate(0, (math.pi * float(fAngleX)) / 180)
    mRot.rotate(1, (math.pi * float(fAngleY)) / 180)
    mRot.rotate(2, (math.pi * float(fAngleZ)) / 180)
    mPos = pos * mRot
    CloneObject.Clone2("mainColumnRotatingDummy", "Nexus", bShow=bOn, bLoad=bOn, matPos=mPos, bAttach=bAttachOn, soAvatar=av)
"""
# Objets mouvants de Myst StarDummy (CalendarGlare05, StarsParticles, CalStar07Dtct, RTCalendarLight12)
# Rien de visible
def myst(bOn=True, bAttachOn=True, fAngleX=90.0, fAngleY=0.0, fAngleZ=0.0):
    av = PtGetLocalAvatar()
    pos = PtGetLocalAvatar().getLocalToWorld()
    mRot = ptMatrix44()
    # rotation selon X : axis = 0
    mRot.rotate(0, (math.pi * float(fAngleX)) / 180)
    mRot.rotate(1, (math.pi * float(fAngleY)) / 180)
    mRot.rotate(2, (math.pi * float(fAngleZ)) / 180)
    mPos = pos * mRot
    CloneObject.Clone2("StarDummy", "Myst", bShow=bOn, bLoad=bOn, matPos=mPos, bAttach=bAttachOn, soAvatar=av)
"""
"""
# A Gahreesen WellSub : ~PIVOTDUMMY ? plouf! rien!
def wellsub(bOn=True, bAttachOn=True, fAngleX=90.0, fAngleY=0.0, fAngleZ=0.0):
    av = PtGetLocalAvatar()
    pos = PtGetLocalAvatar().getLocalToWorld()
    mRot = ptMatrix44()
    # rotation selon X : axis = 0
    mRot.rotate(0, (math.pi * float(fAngleX)) / 180)
    mRot.rotate(1, (math.pi * float(fAngleY)) / 180)
    mRot.rotate(2, (math.pi * float(fAngleZ)) / 180)
    mPos = pos * mRot
    CloneObject.Clone2("WellSub", "Garrison", bShow=bOn, bLoad=bOn, matPos=mPos, bAttach=bAttachOn, soAvatar=av)
"""

#=================================================================

#
def AddGarExt():
    PtConsoleNet("Nav.PageInNode grsnExterior", 1)

#attacher so1 a so2 : attacher(obj, av) ou l'inverse    
def Attacher(so1, so2, bPhys=False):
    """attacher so1 à so2 : attacher(obj, av) ou l'inverse"""
    so1.physics.netForce(1)
    so1.draw.netForce(1)
    PtAttachObject(so1, so2, 1)

# detacher so1 de so2 : detach(obj, av) ou l'inverse    
def Detacher(so1, so2):
    so1.physics.netForce(1)
    so1.draw.netForce(1)
    PtDetachObject(so1, so2, 1)

# A Gahreesen WellSub : ~PIVOTDUMMY ? plouf! rien!
def wellsub(bAttachOn=True):
    av = PtGetLocalAvatar()
    #pos = PtGetLocalAvatar().getLocalToWorld()
    avxyz = av.position()
    avz = avxyz.getZ()
    #so = PtFindSceneobject("WellSub", "Garrison")
    so = PtFindSceneobject("~PIVOTDUMMY", "Garrison")
    #so = PtFindSceneobject("Box14", "Garrison")
    #so.physics.warp(pos)
    sopos = so.getLocalToWorld()
    matTrans = ptMatrix44()
    matTrans.translate(ptVector3(0.0, 0.0, avz - 10000.0))
    so.physics.warp(sopos * matTrans)

    if bAttachOn:
        Attacher(so1=av, so2=so, bPhys=False)
    else:
        Detacher(so1=av, so2=so)

#=================================================================

#
"""
Ahnonay

CloneObject.co3("RTOmniLightFliker", "Ahnonay", bShow=bOn, bLoad=bOn, scale=1, matPos=None)
CloneObject.co3("RTOmniLightFliker01", "Ahnonay", bShow=bOn, bLoad=bOn, scale=1, matPos=None)
CloneObject.co3("RTOmniLightFliker02", "Ahnonay", bShow=bOn, bLoad=bOn, scale=1, matPos=None)
CloneObject.co3("RTOmniLight01", "Ahnonay", bShow=bOn, bLoad=bOn, scale=1, matPos=None)
CloneObject.co3("RTOmniLight03", "Ahnonay", bShow=bOn, bLoad=bOn, scale=1, matPos=None)
CloneObject.co3("RTOmniLight04", "Ahnonay", bShow=bOn, bLoad=bOn, scale=1, matPos=None)
CloneObject.co3("RTOmniLight05", "Ahnonay", bShow=bOn, bLoad=bOn, scale=1, matPos=None)
CloneObject.co3("RTOmniLight06", "Ahnonay", bShow=bOn, bLoad=bOn, scale=1, matPos=None)
CloneObject.co3("RTOmniLight07", "Ahnonay", bShow=bOn, bLoad=bOn, scale=1, matPos=None)
CloneObject.co3("RTSpotLight01", "Ahnonay", bShow=bOn, bLoad=bOn, scale=1, matPos=None)
CloneObject.co3("RTSpotLight02", "Ahnonay", bShow=bOn, bLoad=bOn, scale=1, matPos=None)
CloneObject.co3("RTSpotLight03", "Ahnonay", bShow=bOn, bLoad=bOn, scale=1, matPos=None)
CloneObject.co3("RTSpotLight04", "Ahnonay", bShow=bOn, bLoad=bOn, scale=1, matPos=None)
CloneObject.co3("RTSpotLight05", "Ahnonay", bShow=bOn, bLoad=bOn, scale=1, matPos=None)
CloneObject.co3("RTSpotLight06", "Ahnonay", bShow=bOn, bLoad=bOn, scale=1, matPos=None)
CloneObject.co3("RTSpotLight07", "Ahnonay", bShow=bOn, bLoad=bOn, scale=1, matPos=None)
CloneObject.co3("RTSpotLight08", "Ahnonay", bShow=bOn, bLoad=bOn, scale=1, matPos=None)
CloneObject.co3("RTSpotLight09", "Ahnonay", bShow=bOn, bLoad=bOn, scale=1, matPos=None)
CloneObject.co3("RTSpotLight10", "Ahnonay", bShow=bOn, bLoad=bOn, scale=1, matPos=None)

Jalak
CloneObject.co3("SunShadowtRTDirLight04", "Jalak", bShow=bOn, bLoad=bOn, scale=1, matPos=None)
RTProjDirLight01
RTOmniLight02
RTOmniLight04
RTOmniLight06NEW
RTOmniLight07
RTOmniLight08
RTOmniLight02
RTOmniLight02
RTOmniLightBluAmbient
RTOmniLightBluAmbient01
RTOmniLightBluAmbient02
RTOmniLightBluAmbient03
RTOmniLightBluAmbient04
RTOmniLightBluAmbient05

PelletBahroCave:
MachineCamRespDummy

Personal:
CalStoneFireMaster
 FireworkRotater1
  FireworkRotater2
 FireworkRotater102
  FireworkRotater202
 FireworkRotater103
  FireworkRotater203

Nexus:
mainColumnRotatingDummy


"""