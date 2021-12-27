# -*- coding: utf-8 -*-
from Plasma import *
import math
from . import xBotAge
import traceback

"""
Script proche de CheckPlayersArrival.py a lancer seul
Ne depend pas du joueur qui a envoye meet ou link au bot
Mais controle les joueurs presents dans l'age
"""

# Default method that does nothing.
def DoNothing(player=None, params=[]):
    print("DoNothing : This is just a default method.")

#
def WarpToMe(player=None, params=[]):
    print("WarpToMe(player={}, params={}".format(player, params))
    if not isinstance(player, ptPlayer):
        return
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


#************************************************************************#
# When a new player is arriving in my age,
# I'm doing some automatic stuffs.
# , method=DoNothing, player, params=[]
#************************************************************************#
#=====================#
# CheckPlayersArrival #
#=====================#
class CheckPlayersArrival:
    _running = False
    _nbTry = 0
    _oldIds = 0
    _player = None
    _playerList = []
    _method = None
    _params = []

    #
    def __init__(self):
        print("CheckPlayersArrival : init")
    
    # Pour savoir si le joueur est dans l'age du robot
    def IsPlayerInAge(self):
        isHere = False
        
        # Pour tous les joueurs sauf moi
        agePlayers = PtGetPlayerList()
        if len(agePlayers) > self._nbPlayersInAge:
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
                if self._nbTry > 60:
                    # Il se fait trop attendre
                    self._running = False
                else:
                    # Attendons-le encore
                    if self._nbTry == 1:
                        PtSetAlarm(10, self, 1)
                    else:
                        PtSetAlarm(1, self, 1)
        if param == 2:
            # Execute the desired method
            self._method(self._player, self._params)
        
    def Start(self, player, method=DoNothing, params=[]):
        if not isinstance(player, ptPlayer):
            print("CheckPlayersArrival : not player")
            return
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
function = DoNothing
parameters = []

#DoNothing(player, params=[])
#WarpToMe(player, params=[])
#ProtractorOff(player, params=[])

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
def StartChecking(player):
    global checkArrivals
    #stopchecking()
    checkArrivals = CheckPlayersArrival()
    checkArrivals.Start(player, method=function, params=parameters)

#
