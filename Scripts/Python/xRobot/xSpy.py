# -*- coding: utf-8 -*-

from Plasma import *

import Ride
import Platform
import math
import CloneFactory
import xBotAge

"""    week 2 (14/11/2015)
    Relto 
    Phil's Relto 
    Sky Room (Sharper’s Spyroom)

    There isn’t much to be done with the Reltos. 
    We just need to get to the bot’s Relto, and then warp to Phil’s. 
    The spyroom is another matter, though.
     
    For the spyroom, the goal is to import as much of tokotah as possible, and allow the guests to walk between them. 
    During the CavCon party, we did a little of it, but didn’t have the spyroom there. 
    The idea is to start in the spyroom, and then allow them to walk out of it over to the DRC conference room and down into Tokotah Courtyard. 
    That allows them to see the exact locations of both rooms. 
    A platform of Jalak pillars and a ramp made from one of them usually does the job. 
    Just how much of Ae’gura Island you import is up to you; we just need the parts that surround the spyroom and conference room for the tour, including the alley.
"""

"""
    Age: City
    Date: October 2002
    event manager hooks for the City

    from Plasma import *
    from PlasmaTypes import *

    IsPublic = 0
    IsKadishGallery = 0

    sdlS1FinaleBahro = [    "islmS1FinaleBahro","islmS1FinaleBahroCity1","islmS1FinaleBahroCity2",\
                                "islmS1FinaleBahroCity3","islmS1FinaleBahroCity4","islmS1FinaleBahroCity5",\
                                "islmS1FinaleBahroCity6"]
    pagesS1FinaleBahro = [    "bahroFlyers_arch","bahroFlyers_city1","bahroFlyers_city2",\
                                "bahroFlyers_city3","bahroFlyers_city4","bahroFlyers_city5",\
                                "bahroFlyers_city6"]
    #S1FinaleBahro = []
        pages = []

        # Add the common pages
        ## actually, we'll just set these to load automatically in the .age file
        #pages += ["KadishGallery""]
        
        # For the non-public age, add all the remaining pages
        if not IsKadishGallery:
            pages += ["canyon","cavetjunction","courtyard","ferry","greatstair","guildhall","harbor","HarborReflect"]
            pages += ["islmGreatZeroState","islmJCNote","islmNegilahnCreatureChartGUI","islmNickNote","islmPodMapGUI"]
            pages += ["islmWatsonLetterGUI","KahloPub","kahlopubtunnel","library","LibraryInterior"]
            pages += ["MuseumInteriorPage","palace","trailerCamPage"]
            pages += ["islmBahroShoutFerry","islmBahroShoutLibrary","islmBahroShoutPalace"]
            #pages += ["islmDRCStageState01","islmDRCStageState02","islmDRCTentTablePic","islmFanSoundRun"]
            #pages += ["islmLibBanners00Vis","islmLibBanners02Vis","islmLibBanners03Vis"]
            #pages += ["LibraryAhnonayVis","LibraryErcanaVis","LibraryGarrisonVis","LibraryKadishVis","LibraryTeledahnVis"]

            PtPageInNode(pages)
"""

# ====================================
# Paging city "courtyard"
age = "city"
bCityAdded = False

def AddPrp():
    global bCityAdded
    pages = ["courtyard","greatstair"]
    for page in pages:
        PtConsoleNet("Nav.PageInNode %s" % (page) , 1)
    bCityAdded = True

def AddSpy():
    global bCityAdded
    pages = ["spyroom"]
    for page in pages:
        PtConsoleNet("Nav.PageInNode %s" % (page) , 1)
    bCityAdded = True

def DelPrp():
    global bCityAdded
    pages = ["courtyard"]
    for page in pages:
        PtConsoleNet("Nav.PageOutNode %s" % (page) , 1)
    bCityAdded = False

def DelPrpLocal():
    global bCityAdded
    if bJalakAdded:
        pages = ["courtyard"]
        for page in pages:
            PtPageOutNode(page)
        bCityAdded = False

# ====================================
#
def hide():
    Platform.HideJalak()
    # Hide some objects
    names = ["column_23", "column_22",
        "column_21", "column_20", "column_19",
        "column_18", "column_17", "column_16", 
        "column_15", "Light"]
    Platform.ShowObjectList("jalak", names, False)
    names = ["Dak2FAKE", "Dak1Plane", "dkta",
        "DAK2grndEntrnc"]
    Platform.ShowObjectList("city", names, False)
    names = ["Wall"]
    Platform.ShowObjectList("spyroom", names, False)
    # Disable physics for some objects
    names = ["Collid"]
    Platform.PhysObjectList("spyroom", names, False)

#
def hj():
    Platform.HideJalak()

#
def hc():
    # Hide some objects
    names = ["column_23", "column_22",
        "column_21", "column_20", "column_19",
        "column_18", "column_17", "column_16", 
        "column_15", "Light"]
    Platform.ShowObjectList("jalak", names, False)

#
def hv():
    # Hide some objects
    names = ["Dak2FAKE", "Dak1Plane", "DakB", "dkta"]
    Platform.ShowObjectList("city", names, False)

#
def hw(bShow=False):
    # Hide some objects
    names = ["DAK2grndEntrnc"]
    Platform.ShowObjectList("city", names, bShow)

#
def hs():
    # Hide some objects
    names = ["Wall"]
    Platform.ShowObjectList("spyroom", names, False)
    # Disable physics for some objects
    names = ["Collid"]
    Platform.PhysObjectList("spyroom", names, False)


# platform(name="spy")
def platform(name="spy"):
    matPos = None
    if name == "spy":
        tupPos = ((0.841503858566, -0.540251135826, 0.0, -141.0), (0.540251135826, 0.841503858566, 0.0, -131.0), (0.0, 0.0, 1.0, 255.0), (0.0, 0.0, 0.0, 1.0)) 
        matPos = ptMatrix44()
        matPos.setData(tupPos)
    else:
        pass
    Platform.CreatePlatformSpy(bShow=False, matAv=matPos)

#
def panic():
    PtConsoleNet("Avatar.Spawn.DontPanic" , 1)

# wa(n="sun") wa(n="roof")
def wa(n=0):
    # les points de warp
    ws = { 
        "1": ((-0.444342970848, 0.895856797695, 0.0, -213.294143677), (-0.895856797695, -0.444342970848, 0.0, -322.820526123), (0.0, 0.0, 1.0, 13.7166614532), (0.0, 0.0, 0.0, 1.0)), 
        "2": ((-0.444342970848, 0.895856797695, 0.0, -104.294143677), (-0.895856797695, -0.444342970848, 0.0, -177.820526123), (0.0, 0.0, 1.0, 89.7166614532), (0.0, 0.0, 0.0, 1.0)), 
        "roof": ((-0.931317865849, -0.364206343889, 0.0, -77.659538269), (0.364206343889, -0.931317865849, 0.0, -178.524871826), (0.0, 0.0, 1.0, 159.332183838), (0.0, 0.0, 0.0, 1.0)), 
        "top": ((-0.212570428848, 0.977145791054, 0.0, -68.1296081543), (-0.977145791054, -0.212570428848, 0.0, -224.025436401), (0.0, 0.0, 1.0, 267.009216309), (0.0, 0.0, 0.0, 1.0)), 
        "sun": ((-0.624134302139, -0.78131711483, 0.0, -1188.0), (0.78131711483, -0.624134302139, 0.0, -1138.0), (0.0, 0.0, 1.0, 221.0), (0.0, 0.0, 0.0, 1.0))
        }
    #desactiver les zones de panique
    
    #recuperer tous les joueurs
    playerList = PtGetPlayerList()
    playerList.append(PtGetLocalPlayer())
    for player in playerList:
        objKey = PtGetAvatarKeyFromClientID(player.getPlayerID())
        soavatar = objKey.getSceneObject()
        
        #faire flotter tout le monde
        soavatar.physics.enable(0)
        soavatar.netForce(1)
        
        #deplacer les gens
        mat = ptMatrix44()
        try:
            mat.setData(ws[str(n)])
        except:
            mat = PtGetLocalAvatar().getLocalToWorld()
        soavatar.physics.warp(mat)
        soavatar.netForce(1)
        
        #reactiver la physique pour tous
        if n != 8:
            soavatar.physics.enable(1)
            soavatar.netForce(1)

""" ride
    ride(soName="oiseaut1", t=60.0)
    ride(soName="oiseaut2", t=60.0)
    ride(soName="shooter1", t=60.0)
    ride(soName="shooter2", t=60.0)
    ride(soName="shooter3", t=60.0)
    ride(soName="shooter4", t=60.0)
    ride(soName="shooter5", t=60.0)
    ride(soName="shroomie", t=60.0)
"""
#
def ride(soName="oiseaut1", t=60.0):
    #recuperer tous les joueurs
    playerList = PtGetPlayerList()
    playerList.append(PtGetLocalPlayer())
    for player in playerList:
        """
        objKey = PtGetAvatarKeyFromClientID(player.getPlayerID())
        soavatar = objKey.getSceneObject()
        
        #faire flotter tout le monde
        soavatar.physics.enable(0)
        soavatar.netForce(1)
        """
        #
        playerName = player.getPlayerName()
        Ride.Suivre(objet=soName, Avatar=playerName, duree=t)

"""
"""

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



#===============

#
#def LinkPlayerTo(self, age, playerID = None, spawnPointNumber = None):
def LinkPlayerTo(age, playerID = None, spawnPointNumber = None):
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

"""
    "aegura":["city", "city", "9511bed4-d2cb-40a6-9983-6025cdb68d8b", "Mir-o-Bot's", "LinkInPointBahro-PalaceBalcony"],
    "relto":["Relto", "Personal", "6e7a66cc-e0c1-4efc-977a-cd7a354a736a", "Mir-o-Bot's", "LinkInPointBahroPoles"], 
    "Office":["Ae'gura", "BaronCityOffice", "2aaf334b-a49e-40f2-963b-5be146d40021", "Mir-o-Bot's Office", ""],
    "spyroom":["spyroom", "spyroom", "df9d49ec-0b9c-4716-9a0f-a1b66f7d9814", "mob's (Sharper's spy room)", ""],
    "phil":["philRelto", "philRelto", "e8a2aaed-5cab-40b6-97f3-6d19dd92a71f", "philRelto", ""],
"""

#
def LinkAll(ageName):
    if ageName == "spy":
        age = ["spyroom", "spyroom", "df9d49ec-0b9c-4716-9a0f-a1b66f7d9814", "mob's (Sharper's spy room)", ""]
    elif ageName == "office":
        age = ["Ae'gura", "BaronCityOffice", "2aaf334b-a49e-40f2-963b-5be146d40021", "Mir-o-Bot's Office", ""]
    elif ageName == "phil":
        age = ["philRelto", "philRelto", "e8a2aaed-5cab-40b6-97f3-6d19dd92a71f", "philRelto", ""]
    elif ageName == "relto":
        age = ["Relto", "Personal", "6e7a66cc-e0c1-4efc-977a-cd7a354a736a", "Mir-o-Bot's", "LinkInPointBahroPoles"]
    elif ageName == "aegura":
        age = ["city", "city", "9511bed4-d2cb-40a6-9983-6025cdb68d8b", "Mir-o-Bot's", "LinkInPointBahro-PalaceBalcony"]

    #les autre joueurs dans mon age
    for player in PtGetPlayerList():
        #playerID = player.getPlayerID()
        LinkPlayerTo(age, playerID = player.getPlayerID(), spawnPointNumber = None)
    # link myself
    LinkPlayerTo(age, playerID = None, spawnPointNumber = None)

