# -*- coding: utf-8 -*-

from Plasma import *
from PlasmaKITypes import *

import math
import datetime
import re

from . import xPlayers
from . import xBotAge
from . import xAnim
from . import xSave
from . import xSave2
from . import xJalak

from . import CloneObject
from . import CloneObjects
from . import sdl
from . import Columns2

#Ages de Mirphak, Mir-o-Bot, MagicBot, ages publics
from . import ages

# With old client
#import MarkerGames
# With new client
from . import MarkerGames2
from . import Ride
from . import Ahnonay

from . import CloneBugs
from . import DropObjects
from . import ReltoNight
from . import ReltoNight2
from . import xCleft
from . import xDelin
from . import xHood
from . import xRelto
from . import xScore
from . import xTsogal

from . import Dance
from . import clothing

from . import AnimationList

from . import Pellet
from . import Light

import xFireCamp

#----------------------------------------------------------------------------#
#   Attributs globaux
#----------------------------------------------------------------------------#
debugInfo = ""
bJalakAdded = False
bBlockCmds = False
# My avatars
adminList = [32319, 31420, 2332508]  # Mir-o-Bot, Mirphak, mob
# For the dance events
adminList += [
    11243,   # Luluberlu
    11896,   # MagicYoda
    115763,  # Willy
    #119426,  # Edith
    127131,  # tsuno
    #133403,  # sendlinger
    137998,  # Mabe
    254640,  # Eternal Seeker
    254930, # Kamikatze
    #966183, # y e e s h a
    #2975513, # Didi
    #1261291, # Y E E R K
    1474572, # Fog_man
    5667000, # Minasunda
    #5710565, # Salirama
    #6362551, # vony
    6495949, # Lu*
    6551797, # ondine
    #6559861, # Kawliga
    #6583813, # Roland (Mav Hungary)
    #6670690, # Billy the Cat
    #6682907, # LaDeeDah
    #6725908, # Raymondo
    #6833983, # malcg
    6961947, # Calisia (= Terry L. Britton)
    7060111, # Aeonihya
    7132841, # Mina Sunda
    #7172637, # Baeda
    #7227499, # Lidia (Mav Hungary)
    #7327507, # artopia
    #7517653, # ladylora
    #7731330, # My.St'ro
    #7796072, # Klaide
    #7881034, # Yakoso
    7939982, # Claidi Song
    #7965725, # Z A N D l
    8068100, # NDG Eternal Seeker
    #8315178, # Roland (Mav Hungary)
	9292763, # MinBot
    #9843955, # CatYoh
    9995228, # NDGSeeker
    #10287894, # Thallan
    #10360615, # Thallane
    11884030, # Patsy
    12348922, # ben2
    #12480587, # Tituss
]

# For the Cavern Tours : Larry Ledeay and CT Hostess Susa'n
#adminList += [11308, 9122427]

# liste des instances disponibles pour moi
#linkDic = xBotKiCmds.linkDic

# Authorized age instances
allowedAgeInstanceGuids = {
}

#lastLinkTime = datetime.datetime.now()
lastLinkTime = datetime.datetime.now(datetime.timezone.utc)

#----------------------------------------------------------------------------#
#   Methodes
#----------------------------------------------------------------------------#

## Usage interne

### Display a message to the player (or players).
def SendChatMessage(self, fromPlayer, plyrList, message, flags):
    plyrNameList = [pl.getPlayerName() for pl in plyrList]
    plyrList = [pl for pl in plyrList if pl.getPlayerID() != PtGetLocalPlayer().getPlayerID()]
    if message is None:
        message = "Oops, I forgot what I had to tell you!"
    
    if len(plyrList) > 0:
        # Don't take care of flags nor bots, always send message as buddies inter-age
        PtSendRTChat(fromPlayer, plyrList, message, 24)
    PtSendKIMessage(kKILocalChatStatusMsg, "sent to [" + ",".join(plyrNameList) + "] : " + message)

#Pour savoir si le joueur est dans l'age du robot
def isPlayerInAge(player):
    #PtSendKIMessage(kKILocalChatStatusMsg, "> isPlayerInAge")
    if player.getPlayerID() == PtGetLocalPlayer().getPlayerID():
        return True
    agePlayers = PtGetPlayerList()
    ids = [player.getPlayerID() for player in agePlayers]
    try:
        if player.getPlayerID() in ids:
            return True
        else:
            return False
    except:
        return False

#Recherche d'un avatar par son nom 
#une partie du nom suffit, on peut mettre des * pour remplacer des bouts
def SearchAvatarNameLike(name):
    #PtSendKIMessage(kKILocalChatStatusMsg, "> SearchAvatarNameLike")
    #cond = r"[^a-z1-9*]"
    cond = r"[^?a-z1-9*_\\]"
    name = name.lower().replace("\\", "\\\\").replace("?", "\?")
    pat = re.sub(cond, ".", name)
    pat = pat.replace("*", ".*")
    #pat = pat.replace("?", "\?")
    pat = "^" + pat + ".*$"
    pattern = re.compile(pat)
    agePlayers = PtGetPlayerList()
    agePlayers.append(PtGetLocalPlayer())
    players = [player for player in agePlayers if pattern.match(player.getPlayerName().lower())]
    if len(players) == 0:
        players = [player for player in agePlayers if player.getPlayerName().lower().replace(" ", "") == name.replace(" ", "")]
    return players


def GetAgePlayerByName(name):
    #PtSendKIMessage(kKILocalChatStatusMsg, "> GetAgePlayerByName")
    players = SearchAvatarNameLike(name)
    if len(players) > 0:
        return players[0]
    else:
        return None


##Les methodes suivantes peuvent etre appelees par un autre joueur

# voir dans xBotAge, la methode LinkPlayerToPublic
def LinkToPublicAge(self, cFlags, args = []):
    #PtSendKIMessage(kKILocalChatStatusMsg, "> LinkToPublicAge")
    if len(args) < 2:
        return 0
    linkName = args[1].lower().replace(" ", "").replace("'", "").replace("eder", "")
    myself = PtGetLocalPlayer()
    player = args[0]
    playerID = player.getPlayerID()
    instanceName = xBotAge.LinkPlayerToPublic(self, linkName, playerID)
    if instanceName:
        #msg = "Have fun in " + instanceName + " :)"
        pass
    else:
        msg = "I don't know where '" + args[1] + "' is!"
        SendChatMessage(self, myself, [player], msg, cFlags.flags)
    #SendChatMessage(self, myself, [player], msg, cFlags.flags)
    return 1

# Links the player to the current bot age
def LinkHere(self, cFlags, args = []):
    #PtSendKIMessage(kKILocalChatStatusMsg, "> LinkHere ")
    if len(args) < 1:
        PtSendKIMessage(kKILocalChatStatusMsg, "> LinkHere: len(args) = " + str(len(args)))
        return 0
    elif len(args) > 1:
        LinkToPublicAge(self, cFlags, args)
        return 1
    player = args[0]
    myself = PtGetLocalPlayer()
    #botAgeName = xBotAge.GetPlayerAgeInstanceName()
    #xBotAge.currentBotAge = xBotAge.GetBotAge()
    if len(xBotAge.currentBotAge) < 3:
        xBotAge.currentBotAge = xBotAge.GetBotAge()
    botAgeName = xBotAge.currentBotAge[3] + " " + xBotAge.currentBotAge[0]
    if isPlayerInAge(player):
        SendChatMessage(self, myself, [player], "You are already in " + botAgeName, cFlags.flags)
    else:
        #if len(xBotAge.currentBotAge) < 3:
        #    xBotAge.currentBotAge = xBotAge.GetBotAge()
        #xBotAge.currentBotAge = xBotAge.GetBotAge()
        PtSendKIMessage(kKILocalChatStatusMsg, ", ".join(xBotAge.currentBotAge))
        xBotAge.LinkPlayerTo(self, xBotAge.currentBotAge, player.getPlayerID())
        SendChatMessage(self, myself, [player], "Welcome to " + botAgeName, cFlags.flags)
    return 1

def WarpToMe(self, cFlags, player):
    #PtSendKIMessage(kKILocalChatStatusMsg, "> WarpToMe")
    myself = PtGetLocalPlayer()
    if type(player) == list and len(player) > 0:
        if isPlayerInAge(player[0]):
            av = PtGetAvatarKeyFromClientID(player[0].getPlayerID()).getSceneObject()
            so = PtGetLocalAvatar()
            pos = so.getLocalToWorld()
            av.netForce(1)
            av.physics.warp(pos)
            """ JE LE DESACTIVE POUR L'INSTANT (pendant les tests de CreateReltoNight1)
            # do special stuff in some ages
            if len(xBotAge.currentBotAge) > 3:
                # in Mir-o-Bot's Relto
                if xBotAge.currentBotAge[1] == "Personal" and xBotAge.currentBotAge[3] == "Mir-o-Bot's":
                    #xRelto.SetFog(style = "nofog")
                    xRelto.EnableAll(False)
            """
        else:
            SendChatMessage(self, myself, [player[0]], "You must be in my age, use link to join me." , cFlags.flags)
        return 1
    else:
        return 0

#
def WarpToPlayer(self, cFlags, player, toPlayer):
    #PtSendKIMessage(kKILocalChatStatusMsg, "> WarpToPlayer")
    myself = PtGetLocalPlayer()
    if isPlayerInAge(player):
        av = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
        so = PtGetAvatarKeyFromClientID(toPlayer.getPlayerID()).getSceneObject()
        pos = so.getLocalToWorld()
        av.netForce(1)
        av.physics.warp(pos)
    else:
        #SendChatMessage(self, myself, [player[0]], "You must be in my age, use link to join me." , cFlags.flags)
        SendChatMessage(self, myself, [player], "You must be in my age, use link to join me." , cFlags.flags)
    return 1

def WarpToDefaultLinkInPoint(self, cFlags, player):
    #PtSendKIMessage(kKILocalChatStatusMsg, "> WarpToDefaultLinkInPoint")
    myself = PtGetLocalPlayer()
    if type(player) == list and len(player) > 0:
        if isPlayerInAge(player[0]):
            av = PtGetAvatarKeyFromClientID(player[0].getPlayerID()).getSceneObject()
            try:
                so = PtFindSceneobject('LinkInPointDefault',PtGetAgeName())
                pos = so.getLocalToWorld()
                av.netForce(1)
                av.physics.warp(pos)
            except:
                SendChatMessage(self, myself, [player[0]], "Sorry I did not find the default linking point." , cFlags.flags)
        else:
            SendChatMessage(self, myself, [player[0]], "You must be in my age, use link to join me." , cFlags.flags)
        return 1
    else:
        return 0

def WarpToSpawnPoint(self, cFlags, args = []):
    #PtSendKIMessage(kKILocalChatStatusMsg, "> WarpToSpawnPoint")
    if len(args) < 2:
        return 0
    myself = PtGetLocalPlayer()
    player = args[0]
    try:
        spawnPointNumber = int(args[1])
        spawnPointAlias = None
    except:
        spawnPointNumber = None
        spawnPointAlias = args[1]
    
    if not isPlayerInAge(player):
        SendChatMessage(self, myself, [player], "You must be in my age, use link to join me." , cFlags.flags)
        return 1
    if spawnPointNumber is not None:
        pos = xBotAge.GetSPCoord(spawnPointNumber)
        if isinstance(pos, ptMatrix44):
            spName = xBotAge.GetSPName(spawnPointNumber)
            SendChatMessage(self, myself, [player], spName, cFlags.flags)
            #PtSendKIMessage(kKILocalChatStatusMsg, "> " + spName)
        else:
            SendChatMessage(self, myself, [player], "Unknown spawn point!" , cFlags.flags)
    elif spawnPointAlias is not None:
        pos = xBotAge.GetSPByAlias(spawnPointAlias)[0]
        spName = xBotAge.GetSPByAlias(spawnPointAlias)[1]
        SendChatMessage(self, myself, [player], spName, cFlags.flags)
        #PtSendKIMessage(kKILocalChatStatusMsg, "> " + spName)
    else:
        return 0
    if isinstance(pos, ptMatrix44):
        soAvatar = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
        soAvatar.netForce(1)
        soAvatar.physics.warp(pos)
    return 1

def FindSceneObjectPosition(self, name):
    #PtSendKIMessage(kKILocalChatStatusMsg, "> FindSceneObjectPosition")
    o = list(name + "not found!")
    so = xBotAge.GetFirstSoWithCoord(name)
    if so:
        pos = so.position()
        o = list(so.getName(), pos.getX(), pos.getY(),  pos.getZ())
    return o

#def FindClonePosition(self, name):
#    PtSendKIMessage(kKILocalChatStatusMsg, "> FindClonePosition")
#    o = list(name + "not found!")
#    so = xBotAge.GetFirstClonePosition(name)
#    if so:
#        pos = so.position()
#        o = list(so.getName(), pos.getX(), pos.getY(),  pos.getZ())
#    return o

def ShowSceneObjects(self, cFlags, args = []):
    #PtSendKIMessage(kKILocalChatStatusMsg, "> ShowSceneObjects")
    if len(args) < 2:
        return 0
    myself = PtGetLocalPlayer()
    player = args[0]
    
    if not isPlayerInAge(player):
        SendChatMessage(self, myself, [player], "You must be in my age, use link to join me." , cFlags.flags)
    else:
        name = args[1]
        msg = xBotAge.ShowSOWithCoords(name)
        SendChatMessage(self, myself, [player], msg, cFlags.flags)
    return 1

#
def Red(player):
    #PtSendKIMessage(kKILocalChatStatusMsg, "> Red")
    if type(player) == list and len(player) > 0:
        av = PtGetAvatarKeyFromClientID(player[0].getPlayerID()).getSceneObject()
        av.avatar.netForce(1)
        av.avatar.tintSkin(ptColor().red())
        return 1
    else:
        return 0

#
def SkinColor(self, cFlags, args = []):
    #PtSendKIMessage(kKILocalChatStatusMsg, "> SkinColor player r g b")
    if len(args) < 2:
        #PtSendKIMessage(kKILocalChatStatusMsg, "> SkinColor len(args) = {}".format(len(args)))
        msg = "skin needs 3 parameters, none given."
        PtSendKIMessage(kKILocalChatStatusMsg, msg)
        #PtSendRTChat(myself, [player], msg, cFlags.flags)
        return 0
    myself = PtGetLocalPlayer()
    player = args[0]
    colors = args[1].split()
    if len(colors) != 3:
        msg = "skin needs 3 parameters, {} given.".format(len(colors))
        PtSendKIMessage(kKILocalChatStatusMsg, msg)
        SendChatMessage(self, myself, [player], msg, cFlags.flags)
        return 1
    try:
        r = float(colors[0].strip().lower())
        g = float(colors[1].strip().lower())
        b = float(colors[2].strip().lower())
    except:
        PtSendKIMessage(kKILocalChatStatusMsg, "> r, g and b must be floating points numbers between 0 and 1")
        return 1
    
    if isPlayerInAge(player):
        av = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
        av.avatar.netForce(1)
        av.avatar.tintSkin(ptColor(r, g, b))
        msg = "You have a new skin color :)"
        SendChatMessage(self, myself, [player], msg, cFlags.flags)
        return 1
    else:
        SendChatMessage(self, myself, [player], "You must be in my age, use link to join me." , cFlags.flags)
    return 1

#Bugs
#bugs = PtFindSceneobject("BugFlockingEmitTest", "Garden")
# add prp : "ItinerantBugCloud"
pageBugs = "ItinerantBugCloud"
def AddPrp(page=pageBugs):
    PtConsoleNet("Nav.PageInNode %s" % (page) , 1)
def DelPrp(page=pageBugs):
    PtConsoleNet("Nav.PageOutNode %s" % (page) , 1)
def DelPrpLocal(page=pageBugs):
    PtPageOutNode(page)

##NE FONCTIONNE PAS...
#def Bugs(self, args = []):
#    global bugs
#    PtSendKIMessage(kKILocalChatStatusMsg, "> Bugs")
#    if len(args) < 2:
#        return 0
#    myself = PtGetLocalPlayer()
#    player = args[0]
#    onOff = args[1].strip().lower()
#    av = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
#    #av = PtGetLocalAvatar()
#    #bugs = PtFindSceneobject("BugFlockingEmitTest", "Garden")
#    msg = player.getPlayerName()
#    if onOff == "on":
#        bugs.draw.netForce(1)
#        PtTransferParticlesToObject(bugs.getKey(),av.getKey(),100)
#        msg += " calls bugs."
#    else:
#        PtKillParticles(0,1,av.getKey())
#        msg += " has killed bugs."
#    #PtSendRTChat(myself, [player], msg, 24)
"""
#
def Bugs(self, args = []):
    #global bugs
    PtSendKIMessage(kKILocalChatStatusMsg, "> Bugs")
    if len(args) < 2:
        return 0
    myself = PtGetLocalPlayer()
    player = args[0]
    onOff = args[1].strip().lower()
    av = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
    avPos = av.getLocalToWorld()
    AddPrp(pageBugs)
    bugs = PtFindSceneobject("BugFlockingEmitTest", "Garden")
    #bugsPos = bugs.getLocalToWorld()
    bugs.draw.netForce(1)
    msg = player.getPlayerName()
    if onOff == "on":
        PtTransferParticlesToObject(bugs.getKey(),av.getKey(),100)
        bugs.draw.enable(1)
        msg += " calls bugs."
    else:
        PtKillParticles(0,1,av.getKey())
        #msg += " has killed bugs."
        bugs.draw.enable(0)
        msg += " releases bugs."
    SendChatMessage(self, myself, [player], msg, 24)
"""
#
def Bugs(self, cFlags, args = []):
    #global bugs
    #PtSendKIMessage(kKILocalChatStatusMsg, "> Bugs")
    if len(args) < 2:
        return 0
    myself = PtGetLocalPlayer()
    player = args[0]
    onOff = args[1].strip().lower()
    
    if not isPlayerInAge(player):
        SendChatMessage(self, myself, [player], "You must be in my age, use link to join me." , cFlags.flags)
        return 1

    # /!\ ca plante a payiferen => desactiver la commande si je suis la-bas!!!
    currentAgeInfo = PtGetAgeInfo()
    if currentAgeInfo.getAgeFilename() == "Payiferen":
        SendChatMessage(self, myself, [player], "Sorry, the 'bugs' command is disabled in {0}.".format(currentAgeInfo.getAgeInstanceName()) , cFlags.flags)
        return 1
    
    try:
        av = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
    except (AttributeError):
        if player is None:
            PtSendKIMessage(kKILocalChatStatusMsg, "> Bugs: player is None!!")
        elif isinstance(player, ptPlayer):
            PtSendKIMessage(kKILocalChatStatusMsg, "> Bugs: player {0} ({1}) has no sceneobject attribute!".format(player.getPlayerName(), player.getPlayerID()))
        else:
            PtSendKIMessage(kKILocalChatStatusMsg, "> Bugs: player is not None nor a ptPlayer!!")
        return 1
    avPos = av.getLocalToWorld()
    #AddPrp(pageBugs)
    #bugs = PtFindSceneobject("BugFlockingEmitTest", "Garden")
    #bugsPos = bugs.getLocalToWorld()
    #bugs.draw.netForce(1)
    
    msg = player.getPlayerName()
    if onOff == "on":
        #PtTransferParticlesToObject(bugs.getKey(),av.getKey(),100)
        #bugs.draw.enable(1)
    
        CloneBugs.Bugs(bOn=True, position=avPos, bTie=True, soPlayer=av)
        
        msg += " calls bugs."
    else:
        #PtKillParticles(0,1,av.getKey())
        ##msg += " has killed bugs."
        #bugs.draw.enable(0)
    
        CloneBugs.Bugs(bOn=False, position=avPos, bTie=False, soPlayer=av)
        
        msg += " releases bugs."
    SendChatMessage(self, myself, [player], msg, 24)
    return 1

def GetPeople(kind = "buddy", listedPlayers = []):
    #PtSendKIMessage(kKILocalChatStatusMsg, "> GetPeople")
    selPlyrList = []
    #agePlayers = PtGetPlayerList()
    vault = ptVault()
    people = None
    if kind == "buddy":
        people = vault.getBuddyListFolder()
    elif kind == "recent":
        people = vault.getPeopleIKnowAboutFolder()
    elif kind == "neighbor":
        try:
            people = vault.getLinkToMyNeighborhood().getAgeInfo().getAgeOwnersFolder()
        except:
            pass
    if type(people) != type(None):
        for bud in people.getChildNodeRefList():
            if isinstance(bud, ptVaultNodeRef):
                # then send to player that might be in another age
                ebud = bud.getChild()
                ebud = ebud.upcastToPlayerInfoNode()
                if type(ebud) != type(None):
                    if ebud.playerIsOnline():
                        player = ptPlayer(ebud.playerGetName(),ebud.playerGetID())
                        if player not in listedPlayers:
                            selPlyrList.append(player)
        selPlyrList = [pl for pl in selPlyrList if not(pl.getPlayerID() in list(xPlayers.dicBot.keys()))]
    return selPlyrList

#
def RemovePrpToLocal(self):
    global bJalakAdded
    PtSendKIMessage(kKILocalChatStatusMsg, "> RemovePrpToLocal")
    xCleft.DelPrpLocal()
    Columns2.DelPrpLocal()
    bJalakAdded = False
    #Platform.DelPrpLocal()
    #xBugs.DelPrpLocal()
    #xPub.DelPrpLocal()
    #xRelto.DelPrpLocal()
    #xSpy.DelPrpLocal()
    #ridePages = ["psnlMYSTII", "Desert", "clftSceneBahro", "tldnHarvest", "DrnoExterior", "kemoGarden", "Jungle", "Pod", "giraCanyon", "bahroFlyers_arch", "bahroFlyers_city1", "bahroFlyers_city2", "bahroFlyers_city3", "bahroFlyers_city4", "bahroFlyers_city5", "bahroFlyers_city6"]
    Ride.DelPrpLocal()

# link the robot to an age instance
#def LinkBotTo(player, linkName):
def LinkBotTo(self, cFlags, args = []):
    global lastLinkTime
    #PtSendKIMessage(kKILocalChatStatusMsg, "> LinkBotTo")
    #now = datetime.datetime.now()
    now = datetime.datetime.now(datetime.timezone.utc)
    minDiff = 1 * 60
    
    if len(args) < 2:
        return 0
    linkName = args[1].lower().replace(" ", "").replace("'", "").replace("eder", "")
    myself = PtGetLocalPlayer()
    player = args[0]
    msg = "Available links: "
    availableLinks = list()
    """
    # ages.linkDic et allowedAgeInstanceGuids sont vides
    # TODO : voir si je les remet
    for lk  in linkDic.keys():
        if linkDic[lk][2] in allowedAgeInstanceGuids.values():
            availableLinks.append(lk + " : " +linkDic[lk][0])
    msg += ", ".join(availableLinks)
    """
    for lk  in list(ages.MirobotAgeDict.keys()):
        availableLinks.append("{0} : {1} {2}".format(lk, ages.MirobotAgeDict[lk][3], ages.MirobotAgeDict[lk][0]))
    msg += ", ".join(availableLinks)
    
    link = None
    """
    # Is the age name in linkDic?
    if (linkName in linkDic.keys()):
        link = linkDic[linkName]
        if not(link[2] in allowedAgeInstanceGuids.values()):
            link = None
    # Trying Mir-o-Bot ages
    elif (linkName in ages.MirobotAgeDict.keys()):
    """
    
    if linkName == "ahnonay":
        msg = "Sorry, I can't go to Ahnonay. I'm crashing too often there!"
        SendChatMessage(self, myself, [player], msg, cFlags.flags)
        return 0
    
    """
    elif linkName == "mobelonin":
        msg = "Sorry, I can't go to Mob's Elonin."
        SendChatMessage(self, myself, [player], msg, cFlags.flags)
        return 0
    """
    #elif linkName == "pedia":
    if linkName == "pedia":
        msg = "Sorry, I can't go to Myspedia."
        SendChatMessage(self, myself, [player], msg, cFlags.flags)
        return 0
    elif linkName == "tjh":
        msg = "Sorry, I can't go to Tereeza's Hood."
        SendChatMessage(self, myself, [player], msg, cFlags.flags)
        return 0
    # Trying Mir-o-Bot ages
    #if (linkName in list(ages.MirobotAgeDict.keys())):
    elif (linkName in list(ages.MirobotAgeDict.keys())):
        link = ages.MirobotAgeDict[linkName]
        #if linkName == "ndgelonin":
        #    start_dt_1 = datetime.datetime(2022, 8, 1, 13+6, 0, 0, tzinfo=datetime.timezone.utc)
        #    end_dt_1 = datetime.datetime(2022, 8, 1, 15+6, 0, 0, tzinfo=datetime.timezone.utc)
        #    start_dt_2 = datetime.datetime(2022, 8, 5, 12+6, 30, 0, tzinfo=datetime.timezone.utc)
        #    end_dt_2 = datetime.datetime(2022, 8, 5, 14+6, 30, 0, tzinfo=datetime.timezone.utc)
        #    if (start_dt_1 < now and now < end_dt_1) or (start_dt_2 < now and now < end_dt_2):
        #        link = ages.MirobotAgeDict[linkName]
        #    else:
        #        msg = "Sorry, NDG Elonin is not available at the momant."
        #        SendChatMessage(self, myself, [player], msg, cFlags.flags)
        #else:
        #    link = ages.MirobotAgeDict[linkName]
#        xBotAge.currentBotAge = list(link)
#        if len(link) > 4:
#            xBotAge.SetBotAgeSP(link[4])
#            #PtSendKIMessage(kKILocalChatStatusMsg, ",".join(xBotAge.currentBotAge))
#        xBotAge.LinkPlayerTo(self, link)
    # Trying MagicBot ages
    elif (linkName in list(ages.MagicbotAgeDict.keys())):
        link = ages.MagicbotAgeDict[linkName]
#        xBotAge.currentBotAge = list(link)
#        if len(link) > 4:
#            xBotAge.SetBotAgeSP(link[4])
#            #PtSendKIMessage(kKILocalChatStatusMsg, ",".join(xBotAge.currentBotAge))
#        xBotAge.LinkPlayerTo(self, link)
    elif (linkName in list(ages.PublicAgeDict.keys())):
        msg = "Sorry, I can't go to a public age."
        SendChatMessage(self, myself, [player], msg, cFlags.flags)
        return 0
    # Definitly not found
    else:
        #SendChatMessage(self, myself, [player], msg, cFlags.flags)
        return 0
    #
    if link:
    #if link[2] in allowedAgeInstanceGuids.values():
        if (bJalakAdded == True and link[1].lower() == "jalak"):
            msg = "Sorry I can't go to Jalak."
            SendChatMessage(self, myself, [player], msg, cFlags.flags)
            return 1

        if (now - lastLinkTime).total_seconds() > minDiff:
            #agePlayers = PtGetPlayerList()
            # ne pas tenir compte des robots
            agePlayers = [pl for pl in PtGetPlayerList() if not(pl.getPlayerID() in list(xPlayers.dicBot.keys()))]
            #for pl in agePlayers:
            #    if (pl.getPlayerID() in xPlayers.dicBot.keys()):

            # ne permettre le deplacement du robot que s'il est seul ou avec le demandeur (autres robots exclus)
            if len(agePlayers) == 0 or (agePlayers[0].getPlayerID() == player.getPlayerID()):
                #prevenir que l'on m'a demander de me lier vers un autre age
                msg = myself.getPlayerName() + " is linking to " + link[0] + " for at least " + str(minDiff / 60) + " minute(s)... PM me \"link\" to follow me."
                #Garder Les prp des autres ages peut faire planter lors de la liaison...
                RemovePrpToLocal(self)
                DelPrpLocal(pageBugs)
                
                # Si le feu de camp est allumer, l'éteindre sinon je risque de planter
                if bCampFireOn:
                    PutCampFireHere(self, cFlags, args=[myself, "off"])
                
                xBotAge.currentBotAge = list(link)
                if len(link) > 4:
                    xBotAge.SetBotAgeSP(link[4])
                    PtSendKIMessage(kKILocalChatStatusMsg, ",".join(xBotAge.currentBotAge))
                # Decharger les ages clones
                # Liaison
                xBotAge.LinkPlayerTo(self, link)
                #lastLinkTime = datetime.datetime.now()
                lastLinkTime = datetime.datetime.now(datetime.timezone.utc)
                
                buds = GetPeople("buddy", agePlayers)
                pList = agePlayers + buds
                SendChatMessage(self, myself, pList, msg, cFlags.flags)
            else:
                msg = "Sorry, you can send me somewhere else ONLY if there is no player in my age excepted you."
                SendChatMessage(self, myself, [player], msg, cFlags.flags)
        else:
            waitMinutes = int((minDiff - (now - lastLinkTime).total_seconds()) / 60)
            msg = "Please wait " + str(waitMinutes) + " minutes and retry."
            SendChatMessage(self, myself, [player], msg, cFlags.flags)
        return 1
    else:
        SendChatMessage(self, myself, [player], msg, cFlags.flags)
        return 0

#
def GetCoord(self, cFlags, args = []):
    #PtSendKIMessage(kKILocalChatStatusMsg, "> GetCoord")
    if len(args) < 1:
        return 0
    myself = PtGetLocalPlayer()
    player = args[0]
    if not isPlayerInAge(player):
        SendChatMessage(self, myself, [player], "You must be in my age, use link to join me." , cFlags.flags)
        return 1
    if len(args) < 2:
        # = pas de parametre => Retourne les coordonnees du joueur qui a envoye la commande
        soAvatar = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
        pos = soAvatar.position()
        x = int(round(pos.getX()))
        y = int(round(pos.getY()))
        z = int(math.ceil(pos.getZ()))
        xyz = "{0} {1} {2}".format(x, y, z)
        # D'ni coordinates
        coord = ptDniCoordinates()
        point = ptPoint3(x, y, z)
        coord.fromPoint(point)
        torans = coord.getTorans()
        hSpans = coord.getHSpans()
        vSpans = coord.getVSpans()
        # Prepare the message
        msg = "You are at: "
        if (torans != 0 or hSpans != 0 or vSpans != 0):
            dni = "(torans={0}, hSpan={1}, vSpan={2})".format(torans, hSpans, vSpans)
            msg = "{0} {1} {2}".format(msg, xyz, dni)
        else:
            msg = "{0} {1}".format(msg, xyz)
        SendChatMessage(self, myself, [player], msg, cFlags.flags)
        return 1
    else:
        # = au moins un parametre a ete passe (un nom pouvant contenir des espaces)
        params = args[1].split()
        myself = PtGetLocalPlayer()
        player = args[0]
        msg = "Avatar or object like '{0}' not found!".format(args[1])
        # Recherchons d'abord si c'est un joueur de l'age
        avatar = GetAgePlayerByName(args[1])
        if avatar is not None:
            # Un avatar a ete trouve
            soAvatar = PtGetAvatarKeyFromClientID(avatar.getPlayerID()).getSceneObject()
            pos = soAvatar.position()
            msg = "Player '{0}' found at ({1}, {2}, {3})".format(avatar.getPlayerName(), int(round(pos.getX())), int(round(pos.getY())), int(math.ceil(pos.getZ())))
        else:
            #msg = "{0} not found!".format(args[1])
            #if len(params) == 1:
            # Normalement, il n'y a pas d'espace dans les noms des scene objects.
            # Recherchons s'il existe un scene object portant ce nom
            soName = params[0]
            so = xBotAge.GetFirstSoWithCoord(soName)
            if so is not None:
                # An object was found
                pos = so.position()
                msg = "Object '{0}' found at ({1}, {2}, {3})".format(so.getName(), int(round(pos.getX())), int(round(pos.getY())), int(math.ceil(pos.getZ())))
            else:
                # No object found, try if there is a clone
                so = CloneObject.GetFirstClonePosition(soName)
                if so is not None:
                    pos = so.position()
                    msg = "Clone of '{0}' found at ({1}, {2}, {3})".format(so.getName(), int(round(pos.getX())), int(round(pos.getY())), int(math.ceil(pos.getZ())))
                #else:
                #    msg = soName + " not found!"
            #SendChatMessage(self, myself, [player], msg, cFlags.flags)
            # un scene object a ete trouve, on sort
            #return 1
        SendChatMessage(self, myself, [player], msg, cFlags.flags)
        return 1

#
def Find(self, cFlags, args = []):
    #PtSendKIMessage(kKILocalChatStatusMsg, "> Find")
    if len(args) < 1:
        return 0
    myself = PtGetLocalPlayer()
    player = args[0]
    if not isPlayerInAge(player):
        SendChatMessage(self, myself, [player], "You must be in my age, use link to join me." , cFlags.flags)
        return 1
    if len(args) > 1:
        params = args[1].split()
        myself = PtGetLocalPlayer()
        player = args[0]
        #bFound = False
        msg = "Avatar or object like '{0}' not found!".format(args[1])
        # Recherchons d'abord si c'est un joueur de l'age
        avatar = GetAgePlayerByName(args[1])
        if avatar is not None:
            # An avatar was found
            soAvatar = PtGetAvatarKeyFromClientID(avatar.getPlayerID()).getSceneObject()
            pos = soAvatar.getLocalToWorld()
            soPlayer = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
            soPlayer.netForce(1)
            soPlayer.physics.warp(pos)
            pos = soAvatar.position()
            msg = "Player '{0}' found at ({1}, {2}, {3})".format(avatar.getPlayerName(), int(round(pos.getX())), int(round(pos.getY())), int(math.ceil(pos.getZ())))
            #bFound = True
        else:
            #msg = "{0} not found!".format(args[1])
            #if len(params) == 1:
            # Recherchons s'il existe un scene object portant ce nom
            soName = params[0]
            so = xBotAge.GetFirstSoWithCoord(soName)
            if so is not None:
                # An object was found
                pos = so.position()
                soPlayer = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
                soPlayer.netForce(1)
                soPlayer.physics.warp(pos)
                try:
                    msg = "Object '{0}' found at ({1}, {2}, {3})".format(so.getName(), int(round(pos.getX())), int(round(pos.getY())), int(math.ceil(pos.getZ())))
                except:
                    msg = "Object '{0}' found at ({1}, {2}, {3})".format(so.getName(), pos.getX(), pos.getY(), pos.getZ())
                #bFound = True
            else:
                # No object found, try if there is a clone
                so = CloneObject.GetFirstClonePosition(soName)
                if so is not None:
                    # A clone of an object was found
                    pos = so.position()
                    soPlayer = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
                    soPlayer.netForce(1)
                    soPlayer.physics.warp(pos)
                    try:
                        msg = "Clone of '{0}' found at ({1}, {2}, {3})".format(so.getName(), int(round(pos.getX())), int(round(pos.getY())), int(math.ceil(pos.getZ())))
                    except:
                        msg = "Clone of '{0}' found at ({1}, {2}, {3})".format(so.getName(), pos.getX(), pos.getY(), pos.getZ())
                    #bFound = True
        #if bFound:
        SendChatMessage(self, myself, [player], msg, cFlags.flags)
        return 1

#
def GetRotMat(mat):
    mtr = ptMatrix44()
    matTrans = mat.getTranspose(mtr)
    t = matTrans.getData()
    tr = t[0], t[1], t[2], (0.0, 0.0, 0.0, 1.0)
    mtr.setData(tr)
    rotMat = mtr.getTranspose(ptMatrix44())
    return rotMat

#
def SetMat(mat, x, y, z):
    mt = ptMatrix44()
    matTrans = mat.getTranspose(mt)
    t = matTrans.getData()
    t2 = t[0], t[1], t[2], (x, y, z, 1.0)
    mt.setData(t2)
    newMat = mt.getTranspose(ptMatrix44())
    return newMat

#
def AutoSaveMat(self, player):
    xSave.WriteMatrix44(self, player, None, "auto")

#
def AutoWarp(self, player):
    xSave.WarpToSaved(self, player, None, "auto")

#
def AbsoluteDniGoto(self, cFlags, args = []):
    #PtSendKIMessage(kKILocalChatStatusMsg, "> AbsoluteDniGoto")
    print("AbsoluteDniGoto")
    if len(args) < 2:
        print("AbsoluteDniGoto: {0} arguments given.".format(len(args)))
        return 0
    params = args[1].split()
    myself = PtGetLocalPlayer()
    player = args[0]
    if len(params) < 3:
        print("AbsoluteDniGoto: {0} parameters given.".format(len(params)))
        return 0
    if not isPlayerInAge(player):
        SendChatMessage(self, myself, [player], "You must be in my age, use link to join me." , cFlags.flags)
        return 1
    soAvatar = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
    mpos = soAvatar.getLocalToWorld()
    try:
        #print "AbsoluteDniGoto: {0} {1} {2}".format(params[0], params[1], params[2])
        toran = int(params[0])
        #print "AbsoluteDniGoto: toran={0}".format(toran)
        hSpan = int(params[1])
        #print "AbsoluteDniGoto: hSpan={0}".format(hSpan)
        vSpan = int(params[2])
        #print "AbsoluteDniGoto: vSpan={0}".format(vSpan)
        theta = math.radians(float(toran) / 173.61)
        #print "AbsoluteDniGoto: theta={0}".format(theta)
        norme = float(hSpan) * 16
        #print "AbsoluteDniGoto: norme={0}".format(norme)
        #x = (norme * math.cos(theta)) 
        x = - (norme * math.sin(theta)) 
        #print "AbsoluteDniGoto: x={0}".format(x)
        #y = norme * math.sin(theta) + 688
        y = -(norme * math.cos(theta)) + 688
        #print "AbsoluteDniGoto: y={0}".format(y)
        z = (float(vSpan) * 16.) + 1504
        #print "AbsoluteDniGoto: z={0}".format(z)
        m = SetMat(mpos, x, y, z)
        soAvatar.netForce(1)
        soAvatar.physics.disable()
        soAvatar.physics.warp(m)
        return 1
    except ValueError:
        return 0

#
def AbsoluteGoto(self, cFlags, args = []):
    #PtSendKIMessage(kKILocalChatStatusMsg, "> AbsoluteGoto")
    if len(args) < 2:
        return 0
    params = args[1].split()
    myself = PtGetLocalPlayer()
    player = args[0]
    if len(params) == 1:
        soName = params[0]
        so = xBotAge.GetFirstSoWithCoord(soName)
        if so:
            pos = so.position()
            params = [int(round(pos.getX())), int(round(pos.getY())),  int(pos.getZ()) + 1]
            msg = so.getName() + " found at (" + str(params[0]) + ", " + str(params[1]) + ", " + str(params[2]) + ")"
        else:
            msg = soName + " not found!"
            return 1
        SendChatMessage(self, myself, [player], msg, cFlags.flags)
    if len(params) < 3:
        return 0
    if not isPlayerInAge(player):
        SendChatMessage(self, myself, [player], "You must be in my age, use link to join me." , cFlags.flags)
        return 1
    soAvatar = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
    mpos = soAvatar.getLocalToWorld()
    try:
        x = float(params[0])
        y = float(params[1])
        z = float(params[2])
        m = SetMat(mpos, x, y, z)
        soAvatar.netForce(1)
        soAvatar.physics.disable()
        soAvatar.physics.warp(m)
        return 1
    except ValueError:
        return 0

#
def RelativeGoto(self, cFlags, args = []):
    #PtSendKIMessage(kKILocalChatStatusMsg, "> RelativeGoto")
    if len(args) < 2:
        return 0
    params = args[1].split()
    if len(params) < 3:
        return 0
    myself = PtGetLocalPlayer()
    player = args[0]
    if not isPlayerInAge(player):
        SendChatMessage(self, myself, [player], "You must be in my age, use link to join me." , cFlags.flags)
        return 1
    soAvatar = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
    pos = soAvatar.getLocalToWorld()
    m = ptMatrix44()
    try:
        m.translate(ptVector3(float(params[0]), float(params[1]), float(params[2])))
        soAvatar.netForce(1)
        soAvatar.physics.disable()
        soAvatar.physics.warp(pos * m)
        soAvatar.physics.enable()
        #AutoSaveMat(self, player)
        #AutoWarp(self, player)
        soAvatar.physics.disable()
        return 1
    except ValueError:
        return 0
    
#
def Land(self, cFlags, args = []):
    #PtSendKIMessage(kKILocalChatStatusMsg, "> Land")
    if len(args) < 1:
        return 0
    myself = PtGetLocalPlayer()
    player = args[0]
    if not isPlayerInAge(player):
        SendChatMessage(self, myself, [player], "You must be in my age, use link to join me." , cFlags.flags)
        return 1
    soAvatar = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
    soAvatar.netForce(1)
    soAvatar.physics.enable()
    return 1

#
def Float(self, cFlags, args = []):
    #PtSendKIMessage(kKILocalChatStatusMsg, "> Float")
    if len(args) < 1:
        return 0
    elif len(args) < 2:
        return RelativeGoto(self, cFlags, [args[0], "0 0 0"])
    else:
        params = args[1].split()
        if len(params) > 0:
            return RelativeGoto(self, cFlags, [args[0], "0 0 " + str(params[0])])
        else:
            return RelativeGoto(self, cFlags, [args[0], "0 0 0"])

#
def Jump(self, cFlags, args = []):
    #PtSendKIMessage(kKILocalChatStatusMsg, "> Jump")
    if len(args) < 2:
        return 0
    params = args[1].split()
    if len(params) == 0:
        return 0
    elif len(params) == 1:
        y = str(0)
        z = str(params[0])
    else:
        y = "-" + str(params[0])
        z = str(params[1])
    if RelativeGoto(self, cFlags, [args[0], "0 " + y + " " + z]):
        return Land(self, cFlags, [args[0]])
    else:
        return 0

#
def Warp(self, cFlags, args = []):
    #PtSendKIMessage(kKILocalChatStatusMsg, "> Warp")
    myself = PtGetLocalPlayer()
    player = args[0]
    #PtSendRTChat(myself, [player], str(args) , 1)
    if len(args) == 1:
        return WarpToMe(self, cFlags, [player])
    elif len(args) > 1:
        toPlayer = GetAgePlayerByName(args[1])
        if toPlayer:
            return WarpToPlayer(self, cFlags, args[0], toPlayer)
        else:
            if RelativeGoto(self, cFlags, args) == 0:
                msg = args[1] + " is not a player in this age or it is not coordinates."
                #PtSendRTChat(myself, [player], msg, 16)
                SendChatMessage(self, myself, [player], msg, cFlags.flags)
        return 1
    else:
        return 0

#
def Rotate(self, cFlags, args = []):
    #PtSendKIMessage(kKILocalChatStatusMsg, "> Rotate")
    if len(args) < 2:
        return 0
    params = args[1].split()
    if len(params) < 2:
        return 0
    myself = PtGetLocalPlayer()
    player = args[0]
    if not isPlayerInAge(player):
        #PtSendRTChat(myself, [player], "You must be in my age, use link to join me." , 24)
        SendChatMessage(self, myself, [player], "You must be in my age, use link to join me.", cFlags.flags)
        return 1
    soAvatar = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
    pos = soAvatar.getLocalToWorld()
    m = ptMatrix44()
    axis = 0
    if params[0] == 'x':
        axis = 0
    elif params[0] == 'y':
        axis = 1
    elif params[0] == 'z':
        axis = 2
    else:
        return 0
    try:
        m.rotate(axis, (math.pi * float(params[1])) / 180)
        soAvatar.netForce(1)
        #soAvatar.physics.disable()
        soAvatar.physics.warp(pos * m)
        #AutoSaveMat(self, player)
        #AutoWarp(self, player)
        return 1
    except ValueError:
        return 0

#
def RotateZ(self, cFlags, args = []):
    #PtSendKIMessage(kKILocalChatStatusMsg, "> RotateZ")
    #myself = PtGetLocalPlayer()
    #player = args[0]
    #PtSendRTChat(myself, [player], str(args) , 1)
    if len(args) < 2:
        return 0
    params = args[1].split()
    #PtSendRTChat(myself, [player], str(params) , 1)
    if len(params) < 1:
        return 0
    return Rotate(self, cFlags, [args[0], "z " + str(params[0])])

# Version 1
# Save the position of an avatar in a file
def SavePosition_v1(self, cFlags, args = []):
    PtSendKIMessage(kKILocalChatStatusMsg, "> SavePosition")
    if len(args) < 1:
        return 0
    myself = PtGetLocalPlayer()
    player = args[0]
    if not isPlayerInAge(player):
        SendChatMessage(self, myself, [player], "You must be in my age, use link to join me." , cFlags.flags)
        return 1
    xSave.WriteMatrix44(self, player)
    SendChatMessage(self, myself, [player], "Your position is saved. Use \"ws\" to return to this position." , cFlags.flags)
    return 1

# Warp the avatar to his last saved position
def ReturnToPosition_v1(self, cFlags, args = []):
    #PtSendKIMessage(kKILocalChatStatusMsg, "> ReturnToPosition")
    if len(args) < 1:
        return 0
    myself = PtGetLocalPlayer()
    player = args[0]
    if not isPlayerInAge(player):
        SendChatMessage(self, myself, [player], "You must be in my age, use link to join me." , cFlags.flags)
        return 1
    ret = xSave.WarpToSaved(self, player)
    if ret:
        SendChatMessage(self, myself, [player], "You are at your last saved position." , cFlags.flags)
    else:
        SendChatMessage(self, myself, [player], "No saved position found. Did you use \"save\" before?" , cFlags.flags)
    return 1

# Version 2
# Save the position of an avatar in a file
def SavePosition(self, cFlags, args = []):
    #PtSendKIMessage(kKILocalChatStatusMsg, "> SavePosition")
    if len(args) < 1:
        return 0
    myself = PtGetLocalPlayer()
    player = args[0]
    if not isPlayerInAge(player):
        SendChatMessage(self, myself, [player], "You must be in my age, use link to join me." , cFlags.flags)
        return 1
    strIndex = "0"
    alias = ""
    if len(args) > 1:
        params = args[1].split()
        strIndex = params[0]
        if len(params) > 1:
            alias = re.sub(r'\W+', '', params[1].lower())
    #xSave2.WriteMatrix44(self, strIndex, player, alias)
    xSave2.WriteMatrix44(self, n=strIndex, player=player, ageFileName=None, prefix=None, aliasName=alias)
    SendChatMessage(self, myself, [player], "Your position is saved. Use \"ws " + strIndex + "\" to return to this position." , cFlags.flags)
    return 1

# Warp the avatar to his last saved position
def ReturnToPosition(self, cFlags, args = []):
    #PtSendKIMessage(kKILocalChatStatusMsg, "> ReturnToPosition")
    if len(args) < 1:
        return 0
    myself = PtGetLocalPlayer()
    player = args[0]
    if not isPlayerInAge(player):
        SendChatMessage(self, myself, [player], "You must be in my age, use link to join me." , cFlags.flags)
        return 1
    strIndex = "0"
    alias = ""
    #if len(args) > 1:
    #    strIndex = args[1]
    #if len(args) > 2:
    #    alias = re.sub(r'\W+', '', args[2].lower())
    if len(args) > 1:
        params = args[1].split()
        strIndex = params[0]
        if len(params) > 1:
            alias = re.sub(r'\W+', '', params[1].lower())
    #ret = xSave2.WarpToSaved(self, strIndex, player, alias)
    ret = xSave2.WarpToSaved(self, n=strIndex, player=player, ageFileName=None, prefix=None, aliasName=alias)
    if ret:
        SendChatMessage(self, myself, [player], "You are at your saved position " + strIndex + "." , cFlags.flags)
    else:
        SendChatMessage(self, myself, [player], "No saved position found. Did you use \"save [0 to 9]\" before?" , cFlags.flags)
    return 1


# Faire faire une animation a l'avatar demandeur
def Animer(self, cFlags, args = []):
    #PtSendKIMessage(kKILocalChatStatusMsg, "> Animer")
    if len(args) < 2:
        return 0
    myself = PtGetLocalPlayer()
    player = args[0]
    #PtSendRTChat(myself, [player], str(args) , 1)
    params = args[1].split()
    if len(params) < 2:
        return 0
    if not isPlayerInAge(player):
        SendChatMessage(self, myself, [player], "You must be in my age, use link to join me.", cFlags.flags)
        return 1
    animName = params[0]
    nbTimes = params[1]
    gender = ""
    if len(params) > 2:
        gender = params[2]
    ret = xAnim.Play(player, animName, nbTimes, gender)
    if ret and animName in travelAnimList:
        AutoSaveMat(self, player)
        AutoWarp(self, player)
    return ret

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
        print("Responder():\tResponder not found...")
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

# KiLight(ptPlayer player, int en)
# Activates and deactivates KI light for a player.
def KiLight(self, cFlags, args = []):
    if len(args) < 2:
        return 0
    player = args[0]
    myself = PtGetLocalPlayer()
    if not isPlayerInAge(player):
        SendChatMessage(self, myself, [player], "You must be in my age, use link to join me." , cFlags.flags)
        return 1
    soAvatar = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()

    if args[1] == "on":
        en = 1
    elif args[1] == "off":
        en = 0
    else:
        return 0
    for resp in soAvatar.getResponders():
        if (en == 1 and resp.getName() == 'respKILightOn') or (en == 0 and resp.getName() == 'respKILightOff'):
            RunResponder(soAvatar.getKey(), resp)
            break
    return 1

# BugsLight(ptPlayer player, int en)
# Activates and deactivates Eder Kemo bug lights for a player.
def BugsLight(self, cFlags, args = []):
    if len(args) < 2:
        return 0
    player = args[0]
    myself = PtGetLocalPlayer()
    if not isPlayerInAge(player):
        SendChatMessage(self, myself, [player], "You must be in my age, use link to join me." , cFlags.flags)
        return 1
    soAvatar = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
    
    if args[1] == "on":
        en = 1
    elif args[1] == "off":
        en = 0
    else:
        return 0
    PtSetLightAnimStart(soAvatar.getKey(), "RTOmni-BugLightTest", en)
    return 1

#**********************************************************************

#
def AddCleft(self, cFlags, args = []):
    PtSendKIMessage(kKILocalChatStatusMsg, "> AddCleft")
    if len(args) < 1:
        return 0
    myself = PtGetLocalPlayer()
    player = args[0]
    if not isPlayerInAge(player):
        SendChatMessage(self, myself, [player], "You must be in my age, use link to join me.", cFlags.flags)
        return 1
    ret = xCleft.AddCleft(self, args)
    if ret:
        PtSetAlarm(5, xBotAge.AlarmDisablePanicLinks(), 0)
        SendChatMessage(self, myself, [player], "I'm loading Cleft for you... Please wait.", cFlags.flags)
    else:
        SendChatMessage(self, myself, [player], "Error while loading Cleft.", cFlags.flags)
    return 1

# Test du modue d'Annabelle newdesert.py
def LoadNewDesert(self, cFlags, args = []):
    PtSendKIMessage(kKILocalChatStatusMsg, "> LoadNewDesert")
    if len(args) < 1:
        return 0
    myself = PtGetLocalPlayer()
    player = args[0]
    if not isPlayerInAge(player):
        SendChatMessage(self, myself, [player], "You must be in my age, use link to join me.", cFlags.flags)
        return 1
    from . import newdesert
    newdesert.load()
    SendChatMessage(self, myself, [player], "I'm loading NewDesert for you... Please wait.", cFlags.flags)
    return 1

#
def DisablePanicLinks(self, cFlags, args = []):
    myself = PtGetLocalPlayer()
    player = args[0]
    if not isPlayerInAge(player):
        SendChatMessage(self, myself, [player], "You must be in my age, use link to join me.", cFlags.flags)
        return 1
    try:
        xBotAge.DisablePanicLinks()
        PtSendKIMessage(kKILocalChatStatusMsg, "Panic links are disabled!")
        SendChatMessage(self, myself, [player], "Panic zones are disabled!", cFlags.flags)
        return 1
    except:
        return 0

#
def Ring(self, cFlags, args = []):
    if len(args) < 2:
        return 0
    params = args[1].split()
    if len(params) < 1:
        return 0
    myself = PtGetLocalPlayer()
    player = args[0]
    if not isPlayerInAge(player):
        SendChatMessage(self, myself, [player], "You must be in my age, use link to join me." , cFlags.flags)
        return 1
    soAvatar = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
    #if len(xBotAge.currentBotAge) > 1:
    #if xBotAge.currentBotAge[1] == "Neighborhood":
    PtSendKIMessage(kKILocalChatStatusMsg, ">Ring ")
    
    #1st parameter: color (or reset)
    color = params[0].lower().strip()
    
    if color == "reset":
        try:
            xHood.ResetClones()
            PtSendKIMessage(kKILocalChatStatusMsg, "The clones are reseted!")
            SendChatMessage(self, myself, [player], "The rings are reseted, you can try to create one again!" , cFlags.flags)
            return 1
        except:
            PtSendKIMessage(kKILocalChatStatusMsg, "Err: I failed to reset the clones!")
            SendChatMessage(self, myself, [player], "I failed to reset the rings!" , cFlags.flags)
            return 1
    
    if color == "detach":
        try:
            xHood.DetachClones(soAvatar)
            PtSendKIMessage(kKILocalChatStatusMsg, "The clones are detached!")
            SendChatMessage(self, myself, [player], "The rings are detached, you can try to create one again!" , cFlags.flags)
            return 1
        except:
            PtSendKIMessage(kKILocalChatStatusMsg, "Err: I failed to detach the clones!")
            SendChatMessage(self, myself, [player], "I failed to detach the rings!" , cFlags.flags)
            return 1
    
    #bOn = bOn.lower()
    #if not (color in ("yellow", "blue", "red", "white", "white2", "white3", "white4")):
    if not (color in ("yellow", "blue", "red", "white")):
        color = "red"
    bOn = 1
    #2nd parameter: on/off
    if len(params) > 1:
        if params[1].lower().strip() == "off":
            bOn = 0
        else:
            #if params[1].lower().strip().isnumeric():
            p2 = params[1].lower().strip()
            try:
                float(p2)
                params.insert(1, 'on')
            except ValueError:
                pass
        
    dist = 3
    height = 4
    #3rd parameter: height
    if len(params) > 2:
        try:
            height = float(params[2].lower().strip())
        except:
            PtSendKIMessage(kKILocalChatStatusMsg, "Err: the optional 3rd parameter must be a number!")
            SendChatMessage(self, myself, [player], "The optional 3rd parameter, height, must be a number!" , cFlags.flags)
            return 1
    #4th parameter: distance
    if len(params) > 3:
        try:
            dist = float(params[3].lower().strip())
        except:
            PtSendKIMessage(kKILocalChatStatusMsg, "Err: the optional 4th parameter must be a number!")
            SendChatMessage(self, myself, [player], "The optional 4th parameter, radius, must be a number!" , cFlags.flags)
            return 1
    PtSendKIMessage(kKILocalChatStatusMsg, "ring {}, {}".format(color, bOn))
    xHood.Entourer(dist, height, color, 9, soAvatar, bOn)
    PtSendKIMessage(kKILocalChatStatusMsg, "=> nb clones: {}".format(xHood.CompterClonesBilles()))
    if bOn:
        SendChatMessage(self, myself, [player], "I'm creating a fire marble ring for you, wait a bit ..." , cFlags.flags)
    else:
        SendChatMessage(self, myself, [player], "I'm destroying the fire marble ring ..." , cFlags.flags)
    return 1
    #else:
    #    PtSendKIMessage(kKILocalChatStatusMsg, "=> Je ne suis pas dans un Hood!")
    #    #PtSendRTChat(myself, [player], "This command does'nt work here, we must be in a Hood." , cFlags.flags)
    #    return 1
    #else:
    #    PtSendKIMessage(kKILocalChatStatusMsg, "=> Je ne sais pas dans quel age je suis!")
    #    SendChatMessage(self, myself, [player], "Oops, I don't know where I am ..." , cFlags.flags)
    #    return 1

#
def UnloadClones(self, cFlags, args = []):
    myself = PtGetLocalPlayer()
    player = args[0]
    xHood.DechargerClonesBilles()
    SendChatMessage(self, myself, [player], "Clones unloaded", cFlags.flags)
    return 1

#
def ReloadClones(self, cFlags, args = []):
    myself = PtGetLocalPlayer()
    player = args[0]
    xHood.RechargerClonesBilles()
    SendChatMessage(self, myself, [player], "Clones reloaded", cFlags.flags)
    return 1

#
def CountClones(self, cFlags, args = []):
    myself = PtGetLocalPlayer()
    player = args[0]
    nb = xHood.CompterClonesBilles()
    SendChatMessage(self, myself, [player], "There is {} clone(s)".format(nb), cFlags.flags)
    return 1


# (reprise de Michel)
def Board(self, cFlags, args = []):
    myself = PtGetLocalPlayer()
    player = args[0]
    if not isPlayerInAge(player):
        SendChatMessage(self, myself, [player], "You must be in my age, use link to join me." , cFlags.flags)
        return 1
    if len(xBotAge.currentBotAge) > 1:
        if xBotAge.currentBotAge[1] == "Ahnonay":
            ##xScore.InitScoreJ()
            #xScore.InitScore()
            PtConsoleNet("Nav.PageInNode %s" % ("nb01") , 1)
            PtSetAlarm(8, xScore.Board(xScore.scoreActuel[0], xScore.scoreActuel[1]), 1)
            return 1
        else:
            PtSendKIMessage(kKILocalChatStatusMsg, "=> Je ne suis pas a Ahnonay!")
            SendChatMessage(self, myself, [player], "This command does'nt work here, we must be in Ahnonay." , cFlags.flags)
            return 1
    else:
        PtSendKIMessage(kKILocalChatStatusMsg, "=> Je ne sais pas dans quel age je suis!")
        SendChatMessage(self, myself, [player], "Oops, I don't know where I am ..." , cFlags.flags)
        return 1

# To open or close a Bahro door (in Eder Delin and Eder Tsogal currently)
def OpenOrCloseBahroDoor(self, cFlags, args = []):
    """
    if len(args) < 2:
        return 0
    """
    myself = PtGetLocalPlayer()
    player = args[0]
    """
    if not isPlayerInAge(player):
        SendChatMessage(self, myself, [player], "You must be in my age, use link to join me." , cFlags.flags)
        return 1
    # set action
    sOpenOrClose = args[1]
    if sOpenOrClose == "open":
        action = 0
        sAction = "opening"
    elif sOpenOrClose == "close":
        action = 1
        sAction = "closing"
    else:
        PtSendKIMessage(kKILocalChatStatusMsg, "=> I don't know how to %s a door!" % (sOpenOrClose))
        SendChatMessage(self, myself, [player], "I don't know how to %s a door!" , cFlags.flags)
        return 1
    # age cases
    if len(xBotAge.currentBotAge) > 1:
        if xBotAge.currentBotAge[1] == "EderDelin":
            PtSendKIMessage(kKILocalChatStatusMsg, "OpenOrCloseBahroDoor %s, %s" % (xBotAge.currentBotAge[1], action))
            xDelin.Door(action)
            SendChatMessage(self, myself, [player], "Ok, I am %s the door ..." % (sAction) , cFlags.flags)
        elif xBotAge.currentBotAge[1] == "EderTsogal":
            PtSendKIMessage(kKILocalChatStatusMsg, "OpenOrCloseBahroDoor %s, %s" % (xBotAge.currentBotAge[1], action))
            xTsogal.Door(action)
            SendChatMessage(self, myself, [player], "Ok, I am %s the door ..." % (sAction) , cFlags.flags)
        else:
            PtSendKIMessage(kKILocalChatStatusMsg, "=> Cette fonction ne fonctionne pas dans cet age!")
            SendChatMessage(self, myself, [player], "This command does'nt work here." , cFlags.flags)
    else:
        PtSendKIMessage(kKILocalChatStatusMsg, "=> Je ne sais pas dans quel age je suis!")
        SendChatMessage(self, myself, [player], "Oops, I don't know where I am ..." , cFlags.flags)
    return 1
    """
    PtSendKIMessage(kKILocalChatStatusMsg, "=> OpenOrCloseBahroDoor : cette commande est desactivee!")
    SendChatMessage(self, myself, [player], "Sorry, this command is disactivated." , cFlags.flags)
    return 1
    

#
def DisableFog(self, cFlags, args = []):
    myself = PtGetLocalPlayer()
    player = args[0]
    if not isPlayerInAge(player):
        SendChatMessage(self, myself, [player], "You must be in my age, use link to join me.", cFlags.flags)
        return 1
    try:
        xBotAge.NoFog()
        PtSendKIMessage(kKILocalChatStatusMsg, "Fog gone!")
        SendChatMessage(self, myself, [player], "Fog gone!", cFlags.flags)
        return 1
    except:
        PtSendKIMessage(kKILocalChatStatusMsg, "Error in DisableFog")
        return 0

#
def SetRendererStyle(self, cFlags, args = []):
    myself = PtGetLocalPlayer()
    player = args[0]
    if not isPlayerInAge(player):
        SendChatMessage(self, myself, [player], "You must be in my age, use link to join me.", cFlags.flags)
        return 1
    vstyle = "default"
    if len(args) > 1:
        vstyle = args[1]
        xBotAge.SetRenderer(style = vstyle)
        PtSendKIMessage(kKILocalChatStatusMsg, "> SetRendererStyle: {}".format(vstyle))
        SendChatMessage(self, myself, [player], "{} style".format(vstyle), cFlags.flags)
        return 1
    else:
        PtSendKIMessage(kKILocalChatStatusMsg, "> SetRendererStyle: no param given.")
        return 0

#
def SetRendererFogLinear(self, cFlags, args = []):
    myself = PtGetLocalPlayer()
    player = args[0]
    if not isPlayerInAge(player):
        SendChatMessage(self, myself, [player], "You must be in my age, use link to join me.", cFlags.flags)
        return 1
    vstart = None
    vend = None
    vdensity = None
    if len(args) > 1:
        params = args[1].split()
        if len(params) > 0:
            try:
                vstart = int(params[0])
            except:
                pass
        if len(params) > 1:
            try:
                vend = int(params[1])
            except:
                pass
        if len(params) > 2:
            try:
                vdensity = float(params[2])
            except:
                pass
        xBotAge.SetRenderer(style = None, start = vstart, end = vend, density = vdensity)
        PtSendKIMessage(kKILocalChatStatusMsg, "> SetRendererFogLinear: shape = ({}, {}, {}).".format(vstart, vend, vdensity))
        SendChatMessage(self, myself, [player], "Fog shape changed.", cFlags.flags)
        return 1
    else:
        PtSendKIMessage(kKILocalChatStatusMsg, "> SetRendererFogLinear: no param given.")
        return 0

#
def SetRendererFogColor(self, cFlags, args = []):
    myself = PtGetLocalPlayer()
    player = args[0]
    if not isPlayerInAge(player):
        SendChatMessage(self, myself, [player], "You must be in my age, use link to join me.", cFlags.flags)
        return 1
    vr = None
    vg = None
    vb = None
    strCol = None
    numero = None
    dicColors = {
                "white":[1, 1, 1], 
                "red":[1, 0, 0], 
                "pink":[1, 0.5, 0.5], 
                "orange":[1, .5, 0], 
                "brown":[1, .6, .15], 
                "yellow":[1, 1, 0], 
                "green":[0, 1, 0], 
                "blue":[0, 0, 1], 
                "violet":[1, 0, 1], 
                "purple":[1, 0, .8], 
                "black":[0, 0, 0], 
                "gold":[1, .84, 0],
                }
    if len(args) > 1:
        params = args[1].split()
        if len(params) > 0:
            try:
                vr = float(params[0]) / 100.
            except:
                strCol = params[0].lower()
                numero = 1
                match = re.match(r"([a-z]+)([1-5])", strCol, re.I)
                if match:
                    items = match.groups()
                    strCol = items[0]
                    numero = int(items[1])
                # nom de couleur connu?
                if strCol in list(dicColors.keys()):
                    vr = float(dicColors[strCol][0]) * ((6. - float(numero)) / 5.) ** 2
                    vg = float(dicColors[strCol][1]) * ((6. - float(numero)) / 5.) ** 2
                    vb = float(dicColors[strCol][2]) * ((6. - float(numero)) / 5.) ** 2
                else:
                    strCol = None
        #if strCol is None and len(params) > 1:
        #    try:
        #        vg = float(params[1]) / 100.
        #    except:
        #        pass
        if len(params) > 1:
            if strCol is None:
                try:
                    vg = float(params[1]) / 100.
                except:
                    pass
            else:
                try:
                    vr = float(dicColors[strCol][0]) * ((6. - float(params[1])) / 5.) ** 2
                    vg = float(dicColors[strCol][1]) * ((6. - float(params[1])) / 5.) ** 2
                    vb = float(dicColors[strCol][2]) * ((6. - float(params[1])) / 5.) ** 2
                except:
                    pass
        if strCol is None and len(params) > 2:
            try:
                vb = float(params[2]) / 100.
            except:
                pass
        xBotAge.SetRenderer(style = None, r = vr, g = vg, b = vb)
        PtSendKIMessage(kKILocalChatStatusMsg, "> SetRendererFogColor: color = ({}, {}, {}).".format(vr, vg, vb))
        #SendChatMessage(self, myself, [player], "Fog color changed.", cFlags.flags)
        #SendChatMessage(self, myself, [player], "Back color changed to {} {} ==> ({}, {}, {}).".format(strCol, numero, vr*100, vg*100, vb*100), cFlags.flags)
        if strCol is None:
            if vr is not None and vg is not None and vb is not None:
                SendChatMessage(self, myself, [player], "Fog color changed to  ({}, {}, {}).".format(vr*100, vg*100, vb*100), cFlags.flags)
            else:
                msg = None
                if vr is None:
                    msg = " The red component [r] must be a number"
                if vg is None:
                    if msg is None:
                        msg = " The green component [g] must be a number"
                    else:
                        msg += ", the green component [g] must be a number"
                if vb is None:
                    if msg is None:
                        msg = " The blue component [b] must be a number"
                    else:
                        msg += ", the blue component [b] must be a number"
                SendChatMessage(self, myself, [player], "Fog Color Error: {}.".format(msg), cFlags.flags)
        else:
            SendChatMessage(self, myself, [player], "Fog color changed to {} {} ==> ({}, {}, {}).".format(strCol, numero, vr*100, vg*100, vb*100), cFlags.flags)
        return 1
    else:
        PtSendKIMessage(kKILocalChatStatusMsg, "> SetRendererFogColor: no param given.")
        return 0

#
def SetRendererClearColor(self, cFlags, args = []):
    myself = PtGetLocalPlayer()
    player = args[0]
    if not isPlayerInAge(player):
        SendChatMessage(self, myself, [player], "You must be in my age, use link to join me.", cFlags.flags)
        return 1
    vcr = None
    vcg = None
    vcb = None
    strCol = None
    numero = None
    dicColors = {
                "white":[1, 1, 1], 
                "grey":[.9, .9, .9], 
                "gray":[.9, .9, .9], 
                "red":[1, 0, 0], 
                "pink":[1, 0.5, 0.5], 
                "orange":[1, .5, 0], 
                "brown":[1, .6, .15], 
                "yellow":[1, 1, 0], 
                "green":[0, 1, 0], 
                "blue":[0, 0, 1], 
                "violet":[1, 0, 1], 
                "purple":[1, 0, .8], 
                "black":[0, 0, 0], 
                "gold":[1, .84, 0],
                #"cave":[0.5252, 0.4907, 0.4785],
                "cave":[0.8000, 0.7474, 0.7289],
                }
    if len(args) > 1:
        params = args[1].split()
        if len(params) > 0:
            try:
                vcr = float(params[0]) / 100.
            except:
                strCol = params[0].lower()
                numero = 1
                match = re.match(r"([a-z]+)([1-5])", strCol, re.I)
                if match:
                    items = match.groups()
                    strCol = items[0]
                    numero = int(items[1])
                # nom de couleur connu?
                if strCol in list(dicColors.keys()):
                    vcr = float(dicColors[strCol][0]) * ((6. - float(numero)) / 5.) ** 2
                    vcg = float(dicColors[strCol][1]) * ((6. - float(numero)) / 5.) ** 2
                    vcb = float(dicColors[strCol][2]) * ((6. - float(numero)) / 5.) ** 2
                else:
                    err = "Unknown color"
        #if strCol is None and len(params) > 1:
        if len(params) > 1:
            if strCol is None:
                try:
                    vcg = float(params[1]) / 100.
                except:
                    err = "[g] must be a number between 0 and 100"
            else:
                try:
                    vcr = float(dicColors[strCol][0]) * ((6. - float(params[1])) / 5.) ** 2
                    vcg = float(dicColors[strCol][1]) * ((6. - float(params[1])) / 5.) ** 2
                    vcb = float(dicColors[strCol][2]) * ((6. - float(params[1])) / 5.) ** 2
                except:
                    err = "Unknown color"
        if strCol is None and len(params) > 2:
            try:
                vcb = float(params[2]) / 100.
            except:
                err = "[b] must be a number between 0 and 100"
        xBotAge.SetRenderer(style = None, cr = vcr, cg = vcg, cb = vcb)
        PtSendKIMessage(kKILocalChatStatusMsg, "> SetRendererClearColor: color = ({}, {}, {}).".format(vcr, vcg, vcb))
        #SendChatMessage(self, myself, [player], "Back color changed to {} {} ==> ({}, {}, {}).".format(strCol, numero, vcr*100, vcg*100, vcb*100), cFlags.flags)
        if strCol is None:
            if vcr is not None and vcg is not None and vcb is not None:
                SendChatMessage(self, myself, [player], "Sky color changed to  ({}, {}, {}).".format(vcr*100, vcg*100, vcb*100), cFlags.flags)
            else:
                msg = None
                if vcr is None:
                    msg = " The red component [r] must be a number"
                if vcg is None:
                    if msg is None:
                        msg = " The green component [g] must be a number"
                    else:
                        msg += ", the green component [g] must be a number"
                if vcb is None:
                    if msg is None:
                        msg = " The blue component [b] must be a number"
                    else:
                        msg += ", the blue component [b] must be a number"
                SendChatMessage(self, myself, [player], "Sky Color Error: {}.".format(msg), cFlags.flags)
        else:
            try:
                SendChatMessage(self, myself, [player], "Sky color changed to {} {} ==> ({}, {}, {}).".format(strCol, numero, vcr*100, vcg*100, vcb*100), cFlags.flags)
            except:
                SendChatMessage(self, myself, [player], "Sky color {} is unknown.".format(strCol), cFlags.flags)
        return 1
    else:
        PtSendKIMessage(kKILocalChatStatusMsg, "> SetRendererClearColor: no param given.")
        return 0

# 
def CreateReltoNight1_v1(self, cFlags, args = []):
    myself = PtGetLocalPlayer()
    player = args[0]
    if not isPlayerInAge(player):
        SendChatMessage(self, myself, [player], "You must be in my age, use link to join me.", cFlags.flags)
        return 1
    bOn = True
    if len(args) > 1:
        if args[1] == "off":
            bOn = False
    try:
        msg = None
        # age cases
        if len(xBotAge.currentBotAge) > 1:
            if xBotAge.currentBotAge[1] == "Personal":
                msg = xRelto.CreateNightSky(7.5, bOn)
            elif xRelto.bPagesAdded:
                msg = xRelto.CreateNightSky(100, bOn)
            else:
                msg = xRelto.CreateNightSky(50, bOn)
        else:
            PtSendKIMessage(kKILocalChatStatusMsg, "=> Je ne sais pas dans quel age je suis!")
            SendChatMessage(self, myself, [player], "Oops, I don't know where I am ..." , cFlags.flags)
        PtSendKIMessage(kKILocalChatStatusMsg, "> CreateReltoNight1: {}".format(msg))        
        return 1
    except:
        PtSendKIMessage(kKILocalChatStatusMsg, "> CreateReltoNight1: Error.")
        return 0

# 
def CreateReltoNight1(self, cFlags, args = []):
    myself = PtGetLocalPlayer()
    player = args[0]
    if not isPlayerInAge(player):
        SendChatMessage(self, myself, [player], "You must be in my age, use link to join me.", cFlags.flags)
        return 1
    bOn = True
    scale = None
    if len(args) > 1:
        try:
            scale = float(args[1])
        except:
            if args[1] == "off":
                bOn = False
    try:
        msg = None
        # age cases
        if len(xBotAge.currentBotAge) > 1:
            if xBotAge.currentBotAge[1] == "Personal":
                if scale is None:
                    #scale = 7.5
                    scale = 100
            #elif xRelto.bPagesAdded:
            #    if scale is None:
            #        scale = 100
            elif xBotAge.currentBotAge[1] == "city":
                if scale is None:
                    #scale = 34
                    scale = 400
            else:
                if scale is None:
                    #scale = 50
                    scale = 200
        else:
            PtSendKIMessage(kKILocalChatStatusMsg, "=> Je ne sais pas dans quel age je suis!")
            if scale is None:
                #scale = 75
                scale = 300
        #msg = xRelto.CreateNightSky(scale, bOn)
        msg = ReltoNight.CreateNightSky(scale, bOn)
        PtSendKIMessage(kKILocalChatStatusMsg, "> CreateReltoNight1: {}".format(msg))        
        return 1
    except:
        PtSendKIMessage(kKILocalChatStatusMsg, "> CreateReltoNight1: Error.")
        return 0

# 
def ReltoDay(self, cFlags, args = []):
    onOff = "off"
    if len(args) > 1:
        if args[1] == "off":
            onOff = "on"
    return CreateReltoNight1(self, cFlags, [args[0], onOff])

# 
#def CrimsonNight(self, cFlags, args = []):
#    onOff = "on"
#    if len(args) > 1:
#        if args[1] == "off":
#            onOff = "off"
#    ret = CreateReltoNight1(self, cFlags, [args[0], onOff])
#    #xBotAge.SetRenderer(style = None, start = 0, end = 10000, density = 1., r = .5, g = 0, b = 0)
#   
#    return ret

# 
def CreateReltoNight2(self, cFlags, args = []):
    myself = PtGetLocalPlayer()
    player = args[0]
    if not isPlayerInAge(player):
        SendChatMessage(self, myself, [player], "You must be in my age, use link to join me.", cFlags.flags)
        return 1
    bOn = True
    scale = 400
    style = "default"
    if len(args) > 1:
        style = args[1]
    try:
        msg = None        
        msg = ReltoNight.CreateNightSky2(scale, bOn, style)
        PtSendKIMessage(kKILocalChatStatusMsg, "> CreateReltoNight1: {}".format(msg))        
        return 1
    except:
        PtSendKIMessage(kKILocalChatStatusMsg, "> CreateReltoNight1: Error.")
        return 0

## 
#def ReltoDay2(self, cFlags, args = []):
#    onOff = "off"
#    if len(args) > 1:
#        if args[1] == "off":
#            onOff = "on"
#    return CreateReltoNight2(self, cFlags, [args[0], onOff])

# CMS
def ColoredMovingSky(self, cFlags, args = []):
    myself = PtGetLocalPlayer()
    player = args[0]
    if not isPlayerInAge(player):
        SendChatMessage(self, myself, [player], "You must be in my age, use link to join me.", cFlags.flags)
        return 1
    bOn = True
    #scale = None
    scale = 400
    if len(args) > 1:
        try:
            scale = float(args[1])
        except:
            if args[1] == "off":
                bOn = False
    try:
        msg = None
        #scale = 400
        msg = ReltoNight2.CreateNightSky(scale, bOn)
        PtSendKIMessage(kKILocalChatStatusMsg, "> ColoredMovingSky: {}".format(msg))        
        return 1
    except:
        PtSendKIMessage(kKILocalChatStatusMsg, "> ColoredMovingSky: Error.")
        return 0

# 
def FogOnOff(self, cFlags, args = []):
    myself = PtGetLocalPlayer()
    player = args[0]
    if not isPlayerInAge(player):
        SendChatMessage(self, myself, [player], "You must be in my age, use link to join me.", cFlags.flags)
        return 1
    bOn = True
    state = "on"
    if len(args) > 1:
        if args[1] == "off":
            bOn = False
            state = "off"
    try:
        #xBotAge.ToggleSceneObjects("Fog", age = None, bDrawOn = bOn, bPhysicsOn = bOn)
        if bOn:
            xBotAge.SetRenderer(style = "default")
        else:
            #xBotAge.SetRenderer(style = "100000", start = 0, end = 0, density = 0, r = 0.2, g = 0.2, b = 0.4, cr = 0.4, cg = 0.4, cb = 0.5)
            xBotAge.SetRenderer(style = "100000", start = 0, end = 0, density = 0)
        #PtSendKIMessage(kKILocalChatStatusMsg, "> FogOnOff: {} done.".format(bOn))
        SendChatMessage(self, myself, [player], "Fog is {}.".format(state), cFlags.flags)
        return 1
    except:
        PtSendKIMessage(kKILocalChatStatusMsg, "> FogOnOff: Error.")
        return 0

# 
def SkyOnOff(self, cFlags, args = []):
    myself = PtGetLocalPlayer()
    player = args[0]
    if not isPlayerInAge(player):
        SendChatMessage(self, myself, [player], "You must be in my age, use link to join me.", cFlags.flags)
        return 1
    bOn = True
    state = "on"
    if len(args) > 1:
        if args[1] == "off":
            bOn = False
            state = "off"
    try:
        xBotAge.ToggleSceneObjects("Sky", age = None, bDrawOn = bOn, bPhysicsOn = bOn)
        xBotAge.ToggleSceneObjects("ClearColor", age = "Minkata", bDrawOn = bOn, bPhysicsOn = bOn)
        xBotAge.ToggleSceneObjects("StarGlobe", age = "Minkata", bDrawOn = bOn, bPhysicsOn = bOn)
        #xBotAge.ToggleSceneObjects("Constellation", age = "Minkata", bDrawOn = bOn, bPhysicsOn = bOn)
        #xBotAge.ToggleSceneObjects("Galaxy", age = "Minkata", bDrawOn = bOn, bPhysicsOn = bOn)
        #PtSendKIMessage(kKILocalChatStatusMsg, "> SkyOnOff: {} done.".format(bOn))
        SendChatMessage(self, myself, [player], "Sky is {}.".format(state), cFlags.flags)
        return 1
    except:
        PtSendKIMessage(kKILocalChatStatusMsg, "> SkyOnOff: Error.")
        return 0

# Pour "nosky" equivalent a la commande "sky off"
def DisableSky(self, cFlags, args = []):
    return SkyOnOff(self, cFlags, [args[0], "off"])

# 
def DustOnOff(self, cFlags, args = []):
    myself = PtGetLocalPlayer()
    player = args[0]
    if not isPlayerInAge(player):
        SendChatMessage(self, myself, [player], "You must be in my age, use link to join me.", cFlags.flags)
        return 1
    bOn = True
    if len(args) > 1:
        if args[1] == "off":
            bOn = False
    try:
        xBotAge.ToggleSceneObjects("Dust", age = "Minkata", bDrawOn = bOn, bPhysicsOn = bOn)
        return 1
    except:
        return 0

# Pour "nodust" equivalent a la commande "dust off"
def DisableDust(self, cFlags, args = []):
    return DustOnOff(self, cFlags, [args[0], "off"])

# fait tomber des objets clones de SoccerBall sur sa tete
def Soccer(self, cFlags, args = []):
    myself = PtGetLocalPlayer()
    player = args[0]
    if not isPlayerInAge(player):
        SendChatMessage(self, myself, [player], "You must be in my age, use link to join me.", cFlags.flags)
        return 1
    try:
        print(">> Soccer : soAvatar")
        soAvatar = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
        print(">> Soccer : pos")
        pos = soAvatar.position()
        print(">> Soccer : ready to drop soccer balls ({} - {})".format(soAvatar, pos))
        DropObjects.Soccer(position=pos)
        print(">> Soccer : done")
        return 1
    except:
        return 0
    #SendChatMessage(self, myself, [player], "The SOCCER command is disabled.", cFlags.flags)
    #return 1

# fait tomber des objets clones sur sa tete
def Drop(self, cFlags, args = []):
    #myself = PtGetLocalPlayer()
    #player = args[0]
    #if not isPlayerInAge(player):
    #    SendChatMessage(self, myself, [player], "You must be in my age, use link to join me.", cFlags.flags)
    #    return 1
    #try:
    #    print ">> Drop : soAvatar"
    #    soAvatar = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
    #    print ">> Drop : pos"
    #    pos = soAvatar.position()
    #    print ">> Drop : ready to drop ({} - {})".format(soAvatar, pos)
    #    DropObjects.Drop(position=pos)
    #    print ">> Drop : done"
    #    return 1
    #except:
    #    return 0
    SendChatMessage(self, myself, [player], "The DROP command is disabled.", cFlags.flags)
    return 1


# supprime les objets clones par la commande drop
def Clean(self, cFlags, args = []):
    #myself = PtGetLocalPlayer()
    #player = args[0]
    #if not isPlayerInAge(player):
    #    SendChatMessage(self, myself, [player], "You must be in my age, use link to join me.", cFlags.flags)
    #    return 1
    #try:
    #    DropObjects.Drop(position=None, bOn=False)
    #    print ">> Clean : done"
    #    return 1
    #except:
    #    return 0
    SendChatMessage(self, myself, [player], "The CLEAN command is disabled.", cFlags.flags)
    return 1

#
def LightForKveer(av, bLoadShowOn=True, bAttachOn=False):
    bOn = bLoadShowOn
    pos1 = ptMatrix44()
    pos2 = ptMatrix44()
    pos3 = ptMatrix44()
    pos4 = ptMatrix44()

    tuplePos1 = ((-0.999985933304, -0.00528157455847, 0.0, -0.273455888033), (0.00528157455847, -0.999985933304, 0.0, -47.5185241699), (0.0, 0.0, 1.0, 9.40436553955), (0.0, 0.0, 0.0, 1.0))
    tuplePos2 = ((-0.999986410141, -0.00528157642111, 0.0, -0.273455888033), (0.00528157642111, -0.999986410141, 0.0, -47.5185241699), (0.0, 0.0, 1.0, 48.0664749146), (0.0, 0.0, 0.0, 1.0))
    tuplePos3 = ((0.999998033047, 0.00198203604668, 0.0, 0.119770005345), (-0.00198203604668, 0.999998033047, 0.0, 3.88968443871), (0.0, 0.0, 1.0, 49.4459877014), (0.0, 0.0, 0.0, 1.0))
    tuplePos4 = ((-0.999917268753, -0.0128562794998, 0.0, -0.539468109608), (0.0128562794998, -0.999917268753, 0.0, -71.0015563965), (0.0, 0.0, 1.0, 9.40436553955), (0.0, 0.0, 0.0, 1.0))

    pos1.setData(tuplePos1)
    pos2.setData(tuplePos2)
    pos3.setData(tuplePos3)
    pos4.setData(tuplePos4)
    
    #av = PtGetLocalAvatar()
    #pos = PtGetLocalAvatar().getLocalToWorld()
    mRot = ptMatrix44()
    mRot.rotate(0, (math.pi * float(90.0)) / 180)
    pos6 = pos4 * mRot
    
    mRot = ptMatrix44()
    mRot.rotate(0, (math.pi * float(45.0)) / 180)
    pos5 = pos3 * mRot
    """
    CloneObject.Clone2("RTOmniLight03", "EderTsogal", bShow=bOn, bLoad=bOn, matPos=pos1, bAttach=bAttachOn, soAvatar=av)
    CloneObject.Clone2("RTOmniLight04", "EderTsogal", bShow=bOn, bLoad=bOn, matPos=pos1, bAttach=bAttachOn, soAvatar=av)
    CloneObject.Clone2("RTOmniLight05", "EderTsogal", bShow=bOn, bLoad=bOn, matPos=pos1, bAttach=bAttachOn, soAvatar=av)
    CloneObject.Clone2("RTOmniLight06", "EderTsogal", bShow=bOn, bLoad=bOn, matPos=pos2, bAttach=bAttachOn, soAvatar=av)
    CloneObject.Clone2("RTOmniLight07", "EderTsogal", bShow=bOn, bLoad=bOn, matPos=pos2, bAttach=bAttachOn, soAvatar=av)
    CloneObject.Clone2("RTOmniLight09", "EderTsogal", bShow=bOn, bLoad=bOn, matPos=pos3, bAttach=bAttachOn, soAvatar=av)
    CloneObject.Clone2("RTDirLight01Anim", "EderTsogal", bShow=bOn, bLoad=bOn, matPos=pos3, bAttach=bAttachOn, soAvatar=av)
    CloneObject.Clone2("RTOmniLightFountain", "EderTsogal", bShow=bOn, bLoad=bOn, matPos=pos4, bAttach=bAttachOn, soAvatar=av)
    CloneObject.Clone2("RTProjDirLight03", "Payiferen", bShow=bOn, bLoad=bOn, matPos=pos5, bAttach=bAttachOn, soAvatar=av)
    CloneObject.Clone2("RTProjDirLight02", "Payiferen", bShow=bOn, bLoad=bOn, matPos=pos6, bAttach=bAttachOn, soAvatar=av)
    """
    CloneObject.Clone2("RTOmniLight03", "EderTsogal", bShow=bOn, bLoad=bOn, matPos=pos1, bAttach=bAttachOn, soAvatar=av)
    CloneObject.Clone2("RTOmniLight04", "EderTsogal", bShow=bOn, bLoad=bOn, matPos=pos5, bAttach=bAttachOn, soAvatar=av)
    CloneObject.Clone2("RTOmniLight05", "EderTsogal", bShow=bOn, bLoad=bOn, matPos=pos6, bAttach=bAttachOn, soAvatar=av)
    CloneObject.Clone2("RTOmniLight06", "EderTsogal", bShow=bOn, bLoad=bOn, matPos=pos2, bAttach=bAttachOn, soAvatar=av)
    CloneObject.Clone2("RTOmniLight07", "EderTsogal", bShow=bOn, bLoad=bOn, matPos=pos6, bAttach=bAttachOn, soAvatar=av)
    CloneObject.Clone2("RTOmniLight09", "EderTsogal", bShow=bOn, bLoad=bOn, matPos=pos3, bAttach=bAttachOn, soAvatar=av)
    CloneObject.Clone2("RTOmniLightFountain", "EderTsogal", bShow=bOn, bLoad=bOn, matPos=pos4, bAttach=bAttachOn, soAvatar=av)
    CloneObject.Clone2("RTProjDirLight03", "Payiferen", bShow=bOn, bLoad=bOn, matPos=pos5, bAttach=bAttachOn, soAvatar=av)
    CloneObject.Clone2("RTProjDirLight02", "Payiferen", bShow=bOn, bLoad=bOn, matPos=pos6, bAttach=bAttachOn, soAvatar=av)

#
def LightForKveer2(av, num=1, bLoadShowOn=True, bAttachOn=False):
    bOn = bLoadShowOn
    """
    pos1 = ptMatrix44()
    pos2 = ptMatrix44()
    pos3 = ptMatrix44()
    pos4 = ptMatrix44()
    """
    """
    tuplePos1 = ((-0.999985933304, -0.00528157455847, 0.0, -0.273455888033), (0.00528157455847, -0.999985933304, 0.0, -47.5185241699), (0.0, 0.0, 1.0, 9.40436553955), (0.0, 0.0, 0.0, 1.0))
    tuplePos2 = ((-0.999986410141, -0.00528157642111, 0.0, -0.273455888033), (0.00528157642111, -0.999986410141, 0.0, -47.5185241699), (0.0, 0.0, 1.0, 48.0664749146), (0.0, 0.0, 0.0, 1.0))
    tuplePos3 = ((0.999998033047, 0.00198203604668, 0.0, 0.119770005345), (-0.00198203604668, 0.999998033047, 0.0, 3.88968443871), (0.0, 0.0, 1.0, 49.4459877014), (0.0, 0.0, 0.0, 1.0))
    tuplePos4 = ((-0.999917268753, -0.0128562794998, 0.0, -0.539468109608), (0.0128562794998, -0.999917268753, 0.0, -71.0015563965), (0.0, 0.0, 1.0, 9.40436553955), (0.0, 0.0, 0.0, 1.0))
    """
    """
    tuplePos1 = ((-1.0, 0.0, 0.0, 0.0), (0.0, -1.0, 0.0, -50.0), (0.0, 0.0, 1.0, 10.0), (0.0, 0.0, 0.0, 1.0))
    tuplePos2 = ((-1.0, 0.0, 0.0, 0.0), (0.0, -1.0, 0.0, -50.0), (0.0, 0.0, 1.0, 50.0), (0.0, 0.0, 0.0, 1.0))
    tuplePos3 = ((1.0, 0.0, 0.0, 0.0), (0.0, 1.0, 0.0, 5.0), (0.0, 0.0, 1.0, 50.0), (0.0, 0.0, 0.0, 1.0))
    tuplePos4 = ((-1.0, 0.0, 0.0, 0.0), (0.0, -1.0, 0.0, -70.0), (0.0, 0.0, 1.0, 10.0), (0.0, 0.0, 0.0, 1.0))
    
    pos1.setData(tuplePos1)
    pos2.setData(tuplePos2)
    pos3.setData(tuplePos3)
    pos4.setData(tuplePos4)
    """
    
    #av = PtGetLocalAvatar()
    #pos = PtGetLocalAvatar().getLocalToWorld()
    pos = av.getLocalToWorld()
    
    pos1 = pos
    pos2 = pos
    pos3 = pos
    pos4 = pos
    pos2.translate(ptVector3(0.0, 0.0, 40.0))
    pos3.translate(ptVector3(0.0, 55.0, 40.0))
    pos4.translate(ptVector3(0.0, -20.0, 0.0))
    
    mRot = ptMatrix44()
    mRot.rotate(2, (math.pi * float(180.0)) / 180)
    pos1 = pos1 * mRot
    pos2 = pos2 * mRot
    pos4 = pos4 * mRot
    
    
    mRot = ptMatrix44()
    mRot.rotate(0, (math.pi * float(90.0)) / 180)
    pos6 = pos4 * mRot
    
    mRot = ptMatrix44()
    mRot.rotate(0, (math.pi * float(45.0)) / 180)
    pos5 = pos3 * mRot
    """
    if num == 1:
        CloneObject.Clone2("RTOmniLight03", "EderTsogal", bShow=bOn, bLoad=bOn, matPos=pos1, bAttach=bAttachOn, soAvatar=av)
    elif num == 2:
        CloneObject.Clone2("RTOmniLight04", "EderTsogal", bShow=bOn, bLoad=bOn, matPos=pos5, bAttach=bAttachOn, soAvatar=av)
    elif num == 3:
        CloneObject.Clone2("RTOmniLight05", "EderTsogal", bShow=bOn, bLoad=bOn, matPos=pos6, bAttach=bAttachOn, soAvatar=av)
    elif num == 4:
        CloneObject.Clone2("RTOmniLight06", "EderTsogal", bShow=bOn, bLoad=bOn, matPos=pos2, bAttach=bAttachOn, soAvatar=av)
    elif num == 5:
        CloneObject.Clone2("RTOmniLight07", "EderTsogal", bShow=bOn, bLoad=bOn, matPos=pos6, bAttach=bAttachOn, soAvatar=av)
    elif num == 6:
        CloneObject.Clone2("RTOmniLight09", "EderTsogal", bShow=bOn, bLoad=bOn, matPos=pos3, bAttach=bAttachOn, soAvatar=av)
    elif num == 7:
        CloneObject.Clone2("RTOmniLightFountain", "EderTsogal", bShow=bOn, bLoad=bOn, matPos=pos4, bAttach=bAttachOn, soAvatar=av)
    elif num == 8:
        CloneObject.Clone2("RTProjDirLight03", "Payiferen", bShow=bOn, bLoad=bOn, matPos=pos5, bAttach=bAttachOn, soAvatar=av)
    elif num == 9:
        CloneObject.Clone2("RTProjDirLight02", "Payiferen", bShow=bOn, bLoad=bOn, matPos=pos6, bAttach=bAttachOn, soAvatar=av)
    """
    if num == 1:
        CloneObject.Clone2("RTOmniLight03", "EderTsogal", bShow=bOn, bLoad=bOn, matPos=pos, bAttach=bAttachOn, soAvatar=av)
    elif num == 2:
        CloneObject.Clone2("RTOmniLight04", "EderTsogal", bShow=bOn, bLoad=bOn, matPos=pos, bAttach=bAttachOn, soAvatar=av)
    elif num == 3:
        CloneObject.Clone2("RTOmniLight05", "EderTsogal", bShow=bOn, bLoad=bOn, matPos=pos, bAttach=bAttachOn, soAvatar=av)
    elif num == 4:
        CloneObject.Clone2("RTOmniLight06", "EderTsogal", bShow=bOn, bLoad=bOn, matPos=pos, bAttach=bAttachOn, soAvatar=av)
    elif num == 5:
        CloneObject.Clone2("RTOmniLight07", "EderTsogal", bShow=bOn, bLoad=bOn, matPos=pos, bAttach=bAttachOn, soAvatar=av)
    elif num == 6:
        CloneObject.Clone2("RTOmniLight09", "EderTsogal", bShow=bOn, bLoad=bOn, matPos=pos, bAttach=bAttachOn, soAvatar=av)
    elif num == 7:
        CloneObject.Clone2("RTOmniLightFountain", "EderTsogal", bShow=bOn, bLoad=bOn, matPos=pos, bAttach=bAttachOn, soAvatar=av)
    elif num == 8:
        CloneObject.Clone2("RTProjDirLight03", "Payiferen", bShow=bOn, bLoad=bOn, matPos=pos, bAttach=bAttachOn, soAvatar=av)
    elif num == 9:
        CloneObject.Clone2("RTProjDirLight02", "Payiferen", bShow=bOn, bLoad=bOn, matPos=pos, bAttach=bAttachOn, soAvatar=av)

#
def LightForJalak(av, num=1, bLoadShowOn=True, bAttachOn=False, dx=0, dy=0, dz=0, rx=0, ry=0, rz=0):
    bOn = bLoadShowOn
    pos = av.getLocalToWorld()
    
    pos1 = pos
    pos2 = pos
    pos3 = pos
    pos4 = pos
    
    pos1.translate(ptVector3(dx, dy, dz))
    
    mRot = ptMatrix44()
    mRot.rotate(0, (math.pi * rx) / 180)
    mRot.rotate(1, (math.pi * ry) / 180)
    mRot.rotate(2, (math.pi * rz) / 180)
    
    pos1 = pos1 * mRot
    
    if num == 1:
        CloneObject.Clone2("RTOmniLight03", "EderTsogal", bShow=bOn, bLoad=bOn, matPos=pos1, bAttach=bAttachOn, soAvatar=av)
    elif num == 2:
        CloneObject.Clone2("RTOmniLight04", "EderTsogal", bShow=bOn, bLoad=bOn, matPos=pos1, bAttach=bAttachOn, soAvatar=av)
    elif num == 3:
        CloneObject.Clone2("RTOmniLight09", "EderTsogal", bShow=bOn, bLoad=bOn, matPos=pos1, bAttach=bAttachOn, soAvatar=av)
    elif num == 4:
        CloneObject.Clone2("RTOmniLightFountain", "EderTsogal", bShow=bOn, bLoad=bOn, matPos=pos1, bAttach=bAttachOn, soAvatar=av)
    elif num == 5:
        CloneObject.Clone2("RTProjDirLight01", "Jalak", bShow=bOn, bLoad=bOn, matPos=pos1, bAttach=bAttachOn, soAvatar=av)
    elif num == 6:
        CloneObject.Clone2("RTOmniLightBluAmbient", "Jalak", bShow=bOn, bLoad=bOn, matPos=pos1, bAttach=bAttachOn, soAvatar=av)

"""
E:\MystOnLineUruLiveAgain\PlClient_TEST\Python\plasma
def PtSetLightValue(key,name,r,g,b,a):
    ''' Key is the key of scene object host to light. Name is the name of the light to manipulate'''
    pass
"""

#
def YeeshaGlowLight(av, bLoadShowOn=True, bAttachOn=False, dx=0, dy=0, dz=4, rx=0, ry=0, rz=0, cr=1, cg=1, cb=1, ca=1):
    bOn = bLoadShowOn
    pos = av.getLocalToWorld()
    pos1 = pos
    pos1.translate(ptVector3(dx, dy, dz))
    mRot = ptMatrix44()
    mRot.rotate(0, (math.pi * rx) / 180)
    mRot.rotate(1, (math.pi * ry) / 180)
    mRot.rotate(2, (math.pi * rz) / 180)
    pos1 = pos1 * mRot
    CloneObject.Clone2(objName="RTGlowLight", age="CustomAvatars", bShow=bOn, bLoad=bOn, matPos=pos1, bAttach=bAttachOn, soAvatar=av)
    mso = PtFindSceneobject("RTGlowLight", "CustomAvatars")
    cloneKeys = PtFindClones(mso.getKey())
    if len(cloneKeys) > 0:
        ck = cloneKeys[0]
        PtSetLightValue(key=ck, name="RTGlowLight", r=cr, g=cg, b=cb, a=ca)

# Commande speciale pour un evenement particulier
def SpecialEventCommand(self, cFlags, args = []):
    myself = PtGetLocalPlayer()
    player = args[0]
    if not isPlayerInAge(player):
        SendChatMessage(self, myself, [player], "You must be in my age, use link to join me.", cFlags.flags)
        return 1
    bOn = True
    bOff = False
    onOff = "on"
    eventNumber = 1
    if len(args) > 1:
        params = args[1].split()
        if len(params) > 0:
            try:
                eventNumber = int(params[0])
            except:
                SendChatMessage(self, myself, [player], "The parameter must be an integer.", cFlags.flags)
                return 0
        if len(params) > 1:
            if params[1] == "off":
                bOn = False
                bOff = True
                onOff = "off"

    try:
        xBotAge.DisablePanicLinks()
        """
        if eventNumber == 1:
            # -- 1 -- Magic Relto Cleft et Kveer + clone de Minkata + nuit
            print "==> event 1"
            xBotAge.ToggleSceneObjects("Blocker", age = "Cleft", bDrawOn = bOn, bPhysicsOn = bOff)
            xBotAge.ToggleSceneObjects("ProxyPropertyLine", age = "Cleft", bDrawOn = bOn, bPhysicsOn = bOff)
            xBotAge.ToggleSceneObjects("Sky", age=None, bDrawOn=bOff, bPhysicsOn=True)
            xBotAge.ToggleSceneObjects("sky", age=None, bDrawOn=bOff, bPhysicsOn=True)
            xBotAge.ToggleSceneObjects("Dome", age=None, bDrawOn=bOff, bPhysicsOn=True)
            xBotAge.ToggleSceneObjects("Mountain", age=None, bDrawOn=bOff, bPhysicsOn=True)
            xBotAge.ToggleSceneObjects("nb01", age = "Kveer", bDrawOn = bOff, bPhysicsOn = bOn)
            CloneObject.Minkata(bShow=bOn, bLoad=bOn)
            CreateReltoNight1(self, cFlags, [args[0], onOff])
        """
        if eventNumber == 1:
            # -- 1 -- A Cleft avec ZandiMobile + clone de Minkata + nuit
            print("==> event 1")
            xBotAge.ToggleSceneObjects("Blocker", age = "Cleft", bDrawOn = bOn, bPhysicsOn = bOff)
            xBotAge.ToggleSceneObjects("ProxyPropertyLine", age = "Cleft", bDrawOn = bOn, bPhysicsOn = bOff)
            xBotAge.ToggleSceneObjects("Sky", age=None, bDrawOn=bOff, bPhysicsOn=True)
            xBotAge.ToggleSceneObjects("sky", age=None, bDrawOn=bOff, bPhysicsOn=True)
            xBotAge.ToggleSceneObjects("Dome", age=None, bDrawOn=bOff, bPhysicsOn=True)
            xBotAge.ToggleSceneObjects("Mountain", age=None, bDrawOn=bOff, bPhysicsOn=True)
            xBotAge.ToggleSceneObjects("nb01", age = "Kveer", bDrawOn = bOff, bPhysicsOn = bOn)
            CloneObject.Minkata(bShow=bOn, bLoad=bOn)
            #CloneObject.co3("ZandiMobileRegion", "Cleft", bShow=bOn, bLoad=bOn)
            mat = ptMatrix44()
            tupMat = ((1.0,0.0,0.0,381.0),(0.0,1.0,0.0,74.0),(0.0,0.0,1.0,31.0),(0.0,0.0,0.0,1.0))
            mat.setData(tupMat)
            #CloneObject.co3("C01_Root", "Dereno", bShow=bOn, bLoad=bOn, scale=5, matPos=mat)
            #CloneObject.co3("FishAClockwise", "Dereno", bShow=bOn, bLoad=bOn, scale=5, matPos=mat)
            CloneObject.co3("Basket01", "Gira", bShow=bOn, bLoad=bOn, scale=1, matPos=mat)
            #CloneObject.co3("LavaRiverEdge ", "Gira", bShow=bOn, bLoad=bOn, scale=5, matPos=mat)
            tupMat = ((1.0,0.0,0.0,381.0),(0.0,1.0,0.0,74.0),(0.0,0.0,1.0,41.0),(0.0,0.0,0.0,1.0))
            mat.setData(tupMat)
            CloneObject.co3("Basket02", "Gira", bShow=bOn, bLoad=bOn, scale=1, matPos=mat)
            tupMat = ((1.0,0.0,0.0,381.0),(0.0,1.0,0.0,74.0),(0.0,0.0,1.0,51.0),(0.0,0.0,0.0,1.0))
            mat.setData(tupMat)
            CloneObject.co3("Basket03", "Gira", bShow=bOn, bLoad=bOn, scale=1, matPos=mat)
            CreateReltoNight1(self, cFlags, [args[0], onOff])
            SendChatMessage(self, myself, [player], "Event 1 (Free Cleft night) is {0}".format(onOff), cFlags.flags)
        elif eventNumber == 2:
            # -- 2 -- Hood + nuit + clone de SandscritRoot
            print("==> event 2")
            xBotAge.ToggleSceneObjects("Sky", age=None, bDrawOn=bOff, bPhysicsOn=True)
            xBotAge.ToggleSceneObjects("sky", age=None, bDrawOn=bOff, bPhysicsOn=True)
            xBotAge.ToggleSceneObjects("Dome", age=None, bDrawOn=bOff, bPhysicsOn=True)
            xBotAge.ToggleSceneObjects("Mountain", age=None, bDrawOn=bOff, bPhysicsOn=True)
            print("==> Minkata ground")
            CloneObject.Minkata(bShow=bOn, bLoad=bOn)
            print("==> GT sky")
            #CloneObject.co(["SphereEnviron", "SphereClouds"], "GreatTreePub", 1, bShow=bOn, bLoad=bOn)
            CloneObject.co(["SphereEnviron"], "GreatTreePub", 1, bShow=bOn, bLoad=bOn)
            # mettre l'Arche devant le Pod:
            print("==> Arch")
            #tupMat = ((-0.762557864189,-0.646920084953,0.0,30.8849506378),(0.646920084953,-0.762557864189,0.0,-12.7307682037),(0.0,0.0,1.0,-0.0328427329659),(0.0,0.0,0.0,1.0))
            tupMat = ((-0.541980564594,0.840391099453,0.0,86.2719726562),(-0.840391099453,-0.541980564594,0.0,82.5392074585),(0.0,0.0,1.0,-21.8916854858),(0.0,0.0,0.0,1.0))
            #print "==> Arch 2"
            mat = ptMatrix44()
            #print "==> Arch 3"
            mat.setData(tupMat)
            #print "==> Arch 4"
            CloneObject.co3("ArchOfKerath", "city", bShow=bOn, bLoad=bOn, scale=.2, matPos=mat)
            # mettre le sandscrit dans le Pod:
            print("==> Sandscrit")
            tupMat = ((-0.275523930788,-0.961294174194,0.0,15.0463008881),(0.961294174194,-0.275523930788,0.0,3.88983178139),(0.0,0.0,1.0,2.06506371498),(0.0,0.0,0.0,1.0))
            mat = ptMatrix44()
            mat.setData(tupMat)
            #SandscritRoot
            #SandscritFlipper
            #Sandscrit_Mover
            CloneObject.co3("SandscritRoot", "Payiferen", bShow=bOn, bLoad=bOn, scale=0.2, matPos=mat)
            #CloneObject.co3("Sandscrit_Mover", "Payiferen", bShow=bOn, bLoad=bOn, scale=0.2, matPos=mat)
            print("==> nuit")
            if onOff == "on":
                CreateReltoNight1(self, cFlags, [args[0], 60])
            else:
                CreateReltoNight1(self, cFlags, [args[0], onOff])
            SendChatMessage(self, myself, [player], "Event 2 (Payiferen/GreatTreePub/ArchOfKerath) is {0}".format(onOff), cFlags.flags)
        elif eventNumber == 3:
            # -- 3 -- 
            print("==> event 3")
            xBotAge.ToggleSceneObjects("Sky", age=None, bDrawOn=bOff, bPhysicsOn=True)
            xBotAge.ToggleSceneObjects("sky", age=None, bDrawOn=bOff, bPhysicsOn=True)
            xBotAge.ToggleSceneObjects("Dome", age=None, bDrawOn=bOff, bPhysicsOn=True)
            xBotAge.ToggleSceneObjects("Mountain", age=None, bDrawOn=bOff, bPhysicsOn=True)
            print("==> Minkata ground")
            CloneObject.Minkata(bShow=bOn, bLoad=bOn)
            print("==> 2 Tails Monkey")
            tupMat = ((-0.275523930788,-0.961294174194,0.0,15.0),(0.961294174194,-0.275523930788,0.0,3.9),(0.0,0.0,1.0,11.5),(0.0,0.0,0.0,1.0))
            mat = ptMatrix44()
            mat.setData(tupMat)
            #CloneObject.co3("2Tails_Root", "Negilahn", bShow=bOn, bLoad=bOn, scale=0.2, matPos=mat)
            #CloneObject.co3("TempMonkeyHandle", "Negilahn", bShow=bOn, bLoad=bOn, scale=5)
            CloneObject.co3("TempMonkeyHandle", "Negilahn", bShow=bOn, bLoad=bOn, scale=5, matPos=mat)
            SendChatMessage(self, myself, [player], "Event 3 (Negilahn) is {0}".format(onOff), cFlags.flags)
        elif eventNumber == 4:
            # -- 4 -- 
            print("==> event 4")
            """
            print "==> Cleft Desert Ground Plane"
            #tupMat = ((-0.275523930788,-0.961294174194,0.0,15.0),(0.961294174194,-0.275523930788,0.0,3.9),(0.0,0.0,1.0,11.5),(0.0,0.0,0.0,1.0))
            #mat = ptMatrix44()
            #mat.setData(tupMat)
            #CloneObject.co3("DesertPlane", "Cleft", bShow=bOn, bLoad=bOn, scale=0.2, matPos=mat)
            CloneObject.co3("DesertPlane", "Cleft", bShow=bOn, bLoad=bOn)
            CloneObject.co3("DesertPlanDecal1", "Cleft", bShow=bOn, bLoad=bOn)
            CloneObject.co3("DesertPlainDecal2", "Cleft", bShow=bOn, bLoad=bOn)
            CloneObject.co3("DesertPlainDecal3", "Cleft", bShow=bOn, bLoad=bOn)
            CloneObject.co3("DesertPlainDecal4", "Cleft", bShow=bOn, bLoad=bOn)
            CloneObject.co3("DesertPlane1", "Cleft", bShow=bOn, bLoad=bOn)
            CloneObject.co3("DesertPlane2", "Cleft", bShow=bOn, bLoad=bOn)
            CloneObject.co3("DesertPlane3", "Cleft", bShow=bOn, bLoad=bOn)
            CloneObject.co3("DesertPlane4", "Cleft", bShow=bOn, bLoad=bOn)
            #CloneObject.co3("DesertPlane", "Cleft", bShow=bOn, bLoad=bOn, scale=5, matPos=mat)
            print "==> Jalak Rect0"
            CloneObject.co3("Rect0", "Jalak", bShow=bOn, bLoad=bOn)
            """
            
            xBotAge.ToggleSceneObjects("Sky", age=None, bDrawOn=bOff, bPhysicsOn=True)
            xBotAge.ToggleSceneObjects("sky", age=None, bDrawOn=bOff, bPhysicsOn=True)
            xBotAge.ToggleSceneObjects("Dome", age=None, bDrawOn=bOff, bPhysicsOn=True)
            xBotAge.ToggleSceneObjects("Mountain", age=None, bDrawOn=bOff, bPhysicsOn=True)
            print("==> Gira sky")
            CloneObject.co3("SunDummyNew", "Gira", bShow=bOn, bLoad=bOn)
            CloneObject.co3("Sky", "Gira", bShow=bOn, bLoad=bOn)
            
            #
            if onOff == "on":
                SkyOnOff(self, cFlags, [args[0], "off"])
                FogOnOff(self, cFlags, [args[0], "off"])
            else:
                SkyOnOff(self, cFlags, [args[0], "on"])
                FogOnOff(self, cFlags, [args[0], "on"])
            SendChatMessage(self, myself, [player], "Event 4 (Gira sky) is {0}".format(onOff), cFlags.flags)
        elif eventNumber == 5:
            # -- 5 -- 
            print("==> event 5")
            xBotAge.ToggleSceneObjects("Sky", age=None, bDrawOn=bOff, bPhysicsOn=True)
            xBotAge.ToggleSceneObjects("sky", age=None, bDrawOn=bOff, bPhysicsOn=True)
            xBotAge.ToggleSceneObjects("Dome", age=None, bDrawOn=bOff, bPhysicsOn=True)
            xBotAge.ToggleSceneObjects("Mountain", age=None, bDrawOn=bOff, bPhysicsOn=True)
            #xBotAge.ToggleSceneObjects("Cloud", age=None, bDrawOn=bOff, bPhysicsOn=True)
            xBotAge.ToggleSceneObjects("Back", age=None, bDrawOn=bOff, bPhysicsOn=True)
            xBotAge.ToggleSceneObjects("Fog", age=None, bDrawOn=bOff, bPhysicsOn=True)
            xBotAge.ToggleSceneObjects("Sphere", age=None, bDrawOn=bOff, bPhysicsOn=True)
            xBotAge.ToggleSceneObjects("Dust", age=None, bDrawOn=bOff, bPhysicsOn=True)
            xBotAge.ToggleSceneObjects("Pod", age=None, bDrawOn=bOff, bPhysicsOn=True)
            xBotAge.ToggleSceneObjects("Rain", age=None, bDrawOn=bOff, bPhysicsOn=True)
            print("==> Gira sky")
            CloneObject.co3("SkyGlobe", "Payiferen", bShow=bOn, bLoad=bOn)
            CloneObject.co3("StarSphere", "Payiferen", bShow=bOn, bLoad=bOn)
            SendChatMessage(self, myself, [player], "Event 5 (Payiferen sky) is {0}".format(onOff), cFlags.flags)
        elif eventNumber == 6:
            # -- 6 -- 
            print("==> event 6")
            xBotAge.ToggleSceneObjects("Sky", age=None, bDrawOn=bOff, bPhysicsOn=True)
            xBotAge.ToggleSceneObjects("sky", age=None, bDrawOn=bOff, bPhysicsOn=True)
            xBotAge.ToggleSceneObjects("Dome", age=None, bDrawOn=bOff, bPhysicsOn=True)
            xBotAge.ToggleSceneObjects("Mountain", age=None, bDrawOn=bOff, bPhysicsOn=True)
            #xBotAge.ToggleSceneObjects("Cloud", age=None, bDrawOn=bOff, bPhysicsOn=True)
            xBotAge.ToggleSceneObjects("Back", age=None, bDrawOn=bOff, bPhysicsOn=True)
            xBotAge.ToggleSceneObjects("Fog", age=None, bDrawOn=bOff, bPhysicsOn=True)
            xBotAge.ToggleSceneObjects("Sphere", age=None, bDrawOn=bOff, bPhysicsOn=True)
            xBotAge.ToggleSceneObjects("Dust", age=None, bDrawOn=bOff, bPhysicsOn=True)
            xBotAge.ToggleSceneObjects("Pod", age=None, bDrawOn=bOff, bPhysicsOn=True)
            xBotAge.ToggleSceneObjects("Rain", age=None, bDrawOn=bOff, bPhysicsOn=True)
            print("==> Dereno fish C01")
            CloneObject.co3("C01_Root", "Dereno", bShow=bOn, bLoad=bOn)
            SendChatMessage(self, myself, [player], "Event 6 (Dereno) is {0}".format(onOff), cFlags.flags)
        elif eventNumber == 7:
            # -- 7 -- 
            print("==> event 7")
            """
            !toggle Wheel  0 0
            !toggle Horizon  0 0
            
            //nosky
            //skycolor 10 75 85
            //fogshape 400 1000 10
            //fogcolor 10 75 85
            """
            CloneObject.co3("SkyDome", "Minkata", bShow=bOn, bLoad=bOn)
            #CloneObject.co3("SkyHighStormy", "Personal", bShow=bOn, bLoad=bOn, scale=1, matPos=None)
            xBotAge.ToggleSceneObjects("Clock", age = None, bDrawOn = bOff, bPhysicsOn = bOff)
            xBotAge.ToggleSceneObjects("Wheel", age = None, bDrawOn = bOff, bPhysicsOn = bOff)
            xBotAge.ToggleSceneObjects("Horizon", age = None, bDrawOn = bOff, bPhysicsOn = bOff)
            xBotAge.ToggleSceneObjects("PoolSurfaceInnerFake", age = None, bDrawOn = bOff, bPhysicsOn = bOff)
            if onOff == "on":
                SkyOnOff(self, cFlags, [args[0], "off"])
                FogOnOff(self, cFlags, [args[0], "off"])
                #skycolor:
                #xBotAge.SetRenderer(style = None, cr = 0.10, cg = 0.75, cb = 0.85)
                xBotAge.SetRenderer(style = None, cr = 0.00, cg = 0.80, cb = 0.90)
                #fogshape:
                xBotAge.SetRenderer(style = None, start = 400, end = 1000, density = 10)
                #fogcolor:
                #xBotAge.SetRenderer(style = None, r = 0.10, g = 0.75, b = 0.85)
                xBotAge.SetRenderer(style = None, r = 0.13, g = 0.71, b = 0.80)
            else:
                SkyOnOff(self, cFlags, [args[0], "on"])
                FogOnOff(self, cFlags, [args[0], "on"])
                #style:
                xBotAge.SetRenderer(style = "default")
            SendChatMessage(self, myself, [player], "Event 7 (Caribbean) is {0}".format(onOff), cFlags.flags)
        elif eventNumber == 8:
            # -- 8 -- 
            print("==> event 8 : City, Kahlo Pub, Memorial, Gerbes")
            #xBotAge.ToggleSceneObjects("Crack", age = None, bDrawOn = bOff, bPhysicsOn = bOff)
            xBotAge.ToggleSceneObjects("Curtain", age = None, bDrawOn = False, bPhysicsOn = False)
            xBotAge.ToggleSceneObjects("Debri", age = None, bDrawOn = bOff, bPhysicsOn = bOff)
            xBotAge.ToggleSceneObjects("Floor", age = None, bDrawOn = True, bPhysicsOn = True)
            xBotAge.ToggleSceneObjects("Floral", age = None, bDrawOn = bOn, bPhysicsOn = False)
            xBotAge.ToggleSceneObjects("Flower", age = None, bDrawOn = bOn, bPhysicsOn = False)
            xBotAge.ToggleSceneObjects("Rose", age = None, bDrawOn = bOn, bPhysicsOn = False)
            #xBotAge.ToggleSceneObjects("*Rub*", age = None, bDrawOn = bOff, bPhysicsOn = bOff)
            xBotAge.ToggleSceneObjects("Rub", age = None, bDrawOn = bOff, bPhysicsOn = bOff)
            xBotAge.ToggleSceneObjects("Rubble", age = None, bDrawOn = bOn, bPhysicsOn = bOff)
            xBotAge.ToggleSceneObjects("wreat", age = None, bDrawOn = bOn, bPhysicsOn = False)
            xBotAge.ToggleSceneObjects("Wreat", age = None, bDrawOn = bOn, bPhysicsOn = False)
            #xBotAge.ToggleSceneObjects("Wreath", age = None, bDrawOn = bOn, bPhysicsOn = false)
            SendChatMessage(self, myself, [player], "Event 8 (Memorial) is {0}".format(onOff), cFlags.flags)
        elif eventNumber == 9:
            # -- 9 -- 
            print("==> event 9 : K'veer, Lights for NULP Dance Show")
            #CloneObject.co3("RTDirLightCoolDesertFill", "Minkata", bShow=bOn, bLoad=bOn, scale=1, matPos=None)
            soPlayer = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
            LightForKveer(av=soPlayer, bLoadShowOn=bOn, bAttachOn=bOn)
            SendChatMessage(self, myself, [player], "Event 9 (Projectors) is {0}".format(onOff), cFlags.flags)
        elif eventNumber == 10:
            # -- 10 -- 
            """
            print "==> event 10 : K'veer, Lights for NULP Dance Show"
            soPlayer = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
            LightForKveer2(av=soPlayer, num=1, bLoadShowOn=bOn, bAttachOn=bOn)
            LightForKveer2(av=soPlayer, num=2, bLoadShowOn=bOn, bAttachOn=bOn)
            LightForKveer2(av=soPlayer, num=3, bLoadShowOn=bOn, bAttachOn=bOn)
            LightForKveer2(av=soPlayer, num=4, bLoadShowOn=bOn, bAttachOn=bOn)
            LightForKveer2(av=soPlayer, num=5, bLoadShowOn=bOn, bAttachOn=bOn)
            LightForKveer2(av=soPlayer, num=6, bLoadShowOn=bOn, bAttachOn=bOn)
            LightForKveer2(av=soPlayer, num=7, bLoadShowOn=bOn, bAttachOn=bOn)
            LightForKveer2(av=soPlayer, num=8, bLoadShowOn=bOn, bAttachOn=bOn)
            LightForKveer2(av=soPlayer, num=9, bLoadShowOn=bOn, bAttachOn=bOn)
            """
            print("==> event 10 : Jalak, Lights for NULP Dance Show")
            soPlayer = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
            LightForJalak(av=soPlayer, num=1, bLoadShowOn=bOn, bAttachOn=bOn, dx=0, dy=0, dz=0, rx=180, ry=0, rz=0)
            LightForJalak(av=soPlayer, num=2, bLoadShowOn=bOn, bAttachOn=bOn, dx=0, dy=0, dz=0, rx=0, ry=0, rz=0)
            LightForJalak(av=soPlayer, num=3, bLoadShowOn=bOn, bAttachOn=bOn, dx=0, dy=0, dz=0, rx=180, ry=0, rz=180)
            LightForJalak(av=soPlayer, num=4, bLoadShowOn=bOn, bAttachOn=bOn, dx=0, dy=0, dz=0, rx=180, ry=180, rz=0)
            #LightForJalak(av=soPlayer, num=5, bLoadShowOn=bOn, bAttachOn=bOn, dx=0, dy=-100, dz=100, rx=-90, ry=-20, rz=0)
            LightForJalak(av=soPlayer, num=5, bLoadShowOn=bOn, bAttachOn=False, dx=0, dy=-40, dz=20, rx=-30, ry=0, rz=0)
            LightForJalak(av=soPlayer, num=6, bLoadShowOn=bOn, bAttachOn=bOn, dx=100, dy=100, dz=100, rx=0, ry=0, rz=0)
            SendChatMessage(self, myself, [player], "Event 10 (Projectors) is {0}".format(onOff), cFlags.flags)
        elif eventNumber == 91:
            # -- 91 -- 
            print("==> event 91 : K'veer, Lights for NULP Dance Show")
            soPlayer = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
            LightForKveer2(av=soPlayer, num=1, bLoadShowOn=bOn, bAttachOn=bOn)
            SendChatMessage(self, myself, [player], "Event 91 (Projectors) is {0}".format(onOff), cFlags.flags)
        elif eventNumber == 92:
            # -- 92 -- 
            print("==> event 92 : K'veer, Lights for NULP Dance Show")
            soPlayer = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
            LightForKveer2(av=soPlayer, num=2, bLoadShowOn=bOn, bAttachOn=bOn)
            SendChatMessage(self, myself, [player], "Event 92 (Projectors) is {0}".format(onOff), cFlags.flags)
        elif eventNumber == 93:
            # -- 93 -- 
            print("==> event 93 : K'veer, Lights for NULP Dance Show")
            soPlayer = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
            LightForKveer2(av=soPlayer, num=3, bLoadShowOn=bOn, bAttachOn=bOn)
            SendChatMessage(self, myself, [player], "Event 93 (Projectors) is {0}".format(onOff), cFlags.flags)
        elif eventNumber == 94:
            # -- 94 -- 
            print("==> event 94 : K'veer, Lights for NULP Dance Show")
            soPlayer = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
            LightForKveer2(av=soPlayer, num=4, bLoadShowOn=bOn, bAttachOn=bOn)
            SendChatMessage(self, myself, [player], "Event 94 (Projectors) is {0}".format(onOff), cFlags.flags)
        elif eventNumber == 95:
            # -- 95 -- 
            print("==> event 95 : K'veer, Lights for NULP Dance Show")
            soPlayer = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
            LightForKveer2(av=soPlayer, num=5, bLoadShowOn=bOn, bAttachOn=bOn)
            SendChatMessage(self, myself, [player], "Event 95 (Projectors) is {0}".format(onOff), cFlags.flags)
        elif eventNumber == 96:
            # -- 96 -- 
            print("==> event 96 : K'veer, Lights for NULP Dance Show")
            soPlayer = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
            LightForKveer2(av=soPlayer, num=6, bLoadShowOn=bOn, bAttachOn=bOn)
            SendChatMessage(self, myself, [player], "Event 96 (Projectors) is {0}".format(onOff), cFlags.flags)
        elif eventNumber == 97:
            # -- 97 -- 
            print("==> event 97 : K'veer, Lights for NULP Dance Show")
            soPlayer = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
            LightForKveer2(av=soPlayer, num=7, bLoadShowOn=bOn, bAttachOn=bOn)
            SendChatMessage(self, myself, [player], "Event 97 (Projectors) is {0}".format(onOff), cFlags.flags)
        elif eventNumber == 98:
            # -- 98 -- 
            print("==> event 98 : K'veer, Lights for NULP Dance Show")
            soPlayer = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
            LightForKveer2(av=soPlayer, num=8, bLoadShowOn=bOn, bAttachOn=bOn)
            SendChatMessage(self, myself, [player], "Event 98 (Projectors) is {0}".format(onOff), cFlags.flags)
        elif eventNumber == 99:
            # -- 99 -- 
            print("==> event 99 : K'veer, Lights for NULP Dance Show")
            soPlayer = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
            LightForKveer2(av=soPlayer, num=9, bLoadShowOn=bOn, bAttachOn=bOn)
            SendChatMessage(self, myself, [player], "Event 99 (Projectors) is {0}".format(onOff), cFlags.flags)
        elif eventNumber == 11:
            # -- 11 -- 
            print("==> event 11 : Jalak Light for Mystitech")
            soPlayer = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
            LightForJalak(av=soPlayer, num=1, bLoadShowOn=bOn, bAttachOn=bOn, dx=0, dy=0, dz=0, rx=180, ry=0, rz=0)
            SendChatMessage(self, myself, [player], "Projector 1 is {0}".format(onOff), cFlags.flags)
        elif eventNumber == 12:
            # -- 12 -- 
            print("==> event 12 : Jalak Light for Mystitech")
            soPlayer = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
            LightForJalak(av=soPlayer, num=2, bLoadShowOn=bOn, bAttachOn=bOn, dx=0, dy=0, dz=0, rx=0, ry=0, rz=0)
            SendChatMessage(self, myself, [player], "Projector 2 is {0}".format(onOff), cFlags.flags)
        elif eventNumber == 13:
            # -- 13 -- 
            print("==> event 1 : Jalak Light for Mystitech")
            soPlayer = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
            LightForJalak(av=soPlayer, num=3, bLoadShowOn=bOn, bAttachOn=bOn, dx=0, dy=0, dz=0, rx=180, ry=0, rz=180)
            SendChatMessage(self, myself, [player], "Projector 3 is {0}".format(onOff), cFlags.flags)
        elif eventNumber == 14:
            # -- 14 -- 
            print("==> event 14 : Jalak Light for Mystitech")
            soPlayer = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
            LightForJalak(av=soPlayer, num=4, bLoadShowOn=bOn, bAttachOn=bOn, dx=0, dy=0, dz=0, rx=180, ry=180, rz=0)
            SendChatMessage(self, myself, [player], "Projector 4 is {0}".format(onOff), cFlags.flags)
        elif eventNumber == 15:
            # -- 15 -- 
            print("==> event 15 : Jalak Light for Mystitech")
            soPlayer = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
            LightForJalak(av=soPlayer, num=5, bLoadShowOn=bOn, bAttachOn=False, dx=0, dy=-40, dz=20, rx=-30, ry=0, rz=0)
            SendChatMessage(self, myself, [player], "Projector 5 is {0}".format(onOff), cFlags.flags)
        elif eventNumber == 16:
            # -- 16 -- 
            print("==> event 16 : Jalak Light for Mystitech")
            soPlayer = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
            LightForJalak(av=soPlayer, num=6, bLoadShowOn=bOn, bAttachOn=bOn, dx=100, dy=100, dz=100, rx=0, ry=0, rz=0)
            SendChatMessage(self, myself, [player], "Projector 6 is {0}".format(onOff), cFlags.flags)
        elif eventNumber == 17:
            # -- 17 -- 
            print("==> event 17 : Yeesha Glow Light (detached)")
            soPlayer = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
            YeeshaGlowLight(av=soPlayer, bLoadShowOn=bOn, bAttachOn=False, dx=0, dy=0, dz=4, rx=0, ry=0, rz=0, cr=1, cg=1, cb=1, ca=1)
            SendChatMessage(self, myself, [player], "Yeesha Glow Light is {0}".format(onOff), cFlags.flags)
        elif eventNumber == 170:
            # -- 170 -- 
            print("==> event 170 : Yeesha Glow Light (attached above you)")
            soPlayer = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
            YeeshaGlowLight(av=soPlayer, bLoadShowOn=bOn, bAttachOn=bOn, dx=0, dy=0, dz=9, rx=0, ry=0, rz=0, cr=1, cg=1, cb=1, ca=1)
            SendChatMessage(self, myself, [player], "Yeesha Glow Light (attached above you) is {0}".format(onOff), cFlags.flags)
        elif eventNumber == 171:
            # -- 171 -- 
            print("==> event 171 : Yeesha Glow Light (attached to your right)")
            soPlayer = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
            YeeshaGlowLight(av=soPlayer, bLoadShowOn=bOn, bAttachOn=bOn, dx=-5, dy=0, dz=9, rx=0, ry=0, rz=0, cr=1, cg=1, cb=1, ca=1)
            SendChatMessage(self, myself, [player], "Yeesha Glow Light (attached to your right) is {0}".format(onOff), cFlags.flags)
        elif eventNumber == 172:
            # -- 172 -- 
            print("==> event 172 : Yeesha Glow Light (attached to your left)")
            soPlayer = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
            YeeshaGlowLight(av=soPlayer, bLoadShowOn=bOn, bAttachOn=bOn, dx=5, dy=0, dz=9, rx=0, ry=0, rz=0, cr=1, cg=1, cb=1, ca=1)
            SendChatMessage(self, myself, [player], "Yeesha Glow Light(attached to your left) is {0}".format(onOff), cFlags.flags)
        elif eventNumber == 173:
            # -- 173 -- 
            print("==> event 173 : Yeesha Glow Light (attached in front of you)")
            soPlayer = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
            YeeshaGlowLight(av=soPlayer, bLoadShowOn=bOn, bAttachOn=bOn, dx=0, dy=-5, dz=9, rx=0, ry=0, rz=0, cr=1, cg=1, cb=1, ca=1)
            SendChatMessage(self, myself, [player], "Yeesha Glow Light (attached in front of you) is {0}".format(onOff), cFlags.flags)
        elif eventNumber == 174:
            # -- 174 -- 
            print("==> event 174 : Yeesha Glow Light (attached behind you)")
            soPlayer = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
            YeeshaGlowLight(av=soPlayer, bLoadShowOn=bOn, bAttachOn=bOn, dx=0, dy=5, dz=9, rx=0, ry=0, rz=0, cr=1, cg=1, cb=1, ca=1)
            SendChatMessage(self, myself, [player], "Yeesha Glow Light (attached behind you) is {0}".format(onOff), cFlags.flags)
        elif eventNumber == 18:
            # -- 18 -- 
            print("==> event 18 : City Museum Light")
            soPlayer = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
            tupMat = ((-0.131536126137,0.991311430931,0.0,-177.0),(-0.991311430931,-0.131536126137,0.0,5.6),(0.0,0.0,1.0,322.0),(0.0,0.0,0.0,1.0))
            mat = ptMatrix44()
            mat.setData(tupMat)
            mRot = ptMatrix44()
            mRot.rotate(0, (math.pi * 40.0) / 180)
            pos = mat * mRot
            CloneObject.Clone2("RTProjDirLight03", "Payiferen", bShow=bOn, bLoad=bOn, matPos=pos, bAttach=False, soAvatar=soPlayer)
        elif eventNumber == 19:
            # -- 19 -- 
            print("==> event 19 : City Stalagmite Light")
            soPlayer = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
            tupMat = ((0.00654011964798,0.999978721142,0.0,-0.41703543067),(-0.999978721142,0.00654011964798,0.0,-93.100189209),(0.0,0.0,1.0,294.695495605),(0.0,0.0,0.0,1.0))
            mat = ptMatrix44()
            mat.setData(tupMat)
            CloneObject.Clone2("RTProjDirLight03", "Payiferen", bShow=bOn, bLoad=bOn, matPos=mat, bAttach=False, soAvatar=soPlayer)
        elif eventNumber == 20:
            # -- 20 -- 
            print("==> event 20 : City Library Tent Light and fog")
            soPlayer = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
            tupMat = ((0.862352311611,0.506308674812,0.0,840.0),(-0.506308674812,0.862352311611,0.0,-543.0),(0.0,0.0,1.0,300.0),(0.0,0.0,0.0,1.0))
            mat = ptMatrix44()
            mat.setData(tupMat)
            CloneObject.Clone2("RTProjDirLight03", "Payiferen", bShow=bOn, bLoad=bOn, matPos=mat, bAttach=False, soAvatar=soPlayer)
            SetRendererFogColor(self, cFlags, [player, "yellow2"])
            if bOn:
                CreateReltoNight1(self, cFlags, [args[0], "off"])
            else:
                CreateReltoNight1(self, cFlags, [args[0], "on"])
        elif eventNumber == 21:
            # -- 21 -- 
            print("==> event 21 : Red Testsonot Pulsing Light")
            soPlayer = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
            pos = soPlayer.getLocalToWorld()
            CloneObject.Clone2("RTWindowOmni03", "Tetsonot", bShow=bOn, bLoad=bOn, matPos=pos, bAttach=bOn, soAvatar=soPlayer)
            SendChatMessage(self, myself, [player], "Event 21 (Red Testsonot Pulsing Light) is {0}".format(onOff), cFlags.flags)
        elif eventNumber == 22:
            # -- 22 -- 
            print("==> event 22 : White Kahlo Pulsing Light")
            soPlayer = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
            pos = soPlayer.getLocalToWorld()
            CloneObject.Clone2("kpRTOmniLight04", "city", bShow=bOn, bLoad=bOn, matPos=pos, bAttach=bOn, soAvatar=soPlayer)
            SendChatMessage(self, myself, [player], "Event 22 (White Kahlo Pulsing Light) is {0}".format(onOff), cFlags.flags)
        elif eventNumber == 23:
            # -- 23 -- 
            print("==> event 23 : Fog Test")
            soPlayer = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
            pos = soPlayer.getLocalToWorld()
            #Add 1 clone of each dusts planes of Minkata
            CloneObject.Clone2("DustPlaneParticle01", "Minkata", bShow=bOn, bLoad=bOn, matPos=pos, bAttach=bOn, soAvatar=soPlayer)
            CloneObject.Clone2("DustPlaneParticle02", "Minkata", bShow=bOn, bLoad=bOn, matPos=pos, bAttach=bOn, soAvatar=soPlayer)
            CloneObject.Clone2("DustPlaneParticle03", "Minkata", bShow=bOn, bLoad=bOn, matPos=pos, bAttach=bOn, soAvatar=soPlayer)
            CloneObject.Clone2("DustPlaneParticle04", "Minkata", bShow=bOn, bLoad=bOn, matPos=pos, bAttach=bOn, soAvatar=soPlayer)
            CloneObject.Clone2("DustPlaneParticle05", "Minkata", bShow=bOn, bLoad=bOn, matPos=pos, bAttach=bOn, soAvatar=soPlayer)
            CloneObject.Clone2("DustPlaneParticle06", "Minkata", bShow=bOn, bLoad=bOn, matPos=pos, bAttach=bOn, soAvatar=soPlayer)
            CloneObject.Clone2("DustPlaneParticle07", "Minkata", bShow=bOn, bLoad=bOn, matPos=pos, bAttach=bOn, soAvatar=soPlayer)
            #Add 1 clone of dust plane of Payiferen
            CloneObject.Clone2("DustPlaneParticle", "Payiferen", bShow=bOn, bLoad=bOn, matPos=pos, bAttach=bOn, soAvatar=soPlayer)
            if PtGetAgeInfo().getAgeFilename() != "Minkata":
                #Because the fog is automaticaly restored in Minkata
                xBotAge.SetRenderer(style=None, start=-40, end=500, density=1, r=0.60, g=0.50, b=0.36)
            if onOff == "on":
                SkyOnOff(self, cFlags, [args[0], "off"])
            else:
                SkyOnOff(self, cFlags, [args[0], "on"])
            SendChatMessage(self, myself, [player], "Event 23 (Fog Test) is {0}".format(onOff), cFlags.flags)
        elif eventNumber == 24:
            # -- 24 -- 
            print("==> event 24 : Bright golden mist in Er'cana.")
            #Er'cana : Brume dorée brillante.
            #//nosky (no juse the SkyDome and eventualy the Horizon in Er'cana)
            xBotAge.ToggleSceneObjects("SkyDome", age="Ercana", bDrawOn=bOff, bPhysicsOn=True)
            if onOff == "on":
                #SkyOnOff(self, cFlags, [args[0], "off"])
                #//skycolor gold 2
                SetRendererClearColor(self, cFlags, [player, "gold2"])
                #//fogshape -200 3000 2
                SetRendererFogLinear(self, cFlags, [player, "-200 3000 2"])
                #//fogcolor gold 2
                SetRendererFogColor(self, cFlags, [player, "gold2"])
            else:
                #SkyOnOff(self, cFlags, [args[0], "on"])
                SetRendererStyle(self, cFlags, [player, "default"])
            SendChatMessage(self, myself, [player], "Event 24 (Bright golden mist) is {0}".format(onOff), cFlags.flags)
        elif eventNumber == 241:
            # -- 241 -- 
            print("==> event 241 : Bright golden mist.")
            # Brume dorée brillante.
            if onOff == "on":
                SetRendererClearColor(self, cFlags, [player, "gold2"])
                SetRendererFogLinear(self, cFlags, [player, "-200 3000 2"])
                SetRendererFogColor(self, cFlags, [player, "gold2"])
            else:
                SetRendererStyle(self, cFlags, [player, "default"])
            SendChatMessage(self, myself, [player], "Event 241 (Bright golden mist) is {0}".format(onOff), cFlags.flags)
        elif eventNumber == 242:
            # -- 242 -- 
            print("==> event 242 : Less Bright golden mist.")
            # Brume dorée moins brillante.
            if onOff == "on":
                SetRendererClearColor(self, cFlags, [player, "gold3"])
                SetRendererFogLinear(self, cFlags, [player, "-200 3000 2"])
                SetRendererFogColor(self, cFlags, [player, "gold3"])
            else:
                SetRendererStyle(self, cFlags, [player, "default"])
            SendChatMessage(self, myself, [player], "Event 243 (Less Bright golden mist) is {0}".format(onOff), cFlags.flags)
        elif eventNumber == 243:
            # -- 243 -- 
            print("==> event 243 : Less Bright golden mist.")
            # Brume dorée moins brillante.
            if onOff == "on":
                SetRendererClearColor(self, cFlags, [player, "gold4"])
                SetRendererFogLinear(self, cFlags, [player, "-200 3000 2"])
                SetRendererFogColor(self, cFlags, [player, "gold4"])
            else:
                SetRendererStyle(self, cFlags, [player, "default"])
            SendChatMessage(self, myself, [player], "Event 243 (Less Bright golden mist) is {0}".format(onOff), cFlags.flags)
        elif eventNumber == 244:
            # -- 243 -- 
            print("==> event 244 : Less Bright golden mist.")
            # Brume dorée moins brillante.
            if onOff == "on":
                SetRendererClearColor(self, cFlags, [player, "gold5"])
                SetRendererFogLinear(self, cFlags, [player, "-200 3000 2"])
                SetRendererFogColor(self, cFlags, [player, "gold5"])
            else:
                SetRendererStyle(self, cFlags, [player, "default"])
            SendChatMessage(self, myself, [player], "Event 244 (Less Bright golden mist) is {0}".format(onOff), cFlags.flags)
        elif eventNumber == 25:
            # -- 25 -- 
            print("==> event 25 : Remove Protractor of Great Zero.")
            #GZ : Enlever le rapporteur.
            xBotAge.ToggleSceneObjects("ProtractorPart", age="GreatZero", bDrawOn=bOff, bPhysicsOn=bOff)
            xBotAge.ToggleSceneObjects("ProtractorCrystal01", age="GreatZero", bDrawOn=bOff, bPhysicsOn=bOff)
            xBotAge.ToggleSceneObjects("ProtractorBase04", age="GreatZero", bDrawOn=bOff, bPhysicsOn=bOff)
            xBotAge.ToggleSceneObjects("ProtractorBase03", age="GreatZero", bDrawOn=bOff, bPhysicsOn=bOff)
            xBotAge.ToggleSceneObjects("ProtractorRails", age="GreatZero", bDrawOn=bOff, bPhysicsOn=bOff)
            xBotAge.ToggleSceneObjects("LaserHalo", age="GreatZero", bDrawOn=bOff, bPhysicsOn=bOff)
            SendChatMessage(self, myself, [player], "Event 25 (Remove Protractor of Great Zero) is {0}".format(onOff), cFlags.flags)
        elif eventNumber == 26:
            # -- 26 -- 
            print("==> event 26 : Projector - LightHouse.")
            #Projector - LightHouse.
            soPlayer = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
            Light.PayLight3b(soPlayer, bOn, bOn, 0, 0, 100, 30, 0, 0)
            SendChatMessage(self, myself, [player], "Event 26 (Projector - LightHouse) is {0}".format(onOff), cFlags.flags)
        elif eventNumber == 261:
            # -- 261 -- 
            print("==> event 261 : Projector - LightHouse fixed.")
            #Projector - LightHouse.
            soPlayer = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
            Light.PayLight3b(soPlayer, bOn, False, 0, 0, 100, 30, 0, 0)
            SendChatMessage(self, myself, [player], "Event 261 (Projector - LightHouse fixed) is {0}".format(onOff), cFlags.flags)
        elif eventNumber == 100:
            print("==> event {} : Show all paintings.".format(eventNumber))
            #Pellet Cave : Show all paintings.
            if onOff == "on":
                Pellet.ShowPaintings(nb=0)
            else:
                Pellet.ShowPaintings(nb=-1)
            SendChatMessage(self, myself, [player], "Event {} (Show all paintings) is {}".format(eventNumber, onOff), cFlags.flags)
        elif eventNumber >= 101 and eventNumber <= 117:
            print("==> event {} : Show painting #{}.".format(eventNumber, eventNumber - 100))
            #Pellet Cave : Show a choosen painting with a predefined background color.
            if onOff == "on":
                Pellet.ShowPaintings(nb=eventNumber - 100)
            else:
                Pellet.ShowPaintings(nb=-1)
            SendChatMessage(self, myself, [player], "Event {} (Show painting #{}) is {}".format(eventNumber, eventNumber - 100, onOff), cFlags.flags)
        elif eventNumber == 118:
            print("==> event {} : Changing background color.".format(eventNumber))
            #Pellet Cave : Changing background color.
            if onOff == "on":
                Pellet.ChangeSky(bOn=True)
            else:
                Pellet.ChangeSky(bOn=False)
            SendChatMessage(self, myself, [player], "Event {} (Changing background color) is {}".format(eventNumber, onOff), cFlags.flags)
        elif eventNumber == 119:
            print("==> event {} : Drop white pellets.".format(eventNumber))
            #Pellet Cave : Drop white pellets.
            if onOff == "on":
                Pellet.DropPellets(bOn=True, type=4, delay=19.0)
            else:
                Pellet.DropPellets(bOn=False)
            SendChatMessage(self, myself, [player], "Event {} (Drop white pellets) is {}".format(eventNumber, onOff), cFlags.flags)
        elif eventNumber == 120:
            print("==> event {} : Hide some objects 1.".format(eventNumber))
            # Hide some objects.
            xBotAge.ToggleSceneObjects("Ladder", age="Cleft", bDrawOn=bOff, bPhysicsOn=bOff)
            xBotAge.ToggleSceneObjects("Ladder", age="Teledahn", bDrawOn=bOff, bPhysicsOn=bOff)
            xBotAge.ToggleSceneObjects("PipeInside", age="Teledahn", bDrawOn=bOff, bPhysicsOn=True)
            xBotAge.ToggleSceneObjects("Tree", age="Garden", bDrawOn=bOff, bPhysicsOn=bOff)
            xBotAge.ToggleSceneObjects("Bamboo", age="Garden", bDrawOn=bOff, bPhysicsOn=True)
            SendChatMessage(self, myself, [player], "Event {} (Hide some objects 1) is {}".format(eventNumber, onOff), cFlags.flags)
            
        elif eventNumber == 121:
            print("==> event {} : Hide some objects 2.".format(eventNumber))
            # Hide some objects.
            xBotAge.ToggleSceneObjects("Dome", age=None, bDrawOn=bOff, bPhysicsOn=True)
            xBotAge.ToggleSceneObjects("Rain", age=None, bDrawOn=bOff, bPhysicsOn=True)
            xBotAge.ToggleSceneObjects("Garden", age=None, bDrawOn=bOff, bPhysicsOn=True)
            xBotAge.ToggleSceneObjects("Water", age=None, bDrawOn=bOff, bPhysicsOn=True)
            SendChatMessage(self, myself, [player], "Event {} (Hide some objects 2) is {}".format(eventNumber, onOff), cFlags.flags)
        elif eventNumber == 27:
            # -- 27 -- 
            print("==> event 27")
            xBotAge.ToggleSceneObjects("Sky", age=None, bDrawOn=bOff, bPhysicsOn=True)
            xBotAge.ToggleSceneObjects("sky", age=None, bDrawOn=bOff, bPhysicsOn=True)
            xBotAge.ToggleSceneObjects("Dome", age=None, bDrawOn=bOff, bPhysicsOn=True)
            xBotAge.ToggleSceneObjects("Mountain", age=None, bDrawOn=bOff, bPhysicsOn=True)
            xBotAge.ToggleSceneObjects("Cloud", age=None, bDrawOn=bOff, bPhysicsOn=True)
            xBotAge.ToggleSceneObjects("Back", age=None, bDrawOn=bOff, bPhysicsOn=True)
            xBotAge.ToggleSceneObjects("Fog", age=None, bDrawOn=bOff, bPhysicsOn=True)
            xBotAge.ToggleSceneObjects("Sphere", age=None, bDrawOn=bOff, bPhysicsOn=True)
            xBotAge.ToggleSceneObjects("Dust", age=None, bDrawOn=bOff, bPhysicsOn=True)
            xBotAge.ToggleSceneObjects("Pod", age=None, bDrawOn=bOff, bPhysicsOn=True)
            xBotAge.ToggleSceneObjects("Rain", age=None, bDrawOn=bOff, bPhysicsOn=True)
            xBotAge.SetRenderer(style = None, cr=0.00, cg=0.06, cb=0.13)
            print("==> Minkata night sky")
            CloneObject.co3("StarGlobe", "Minkata", bShow=bOn, bLoad=bOn)
            CloneObject.co3("GalaxyDecal", "Minkata", bShow=bOn, bLoad=bOn)
            CloneObject.co3("GalaxyDecalSmall", "Minkata", bShow=bOn, bLoad=bOn)
            #CloneObject.co3("Constellation01Decal01", "Minkata", bShow=bOn, bLoad=bOn)
            #CloneObject.co3("Constellation01Decal02", "Minkata", bShow=bOn, bLoad=bOn)
            #CloneObject.co3("Constellation01Decal03", "Minkata", bShow=bOn, bLoad=bOn)
            #CloneObject.co3("Constellation01Decal04", "Minkata", bShow=bOn, bLoad=bOn)
            #CloneObject.co3("Constellation01Decal05", "Minkata", bShow=bOn, bLoad=bOn)
            #CloneObject.co3("ConstellationDummyCave01", "Minkata", bShow=bOn, bLoad=bOn)
            #CloneObject.co3("ConstellationDummyCave02", "Minkata", bShow=bOn, bLoad=bOn)
            #CloneObject.co3("ConstellationDummyCave03", "Minkata", bShow=bOn, bLoad=bOn)
            #CloneObject.co3("ConstellationDummyCave04", "Minkata", bShow=bOn, bLoad=bOn)
            #CloneObject.co3("ConstellationDummyCave05", "Minkata", bShow=bOn, bLoad=bOn)
            SendChatMessage(self, myself, [player], "Event 27 (Minkata night sky) is {0}".format(onOff), cFlags.flags)
        elif eventNumber == 271:
            # -- 271 -- 
            print("==> event 271")
            print("==> Minkata night sky 1")
            CloneObject.co3("StarGlobe", "Minkata", bShow=bOn, bLoad=bOn)
            SendChatMessage(self, myself, [player], "Event 271 (Minkata night sky 1) is {0}".format(onOff), cFlags.flags)
        elif eventNumber == 272:
            # -- 272 -- 
            print("==> event 272")
            print("==> Minkata night sky 2")
            CloneObject.co3("GalaxyDecal", "Minkata", bShow=bOn, bLoad=bOn)
            SendChatMessage(self, myself, [player], "Event 272 (Minkata night sky 2) is {0}".format(onOff), cFlags.flags)
        elif eventNumber == 273:
            # -- 273 -- 
            print("==> event 273")
            print("==> Minkata night sky 3")
            CloneObject.co3("GalaxyDecalSmall", "Minkata", bShow=bOn, bLoad=bOn)
            SendChatMessage(self, myself, [player], "Event 273 (Minkata night sky 3) is {0}".format(onOff), cFlags.flags)
        elif eventNumber == 28:
            # -- 28 -- 
            print("==> event 28")
            xBotAge.ToggleSceneObjects("Sky", age=None, bDrawOn=bOff, bPhysicsOn=True)
            xBotAge.ToggleSceneObjects("sky", age=None, bDrawOn=bOff, bPhysicsOn=True)
            xBotAge.ToggleSceneObjects("Dome", age=None, bDrawOn=bOff, bPhysicsOn=True)
            xBotAge.ToggleSceneObjects("Mountain", age=None, bDrawOn=bOff, bPhysicsOn=True)
            xBotAge.ToggleSceneObjects("Cloud", age=None, bDrawOn=bOff, bPhysicsOn=True)
            xBotAge.ToggleSceneObjects("Back", age=None, bDrawOn=bOff, bPhysicsOn=True)
            xBotAge.ToggleSceneObjects("Fog", age=None, bDrawOn=bOff, bPhysicsOn=True)
            xBotAge.ToggleSceneObjects("Sphere", age=None, bDrawOn=bOff, bPhysicsOn=True)
            xBotAge.ToggleSceneObjects("Dust", age=None, bDrawOn=bOff, bPhysicsOn=True)
            xBotAge.ToggleSceneObjects("Pod", age=None, bDrawOn=bOff, bPhysicsOn=True)
            xBotAge.ToggleSceneObjects("Rain", age=None, bDrawOn=bOff, bPhysicsOn=True)
            xBotAge.SetRenderer(style = None, cr=0.00, cg=0.06, cb=0.13)
            print("==> Veelay night sky")
            CloneObject.co3("SkyDome", "VeeTsah", bShow=bOn, bLoad=bOn)
            SendChatMessage(self, myself, [player], "Event 28 (Veelay night sky) is {0}".format(onOff), cFlags.flags)
        elif eventNumber == 281:
            # -- 281 -- 
            print("==> event 281")
            print("==> Veelay Aurora 1")
            CloneObject.co3("Aurora01", "VeeTsah", bShow=bOn, bLoad=bOn)
            SendChatMessage(self, myself, [player], "Event 281 (Veelay Aurora 1) is {0}".format(onOff), cFlags.flags)
        elif eventNumber == 282:
            # -- 282 -- 
            print("==> event 282")
            print("==> Veelay Aurora 2")
            CloneObject.co3("Aurora02", "VeeTsah", bShow=bOn, bLoad=bOn)
            SendChatMessage(self, myself, [player], "Event 282 (Veelay Aurora 2) is {0}".format(onOff), cFlags.flags)
        elif eventNumber == 283:
            # -- 283 -- 
            print("==> event 283")
            print("==> Veelay Aurora 3")
            CloneObject.co3("Aurora03", "VeeTsah", bShow=bOn, bLoad=bOn)
            SendChatMessage(self, myself, [player], "Event 283 (Veelay Aurora 3) is {0}".format(onOff), cFlags.flags)
        elif eventNumber == 29:
            # -- 29 -- 
            print("==> event 29")
            print("==> Upper Planet Vessal Fog")
            xBotAge.ToggleSceneObjects("Dust", age=None, bDrawOn=False, bPhysicsOn=False)
            xBotAge.ToggleSceneObjects("Fog", age=None, bDrawOn=False, bPhysicsOn=False)
            xBotAge.ToggleSceneObjects("Sky", age=None, bDrawOn=False, bPhysicsOn=False)
            xBotAge.ToggleSceneObjects("sky", age=None, bDrawOn=False, bPhysicsOn=False)
            xBotAge.ToggleSceneObjects("Dome", age=None, bDrawOn=False, bPhysicsOn=False)
            xBotAge.ToggleSceneObjects("Sphere", age=None, bDrawOn=False, bPhysicsOn=False)
            xBotAge.ToggleSceneObjects("Fog", age="Personal", bDrawOn=False, bPhysicsOn=False)
            xBotAge.ToggleSceneObjects("Sky", age="Personal", bDrawOn=False, bPhysicsOn=False)
            SendChatMessage(self, myself, [player], "Event 29 (Upper Planet Vessal Fog) is {0}".format(onOff), cFlags.flags)
        elif eventNumber == 291:
            # -- 291 -- 
            print("==> event 291")
            print("==> Upper Planet Vessal Fog")
            tupMat = ((-0.6027394533157349, -0.7979380488395691, 0.0, -49.398189544677734), (0.7979380488395691, -0.6027394533157349, 0.0, -105.94088745117188), (0.0, 0.0, 1.0, 2993.45263671875), (0.0, 0.0, 0.0, 1.0))
            pos.setData(tupMat)
            CloneObjects.CloneThat(objName="DustPlaneParticle01", age="Minkata", bShow=bOn, bLoad=bOn, number=1, thisone=0, scale=ptVector3(0.5, 0.5, 0.5), matPos=pos, bAttach=False, fct=CloneObjects.DoStuff2)
            SendChatMessage(self, myself, [player], "Event 291 (Upper Planet Vessal Fog) is {0}".format(onOff), cFlags.flags)
        elif eventNumber == 292:
            # -- 292 -- 
            print("==> event 292")
            print("==> Upper Planet Vessal Fog")
            tupMat = ((-0.6027394533157349, -0.7979380488395691, 0.0, -49.398189544677734), (0.7979380488395691, -0.6027394533157349, 0.0, -105.94088745117188), (0.0, 0.0, 1.0, -50000.0), (0.0, 0.0, 0.0, 1.0))
            pos.setData(tupMat)
            CloneObjects.CloneThat(objName="DustPlaneParticle01", age="Minkata", bShow=bOn, bLoad=bOn, number=1, thisone=0, scale=ptVector3(0.5, 0.5, 0.5), matPos=pos, bAttach=False, fct=CloneObjects.DoStuff2)
            SendChatMessage(self, myself, [player], "Event 292 (Upper Planet Vessal Fog) is {0}".format(onOff), cFlags.flags)
        else:
            pass
        return 1
    except:
        return 0

# AddClone
def AddClone(self, cFlags, args = []):
    myself = PtGetLocalPlayer()
    player = args[0]
    if not isPlayerInAge(player):
        SendChatMessage(self, myself, [player], "You must be in my age, use link to join me.", cFlags.flags)
        return 1
    bOn = True
    bOff = False
    onOff = "on"
    what = None
    if len(args) > 1:
        params = args[1].split()
        if len(params) > 0:
            try:
                what = params[0]
            except:
                pass
        if len(params) > 1:
            if params[1] == "off":
                bOn = False
                bOff = True
                onOff = "off"
    #
    soAvatar = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
    mPos = soAvatar.getLocalToWorld()
    #
    try:
        xBotAge.DisablePanicLinks()
        if what == "star":
            CloneObject.co3("StarDummy", "Gira", bShow=bOn, bLoad=bOn, scale=1, matPos=mPos)
        elif what == "sun":
            CloneObject.co3("SunDummyNew", "Gira", bShow=bOn, bLoad=bOn, scale=1, matPos=mPos)
        elif what == "sky":
            CloneObject.co3("Sky", "Gira", bShow=bOn, bLoad=bOn, scale=1, matPos=mPos)
        else:
            pass
        return 1
    except:
        return 0

# OnLake
def OnLake(self, cFlags, args = []):
    myself = PtGetLocalPlayer()
    player = args[0]
    bOn = True
    if len(args) > 1:
        params = args[1].split()
        if len(params) > 0:
            try:
                if params[0] == "off":
                    bOn = False
            except:
                pass
    if not isPlayerInAge(player):
        SendChatMessage(self, myself, [player], "You must be in my age, use link to join me.", cFlags.flags)
        return 1
    if bOn:
        #print "==> OnLake 1"
        soAvatar = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
        mPos = soAvatar.getLocalToWorld()
        #print "==> OnLake 2"
        try:
            afn = PtGetAgeInfo().getAgeFilename()
            if afn == "city":
                mPos = SetMat(mPos, 0, -600, 1)
            elif afn == "Neighborhood":
                mPos = SetMat(mPos, 300, -900, 1)
            elif afn == "Kadish":
                mPos = SetMat(mPos, 600, -300, 1)
            elif afn == "Teledahn":
                mPos = SetMat(mPos, -716, 529, 1)
            else:
                #mPos = None
                mPos = SetMat(mPos, 0, 22, 10)
            #print "==> OnLake 3 ok"
            #return 1
        except ValueError:
            #print "==> OnLake 3 ko"
            return 0
        print("==> OnLake 4")
        CloneObject.Minkata(bShow=True, bLoad=True, soPlayer=soAvatar, matPos=mPos)
        SendChatMessage(self, myself, [player], "To remove the 'onlake' effect... PM me 'nolake' or 'onlake off' then visit Minkata.", cFlags.flags)
        return 1
    else:
        CloneObject.Minkata(bShow=False, bLoad=False)
        SendChatMessage(self, myself, [player], "I'm removing the 'onlake' effect... The command will take effect after you have visited Minkata.", cFlags.flags)
        return 1


# NoLake
def NoLake(self, cFlags, args = []):
    myself = PtGetLocalPlayer()
    player = args[0]
    CloneObject.Minkata(bShow=False, bLoad=False)
    SendChatMessage(self, myself, [player], "I'm removing the 'onlake' effect... The command will take effect after you have visited Minkata.", cFlags.flags)
    return 1

# Changing some Hood SDL
def ToggleHoodSDL(self, cFlags, args = []):
    myself = PtGetLocalPlayer()
    player = args[0]
    if not isPlayerInAge(player):
        SendChatMessage(self, myself, [player], "You must be in my age, use link to join me.", cFlags.flags)
        return 1
    if len(args) > 1:
        name = args[1]
        sdl.ToggleHoodSDL(name)
        return 1
    else:
        return 0

# ColumnUnderPlayer => command lift
def ColumnUnderPlayer(self, cFlags, args = []):
    global bJalakAdded
    myself = PtGetLocalPlayer()
    player = args[0]
    if not isPlayerInAge(player):
        SendChatMessage(self, myself, [player], "You must be in my age, use link to join me." , cFlags.flags)
        return 1
    bShow = True
    if len(args) > 1:
        params = args[1].split()
        if len(params) > 0:
            if params[0] == "hide":
                bShow = False
    Columns2.ColumnUnderPlayer(True, bShow, player)
    bJalakAdded = True
    return 1

# ColumnUnderPlayer2 => command lift v2 (lift [up/down/off/hide])
def ColumnUnderPlayer2(self, cFlags, args = []):
    global bJalakAdded
    myself = PtGetLocalPlayer()
    player = args[0]
    if not isPlayerInAge(player):
        SendChatMessage(self, myself, [player], "You must be in my age, use link to join me." , cFlags.flags)
        return 1
    bShow = True
    bAttach = True
    fXAngle = 0.0
    fYAngle = 0.0
    fZAngle = 0.0
    if len(args) > 1:
        print("ColumnUnderPlayer2 : args[1] = [{}]".format(args[1]))
        params = args[1].split()
        print("ColumnUnderPlayer2 : len(params) = {}".format(len(params)))
        if len(params) > 0:
            print("params[0]='{}'".format(params[0]))
            try:
                fXAngle = float(params[0])
                print("fXAngle={}".format(fXAngle))
            except:
                if params[0] == "up":
                    fXAngle = 30.0
                elif params[0] == "down":
                    fXAngle = -30.0
                elif params[0] == "hide":
                    bShow = False
                elif params[0] == "off":
                    bAttach = False
                else:
                    print("Error on params[0]='{}'".format(params[0]))
        if len(params) > 1:
            print("params[0]='{}'".format(params[1]))
            try:
                fYAngle = float(params[1])
                print("fYAngle={}".format(fYAngle))
            except:
                if params[1] == "up":
                    fYAngle = 30.0
                elif params[1] == "down":
                    fYAngle = -30.0
                elif params[1] == "hide":
                    bShow = False
                elif params[1] == "off":
                    bAttach = False
                else:
                    print("Error on params[1]='{}'".format(params[1]))
        if len(params) > 2:
            print("params[0]='{}'".format(params[2]))
            try:
                fZAngle = float(params[2])
                print("fZAngle={}".format(fZAngle))
            except:
                if params[2] == "up":
                    fZAngle = 30.0
                elif params[2] == "down":
                    fZAngle = -30.0
                elif params[2] == "hide":
                    bShow = False
                elif params[2] == "off":
                    bAttach = False
                else:
                    print("Error on params[2]='{}'".format(params[2]))
        if len(params) > 3:
            print("params[0]='{}'".format(params[3]))
            if params[3] == "hide":
                bShow = False
            elif params[3] == "off":
                bAttach = False
            else:
                print("Error on params[3]='{}'".fromat(params[3]))
    print("Calling Columns2.ColumnUnderPlayer2(bOn={}, bShow{}, player={}, fXAngle={}, fYAngle={}, fZAngle={}, bAttach={})".format(True, bShow, player, fXAngle, fYAngle, fZAngle, bAttach))
    Columns2.ColumnUnderPlayer2(True, bShow, player, fXAngle, fYAngle, fZAngle, bAttach)
    bJalakAdded = True
    return 1

# ColumnInFrontOfPlayer => command column angle
def ColumnInFrontOfPlayer(self, cFlags, args = []):
    global bJalakAdded
    myself = PtGetLocalPlayer()
    player = args[0]
    if not isPlayerInAge(player):
        SendChatMessage(self, myself, [player], "You must be in my age, use link to join me." , cFlags.flags)
        return 1
    fXAngle = 0.0
    if len(args) > 1:
        params = args[1].split()
        if len(params) > 0:
            try:
                fXAngle = float(params[0])
            except:
                if params[0] == "up":
                    fXAngle = 30.0
                elif params[0] == "down":
                    fXAngle = -30.0
                
    Columns2.ColumnInFrontOfPlayer(True, fXAngle, player)
    bJalakAdded = True
    return 1

#
def Cercle(self, cFlags, args = []):
    myself = PtGetLocalPlayer()
    player = args[0]
    if not isPlayerInAge(player):
        SendChatMessage(self, myself, [player], "You must be in my age, use link to join me." , cFlags.flags)
        return 1
    soAvatar = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
    xPlayers.Cercle(coef=2.0, h=3.0, avCentre=soAvatar)
    return 1

# MarkerGames.SendGameList(title, playerId=None):
# MarkerGames.SendGame(gameId, playerId=None):
def SendGame(self, cFlags, args = []):
    myself = PtGetLocalPlayer()
    player = args[0]
    idAvatar = player.getPlayerID()
    
    print("SendGame {}, {}".format(idAvatar, type(idAvatar)))
    
    # Ne rien envoyer si le joueur n'est pas un ami (ca va peut-etre eviter les plantages)
    if not xPlayers.IsBud(idAvatar):
        print("This player is not yet my friend => Don't send anything!")
        return 1
    
    if len(args) > 1:
        params = args[1].split()
        for param in params:
            print("SendGame #{}, {}".format(param, type(param)))
            # With old client
            #ret = MarkerGames.SendGame(gameId=param, playerId=idAvatar)
            # With new client
            ret = MarkerGames2.SendGame(gameId=param, playerId=idAvatar)
            if ret[0] == 1:
                SendChatMessage(self, myself, [player], "I'm sending you game #{} : {}. Look in your Incoming folder.".format(param, ret[1]), cFlags.flags)
                print("SendGame : game sent -> #{} - {}".format(param, ret[1]))
            else:
                SendChatMessage(self, myself, [player], "Game #{0} not found, sorry.".format(param), cFlags.flags)
                print("SendGame error : game not sent")
        print("SendGame end 1")
        return 1
    else:
        print("SendGame => list")
        title = "{0}'s Marker Games".format(myself.getPlayerName())
        # With old client
        #ret = MarkerGames.SendGameList(title, playerId=idAvatar)
        # With new client
        ret = MarkerGames2.SendGameList(title, playerId=idAvatar)
        if ret == 1:
            SendChatMessage(self, myself, [player], "I'm sending you my game list, look in your Incoming folder.", cFlags.flags)
            print("SendGame : list sent")
        else:
            SendChatMessage(self, myself, [player], "No game list available, sorry.", cFlags.flags)
            print("SendGame error : list not sent")
        print("SendGame end 2")
        return 1

# Ride an animal
# en ville les oiseaux b1 a b6 + bahro
def RideAnimal(self, cFlags, args = []):
    myself = PtGetLocalPlayer()
    player = args[0]
    if not isPlayerInAge(player):
        SendChatMessage(self, myself, [player], "You must be in my age, use link to join me.", cFlags.flags)
        return 1
    t=30.0
    soName="b1"
    if len(args) > 1:
        params = args[1].split()
        for param in params:
            print("RideAnimal : {} ({})".format(param, type(param)))
        if len(params) > 2:
            t = params[1]
        if len(params) > 0:
            soName=params[0]
        else:
            return 0
        playerName = player.getPlayerName()
        Ride.Suivre(objet=soName, Avatar=playerName, duree=t)
        return 1
    else:
        return 0

# To rotate to the next sphere, return the active sphere (sphere = 1 a 4)
def RotateAhnonaySphere(self, cFlags, args = []):
    myself = PtGetLocalPlayer()
    player = args[0]
    """
    if not isPlayerInAge(player):
        SendChatMessage(self, myself, [player], "You must be in my age, use link to join me.", cFlags.flags)
        return 1
    """
    ret = Ahnonay.RotateSphere()
    if ret[0] == 0:
        SendChatMessage(self, myself, [player], "{0} To move me to Ahnonay, PM me BOTTO AHNONAY.".format(ret[1]), cFlags.flags)
    else:
        SendChatMessage(self, myself, [player], ret[1], cFlags.flags)
    return 1

# Ca m'ennuie de creer une classe ici, mais pour l'instant je n'ai pas la bonne idee...
# Classe pour executer une danse pas a pas
class ExecuteDanceSteps:
    xKiSelf = None
    xKiFlags = None
    isRunning = False
    lstActions = list()
    lstIdDancers = list()
    bAllOn = False
    bBypassGroups = False
    groupOfDancers = dict()
    nbActions = 0
    currentActionIndex = 0

    #def __init__(self):
    def __init__(self, bBypassGroups):
        print("ExecuteDanceSteps : init")
        self.bBypassGroups = bBypassGroups
    def Step(self):
        print("ExecuteDanceSteps : Step {} ({}, {})".format(self.currentActionIndex, self.nbActions, len(self.lstActions)))
        delay = 0
        
        strAct = self.lstActions[self.currentActionIndex]
        if strAct.lower().startswith("dance "):
            print("ExecuteDanceSteps [Step] : Dance name = {}".fromat(strAct))
        elif strAct.lower().startswith("end"):
            print("ExecuteDanceSteps : This is the end!")
        elif strAct.lower().startswith("#"):
            print("ExecuteDanceSteps : Comment, skip it.")
        elif strAct.lower().startswith("group"):
            print("ExecuteDanceSteps [Step] : New group of dancers.")
            #self.lstIdDancers = Dance.GetIdDancerList(strAct)
            self.lstIdDancers, self.bAllOn = Dance.GetIdDancerList(strAct)
        elif strAct.lower().startswith("aliasgroup"):
            print("ExecuteDanceSteps [Step] : New group of dancers by alias.")
            self.lstIdDancers = Dance.GetIdDancerListFromAlias(strAct, self.groupOfDancers)
        elif strAct.lower().startswith("definegroup"):
            print("ExecuteDanceSteps [Step] : Define a new group of dancers.")
            self.groupOfDancers = Dance.DefineGroup(strAct)
        else:
            print("ExecuteDanceSteps [Step] : Command line : {}".format(strAct))
            cmdLine = Dance.ConvertActionToCommand(strAct)
            # Executer la commande pour chaque danseur present dans mon age
            #self.lstIdDancers
            agePlayers = PtGetPlayerList()
            agePlayers.append(PtGetLocalPlayer())
            if self.bAllOn or self.bBypassGroups:
                ageDancers = agePlayers
            else:
                ageDancers = [pl for pl in agePlayers if pl.getPlayerID() in self.lstIdDancers]
            # pour tester : je m'ajoute si la liste est vide
            if len(ageDancers) == 0:
                ageDancers.append(PtGetLocalPlayer())
            # Dispatch the command to all players in the group
            for player in ageDancers:
                cmdArgs = [player]
                cmdArgs.append(cmdLine[1])
                CallMethod(self=self.xKiSelf, cmdName=cmdLine[0], cFlags=self.xKiFlags, pAmIRobot=xBotAge.AmIRobot, args=cmdArgs)
            # Attendre et lancer la commande suivante
            delay = cmdLine[2]
            print("ExecuteDanceSteps [Step {}] : delay = {}".format(self.currentActionIndex, delay))
        
        if self.currentActionIndex < self.nbActions - 1:
            self.currentActionIndex += 1
            print("ExecuteDanceSteps [Step] : PtSetAlarm(delay = {})".format(delay))
            PtSetAlarm(delay, self, 0)
        else:
            print("ExecuteDanceSteps [Step] : Stop")
            self.Stop()
        
        #PtSetAlarm(delay, self, 0)
        #pass

    def onAlarm(self, param=0):
        #print "ExecuteDanceSteps : onalarm"
        if not self.isRunning:
            print("ExecuteDanceSteps [onAlarm] : Not running")
            return
        #
        #for strAct in self.lstActions:
        #self.Stop()
        
        #
        print("ExecuteDanceSteps [onAlarm] : call Step")
        self.Step()
        
        #if param == 1:
        #    machine(3)
        #    PtSetAlarm(19, self, 0)
        #else:
        #    machine(4)
        #    PtSetAlarm(19, self, 1)
        
    def Start(self, xKiSelf, xKiFlags, lstActions):
        #print "ExecuteDanceSteps : Start 1"
        self.xKiSelf = xKiSelf
        self.xKiFlags = xKiFlags
        self.lstActions = lstActions
        self.nbActions = len(self.lstActions)
        self.currentActionIndex = 0
        if not self.isRunning:
            self.isRunning = True
            print("ExecuteDanceSteps : Start 2")
            self.onAlarm()

    def Stop(self):
        print("ExecuteDanceSteps : Stop")
        self.isRunning = False

# Il me faut une instance de la classe ExecuteDanceSteps
# A voir si je prevois de permettre a plusieurs joueurs de lancer chacun sa danse
# Il me faudra creer un dictionnaire de danses (joueur / instance de danse)
#executeDanceSteps = ExecuteDanceSteps()
executeDanceSteps = None

# Methode pour executer une danse complete
def StartDance(self, cFlags, args=[]):
    #print "StartDance 1"
    global executeDanceSteps
    myself = PtGetLocalPlayer()
    player = args[0]
    if not isPlayerInAge(player):
        SendChatMessage(self, myself, [player], "You must be in my age, use link to join me.", cFlags.flags)
        return 1
    bBypassGroups = False
    #print "StartDance 2"
    if len(args) > 1:
        params = args[1].split()
    else:
        return 0
    print("StartDance 3")
    if len(params) > 1:
        # 2nd agument : Optional, dance for all, bypass the groups
        if params[1].strip() == "all":
            bBypassGroups = True
    print("StartDance 4")
    if len(params) > 0:
        # Un seul parametre est attendu : le nom du fichier de danse.
        #print "StartDance 4"
        danceFileName = params[0].strip()
        print("ExecuteDance : name = {}, for all = {}".format(danceFileName, bBypassGroups))
        lstActions = Dance.ReadDanceFile(danceFileName)
        #print "StartDance 5"
        # Au cas ou une danse soit deja lancee, il faut l'arreter avant de demarrer la nouvelle
        if executeDanceSteps is not None:
            executeDanceSteps.Stop()
        
        #print "StartDance 6"
        if len(lstActions) > 0:
            #print "StartDance 7"
            if executeDanceSteps is None:
                executeDanceSteps = ExecuteDanceSteps(bBypassGroups)
                #print "StartDance 8"
            else:
                executeDanceSteps.bBypassGroups = bBypassGroups
            # C'est parti...
            executeDanceSteps.Start(self, cFlags, lstActions)
            #print "StartDance 9"
        else:
            SendChatMessage(self, myself, [player], "The dance file '{}' is empty or does not exist.".format(danceFileName), cFlags.flags)
        #print "StartDance 10"
        return 1
    else:
        #print "StartDance 11"
        return 0

# Methode pour arreter l'execution d'une danse
def StopDance(self, cFlags, args=[]):
    #print "StopDance 1"
    global executeDanceSteps
    myself = PtGetLocalPlayer()
    player = args[0]
    if not isPlayerInAge(player):
        SendChatMessage(self, myself, [player], "You must be in my age, use link to join me.", cFlags.flags)
        return 1
    if executeDanceSteps is not None:
        executeDanceSteps.Stop()
        executeDanceSteps = None
    return 1

"""
    agePlayers = filter(lambda pl: not(pl.getPlayerID() in dicBot.keys()), PtGetPlayerList())
    agePlayers.append(PtGetLocalPlayer())
    playerIdList = map(lambda player: player.getPlayerID(), agePlayers)
    
    avatar = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
    
    CallMethod(self, cmdName, cFlags, pAmIRobot, args=[]):
    xBotAge.AmIRobot = pAmIRobot
"""

# Methode pour sauvegarder l'apparence d'un joueur
def SaveMe(self, cFlags, args=[]):
    myself = PtGetLocalPlayer()
    player = args[0]
    if not isPlayerInAge(player):
        SendChatMessage(self, myself, [player], "You must be in my age, use link to join me.", cFlags.flags)
        return 1
    if len(args) > 1:
        # Un seul parametre est attendu : le nom du fichier d'habillement.
        clothingName = args[1].strip()
        print("SaveMe : {} ({})".format(clothingName, type(clothingName)))
        
        ret = clothing.SaveAvatarClothingTo(player, clothingName)
        return ret
    else:
        return 0

# Methode pour restaurer l'apparence d'un joueur
def RestoreMe(self, cFlags, args=[]):
    myself = PtGetLocalPlayer()
    player = args[0]
    if not isPlayerInAge(player):
        SendChatMessage(self, myself, [player], "You must be in my age, use link to join me.", cFlags.flags)
        return 1
    if len(args) > 1:
        # Un seul parametre est attendu : le nom du fichier d'habillement.
        clothingName = args[1].strip()
        print("RestoreMe : {} ({})".format(clothingName, type(clothingName)))
        
        ret = clothing.LoadAvatarClothingFrom(player, clothingName)
        return ret
    else:
        return 0

# Toggles the visibility of the avatar.
def ToggleVisibility(self, cFlags, args=[]):
    myself = PtGetLocalPlayer()
    player = args[0]
    if not isPlayerInAge(player):
        SendChatMessage(self, myself, [player], "You must be in my age, use link to join me.", cFlags.flags)
        return 1
    if len(args) > 1:
        bOn = False
        # Un seul parametre est attendu.
        strOnOff = args[1].strip()
        print("ToggleVisibility : {}".format(strOnOff))
        if strOnOff == "1" or strOnOff == "on" or strOnOff == "true" :
            bOn = True
        soAvatar = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
        soAvatar.draw.netForce(1)
        soAvatar.draw.enable(bOn)
        return 1
    else:
        return 0

# Unload all the clones
def UnloadClones(objectName, ageFileName):
    print(">> UnloadClones(objectName='{}', ageFileName='{}') <<".format(objectName, ageFileName))
    demandeur = xFireCamp.placeCleftFireCamp.Demandeur
    print("demandeur = {}".format(demandeur))
    masterKey = PtFindSceneobject(objectName, ageFileName).getKey()
    xFireCamp.GestionClones.CacheCloneInutile(demandeur, masterKey, 0)
    cloneKeys = PtFindClones(masterKey)
    for ck in cloneKeys:
        PtCloneKey(ck, 0)

# Global variable to store the campfire state
bCampFireOn = False

# Add or remove the campfire
def PutCampFireHere(self, cFlags, args=[]):
    global bCampFireOn
    myself = PtGetLocalPlayer()
    player = args[0]
    if not isPlayerInAge(player):
        SendChatMessage(self, myself, [player], "You must be in my age, use link to join me.", cFlags.flags)
        return 1
    bOn = True
    if len(args) > 1:
        bOn = False
        # Un seul parametre est attendu.
        strOnOff = args[1].strip()
        print("PutCampFireHere : {}".format(strOnOff))
        if strOnOff == "1" or strOnOff == "on" or strOnOff == "true" :
            bOn = True
    if bOn:
        SendChatMessage(self, myself, [player], "At first use loading firecamp takes about 40s, please be patient...", cFlags.flags)
        xFireCamp.PutCleftFireCampHere(player)
        bCampFireOn = True
        return 1
    else:
        # removing campfire elements
        print("Avant : DicDemandeursClones = {}".format(xFireCamp.GestionClones.VarPerso.AccessVarPerso.DicDemandeursClones))
        UnloadClones(objectName="ClockPart08",       ageFileName="Ahnonay")
        UnloadClones(objectName="ClockPart05",       ageFileName="Ahnonay")
        UnloadClones(objectName="FlamerRed01",       ageFileName="BahroCave")
        UnloadClones(objectName="SmokerUpRed",       ageFileName="BahroCave")
        UnloadClones(objectName="DusterRed",         ageFileName="BahroCave")
        UnloadClones(objectName="RTomniRed01",       ageFileName="BahroCave")
        UnloadClones(objectName="RTomniRed06",       ageFileName="BahroCave")
        UnloadClones(objectName="Flamer",            ageFileName="BahroCave")
        UnloadClones(objectName="SmokerUp",          ageFileName="BahroCave")
        UnloadClones(objectName="Duster",            ageFileName="BahroCave")
        UnloadClones(objectName="RTOmniLighFlame",   ageFileName="BahroCave")
        UnloadClones(objectName="RTOmniLighFlame01", ageFileName="BahroCave")
        xFireCamp.placeCleftFireCamp = None
        print("Apres : DicDemandeursClones = {}".format(xFireCamp.GestionClones.VarPerso.AccessVarPerso.DicDemandeursClones))
        bCampFireOn = False
        return 1
"""
#Exemple:
#Appelle la fonction maFonction de monModule.py
def MaMethode(self, cFlags, args = []):
    #histoire de savoir que quelqu'un a appele cette methode
    PtSendKIMessage(kKILocalChatStatusMsg, "> MaMethode")
    #Testons la presence de parametres, normalement "player" a ete ajoute automatiquement
    if len(args) < 1:
        #Pas de parametre ==> erreur
        return 0
    myself = PtGetLocalPlayer()
    player = args[0]
    # Si la commande a besoin de parametres (autre que le joueur)
    if len(args) < 2:
        #Pas de parametre ==> erreur
        return 0
    # Decomposons la chaine qui contient les parametres separes par des espaces
    params = args[1].split()
    # En avons-nous assez? (ici 2)
    if len(params) < 2:
        #Pas assez de parametres ==> erreur
        return 0
    #Si la commande doit etre executee dans l'age du robot
    if not isPlayerInAge(player):
        SendChatMessage(self, myself, [player], "You must be in my age, use link to join me.", cFlags.flags)
        return 1
    #On peut ajouter des tests sur les parametres aussi...
    #Tout semble ok, appelons la fonction tant desiree
    playerID = player.getPlayerID()
    resultat = monModule.maFonction(self, playerID, params[0], params[1])
    SendChatMessage(self, myself, [player], str(resultat), cFlags.flags)
    return 1
"""

# Envoyer une note d'aide au demandeur (inspire du script de Michel)
def Help(self, cFlags, args = []):
    #PtSendKIMessage(kKILocalChatStatusMsg, "> Help")
    if len(args) < 1:
        PtSendKIMessage(kKILocalChatStatusMsg, "** Help: no arg! **")
        print("** Help: no arg! **")
        return 0
    myself = PtGetLocalPlayer()
    player = args[0]
    idAvatar = player.getPlayerID()
    
    #PtSendKIMessage(kKILocalChatStatusMsg, "** Help: sending to \"{}\". **".format(player.getPlayerName()))
    #print("** Help: sending to \"{}\". **".format(player.getPlayerName()))
    msg = "** Help: sending to \"{0}\" [{1}]. **".format(player.getPlayerName(), idAvatar)
    PtSendKIMessage(kKILocalChatStatusMsg, msg)
    print(msg)
    
    # aide sur une commande (en chat prive)
    if len(args) > 1:
        cmdName = args[1]
        HelpCmd(self, player, cFlags, cmdName)
        return 1
    
    # si pas de commande specifiee, envoyer le KiMail
    # mais seulement si le joueur est un ami (ca va peut-etre eviter les plantages)
    # Ne rien envoyer si le joueur n'est pas un ami (ca va peut-etre eviter les plantages)
    if not xPlayers.IsBud(idAvatar):
        print("This player is not yet my friend => Don't send anything!")
        return 1
    
    """
    #pour en mettre une copie dans mon journal Nexus
    journals = ptVault().getAgeJournalsFolder()
    agefolderRefs = journals.getChildNodeRefList()
    for agefolderRef in agefolderRefs:
        agefolder = agefolderRef.getChild()
        if agefolder.getType() == PtVaultNodeTypes.kFolderNode:
            agefolder = agefolder.upcastToFolderNode()
            if agefolder.getName() == 'Nexus':
                journal = agefolder
                break
    """
    
    title1 = myself.getPlayerName() + "'s help"
    msg = "Shorah!\n"
    msg += "I'm an automated avatar created by Mirphak.\n"
    #msg += "I'm not a magic bot, the commands you can PM to me are different.\n"
    msg += "\n"
    msg += "*** Please remember to log out after using the bot. ***\n"
    msg += "\n"
    msg += "Here the list of available commands (last update 2022-06-19):\n"
    msg += "------------------------------------------------------------\n\n"
    msg += "help : sends you this text note.\n"
    msg += "help [command name]: PM you a specific help on a command.\n\n"
    msg += "** LINKING THROUGH AGES:\n"
    msg += "link or meet : links your avatar to Mir-o-Bot's current Age.\n\n"
    msg += "to {city/library/ferry/dakotah/tokotah/concert/palace} : links YOU to different points of the public city\n"
    msg += "or some public ages {gog/gome/kirel/kveer/phil/chiso/messengerspub/veelay}\n"
    #msg += "or a Mir-o-Bot age {Ae'gura/Ahnonay Cathedral/Cleft/Relto/Eder Gira/Eder Kemo/Er'cana/Gahreesen/Hood/Kadish/Pellet Cave/Teledahn}.\n"
    #msg += "or Mir-o-Bot's private ages {aegura/ahnonay/cathedral/cleft/dereno/descent/ercana/gahreesen/gz/gira/hood/jalak/kadish/kemo/minkata/myst/negilahn/office/payiferen/pelletcave/relto/silo/spyroom/teledahn/tetsonot/mobkveer/mobgomepub}.\n"
    msg += "or Mir-o-Bot's private ages {aegura/ahnonay/cathedral/cleft/dereno/descent/...}.\n"
    #msg += "or a Magic age: to {MBCity/MBRelto/MBErcana/MBTeledahn/MBOffice/MBKadish/MBKveer/MBHood/MBDereno/MBRudenna}.\n\n"
    #msg += "linkbotto {fh/fhci/fhde/fhga/fhte/fhka/fhgi/fhcl/mbe/mcl/mre/mkv/mka/scl}: links Mir-o-Bot to the specified Age.\n"
    msg += "linkbotto [age name]: links Mir-o-Bot to the specified Age.\n"
    """
    msg += "   linkbotto fh   = The Fun House\n"
    msg += "   linkbotto fhci = The Fun House - City\n"
    msg += "   linkbotto fhde = Fun House\'s (1) Eder Delin\n"
    msg += "   linkbotto fhga = The Fun House - Gahreesen\n"
    msg += "   linkbotto fhte = The Fun House - Teledahn\n"
    #msg += "   linkbotto fhcl = Fun House\'s Cleft\n"
    msg += "   linkbotto fhka = The Fun House - Kadish Tolesa\n"
    msg += "   linkbotto fhgi = The Fun House - Eder Gira\n"
    msg += "   linkbotto mbe = MagicBot Ercana\n"
    #msg += "   linkbotto mcl = Magic Cleft\n"
    msg += "   linkbotto mre = Magic Relto\n"
    msg += "   linkbotto mkv = Magic Kveer\n"
    msg += "   linkbotto mka = Magic Tolesa\n"
    #msg += "   linkbotto scl = Stone5's Cleft\n\n"
    """
    """
    msg += "aegura, ahnonay, cathedral, cleft, delin, dereno, \n"
    msg += "descent, edercave, ercana, gahreesen, gira, \n"
    msg += "gz, hood, jalak, kadish, \n"
    msg += "kemo, minkata, \n"
    msg += "\n"
    msg += "myst, negilahn, office, payiferen, \n"
    msg += "pelletcave, podscave, primecave, \n"
    msg += "relto, silo, spyroom, \n"
    msg += "teledahn, tetsonot, tiam, \n"
    msg += "training, tsogal.\n"
    
    cleft1, cleft2, 
    gctrl, gctrl2, gear, gnexus, pinnacle, prison, 
    greatshaft, tiwah, 
    greattreepub, 
    greatzero, 
    mobchiso, mobelonin, mobgahreesen, mobgomepub, mobgz, 
    mobkemo, mobkveer, mobrelto, mobserene, mobtiam, mobtrebivdil, 
    mobveelay, mobvothol, 
    myst1, 
    oven, 
    pellet1, pellet2, 
    teledahn2, 
    team, team2, 
    purple, purpleteam, 
    teampurple, teamyellow, 
    , veranda, yellow, yellowteam
    """
    msg += "\n"
    #msg += "   Mir-o-Bot's ages are available too :Ae'gura, Ahnonay, Ahnonay Cathedral, Cleft, Eder Gira, Eder Kemo, Eder Tsogal, Eder Delin, Er'cana, Gahreesen, Hood, Jalak, Kadish, Minkata, Pellet Cave, Relto, Teledahn\n"
    msg += "   Available Mir-o-Bots ages:\n"
    msg += "   aegura, ahnonay, cathedral, cleft, delin, dereno, descent, \n"
    msg += "   edercave, ercana, gahreesen, gira, gz, hood, jalak, kadish, \n"
    msg += "   kemo, minkata, myst, negilahn, office, payiferen, pelletcave, \n"
    msg += "   podscave, primecave, relto, rudenna, silo, spyroom, teledahn, \n"
    msg += "   tetsonot, tiam, tsogal, mobgahreesen, mobgz, mobkemo, mobkveer, mobrelto.\n"
    msg += "   Aliases : tiwah, greatzero\n"
    msg += "   New ages:\n"
    msg += "   mobchiso, mobelonin, mobgomepub, mobserene, mobtiam, \n"
    msg += "   mobtrebivdil, mobveelay, mobvothol.\n"
    msg += "\n"
    msg += "   Some more arrival points in Mir-o-Bots ages that works with the to and linkbotto commands:\n"
    msg += "   Cleft : cleft1, cleft2.\n"
    msg += "   Er'cana : oven.\n"
    msg += "   Gahreesen : gear, pinnacle, training, team, team2, prison, veranda, gctrl, gctrl2, gnexus.\n"
    msg += "      For the Wall games, you can acces to your team control room with:\n"
    msg += "         yellowteam, teamyellow or yellow\n"
    msg += "         purpleteam, teampurple or purple\n"
    msg += "   \n"
    msg1 = msg

    title2 = myself.getPlayerName() + "'s moving help"
    msg = "** MOVING IN Mir-o-Bot AGES:\n"
    msg += "onbot or warp or w : warps your avatar to Mir-o-Bot's current position.\n\n"
    msg += "onlake: Adds an invisible floor and warps you on it.\n"
    msg += "  /!\ Once added by a player all others visiting will have the invisible floor.\n\n"
    msg += "      It will follow you in other ages til you quit the game.\n\n"
    msg += "nolake: Removes the invisible floor, maybe ... (Seems not working anymore)\n"
    msg += "warp or warp [avatar name] or warp [x] [y] [z] : see onbot, find and rgoto.\n (the avatar name can be incomplete).\n\n"
    msg += "wd : warps your avatar to the default linkin point.\n\n"
    msg += " You can save and return to 10 positions in each age with:\n"
    msg += "  save [n] : Save your current position. Where n = 0 to 9\n"
    msg += "  ws [n] : Warps you to your n-th saved position. Where n = 0 to 9\n"
    msg += "  I save them on my disk. You will be able to return to a saved position when you want!\n\n"
    msg += "sp [number]: warps you to a spawn point (number depending of the age). Works in city, ercana, gahreesen, kadish, minkata, teledahn.\n"
    msg += "    City specific spots (sp 0 to sp 22):\n"
    msg += "        Ferry Gate       = FG               (= sp 1)\n"
    msg += "        Ferry Roof       = FR               (= sp 2)\n"
    msg += "        Opera House      = OH               (= sp 3)\n"
    msg += "        Tokotah Roof     = TR               (= sp 4)\n"
    msg += "        Kahlo Roof       = KR               (= sp 5)\n"
    msg += "        Library Roof     = LR               (= sp 6)\n"
    msg += "        Palace Roof      = PR               (= sp 7)\n"
    msg += "        Concert Hall     = CH               (= sp 9)\n"
    msg += "        Museum           = MU               \n"
    msg += "        Tokotah Roof Top = DAKOTAH or TRT   \n"
    msg += "        Palace Balconies = PB1, PB2 and PB3.\n"
    #msg += "        Great Stairs Roof = GSR (= kahlo pub roof)\n"
    #msg += "        Palace Balcony = PB (= palace roof)\n"
    msg += "    Er'cana specific spots (sp or e 0 to 14)\n"
    msg += "    Gahreesen specific spots (sp or g 0 to 34); for wall games : yellowteam, purpleteam)\n"
    msg += "    Kadish specific spots (sp or k 0 to 19)\n"
    msg += "    Minkata specific spots (sp, cave, k, kiva or m 0 to 5)\n"
    msg += "    Teledahn specific spots (sp or t 0 to 19)\n\n"
    msg += "rsph : Rotates the Ahnonay spheres. Works only if the bot is in Ahnonay.\n\n"
    msg += "nopanic : Disables most of the panic zones.\n\n"
    msg += "coord : returns your current position.\n\n"
    msg += "agoto [x] [y] [z] or teleport [x] [y] [z] : disable physics and warps your avatar to an absolute position.\n\n"
    msg += "rgoto [x] [y] [z] or xwarp [x] [y] [z] or warp [x] [y] [z] : disable physics and warps your avatar relative to your current position.\n\n"
    msg += "rot [axis] [angle] : disables physics and rotates your avatar along the specified x, y or z axis, and following the specified angle in degrees.\n\n"
    msg += "turn [angle] : disables physics and rotates your avatar on Z axis relative to your current position.\n\n"
    msg += "float [height]: disables physics and warps your avatar up or down relative to your current position.\n\n"
    msg += "jump [height] or jump [forward] [height]: jump in the air.\n\n"
    msg += "land or normal: enables physics.\n\n"
    msg += "find [object or avatar name]: warps you to the first object or avatar found (use * as any unknown caracters but not only a *), this command is case sensitive.\n\n"
    msg += "list [object name]: shows you the list of object names found (use * as any unknown caracters but not only a *), this command is case sensitive.\n\n"
    msg += "Some animations: [animation name] [n] \n"
    msg += "    where [animation name] is in: \n"
    msg += "    {ladderup/ladderdown/climbup/climbdown/stairs\n"
    msg += "    /walk/run/back/moonwalk/swim\n"
    msg += "    /dance/crazy/what/zomby/hammer/wait/laugh/thank/talk}.\n"
    msg += "    and [n] is the number of times you want to do.\n\n"
    msg2 = msg

    title3 = myself.getPlayerName() + "'s fun help"
    msg = "** HAVING FUN IN Mir-o-Bot AGES:\n"
    msg += " You want to see stars? Try that:\n"
    #msg += "night : To see the Relto by night.\n\n"
    #msg += "night [on/off/scale]: on = enables night, off = disable night, scale = enables night with a specified enlargement of star field.\n"
    msg += "night [on/off]: on = enables night, off = disable night.\n"
    msg += "day : disables night.\n\n"
    #msg += "cms [on/off]: on = enables Colored Moving Sky during 5 minutes, off = disables Colored Moving Sky.\n\n"
    msg += "cms [on/off]: on = enables Colored Moving Sky, off = disables Colored Moving Sky.\n\n"
    #msg += "door [open/close] : opens or closes the bahro door (only in Delin or Tsogal).\n\n"
    msg += "soccer : Drops some soccer balls.\n\n"
    #msg += "drop : Drops some objects.\n\n"
    #msg += "clean : Cleans the previously droped objects.\n\n"
    #msg += "ring [yellow/blue/red/white] [on/off] : Activates and deactivates a ring of Firemarbles (in hood only).\n"
    msg += "ring [yellow/blue/red/white] [on/off] : Activates and deactivates a ring of Firemarbles.\n"
    msg += "    Optionally: ring [color] [on] [height] [radius].\n"
    msg += "    If it not works anymore, you can reset the rings: ring reset.\n\n"
    #msg += "load : loads \"A New Cycle Has Begun\", enjoy!\n\n"
    #msg += "addcleft : Add a partially invisible Cleft and disable panic links, enjoy!\n\n"
    msg += "style [value] : Changes the \"style\". Where value can be default or an age file name (i.e. city for Ae'gura)\n\n"
    msg += "fogshape [start] [end] [density]: Changes the \"shape\" of the fog. Where start, end and density are integers.\n\n"
    msg += "fogcolor [r] [g] [b] : Changes the fog color. Where r, g and b (red, green and blue) are numbers between 0 and 100.\n"
    msg += "fogcolor [color name] : Changes the fog color. Where [color name] can be white, red, pink, orange, brown, yellow, green, blue, violet, purple, black or gold.\n\n"
    msg += "fog [on/off]: Adds or removes the fog layer.\n\n"
    msg += "nofog : Disables the fog.\n\n"
    msg += "skycolor [r] [g] [b] : Changes the sky color. Where r, g and b (red, green and blue) are numbers between 0 and 100.\n"
    msg += "skycolor [color name] : Changes the sky color. Where [color name] can be white, red, pink, orange, brown, yellow, green, blue, violet, purple, black or gold.\n\n"
    msg += "sky [on/off]: Adds or removes the sky layers.\n\n"
    msg += "nosky : Disables the sky.\n\n"
    msg += "sendme : Sends you the list of the marker games I have.\n sendme [id]: Sends you the #id game.\n\n" 
    msg3 = msg

    title4 = myself.getPlayerName() + "'s Jalak help"
    msg = "** HAVING FUN IN Mir-o-Bot JALAK:\n"
    msg += "-- Jalak creations (thanks to Michel) --\n"
    msg += "    savestruct [savename] : Saves a structure.\n"
    msg += "    loadstruct [savename] : Loads a structure.\n"
    msg += "    savecolumns [savename]: Saves only columns.\n"
    msg += "    loadcolumns [savename]: Loads only columns.\n"
    msg += "    savecubes [savename]  : Saves only widgets.\n"
    msg += "    loadcubes [savename]  : Loads only widgets.\n"
    msg += "    resetcubes            : Takes off widgets.\n\n"
    #msg += "\nThats all for the moment."
    msg4 = msg


    helpNote1 = None
    helpNote2 = None
    helpNote3 = None
    helpNote4 = None
    # create the note
    try:
        helpNote1 = ptVaultTextNoteNode(0)
        helpNote1.setText(msg1)
        helpNote1.setTitle(title1)
        #journal.addNode(helpNote1)
    except:
        msg = "An error occured when creating help note 1."
        SendChatMessage(self, myself, [player], msg, cFlags.flags)

    try:
        helpNote2 = ptVaultTextNoteNode(0)
        helpNote2.setText(msg2)
        helpNote2.setTitle(title2)
        #journal.addNode(helpNote2)
    except:
        msg = "An error occured when creating help note 2."
        SendChatMessage(self, myself, [player], msg, cFlags.flags)

    try:
        helpNote3 = ptVaultTextNoteNode(0)
        helpNote3.setText(msg3)
        helpNote3.setTitle(title3)
        #journal.addNode(helpNote3)
    except:
        msg = "An error occured when creating help note 3."
        SendChatMessage(self, myself, [player], msg, cFlags.flags)

    try:
        helpNote4 = ptVaultTextNoteNode(0)
        helpNote4.setText(msg4)
        helpNote4.setTitle(title4)
        #journal.addNode(helpNote4)
    except:
        msg = "An error occured when creating help note 4."
        SendChatMessage(self, myself, [player], msg, cFlags.flags)
    
    msg = "I'm sending you help Ki-mails..."
    SendChatMessage(self, myself, [player], msg, cFlags.flags)
    if helpNote1 is not None and idAvatar is not None and idAvatar != 0 and idAvatar != myself.getPlayerID():
        try:
            helpNote1.sendTo(idAvatar)
        except:
            msg = "An error occured while sending help note 1."
            SendChatMessage(self, myself, [player], msg, cFlags.flags)
    if helpNote2 is not None and idAvatar is not None and idAvatar != 0 and idAvatar != myself.getPlayerID():
        try:
            helpNote2.sendTo(idAvatar)
        except:
            msg = "An error occured while sending help note 2."
            SendChatMessage(self, myself, [player], msg, cFlags.flags)
    if helpNote3 is not None and idAvatar is not None and idAvatar != 0 and idAvatar != myself.getPlayerID():
        try:
            helpNote3.sendTo(idAvatar)
        except:
            msg = "An error occured while sending help note 3."
            SendChatMessage(self, myself, [player], msg, cFlags.flags)
    if helpNote4 is not None and idAvatar is not None and idAvatar != 0 and idAvatar != myself.getPlayerID():
        try:
            helpNote4.sendTo(idAvatar)
        except:
            msg = "An error occured while sending help note 4."
            SendChatMessage(self, myself, [player], msg, cFlags.flags)
    
    msg = "You can also use \"help [command name]\".\n ** Available commands : " + ", ".join(list(cmdDict.keys()))
    SendChatMessage(self, myself, [player], msg, cFlags.flags)
    return 1

# Envoie un message d'aide specifique a une commande
def HelpCmd(self, player, cFlags, cmdName):
    #PtSendKIMessage(kKILocalChatStatusMsg, "> HelpCmd")
    myself = PtGetLocalPlayer()
    try:
        cmdName = RetreaveCmdName(cmdName)
    except:
        pass
    #raccourcis pour les animations (sans taper "anim")
    animCmd = RetreaveAnimCmdName(cmdName)
    if animCmd:
        cmdName = "anim"
    #traitement "normal"
    if cmdName in cmdDict:
        helps = cmdDict[cmdName][1]
        for msg in helps:
            SendChatMessage(self, myself, [player], msg, cFlags.flags)    
    else:
        #command not found, PM command list
        msg = "\"" + cmdName + "\" not found."
        SendChatMessage(self, myself, [player], msg, cFlags.flags)
        #msg = "Available commands: " + ", ".join(cmdDict.keys())
        #SendChatMessage(self, myself, [player], msg, cFlags.flags)
    return 1

# Envoyer la liste complete des animations au demandeur
def SendAnimListNote(self, cFlags, args = []):
    #PtSendKIMessage(kKILocalChatStatusMsg, "> SendAnimListNote")
    if len(args) < 1:
        PtSendKIMessage(kKILocalChatStatusMsg, "** SendAnimListNote: no arg! **")
        print("** SendAnimListNote: no arg! **")
        return 0
    myself = PtGetLocalPlayer()
    player = args[0]
    idAvatar = player.getPlayerID()
    
    msg = "** SendAnimListNote: sending to \"{0}\" [{1}]. **".format(player.getPlayerName(), idAvatar)
    PtSendKIMessage(kKILocalChatStatusMsg, msg)
    print(msg)
    
    # Ne rien envoyer si le joueur n'est pas un ami (ca va peut-etre eviter les plantages)
    if not xPlayers.IsBud(idAvatar):
        print("This player is not yet my friend => Don't send anything!")
        return 1
    
    # create the note
    try:
        helpNote = ptVaultTextNoteNode(0)
        helpNote.setText(AnimationList.containt)
        helpNote.setTitle(AnimationList.title)
    except:
        msg = "An error occured when creating the list of animations note."
        SendChatMessage(self, myself, [player], msg, cFlags.flags)
    
    msg = "I'm sending you the list of animations KI-mail ..."
    SendChatMessage(self, myself, [player], msg, cFlags.flags)
    if helpNote is not None and idAvatar is not None and idAvatar != 0 and idAvatar != myself.getPlayerID():
        try:
            helpNote.sendTo(idAvatar)
        except:
            msg = "An error occured while sending the list of animations note."
            SendChatMessage(self, myself, [player], msg, cFlags.flags)
    return 1


#----------------------------------------------------------------------------#
#   Dictionnaire Commande/Methode/(help)
#----------------------------------------------------------------------------#
cmdDict = {
    'link':(LinkHere,["link or meet : links your avatar to Mir-o-Bot's current Age."]),
    #'linkbotto':(LinkBotTo,["linkbotto {fh/fhci/fhde/fhga/fhte/fhka/fhgi/fhcl/mbe/mcl/mre/mkv/mka/scl}:", 
    #'linkbotto':(LinkBotTo,["linkbotto {hood/aegura/relto/...//fh/fhci/fhcl/fhde/fhga/fhgi/fhka/fhte//mbe/mka/mkv/mre}:", 
    'linkbotto':(LinkBotTo,["linkbotto {aegura/cathedral/cleft/dereno/descent/ercana/gahreesen/gira/hood/jalak/kadish/kemo/minkata/myst/negilahn/office/payiferen/pelletcave/relto/silo/spyroom/teledahn/tetsonot}:", 
        " links Mir-o-Bot to the specified Age."]),
    #'to':(LinkToPublicAge,["to {city/dakotah/greeters/kirel/kveer/watcher/...} : links you to a public age or a Mir-o-bot age (aegura/hood/teledahn/...)."]),
    'to':(LinkToPublicAge,["to {city/library/ferry/dakotah/tokotah/concert/palace} : links YOU to different points of the public city or some public ages (kirel/kveer/pub/gog/gome) or a Mir-o-bot age (aegura/hood/teledahn/...)."]),
    'onbot':(WarpToMe,["onbot or warp or w: warps your avatar to Mir-o-Bot's current position."]),
    'wd':(WarpToDefaultLinkInPoint,["wd: warps your avatar to the default linkin point."]),
    'warp':(Warp,["warp or warp [avatar name] or warp [x] [y] [z] : see onbot, find and rgoto."]),
    'onlake':(OnLake,["onlake: Adds an invisible floor and warps you on it."]),
    'nolake':(NoLake,["nolake: Removes the invisible floor, maybe ..."]),
    'coord':(GetCoord,["coord : returns your current position."]),
    'save':(SavePosition,["save [n]: saves your current position. Where n = 0 to 9"]),
    'ws':(ReturnToPosition,["ws [n]: warps you to your n-th saved position. Where n = 0 to 9 (if exists)."]),
    'agoto':(AbsoluteGoto,["agoto [x] [y] [z] or teleport [x] [y] [z] :", 
        " disable physics and warps your avatar to an absolute position. Where x, y and z are numbers."]),
    'rgoto':(RelativeGoto,["rgoto [x] [y] [z] or xwarp [x] [y] [z] or warp [x] [y] [z] :", 
        " disable physics and warps your avatar relative to your current position. Where x, y and z are numbers"]),
    'dnigoto':(AbsoluteDniGoto,["dnigoto [toran] [hSpan] [vSpan] :", 
        " disable physics and warps your avatar to an absolute D'ni position. Where [toran], [hSpan] and [vSpan] are integers."]),
    'land':(Land,["land or normal: enables physics."]),
    'turn':(RotateZ,["turn [angle] : disables physics and rotates your avatar on Z axis relative to your current position."]),
    'rot':(Rotate,["rot [axis] [angle] : disables physics and rotates your avatar along the specified x, y or z axis,", 
        " and following the specified angle in degrees."]),
    'float':(Float,["float [height] or float [forward] [height]: disables physics and warps your avatar up or down relative to your current position."]),
    'jump':(Jump,["jump [height] or jump [forward] [height]: jump in the air. Where forward and height are numbers"]),
    'find':(Find,["find [object or avatar name]:", 
        " warps you to the avatar", 
        " or the first object found (use * as any unknown caracters but not a * alone), this command is case sensitive.\n\"list [object name]\" will help you to find object names"]),
    'list':(ShowSceneObjects,["list [object name]: shows you the list of object names found (use * as any unknown caracters but not a * alone), this command is case sensitive.\nTry \"find [one of the listed objects]\""]),
    'anim':(Animer, ["[animation name] [n] [f/m/b]: where", 
        "- [animation name] is in the animation list (PM me animlist to have it)", 
    #    "    {ladderup/ladderdown/climbup/climbdown/stairs", 
    #    "    /walk/run/back/moonwalk/swim", 
    #    "    /dance/crazy/what/zomby/hammer/wait/laugh/thank/talk}.", 
        "- [n] is the number of times you want to do it.",
        "- [f/m/b] (optional) f = female animation, m = male animation, b = bahro animation."]),
    'animlist':(SendAnimListNote, ["animlist : Sends you a KI-mail contains the list of the avatar's animations"]),
    #'addcleft':(AddCleft,["addcleft: adds partially invisible Cleft."]),
    #'load':(LoadNewDesert,["load: loads \"A New Cycle Has Begun\"."]),
    'sp':(WarpToSpawnPoint,["sp [number]: warps you to a spawn point. Number is an integer, the max depending of the age."]),
    'ki':(KiLight,["ki [on/off] : Activates and deactivates KI light."]),
    'light':(BugsLight,["light [on/off] : Activates and deactivates Eder Kemo bug lights ."]),
    'bugs':(Bugs,["bugs [on/off] : Calls the Eder Kemo bugs."]),
    'soccer':(Soccer,["Drops some soccer balls."]),
    #'drop':(Drop,["Drops some objects."]),
    #'clean':(Clean,["Cleans the objects previously droped."]),
    #'ring':(Ring,["ring [yellow/blue/red/white] [on/off] : Activates and deactivates a ring of Firemarbles (IN HOOD ONLY). Optionally: ring [color] [on] [height] [radius]"]),
    'ring':(Ring,["ring [yellow/blue/red/white/reset] [on/off] : Activates and deactivates a ring of Firemarbles. Optionally: ring [color] [on] [height] [radius]."]),
    #'unloadclones':(UnloadClones, [""]),
    #'reloadclones':(ReloadClones, [""]),
    'countclones':(CountClones, [""]),
    'nopanic':(DisablePanicLinks,["Disables most of the panic zones."]),
    #'board':(Board,["board : Shows the score board."]),
    'door':(OpenOrCloseBahroDoor,["door [open/close] : the bahro door (in Delin or Tsogal only)."]),
    'skin':(SkinColor,["skin [r] [g] [b] : Changes your skin tint. Where r, g and b are numbers between 0 and 1."]),
    #'night1':(CreateReltoNight1_v1,["night1 [on/off]: No need to explain."]),
    'night':(CreateReltoNight1,["night [on/off/scale]: on = enables night, off = disables night, scale = enables night with a specified enlargement of star field."]),
    #'night2':(CrimsonNight,["night2 [on/off/scale]: on = enables night, off = disable night, scale = enables night with a specified enlargement of star field."]),
    'night2':(CreateReltoNight2,["night2 [style]: on = enables night, off = disables night, style = enables night with a specified color style name."]),
    'cms':(ColoredMovingSky,["cms [on/off]: on = enables Colored Moving Sky during 5 minutes, off = disables Colored Moving Sky."]),
    'day':(ReltoDay,["day [on/off]: Opposite of 'night'."]),
    #'day2':(ReltoDay2,["day2 [on/off]: Opposite of 'night2'."]),
    'style':(SetRendererStyle,["style [value] : Changes the \"style\". Where value can be default or an age file name (i.e. city for Ae'gura)"]),
    'fogshape':(SetRendererFogLinear,["fogshape [start] [end] [density]: Changes the \"shape\" of the fog. Where start, end and density are integers."]),
    'fogcolor':(SetRendererFogColor,["fogcolor [r] [g] [b] or fogcolor [color name]: Changes the fog color. Where r, g and b (red, green and blue) are numbers between 0 and 100."]),
    'nofog':(DisableFog,["Disables the fog."]),
    'fog':(FogOnOff,["fog [on/off]: Adds or removes the fog layer."]),
    'skycolor':(SetRendererClearColor,["skycolor [r] [g] [b] or skycolor [color name]: Changes the sky color. Where r, g and b (red, green and blue) are numbers between 0 and 100."]),
    'sky':(SkyOnOff,["sky [on/off]: Adds or removes the sky layers."]),
    'nosky':(DisableSky,["Disables the sky."]),
    'savestruct': (xJalak.SaveStruct,["savestruct [savename]: Saves a structure (Works in Jalak only)."]),
    'loadstruct': (xJalak.LoadStruct,["loadstruct [savename]: Loads a structure (Works in Jalak only)."]),
    'savecolumns':(xJalak.SaveColumns,["savecolumns [savename]: Saves only columns (Works in Jalak only)."]),
    'loadcolumns':(xJalak.LoadColumns,["loadcolumns [savename]: Loads only columns (Works in Jalak only)."]),
    'savecubes':  (xJalak.SaveCubes,["savecubes [savename]: Saves only widgets (Works in Jalak only)."]),
    'loadcubes':  (xJalak.LoadCubes,["loadcubes [savename]: Loads only widgets (Works in Jalak only)."]),
    'resetcubes:':(xJalak.ResetCubes,["resetcubes: Takes off widgets (Works in Jalak only)."]),
    'event':(SpecialEventCommand,["Special Event Command."]),
    #'add':(AddClone,["AddClone (test)."]),
    'sdl':(ToggleHoodSDL,["sdl [name] : Toggles some sdl in hood only."]),
    #'lift':(ColumnUnderPlayer,["lift : Puts a column below you."]), #version 1
    'lift':(ColumnUnderPlayer2,["lift or lift [up/down/off]: Puts a column below you."]), #version 2
    'column':(ColumnInFrontOfPlayer,["column [up/down]: Puts a column in front of you."]),
    #'allonme':(Cercle,["allonme : Warps all players around you."]),
    'sendme':(SendGame, ["sendme : Sends you the list of the marker games I have.", "sendme [id]: Sends you the #id game."]), 
    'ride':(RideAnimal,["ride [AnimalName] : To ride an animal. [AnimalName] can be bahro, urwin, sandscrit... (WARNING: may not not works perfectly and may cause crash!)"]),
    'startdance':(StartDance,["startdance [dance name]: Starts the dance named [dance name]."]),
    'stopdance':(StopDance,["stopdance : Stops the active dance."]),
    'rsph':(RotateAhnonaySphere, ["rsph : Rotates the Ahnonay spheres. Works only if the bot is in Ahnonay."]),
    'saveme':(SaveMe,["saveme [name]: Saves my clothing in a file named [name]."]),
    'restoreme':(RestoreMe,["restoreme [name]: Loads the clothing named [name]."]),
    'vis':(ToggleVisibility,["vis [on/off]: Makes you visible or invisible."]),
    'campfire':(PutCampFireHere,["campfire [on/off]: Puts a campfire where you are."]),
    #exemple:
    #'macommande':(MaMethode,["ligne d'aide 1", "ligne d'aide 2", "etc."]),
    'help':(Help, ["help: sends you a help text note.", "help [command name]: PM you a specific help on a command."])
}
#Trions cette liste
#cmdKeyList = sorted(cmdDict)

# Nom alternatifs des commandes (alias)
alternatives = {
    'link':['link', 'meet', 'linkme', 'lier'],
    'linkbotto':['linkbotto', 'sendbotto', 'botto'],
    'to':['to', 'linkmeto', 'sendmeto'],
    'onbot':['w', 'onbot'],
    'warp':['warp', 'vers', 'move', 'moveto', 'moveme', 'movemeto'],
    'wd':['wd', 'a'],
    'coord':['coord', 'locate', 'pos'],
    'agoto':['agoto', 'teleport'],
    'rgoto':['rgoto', 'xwarp'],
    'land':['land', 'normal', 'nofloat'],
    'turn':['turn'],
    'rot':['rot', 'rotate'],
    'float':['float', 'fl', 'fly', 'flotte'],
    'jump':['jump', 'j', 'runjump', 'rj', 'saut'],
    'find':['find', 'fi', 'warpto', 'wt', 'trouve'],
    'list':['list', 'show', 'search', 's', 'montre'],
    'help':['help', 'h', 'elp', 'aide', '?'],
    'anim':['anim', 'animation'],
    'animlist':['animlist', 'animationlist', 'listanim', 'listanimation', 'listofanim', 'listofanimation', 'animslist', 'animationslist', 'listanims', 'listanimations', 'listofanims', 'listofanimations'],
    'light':['light', 'aura'],
    'fogshape':['fogshape', 'fogdensity'],
    'column':['col', 'colonne'],
    'onlake':['lakeon', 'lake'],
    'nolake':['lakeoff', 'onlakeoff', 'offlake'],
    'rsph':['rsph', 'rotsphere', 'rotspheres', 'rotatesphere', 'rotatespheres', 'turnsphere', 'turnspheres'],
    'vis':['vis', 'visible'],
    'campfire':['campfire', 'firecamp'],
    'startdance':['startdance', 'startshow'],
    'stopdance':['startdance', 'stopshow'],
}

# Noms alternatifs des animations
altAnim = {
    'danse'     :['danse'     , 'dance', 'tanz', 'balla', 'bailar'],
    'danseretro':['danseretro', 'danceretro', 'retrodanse', 'retrodance', 'retrotanz', 'balloretro', 'baileretro'],
    'fou'       :['fou'       , 'crazy'],
    'echelle'   :['echelle'   , 'climbup', 'climb'],
    'ladderup'  :['ladderup'],
    'descendre' :['descendre' , 'climbdown'],
    'ladderdown':['ladderdown'],
    'escalier'  :['escalier'  , 'stairs'],
    'quoi'      :['quoi'      , 'what'],
    'nage'      :['nage'      , 'swim'],
    'moonwalk'  :['moonwalk'],
    'zombie'    :['zombie'    , 'zomby', 'ombie', 'omby'],
    'marteau'   :['marteau'   , 'hammer'],
    'attente'   :['attente'   , 'wait'],
    'rire2'     :['rire2'     , 'laugh2'],
    'merci'     :['merci'     , 'thank', 'thanks'],
    'marche'    :['marche'    , 'walk'],
    'cours'     :['cours'     , 'run'],
    'recule'    :['recule'    , 'back'],
    'parler'    :['parler'    , 'talk'],
    'brasse'    :['brasse'    , 'swimslow'],
    'pasdroite' :['pasdroite' , 'stepright'],
    'pasgauche' :['pasgauche' , 'stepleft'],
    # Other simple animations
    "agree"               : ["agree", "yes", "oui"], 
    "amazed"              : ["amazed", "etonne"], 
    "askquestion"         : ["askquestion", "ask", "question"], 
    "ballpushwalk"        : ["ballpushwalk"], 
    "beckonbig"           : ["beckonbig"], 
    "beckonsmall"         : ["beckonsmall"], 
    "blowkiss"            : ["blowkiss"], 
    "bow"                 : ["bow"], 
    "callme"              : ["callme"], 
    "cheer"               : ["cheer"], 
    "clap"                : ["clap"], 
    "cough"               : ["cough"], 
    "cower"               : ["cower"], 
    "cringe"              : ["cringe"], 
    "crossarms"           : ["crossarms"], 
    "cry"                 : ["cry", "cries"], 
    "doh"                 : ["doh"], 
    "fall"                : ["fall"], 
    "fall2"               : ["fall2"], 
    "flinch"              : ["flinch"], 
    "groan"               : ["groan"], 
    "groundimpact"        : ["groundimpact"], 
    "kiglance"            : ["kiglance"], 
    "kneel"               : ["kneel"], 
    "ladderdown"          : ["ladderdown"], 
    "ladderdownoff"       : ["ladderdownoff"], 
    "ladderdownon"        : ["ladderdownon"], 
    "ladderup"            : ["ladderup"], 
    "ladderupoff"         : ["ladderupoff"], 
    "ladderupon"          : ["ladderupon"], 
    "laugh"               : ["laugh", "lol", "rotfl"], 
    "leanleft"            : ["leanleft"], 
    "leanright"           : ["leanright"], 
    "lookaround"          : ["lookaround"], 
    "okay"                : ["okay"], 
    "overhere"            : ["overhere"], 
    "peer"                : ["peer"], 
    "point"               : ["point"], 
    "runningimpact"       : ["runningimpact"], 
    "runningjump"         : ["runningjump"], 
    "salute"              : ["salute"], 
    "scratchhead"         : ["scratchhead"], 
    "shakefist"           : ["shakefist"], 
    "shakehead"           : ["shakehead", "no", "non"], 
    "shoo"                : ["shoo"], 
    "shrug"               : ["shrug", "dontknow", "dunno"], 
    "sideswimleft"        : ["sideswimleft"], 
    "sideswimright"       : ["sideswimright"], 
    "sit"                 : ["sit"], 
    "slouchsad"           : ["slouchsad"], 
    "sneeze"              : ["sneeze"], 
    "standingjump"        : ["standingjump"], 
    "stop"                : ["stop"], 
    "swimbackward"        : ["swimbackward"], 
    "swimfast"            : ["swimfast"], 
    "talkhand"            : ["talkhand"], 
    "tapfoot"             : ["tapfoot"], 
    "taunt"               : ["taunt"], 
    "thx"                 : ["thx"], 
    "thumbsdown"          : ["thumbsdown"], 
    "thumbsdown2"         : ["thumbsdown2"], 
    "thumbsup"            : ["thumbsup"], 
    "thumbsup2"           : ["thumbsup2"], 
    "treadwaterturnleft"  : ["treadwaterturnleft"], 
    "treadwaterturnright" : ["treadwaterturnright"], 
    "turnleft"            : ["turnleft"], 
    "turnright"           : ["turnright"], 
    "walkingjump"         : ["walkingjump"], 
    "wallslide"           : ["wallslide"], 
    "wave"                : ["wave", "wavebye"], 
    "wavelow"             : ["wavelow"], 
    "winded"              : ["winded"], 
    "yawn"                : ["yawn"], 
    # Thoses other animations are working everywhere
    "buttontouch"         : ["buttontouch"],
    "doorbuttontouch"     : ["doorbuttontouch"],
    "floorlevera"         : ["floorlevera"],
    "floorleveraup"       : ["floorleveraup"],
    "globalscopegrab"     : ["globalscopegrab"],
    "globalscopehold"     : ["globalscopehold"],
    "globalscoperelease"  : ["globalscoperelease"],
    #"kihand"              : ["kihand"],
    #"kihandlonger"        : ["kihandlonger"],
    "kibegin"             : ["kibegin"],
    "kiend"               : ["kiend"],
    "kitap"               : ["kitap"],
    "kiuse"               : ["kiuse"],
    "pelletbookleft"      : ["pelletbookleft"],
    "pelletbookright"     : ["pelletbookright"],
    "pelletbookwait"      : ["pelletbookwait"],
    #"personnallink"       : ["personnallink"],
    "shootertrapactivate" : ["shootertrapactivate"],
    "shortidle"           : ["shortidle"],
    "shortleap"           : ["shortleap"],
    "sitfront"            : ["sitfront"],
    "sitidle"             : ["sitidle"],
    "sitidleground"       : ["sitidleground"],
    "steponfloorplate"    : ["steponfloorplate"],
    # ** These should also work everywhere **
    "afkidle"                 : ["afkidle"],
    "blindsleverdown"         : ["blindsleverdown"],
    "blindsleverup"           : ["blindsleverup"],
    "blndfrntleverdown"       : ["blndfrntleverdown"],
    "blndfrntleverup"         : ["blndfrntleverup"],
    "bookaccept"              : ["bookaccept"],
    "bookacceptidle"          : ["bookacceptidle"],
    "bookoffer"               : ["bookoffer"],
    "bookofferfinish"         : ["bookofferfinish"],
    "bookofferidle"           : ["bookofferidle"],
    "insertkihand"            : ["insertkihand"],
    "insertkihandlonger"      : ["insertkihandlonger"],
    "softlanding"             : ["softlanding"],
    "touchpellet"             : ["touchpellet"],
    # ** These only work in Ahnonay **
    "swimdockexit"            : ["swimdockexit"],
    "swimsurfacedive"         : ["swimsurfacedive"],
    "swimunderwater"          : ["swimunderwater"],
    "valvewheelcw"            : ["valvewheelcw"],
    "valvewheelccw"           : ["valvewheelccw"],
    # ** These only work in Er'cana **
    "floorleverapullhard"     : ["floorleverapullhard"],
    "floorleverapushhard"     : ["floorleverapushhard"],
    "floorleverastuck"        : ["floorleverastuck"],
    "floorleveraup"           : ["floorleveraup"],
    "hatchlockedbelow"        : ["hatchlockedbelow"],
    "hrvstrleverbackward"     : ["hrvstrleverbackward"],
    "hrvstrleverforward"      : ["hrvstrleverforward"],
    "pushdebris"              : ["pushdebris"],
    # ** These only work in Cleft **
    "cleftdropin"             : ["cleftdropin"],
    "windmilllockedccw"       : ["windmilllockedccw"],
    "windmilllockedcw"        : ["windmilllockedcw"],
    # ** These only work in Gahreesen **
    "elevatorarrivingbottom"  : ["elevatorarrivingbottom"],
    "elevatorarrivingtop"     : ["elevatorarrivingtop"],
    "elevatorleavingbottom"   : ["elevatorleavingbottom"],
    "elevatorleavingtop"      : ["elevatorleavingtop"],
    "wallclimbdismountdown"   : ["wallclimbdismountdown"],
    "wallclimbdismountleft"   : ["wallclimbdismountleft"],
    "wallclimbdismountright"  : ["wallclimbdismountright"],
    "wallclimbdismountup"     : ["wallclimbdismountup"],
    "wallclimbdown"           : ["wallclimbdown"],
    "wallclimbidle"           : ["wallclimbidle"],
    "wallclimbleft"           : ["wallclimbleft"],
    "wallclimbright"          : ["wallclimbright"],
    "wallclimbmountdown"      : ["wallclimbmountdown"],
    "wallclimbmountleft"      : ["wallclimbmountleft"],
    "wallclimbmountright"     : ["wallclimbmountright"],
    "wallclimbmountup"        : ["wallclimbmountup"],
    # ** These only work in Eder Gira **
    "fumerolclothjump"        : ["fumerolclothjump"],
    "fumerolledgeblast"       : ["fumerolledgeblast"],
    "fumerolrockblast"        : ["fumerolrockblast"],
    "vertblastlevel01"        : ["vertblastlevel01"],
    "vertblastlevel02"        : ["vertblastlevel02"],
    "vertblastlevel03"        : ["vertblastlevel03"],
    "vertblastlevel04"        : ["vertblastlevel04"],
    "vertblastlevel05"        : ["vertblastlevel05"],
    "vertblastlevel06"        : ["vertblastlevel06"],
    # ** These only work in Teledahn **
    "aquariumbuttonhold"      : ["aquariumbuttonhold"],
    "aquariumbuttonpress"     : ["aquariumbuttonpress"],
    "aquariumbuttonrelease"   : ["aquariumbuttonrelease"],
    "clutchlevergeargrind"    : ["clutchlevergeargrind"],
    "dropoutofbucket"         : ["dropoutofbucket"],
    "getinbucket"             : ["getinbucket"],
    "getoutofbucket"          : ["getoutofbucket"],
    "hatchclose"              : ["hatchclose"],
    "hatchlockedabove"        : ["hatchlockedabove"],
    "hatchlockedbelow"        : ["hatchlockedbelow"],
    "hatchopenabove"          : ["hatchopenabove"],
    "hatchopenbelow"          : ["hatchopenbelow"],
    "noxiouscavedoorpullopen" : ["noxiouscavedoorpullopen"],
    "noxiouscavedoorpushopen" : ["noxiouscavedoorpushopen"],
    "noxiousdoorclose"        : ["noxiousdoorclose"],
    "powertowerprimerbutton"  : ["powertowerprimerbutton"],
    "powertowerprimerlevers"  : ["powertowerprimerlevers"],
    "secretwallbutton"        : ["secretwallbutton"],
}

travelAnimList = ("echelle", "descendre", "ladderup", "ladderdown", "escalier", "nage", "marche", "cours", "recule", "pasdroite", "pasgauche", "brasse")

def RetreaveCmdName(altCmdName):
    for k, v in list(alternatives.items()):
        if altCmdName.lower() in v:
            return str(k)
    return altCmdName

def RetreaveAnimCmdName(altCmdName):
    for k, v in list(altAnim.items()):
        if altCmdName.lower() in v:
            return str(k)
    return None

def RetreaveSPCmd(altCmdName):
    altSP = {
        "city":[
            "fg", "fr", "oh", "tr", "gsr", "kr", "lr", "pb", "pr", "ch", 
            "mu", "trt", "pb1", "pb2", "pb3", "museum", "dakotah", "ferry", 
            "alley", "concert", "greattree", "library", "palace", "gallery"
        ],
        "ercana":["e", "e1", "e2", "e3", "e4", "e5", "e6", "e7", "e8", "e9", "e10", "e11", "e12", "e13", "e14"],
        "kadish":["k", "k1", "k2", "k3", "k4", "k5", "k6", "k7", "k8", "k9", "k10", "k11", "k12", "k13", "k14", "k15", "k16", "k17", "k18", "k19"],
        "minkata":[
            "m", "k", "cave", "kiva", 
            "m0", "k0", "cave0", "kiva0", 
            "m1", "k1", "cave1", "kiva1", 
            "m2", "k2", "cave2", "kiva2", 
            "m3", "k3", "cave3", "kiva3", 
            "m4", "k4", "cave4", "kiva4", 
            "m5", "k5", "cave5", "kiva5", 
            ], 
        "teledahn":["t", "t1", "t2", "t3", "t4", "t5", "t6", "t7", "t8", "t9", "t10", "t11", "t12", "t13", "t14", "t15", "t16", "t17", "t18", "t19"],
        "garrison":[
            "g", "g1", "g2", "g3", "g4", "g5", "g6", "g7", "g8", "g9", 
            "g10", "g11", "g12", "g13", "g14", "g15", "g16", "g17", "g18", "g19", 
            "g20", "g21", "g22", "g23", "g24", "g25", "g26", "g27", "g28", "g29", 
            "g30", "g31", "g32", "g33", "g34", "g35", "yellowteam", "teamyellow", "yellow", "purpleteam", "teampurple", "purple"
            ],
    }
    ageInfo = PtGetAgeInfo()
    ageFileName = ageInfo.getAgeFilename().lower()
    if ageFileName in list(altSP.keys()):
        if altCmdName.lower() in altSP[ageFileName]:
            return altCmdName.lower()
    return None

def RetreaveCmd(altCmd, args):
    if altCmd == "no":
        if len(args) > 1:
            if args[1] in ["ki", "light", "aura", "night", "sky", "fog", "bug", "bugs", "lake"]:
                print("(a): {} off".format(args[1]))
                cmd = "{} off".format(args[1])
                args.pop(1)
                return cmd
    if altCmd in ["open", "close"]:
        if len(args) > 1:
            if args[1] == "door":
                print("(b): door {}".format(altCmd))
                cmd = "door {}".format(altCmd)
                args.pop(1)
                return cmd
    altCmds = {
        "ki on":["kion",],
        "ki off":["kioff", "noki"],
        "light on":["lighton", "auraon"],
        "light off":["lightoff", "auraoff", "nolight"],
        "door open":["opendoor", "dooropen"],
        "door close":["closedoor", "doorclose"],
        "night on":["nighton", "starson"],
        "night off":["nightoff", "nonight", "starsoff"],
        "sky on":["skyon",],
        "sky off":["skyoff", "nosky"],
        "fog on":["fogon",],
        "fog off":["fogoff", "nofog"],
        "bugs on":["bugson", "flieson", "fireflieson"],
        "bugs off":["bugsoff", "nobug", "firefliesoff"],
        "vis on":["vison", "vis1", "vistrue", "visible", "unhideme", "showme"],
        "vis off":["visoff", "vis0", "visfalse", "invisible", "hideme"],
        }
    for k, v in list(altCmds.items()):
        if altCmd.lower() in v:
            print("(c): {}".format(k))
            return str(k)
    return None


#----------------------------------------------------------------------------#
#   Method to call the desired method
#----------------------------------------------------------------------------#
"""
 Appelee par xKiBot.py, permet d'appeler toutes les autres methodes
 Suivant les modele:
def MaMethode(self, cFlags, args = []):
    #histoire de savoir que quelqu'un a appele cette methode
    PtSendKIMessage(kKILocalChatStatusMsg, "> MaMethode")
    #Testons la presence de parametres, normalement "player" a ete ajoute automatiquement
    if len(args) < 1:
        #Pas de parametre ==> erreur
        return 0
    myself = PtGetLocalPlayer()
    player = args[0]
    # Si la commande a besoin de parametres (autre que le joueur)
    if len(args) < 2:
        #Pas de parametre ==> erreur
        return 0
    # Decomposons la chaine qui contient les parametres separes par des espaces
    params = args[1].split()
    # En avons-nous assez? (ici 2)
    if len(params) < 2:
        #Pas assez de parametres ==> erreur
        return 0
    #Si la commande doit etre executee dans l'age du robot
    if not isPlayerInAge(player):
        SendChatMessage(self, myself, [player], "You must be in my age, use link to join me.", cFlags.flags)
        return 1
    #...
    return 1
"""
#amIRobot = 0
#
def CallMethod(self, cmdName, cFlags, pAmIRobot, args=[]):
    xBotAge.AmIRobot = pAmIRobot
    print("xBotAge.AmIRobot = {}".format(xBotAge.AmIRobot))
    #traiter les noms de commande alternatifs
    try:
        cmdName = RetreaveCmdName(cmdName)
        #PtSendKIMessage(kKILocalChatStatusMsg, "=> " + cmdName)
    except:
        pass
    #raccourcis pour les animations (sans taper "anim")
    animCmd = RetreaveAnimCmdName(cmdName)
    if animCmd:
        if len(args) > 1:
            args[1] = animCmd + " " + args[1]
        else:
            args.append(animCmd + " 1")
        cmdName = "anim"
    #raccourcis pour les spawn points
    spAlias = RetreaveSPCmd(cmdName)
    if spAlias is not None:
        cmdName = "sp"
        if len(args) > 1:
            args[1] = spAlias + args[1]
        else:
            args.append(spAlias)
    #commande agglutinee
    if len(args) > 1:
        print("avant: {} {}".format(cmdName, args[1]))
    #cmdAndArgs = RetreaveCmd(cmdName, args)
    #cmd = cmdAndArgs[0]
    #args = cmdAndArgs[1]
    cmd = RetreaveCmd(cmdName, args)
    if cmd is not None:
        cmdNameAndArg = cmd.split(" ", 1)
        cmdName = cmdNameAndArg[0]
        args.append(cmdNameAndArg[1])
    
    if len(args) > 1:
        print("apres: {} {}".format(cmdName, args[1]))
    #traitement "normal"
    if cmdName in cmdDict:
        #PtSendKIMessage(kKILocalChatStatusMsg, "** CallMethod: \"{}\" found. **".format(cmdName))
        print(("** CallMethod: \"{}\" found. **".format(cmdName)))
        ret = None
        # During events I may have to disable all the commands but warp to bot
        if bBlockCmds:
            #
            #authorizedCmds = ('onbot', 'link')
            # During Cavern Tours
            #authorizedCmds = ('link', 'to', 'onbot', 'wd', 'warp', 'nolake', 'coord', 'save', 'ws', 'agoto', 'rgoto', 'dnigoto', 'land', 'turn', 'rot', 'float', 'jump', 'find', 'list', 'anim', 'sp', 'ki', 'light', 'nopanic', 'sdl', 'sendme', 'help')
            authorizedCmds = () # aucune commande autorisee par defaut quand je bloque les non admin
            myself = PtGetLocalPlayer()
            if myself.getPlayerID() != 2332508: # si je ne suis pas mob, j'en debloque quelques unes
                #authorizedCmds = ('link', 'to', 'onbot', 'wd', 'warp', 'onlake', 'nolake', 'coord', 'save', 'ws', 'agoto', 'rgoto', 'dnigoto', 'land', 'turn', 'rot', 'float', 'jump', 'find', 'list', 'anim', 'sp', 'ki', 'light', 'nopanic', 'sdl', 'sendme', 'help')
                #authorizedCmds = ('link', 'to', 'onbot', 'wd', 'warp', 'coord', 'save', 'ws', 'agoto', 'rgoto', 'land', 'turn', 'rot', 'float', 'jump', 'find', 'list', 'anim', 'sp', 'ki', 'light', 'nopanic', 'saveme', 'sendme', 'restoreme', 'help')
                #authorizedCmds = ('onbot', 'link')
                authorizedCmds = () # ou pas!
            if cmdName not in authorizedCmds:
                #myself = PtGetLocalPlayer()
                player = args[0]
                if player.getPlayerID() not in adminList :
                    if not authorizedCmds:
                        msg = "Sorry, I'm not available for the moment."
                    else:
                        #msg = "An event is running, only the W / LINK commands are enabled."
                        #msg = "Cavern Tour is running, only basic commands are enabled."
                        msg = "An event is running, only basic commands are enabled."
                    SendChatMessage(self, myself, [player], msg, cFlags.flags)  
                    return 1
        if len(args) == 0:
            #return cmdDict[cmdName][0]()
            ret = cmdDict[cmdName][0]()
        else:
            isBuddyAdded = xPlayers.AddBud(args[0].getPlayerID())
            if isBuddyAdded:
                PtSendKIMessage(kKILocalChatStatusMsg, "----> '{0}' [{1}] a ete ajoute a mes buddies.".format(args[0].getPlayerName(), args[0].getPlayerID()))
            ret = cmdDict[cmdName][0](self, cFlags, args)
        #PtSendKIMessage(kKILocalChatStatusMsg, "** CallMethod: \"{}\" returned: {}. **".format(cmdName, ret))
        print(("** CallMethod: \"{}\" returned: {}. **".format(cmdName, ret)))
        return ret
    else:
        return 0
