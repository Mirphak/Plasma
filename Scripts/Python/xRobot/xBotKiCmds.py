# -*- coding: utf-8 -*-

from Plasma import *
#from PlasmaGame import *
#from PlasmaGameConstants import *
from PlasmaKITypes import *
from PlasmaVaultConstants import *

import re

import xBotAge
import xCleft
import xHood
import xRelto
import xDelin
import xTsogal
import Columns2

#Ages de Mirphak et de Mir-o-Bot (d'autres viendront peut-etre)
import ages

# liste des instances disponibles pour moi
linkDic = ages.linkDic


# link yourself to an age instance
# type /linkto <ageName> in chat
#(the message is transformed in lowercase in xKI.py near line 7000)
#self.chatMgr.DisplayStatusMessage("Linking to " + ageName + " ...")
def LinkToAge(self, linkName):
    myself = PtGetLocalPlayer()
    linkName = linkName.lower().replace(" ", "").replace("'", "").replace("eder", "")
    #ageNames = map(lambda key: key.lower().replace(" ", "").replace("'", ""), ages.MirphakAgeDict)
    #plist = [myself]
    RemovePrpToLocal(self)
    if (linkName in linkDic.keys()):
        link = linkDic[linkName]
        #PtConsole("Net.LinkToAgeInstance " + link[1] + " " + link[2])
        #xBotAge.ChangerNomAge(link[0])
        xBotAge.currentBotAge = list(link)
        if len(link) > 4:
            xBotAge.SetBotAgeSP(link[4])
            self.chatMgr.AddChatLine(None, ",".join(xBotAge.currentBotAge), 3)
        xBotAge.LinkPlayerTo(self, link)
#    elif (linkName in ages.MirphakAgeDict.keys()):
#        link = ages.MirphakAgeDict[linkName]
#        xBotAge.currentBotAge = link
#        xBotAge.LinkPlayerTo(self, link)
    elif (linkName in ages.MirobotAgeDict.keys()):
        link = ages.MirobotAgeDict[linkName]
        xBotAge.currentBotAge = list(link)
        if len(link) > 4:
            xBotAge.SetBotAgeSP(link[4])
            self.chatMgr.AddChatLine(None, ",".join(xBotAge.currentBotAge), 3)
        xBotAge.LinkPlayerTo(self, link)
    elif (linkName in ages.MagicbotAgeDict.keys()):
        link = ages.MagicbotAgeDict[linkName]
        xBotAge.currentBotAge = list(link)
        if len(link) > 4:
            xBotAge.SetBotAgeSP(link[4])
            self.chatMgr.AddChatLine(None, ",".join(xBotAge.currentBotAge), 3)
        xBotAge.LinkPlayerTo(self, link)
    else:
        #pass
        msg = "Available links: " + str(linkDic.keys()) + " ** " + str(age.MirobotAgeDict.keys())
        #self.chatMgr.DisplayStatusMessage(msg)
        self.chatMgr.AddChatLine(None, msg, 3)

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
            self.chatMgr.AddChatLine(None, "You are warping to {}".format(spName), 3)
        else:
            self.chatMgr.AddChatLine(None, "Unknown spawn point! #{0}:{1}".format(spawnPointNumber, spName), 3)
    else:
        self.chatMgr.AddChatLine(None, "spawnPointNumber is None!", 3)

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
        #self.chatMgr.AddChatLine(None, msg, 3)
        return [1, msg]
    else:
        msg = name + " not found!"
        #self.chatMgr.AddChatLine(None, msg, 3)
        return [0, msg]

def ShowSceneObjects(self, name):
    msg = xBotAge.ShowSOWithNameLike(name)
    self.chatMgr.AddChatLine(None, msg, 3)

def ShowSceneObjectsInAge(self, name, age):
    msg = xBotAge.ShowSOWithNameLikeInAge(name, age)
    self.chatMgr.AddChatLine(None, msg, 3)

def ShowSceneObjectsWithCoords(self, name):
    msg = xBotAge.ShowSOWithCoords(name)
    self.chatMgr.AddChatLine(None, msg, 3)

#
def ShowSceneObjectsInAgeWithCoords(self, name, age):
    msg = xBotAge.ShowSOWithNameLikeInAgeWithCoords(name, age)
    self.chatMgr.AddChatLine(None, msg, 3)

#
def SearchAvatarNameLike(name):
    cond = r"[^a-z1-9*]"
    pat = re.sub(cond, ".", name.lower())
    pat = "^" + pat.replace("*", ".*") + ".*$"
    pattern = re.compile(pat)
    
    players = filter(lambda player: pattern.match(player.getPlayerName().lower()), PtGetPlayerList())
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
        #self.chatMgr.AddChatLine(None, msg, 3)
        return [1, msg]
    else:
        msg = name + " not found!"
        #self.chatMgr.AddChatLine(None, msg, 3)
        return [0, msg]

#
def GetCoord(self, name = None):
    self.chatMgr.AddChatLine(None, "> GetCoord", 3)
    if name is None:
        player = PtGetLocalPlayer()
    else:
        player = GetAgePlayerByName(name)
    if player is None:
        self.chatMgr.AddChatLine(None, "> No player like {} found in this age".format(name), 3)
        return 1
    else:
        soAvatar = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
        pos = soAvatar.position()
        params = [int(round(pos.getX())), int(round(pos.getY())),  int(pos.getZ()) + 1]
        msg = player.getPlayerName() + " found at (" + str(params[0]) + ", " + str(params[1]) + ", " + str(params[2]) + ")"
        self.chatMgr.AddChatLine(None, msg, 3)
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
    import newdesert
    newdesert.load()

#
def DisablePanicLinks(self):
    xBotAge.DisablePanicLinks()
    self.chatMgr.AddChatLine(None, "Panic links are disabled!", 3)

#
def RemovePrpToLocal(self):
    xCleft.DelPrpLocal()
    Columns2.DelPrpLocal()
    #Platform.DelPrpLocal()
    #xBugs.DelPrpLocal()
    #xPub.DelPrpLocal()
    #xRelto.DelPrpLocal()
    #xSpy.DelPrpLocal()

#
def Ring(self, color, bOn, height=4, dist=3):
    self.chatMgr.AddChatLine(None, ">Ring ", 3)
    color = color.lower()
    bOn = bOn.lower()
    #if not (color in ("yellow", "blue", "red", "white", "white2", "white3", "white4")):
    if not (color in ("yellow", "blue", "red", "white")):
        self.chatMgr.AddChatLine(None, "Err: the optional 1st parameter (color) must be yellow, blue, red or white!", 3)
        color = "white"
    if bOn == "off":
        bOn = 0
    else:
        bOn = 1
    try:
        height = float(height)
    except:
        self.chatMgr.AddChatLine(None, "Err: the optional 3rd parameter (height) must be a number!", 3)
        height = 4
    try:
        dist = float(dist)
    except:
        self.chatMgr.AddChatLine(None, "Err: the optional 3rd parameter (dist) must be a number!", 3)
        dist = 3

    if len(xBotAge.currentBotAge) > 1:
        if xBotAge.currentBotAge[1] == "Neighborhood":
            self.chatMgr.AddChatLine(None, "ring " + color + ", " + str(bOn), 3)
            #xHood.Entourer(3, 4, color, 9, PtGetLocalAvatar(), bOn)
            xHood.Entourer(dist, height, color, 9, PtGetLocalAvatar(), bOn)
            self.chatMgr.AddChatLine(None, "=> nb clones: " + str(len(xHood.lstClones)), 3)
        else:
            self.chatMgr.AddChatLine(None, "=> Je ne suis pas dans un Hood!", 3)
            xHood.Entourer(dist, height, color, 9, PtGetLocalAvatar(), bOn)
    else:
        self.chatMgr.AddChatLine(None, "=> Je ne sais pas dans quel age je suis!", 3)

# To open or close a Bahro door (in Eder Delin and Eder Tsogal currently)
def OpenOrCloseBahroDoor(self, sOpenOrClose):
    # set action
    if sOpenOrClose == "open":
        action = 0
    elif sOpenOrClose == "close":
        action = 1
    else:
        self.chatMgr.AddChatLine(None, "=> I don't know how to %s a door!" % (sOpenOrClose), 3)
        return
    # age cases
    if len(xBotAge.currentBotAge) > 1:
        if xBotAge.currentBotAge[1] == "EderDelin":
            self.chatMgr.AddChatLine(None, "OpenOrCloseBahroDoor %s, %s" % (xBotAge.currentBotAge[1], action), 3)
            xDelin.Door(action)
        elif xBotAge.currentBotAge[1] == "EderTsogal":
            self.chatMgr.AddChatLine(None, "OpenOrCloseBahroDoor %s, %s" % (xBotAge.currentBotAge[1], action), 3)
            xTsogal.Door(action)
        #elif xBotAge.currentBotAge[1] == "Garden":
        #    self.chatMgr.AddChatLine(None, "OpenOrCloseBahroDoor %s, %s" % (xBotAge.currentBotAge[1], action), 3)
        #    import xGarden
        #    xGarden.Door(action)
        else:
            self.chatMgr.AddChatLine(None, "=> Cette fonction ne fonctionne pas dans cet age!", 3)
    else:
        self.chatMgr.AddChatLine(None, "=> Je ne sais pas dans quel age je suis!", 3)

"""
    NEW
"""
#
def DisableFog(self):
    self.chatMgr.AddChatLine(None, ">DisableFog ", 3)
    try:
        xBotAge.NoFog()
        self.chatMgr.AddChatLine(None, "==> done.", 3)
        return 1
    except:
        return 0

#
def SetRendererStyle(self, vstyle="default"):
    self.chatMgr.AddChatLine(None, ">SetRendererStyle {}".format(vstyle), 3)
    try:
        xBotAge.SetRenderer(style = vstyle)
        self.chatMgr.AddChatLine(None, "==> done.", 3)
        return 1
    except:
        return 0

#
def SetRendererFogLinear(self, vstart=None, vend=None, vdensity=None):
    self.chatMgr.AddChatLine(None, ">SetRendererFogLinear {}, {}, {}".format(vstart, vend, vdensity), 3)
    try:
        xBotAge.SetRenderer(style = None, start = vstart, end = vend, density = vdensity)
        self.chatMgr.AddChatLine(None, "==> done.", 3)
        return 1
    except:
        return 0

#
def SetRendererFogColor(self, vr=None, vg=None, vb=None):
    self.chatMgr.AddChatLine(None, ">SetRendererFogColor {}, {}, {}".format(vr, vg, vb), 3)
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
        self.chatMgr.AddChatLine(None, "==> done. {}, {}, {}".format(vr, vg, vb), 3)
        return 1
    except:
        return 0

#
def SetRendererClearColor(self, vcr=None, vcg=None, vcb=None):
    self.chatMgr.AddChatLine(None, ">SetRendererClearColor {}, {}, {}".format(vcr, vcg, vcb), 3)
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
        self.chatMgr.AddChatLine(None, ">SetRendererClearColor vcr = {}".format(vcr), 3)
    else:
        strCol = str(vcr).lower()
        numero = 1
        match = re.match(r"([a-z]+)([1-5])", strCol, re.I)
        if match:
            items = match.groups()
            strCol = items[0]
            numero = int(items[1])
            self.chatMgr.AddChatLine(None, ">SetRendererClearColor match: strCol = {}, numero = {}".format(strCol, numero), 3)
        # nom de couleur connu?
        if strCol in dicColors.keys():
            #vcr = float(dicColors[strCol][0]) * (6. - float(numero)) / 5.
            #vcg = float(dicColors[strCol][1]) * (6. - float(numero)) / 5.
            #vcb = float(dicColors[strCol][2]) * (6. - float(numero)) / 5
            vcr = float(dicColors[strCol][0]) * ((6. - float(numero)) / 5.) ** 2
            vcg = float(dicColors[strCol][1]) * ((6. - float(numero)) / 5.) ** 2
            vcb = float(dicColors[strCol][2]) * ((6. - float(numero)) / 5.) ** 2
            self.chatMgr.AddChatLine(None, ">SetRendererClearColor color found and converted: ({}, {}, {}).".format(vcr, vcg, vcb), 3)
        else:
            vcr = None
            vcg = None
            vcb = None
            self.chatMgr.AddChatLine(None, ">SetRendererClearColor color not found, converted in: ({}, {}, {}).".format(vcr, vcg, vcb), 3)
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
        self.chatMgr.AddChatLine(None, "==> done. Back color changed to {} {} ==> ({}, {}, {}).".format(strCol, numero, vcr, vcg, vcb), 3)
        return 1
    except:
        return 0

# 
def ReltoNight(self, onoff="on", scale=None):
    self.chatMgr.AddChatLine(None, ">ReltoNight {} {}".format(onoff, scale), 3)
    
    bOn = True
    if onoff == "off":
        bOn = False
    #
    try:
        # age cases
        if len(xBotAge.currentBotAge) > 1:
            if xBotAge.currentBotAge[1] == "Personal":
                #self.chatMgr.AddChatLine(None, ">>ReltoNight xRelto.CreateNightSky(7.5, {})".format(bOn), 3)
                if scale is None:
                    scale = 7.5
                self.chatMgr.AddChatLine(None, ">>ReltoNight {}".format(msg), 3)
            elif xRelto.bPagesAdded:
                #self.chatMgr.AddChatLine(None, ">>ReltoNight xRelto.CreateNightSky(100, {})".format(bOn), 3)
                #msg = xRelto.CreateNightSky(100, bOn)
                if scale is None:
                    scale = 100
                self.chatMgr.AddChatLine(None, ">>ReltoNight {}".format(msg), 3)
            else:
                if scale is None:
                    scale = 50
        else:
            self.chatMgr.AddChatLine(None, "=> Je ne sais pas dans quel age je suis!", 3)
            if scale is None:
                scale = 75
        self.chatMgr.AddChatLine(None, ">>ReltoNight xRelto.CreateNightSky({}, {})".format(scale, bOn), 3)
        msg = xRelto.CreateNightSky(scale, bOn)
        self.chatMgr.AddChatLine(None, "==> done.", 3)
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
    self.chatMgr.AddChatLine(None, ">SkyOnOff {}".format(bOn), 3)
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
        self.chatMgr.AddChatLine(None, "==> done.", 3)
        return 1
    except:
        return 0

# Pour "nosky" equivalent a la commande "sky off"
def DisableSky(self, bOn=False):
    return SkyOnOff(self, bOn)

# 
def DustOnOff(self, bOn=True):
    self.chatMgr.AddChatLine(None, ">DustOnOff {}".format(bOn), 3)
    #bOn = True
    #if len(args) > 1:
    #    if args[1] == "off":
    #        bOn = False
    try:
        xBotAge.ToggleSceneObjects("Dust", age = "Minkata", bDrawOn = bOn, bPhysicsOn = bOn)
        self.chatMgr.AddChatLine(None, "==> done.", 3)
        return 1
    except:
        return 0

# Pour "nosky" equivalent a la commande "sky off"
def DisableDust(self, bOn=False):
    return DustOnOff(self, bOn)

#
# ** FIN **