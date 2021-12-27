# -*- coding: utf-8 -*-
from Plasma import *
import math
from . import xBotAge
from . import BahroCaveFloor
import traceback
    
# Default method that does nothing.
def DoNothing(player=None, params=[]):
    print("DoNothing : This is just a default method.")

#
def WarpToMe(player=None, params=[]):
    print("WarpToMe(player={}, params={}".format(player, params))
    try:
        av = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
        so = PtGetLocalAvatar()
        pos = so.getLocalToWorld()
        av.netForce(1)
        av.physics.warp(pos)
    except Exception as ex:
        traceback.print_exc()

#
def ProtractorOff(player=None, params=[]):
    bOff = False
    xBotAge.ToggleSceneObjects("ProtractorPart", age="GreatZero", bDrawOn=bOff, bPhysicsOn=bOff)
    xBotAge.ToggleSceneObjects("ProtractorCrystal01", age="GreatZero", bDrawOn=bOff, bPhysicsOn=bOff)
    xBotAge.ToggleSceneObjects("ProtractorBase04", age="GreatZero", bDrawOn=bOff, bPhysicsOn=bOff)
    xBotAge.ToggleSceneObjects("ProtractorBase03", age="GreatZero", bDrawOn=bOff, bPhysicsOn=bOff)
    xBotAge.ToggleSceneObjects("ProtractorRails", age="GreatZero", bDrawOn=bOff, bPhysicsOn=bOff)
    xBotAge.ToggleSceneObjects("LaserHalo", age="GreatZero", bDrawOn=bOff, bPhysicsOn=bOff)

#
def NoLadder(player=None, params=[]):
    ageName = PtGetAgeInfo().getAgeFilename()
    xBotAge.ToggleSceneObjects("Ladder", age=ageName, bDrawOn=True, bPhysicsOn=False)
    xBotAge.ToggleSceneObjects("ladder", age=ageName, bDrawOn=True, bPhysicsOn=False)
    #xBotAge.ToggleSceneObjects("Ladder", age=None, bDrawOn=True, bPhysicsOn=False)
    #xBotAge.ToggleSceneObjects("ladder", age=None, bDrawOn=True, bPhysicsOn=False)
    xBotAge.ToggleSceneObjects("cliimbTrigger", age=ageName, bDrawOn=True, bPhysicsOn=False)

#
def PageInAllCaves():
    pages = ["YeeshaCave", "BlueSpiralCave", "PODcave", "MINKcave", "POTScave", "Cave"]
    for page in pages:
        PtConsoleNet("Nav.PageInNode {0}".format(page), 1)

# 
def PageInJalak():
    pages = ["jlakArena"]
    for page in pages:
        PtConsoleNet("Nav.PageInNode {0}".format(page), 1)


#
def Cave(player=None, params=[]):
    PageInAllCaves()
    PageInJalak()
    PtConsoleNet("Avatar.Spawn.DontPanic", 1)
    BahroCaveFloor.Floor(en=True)
    WarpToMe(player, params)

#************************************************************************#
# When a new player is arriving in my age,
# I'm doing some automatic stuffs.
# , method=DoNothing, params=[]
#************************************************************************#
#=====================#
# CheckPlayersArrival #
#=====================#
class CheckPlayersArrival:
    _running = False
    _nbTry   = 0
    _xKiSelf = None
    _player  = None
    _playerList = []
    _method = None
    _params = []

    #
    def __init__(self):
        print("CheckPlayersArrival : init")
    
    # Pour savoir si le joueur est dans l'age du robot
    def IsPlayerInAge(self):
        isHere = False
        playerId = self._player.getPlayerID()
        print("IsPlayerInAge for player #{}".format(playerId))
        if playerId is None or playerId == 0:
            return False
        avatarKey = PtGetAvatarKeyFromClientID(playerId)
        if avatarKey is None:
            return False
        soAvatar = avatarKey.getSceneObject()
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
    
    ## Default method that does nothing.
    #def DoNothing(self, params=[]):
    #    print "DoNothing : This is just a default method."
    #
    ##
    #def WarpToMe(self, params=[]):
    #    if self.IsPlayerInAge():
    #        av = PtGetAvatarKeyFromClientID(self._player.getPlayerID()).getSceneObject()
    #        so = PtGetLocalAvatar()
    #        pos = so.getLocalToWorld()
    #        av.netForce(1)
    #        av.physics.warp(pos)

    #
    def onAlarm(self, param=1):
        #print "CheckPlayersArrival:onalarm"
        if not self._running:
            print("CheckPlayersArrival : not running")
            return
        if param == 1:
            print("CheckPlayersArrival : onAlarm 1 => call IsPlayerInAge")
            playerIsHere = self.IsPlayerInAge()
            if playerIsHere:
                # Le joueur est arrive
                PtSetAlarm(0, self, 2)
            else:
                # Le joueur n'est pas encore arrive
                self._nbTry += 1
                if self._nbTry > 240:
                    # Il se fait trop attendre
                    self._running = False
                else:
                    # Attendons-le encore
                    PtSetAlarm(0.5, self, 1)
        if param == 2:
            # Deplacer le joueur sur moi
            #pass
            self._method(self._player, self._params)
        
    def Start(self, xKiSelf, player, method=DoNothing, params=[]):
        if xKiSelf is None:
            print("CheckPlayersArrival : Error : self._xKiSelf is none")
            return
        if not isinstance(player, ptPlayer):
            print("CheckPlayersArrival : not player")
            return
        self._xKiSelf = xKiSelf
        self._player = player
        self._method = method
        self._params = params
        if not self._running:
            self._running = True
            self._nbTry = 0
            print("CheckPlayersArrival : starts for player # {}".format(self._player.getPlayerID()))
            self.onAlarm()

    def Stop(self):
        print("CheckPlayersArrival:stop")
        self._running = False

#************************************************************************#

# Global variables
isActive = False
checkArrivals = None
#strArgs = ""
function = DoNothing
parameters = []

#DoNothing(self, params=[])
#WarpToMe(self, params=[])
#ProtractorOff(self, params=[])
#NoLadder(self, params=[])

# Convert strArgs in [method, [params]]
def stringToMethodParams(strArgs=""):
    global function
    global parameters
    function = DoNothing
    parameters = []
    print("strArgs = '{}'".format(strArgs))
    if isinstance(strArgs, str):
        worlds = strArgs.strip().split(" ", 1)
        print("worlds = '{}'".format(worlds))
        if len(worlds) > 1:
            parameters = worlds[1].split(" ")
            print("parameters = '{}'".format(parameters))
        if len(worlds) > 0:
            fct = worlds[0]
            print("fct = '{}'".format(fct))
            if fct == "warptome":
                function = WarpToMe
            elif fct == "protractoroff":
                function = ProtractorOff
            elif fct == "noladder":
                function = NoLadder
            elif fct == "cave":
                function = Cave
            else:
                print("unknown fct {}".format(fct))
    else:
        print("not a str!")
#
def StopChecking():
    global checkArrivals
    if isinstance(checkArrivals, CheckPlayersArrival):
        checkArrivals.Stop()
        checkArrivals = None

#
#def StartChecking(xKiSelf, player, method=DoNothing, params=[]):
def StartChecking(xKiSelf, player):
    global checkArrivals
    #stopchecking()
    checkArrivals = CheckPlayersArrival()
    checkArrivals.Start(xKiSelf, player, method=function, params=parameters)

#
