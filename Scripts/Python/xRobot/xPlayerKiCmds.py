# -*- coding: utf-8 -*-

from Plasma import *

import math
import datetime
import re

import xPlayers
import xBotAge
import xAnim
import xSave
import xSave2
import xJalak

import CloneObject
import sdl
import Columns2

#Ages de Mirphak, Mir-o-Bot, MagicBot, ages publics
import ages

import MarkerGames

import Ride
import Ahnonay

import CloneBugs
import DropObjects
import ReltoNight
import ReltoNight2
import xCleft
import xDelin
import xHood
import xRelto
import xScore
import xTsogal

import Dance

#----------------------------------------------------------------------------#
#   Attributs globaux
#----------------------------------------------------------------------------#
debugInfo = ""
bJalakAdded = False
bBlockCmds = False
adminList = [32319L, 31420L, 2332508L]
adminList += [
]

# liste des instances disponibles pour moi
#linkDic = xBotKiCmds.linkDic

# Authorized age instances
allowedAgeInstanceGuids = {
}

lastLinkTime = datetime.datetime.now()

#----------------------------------------------------------------------------#
#   Methodes
#----------------------------------------------------------------------------#

## Usage interne

### Display a message to the player (or players).
def SendChatMessage(self, fromPlayer, plyrList, message, flags):
    plyrNameList = map(lambda pl: pl.getPlayerName(), plyrList)
    plyrList = filter(lambda pl: pl.getPlayerID() != PtGetLocalPlayer().getPlayerID(), plyrList)
    if message is None:
        message = "Oops, I forgot what I had to tell you!"
    if len(plyrList) > 0:
        # Don't take care of flags nor bots, always send message as buddies inter-age
        PtSendRTChat(fromPlayer, plyrList, message, 24)
    self.chatMgr.DisplayStatusMessage("sent to [" + ",".join(plyrNameList) + "] : " + message)

#Pour savoir si le joueur est dans l'age du robot
def isPlayerInAge(player):
    #self.chatMgr.AddChatLine(None, "> isPlayerInAge", 3)
    if player.getPlayerID() == PtGetLocalPlayer().getPlayerID():
        return True
    agePlayers = PtGetPlayerList()
    ids = map(lambda player: player.getPlayerID(), agePlayers)
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
    #self.chatMgr.AddChatLine(None, "> SearchAvatarNameLike", 3)
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
    players = filter(lambda player: pattern.match(player.getPlayerName().lower()), agePlayers)
    if len(players) == 0:
        players = filter(lambda player: player.getPlayerName().lower().replace(" ", "") == name.replace(" ", ""), agePlayers)
    return players


def GetAgePlayerByName(name):
    #self.chatMgr.AddChatLine(None, "> GetAgePlayerByName", 3)
    players = SearchAvatarNameLike(name)
    if len(players) > 0:
        return players[0]
    else:
        return None


##Les methodes suivantes peuvent etre appelees par un autre joueur

# voir dans xBotAge, la methode LinkPlayerToPublic
def LinkToPublicAge(self, cFlags, args = []):
    #self.chatMgr.AddChatLine(None, "> LinkToPublicAge", 3)
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
    #self.chatMgr.AddChatLine(None, "> LinkHere ", 3)
    if len(args) < 1:
        self.chatMgr.AddChatLine(None, "> LinkHere: len(args) = " + str(len(args)), 3)
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
        self.chatMgr.AddChatLine(None, ", ".join(xBotAge.currentBotAge), 3)
        xBotAge.LinkPlayerTo(self, xBotAge.currentBotAge, player.getPlayerID())
        SendChatMessage(self, myself, [player], "Welcome to " + botAgeName, cFlags.flags)
    return 1

def WarpToMe(self, cFlags, player):
    #self.chatMgr.AddChatLine(None, "> WarpToMe", 3)
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
    #self.chatMgr.AddChatLine(None, "> WarpToPlayer", 3)
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
    #self.chatMgr.AddChatLine(None, "> WarpToDefaultLinkInPoint", 3)
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
    #self.chatMgr.AddChatLine(None, "> WarpToSpawnPoint", 3)
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
            #self.chatMgr.AddChatLine(None, "> " + spName, 3)
        else:
            SendChatMessage(self, myself, [player], "Unknown spawn point!" , cFlags.flags)
    elif spawnPointAlias is not None:
        pos = xBotAge.GetSPByAlias(spawnPointAlias)[0]
        spName = xBotAge.GetSPByAlias(spawnPointAlias)[1]
        SendChatMessage(self, myself, [player], spName, cFlags.flags)
        #self.chatMgr.AddChatLine(None, "> " + spName, 3)
    else:
        return 0
    if isinstance(pos, ptMatrix44):
        soAvatar = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
        soAvatar.netForce(1)
        soAvatar.physics.warp(pos)
    return 1

def FindSceneObjectPosition(self, name):
    #self.chatMgr.AddChatLine(None, "> FindSceneObjectPosition", 3)
    o = list(name + "not found!")
    so = xBotAge.GetFirstSoWithCoord(name)
    if so:
        pos = so.position()
        o = list(so.getName(), pos.getX(), pos.getY(),  pos.getZ())
    return o

#def FindClonePosition(self, name):
#    self.chatMgr.AddChatLine(None, "> FindClonePosition", 3)
#    o = list(name + "not found!")
#    so = xBotAge.GetFirstClonePosition(name)
#    if so:
#        pos = so.position()
#        o = list(so.getName(), pos.getX(), pos.getY(),  pos.getZ())
#    return o

def ShowSceneObjects(self, cFlags, args = []):
    #self.chatMgr.AddChatLine(None, "> ShowSceneObjects", 3)
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
    #self.chatMgr.AddChatLine(None, "> Red", 3)
    if type(player) == list and len(player) > 0:
        av = PtGetAvatarKeyFromClientID(player[0].getPlayerID()).getSceneObject()
        av.avatar.netForce(1)
        av.avatar.tintSkin(ptColor().red())
        return 1
    else:
        return 0

#
def SkinColor(self, cFlags, args = []):
    #self.chatMgr.AddChatLine(None, "> SkinColor player r g b", 3)
    if len(args) < 2:
        #self.chatMgr.AddChatLine(None, "> SkinColor len(args) = {}".format(len(args)), 3)
        msg = "skin needs 3 parameters, none given."
        self.chatMgr.AddChatLine(None, msg, 3)
        #PtSendRTChat(myself, [player], msg, cFlags.flags)
        return 0
    myself = PtGetLocalPlayer()
    player = args[0]
    colors = args[1].split()
    if len(colors) != 3:
        msg = "skin needs 3 parameters, {} given.".format(len(colors))
        self.chatMgr.AddChatLine(None, msg, 3)
        SendChatMessage(self, myself, [player], msg, cFlags.flags)
        return 1
    try:
        r = float(colors[0].strip().lower())
        g = float(colors[1].strip().lower())
        b = float(colors[2].strip().lower())
    except:
        self.chatMgr.AddChatLine(None, "> r, g and b must be floating points numbers between 0 and 1", 3)
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
#    self.chatMgr.AddChatLine(None, "> Bugs", 3)
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
    self.chatMgr.AddChatLine(None, "> Bugs", 3)
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
    #self.chatMgr.AddChatLine(None, "> Bugs", 3)
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
            self.chatMgr.AddChatLine(None, "> Bugs: player is None!!", 3)
        elif isinstance(player, ptPlayer):
            self.chatMgr.AddChatLine(None, "> Bugs: player {0} ({1}) has no sceneobject attribute!".format(player.getPlayerName(), player.getPlayerID()), 3)
        else:
            self.chatMgr.AddChatLine(None, "> Bugs: player is not None nor a ptPlayer!!", 3)
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
    #self.chatMgr.AddChatLine(None, "> GetPeople", 3)
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
        selPlyrList = filter(lambda pl: not(pl.getPlayerID() in xPlayers.dicBot.keys()), selPlyrList)
    return selPlyrList

#
def RemovePrpToLocal(self):
    global bJalakAdded
    self.chatMgr.AddChatLine(None, "> RemovePrpToLocal", 3)
    xCleft.DelPrpLocal()
    Columns2.DelPrpLocal()
    bJalakAdded = False
    #Platform.DelPrpLocal()
    #xBugs.DelPrpLocal()
    #xPub.DelPrpLocal()
    #xRelto.DelPrpLocal()
    #xSpy.DelPrpLocal()
    #ridePages = ["psnlMYSTII", "Desert", "clftSceneBahro", "tldnHarvest", "DrnoExterior", "kemoGarden", "Jungle", "Pod", "giraCanyon", "bahroFlyers_arch", "bahroFlyers_city1", "bahroFlyers_city2", "bahroFlyers_city3", "bahroFlyers_city4", "bahroFlyers_city5", "bahroFlyers_city6"]


# link the robot to an age instance
#def LinkBotTo(player, linkName):
def LinkBotTo(self, cFlags, args = []):
    global lastLinkTime
    #self.chatMgr.AddChatLine(None, "> LinkBotTo", 3)
    now = datetime.datetime.now()
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
    for lk  in ages.MirobotAgeDict.keys():
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
    # Trying Mir-o-Bot ages
    if (linkName in ages.MirobotAgeDict.keys()):
        link = ages.MirobotAgeDict[linkName]
#        xBotAge.currentBotAge = list(link)
#        if len(link) > 4:
#            xBotAge.SetBotAgeSP(link[4])
#            #self.chatMgr.AddChatLine(None, ",".join(xBotAge.currentBotAge), 3)
#        xBotAge.LinkPlayerTo(self, link)
    # Trying MagicBot ages
    elif (linkName in ages.MagicbotAgeDict.keys()):
        link = ages.MagicbotAgeDict[linkName]
#        xBotAge.currentBotAge = list(link)
#        if len(link) > 4:
#            xBotAge.SetBotAgeSP(link[4])
#            #self.chatMgr.AddChatLine(None, ",".join(xBotAge.currentBotAge), 3)
#        xBotAge.LinkPlayerTo(self, link)
    elif (linkName in ages.PublicAgeDict.keys()):
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
            agePlayers = filter(lambda pl: not(pl.getPlayerID() in xPlayers.dicBot.keys()), PtGetPlayerList())
            #for pl in agePlayers:
            #    if (pl.getPlayerID() in xPlayers.dicBot.keys()):

            # ne permettre le deplacement du robot que s'il est seul ou avec le demandeur (autres robots exclus)
            if len(agePlayers) == 0 or (agePlayers[0].getPlayerID() == player.getPlayerID()):
                #prevenir que l'on m'a demander de me lier vers un autre age
                msg = myself.getPlayerName() + " is linking to " + link[0] + " for at least " + str(minDiff / 60) + " minute(s)... PM me \"link\" to follow me."
                #Garder Les prp des autres ages peut faire planter lors de la liaison...
                RemovePrpToLocal(self)
                DelPrpLocal(pageBugs)
                
                xBotAge.currentBotAge = list(link)
                if len(link) > 4:
                    xBotAge.SetBotAgeSP(link[4])
                    self.chatMgr.AddChatLine(None, ",".join(xBotAge.currentBotAge), 3)
                # Decharger les ages clones
                # Liaison
                xBotAge.LinkPlayerTo(self, link)
                lastLinkTime = datetime.datetime.now()
                
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
    #self.chatMgr.AddChatLine(None, "> GetCoord", 3)
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
    #self.chatMgr.AddChatLine(None, "> Find", 3)
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
    #self.chatMgr.AddChatLine(None, "> AbsoluteDniGoto", 3)
    print "AbsoluteDniGoto"
    if len(args) < 2:
        print "AbsoluteDniGoto: {0} arguments given.".format(len(args))
        return 0
    params = args[1].split()
    myself = PtGetLocalPlayer()
    player = args[0]
    if len(params) < 3:
        print "AbsoluteDniGoto: {0} parameters given.".format(len(params))
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
    #self.chatMgr.AddChatLine(None, "> AbsoluteGoto", 3)
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
    #self.chatMgr.AddChatLine(None, "> RelativeGoto", 3)
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
    #self.chatMgr.AddChatLine(None, "> Land", 3)
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
    #self.chatMgr.AddChatLine(None, "> Float", 3)
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
    #self.chatMgr.AddChatLine(None, "> Jump", 3)
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
    #self.chatMgr.AddChatLine(None, "> Warp", 3)
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
    #self.chatMgr.AddChatLine(None, "> Rotate", 3)
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
    #self.chatMgr.AddChatLine(None, "> RotateZ", 3)
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
    self.chatMgr.AddChatLine(None, "> SavePosition", 3)
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
    #self.chatMgr.AddChatLine(None, "> ReturnToPosition", 3)
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
    #self.chatMgr.AddChatLine(None, "> SavePosition", 3)
    if len(args) < 1:
        return 0
    myself = PtGetLocalPlayer()
    player = args[0]
    if not isPlayerInAge(player):
        SendChatMessage(self, myself, [player], "You must be in my age, use link to join me." , cFlags.flags)
        return 1
    strIndex = "0"
    if len(args) > 1:
        strIndex = args[1]
    xSave2.WriteMatrix44(self, strIndex, player)
    SendChatMessage(self, myself, [player], "Your position is saved. Use \"ws " + strIndex + "\" to return to this position." , cFlags.flags)
    return 1

# Warp the avatar to his last saved position
def ReturnToPosition(self, cFlags, args = []):
    #self.chatMgr.AddChatLine(None, "> ReturnToPosition", 3)
    if len(args) < 1:
        return 0
    myself = PtGetLocalPlayer()
    player = args[0]
    if not isPlayerInAge(player):
        SendChatMessage(self, myself, [player], "You must be in my age, use link to join me." , cFlags.flags)
        return 1
    strIndex = "0"
    if len(args) > 1:
        strIndex = args[1]
    ret = xSave2.WarpToSaved(self, strIndex, player)
    if ret:
        SendChatMessage(self, myself, [player], "You are at your saved position " + strIndex + "." , cFlags.flags)
    else:
        SendChatMessage(self, myself, [player], "No saved position found. Did you use \"save [0 to 9]\" before?" , cFlags.flags)
    return 1


# Faire faire une animation a l'avatar demandeur
def Animer(self, cFlags, args = []):
    #self.chatMgr.AddChatLine(None, "> Animer", 3)
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
    ret = xAnim.Play(player, animName, nbTimes)
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
    self.chatMgr.AddChatLine(None, "> AddCleft", 3)
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
    self.chatMgr.AddChatLine(None, "> LoadNewDesert", 3)
    if len(args) < 1:
        return 0
    myself = PtGetLocalPlayer()
    player = args[0]
    if not isPlayerInAge(player):
        SendChatMessage(self, myself, [player], "You must be in my age, use link to join me.", cFlags.flags)
        return 1
    import newdesert
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
        self.chatMgr.AddChatLine(None, "Panic links are disabled!", 3)
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
    self.chatMgr.AddChatLine(None, ">Ring ", 3)
    
    #1st parameter: color (or reset)
    color = params[0].lower().strip()
    
    if color == "reset":
        try:
            xHood.ResetClones()
            self.chatMgr.AddChatLine(None, "The clones are reseted!", 3)
            SendChatMessage(self, myself, [player], "The rings are reseted, you can try to create one again!" , cFlags.flags)
            return 1
        except:
            self.chatMgr.AddChatLine(None, "Err: I failed to reset the clones!", 3)
            SendChatMessage(self, myself, [player], "I failed to reset the rings!" , cFlags.flags)
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
            if params[1].lower().strip().isnumeric():
                params.insert(1, 'on')
        
    dist = 3
    height = 4
    #3rd parameter: height
    if len(params) > 2:
        try:
            height = float(params[2].lower().strip())
        except:
            self.chatMgr.AddChatLine(None, "Err: the optional 3rd parameter must be a number!", 3)
            SendChatMessage(self, myself, [player], "The optional 3rd parameter, height, must be a number!" , cFlags.flags)
            return 1
    #4th parameter: distance
    if len(params) > 3:
        try:
            dist = float(params[3].lower().strip())
        except:
            self.chatMgr.AddChatLine(None, "Err: the optional 4th parameter must be a number!", 3)
            SendChatMessage(self, myself, [player], "The optional 4th parameter, radius, must be a number!" , cFlags.flags)
            return 1
    self.chatMgr.AddChatLine(None, "ring {}, {}".format(color, bOn), 3)
    xHood.Entourer(dist, height, color, 9, soAvatar, bOn)
    self.chatMgr.AddChatLine(None, "=> nb clones: {}".format(xHood.CompterClonesBilles()), 3)
    if bOn:
        SendChatMessage(self, myself, [player], "I'm creating a fire marble ring for you, wait a bit ..." , cFlags.flags)
    else:
        SendChatMessage(self, myself, [player], "I'm destroying the fire marble ring ..." , cFlags.flags)
    return 1
    #else:
    #    self.chatMgr.AddChatLine(None, "=> Je ne suis pas dans un Hood!", 3)
    #    #PtSendRTChat(myself, [player], "This command does'nt work here, we must be in a Hood." , cFlags.flags)
    #    return 1
    #else:
    #    self.chatMgr.AddChatLine(None, "=> Je ne sais pas dans quel age je suis!", 3)
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
            self.chatMgr.AddChatLine(None, "=> Je ne suis pas a Ahnonay!", 3)
            SendChatMessage(self, myself, [player], "This command does'nt work here, we must be in Ahnonay." , cFlags.flags)
            return 1
    else:
        self.chatMgr.AddChatLine(None, "=> Je ne sais pas dans quel age je suis!", 3)
        SendChatMessage(self, myself, [player], "Oops, I don't know where I am ..." , cFlags.flags)
        return 1

# To open or close a Bahro door (in Eder Delin and Eder Tsogal currently)
def OpenOrCloseBahroDoor(self, cFlags, args = []):
    if len(args) < 2:
        return 0
    myself = PtGetLocalPlayer()
    player = args[0]
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
        self.chatMgr.AddChatLine(None, "=> I don't know how to %s a door!" % (sOpenOrClose), 3)
        SendChatMessage(self, myself, [player], "I don't know how to %s a door!" , cFlags.flags)
        return 1
    # age cases
    if len(xBotAge.currentBotAge) > 1:
        if xBotAge.currentBotAge[1] == "EderDelin":
            self.chatMgr.AddChatLine(None, "OpenOrCloseBahroDoor %s, %s" % (xBotAge.currentBotAge[1], action), 3)
            xDelin.Door(action)
            SendChatMessage(self, myself, [player], "Ok, I am %s the door ..." % (sAction) , cFlags.flags)
        elif xBotAge.currentBotAge[1] == "EderTsogal":
            self.chatMgr.AddChatLine(None, "OpenOrCloseBahroDoor %s, %s" % (xBotAge.currentBotAge[1], action), 3)
            xTsogal.Door(action)
            SendChatMessage(self, myself, [player], "Ok, I am %s the door ..." % (sAction) , cFlags.flags)
        else:
            self.chatMgr.AddChatLine(None, "=> Cette fonction ne fonctionne pas dans cet age!", 3)
            SendChatMessage(self, myself, [player], "This command does'nt work here." , cFlags.flags)
    else:
        self.chatMgr.AddChatLine(None, "=> Je ne sais pas dans quel age je suis!", 3)
        SendChatMessage(self, myself, [player], "Oops, I don't know where I am ..." , cFlags.flags)
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
        self.chatMgr.AddChatLine(None, "Fog gone!", 3)
        SendChatMessage(self, myself, [player], "Fog gone!", cFlags.flags)
        return 1
    except:
        self.chatMgr.AddChatLine(None, "Error in DisableFog", 3)
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
        self.chatMgr.AddChatLine(None, "> SetRendererStyle: {}".format(vstyle), 3)
        SendChatMessage(self, myself, [player], "{} style".format(vstyle), cFlags.flags)
        return 1
    else:
        self.chatMgr.AddChatLine(None, "> SetRendererStyle: no param given.", 3)
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
        self.chatMgr.AddChatLine(None, "> SetRendererFogLinear: shape = ({}, {}, {}).".format(vstart, vend, vdensity), 3)
        SendChatMessage(self, myself, [player], "Fog shape changed.", cFlags.flags)
        return 1
    else:
        self.chatMgr.AddChatLine(None, "> SetRendererFogLinear: no param given.", 3)
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
                if strCol in dicColors.keys():
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
        self.chatMgr.AddChatLine(None, "> SetRendererFogColor: color = ({}, {}, {}).".format(vr, vg, vb), 3)
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
        self.chatMgr.AddChatLine(None, "> SetRendererFogColor: no param given.", 3)
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
                if strCol in dicColors.keys():
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
        self.chatMgr.AddChatLine(None, "> SetRendererClearColor: color = ({}, {}, {}).".format(vcr, vcg, vcb), 3)
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
        self.chatMgr.AddChatLine(None, "> SetRendererClearColor: no param given.", 3)
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
            self.chatMgr.AddChatLine(None, "=> Je ne sais pas dans quel age je suis!", 3)
            SendChatMessage(self, myself, [player], "Oops, I don't know where I am ..." , cFlags.flags)
        self.chatMgr.AddChatLine(None, "> CreateReltoNight1: {}".format(msg), 3)        
        return 1
    except:
        self.chatMgr.AddChatLine(None, "> CreateReltoNight1: Error.", 3)
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
            self.chatMgr.AddChatLine(None, "=> Je ne sais pas dans quel age je suis!", 3)
            if scale is None:
                #scale = 75
                scale = 300
        #msg = xRelto.CreateNightSky(scale, bOn)
        msg = ReltoNight.CreateNightSky(scale, bOn)
        self.chatMgr.AddChatLine(None, "> CreateReltoNight1: {}".format(msg), 3)        
        return 1
    except:
        self.chatMgr.AddChatLine(None, "> CreateReltoNight1: Error.", 3)
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
        self.chatMgr.AddChatLine(None, "> CreateReltoNight1: {}".format(msg), 3)        
        return 1
    except:
        self.chatMgr.AddChatLine(None, "> CreateReltoNight1: Error.", 3)
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
        self.chatMgr.AddChatLine(None, "> ColoredMovingSky: {}".format(msg), 3)        
        return 1
    except:
        self.chatMgr.AddChatLine(None, "> ColoredMovingSky: Error.", 3)
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
        #self.chatMgr.AddChatLine(None, "> FogOnOff: {} done.".format(bOn), 3)
        SendChatMessage(self, myself, [player], "Fog is {}.".format(state), cFlags.flags)
        return 1
    except:
        self.chatMgr.AddChatLine(None, "> FogOnOff: Error.", 3)
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
        #self.chatMgr.AddChatLine(None, "> SkyOnOff: {} done.".format(bOn), 3)
        SendChatMessage(self, myself, [player], "Sky is {}.".format(state), cFlags.flags)
        return 1
    except:
        self.chatMgr.AddChatLine(None, "> SkyOnOff: Error.", 3)
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
        print ">> Soccer : soAvatar"
        soAvatar = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
        print ">> Soccer : pos"
        pos = soAvatar.position()
        print ">> Soccer : ready to drop soccer balls ({} - {})".format(soAvatar, pos)
        DropObjects.Soccer(position=pos)
        print ">> Soccer : done"
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
            xBotAge.ToggleSceneObjects("Sky", age = None, bDrawOn = bOff, bPhysicsOn = True)
            xBotAge.ToggleSceneObjects("sky", age = None, bDrawOn = bOff, bPhysicsOn = True)
            xBotAge.ToggleSceneObjects("Dome", age = None, bDrawOn = bOff, bPhysicsOn = True)
            xBotAge.ToggleSceneObjects("Mountain", age = None, bDrawOn = bOff, bPhysicsOn = True)
            xBotAge.ToggleSceneObjects("nb01", age = "Kveer", bDrawOn = bOff, bPhysicsOn = bOn)
            CloneObject.Minkata(bShow=bOn, bLoad=bOn)
            CreateReltoNight1(self, cFlags, [args[0], onOff])
        """
        if eventNumber == 1:
            # -- 1 -- A Cleft avec ZandiMobile + clone de Minkata + nuit
            print "==> event 1"
            xBotAge.ToggleSceneObjects("Blocker", age = "Cleft", bDrawOn = bOn, bPhysicsOn = bOff)
            xBotAge.ToggleSceneObjects("ProxyPropertyLine", age = "Cleft", bDrawOn = bOn, bPhysicsOn = bOff)
            xBotAge.ToggleSceneObjects("Sky", age = None, bDrawOn = bOff, bPhysicsOn = True)
            xBotAge.ToggleSceneObjects("sky", age = None, bDrawOn = bOff, bPhysicsOn = True)
            xBotAge.ToggleSceneObjects("Dome", age = None, bDrawOn = bOff, bPhysicsOn = True)
            xBotAge.ToggleSceneObjects("Mountain", age = None, bDrawOn = bOff, bPhysicsOn = True)
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
            print "==> event 2"
            xBotAge.ToggleSceneObjects("Sky", age = None, bDrawOn = bOff, bPhysicsOn = True)
            xBotAge.ToggleSceneObjects("sky", age = None, bDrawOn = bOff, bPhysicsOn = True)
            xBotAge.ToggleSceneObjects("Dome", age = None, bDrawOn = bOff, bPhysicsOn = True)
            xBotAge.ToggleSceneObjects("Mountain", age = None, bDrawOn = bOff, bPhysicsOn = True)
            print "==> Minkata ground"
            CloneObject.Minkata(bShow=bOn, bLoad=bOn)
            print "==> GT sky"
            CloneObject.co(["SphereEnviron", "SphereClouds"], "GreatTreePub", 1, bShow=bOn, bLoad=bOn)
            # mettre l'Arche devant le Pod:
            print "==> Arch"
            #tupMat = ((-0.762557864189,-0.646920084953,0.0,30.8849506378),(0.646920084953,-0.762557864189,0.0,-12.7307682037),(0.0,0.0,1.0,-0.0328427329659),(0.0,0.0,0.0,1.0))
            tupMat = ((-0.541980564594,0.840391099453,0.0,86.2719726562),(-0.840391099453,-0.541980564594,0.0,82.5392074585),(0.0,0.0,1.0,-21.8916854858),(0.0,0.0,0.0,1.0))
            #print "==> Arch 2"
            mat = ptMatrix44()
            #print "==> Arch 3"
            mat.setData(tupMat)
            #print "==> Arch 4"
            CloneObject.co3("ArchOfKerath", "city", bShow=bOn, bLoad=bOn, scale=.2, matPos=mat)
            # mettre le sandscrit dans le Pod:
            print "==> Sandscrit"
            tupMat = ((-0.275523930788,-0.961294174194,0.0,15.0463008881),(0.961294174194,-0.275523930788,0.0,3.88983178139),(0.0,0.0,1.0,2.06506371498),(0.0,0.0,0.0,1.0))
            mat = ptMatrix44()
            mat.setData(tupMat)
            #SandscritRoot
            #SandscritFlipper
            #Sandscrit_Mover
            CloneObject.co3("SandscritRoot", "Payiferen", bShow=bOn, bLoad=bOn, scale=0.2, matPos=mat)
            #CloneObject.co3("Sandscrit_Mover", "Payiferen", bShow=bOn, bLoad=bOn, scale=0.2, matPos=mat)
            print "==> nuit"
            if onOff == "on":
                CreateReltoNight1(self, cFlags, [args[0], 60])
            else:
                CreateReltoNight1(self, cFlags, [args[0], onOff])
            SendChatMessage(self, myself, [player], "Event 2 (Payiferen/GreatTreePub/ArchOfKerath) is {0}".format(onOff), cFlags.flags)
        elif eventNumber == 3:
            # -- 3 -- 
            print "==> event 3"
            xBotAge.ToggleSceneObjects("Sky", age = None, bDrawOn = bOff, bPhysicsOn = True)
            xBotAge.ToggleSceneObjects("sky", age = None, bDrawOn = bOff, bPhysicsOn = True)
            xBotAge.ToggleSceneObjects("Dome", age = None, bDrawOn = bOff, bPhysicsOn = True)
            xBotAge.ToggleSceneObjects("Mountain", age = None, bDrawOn = bOff, bPhysicsOn = True)
            print "==> Minkata ground"
            CloneObject.Minkata(bShow=bOn, bLoad=bOn)
            print "==> 2 Tails Monkey"
            tupMat = ((-0.275523930788,-0.961294174194,0.0,15.0),(0.961294174194,-0.275523930788,0.0,3.9),(0.0,0.0,1.0,11.5),(0.0,0.0,0.0,1.0))
            mat = ptMatrix44()
            mat.setData(tupMat)
            #CloneObject.co3("2Tails_Root", "Negilahn", bShow=bOn, bLoad=bOn, scale=0.2, matPos=mat)
            #CloneObject.co3("TempMonkeyHandle", "Negilahn", bShow=bOn, bLoad=bOn, scale=5)
            CloneObject.co3("TempMonkeyHandle", "Negilahn", bShow=bOn, bLoad=bOn, scale=5, matPos=mat)
            SendChatMessage(self, myself, [player], "Event 3 (Negilahn) is {0}".format(onOff), cFlags.flags)
        elif eventNumber == 4:
            # -- 4 -- 
            print "==> event 4"
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
            
            xBotAge.ToggleSceneObjects("Sky", age = None, bDrawOn = bOff, bPhysicsOn = True)
            xBotAge.ToggleSceneObjects("sky", age = None, bDrawOn = bOff, bPhysicsOn = True)
            xBotAge.ToggleSceneObjects("Dome", age = None, bDrawOn = bOff, bPhysicsOn = True)
            xBotAge.ToggleSceneObjects("Mountain", age = None, bDrawOn = bOff, bPhysicsOn = True)
            print "==> Gira sky"
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
            print "==> event 5"
            xBotAge.ToggleSceneObjects("Sky", age = None, bDrawOn = bOff, bPhysicsOn = True)
            xBotAge.ToggleSceneObjects("sky", age = None, bDrawOn = bOff, bPhysicsOn = True)
            xBotAge.ToggleSceneObjects("Dome", age = None, bDrawOn = bOff, bPhysicsOn = True)
            xBotAge.ToggleSceneObjects("Mountain", age = None, bDrawOn = bOff, bPhysicsOn = True)
            #xBotAge.ToggleSceneObjects("Cloud", age = None, bDrawOn = bOff, bPhysicsOn = True)
            xBotAge.ToggleSceneObjects("Back", age = None, bDrawOn = bOff, bPhysicsOn = True)
            xBotAge.ToggleSceneObjects("Fog", age = None, bDrawOn = bOff, bPhysicsOn = True)
            xBotAge.ToggleSceneObjects("Sphere", age = None, bDrawOn = bOff, bPhysicsOn = True)
            xBotAge.ToggleSceneObjects("Dust", age = None, bDrawOn = bOff, bPhysicsOn = True)
            xBotAge.ToggleSceneObjects("Pod", age = None, bDrawOn = bOff, bPhysicsOn = True)
            xBotAge.ToggleSceneObjects("Rain", age = None, bDrawOn = bOff, bPhysicsOn = True)
            print "==> Gira sky"
            CloneObject.co3("SkyGlobe", "Payiferen", bShow=bOn, bLoad=bOn)
            CloneObject.co3("StarSphere", "Payiferen", bShow=bOn, bLoad=bOn)
            SendChatMessage(self, myself, [player], "Event 5 (Payiferen sky) is {0}".format(onOff), cFlags.flags)
        elif eventNumber == 6:
            # -- 6 -- 
            print "==> event 6"
            xBotAge.ToggleSceneObjects("Sky", age = None, bDrawOn = bOff, bPhysicsOn = True)
            xBotAge.ToggleSceneObjects("sky", age = None, bDrawOn = bOff, bPhysicsOn = True)
            xBotAge.ToggleSceneObjects("Dome", age = None, bDrawOn = bOff, bPhysicsOn = True)
            xBotAge.ToggleSceneObjects("Mountain", age = None, bDrawOn = bOff, bPhysicsOn = True)
            #xBotAge.ToggleSceneObjects("Cloud", age = None, bDrawOn = bOff, bPhysicsOn = True)
            xBotAge.ToggleSceneObjects("Back", age = None, bDrawOn = bOff, bPhysicsOn = True)
            xBotAge.ToggleSceneObjects("Fog", age = None, bDrawOn = bOff, bPhysicsOn = True)
            xBotAge.ToggleSceneObjects("Sphere", age = None, bDrawOn = bOff, bPhysicsOn = True)
            xBotAge.ToggleSceneObjects("Dust", age = None, bDrawOn = bOff, bPhysicsOn = True)
            xBotAge.ToggleSceneObjects("Pod", age = None, bDrawOn = bOff, bPhysicsOn = True)
            xBotAge.ToggleSceneObjects("Rain", age = None, bDrawOn = bOff, bPhysicsOn = True)
            print "==> Dereno fish C01"
            CloneObject.co3("C01_Root", "Dereno", bShow=bOn, bLoad=bOn)
            SendChatMessage(self, myself, [player], "Event 6 (Dereno) is {0}".format(onOff), cFlags.flags)
        elif eventNumber == 7:
            # -- 7 -- 
            print "==> event 7"
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
            print "==> event 8 : City, Kahlo Pub, Memorial, Gerbes"
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
            print "==> event 9 : K'veer, Lights for NULP Dance Show"
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
            print "==> event 10 : Jalak, Lights for NULP Dance Show"
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
            print "==> event 91 : K'veer, Lights for NULP Dance Show"
            soPlayer = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
            LightForKveer2(av=soPlayer, num=1, bLoadShowOn=bOn, bAttachOn=bOn)
            SendChatMessage(self, myself, [player], "Event 91 (Projectors) is {0}".format(onOff), cFlags.flags)
        elif eventNumber == 92:
            # -- 92 -- 
            print "==> event 92 : K'veer, Lights for NULP Dance Show"
            soPlayer = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
            LightForKveer2(av=soPlayer, num=2, bLoadShowOn=bOn, bAttachOn=bOn)
            SendChatMessage(self, myself, [player], "Event 92 (Projectors) is {0}".format(onOff), cFlags.flags)
        elif eventNumber == 93:
            # -- 93 -- 
            print "==> event 93 : K'veer, Lights for NULP Dance Show"
            soPlayer = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
            LightForKveer2(av=soPlayer, num=3, bLoadShowOn=bOn, bAttachOn=bOn)
            SendChatMessage(self, myself, [player], "Event 93 (Projectors) is {0}".format(onOff), cFlags.flags)
        elif eventNumber == 94:
            # -- 94 -- 
            print "==> event 94 : K'veer, Lights for NULP Dance Show"
            soPlayer = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
            LightForKveer2(av=soPlayer, num=4, bLoadShowOn=bOn, bAttachOn=bOn)
            SendChatMessage(self, myself, [player], "Event 94 (Projectors) is {0}".format(onOff), cFlags.flags)
        elif eventNumber == 95:
            # -- 95 -- 
            print "==> event 95 : K'veer, Lights for NULP Dance Show"
            soPlayer = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
            LightForKveer2(av=soPlayer, num=5, bLoadShowOn=bOn, bAttachOn=bOn)
            SendChatMessage(self, myself, [player], "Event 95 (Projectors) is {0}".format(onOff), cFlags.flags)
        elif eventNumber == 96:
            # -- 96 -- 
            print "==> event 96 : K'veer, Lights for NULP Dance Show"
            soPlayer = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
            LightForKveer2(av=soPlayer, num=6, bLoadShowOn=bOn, bAttachOn=bOn)
            SendChatMessage(self, myself, [player], "Event 96 (Projectors) is {0}".format(onOff), cFlags.flags)
        elif eventNumber == 97:
            # -- 97 -- 
            print "==> event 97 : K'veer, Lights for NULP Dance Show"
            soPlayer = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
            LightForKveer2(av=soPlayer, num=7, bLoadShowOn=bOn, bAttachOn=bOn)
            SendChatMessage(self, myself, [player], "Event 97 (Projectors) is {0}".format(onOff), cFlags.flags)
        elif eventNumber == 98:
            # -- 98 -- 
            print "==> event 98 : K'veer, Lights for NULP Dance Show"
            soPlayer = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
            LightForKveer2(av=soPlayer, num=8, bLoadShowOn=bOn, bAttachOn=bOn)
            SendChatMessage(self, myself, [player], "Event 98 (Projectors) is {0}".format(onOff), cFlags.flags)
        elif eventNumber == 99:
            # -- 99 -- 
            print "==> event 99 : K'veer, Lights for NULP Dance Show"
            soPlayer = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
            LightForKveer2(av=soPlayer, num=9, bLoadShowOn=bOn, bAttachOn=bOn)
            SendChatMessage(self, myself, [player], "Event 99 (Projectors) is {0}".format(onOff), cFlags.flags)
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
        print "==> OnLake 4"
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
        print "ColumnUnderPlayer2 : args[1] = [{}]".format(args[1])
        params = args[1].split()
        print "ColumnUnderPlayer2 : len(params) = {}".format(len(params))
        if len(params) > 0:
            print "params[0]='{}'".format(params[0])
            try:
                fXAngle = float(params[0])
                print "fXAngle={}".format(fXAngle)
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
                    print "Error on params[0]='{}'".format(params[0])
        if len(params) > 1:
            print "params[0]='{}'".format(params[1])
            try:
                fYAngle = float(params[1])
                print "fYAngle={}".format(fYAngle)
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
                    print "Error on params[1]='{}'".format(params[1])
        if len(params) > 2:
            print "params[0]='{}'".format(params[2])
            try:
                fZAngle = float(params[2])
                print "fZAngle={}".format(fZAngle)
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
                    print "Error on params[2]='{}'".format(params[2])
        if len(params) > 3:
            print "params[0]='{}'".format(params[3])
            if params[3] == "hide":
                bShow = False
            elif params[3] == "off":
                bAttach = False
            else:
                print "Error on params[3]='{}'".fromat(params[3])
    print "Calling Columns2.ColumnUnderPlayer2(bOn={}, bShow{}, player={}, fXAngle={}, fYAngle={}, fZAngle={}, bAttach={})".format(True, bShow, player, fXAngle, fYAngle, fZAngle, bAttach)
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
    
    print "SendGame {}, {}".format(idAvatar, type(idAvatar))
    if len(args) > 1:
        params = args[1].split()
        for param in params:
            print "SendGame #{}, {}".format(param, type(param))
            ret = MarkerGames.SendGame(gameId=param, playerId=idAvatar)
            if ret[0] == 1:
                SendChatMessage(self, myself, [player], "I'm sending you game #{} : {}. Look in your Incoming folder.".format(param, ret[1]), cFlags.flags)
                print "SendGame : game sent -> #{} - {}".format(param, ret[1])
            else:
                SendChatMessage(self, myself, [player], "Game #{0} not found, sorry.".format(param), cFlags.flags)
                print "SendGame error : game not sent"
        print "SendGame end 1"
        return 1
    else:
        print "SendGame => list"
        title = "{0}'s Marker Games".format(myself.getPlayerName())
        ret = MarkerGames.SendGameList(title, playerId=idAvatar)
        if ret == 1:
            SendChatMessage(self, myself, [player], "I'm sending you my game list, look in your Incoming folder.", cFlags.flags)
            print "SendGame : list sent"
        else:
            SendChatMessage(self, myself, [player], "No game list available, sorry.", cFlags.flags)
            print "SendGame error : list not sent"
        print "SendGame end 2"
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
            print "RideAnimal : {} ({})".format(param, type(param))
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
    nbActions = 0
    currentActionIndex = 0

    def __init__(self):
        print "ExecuteDanceSteps : init"
        
    def Step(self):
        print "ExecuteDanceSteps : Step {} ({}, {})".format(self.currentActionIndex, self.nbActions, len(self.lstActions))
        delay = 0
        
        strAct = self.lstActions[self.currentActionIndex]
        if strAct.lower().startswith("dance "):
            print strAct
        elif strAct.lower().startswith("end"):
            print "This is the end!"
        elif strAct.lower().startswith("group"):
            print "New group of dancers."
            self.lstIdDancers = Dance.GetIdDancerList(strAct)
        else:
            print "Command line"
            cmdLine = Dance.ConvertActionToCommand(strAct)
            # Executer la commande pour chaque danseur present dans mon age
            self.lstIdDancers
            agePlayers = PtGetPlayerList()
            agePlayers.append(PtGetLocalPlayer())
            ageDancers = filter(lambda pl: pl.getPlayerID() in self.lstIdDancers, agePlayers)
            # pour tester : je m'ajoute si la liste est vides
            if len(ageDancers) == 0:
                ageDancers.append(PtGetLocalPlayer())
            for player in ageDancers:
                cmdArgs = [player]
                cmdArgs.append(cmdLine[1])
                CallMethod(self=self.xKiSelf, cmdName=cmdLine[0], cFlags=self.xKiFlags, pAmIRobot=xBotAge.AmIRobot, args=cmdArgs)
            # Attendre et lancer la commande suivante
            delay = cmdLine[2]
        
        if self.currentActionIndex < self.nbActions - 1:
            self.currentActionIndex += 1
            PtSetAlarm(delay, self, 0)
        else:
            self.Stop()
        
        #PtSetAlarm(delay, self, 0)
        #pass

    def onAlarm(self, param=1):
        #print "ExecuteDanceSteps : onalarm"
        if not self.isRunning:
            print "ExecuteDanceSteps : Not running"
            return
        #
        #for strAct in self.lstActions:
        #self.Stop()
        
        #
        print "ExecuteDanceSteps : call Step"
        self.Step()
        
        #if param == 1:
        #    machine(3)
        #    PtSetAlarm(19, self, 0)
        #else:
        #    machine(4)
        #    PtSetAlarm(19, self, 1)
        
    def Start(self, xKiSelf, xKiFlags, lstActions):
        self.xKiSelf = xKiSelf
        self.xKiFlags = xKiFlags
        self.lstActions = lstActions
        self.nbActions = len(self.lstActions)
        self.currentActionIndex = 0
        if not self.isRunning:
            self.isRunning = True
            print "ExecuteDanceSteps : Start"
            self.onAlarm()

    def Stop(self):
        print "ExecuteDanceSteps : Stop"
        self.isRunning = False

# Il me faut une instance de la classe ExecuteDanceSteps
# A voir si je prevois de permettre a plusieurs joueurs de lancer chacun sa danse
# Il me faudra creer un dictionnaire de danses (joueur / instance de danse)
#executeDanceSteps = ExecuteDanceSteps()
executeDanceSteps = None

# Methode pour executer une danse complete
def StartDance(self, cFlags, args=[]):
    global executeDanceSteps
    myself = PtGetLocalPlayer()
    player = args[0]
    if not isPlayerInAge(player):
        SendChatMessage(self, myself, [player], "You must be in my age, use link to join me.", cFlags.flags)
        return 1
    if len(args) > 1:
        # Un seul parametre est attendu : le nom du fichier de danse.
        danceFileName = args[1].strip()
        print "ExecuteDance : {} ({})".format(danceFileName, type(danceFileName))
        
        lstActions = Dance.ReadDanceFile(danceFileName)
        # Au cas ou une danse soit deja lancee, il faut l'arreter avant de demarrer la nouvelle
        if executeDanceSteps is not None:
            executeDanceSteps.Stop()
        
        if len(lstActions) > 0:
            if executeDanceSteps is None:
                executeDanceSteps = ExecuteDanceSteps()
            # C'est parti...
            executeDanceSteps.Start(self, cFlags, lstActions)
        else:
            SendChatMessage(self, myself, [player], "The dance file '{}' is empty or does not exist.".format(danceFileName), cFlags.flags)
        return 1
    else:
        return 0

# Methode pour arreter l'execution d'une danse
def StopDance(self, cFlags, args=[]):
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

"""
#Exemple:
#Appelle la fonction maFonction de monModule.py
def MaMethode(self, cFlags, args = []):
    #histoire de savoir que quelqu'un a appele cette methode
    self.chatMgr.AddChatLine(None, "> MaMethode", 3)
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
    #self.chatMgr.AddChatLine(None, "> Help", 3)
    if len(args) < 1:
        self.chatMgr.AddChatLine(None, "** Help: no arg! **", 3)
        print("** Help: no arg! **")
        return 0
    myself = PtGetLocalPlayer()
    player = args[0]
    idAvatar = player.getPlayerID()
    
    self.chatMgr.AddChatLine(None, "** Help: sending to \"{}\". **".format(player.getPlayerName()), 3)
    print("** Help: sending to \"{}\". **".format(player.getPlayerName()))

    # aide sur une commande (en chat prive)
    if len(args) > 1:
        cmdName = args[1]
        HelpCmd(self, player, cFlags, cmdName)
        return 1
    # si pas de commade specifiee, envoyer le KiMail
    
#    #pour en mettre une copie dans mon journal Nexus
#    journals = ptVault().getAgeJournalsFolder()
#    agefolderRefs = journals.getChildNodeRefList()
#    for agefolderRef in agefolderRefs:
#        agefolder = agefolderRef.getChild()
#        if agefolder.getType() == PtVaultNodeTypes.kFolderNode:
#            agefolder = agefolder.upcastToFolderNode()
#            if agefolder.folderGetName() == 'Nexus':
#                journal = agefolder
#                break

    title1 = myself.getPlayerName() + "'s help"
    msg = "Shorah!\n"
    msg += "I'm an automated avatar created by Mirphak.\n"
    msg += "I'm not a magic bot, the commands you can PM to me are different.\n"
    msg += "Here the list of available commands (last update 2017-08-13):\n"
    msg += "------------------------------------------------------------\n\n"
    msg += "help : sends you this text note.\n"
    msg += "help [command name]: PM you a specific help on a command.\n\n"
    msg += "** LINKING THROUGH AGES:\n"
    msg += "link or meet : links your avatar to Mir-o-Bot's current Age.\n\n"
    msg += "to {city/library/ferry/dakotah/tokotah/concert/palace} : links YOU to different points of the public city\n"
    msg += "or some public ages {gog/gome/kirel/kveer/phil}\n"
    #msg += "or a Mir-o-Bot age {Ae'gura/Ahnonay Cathedral/Cleft/Relto/Eder Gira/Eder Kemo/Er'cana/Gahreesen/Hood/Kadish/Pellet Cave/Teledahn}.\n"
    msg += "or a Mir-o-Bot age {aegura/ahnonay/cathedral/cleft/dereno/descent/ercana/gahreesen/gz/gira/hood/jalak/kadish/kemo/minkata/myst/negilahn/office/payiferen/pelletcave/relto/silo/spyroom/teledahn/tetsonot}.\n"
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
    #msg += "   Mir-o-Bot's ages are available too :Ae'gura, Ahnonay, Ahnonay Cathedral, Cleft, Eder Gira, Eder Kemo, Eder Tsogal, Eder Delin, Er'cana, Gahreesen, Hood, Jalak, Kadish, Minkata, Pellet Cave, Relto, Teledahn\n"
    msg += "   Available Mir-o-Bots ages:\n"
    msg += "   aegura, ahnonay, cathedral, cleft, dereno, descent, ercana, gahreesen, gira, gz, hood, jalak, kadish, kemo, minkata, mobkveer, myst, negilahn, office, payiferen, pelletcave, relto, silo, spyroom, teledahn, tetsonot\n\n"
    msg += "   Some more arrival points in Mir-o-Bots ages that works with the to and linkbotto commands:\n"
    msg += "   Cleft : cleft1, cleft2.\n"
    msg += "   Er'cana : oven.\n"
    msg += "   Gahrissen : gear, pinnacle, training, team, prison, veranda, gctrl, gnexus.\n"
    msg += "   \n"
    msg1 = msg

    title2 = myself.getPlayerName() + "'s moving help"
    msg = "** MOVING IN Mir-o-Bot AGES:\n"
    msg += "onbot or warp or w : warps your avatar to Mir-o-Bot's current position.\n\n"
    msg += "onlake: Adds an invisible floor and warps you on it.\n"
    msg += "  /!\ Once added by a player all others visiting will have the invisible floor.\n\n"
    msg += "      It will follow you in other ages til you quit the game.\n\n"
    msg += "nolake: Removes the invisible floor, maybe ...\n"
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
    msg += "    Gahreesen specific spots (sp or g 0 to 34)\n"
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
    msg += "door [open/close] : opens or closes the bahro door (only in Delin or Tsogal).\n\n"
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
        helpNote1.setTextW(msg1)
        helpNote1.setTitleW(title1)
        #journal.addNode(helpNote1)
    except:
        msg = "An error occured when creating help note 1."
        SendChatMessage(self, myself, [player], msg, cFlags.flags)

    try:
        helpNote2 = ptVaultTextNoteNode(0)
        helpNote2.setTextW(msg2)
        helpNote2.setTitleW(title2)
        #journal.addNode(helpNote2)
    except:
        msg = "An error occured when creating help note 2."
        SendChatMessage(self, myself, [player], msg, cFlags.flags)

    try:
        helpNote3 = ptVaultTextNoteNode(0)
        helpNote3.setTextW(msg3)
        helpNote3.setTitleW(title3)
        #journal.addNode(helpNote3)
    except:
        msg = "An error occured when creating help note 3."
        SendChatMessage(self, myself, [player], msg, cFlags.flags)

    try:
        helpNote4 = ptVaultTextNoteNode(0)
        helpNote4.setTextW(msg4)
        helpNote4.setTitleW(title4)
        #journal.addNode(helpNote4)
    except:
        msg = "An error occured when creating help note 4."
        SendChatMessage(self, myself, [player], msg, cFlags.flags)

    msg = "I'm sending you help Ki-mails..."
    SendChatMessage(self, myself, [player], msg, cFlags.flags)
    if helpNote1 is not None:
        try:
            helpNote1.sendTo(idAvatar)
        except:
            msg = "An error occured while sending help note 1."
            SendChatMessage(self, myself, [player], msg, cFlags.flags)
    if helpNote2 is not None:
        try:
            helpNote2.sendTo(idAvatar)
        except:
            msg = "An error occured while sending help note 2."
            SendChatMessage(self, myself, [player], msg, cFlags.flags)
    if helpNote3 is not None:
        try:
            helpNote3.sendTo(idAvatar)
        except:
            msg = "An error occured while sending help note 3."
            SendChatMessage(self, myself, [player], msg, cFlags.flags)
    if helpNote4 is not None:
        try:
            helpNote4.sendTo(idAvatar)
        except:
            msg = "An error occured while sending help note 4."
            SendChatMessage(self, myself, [player], msg, cFlags.flags)
    
    msg = "You can also use \"help [command name]\".\n ** Available commands : " + ", ".join(cmdDict.keys())
    SendChatMessage(self, myself, [player], msg, cFlags.flags)
    return 1

# Envoie un message d'aide specifique a une commande
def HelpCmd(self, player, cFlags, cmdName):
    #self.chatMgr.AddChatLine(None, "> HelpCmd", 3)
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

def TestMsg(self, cFlags, args = []):
    self.chatMgr.AddChatLine(None, "> TestMsg", 3)
    if len(args) < 2:
        return 0
    myself = PtGetLocalPlayer()
    player = args[0]
    nFlag = int(args[1])
    SendChatMessage(self, myself, [player], "type msg: %i" % (nFlag) , nFlag)
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
    'anim':(Animer, ["[animation name] [n]:", 
        " where [animation name] is in:", 
        "    {ladderup/ladderdown/climbup/climbdown/stairs", 
        "    /walk/run/back/moonwalk/swim", 
        "    /dance/crazy/what/zomby/hammer/wait/laugh/thank/talk}.", 
        " and [n] is the number of times you want to do."]),
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
    'light':['light', 'aura'],
    'fogshape':['fogshape', 'fogdensity'],
    'column':['col', 'colonne'],
    'onlake':['lakeon', 'lake'],
    'nolake':['lakeoff', 'onlakeoff', 'offlake'],
    'rsph':['rsph', 'rotsphere', 'rotspheres', 'rotatesphere', 'rotatespheres', 'turnsphere', 'turnspheres'],
}

# Noms alternatifs des animations
altAnim = {
    'danse'     :['danse'     , 'dance'],
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
    'rire2'      :['rire2'      , 'laugh2'],
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
    "askquestion"         : ["askquestion"], 
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
}

travelAnimList = ("echelle", "descendre", "ladderup", "ladderdown", "escalier", "nage", "marche", "cours", "recule", "pasdroite", "pasgauche", "brasse")

def RetreaveCmdName(altCmdName):
    for k, v in alternatives.items():
        if altCmdName.lower() in v:
            return str(k)
    return altCmdName

def RetreaveAnimCmdName(altCmdName):
    for k, v in altAnim.items():
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
            "g30", "g31", "g32", "g33", "g34"
            ],
    }
    ageInfo = PtGetAgeInfo()
    ageFileName = ageInfo.getAgeFilename().lower()
    if ageFileName in altSP.keys():
        if altCmdName.lower() in altSP[ageFileName]:
            return altCmdName.lower()
    return None

def RetreaveCmd(altCmd, args):
    if altCmd == "no":
        if len(args) > 1:
            if args[1] in ["ki", "light", "aura", "night", "sky", "fog", "bug", "bugs", "lake"]:
                print "(a): {} off".format(args[1])
                cmd = "{} off".format(args[1])
                args.pop(1)
                return cmd
    if altCmd in ["open", "close"]:
        if len(args) > 1:
            if args[1] == "door":
                print "(b): door {}".format(altCmd)
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
        "night on":["nighton",],
        "night off":["nightoff", "nonight"],
        "sky on":["skyon",],
        "sky off":["skyoff", "nosky"],
        "fog on":["fogon",],
        "fog off":["fogoff", "nofog"],
        "bugs on":["bugson",],
        "bugs off":["bugsoff", "nobug"],
        }
    for k, v in altCmds.items():
        if altCmd.lower() in v:
            print "(c): {}".format(k)
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
    self.chatMgr.AddChatLine(None, "> MaMethode", 3)
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
    print "xBotAge.AmIRobot = {}".format(xBotAge.AmIRobot)
    #traiter les noms de commande alternatifs
    try:
        cmdName = RetreaveCmdName(cmdName)
        #self.chatMgr.DisplayStatusMessage("=> " + cmdName)
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
        print "avant: {} {}".format(cmdName, args[1])
    #cmdAndArgs = RetreaveCmd(cmdName, args)
    #cmd = cmdAndArgs[0]
    #args = cmdAndArgs[1]
    cmd = RetreaveCmd(cmdName, args)
    if cmd is not None:
        cmdNameAndArg = cmd.split(" ", 1)
        cmdName = cmdNameAndArg[0]
        args.append(cmdNameAndArg[1])
    
    if len(args) > 1:
        print "apres: {} {}".format(cmdName, args[1])
    #traitement "normal"
    if cmdName in cmdDict:
        #self.chatMgr.AddChatLine(None, "** CallMethod: \"{}\" found. **".format(cmdName), 3)
        print("** CallMethod: \"{}\" found. **".format(cmdName))
        ret = None
        # During events I may have to disable all the commands but warp to bot
        if bBlockCmds:
            #
            #authorizedCmds = ('onbot', 'link')
            # During Cavern Tours
            #authorizedCmds = ('link', 'to', 'onbot', 'wd', 'warp', 'nolake', 'coord', 'save', 'ws', 'agoto', 'rgoto', 'dnigoto', 'land', 'turn', 'rot', 'float', 'jump', 'find', 'list', 'anim', 'sp', 'ki', 'light', 'nopanic', 'sdl', 'sendme', 'help')
            authorizedCmds = ()
            myself = PtGetLocalPlayer()
            if myself.getPlayerID() != 2332508L:
                authorizedCmds = ('link', 'to', 'onbot', 'wd', 'warp', 'onlake', 'nolake', 'coord', 'save', 'ws', 'agoto', 'rgoto', 'dnigoto', 'land', 'turn', 'rot', 'float', 'jump', 'find', 'list', 'anim', 'sp', 'ki', 'light', 'nopanic', 'sdl', 'sendme', 'help')
            if cmdName not in authorizedCmds:
                #myself = PtGetLocalPlayer()
                player = args[0]
                if player.getPlayerID() not in adminList :
                    #msg = "An event is running, only the W / LINK commands are enabled."
                    #msg = "Cavern Tour is running, only basic commands are enabled."
                    msg = "An event is running, only basic commands are enabled."
                    SendChatMessage(self, myself, [player], msg, cFlags.flags)  
                    return 0
        if len(args) == 0:
            #return cmdDict[cmdName][0]()
            ret = cmdDict[cmdName][0]()
        else:
            #self.chatMgr.DisplayStatusMessage("=> " + cmdName)
            #return cmdDict[cmdName][0](self, cFlags, args)
            ret = cmdDict[cmdName][0](self, cFlags, args)
            #if ret == 1 and not cmdName in ("help", "to", "link"):
            if ret == 1:
                isBuddyAdded = xPlayers.AddBud(args[0].getPlayerID())
                if isBuddyAdded:
                    self.chatMgr.AddChatLine(None, "----> '{0}' [{1}] a ete ajoute a mes buddies.".format(args[0].getPlayerName(), args[0].getPlayerID()), 3)
                #self.chatMgr.AddChatLine(None, "----> '{0}' [{1}] m'a utilise.".format(args[0].getPlayerName(), args[0].getPlayerID()), 3)
        #self.chatMgr.AddChatLine(None, "** CallMethod: \"{}\" returned: {}. **".format(cmdName, ret), 3)
        print("** CallMethod: \"{}\" returned: {}. **".format(cmdName, ret))
        return ret
    else:
        return 0

