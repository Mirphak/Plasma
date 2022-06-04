# -*- coding: utf-8 -*-

from Plasma import *
#from PlasmaGame import *
#from PlasmaGameConstants import *
from PlasmaKITypes import *
from PlasmaVaultConstants import *

import re

from . import xBotAge
from . import xCleft
from . import xHood
from . import xRelto
from . import xDelin
from . import xTsogal
from . import Columns2
from . import Ride

#Ages de Mirphak et de Mir-o-Bot (d'autres viendront peut-etre)
from . import ages

# liste des instances disponibles pour moi
linkDic = ages.linkDic


# link yourself to an age instance
# type /linkto <ageName> in chat
#(the message is transformed in lowercase in xKI.py near line 7000)
def LinkToAge(self, linkName):
    myself = PtGetLocalPlayer()
    linkName = linkName.lower().replace(" ", "").replace("'", "").replace("eder", "")
    #ageNames = map(lambda key: key.lower().replace(" ", "").replace("'", ""), ages.MirphakAgeDict)
    #plist = [myself]
    RemovePrpToLocal(self)
    if (linkName in list(linkDic.keys())):
        link = linkDic[linkName]
        #PtConsole("Net.LinkToAgeInstance " + link[1] + " " + link[2])
        #xBotAge.ChangerNomAge(link[0])
        xBotAge.currentBotAge = list(link)
        if len(link) > 4:
            xBotAge.SetBotAgeSP(link[4])
            PtSendKIMessage(kKILocalChatStatusMsg, ",".join(xBotAge.currentBotAge))
        xBotAge.LinkPlayerTo(self, link)
#    elif (linkName in ages.MirphakAgeDict.keys()):
#        link = ages.MirphakAgeDict[linkName]
#        xBotAge.currentBotAge = link
#        xBotAge.LinkPlayerTo(self, link)
    elif (linkName in list(ages.MirobotAgeDict.keys())):
        link = ages.MirobotAgeDict[linkName]
        xBotAge.currentBotAge = list(link)
        if len(link) > 4:
            xBotAge.SetBotAgeSP(link[4])
            PtSendKIMessage(kKILocalChatStatusMsg, ",".join(xBotAge.currentBotAge))
        xBotAge.LinkPlayerTo(self, link)
    elif (linkName in list(ages.MagicbotAgeDict.keys())):
        link = ages.MagicbotAgeDict[linkName]
        xBotAge.currentBotAge = list(link)
        if len(link) > 4:
            xBotAge.SetBotAgeSP(link[4])
            PtSendKIMessage(kKILocalChatStatusMsg, ",".join(xBotAge.currentBotAge))
        xBotAge.LinkPlayerTo(self, link)
    else:
        #pass
        msg = "Available links: " + str(list(linkDic.keys())) + " ** " + str(list(age.MirobotAgeDict.keys()))
        PtSendKIMessage(kKILocalChatStatusMsg, msg)

#
def WarpToSpawnPoint(self, spNum=None):
    try:
        spawnPointNumber = int(spNum)
    except:
        spawnPointNumber = None
    if spawnPointNumber is not None:
        pos = xBotAge.GetSPCoord(spawnPointNumber)
        spName = xBotAge.GetSPName(spawnPointNumber)
        if isinstance(pos, ptMatrix44):
            soAvatar = PtGetLocalAvatar()
            soAvatar.netForce(1)
            soAvatar.physics.warp(pos)
            PtSendKIMessage(kKILocalChatStatusMsg, "You are warping to {}".format(spName))
        else:
            PtSendKIMessage(kKILocalChatStatusMsg, "Unknown spawn point! #{0}:{1}".format(spawnPointNumber, spName))
    else:
        PtSendKIMessage(kKILocalChatStatusMsg, "spawnPointNumber is None!")

#
def WarpToSceneObject(self, name):
    msg = ""
    so = xBotAge.GetFirstSoWithCoord(name)
    if so:
        pos = so.position()
        soAvatar = PtGetLocalAvatar()
        soAvatar.netForce(1)
        soAvatar.physics.warp(pos)
        msg = so.getName() + " found at (" + str(int(pos.getX())) + ", " + str(int(pos.getY())) + ", " + str(int(pos.getZ())) + ")"
        #PtSendKIMessage(kKILocalChatStatusMsg, msg)
        return [1, msg]
    else:
        msg = name + " not found!"
        #PtSendKIMessage(kKILocalChatStatusMsg, msg)
        return [0, msg]

def ShowSceneObjects(self, name):
    msg = xBotAge.ShowSOWithNameLike(name)
    PtSendKIMessage(kKILocalChatStatusMsg, msg)

def ShowSceneObjectsInAge(self, name, age):
    msg = xBotAge.ShowSOWithNameLikeInAge(name, age)
    PtSendKIMessage(kKILocalChatStatusMsg, msg)

def ShowSceneObjectsWithCoords(self, name):
    msg = xBotAge.ShowSOWithCoords(name)
    PtSendKIMessage(kKILocalChatStatusMsg, msg)

#
def ShowSceneObjectsInAgeWithCoords(self, name, age):
    msg = xBotAge.ShowSOWithNameLikeInAgeWithCoords(name, age)
    PtSendKIMessage(kKILocalChatStatusMsg, msg)

#
def SearchAvatarNameLike(name):
    cond = r"[^a-z1-9*]"
    pat = re.sub(cond, ".", name.lower())
    pat = "^" + pat.replace("*", ".*") + ".*$"
    pattern = re.compile(pat)
    
    players = [player for player in PtGetPlayerList() if pattern.match(player.getPlayerName().lower())]
    return players

#
def GetAgePlayerByName(name):
    players = SearchAvatarNameLike(name)
    if len(players) > 0:
        return players[0]
    else:
        return None

#
def WarpToPlayer(self, name):
    msg = ""
    avatar = GetAgePlayerByName(name)
    if avatar:
        soAvatar = PtGetAvatarKeyFromClientID(avatar.getPlayerID()).getSceneObject()
        pos = soAvatar.getLocalToWorld()
        soMe = PtGetLocalAvatar()
        soMe.netForce(1)
        soMe.physics.warp(pos)
        pos = soAvatar.position()
        msg = avatar.getPlayerName() + " found at (" + str(int(pos.getX())) + ", " + str(int(pos.getY())) + ", " + str(int(pos.getZ())) + ")"
        #PtSendKIMessage(kKILocalChatStatusMsg, msg)
        return [1, msg]
    else:
        msg = name + " not found!"
        #PtSendKIMessage(kKILocalChatStatusMsg, msg)
        return [0, msg]

#
def GetCoord(self, name = None):
    PtSendKIMessage(kKILocalChatStatusMsg, "> GetCoord")
    if name is None:
        player = PtGetLocalPlayer()
    else:
        player = GetAgePlayerByName(name)
    if player is None:
        PtSendKIMessage(kKILocalChatStatusMsg, "> No player like {} found in this age".format(name))
        return 1
    else:
        soAvatar = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
        pos = soAvatar.position()
        params = [int(round(pos.getX())), int(round(pos.getY())),  int(pos.getZ()) + 1]
        msg = player.getPlayerName() + " found at (" + str(params[0]) + ", " + str(params[1]) + ", " + str(params[2]) + ")"
        PtSendKIMessage(kKILocalChatStatusMsg, msg)
        return 1

#
def AddCleft(self):
    ret = xCleft.AddCleft(self, [0])
    if ret:
        PtSetAlarm(5, xBotAge.AlarmDisablePanicLinks(), 0)

#
def AddHood(self):
    ret = xHood.AddHood(self, [0])
    if ret:
        PtSetAlarm(5, xBotAge.AlarmDisablePanicLinks(), 0)

#
def AddRelto(self):
    ret = xRelto.AddRelto(self, [0])
    if ret:
        PtSetAlarm(5, xBotAge.AlarmDisablePanicLinks(), 0)

#Test du module d'Annabelle newdesert.py
def LoadNewDesert(self):
    from . import newdesert
    newdesert.load()

#
def DisablePanicLinks(self):
    xBotAge.DisablePanicLinks()
    PtSendKIMessage(kKILocalChatStatusMsg, "Panic links are disabled!")

#
def RemovePrpToLocal(self):
    xCleft.DelPrpLocal()
    Columns2.DelPrpLocal()
    #Platform.DelPrpLocal()
    #xBugs.DelPrpLocal()
    #xPub.DelPrpLocal()
    #xRelto.DelPrpLocal()
    #xSpy.DelPrpLocal()
    Ride.DelPrpLocal()

#
def Ring(self, color, bOn, height=4, dist=3):
    PtSendKIMessage(kKILocalChatStatusMsg, ">Ring ")
    color = color.lower()
    bOn = bOn.lower()
    #if not (color in ("yellow", "blue", "red", "white", "white2", "white3", "white4")):
    if not (color in ("yellow", "blue", "red", "white")):
        PtSendKIMessage(kKILocalChatStatusMsg, "Err: the optional 1st parameter (color) must be yellow, blue, red or white!")
        color = "white"
    if bOn == "off":
        bOn = 0
    else:
        bOn = 1
    try:
        height = float(height)
    except:
        PtSendKIMessage(kKILocalChatStatusMsg, "Err: the optional 3rd parameter (height) must be a number!")
        height = 4
    try:
        dist = float(dist)
    except:
        PtSendKIMessage(kKILocalChatStatusMsg, "Err: the optional 3rd parameter (dist) must be a number!")
        dist = 3

    if len(xBotAge.currentBotAge) > 1:
        if xBotAge.currentBotAge[1] == "Neighborhood":
            PtSendKIMessage(kKILocalChatStatusMsg, "ring " + color + ", " + str(bOn))
            #xHood.Entourer(3, 4, color, 9, PtGetLocalAvatar(), bOn)
            xHood.Entourer(dist, height, color, 9, PtGetLocalAvatar(), bOn)
            PtSendKIMessage(kKILocalChatStatusMsg, "=> nb clones: " + str(len(xHood.lstClones)))
        else:
            PtSendKIMessage(kKILocalChatStatusMsg, "=> Je ne suis pas dans un Hood!")
            xHood.Entourer(dist, height, color, 9, PtGetLocalAvatar(), bOn)
    else:
        PtSendKIMessage(kKILocalChatStatusMsg, "=> Je ne sais pas dans quel age je suis!")

# To open or close a Bahro door (in Eder Delin and Eder Tsogal currently)
def OpenOrCloseBahroDoor(self, sOpenOrClose):
    # set action
    if sOpenOrClose == "open":
        action = 0
    elif sOpenOrClose == "close":
        action = 1
    else:
        PtSendKIMessage(kKILocalChatStatusMsg, "=> I don't know how to %s a door!" % (sOpenOrClose))
        return
    # age cases
    if len(xBotAge.currentBotAge) > 1:
        if xBotAge.currentBotAge[1] == "EderDelin":
            PtSendKIMessage(kKILocalChatStatusMsg, "OpenOrCloseBahroDoor %s, %s" % (xBotAge.currentBotAge[1], action))
            xDelin.Door(action)
        elif xBotAge.currentBotAge[1] == "EderTsogal":
            PtSendKIMessage(kKILocalChatStatusMsg, "OpenOrCloseBahroDoor %s, %s" % (xBotAge.currentBotAge[1], action))
            xTsogal.Door(action)
        #elif xBotAge.currentBotAge[1] == "Garden":
        #    PtSendKIMessage(kKILocalChatStatusMsg, "OpenOrCloseBahroDoor %s, %s" % (xBotAge.currentBotAge[1], action))
        #    import xGarden
        #    xGarden.Door(action)
        else:
            PtSendKIMessage(kKILocalChatStatusMsg, "=> Cette fonction ne fonctionne pas dans cet age!")
    else:
        PtSendKIMessage(kKILocalChatStatusMsg, "=> Je ne sais pas dans quel age je suis!")

"""
    NEW
"""
#
def DisableFog(self):
    PtSendKIMessage(kKILocalChatStatusMsg, ">DisableFog ")
    try:
        xBotAge.NoFog()
        PtSendKIMessage(kKILocalChatStatusMsg, "==> done.")
        return 1
    except:
        return 0

#
def SetRendererStyle(self, vstyle="default"):
    PtSendKIMessage(kKILocalChatStatusMsg, ">SetRendererStyle {}".format(vstyle))
    try:
        xBotAge.SetRenderer(style = vstyle)
        PtSendKIMessage(kKILocalChatStatusMsg, "==> done.")
        return 1
    except:
        return 0

#
def SetRendererFogLinear(self, vstart=None, vend=None, vdensity=None):
    PtSendKIMessage(kKILocalChatStatusMsg, ">SetRendererFogLinear {}, {}, {}".format(vstart, vend, vdensity))
    try:
        xBotAge.SetRenderer(style = None, start = vstart, end = vend, density = vdensity)
        PtSendKIMessage(kKILocalChatStatusMsg, "==> done.")
        return 1
    except:
        return 0

#
def SetRendererFogColor(self, vr=None, vg=None, vb=None):
    PtSendKIMessage(kKILocalChatStatusMsg, ">SetRendererFogColor {}, {}, {}".format(vr, vg, vb))
    try:
        vr = float(vr)
    except:
        pass
    try:
        vg = float(vg)
    except:
        pass
    try:
        vb = float(vb)
    except:
        pass
    try:
        xBotAge.SetRenderer(style = None, r = vr, g = vg, b = vb)
        PtSendKIMessage(kKILocalChatStatusMsg, "==> done. {}, {}, {}".format(vr, vg, vb))
        return 1
    except:
        return 0

#
def SetRendererClearColor(self, vcr=None, vcg=None, vcb=None):
    PtSendKIMessage(kKILocalChatStatusMsg, ">SetRendererClearColor {}, {}, {}".format(vcr, vcg, vcb))
    strCol = None
    numero = None
    dicColors = {
                "white":[1, 1, 1], 
                "red":[1, 0, 0], 
                "orange":[1, .5, 0], 
                "brown":[1, .6, .15], 
                "yellow":[1, 1, 0], 
                "green":[0, 1, 0], 
                "blue":[0, 0, 1], 
                "violet":[1, 0, 1], 
                "black":[0, 0, 0], 
                "gold":[1, .84, 0],
                }
    if isinstance(vcr, float):
        vcr = float(vcr)
        PtSendKIMessage(kKILocalChatStatusMsg, ">SetRendererClearColor vcr = {}".format(vcr))
    else:
        strCol = str(vcr).lower()
        numero = 1
        match = re.match(r"([a-z]+)([1-5])", strCol, re.I)
        if match:
            items = match.groups()
            strCol = items[0]
            numero = int(items[1])
            PtSendKIMessage(kKILocalChatStatusMsg, ">SetRendererClearColor match: strCol = {}, numero = {}".format(strCol, numero))
        # nom de couleur connu?
        if strCol in list(dicColors.keys()):
            #vcr = float(dicColors[strCol][0]) * (6. - float(numero)) / 5.
            #vcg = float(dicColors[strCol][1]) * (6. - float(numero)) / 5.
            #vcb = float(dicColors[strCol][2]) * (6. - float(numero)) / 5
            vcr = float(dicColors[strCol][0]) * ((6. - float(numero)) / 5.) ** 2
            vcg = float(dicColors[strCol][1]) * ((6. - float(numero)) / 5.) ** 2
            vcb = float(dicColors[strCol][2]) * ((6. - float(numero)) / 5.) ** 2
            PtSendKIMessage(kKILocalChatStatusMsg, ">SetRendererClearColor color found and converted: ({}, {}, {}).".format(vcr, vcg, vcb))
        else:
            vcr = None
            vcg = None
            vcb = None
            PtSendKIMessage(kKILocalChatStatusMsg, ">SetRendererClearColor color not found, converted in: ({}, {}, {}).".format(vcr, vcg, vcb))
    if strCol is None:
        if isinstance(vcg, float):
            vcg = float(vcg)
        else:
            vcg = None
        if isinstance(vcb, float):
            vcb = float(vcb)
        else:
            vcb = None
    try:
        xBotAge.SetRenderer(style = None, cr = vcr, cg = vcg, cb = vcb)
        PtSendKIMessage(kKILocalChatStatusMsg, "==> done. Back color changed to {} {} ==> ({}, {}, {}).".format(strCol, numero, vcr, vcg, vcb))
        return 1
    except:
        return 0

# 
def ReltoNight(self, onoff="on", scale=None):
    PtSendKIMessage(kKILocalChatStatusMsg, ">ReltoNight {} {}".format(onoff, scale))
    
    bOn = True
    if onoff == "off":
        bOn = False
    #
    try:
        # age cases
        if len(xBotAge.currentBotAge) > 1:
            if xBotAge.currentBotAge[1] == "Personal":
                #PtSendKIMessage(kKILocalChatStatusMsg, ">>ReltoNight xRelto.CreateNightSky(7.5, {})".format(bOn))
                if scale is None:
                    scale = 7.5
                PtSendKIMessage(kKILocalChatStatusMsg, ">>ReltoNight {}".format(msg))
            elif xRelto.bPagesAdded:
                #PtSendKIMessage(kKILocalChatStatusMsg, ">>ReltoNight xRelto.CreateNightSky(100, {})".format(bOn))
                #msg = xRelto.CreateNightSky(100, bOn)
                if scale is None:
                    scale = 100
                PtSendKIMessage(kKILocalChatStatusMsg, ">>ReltoNight {}".format(msg))
            else:
                if scale is None:
                    scale = 50
        else:
            PtSendKIMessage(kKILocalChatStatusMsg, "=> Je ne sais pas dans quel age je suis!")
            if scale is None:
                scale = 75
        PtSendKIMessage(kKILocalChatStatusMsg, ">>ReltoNight xRelto.CreateNightSky({}, {})".format(scale, bOn))
        msg = xRelto.CreateNightSky(scale, bOn)
        PtSendKIMessage(kKILocalChatStatusMsg, "==> done.")
        return 1
    except:
        return 0

# 
def ReltoDay(self, bOn=True):
    
    #if len(args) > 1:
    #    if args[1] == "off":
    #        bOn = True
    return ReltoNight(self, not bOn)

# 
def SkyOnOff(self, bOn=True):
    PtSendKIMessage(kKILocalChatStatusMsg, ">SkyOnOff {}".format(bOn))
    #bOn = True
    #if len(args) > 1:
    #    if args[1] == "off":
    #        bOn = False
    try:
        xBotAge.ToggleSceneObjects("Sky", age = None, bDrawOn = bOn, bPhysicsOn = bOn)
        xBotAge.ToggleSceneObjects("ClearColor", age = "Minkata", bDrawOn = bOn, bPhysicsOn = bOn)
        xBotAge.ToggleSceneObjects("StarGlobe", age = "Minkata", bDrawOn = bOn, bPhysicsOn = bOn)
        #xBotAge.ToggleSceneObjects("Constellation", age = "Minkata", bDrawOn = bOn, bPhysicsOn = bOn)
        #xBotAge.ToggleSceneObjects("Galaxy", age = "Minkata", bDrawOn = bOn, bPhysicsOn = bOn)
        PtSendKIMessage(kKILocalChatStatusMsg, "==> done.")
        return 1
    except:
        return 0

# Pour "nosky" equivalent a la commande "sky off"
def DisableSky(self, bOn=False):
    return SkyOnOff(self, bOn)

# 
def DustOnOff(self, bOn=True):
    PtSendKIMessage(kKILocalChatStatusMsg, ">DustOnOff {}".format(bOn))
    #bOn = True
    #if len(args) > 1:
    #    if args[1] == "off":
    #        bOn = False
    try:
        xBotAge.ToggleSceneObjects("Dust", age = "Minkata", bDrawOn = bOn, bPhysicsOn = bOn)
        PtSendKIMessage(kKILocalChatStatusMsg, "==> done.")
        return 1
    except:
        return 0

# Pour "nosky" equivalent a la commande "sky off"
def DisableDust(self, bOn=False):
    return DustOnOff(self, bOn)

#
# ** FIN **