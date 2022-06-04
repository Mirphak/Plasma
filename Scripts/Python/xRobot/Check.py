# -*- coding: utf-8 -*-
from Plasma import *
from PlasmaKITypes import *
import math

# Variable pour savoir si le mode robot est actif
amIRobot = 0

#==========================#
# Survey Bot Age
#==========================#
class SurveyBotAge:
    _running = False
    _xKiSelf = None
    _nbTry   = 0

    def __init__(self):
        print("SurveyBotAge:")
        
    def WhereAmI(self):
        #print "SurveyBotAge:"
        myCurrentAgeInstanceGuid = PtGetAgeInfo().getAgeInstanceGuid()
        # Am I in one of Mir-o-Bot's age?
        for val in list(ages.MirobotAgeDict.values()):
            if val[2] == myCurrentAgeInstanceGuid:
                # I am in a Mir-o-Bot age, it's ok.
                #print "SurveyBotAge:ok mob"
                self._nbTry = 0
                return
        # Am I in one of MagicBot age?
        for val in list(ages.MagicbotAgeDict.values()):
            if val[2] == myCurrentAgeInstanceGuid:
                # I am in a Mir-o-Bot age, it's ok.
                #print "SurveyBotAge:ok magic"
                self._nbTry = 0
                return
        # Am I in one of my own private age?
        myAges = ptVault().getAgesIOwnFolder().getChildNodeRefList()
        for age in myAges:
            ageInfo = age.getChild().upcastToAgeLinkNode().getAgeInfo()
            if ageInfo.getAgeInstanceGuid() == myCurrentAgeInstanceGuid:
                # OK
                #print "SurveyBotAge:ok own"
                self._nbTry = 0
                return
        print("This age is not allowed for the bot: {0}, {1}".format(PtGetAgeInfo().getAgeFilename(), myCurrentAgeInstanceGuid))
        # I am not welcome here, link myself in an allowed age
        if self._xKiSelf is None:
            print("SurveyBotAge:Error: self._xKiSelf is none, quit MOULa")
            PtConsole("App.Quit")
        else:
            self._nbTry += 1
            print("SurveyBotAge:try link (#{})".format(self._nbTry))
            if self._nbTry > 8:
                PtConsole("App.Quit")
            try:
                LinkToPublicAge(self._xKiSelf, "hood")
            except:
                print("SurveyBotAge:error linking")
                PtConsole("App.Quit")
        
    def onAlarm(self, param=1):
        #print "SurveyBotAge:onalarm"
        if not self._running:
            print("SurveyBotAge:not running")
            return
        #print "SurveyBotAge:call WhereAmI"
        self.WhereAmI()
        PtSetAlarm(15, self, 1)
        
    def Start(self, xKiSelf):
        self._xKiSelf = xKiSelf
        if not self._running:
            self._running = True
            print("SurveyBotAge:start")
            self.onAlarm()

    def Stop(self):
        print("SurveyBotAge:stop")
        self._running = False

#surveyBot = SurveyBotAge()
#************************************************************************#
"""
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)
except ValueError:
    print "Could not convert data to an integer."
except:
    print "Unexpected error:", sys.exc_info()[0]
    raise
"""

"""

#Pour savoir si le joueur est dans l'age du robot
def isPlayerInAge(player):
    #PtSendKIMessage(kKILocalChatStatusMsg, "> isPlayerInAge")
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
    players = filter(lambda player: pattern.match(player.getPlayerName().lower()), agePlayers)
    if len(players) == 0:
        players = filter(lambda player: player.getPlayerName().lower().replace(" ", "") == name.replace(" ", ""), agePlayers)
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
    #global xBotAge.AmIRobot = AmIRobot
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
            # JE LE DESACTIVE POUR L'INSTANT (pendant les tests de CreateReltoNight1)
            ## do special stuff in some ages
            #if len(xBotAge.currentBotAge) > 3:
            #    # in Mir-o-Bot's Relto
            #    if xBotAge.currentBotAge[1] == "Personal" and xBotAge.currentBotAge[3] == "Mir-o-Bot's":
            #        #xRelto.SetFog(style = "nofog")
            #        xRelto.EnableAll(False)
            #
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

"""

#************************************************************************#
# When a new player is arriving in my age,
# I'm doing some automatic stuffs.
#************************************************************************#
#==========================#
# Survey Player
#==========================#
class SurveyPlayer:
    _running = False
    _nbTry   = 0
    _xKiSelf = None
    _player  = None
    _playerList = []

    #
    def __init__(self):
        print("SurveyPlayer : init")
    
    # Pour savoir si le joueur est dans l'age du robot
    def IsPlayerInAge(self):
        isHere = False
        playerId = self._player.getPlayerID()
        soAvatar = PtGetAvatarKeyFromClientID(playerId).getSceneObject()
        if soAvatar is None:
            # si je joueur n'a pas de sceneobject associe, il n'est pas ici.
            return False
        
        if playerId == PtGetLocalPlayer().getPlayerID():
            # Je suis forcement dans mon age (sauf si je suis en cours de liaison).
            isHere = True
        else:   
            # Pour les autres joueurs
            agePlayers = PtGetPlayerList()
            ids = [agePlayer.getPlayerID() for agePlayer in agePlayers]
            try:
                if playerId in ids:
                    isHere = True
                else:
                    isHere = False
            except:
                isHere = False
        
        if isHere:
            # Verifier aussi que le joueur a des coordonnees
            pos = soAvatar.position()
            if pos.getX() == 0 and pos.getY() == 0 and pos.getZ() == 0:
                isHere = False
        
        return isHere
    
    #
    def WarpToMe(self):
        if self.IsPlayerInAge():
            av = PtGetAvatarKeyFromClientID(self._player.getPlayerID()).getSceneObject()
            so = PtGetLocalAvatar()
            pos = so.getLocalToWorld()
            av.netForce(1)
            av.physics.warp(pos)

    #
    def onAlarm(self, param=1):
        #print "SurveyPlayer:onalarm"
        if not self._running:
            print("SurveyPlayer : not running")
            return
        if param == 1:
            print("SurveyPlayer : onAlarm 1 => call IsPlayerInAge")
            playerIsHere = self.IsPlayerInAge()
            if playerIsHere:
                # Le joueur est arrive
                PtSetAlarm(1, self, 2)
            else:
                # Le joueur n'est pas encore arrive
                self._nbTry += 1
                if self._nbTry > 8:
                    # Il se fait trop attendre
                    self._running = False
                else:
                    # Attendons-le encore
                    PtSetAlarm(15, self, 1)
        if param == 2:
            # Deplacer le joueur sur moi
            pass
        
    def Start(self, player, xKiSelf):
        if not isinstance(player, ptPlayer):
            print("SurveyPlayer : not player")
            return
        if xKiSelf is None:
            print("SurveyPlayer : Error : self._xKiSelf is none")
            return
        self._player = player
        self._xKiSelf = xKiSelf
        if not self._running:
            self._running = True
            self._nbTry = 0
            print("SurveyPlayer : start")
            self.onAlarm()

    def Stop(self):
        print("SurveyPlayer:stop")
        self._running = False

#surveyPlayer = SurveyPlayer()
#************************************************************************#

adminList = [
    32319,   # Mir-o-Bot
    31420,   # Mirphak
    2332508, # mob
    11896,  # MagicYoda
    #115763L,  # Willy
    #127131,  # tsuno
    #133403L,  # sendlinger
    #137998,  # Mabe
    #254640,  # Eternal Seeker
    #254930,  # Kamikatze
    #966183L,  # y e e s h a
    #2975513L, # Didi
    #1261291L, # Y E E R K
    #5667000, # Minasunda
    #5710565, # Salirama
    #6725908L, # Raymondo
    #6559861L, # Kawliga
    #6583813L, # Roland (Mav Hungary)
    #6682907,  # 
    #6833983L, # malcg
    #6961947, # Calisia (= Terry L. Britton)
    #7060111, # Aeonihya
    #7132841, # Mina Sunda
    #7172637L, # Baeda
    #7227499L, # Lidia (Mav Hungary)
    #7327507L, # artopia
    #7517653L, # ladylora
    #7881034L, # Yakoso
    #7939982, # Claidi Song
    #7965725L, # Z A N D l
    #8068100L,  # NDG Eternal Seeker
    #8315178L,  # Roland (Mav Hungary)
]

#
def Arena():
    agePlayers = PtGetPlayerList()
    agePlayers = [pl for pl in PtGetPlayerList() if not(pl.getPlayerID() in adminList)]
    for player in agePlayers:
        soav = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
        some = PtGetLocalAvatar()
        #pos = so.getLocalToWorld()
        posav = soav.position()
        if posav.getX() > -20 and posav.getX() < 18:
            if posav.getY() > -18 and posav.getY() < 18:
                if posav.getZ() > -4 and posav.getZ() < 15:
                    some = PtGetLocalAvatar()
                    posme = some.getLocalToWorld()
                    soav.netForce(1)
                    soav.physics.warp(posme)

#
def MovePlayersOutsideMyst25ReltoDanceArea():
    agePlayers = PtGetPlayerList()
    agePlayers = [pl for pl in PtGetPlayerList() if not(pl.getPlayerID() in adminList)]
    x0 = 34.5
    y0 = 100.4
    r0 = 30.0
    for player in agePlayers:
        soav = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
        some = PtGetLocalAvatar()
        posav = soav.position()
        x = posav.getX() - x0
        y = posav.getY() - y0
        r = math.sqrt(x**2 + y**2)
        if r < r0:
            if posav.getZ() > -25 and posav.getZ() < 50:
                some = PtGetLocalAvatar()
                posme = some.getLocalToWorld()
                soav.netForce(1)
                soav.physics.warp(posme)

#==================================#
# Survey Player in Relto Dance Area
#==================================#
class SurveyPlayerInReltoDanceArea:
    _running = False
    _pos = ptMatrix44()
    #_x0 = 34.5
    #_y0 = 100.4
    #_r0 = 30.0
    #_x0 = 74.5
    #_y0 = 140.4
    #_r0 = 78.0
    _x0 = 50.0
    _y0 = 132.0
    _r0 = 55.0

    #
    def __init__(self):
        print("SurveyPlayerInReltoDanceArea : init")
        try:
            so = PtFindSceneobject("LinkInPointBahroPoles", "Personal")
            self._pos = so.getLocalToWorld()
        except:
            print("Error 1")
            try:
                some = PtGetLocalAvatar()
                self._pos = some.getLocalToWorld()
            except:
                print("Error 2")
    #
    def MovePlayersOutsideMyst25ReltoDanceArea(self):
        agePlayers = PtGetPlayerList()
        agePlayers = [pl for pl in PtGetPlayerList() if not(pl.getPlayerID() in adminList)]
        agePlayers.append(PtGetLocalPlayer())
        for player in agePlayers:
            soav = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
            #some = PtGetLocalAvatar()
            posav = soav.position()
            x = posav.getX() - self._x0
            y = posav.getY() - self._y0
            r = math.sqrt(x**2 + y**2)
            #try:
            #    print "Player : {0} => X={1}, Y={2}, Z={3}, x={4}, y={5}, r={6}".format(player.getPlayerID(), posav.getX(), posav.getY(), posav.getZ(), x, y, r)
            #except:
            #    print "Error 3"
            if r < self._r0:
                if posav.getZ() > -25 and posav.getZ() < 50:
                    try:
                        print("SurveyPlayerInReltoDanceArea : Moving player => {0} => X={1}, Y={2}, Z={3}, x={4}, y={5}, r={6}".format(player.getPlayerName(), posav.getX(), posav.getY(), posav.getZ(), x, y, r))
                    except:
                        print("Error 4")
                    #some = PtGetLocalAvatar()
                    #posme = some.getLocalToWorld()
                    soav.netForce(1)
                    #soav.physics.warp(posme)
                    #Move player to LinkInPointBahroPoles
                    try:
                        soav.physics.warp(self._pos)
                    except:
                        print("Error 5")
    
    #
    def onAlarm(self, param=1):
        #print "SurveyPlayerInReltoDanceArea : onalarm"
        if not self._running:
            print("SurveyPlayerInReltoDanceArea : not running")
            return
        
        #
        if PtGetAgeInfo().getAgeFilename() != "Personal":
            print("SurveyPlayerInReltoDanceArea : I'm not in Relto, stop running")
            self.Stop()
            return
        
        #print "SurveyPlayerInReltoDanceArea : onAlarm => call MovePlayersOutsideMyst25ReltoDanceArea"
        self.MovePlayersOutsideMyst25ReltoDanceArea()
        PtSetAlarm(1, self, 1)
        
    def Start(self):
        if not self._running:
            self._running = True
            print("SurveyPlayerInReltoDanceArea : start")
            self.onAlarm()

    def Stop(self):
        print("SurveyPlayerInReltoDanceArea:stop")
        self._running = False

#
surveille = None

#
def stopchecking():
    global surveille
    if isinstance(surveille, SurveyPlayerInReltoDanceArea):
        surveille.Stop()
        surveille = None

#
def startchecking():
    global surveille
    stopchecking()
    surveille = SurveyPlayerInReltoDanceArea()
    surveille.Start()

#
