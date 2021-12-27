# -*- coding: utf-8 -*-
"""
TEST 1
"""

from Plasma import *
from PlasmaTypes import *

from PlasmaVaultConstants import *


###########
#   SDL   #
###########

# Get an SDL value.
def GetSDL(name):
	sdl = PtGetAgeSDL()
	value = sdl[name][0]
	return value

# Set an SDL value.
def SetSDL(name, value):
	sdl = PtGetAgeSDL()
	sdl[name] = (value,)

# Toggle books.
def Books():
    Eder = GetSDL("nb01LinkBookEderVis")
    Garrison = GetSDL("nb01LinkBookGarrisonVis")
    GZ = GetSDL("nb01LinkBookGZVis")
    Nexus = GetSDL("nb01LinkBookNexusVis")
    Bahro = GetSDL("nb01BahroStonePedestalVis")
    if Eder == 0 or Garrison == 0 or GZ == 0 or Nexus == 0 or Bahro == 0:
        SetSDL("nb01LinkBookEderVis", 1)
        SetSDL("nb01LinkBookEderToggle", 2)
        SetSDL("nb01LinkBookGarrisonVis", 1)
        SetSDL("nb01LinkBookGZVis", 1)
        SetSDL("nb01LinkBookNexusVis", 1)
        SetSDL("nb01BahroStonePedestalVis", 1)
    else:
        SetSDL("nb01LinkBookEderVis", 0)
        SetSDL("nb01LinkBookEderToggle", 1)
        SetSDL("nb01LinkBookGarrisonVis", 0)
        SetSDL("nb01LinkBookGZVis", 0)
        SetSDL("nb01LinkBookNexusVis", 0)
        SetSDL("nb01BahroStonePedestalVis", 0)

# Toggle Eder books.
def Eders(i):
    eder = GetSDL("nb01LinkBookEderVis")
    print eder
    try:
        i = int(i)
        #2 = Delin
        #3 = Tsogal
        SetSDL("nb01LinkBookEderVis", 1)
        SetSDL("nb01LinkBookEderToggle", i)
    except:
        pass

#
"""
    VAR BYTE    nb01StainedWindowOption[1]   DEFAULT=0 DEFAULTOPTION=VAULT
    VAR BYTE    nb01StainedGlassEders[1]   DEFAULT=0 DEFAULTOPTION=VAULT
    VAR BYTE    nb01StainedGlassGZ[1]   DEFAULT=0 DEFAULTOPTION=VAULT
"""
# Changing the Stained Glass Panels
def Glass(name, i):
    try:
        ga = GetSDL("nb01StainedWindowOption")
        ed = GetSDL("nb01StainedGlassEders")
        gz = GetSDL("nb01StainedGlassGZ")
        print "Stain glass panels: ga={}, ed={}, gz{}".format(ga, ed, gz)
    except KeyError:
        print "sdl not found"
    name = name.lower()
    if name.startswith("ga"):
        try:
            i = int(i)
            SetSDL("nb01StainedWindowOption", i)
        except:
            print "wrong sdl value"
    elif name.startswith("ed"):
        try:
            i = int(i)
            SetSDL("nb01StainedGlassEders", i)
        except:
            print "wrong sdl value"
    elif name.startswith("gr") or name == "gz":
        try:
            i = int(i)
            SetSDL("nb01StainedGlassGZ", i)
        except:
            print "wrong sdl value"
    else:
        print "name <> 'ga' or 'ed' or 'gz'"
        return 0

#
"""
    VAR BOOL    nb01BeachBallVis[1]          DEFAULT=1 DEFAULTOPTION=VAULT
    VAR BOOL    nb01ClockVis[1]              DEFAULT=0 DEFAULTOPTION=VAULT
    VAR BOOL    nb01GardenFungusVis[1]       DEFAULT=0 DEFAULTOPTION=VAULT
    VAR BOOL    nb01GardenLightsVis[1]       DEFAULT=1 DEFAULTOPTION=VAULT
    VAR BOOL    nb01DestructionCracksVis[1]  DEFAULT=1 DEFAULTOPTION=VAULT
    VAR BOOL    nb01LanternsVis[1]           DEFAULT=0 DEFAULTOPTION=VAULT
    VAR BOOL    nb01LampOption01Vis[1]       DEFAULT=1 DEFAULTOPTION=VAULT
    VAR BOOL    nb01OldImager01Vis[1]        DEFAULT=1 DEFAULTOPTION=VAULT
    VAR BOOL    nb01OldImager02Vis[1]        DEFAULT=1 DEFAULTOPTION=VAULT
    VAR BOOL    nb01WaterfallTorchesVis[1]   DEFAULT=1 DEFAULTOPTION=VAULT
    VAR BOOL    nb01ResidenceAdditionsVis[1] DEFAULT=1 DEFAULTOPTION=VAULT
"""

# Toggle Bool SDL.
def ToggleBoolSDL(name):
    try:
        sdlValue = GetSDL(name)
    except:
        print "sdl not found"
        return 0
    sdlValue = not sdlValue
    print "sdlValue={}".format(sdlValue)
    try:
        SetSDL(name, sdlValue)
    except:
        pass

#
def tb():
    ToggleBoolSDL("tsoYeeshaPageGrassVis")

# Toggle Integer SDL.
def ToggleIntSDL(name, minValue, maxValue):
    try:
        sdlValue = GetSDL(name)
    except:
        print "sdl not found"
        return 0
    sdlValue = (sdlValue + 1) % (maxValue - minValue + 1)
    print "sdlValue={}".format(sdlValue)
    try:
        SetSDL(name, sdlValue)
    except:
        pass

#
def ti():
    ToggleBoolSDL("", 0, 7)

#
def ListMyAges():
    ages = ptVault().getAgesIOwnFolder().getChildNodeRefList()
    for age in ages:
        ageInfo = age.getChild().upcastToAgeLinkNode().getAgeInfo()
        print "{3} ({4}) {0}|{1}|{2}".format(ageInfo.getAgeInstanceName(), ageInfo.getAgeFilename(), ageInfo.getAgeInstanceGuid(), ageInfo.getAgeUserDefinedName(), ageInfo.getAgeSequenceNumber())

"""
# Mes ages sur Destiny:
# relto : Mirphak's (0) Relto|Personal|d924cbbd-7522-41c4-84f0-63113fe51140
# neighborhood : DS (2) Neighborhood|Neighborhood|9e683602-655d-4f07-aa7d-580bb76eb446
# aegura :  M¯À5­hï8hï8;#«x (0) Ae'gura|city|7e0facea-dae1-4aec-a4ca-e76c05fdcfcf
# avatarcustomization : Mirphak's (0) AvatarCustomization|AvatarCustomization|d93536c8-3817-4030-a2b6-ddd545811521
# pelletcave : Mirphak's (0) Pellet Cave|PelletBahroCave|093d762a-c544-4aeb-b596-a56860e421be
# nexus : Mirphak's (0) Nexus|Nexus|28454641-68fa-4fa4-905d-2c16e02e28e8
# kadish : Mirphak's (0) Kadish|Kadish|28b745f7-a652-4006-b851-12aa90ff00eb
# ercana : Mirphak's (0) Er'cana|Ercana|681fe7e3-7028-4832-a761-74135556e2c1
"""

# ** Test de recherche d'un joueur **
## never use that!
def FindPlayerByIDs(fromID, toID):
    playerNames = list()
    for playerID in range(fromID, toID):
        #print playerID
        tempNode = ptVaultPlayerInfoNode()
        tempNode.playerSetID(playerID)
        try:
            vault = ptVault()
            #print playerID
            playerName = vault.findNode(tempNode).upcastToPlayerInfoNode().playerGetName()
            print "%i %s" % (playerID, playerName)
            playerNames.append((playerID, playerName))
        except:
            pass
    return playerNames

#
class test1(ptResponder):
    ############################
    def __init__(self):
        ptResponder.__init__(self)
        #self.id = 9999
        #city.py
        self.id = 5026
        version = 1
        self.version = version
        print "__init__test1 v.", version,".0"

    ############################
    def OnFirstUpdate(self):
        #random.seed()
        print "====> OnFirstUpdate : no parameter"

    ############################
    def OnServerInitComplete(self):
        print "====> OnServerInitComplete : no parameter"
 
    ###########################
    def OnSDLNotify(self,VARname,SDLname,playerID,tag):
        print "====> OnNotify : VARname='{0}', SDLname='{1}', playerID='{2}', tag='{3}'".format(VARname,SDLname,playerID,tag)

   ############################
    def OnNotify(self,state,id,events):
        print "====> OnNotify : state='{0}', id='{1}', events='{2}', owned='{3}'".format(state, id, events, self.sceneobject.isLocallyOwned())

    ############################
    def OnTimer(self,TimerID):
        print "====> OnTimer : TimerID='{0}'".format(TimerID)

    ###########################
    def OnBackdoorMsg(self, target, param):
        print "====> OnBackdoorMsg : target='{0}', param='{1}'".format(target, param)
