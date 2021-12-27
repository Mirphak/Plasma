# -*- coding: utf-8 -*-

"""
* Ercana Tour V1 19/12/2015

* Ercana Tour V2 25/05/2017
    LARRY (EN) :
        Okay. What's the wish list for this one again...?

        * The harvester. 
        We want to move the wings down at some point when we talk about it. 
        I talk about the features on its top, 
        so it would be nice if we could get the tour guests up high enough to see it.

        We will want to cross the sinkhole and go see that pattern on the canyon wall 
        at the end of the second set of harvester tracks.

        In Path of the Shell, 
        the cave that holds the shell shaped glyph where you link 
        to the Bahro cave has the shape of the star fissure on the wall. 
        Is that available to page in so the guests can see it when I talk about it?

        When we get to the factory, I'd like to take the guests up to the buildings 
        with all the pipes on the left canyon wall so they can see them up close.

        * Inside the factory, 
        there is a transverse corridor just inside the hopper car track entrance. 
        That's another place I'd like to show them if possible, 
        since it's a hidden feature no one notices when the ride the hopper into the factory.

        We want to move the guests across the gap in the catwalk over the mixing tanks, 
        so that we don't have to have them all run through the drain tunnel and climb the ladder at the end. 
        I'd also like to cycle one of the tanks while we are outside to see the animations.

        In the oven control room, 
        we want to cycle the moon shaped platforms over the 
        elevating platform so that the guests can see the animation inside the room. 
        We can ride the elevator up and walk from there to the top of the dam.

        The ladder in the pellet baking room is safe enough, 
        but warping down to the pellet room instead of climbing down it would keep the guests together. 
        Would it be an unnecessary risk of crashing to warp them?

        After the tour ends, 
        we'll want to warp up to the top of the canyon walls and have an on-lake effect 
        to let them run around the lake beyond the dam if it's possible, along with 
        anything else your imaginations and the limitations allow you to do.

        That's about all I can think of or remember. 
        Any other suggestions?

    Larry (FR) :
        D'accord. Quelle est la liste de souhaits pour celle-ci encore ...?

        * La moissonneuse-batteuse.
        Nous voulons déplacer les ailes vers le bas à un moment où nous en parlons.
        Je parle des fonctionnalités sur son sommet, 
        alors il serait bien que nous puissions faire en sorte que les invités 
        soient suffisamment élevés pour le voir.

        Nous voudrons traverser le puit et aller voir ce modèle sur le mur du 
        canyon à la fin de la deuxième série de pistes de récolte.

        Dans Path of the Shell, 
        la grotte qui détient le glyphe en forme de coquille où vous reliez 
        à la grotte Bahro a la forme de la fissure étoile sur le mur.
        Est-ce disponible pour la page afin que les invités puissent le voir quand je en parle?

        Lorsque nous arrivons à l'usine, 
        j'aimerais attirer les invités dans les bâtiments avec tous les tuyaux 
        du mur du canyon gauche afin qu'ils puissent les voir de près.

        * À l'intérieur de l'usine, 
        il y a un couloir transversal juste à l'intérieur de l'entrée de la voie de la trémie.
        C'est un autre endroit où j'aimerais leur montrer si possible, 
        car c'est une caractéristique cachée que personne ne remarque quand on monte la trémie dans l'usine.

        Nous voulons déplacer les invités à travers l'espace dans le défilé sur les réservoirs de mélange, 
        de sorte que nous ne devons pas tous les traverser à travers le tunnel de drainage et grimper à l'échelle à la fin.
        J'aimerais également faire un cycle de l'un des chars pendant que nous sommes à l'extérieur pour voir les animations.

        Dans la salle de contrôle du four, 
        nous voulons faire du vélo les plates-formes en forme de lune sur la plate-forme 
        élévatrice afin que les invités puissent voir l'animation dans la pièce.
        Nous pouvons monter l'ascenseur et marcher de là vers le haut du barrage.

        L'échelle dans la salle de cuisson des pastilles est assez sûre, 
        mais la déformation jusqu'à la salle des pastilles au lieu de descendre elle permettrait aux invités ensemble.
        Est-ce que ce serait un risque inutile de s'écraser pour les déformer?

        Après la fin de la tournée, 
        nous voulons nous enrayer au sommet des parois du canyon et avoir un effet 
        sur le lac pour les laisser courir autour du lac au-delà du barrage si cela est possible, 
        avec tout ce que votre imagination et les limites permettent que vous fassiez.

        C'est à propos de tout ce que je peux penser ou me souvenir.
        D'autres suggestions?

    ***
    Devant la fissure : //sp3
    Rendre la fissure visible : !toggle Object03  0 1
"""

from Plasma import *
import math
import sdl

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
def panic():
    PtConsoleNet("Avatar.Spawn.DontPanic" , 1)

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
