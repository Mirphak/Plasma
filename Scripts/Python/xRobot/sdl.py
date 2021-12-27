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
    #ToggleBoolSDL("tsoYeeshaPageGrassVis")
    ToggleBoolSDL("nb01LampOption01Vis")

#
def mink():
    ToggleBoolSDL("minkIsDayTime")


# Toggle Integer SDL.
def ToggleIntSDL(name, minValue, maxValue):
    try:
        sdlValue = GetSDL(name)
    except:
        print "sdl not found"
        return 0
    sdlValue = (sdlValue + 1 - minValue) % (maxValue - minValue + 1)
    sdlValue = sdlValue + minValue
    print "sdlValue={}".format(sdlValue)
    try:
        SetSDL(name, sdlValue)
    except:
        pass

#
def ti():
    ToggleIntSDL("", 0, 7)

# Changing the Hood SDL
def ToggleHoodSDL(name):
    ageInfo = PtGetAgeInfo()
    if (ageInfo.getAgeFilename() != "Neighborhood"):
        return 0
    name = name.lower()
    #
    if name.startswith("ga"):
        try:
            ToggleIntSDL("nb01StainedWindowOption", 0, 2)
        except:
            print "wrong sdl value"
    elif name.startswith("ed"):
        try:
            ToggleIntSDL("nb01StainedGlassEders", 1, 6)
        except:
            print "wrong sdl value"
    elif name.startswith("gr") or name == "gz":
        try:
            ToggleIntSDL("nb01StainedGlassGZ", 1, 3)
        except:
            print "wrong sdl value"
    elif name == "lamp":
        try:
            ToggleBoolSDL("nb01LampOption01Vis")
        except:
            print "wrong sdl value"

    else:
        print "name <> 'ga' or 'ed' or 'gz'"
        return 0

#

## Toggle Integer SDL.
#def ToggleIntSDL(name, minValue, maxValue):
#    try:
#        sdlValue = GetSDL(name)
#    except:
#        print "sdl not found"
#        return 0
#    sdlValue = (sdlValue + 1 - minValue) % (maxValue - minValue + 1)
#    sdlValue = sdlValue + minValue
#    print "sdlValue={}".format(sdlValue)
#    try:
#        SetSDL(name, sdlValue)
#    except:
#        pass

# globals
gotPellet = 0
lowerCave = 0
sdlSolutions = []
chronSolutions = []
SymbolsOnSecs = 0.0
sdlSolutionNames = ["plltImagerSolutionN","plltImagerSolutionE","plltImagerSolutionS","plltImagerSolutionW"]


def init():
    global gotPellet
    global lowerCave
    global sdlSolutions
    global chronSolutions
    
    ageSDL = PtGetAgeSDL()
    #ageSDL.setFlags(SDLGotPellet.value,1,1)
    #ageSDL.setFlags(1,1,1)
    #ageSDL.sendToClients(SDLGotPellet.value)

    for sdl in sdlSolutionNames:
        ageSDL = PtGetAgeSDL()
        ageSDL.setFlags(sdl,1,1)
        ageSDL.sendToClients(sdl)
        #ageSDL.setNotify(self.key,sdl,0.0)
        val = ageSDL[sdl][0]
        sdlSolutions.append(val)
    chronString = GetPelletCaveSolution()
    #print "found pellet cave solution: ",chronString
    try:
        chronString = chronString.split(",")
        for sol in chronString:
            chronSolutions.append(string.atoi(sol))
        print "found pellet cave solution: ",chronSolutions
        print "current sdl values for solution = ",sdlSolutions
        #if self.sceneobject.isLocallyOwned():
        ShowSymbols()
    except:
        print "ERROR!  Couldn't get the solution information, symbols won't appear"

    linkmgr = ptNetLinkingMgr()
    link = linkmgr.getCurrAgeLink()
    spawnPoint = link.getSpawnPoint()

    spTitle = spawnPoint.getTitle()
    spName = spawnPoint.getName()
    
    if spName == "LinkInPointLower":
        lowerCave = 1
        avatar = 0
        try:
            avatar = PtGetLocalAvatar()
        except:
            print"failed to get local avatar"
            return
        #avatar.avatar.registerForBehaviorNotify(self.key)
    else:
        lowerCave = 0
        vault = ptVault()
        entry = vault.findChronicleEntry("GotPellet")
        if type(entry) != type(None):
            entryValue = entry.chronicleGetValue()
            gotPellet = string.atoi(entryValue)
            if gotPellet != 0:
                entry.chronicleSetValue("%d" % (0))
                entry.save()
                avatar = PtGetLocalAvatar()
                avatar.avatar.registerForBehaviorNotify(self.key)
            else:
                return
        else:
            return
        
        try:
            ageSDL = PtGetAgeSDL()
        except:
            print "PelletBahroCave.OnServerInitComplete():\tERROR---Cannot find the PelletBahroCave Age SDL"
            ageSDL[SDLGotPellet.value] = (0,)
    
        ageSDL.setNotify(self.key,SDLGotPellet.value,0.0)
    
        pelletSDL = ageSDL[SDLGotPellet.value][0]
        if pelletSDL != gotPellet:
            ageSDL[SDLGotPellet.value] = (gotPellet,)
    
        PtDebugPrint("PelletBahroCave:OnServerInitComplete:  SDL for pellet is now %d" % (gotPellet))


def GetPelletCaveSolution():
    ageVault = ptAgeVault()
    ageInfoNode = ageVault.getAgeInfo()
    ageInfoChildren = ageInfoNode.getChildNodeRefList()
    for ageInfoChildRef in ageInfoChildren:
        ageInfoChild = ageInfoChildRef.getChild()
        folder = ageInfoChild.upcastToFolderNode()
        if folder and folder.folderGetName() == "AgeData":
            print "Found age data folder"
            ageDataChildren = folder.getChildNodeRefList()
            for ageDataChildRef in ageDataChildren:
                ageDataChild = ageDataChildRef.getChild()
                chron = ageDataChild.upcastToChronicleNode()
                if chron and chron.getName() == "PelletCaveSolution":
                    solution = chron.getValue()
                    return solution
                else:
                    return 0

def ShowSymbols():
    global sdlSolutions
    ageSDL = PtGetAgeSDL()
    n = 0
    chronSolutions = [1,2,3,4]
    sdlSolutions = [1,2,3,4]
    for sdl in sdlSolutions:
        """
        if sdlSolutions[n] != chronSolutions[n]:
            newVal = chronSolutions[n]
            ageSDL[sdlSolutionNames[n]] = (newVal,)
            sdlSolutions[n] = newVal
        """
        newVal = 1
        ageSDL[sdlSolutionNames[n]] = (newVal,)
        sdlSolutions[n] = newVal        
        n += 1
    print "SDL solutions list now = ",sdlSolutions

#=====================================
# GreatTreePub.sdl
#=====================================
"""
STATEDESC GreatTreePub
{
	VERSION 3

## Age Mechanics ##
    	VAR BOOL grtpErcanaLinkingBookVis[1] 		DEFAULT=0 DEFAULTOPTION=VAULT
    	VAR BOOL grtpAhnonayLinkingBookVis[1] 		DEFAULT=0 DEFAULTOPTION=VAULT
    	VAR BOOL grtpDRCWatchersJournalVis[1] 		DEFAULT=0 DEFAULTOPTION=VAULT
	VAR BOOL grtpWatchersJournalsVis[1] 		DEFAULT=0 DEFAULTOPTION=VAULT
	VAR BOOL islmGZBeamVis[1] 			DEFAULT=0 DEFAULTOPTION=VAULT
	VAR BOOL grtpBallHallDoorVis[1] 		DEFAULT=0 DEFAULTOPTION=VAULT
	VAR BOOL grtpDeadBahroVis[1] 			DEFAULT=0 DEFAULTOPTION=VAULT

}
"""

#
def GuildSdl():
    names = [
        "grtpErcanaLinkingBookVis",  # BOOL      0
        "grtpAhnonayLinkingBookVis", # BOOL      0
        "grtpDRCWatchersJournalVis", # BOOL      0
        "grtpWatchersJournalsVis",   # BOOL      0
        "islmGZBeamVis",             # BOOL      0
        "grtpBallHallDoorVis"        # BOOL      0
        "grtpDeadBahroVis"           # BOOL      0
    ]
    for name in names:
        try:
            value = GetSDL(name)
            print "Guil SDL name={}, value={}".format(name, value)
        except:
            print "Guil SDL \"{}\" not found".format(name)

# toggles guild bool sdl
def guild(name):
    dicNames = {
        "book":"grtpErcanaLinkingBookVis", 
        "first":"grtpAhnonayLinkingBookVis", 
        "switch":"grtpDRCWatchersJournalVis", 
        "bridge":"grtpWatchersJournalsVis", 
        "door":"islmGZBeamVis", 
        "ladder":"grtpBallHallDoorVis", 
        "ball":"grtpDeadBahroVis"
    }
    if (name in dicNames.keys()):
        ToggleBoolSDL(dicNames[name])
    else:
        print("wrong sdl name")


#=====================================
# city.sdl
#=====================================

# toggles city bool sdl
def city(name):
    dicNames = {
        "light":"islmLakeLightMeterVis", 
        "board":"islmReaderBoardVis", 
        "tent":"islmDRCTentVis", 
        "meet":"islmTokotahMeetingsVis", 
        "minorah":"islmMinorahVis", 
        "blocker":"islmCityBlocker17Vis", 
        "kahlo":"islmKahloPubHallCollapse", 
        "memorial":"islmMemorialImagerVis"
    }
    if (name in dicNames.keys()):
        ToggleBoolSDL(dicNames[name])
    else:
        print("wrong sdl name")



#
