# -*- coding: utf-8 -*-

"""
    Version 1 : 05/12/2015
    
    Version 2 : 31/07/2017
        *** Larry whishes ***
            Tour wish list:
            Gahreesen is, of course, chock full of glitches and choke points, so much of the work for Stone and Mirphak will be crowd control and warping. 
            We know that we'll have to avoid the elevator and the outside doors of Gahreesen II like the plague.

            === First week ===
                * Gahreesen I: 
                This is easy, up to a point. 
                Warp to the normal link-in room. We'll walk through the downstairs rooms normally. 
                Warp us up to the second floor next to the sniper's window and we'll walk around up there. 
                The power needs to be turned on for the doors to work.

                * Gahreesen III: 
                This is the outdoors part of the tour. 
                We'll need to warp up to the top of Gahreesen I to avoid the elevator both as a choke point and a source of glitches, 
                and that's been a difficult process in the past. 
                Hope it goes smoothly this time.

                * Once outside on the roof, 
                no further effects are needed until we go to the center spire; 
                I'd like to link there to avoid timing issues and people falling and panic linking if possible.

                * Exception #1: 
                if you can, being able to trigger the sound files of the monsters on demand would be nice. 
                In the sound effects, the files are called grsnCreature01_02.ogg, grsnCreature03_04.ogg, grsnCreature05_06.ogg, and grsnCreature07_08.ogg.

                * Exception #2: 
                Gahreesen II has retractable bridges that can be drawn in to prevent access when the fortresses are on alert. 
                When the Age was first opened by the DRC, the bridges were pulled in, preventing explorers from getting past the rock spire. 
                If you can, it would be great if you could have the bridges pulled in when we first go up to the top of Gahreesen I, and then extend them on demand. 
                If you can't, that's okay, but it's something we've never done before.

            === Second Week ===
                * Gahreesen II: 
                This is another place where we want to avoid jumping across the gap and dealing with the one-person only doors. 
                Linking to the conference room directly would be okay; we can backtrack to a mud room from there.

                * In the prison, 
                it would be nice if we can avoid wasting time searching for the two sets of bones in the outer ring corridor. 
                If you can set coordinate markers to warp us directly to both the alien and human bones, that would save us a lot of time. 
                It would also be better if we can avoid the ladders and warp to the middle-level corridor outside the control room, and then warp up to the top level. 
                While the ladders to both places are safe enough, we waste time hunting for the ladder from the prison corridors and then waiting for everyone to climb up. 
                The more time we save getting people to the next lecture locations, the more time we can save actually giving the lecture.

                * The Wall: 
                Bitter experience has shown time and again that no matter how much we say 
                "stay off the wall and don't touch the glowing buttons over under the window", someone always does what they should not. 
                If you can disable the linking buttons and place a barrier of some kind to keep them off the wall catwalks, that would be a blessing. 
                Otherwise, we'll probably end up crashing at some point during the lecture. 
                I don't know if there are any effects built into the chamber you can activate, but if there aren't any, so be it.

                * The Maintainer's Nexus: 
                This is another area we've had problems with in the past. 
                The link into the Nexus takes you to a sunken pit where an elevator raises you into the main part of the room. 
                That pit and elevator don't like crowds and tend to glitch. 
                If you can get us into the room while avoiding it, it would help avoid a frustrating experience for all of us. 
                The linking book machine there also tends to be quirky, but I have no ideas about how to deal with that.
            ===
            I'm not sure what to do about the after-tour playtime in either session. 
            In Gahreesen III, if we can set up a surface for an on-lake effect and let them explore the model around the towers, that would work. 
            But I seem to recall you both saying that you couldn't. 
            And the second week, I have no ideas at all. 
            Does anyone else?     
"""

from Plasma import *
import math

"""
            pages += ["grsnWellOccluders","grsnWellSecondFloorRooms","grsnWellSecondFloorGearRoom","grsnElevator","grsnExterior"]
            pages += ["grsnVeranda","grsnVerandaExterior","grsnObsRoom01Imager","grsnObsRoom02Imager","grsnPrison","grsnPrisonTunnels"]
            pages += ["grsnTeamRoom01","grsnTeamRoom02","grsnTrainingCenterHalls","grsnTrainingCenterMudRooms","grsnTrainingCntrLinkRm"]
            pages += ["TrnCtrControlRoom01","TrnCtrControlRoom02","trainingCenterObservationRooms","NexusBlackRoom","NexusWhiteRoom"]
            pages += ["WallRoom","grsnWallRoomClimbingPhys"]
            pages += ["FemaleElevatorArrivingBottom","FemaleElevatorArrivingTop","FemaleElevatorLeavingBottom","FemaleElevatorLeavingTop"]
            pages += ["FemaleLandingRoll","FemaleReadyIdle","FemaleReadyJump","FemaleTubeFall"]
            pages += ["FemaleWallClimbDismountDown","FemaleWallClimbDismountLeft","FemaleWallClimbDismountRight","FemaleWallClimbDismountUp"]
            pages += ["FemaleWallClimbDown","FemaleWallClimbFallOff","FemaleWallClimbIdle","FemaleWallClimbLeft"]
            pages += ["FemaleWallClimbMountDown","FemaleWallClimbMountLeft","FemaleWallClimbMountRight","FemaleWallClimbMountUp"]
            pages += ["FemaleWallClimbRelease","FemaleWallClimbRight","FemaleWallClimbUp"]
            pages += ["MaleElevatorArrivingBottom","MaleElevatorArrivingTop","MaleElevatorLeavingBottom","MaleElevatorLeavingTop"]
            pages += ["MaleLandingRoll","MaleReadyIdle","MaleReadyJump","MaleTubeFall"]
            pages += ["MaleWallClimbDismountDown","MaleWallClimbDismountLeft","MaleWallClimbDismountRight","MaleWallClimbDismountUp"]
            pages += ["MaleWallClimbDown","MaleWallClimbFallOff","MaleWallClimbIdle","MaleWallClimbLeft"]
            pages += ["MaleWallClimbMountDown","MaleWallClimbMountLeft","MaleWallClimbMountRight","MaleWallClimbMountUp"]
            pages += ["MaleWallClimbRelease","MaleWallClimbRight","MaleWallClimbUp"]
"""

"""
#
def Play(player, animName, nbTimes):
    try :
        repet = int(nbTimes)
    except ValueError:
        repet = 0
    objKey = PtGetAvatarKeyFromClientID(player.getPlayerID())
    avatar = objKey.getSceneObject().avatar
"""

"""
#
def warpall():
    
    subworld = PtFindSceneobject("WellSub", "Garrison")
    #upElevWarpPoint = PtFindSceneobject("UpElevatorWarpPoint", "Garrison")
    topWarpPoint = ptVector3(65, -422, 10088)
    for player in PtGetPlayerList():
        objKey = PtGetAvatarKeyFromClientID(player.getPlayerID())
        soavatar = objKey.getSceneObject()
        soavatar.avatar.enterSubWorld(subworld)
        #soavatar.physics.warpObj(upElevWarpPoint.getKey())
        soavatar.physics.warp(topWarpPoint)
    soavatar = PtGetLocalAvatar()
    soavatar.avatar.enterSubWorld(subworld)
    #soavatar.physics.warpObj(upElevWarpPoint.getKey())
    soavatar.physics.warp(topWarpPoint)
"""

"""
#
def LinkAll():
    age = ["Ahnonay", "Ahnonay", "55ce4207-aba9-4f2e-80de-7980a75ac3f2", "Mir-o-Bot", ""]
    #les autre joueurs dans mon age
    for player in PtGetPlayerList():
        #playerID = player.getPlayerID()
        LinkPlayerTo(age, playerID = player.getPlayerID(), spawnPointNumber = None)
    # link myself
    LinkPlayerTo(age, playerID = None, spawnPointNumber = None)
"""

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
    """
    for i in range(n):
        player = agePlayers[i]
        avatar = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
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
        avatar.physics.enable(bPhys)
        avatar.physics.warp(matrix * mRot)
    """
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
        #reactiver la physique pour tous
        #if n != 8:
        soavatar.netForce(1)
        soavatar.physics.enable(bPhys)


"""    Pour aller sur le toit de la 1ere tour: wa(3) + wa(8) + wa(9)
    "0": Point d'arrivee dans l'age
    "1": Salle scarabee 2e etage
    #"2": Devant ascenseur montant
    "2": Salle des machines
    "3": Exterieur, ile centrale
    "4": Interieur, entree tour entrainement
    "5": Cellule prison
    "6": Salle du mur
    "7": Nexus mur
    "8": Intermediaire pour monter sur le toit
    "9": Toit exterieur
    "10": Cellule Prison
    "11": Sous cellule prison
    "12": Prison, squelette 1
    "13": Prison, squelette 2
    "14": Prison echelle bas
    "15": Prison echelle inter
    "16": Prison centre salle echelles bas
    "17": Veranda centre echelles haut
"""
def wa(n=0, bCircle=False):
    # les points de warp
    ws = { 
        #"0": ((0.986239790916, 0.165321528912, 0.0, 92.0742950439), (-0.165321528912, 0.986239790916, 0.0, -421.575561523), (0.0, 0.0, 1.0, 10087.4404297), (0.0, 0.0, 0.0, 1.0)), 
        "0": ((0.999802947044, -0.0198498461396, 0.0, 76.9855041504), (0.0198498461396, 0.999802947044, 0.0, -486.937957764), (0.0, 0.0, 1.0, -278.870513916), (0.0, 0.0, 0.0, 1.0)), 
        "1": ((-0.99768871069, 0.0679508671165, 0.0, 95.7189483643), (-0.0679508671165, -0.99768871069, 0.0, -449.018035889), (0.0, 0.0, 1.0, -250.387756348), (0.0, 0.0, 0.0, 1.0)), 
        #"2": ((-0.794308185577, 0.607515096664, 0.0, 31.8062763214), (-0.607515096664, -0.794308185577, 0.0, -426.600250244), (0.0, 0.0, 1.0, -279.017913818), (0.0, 0.0, 0.0, 1.0)), 
        "2": ((-0.802598953247, -0.596519052982, 0.0, 23.788734436), (0.596519052982, -0.802598953247, 0.0, -508.485046387), (0.0, 0.0, 1.0, -250.534179688), (0.0, 0.0, 0.0, 1.0)), 
        "3": ((0.985827445984, -0.167762547731, 0.0, 73.2108154297), (0.167762547731, 0.985827445984, 0.0, -267.512207031), (0.0, 0.0, 1.0, 10085.6845703), (0.0, 0.0, 0.0, 1.0)), 
        "4": ((0.451631933451, 0.892204344273, 0.0, 211.293777466), (-0.892204344273, 0.451631933451, 0.0, 297.770355225), (0.0, 0.0, 1.0, -9.74115753174), (0.0, 0.0, 0.0, 1.0)), 
        "5": ((-0.997065663338, -0.0765519589186, 0.0, 72.6664428711), (0.0765519589186, -0.997065663338, 0.0, 439.641204834), (0.0, 0.0, 1.0, 965.71081543), (0.0, 0.0, 0.0, 1.0)), 
        "6": ((-0.490352004766, 0.871524512768, 0.0, 0.0407438091934), (-0.871524512768, -0.490352004766, 0.0, 134.997406006), (0.0, 0.0, 1.0, -30.0120010376), (0.0, 0.0, 0.0, 1.0)), 
        "7": ((-0.0984519198537, 0.995141744614, 0.0, -376.244354248), (-0.995141744614, -0.0984519198537, -0.0, -6.76931190491), (-0.0, 0.0, 1.0, -0.022900916636), (0.0, 0.0, 0.0, 1.0)), 
        "8": ((-0.999864518642, 0.0164644680917, 0.0, 76.7055206299), (-0.0164644680917, -0.999864518642, 0.0, -289.055328369), (0.0, 0.0, 1.0, 10086.1855469), (0.0, 0.0, 0.0, 1.0)), 
        "9": ((-0.951500952244, -0.307654172182, 0.0, 33.7776107788), (0.307654172182, -0.951500952244, 0.0, -458.413269043), (0.0, 0.0, 1.0, 10087.4404297), (0.0, 0.0, 0.0, 1.0)), 
        "10": ((-1.34358856485e-07, -1.00000011921, 0.0, 72.1411972046), (1.00000011921, -1.34358856485e-07, 0.0, 443.795959473), (0.0, 0.0, 1.0, 965.71081543), (0.0, 0.0, 0.0, 1.0)), 
        "11": ((-0.695429027081, -0.718594908714, 0.0, 74.3801956177), (0.718594908714, -0.695429027081, 0.0, 448.348876953), (0.0, 0.0, 1.0, 955.553771973), (0.0, 0.0, 0.0, 1.0)), 
        "12": ((-0.783920109272, 0.620861828327, 0.0, -6.6934876442), (-0.620861828327, -0.783920109272, 0.0, 490.109649658), (0.0, 0.0, 1.0, 955.553710938), (0.0, 0.0, 0.0, 1.0)), 
        "13": ((-0.883565783501, -0.468307256699, 0.0, 151.240356445), (0.468307256699, -0.883565783501, 0.0, 497.088775635), (0.0, 0.0, 1.0, 955.553710938), (0.0, 0.0, 0.0, 1.0)), 
        "14": ((0.541787862778, 0.840515255928, 0.0, 114.343582153), (-0.840515255928, 0.541787862778, 0.0, 559.231994629), (0.0, 0.0, 1.0, 955.553710938), (0.0, 0.0, 0.0, 1.0)), 
        "15": ((-0.886784672737, 0.462182939053, 0.0, 119.639907837), (-0.462182939053, -0.886784672737, 0.0, 549.495178223), (0.0, 0.0, 1.0, 965.579162598), (0.0, 0.0, 0.0, 1.0)), 
        "16": ((0.999342978001, -0.0362437516451, 0.0, 71.1204833984), (0.0362437516451, 0.999342978001, 0.0, 530.367980957), (0.0, 0.0, 1.0, 965.72277832), (0.0, 0.0, 0.0, 1.0)), 
        "17": ((0.999342978001, -0.0362437516451, 0.0, 71.1204833984), (0.0362437516451, 0.999342978001, 0.0, 530.367980957), (0.0, 0.0, 1.0, 993.55480957), (0.0, 0.0, 0.0, 1.0)), 
        }
    #desactiver les zones de panique
    #DisablePanicLinks()
    
    mat = ptMatrix44()
    mat.setData(ws[str(n)])
    
    if bCircle:
        Cercle(coef=2.0, h=10.0, avCentre=mat, bPhys=True)
    else:
        #recuperer tous les joueurs
        playerList = PtGetPlayerList()
        playerList.append(PtGetLocalPlayer())
        """
        for player in playerList:
            objKey = PtGetAvatarKeyFromClientID(player.getPlayerID())
            soavatar = objKey.getSceneObject()
            
            #faire flotter tout le monde
            soavatar.physics.enable(0)
            soavatar.netForce(1)
            
            #deplacer les gens
            soavatar.physics.warp(mat)
            soavatar.netForce(1)
            
            #reactiver la physique pour tous
            if n != 8:
                soavatar.physics.enable(1)
                soavatar.netForce(1)
        """
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
            if n != 8:
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
    sol = FindSOLike("anic")
    for so in sol:
        so.netForce(1)
        so.physics.disable()

#
def panic():
    PtConsoleNet("Avatar.Spawn.DontPanic" , 1)

#
def RemoveLadder():
    ''' Stop people from climbing the ladder. '''
    for i in range(1, 3):
        p = PtFindSceneobject('LadderUpOn POS%02d' % i, 'Garrison').physics
        p.netForce(1)
        p.enable(0)

#
def AddPrp():
    ''' Add Gahreesen Wall pages '''
    #global bWallAdded
    pages = ["WallRoom","grsnWallRoomClimbingPhys"]
    for page in pages:
        PtConsoleNet("Nav.PageInNode %s" % (page) , 1)
    #bWallAdded = True

#
def nowall():
    ''' Unload Gahreesen Wall climbing pages '''
    #global bWallAdded
    pages = []
    pages += ["FemaleWallClimbDismountDown","FemaleWallClimbDismountLeft","FemaleWallClimbDismountRight","FemaleWallClimbDismountUp"]
    pages += ["FemaleWallClimbDown","FemaleWallClimbFallOff","FemaleWallClimbIdle","FemaleWallClimbLeft"]
    pages += ["FemaleWallClimbMountDown","FemaleWallClimbMountLeft","FemaleWallClimbMountRight","FemaleWallClimbMountUp"]
    pages += ["FemaleWallClimbRelease","FemaleWallClimbRight","FemaleWallClimbUp"]
    pages += ["MaleWallClimbDismountDown","MaleWallClimbDismountLeft","MaleWallClimbDismountRight","MaleWallClimbDismountUp"]
    pages += ["MaleWallClimbDown","MaleWallClimbFallOff","MaleWallClimbIdle","MaleWallClimbLeft"]
    pages += ["MaleWallClimbMountDown","MaleWallClimbMountLeft","MaleWallClimbMountRight","MaleWallClimbMountUp"]
    pages += ["MaleWallClimbRelease","MaleWallClimbRight","MaleWallClimbUp"]
    for page in pages:
        PtConsoleNet("Nav.PageOutNode %s" % (page) , 1)
    #bWallAdded = False

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
    if ageName == "spy":
        age = ["spyroom", "spyroom", "df9d49ec-0b9c-4716-9a0f-a1b66f7d9814", "mob's (Sharper's spy room)", ""]
    elif ageName == "gahreesen":
        age = ["Gahreesen", "Garrison", "42f261ba-b74e-45a3-afb8-0bda76f44b34", "Mir-o-Bot's", ""]
    elif ageName == "prison":
        age = ["Gahreesen", "Garrison", "42f261ba-b74e-45a3-afb8-0bda76f44b34", "Mir-o-Bot's", "LinkInPointPrison"]
    elif ageName == "veranda":
        age = ["Gahreesen", "Garrison", "42f261ba-b74e-45a3-afb8-0bda76f44b34", "Mir-o-Bot's", "PlayerStart"]

    # Lier les joueurs connus dans l'age choisi
    for playerId in playerIdList:
        LinkPlayerTo(age, playerID=playerId, spawnPointNumber=None)
