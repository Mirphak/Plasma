# -*- coding: utf-8 -*-

"""
    V1 : 23/01/2016
        - Cavern Tour 
    V2 : 11/02/2017
        - Cavern Tour 

	"Garden":{
		"SingleShow":{"Night":[], "Day":[]},
		"SingleHide":{"Day":[], "Night":[]},
		"GroupShow":{"Night":[], "Day":["Dome", "Rain", "Garden"]},
		"GroupHide":{"Day":[], "Night":["Dome", "Rain", "Garden"]}
	},
    
    delprp("kemoStorm") => ne fonctionne pas :(
    
    hide()
    
    //skycolor blue 4
"""
from Plasma import *
import math
import sdl
import Ride
import Platform

#
dicBot = {
    32319L:"Mir-o-Bot", 
    27527L:"Magic Bot", 
    71459L:"Mimi Bot", 
    #L:"Stone5", 
    64145L:"Annabot",
    #L:"SkydiverBot",
    3975L:"OHBot",
    24891L:"Magic-Treasure",
    26224L:"Magic Treasure",
    21190L:"Mimi Treasure",
    2332508L:"mob",
    }

# Larry LeDeay [KI: 11308]
plSpeakerID = 11308


#
def CercleV(coef=2.0, avCentre=None):
    if avCentre is None:
        avCentre = PtGetLocalAvatar()
    #agePlayers = GetAllAgePlayers()
    # ne pas tenir compte des robots
    agePlayers = filter(lambda pl: not(pl.getPlayerID() in dicBot.keys()), PtGetPlayerList())
    i = 0
    n = len(agePlayers)
    print "nb de joueurs: %s" % (n)
    dist = float(coef * n) / (2.0 * math.pi)
    print "distance: %s" % (dist)
    for i in range(n):
        player = agePlayers[i]
        avatar = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
        angle = (float(i) * 2.0 * math.pi) / float(n)
        print "angle(%s): %s" % (i, angle)
        dx = float(dist)*math.cos(angle)
        #dy = float(dist)*math.sin(angle)
        dy = 0
        dz = float(dist)*math.sin(angle)
        matrix = avCentre.getLocalToWorld()
        matrix.translate(ptVector3(dx, dy, dz))
        avatar.netForce(1)
        avatar.physics.warp(matrix)

#
def Cercle(coef=3.0, h=10.0, avCentre=None, bPhys=True):
    maxdist = 5
    matrix  = ptMatrix44()
    if isinstance(avCentre, ptMatrix44):
        matrix = avCentre
    elif avCentre is None:
        avCentre = PtGetLocalAvatar()
        matrix = avCentre.getLocalToWorld()
    
    #agePlayers = GetAllAgePlayers()
    # ne pas tenir compte des robots
    agePlayers = filter(lambda pl: not(pl.getPlayerID() in dicBot.keys()), PtGetPlayerList())
    agePlayers.append(PtGetLocalPlayer())
    soAvatarList = map(lambda player: PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject(), agePlayers)
    for soavatar in soAvatarList:
        #faire flotter tout le monde
        soavatar.netForce(1)
        soavatar.physics.disable()
        soavatar.physics.enable(0)
        soavatar.netForce(1)

    i = 0
    n = len(agePlayers)
    print "nb de joueurs: %s" % (n)
    dist = float(coef * n) / (2.0 * math.pi)
    print "distance: %s" % (dist)
    nbCercles = dist // maxdist
    if nbCercles > 0:
        dist = dist / nbCercles
    for i in range(n):
        avatar = soAvatarList[i]
        angle = (float(i%maxdist) * float(nbCercles) * 2.0 * math.pi) / float(n)
        dist = dist + (n // maxdist)
        print "angle(%s): %s" % (i, angle)
        dx = float(dist)*math.cos(angle)
        dy = float(dist)*math.sin(angle)
        #matrix = avCentre.getLocalToWorld()
        matrix.translate(ptVector3(dx, dy, float(h)))
        mRot = ptMatrix44()
        mRot.rotate(2, angle - math.pi)
        avatar.netForce(1)
        avatar.physics.warp(matrix * mRot)
    for soavatar in soAvatarList:
        soavatar.netForce(1)
        soavatar.physics.enable(bPhys)


"""    
    0 : Point d'arrivee dans l'age
    1 : 
    2 : 
    2 : 
    3 : 
    4 : 
    5 : 
    6 : 
    7 : 
    8 : 
    9 : 
    10: 
"""
def wa(n=None, bCircle=False):
    # les points de warp
    ws = { 
        "1": ((0.915973901749, 0.401237934828, 0.0, 0.772684156895), (-0.401237934828, 0.915973901749, 0.0, 565.721313477), (0.0, 0.0, 1.0, 81.0414657593), (0.0, 0.0, 0.0, 1.0)), 
        "2": ((0.569607973099, 0.821916520596, 0.0, 10.3826160431), (-0.821916520596, 0.569607973099, 0.0, 650.22277832), (0.0, 0.0, 1.0, 76.1073455811), (0.0, 0.0, 0.0, 1.0)), 
        "3": None, 
        "4": ((-0.0965752005577, 0.995325684547, 0.0, 2.53837513924), (-0.995325684547, -0.0965752005577, 0.0, 754.439575195), (0.0, 0.0, 1.0, 79.3089447021), (0.0, 0.0, 0.0, 1.0)), 
        "5": ((-0.57836407423, -0.815778672695, 0.0, -0.466578423977), (0.815778672695, -0.57836407423, 0.0, 722.526062012), (0.0, 0.0, 1.0, 102.935997009), (0.0, 0.0, 0.0, 1.0)), 
        "6": ((0.544339835644, -0.838864803314, 0.0, -611.133117676), (0.838864803314, 0.544339835644, 0.0, -1087.43554688), (0.0, 0.0, 1.0, -50.0952033997), (0.0, 0.0, 0.0, 1.0)), 
        "7": ((0.371672362089, 0.928363978863, 0.0, 0.428003937006), (-0.928363978863, 0.371672362089, 0.0, 762.25378418), (0.0, 0.0, 1.0, 67.1000213623), (0.0, 0.0, 0.0, 1.0)), 
        "8": ((-0.110311843455, -0.993897020817, 0.0, -201.041244507), (0.993897020817, -0.110311843455, 0.0, -100.712028503), (0.0, 0.0, 1.0, 90.8599853516), (0.0, 0.0, 0.0, 1.0)), 
        "9": ((-0.848161041737, -0.529738605022, 0.0, -195.748031616), (0.529738605022, -0.848161041737, 0.0, -255.898422241), (0.0, 0.0, 1.0, 116.248588562), (0.0, 0.0, 0.0, 1.0)), 

        }
    #desactiver les zones de panique
    #DisablePanicLinks()
    
    mat = ptMatrix44()
    if n is None:
        avCentre = PtGetLocalAvatar()
        mat = avCentre.getLocalToWorld()

    else:
        mat.setData(ws[str(n)])
    
    if bCircle:
        Cercle(coef=2.0, h=10.0, avCentre=mat, bPhys=True)
    else:
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
def panic(bOn=True):
    PtConsoleNet("Avatar.Spawn.DontPanic" , True)

# =====================================================================
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
    
    # Debut gestion du spawn point
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
    # Fin gestion du spawn point
    
    ptNetLinkingMgr().linkPlayerToAge(ageLink, playerID)
    return ageUserDefinedName + " " + ageInstanceName

#
playerIdList = []

#
def SavePlayers():
    global playerIdList
    agePlayers = filter(lambda pl: not(pl.getPlayerID() in dicBot.keys()), PtGetPlayerList())
    agePlayers.append(PtGetLocalPlayer())
    playerIdList = map(lambda player: player.getPlayerID(), agePlayers)

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
    elif ageName == "gahreesen":
        age = ["Gahreesen", "Garrison", "42f261ba-b74e-45a3-afb8-0bda76f44b34", "Mir-o-Bot's", ""]
    elif ageName == "prison":
        age = ["Gahreesen", "Garrison", "42f261ba-b74e-45a3-afb8-0bda76f44b34", "Mir-o-Bot's", "LinkInPointPrison"]
    elif ageName == "veranda":
        age = ["Gahreesen", "Garrison", "42f261ba-b74e-45a3-afb8-0bda76f44b34", "Mir-o-Bot's", "PlayerStart"]

    #les autre joueurs dans mon age
    for player in PtGetPlayerList():
        #playerID = player.getPlayerID()
        LinkPlayerTo(age, playerID = player.getPlayerID(), spawnPointNumber = None)
    # link myself
    LinkPlayerTo(age, playerID = None, spawnPointNumber = None)

# Link all saved players in choosen age
def la(ageName):
    global playerIdList
    if ageName == "gira":
        age = ["Eder Gira", "Gira", "5b4678a9-73ab-4b45-9058-e710b45e4dbe", "Mir-o-Bot's", ""]
    elif ageName == "kemo":
        age = ["Eder Kemo", "Garden", "3a366b1e-9488-4c77-a278-a6375161ac92", "Mir-o-Bot's", ""]
    #"gira":["Eder Gira", "Gira", "5b4678a9-73ab-4b45-9058-e710b45e4dbe", "Mir-o-Bot's", "LinkInPointFromKemo"], 
    #"kemo":["Eder Kemo", "Garden", "3a366b1e-9488-4c77-a278-a6375161ac92", "Mir-o-Bot's", "Perf-SpawnPointKemo02"], 

    # Lier les joueurs connus dans l'age choisi
    for playerId in playerIdList:
        LinkPlayerTo(age, playerID=playerId, spawnPointNumber=None)


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

#
def ride(soName="bird1", t=60.0):
    #recuperer tous les joueurs
    playerList = PtGetPlayerList()
    playerList.append(PtGetLocalPlayer())
    for player in playerList:
        playerName = player.getPlayerName()
        Ride.Suivre(objet=soName, Avatar=playerName, duree=t)
    CercleV(coef=2.0, avCentre=None)

#
def AddPrp(pages=["kemoStorm"]):
    #global bCleftAdded
    for page in pages:
        PtConsoleNet("Nav.PageInNode {0}".format(pages) , 1)
    bCleftAdded = True

#
def DelPrp(pages=["kemoStorm"]):
    #global bCleftAdded
    for page in pages:
        PtConsoleNet("Nav.PageOutNode {0}".format(pages) , 1)
    bCleftAdded = False

#
def hide(bOn=False):
    #Platform.HideJalak()
    # Hide some objects
    names = ["Bamboo", "Dome", "Garden", "Pillar", "TreeTrunk", "Rain", "Water"]
    Platform.ShowObjectList("garden", names, bOn)
    # Disable physics for some objects
    names = ["TreeTrunk"]
    Platform.PhysObjectList("garden", names, bOn)

# platform(name="sun") platform(name="roof")
def platform(name="sun"):
    matPos = None
    if name == "roof":
        tupPos = ((-0.931317865849, -0.364206343889, 0.0, -77.659538269), (0.364206343889, -0.931317865849, 0.0, -178.524871826), (0.0, 0.0, 1.0, 159.332183838), (0.0, 0.0, 0.0, 1.0)) 
        matPos = ptMatrix44()
        matPos.setData(tupPos)
    elif name == "sun":
        tupPos = ((-0.624134302139, -0.78131711483, 0.0, -1188.0), (0.78131711483, -0.624134302139, 0.0, -1138.0), (0.0, 0.0, 1.0, 221.0), (0.0, 0.0, 0.0, 1.0))
        matPos = ptMatrix44()
        matPos.setData(tupPos)
    else:
        pass
    Platform.CreatePlatform(bShow=False, matAv=matPos)

#
# long platform(where=1)
def platform2(where=None):
    matPos = None
    if where is None or where not in range(1, 5):
        matPos = PtGetLocalAvatar().getLocalToWorld()
    else:
        #Ahnonay
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

#