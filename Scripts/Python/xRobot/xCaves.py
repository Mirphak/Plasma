
"""
"""
from Plasma import *
from PlasmaTypes import *
from xPsnlVaultSDL import *
import time

import math
import sdl
import Platform



#Cette fonction ne s'utilise pas seule, elle est appelee par Courant()
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

# 

#
def LinkPlayerTo(age, playerID=None, spawnPointNumber=None):
    if not playerID or playerID == "":
        playerID = PtGetLocalPlayer().getPlayerID()
    else:
        try:
            playerID = long(playerID)
        except:
            return "incorrect playerID"
            #pass
    if len(age) < 3:
        #pass
        return "incorrect age"
    ageInstanceName = age[0]
    ageFileName = age[1]
    ageGuid = age[2]
    ageUserDefinedName = ""
    if len(age) > 3:
        ageUserDefinedName = age[3]
    
    ageLink = ptAgeLinkStruct()
    ageInfo = ptAgeInfoStruct()
    ageInfo.setAgeFilename(ageFileName)
    ageInfo.setAgeInstanceGuid(ageGuid)
    ageInfo.setAgeInstanceName(ageInstanceName)
    
    ageLink.setAgeInfo(ageInfo)
    """
    spawnPt = "LinkInPointDefault"
    if spawnPointNumber:
        spawnPt = GetSpawnPoint(spawnPointNumber)
    else:
        ageSpawPoint = ""
        if len(age) > 4:
            ageSpawPoint = age[4]
        if ageSpawPoint != "":
            spawnPt = ageSpawPoint
    #self.chatMgr.AddChatLine(None, "sp=\""+spawnPt+"\"", 3)
    spawnPoint = ptSpawnPointInfo()
    spawnPoint.setName(spawnPt)
    ageLink.setSpawnPoint(spawnPoint)
    """
    ptNetLinkingMgr().linkPlayerToAge(ageLink, playerID)
    return ageUserDefinedName + " " + ageInstanceName

#
def LinkAll(ageName="pelletcave"):
    ages = {
        "hi":["Hood of Illusions", "Neighborhood", "3cc44d4b-31e1-4dec-b6e6-4b63c72becc3", "The", ""],
        "cleft":["Cleft", "Cleft", "fef1ef9f-09dd-422c-a3d6-1229d615af85", "Mir-o-Bot's", "LinkInPointFissureDrop"], 
        "PrimeCave":["LiveBahroCaves", "LiveBahroCaves", "74b81313-c5f4-4eec-8e21-94d55e59ea8a", "Mir-o-Bot's Prime", ""],
        "PodsCave":["LiveBahroCaves", "LiveBahroCaves", "9b764f14-2d0e-493e-aa4a-e7ed218e3168", "Mir-o-Bot's Pods", ""],
        "EderCave":["LiveBahroCaves", "LiveBahroCaves", "1c9388c2-e4da-4e2e-a442-a0f58ad216b9", "Mir-o-Bot's Eder", ""],
        "Rudenna":["BahroCave", "BahroCave", "a8f6a5a6-4e5e-4d3f-9160-a9b75f0768c5", "Mir-o-Bot's Rudenna", ""],
        "pelletcave":["Pellet Cave", "PelletBahroCave", "13c1fdfc-44e2-4230-803a-147d8e6918a0", "Mir-o-Bot's (top)", ""], 
        "pellet1":["Pellet Cave", "PelletBahroCave", "13c1fdfc-44e2-4230-803a-147d8e6918a0", "Mir-o-Bot's (top)", "LinkInWithPellet"], 
        "pellet2":["Pellet Cave", "PelletBahroCave", "13c1fdfc-44e2-4230-803a-147d8e6918a0", "Mir-o-Bot's (bottom)", "LinkInPointLower"], 
    }
    
    ageName = ageName.lower()
    if (ageName in ages.keys()):
        age = ages[ageName]
    else:
        return
    
    #les autre joueurs dans mon age
    for player in PtGetPlayerList():
        LinkPlayerTo(age, playerID = player.getPlayerID(), spawnPointNumber = None)
    # link myself
    LinkPlayerTo(age, playerID = None, spawnPointNumber = None)

#
def wa(where=None):
    #avCentre = PtGetLocalAvatar()
    #mat = avCentre.getLocalToWorld()
    mat = None
    if where is None or where not in range(1, 5):
        mat = PtGetLocalAvatar().getLocalToWorld()
    else:
        """
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
        mat = ptMatrix44()
        mat.setData(tupPos)
        """
        return 0
    
    #recuperer tous les joueurs
    playerList = PtGetPlayerList()
    playerList.append(PtGetLocalPlayer())
    soAvatarList = map(lambda player: PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject(), playerList)
    for soavatar in soAvatarList:
        #faire flotter tout le monde
        soavatar.netForce(1)
        soavatar.physics.disable()
        soavatar.physics.enable(0)
        soavatar.netForce(1)
    for soavatar in soAvatarList:
        #deplacer les gens
        soavatar.physics.warp(mat)
        soavatar.netForce(1)
    for soavatar in soAvatarList:
        #reactiver la physique pour tous
        soavatar.physics.enable(1)
        soavatar.netForce(1)

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
    sol = FindSOLike("Panic")
    sol = sol.append(FindSOLike("panic"))
    for so in sol:
        so.netForce(1)
        so.physics.disable()

#
def panic():
    PtConsoleNet("Avatar.Spawn.DontPanic" , 1)

# =======================================================================================================


"""
# Compilation de:
# BahroCaveFloor.py (11/11/2014) [Created by Stone]
# Pellet.py (15/11/2014)
# Ajouts pour le Cavern Tour 9 du 30/01/2016
"""

"""
# -*- coding: utf-8 -*-
"""

from Plasma import *

"""
 1 : Cleft - Caverne du livre de Relto
 2 : Pellet Bahro Cave (a:top=ercana, b:bottom=ahnonay)
 3 : Bahro Cave (Rudenna, ...)
"""

# === 1 ===

# === 2 ===

#**********************************************************************
# Other backend functions. Undocumented.
def RunResponder(key, resp, stateidx = None, netForce = 1, netPropagate = 1, fastforward = 0):
    nt = ptNotify(key)
    nt.addReceiver(resp)
    nt.netPropagate(netPropagate)
    nt.netForce(netForce)
    if stateidx != None:
        nt.addResponderState(stateidx)
    if fastforward:
        nt.setType(PlasmaConstants.PtNotificationType.kResponderFF)
        nt.netPropagate(0)
        nt.netForce(0)
    nt.setActivate(1.0)
    nt.send()
    
def Responder(soName, respName, pfm = None, ageName = None, state = None, ff = False):
    if ageName == None:
        ageName = PtGetAgeName()
    
    so = PtFindSceneobject(soName, ageName)
    respKey = None
    for i in so.getResponders():
        if i.getName() == respName:
            respKey = i
            break
    
    if respKey == None:
        print "Responder():\tResponder not found..."
        return
    
    if pfm == None:
        pms = so.getPythonMods()
        if len(pms) == 0:
            key = respKey
        else:
            key = pms[0]
    else:
        key = PtFindSceneobject(pfm, ageName).getPythonMods()[0]
    
    RunResponder(PtGetLocalAvatar().getKey(), key, stateidx = state, fastforward = ff)

# BahroSymbolDecal + (N E S W) + _0 + (1 a 7)
soNameSymbols = [
    "BahroSymbolDecalN_01", 
    "BahroSymbolDecalE_01", 
    "BahroSymbolDecalS_01", 
    "BahroSymbolDecalW_01", 
    "BahroSymbolDecalN_02", 
    "BahroSymbolDecalE_02", 
    "BahroSymbolDecalS_02", 
    "BahroSymbolDecalW_02", 
    "BahroSymbolDecalN_03", 
    "BahroSymbolDecalE_03", 
    "BahroSymbolDecalS_03", 
    "BahroSymbolDecalW_03", 
    "BahroSymbolDecalN_04", 
    "BahroSymbolDecalE_04", 
    "BahroSymbolDecalS_04", 
    "BahroSymbolDecalW_04", 
    "BahroSymbolDecalN_05", 
    "BahroSymbolDecalE_05", 
    "BahroSymbolDecalS_05", 
    "BahroSymbolDecalW_05", 
    "BahroSymbolDecalN_06", 
    "BahroSymbolDecalE_06", 
    "BahroSymbolDecalS_06", 
    "BahroSymbolDecalW_06", 
    "BahroSymbolDecalN_07", 
    "BahroSymbolDecalE_07", 
    "BahroSymbolDecalS_07", 
    "BahroSymbolDecalW_07", 
    ]

# cRepSolutionSymbols + (On Off) + (N E S W)
symbolResps = [
    "cRepSolutionSymbolsOnN", 
    "cRepSolutionSymbolsOffN", 
    "cRepSolutionSymbolsOnE", 
    "cRepSolutionSymbolsOffE", 
    "cRepSolutionSymbolsOnS", 
    "cRepSolutionSymbolsOffS", 
    "cRepSolutionSymbolsOnW", 
    "cRepSolutionSymbolsOffW", 
    ]

# entree en haut avec un pellet
liwp={"LinkInWithPellet":["cRespFadeInPellet", "cRespDropPellet"]}

age = "PelletBahroCave"
#def RunResponder(key, resp, stateidx = None, netForce = 1, netPropagate = 1, fastforward = 0):
def pellet(respnum=0):
    so = PtFindSceneobject("LinkInWithPellet", age)
    sok = so.getKey()
    rn = liwp["LinkInWithPellet"][respnum]
    for resp in so.getResponders():
        if resp.getName() == rn:
            RunResponder(sok, resp)
            break

#def RunResponder(key, resp, stateidx = None, netForce = 1, netPropagate = 1, fastforward = 0):
def symbol(quad="N", n=1, bOn=True):
    quad = quad.upper()
    if quad not in ("N", "E", "S", "W"):
        quad = "N"
    if n not in range(1, 7):
        n = 1
    #soName = "BahroSymbolDecal" + quad + "_0" + str(n)
    soName = "BahroSymbolDecal" + quad + "_01"
    so = PtFindSceneobject(soName, age)
    print "so {} found".format(soName)
    sok = so.getKey()
    OnOff = "Off"
    if bOn:
        OnOff = "On"
    rn = "cRespSolutionSymbols" + OnOff + quad
    print "resp {} search...".format(rn)
    for resp in so.getResponders():
        print "= resp {} ?".format(resp.getName())
        if resp.getName() == rn:
            print "resp {} found".format(rn)
            RunResponder(sok, resp, n)
            break

#def RunResponder(key, resp, stateidx = None, netForce = 1, netPropagate = 1, fastforward = 0):
def machine(n=0):
    if n not in range(0, 6):
        n = 0
    soName = "MachineCamRespDummy"
    so = PtFindSceneobject(soName, age)
    print "so {} found".format(soName)
    sok = so.getKey()
    #rn = "cRespSolutionSymbols" + OnOff + quad
    #print "resp {} search...".format(rn)
    """
    for resp in so.getResponders():
        print "= resp {} ?".format(resp.getName())
        if resp.getName() == rn:
            print "resp {} found".format(rn)
            RunResponder(sok, resp)
            break
    """
    RunResponder(sok, so.getResponders()[n])

#
def drop():
    pellet(0)
    pellet(1)
    machine(4)
    symbol("N", 2, True)
    symbol("E", 4, True)
    symbol("S", 3, True)
    symbol("W", 7, True)


# === 3 ===

#
def Floor(en=True):
    age = 'BahroCave'
    d = {
        'Wedge-Garden': (
            ((1.0, 0.0, 0.0, 107.82222747802734), (0.0, 1.0, 0.0, -72.66735076904297), (0.0, 0.0, 1.0, 0.0), (0.0, 0.0, 0.0, 1.0)),
            ((1.0, 0.0, 0.0, 99.92294311523438), (0.0, 1.0, 0.0, -63.619476318359375), (0.0, 0.0, 1.0, 0.0), (0.0, 0.0, 0.0, 1.0)),
            ),
        'Wedge-Garrison': (
            ((1.0, 0.0, 0.0, 91.82986450195312), (0.0, 1.0, 0.0, -71.0843505859375), (0.0, 0.0, 1.0, 0.0), (0.0, 0.0, 0.0, 1.0)),
            ((1.0, 0.0, 0.0, 99.92294311523438), (0.0, 1.0, 0.0, -63.619476318359375), (0.0, 0.0, 1.0, 0.0), (0.0, 0.0, 0.0, 1.0)),
            ),
        'Wedge-Kadish': (
            ((1.0, 0.0, 0.0, 94.52781677246094), (0.0, 1.0, 0.0, -55.63653564453125), (0.0, 0.0, 1.0, 0.0), (0.0, 0.0, 0.0, 1.0)),
            ((1.0, 0.0, 0.0, 99.92294311523438), (0.0, 1.0, 0.0, -63.619476318359375), (0.0, 0.0, 1.0, 0.0), (0.0, 0.0, 0.0, 1.0)),
            ),
        'Wedge-Teledahn': (
            ((1.0, 0.0, 0.0, 108.13623809814453), (0.0, 1.0, 0.0, -56.494140625), (0.0, 0.0, 1.0, 0.0), (0.0, 0.0, 0.0, 1.0)),
            ((1.0, 0.0, 0.0, 99.92294311523438), (0.0, 1.0, 0.0, -63.619476318359375), (0.0, 0.0, 1.0, 0.0), (0.0, 0.0, 0.0, 1.0)),
            ),
        }
    for key, items in d.items():
        m = ptMatrix44()
        m.setData(items[en])
        p = PtFindSceneobject(key, age).physics
        p.netForce(1)
        p.warp(m)
         
        key = key + 'Exclude'
        p = PtFindSceneobject(key, age).physics
        p.netForce(1)
        p.enable(en)

# =============================
#==========================#
# Pellets
#==========================#
class Pellets:
    _running = False
    _xKiSelf = None
    _nbTry   = 0

    def __init__(self):
        print "Pellets: init"
        
    def Launch(self):
        #print "Pellets:"
        pass

    def onAlarm(self, param=1):
        #print "Pellets:onalarm"
        if not self._running:
            print "Pellets:not running"
            return
        #print "Pellets:call Launch"
        #self.Launch()
        if param == 1:
            machine(3)
            PtSetAlarm(19, self, 0)
        else:
            machine(4)
            PtSetAlarm(19, self, 1)
        
    def Start(self, xKiSelf):
        self._xKiSelf = xKiSelf
        if not self._running:
            self._running = True
            print "Pellets:start"
            self.onAlarm()

    def Stop(self):
        print "Pellets:stop"
        self._running = False

pellets = Pellets()
#


#