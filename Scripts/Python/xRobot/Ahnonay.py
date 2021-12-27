# -*- coding: utf-8 -*-

# == Script pour Ahnonay ==
# Mirphak 2016-12-01 version 1
# Mirphak 2017-06-24 version 2
"""
    ** Larry's wish list 2017-06-05 **
    1 - We start out in the Ahnonay Cathedral, and that’s just a matter of getting there. 
        There is nothing outside the model and no special effects are needed. 
        We give a short lecture on it and then move on.

    2 - Water Ahnonay: 
        Nothing much to do here except the lecture. 
        However, if you can find a way to increase the size of one of the quabs and superimpose it on your avatar, 
        that might be fun. We’ve never tried that before.

    3 - Misty Ahnonay: 
        We want to warp directly to it, and the ning trees should be intact. 
        Otherwise, no special effects are needed.

    4 - Space Ahnonay: 
        Again, we want to warp directly there. 
        Another idea that we’ve never tried before is setting up an onlake effect so that we can run around 
        inside the sphere and see the rings from different points of view. 
        That’s not essential, though.

    5 - The 4th Sphere: 
        We want to show as much of the interior as possible, so if you can increase the light there, that would be nice. 
        An onlake effect would also be nice if we can do it. But we can get away with no effects at all if it’s too much bother. 
        That sphere often causes a lot of lag, so I’m not sure how much you can get away with.

    6 - The control rooms: 
        We can warp over to the control room attached to the 4th sphere directly, since it’s representative of them all. 
        Once there, we will want to open the hatch on request.

    7 - The hub room: 
        In the hub, we will want the machinery to cycle on request, so that the guest can see the 
        gears turning and the scene in the viewer change.

    8 - Kadish’s office: 
        We want to have the doors and window shutters open in advance. 
        We will want the sphere machine to turn on request.

    9 - After the tour: 
        We want to have two areas where the guests can see the outside. 
        The first is the area outside Kadish’s office where the vogondola track changes from magnetic levitation to the sail car. 
        The second is the area around the sphere machine. 
        Some kind of platform or onlake effect will be needed so that the guests can run around. 
        The areas are tricky, since there are zones where all the scenery disappears and we lose all points of reference. 
        Whatever you can do will be appreciated.

    **
        80, -1108, 1011
        -83, -2042, 17
        66, -1066, -980
        51, -127, 83
        147, 118, 84
        31, -489, 1007
        -12, -418, 1007
        10, 590, 84
        3, 688, 87
        -874, -1243, 9762
        -852, -1255, 9768
        -822, -1291, 9765
        674, 79, 9740

"""

from Plasma import *
from PlasmaTypes import *
from xPsnlVaultSDL import *
import time

import math
import sdl
import Platform

# Cette fonction ne s'utilise pas seule, elle est appelee par Courant()
def RunResp(key, resp, stateidx=None, netForce=1, netPropagate=1, fastforward=0):
    nt = ptNotify(key)
    nt.addReceiver(resp)
    nt.netPropagate(netPropagate)
    nt.netForce(netForce)
    if stateidx != None:
        nt.addResponderState(stateidx)
    if fastforward:
        nt.setType(PtNotificationType.kResponderFF)
        nt.netPropagate(0)
        nt.netForce(0)
    nt.setActivate(1.0)
    nt.send()

# Turn the current on or off ('off' = 0, 'on' = 1)
def Courant(action=0):
    objName = "hutValveWheel"
    ageName = "Ahnonay"
    so = PtFindSceneobject(objName, ageName)
    responders = so.getResponders()
    RunResp(key = so.getKey(), resp = responders[0], stateidx = action, netForce = 1, netPropagate = 1, fastforward = 0)
    RunResp(key = so.getKey(), resp = responders[1], stateidx = action, netForce = 1, netPropagate = 1, fastforward = 0)

# pour savoir dans quelle sphere on se trouve
def QSphere():
    ageName = PtGetAgeName()
    if ageName != 'Ahnonay' :
        print "Vous n'etes pas a Ahnonay"
        return 0
    else:
        ageSDL = PtGetAgeSDL ()
        sphere = ageSDL ["ahnyCurrentSphere"] [0]
        print "Vous etes dans la sphere {}".format(sphere)
        return sphere

# To rotate to the next sphere, return the active sphere (sphere = 1 a 4)
def RotateSphere():
    ageName = PtGetAgeName()
    
    if ageName != 'Ahnonay':
        return [0, "The bot must be in Ahnonay to use this command."]
    
    ageSDL = PtGetAgeSDL()
    sphere = ageSDL["ahnyCurrentSphere"][0]
    val = (sphere % 4) + 1
    ageSDL ["ahnyCurrentSphere"] = (val,)
    return [1, "The sphere {0} is now active. PM me 'TO AHNONAY' to go there or turn again.".format(val)]

#================================================
#
#================================================
"""
        if newSphere == 1:
            PtPageInNode("Sphere01BuildingInterior")
            PtPageInNode("MaintRoom01")
            PtPageInNode("ahnySphere01")
        elif newSphere == 2:
            PtPageInNode("MaintRoom02")
            PtPageInNode("ahnySphere02")
        elif newSphere == 3:
            PtPageInNode("MaintRoom03")
            PtPageInNode("ahnySphere03")
        elif newSphere == 4:
            PtPageInNode("Vortex")
            PtPageInNode("Hub")
            PtPageInNode("MaintRoom04")
            PtPageInNode("EngineerHut")
            PtPageInNode("ahnySphere04")
"""

# Find scene objects with name like soName in all loaded districts (aka pages or prp files)
# ex.: soName = "Bahro*Stone" will be transformed in regexp "^.*Bahro.*Stone.*$"
def FindSOName(soName):
    import re
    cond = "^.*" + soName.replace("*", ".*") + ".*$"
    try:
        pattern = re.compile(cond, re.IGNORECASE)
    except:
        return list()
    strList = soName.split("*")
    nameList = list()
    for str in strList:
        nameList.extend(map(lambda so: so.getName(), PtFindSceneobjects(str)))
    nameList = list(set(nameList))
    nameList = filter(lambda x: pattern.match(x) != None, nameList)
    return nameList

# Find scene objects with name like soName in all loaded districts (Warning, it includes GUI)
def FindSOLike(soName):
    nameList = FindSOName(soName)
    soList = list()
    for soName in nameList:
        sol = PtFindSceneobjects(soName)
        soList.extend(sol)
    return soList

# Remove the panic regions, I assume that all the panic links contain "Panic" or "panic" in there names.
def DisablePanicLinks():
    sol = FindSOLike("anic")
    for so in sol:
        so.netForce(1)
        so.physics.disable()

#
def panic():
    PtConsoleNet("Avatar.Spawn.DontPanic" , 1)

# toggles guild bool sdl
def togglesdl(name):
    dicNames = {
        "wings":"ercaHrvstrWingsOk", 
        "wd":"ercaHrvstrWingLeverDown", 
    }
    if (name in dicNames.keys()):
        sdl.ToggleBoolSDL(dicNames[name])
    else:
        print("wrong sdl name")

# platform(name="spy")
def platform(where=None):
    matPos = None
    if where is None or where not in range(1, 5):
        matPos = PtGetLocalAvatar().getLocalToWorld()
    else:
        if where == 1:
            tupPos = ((0.98276501894, 0.184859260917, 0.0, 23.3415126801), (-0.184859260917, 0.98276501894, 0.0, 54.0308570862), (0.0, 0.0, 1.0, -0.0328424945474), (0.0, 0.0, 0.0, 1.0))
        elif where == 2:
            tupPos = ((-0.897078573704, -0.44187015295, 0.0, 649.721862793), (0.44187015295, -0.897078573704, 0.0, -877.984619141), (0.0, 0.0, 1.0, 9445.71386719), (0.0, 0.0, 0.0, 1.0))
        elif where == 3:
            tupPos = ((0.00954949762672, -0.999954581261, 0.0, -102.545890808), (0.999954581261, 0.00954949762672, 0.0, 54.9582672119), (0.0, 0.0, 1.0, 10563.0976562), (0.0, 0.0, 0.0, 1.0))
        elif where == 4:
            tupPos = ((-0.748968303204, 0.662607133389, 0.0, 1560.00488281), (-0.662607133389, -0.748968303204, 0.0, -51.4498291016), (0.0, 0.0, 1.0, 10171.9091797), (0.0, 0.0, 0.0, 1.0))
        elif where == 5:
            tupPos = ((-0.937420606613, -0.3482016325, 0.0, 993.751708984), (0.3482016325, -0.937420606613, 0.0, -455.378509521), (0.0, 0.0, 1.0, 9424.86523438), (0.0, 0.0, 0.0, 1.0))
        matPos = ptMatrix44()
        matPos.setData(tupPos)
        
    Platform.CreatePlatform2(bShow=False, matAv=matPos)

#========================================================


#