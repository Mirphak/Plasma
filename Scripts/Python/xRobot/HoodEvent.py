# -*- coding: utf-8 -*-
from Plasma import *

from . import xBotAge
from . import CloneObject
from . import Fog2

"""
        # show or hide and/or (en/dis)able physics of an object list (optionnaly in age)
        elif chatmessage.lower().startswith("toggle "):
            chatmessage += "    "
            words = chatmessage.split(" ", 4)
            if len(words) > 4:
                name = words[1].strip()
                age = words[2].strip()
                bDrawOn = words[3].strip()
                bPhysicsOn = words[4].strip()
                if age == "":
                    #age = None
                    age = PtGetAgeInfo().getAgeFilename()
                if bDrawOn == "":
                    bDrawOn = False
                else:
                    try:
                        bDrawOn = bool(int(bDrawOn))
                    except:
                        PtSendKIMessage(kKILocalChatStatusMsg, "Err: the 3rd parameter must be a boolean! (0 = False, 1 = True)")
                        return
                if bPhysicsOn == "":
                    bPhysicsOn = False
                else:
                    try:
                        bPhysicsOn = bool(int(bPhysicsOn))
                    except:
                        PtSendKIMessage(kKILocalChatStatusMsg, "Err: the 4th parameter must be a boolean! (0 = False, 1 = True)")
                        return
                PtSendKIMessage(kKILocalChatStatusMsg, "toggle %s %s %s %s" % (name, age, str(bDrawOn), str(bPhysicsOn)))
                xBotAge.ToggleSceneObjects(name, age, bDrawOn, bPhysicsOn)
            return None
"""

"""
# Basic.ToggleDraw(string/ptSceneobject obj, int en, string age)
# Toggles the visibility setting on an object.
def ToggleDraw(obj, en=False, age=None):

    if age is None:
        age = PtGetAgeName()
    if not isinstance(obj, ptSceneobject):
        obj = PtFindSceneobject(obj, age)
    obj.draw.netForce(True)
    obj.draw.enable(en)

# Basic.TogglePhysics(string/ptSceneobject obj, int en, string age)
# Toggles the physics setting on an object.
def TogglePhysics(object, en=False, age=None):

    if age is None:
        age = PtGetAgeName()
    if not isinstance(object, ptSceneobject):
        object = PtFindSceneobject(object, age)
    object.physics.netForce(True)
    object.physics.enable(en)

# xRobot.xRelto
def ToggleObjects(name, bOn = True):
    pf = PtFindSceneobjects(name)
    for so in pf:
        so.netForce(1)
        so.draw.enable(bOn)

# xRobot.xRelto
def ToggleObject(name, bOn = True):
    so = PtFindSceneobject(name, age)
    if so is not None:
        so.netForce(1)
        so.draw.enable(bOn)

"""

"""
!toggle BlueLamp  0 0
Les objets :
    beeLamp01 à beeLamp27 (sauf beeLamp08) => pas ces lampes là!
    BlueLamp01 à 18, 21 à 27 => parmi celles-ci
    => 
    !toggle BlueLamp13  0 0 à !toggle BlueLamp18  0 0
    et 
    !toggle BlueLampGlare13  0 0 à !toggle BlueLampGlare18  0 0
    
    
    ImagerBody01 et 02
    ImagerBracket01 à 04
    img01-03 à 07, 11, 13 à 15, 17, 18, 25, 27, 29, 31 et 35
    img01-LegShad01 à 04
    img02-01 à 05, 08 à 10, 12 et 13
    ImgrHinge01 à 08
    Imgr-KI-Glow01 et 02
    Imgr-KI-Logo01 et 02
    ImgrPhotoPlane01 et 02
    ImgrShadow01 et 02
    ImgrStaticPlane01 et 02
    
    Plaza01, Plaza01SideFloor, plaza2
    RailCirc
    RockUnderTelescope, ScopePiece, TeleHandles, Telescope01, TelescopeLens01
    
    FountPillar01 à 04 => non
    => CommCenBalcPillars
    
    CommCenWall
    
    CaveWalls
    
 """

#
def NightTime(bOn=True):
    print("NightTime begin")
    
    # le style de rendu
    xBotAge.SetRenderer(style = "100000", start = 0, end = 0, density = 0, r = 0.2, g = 0.2, b = 0.4, cr = 0.4, cg = 0.4, cb = 0.5)
    
    if bOn:
        # Ajoutons le fog a couleur changeante
        Fog2.Start(delay=2., start=None, end=None, density=None)
    else:
        Fog2.Stop()
    
    print("NightTime done")
    return 0

#

# Page in the city harbor (to load lake, arch, mountains) 
def PageInHarbor():
    PtConsoleNet("Nav.PageInNode city_harbor", True)

# Page out the city harbor 
def PageOutHarbor():
    PtConsoleNet("Nav.PageOutNode city_harbor", True)

# Page in the city library 
def PageInLibrary():
    PtConsoleNet("Nav.PageInNode city_library", True)

# Page out the city library 
def PageOutLibrary():
    PtConsoleNet("Nav.PageOutNode city_library", True)

# Page in the city harbor (to load lake, arch, mountains) 
def PageInHarbor2():
    if PtGetAgeInfo().getAgeFilename() != "city":
        PtConsoleNet("Nav.PageInNode harbor", True)

# Page out the city harbor 
def PageOutHarbor2():
    if PtGetAgeInfo().getAgeFilename() != "city":
        PtConsoleNet("Nav.PageOutNode harbor", True)

# Page in the city library 
def PageInLibrary2():
    if PtGetAgeInfo().getAgeFilename() != "city":
        PtConsoleNet("Nav.PageInNode library", True)

# Page out the city library 
def PageOutLibrary2():
    if PtGetAgeInfo().getAgeFilename() != "city":
        PtConsoleNet("Nav.PageOutNode library", True)

#
def Toggle(objName, draw=False, phys=True):
    ageName = PtGetAgeInfo().getAgeFilename()
    xBotAge.ToggleSceneObjects(name=objName, age=ageName, bDrawOn=draw, bPhysicsOn=phys)

#
lstObjNames = [
    "BlueLamp13", 
    "BlueLamp14", 
    "BlueLamp15", 
    "BlueLamp16", 
    "BlueLamp17", 
    "BlueLamp18", 
    "BlueLampGlare13", 
    "BlueLampGlare14", 
    "BlueLampGlare15", 
    "BlueLampGlare16", 
    "BlueLampGlare17", 
    "BlueLampGlare18", 
    #"CollisionGeom", 
    "CommCenWall",
    "CommCenBalcPillars", 
    "RockUnderTelescope", 
    "ScopePiece", 
    "TeleHandles", 
    "Telescope01", 
    "TelescopeLens01", 
    "TelescopeProxyTerrain", 
    "ImagerBody0", 
    "ImagerBracket0", 
    "img0", 
    "Imgr", 
    "laza"
]

#
def LakeFront(bDraw=False, bPhys=False):
    for objName in lstObjNames:
        Toggle(objName, draw=bDraw, phys=bPhys)
    #Toggle("Cam", draw=bDraw, phys=bPhys)

#
def start():
    #LakeFront(bDraw=False, bPhys=False)
    CloneObject.Minkata(bShow=True, bLoad=True, soPlayer=None, matPos=None)
    PageInHarbor()
    PageInLibrary()
    PageInHarbor2()
    PageInLibrary2()
    NightTime(bOn=True)

#
def stop():
    #LakeFront(bDraw=True, bPhys=True)
    #CloneObject.Minkata(bShow=False, bLoad=False, soPlayer=None, matPos=None)
    #PageOutHarbor()
    #PageOutLibrary()
    #PageOutHarbor2()
    #PageOutLibrary2()
    NightTime(bOn=False)
