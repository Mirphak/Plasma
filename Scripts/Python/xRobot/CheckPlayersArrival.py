# -*- coding: utf-8 -*-
from Plasma import *
from PlasmaKITypes import *
import math
from . import xBotAge
from . import BahroCaveFloor
from . import xJMD
import traceback
    
# Default method that does nothing.
def DoNothing(player=None, params=[]):
    print("DoNothing : This is just a default method.")

#
def WarpToMe(player=None, params=[]):
    print("WarpToMe(player={}, params={}".format(player, params))
    ageName = PtGetAgeInfo().getAgeFilename()
    xBotAge.ToggleSceneObjects("Panic", age=ageName, bDrawOn=False, bPhysicsOn=False)
    xBotAge.ToggleSceneObjects("Cam", age=ageName, bDrawOn=False, bPhysicsOn=False)
    try:
        av = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
        so = PtGetLocalAvatar()
        pos = so.getLocalToWorld()
        av.netForce(1)
        av.physics.warp(pos)
    except Exception as ex:
        traceback.print_exc()

#
def Green(player=None, params=[]):
    bOff = False
    xBotAge.ToggleSceneObjects("Sphere", age="Elonin", bDrawOn=bOff, bPhysicsOn=bOff)
    xBotAge.SetRenderer(style="100000", start=-100, end=5000, density=3, r=0.0, g=1.0, b=0.0, cr=0.0, cg=0.36, cb=0.0)
    me = PtGetLocalAvatar()
    me.draw.netForce(True)
    me.draw.enable(False)
    PtToggleAvatarClickability(False)

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
    WarpToMe(player, params)

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

#
def Tiwah(player=None, params=[]):
    #print(f"CheckPlayersArrival.Tiwah({player.getPlayerName()},{params})")
    print("CheckPlayersArrival.Tiwah")
    ageName = PtGetAgeInfo().getAgeFilename()
    #PtSendKIMessage(kKILocalChatStatusMsg, f"CheckPlayersArrival.Tiwah({player.getPlayerName()},{params})")
    print("CheckPlayersArrival.Tiwah : PageInJalak")
    PageInJalak()
    #tSendKIMessage(kKILocalChatStatusMsg, "    > PageInJalak")
    #PtConsoleNet("Avatar.Spawn.DontPanic", 1)
    print("CheckPlayersArrival.Tiwah : Cam")
    xBotAge.ToggleSceneObjects("Cam", age=ageName, bDrawOn=False, bPhysicsOn=False)
    #PtSendKIMessage(kKILocalChatStatusMsg, "    > Cam")
    print("CheckPlayersArrival.Tiwah : Panic")
    xBotAge.ToggleSceneObjects("Panic", age=ageName, bDrawOn=False, bPhysicsOn=False)
    #PtSendKIMessage(kKILocalChatStatusMsg, "    > Panic")
    print("CheckPlayersArrival.Tiwah : platform")
    xJMD.platform(where=6, bAttachOn=False)
    #PtSendKIMessage(kKILocalChatStatusMsg, "    > platform")
    print("CheckPlayersArrival.Tiwah : WarpToMe")
    WarpToMe(player, params)
    #PtSendKIMessage(kKILocalChatStatusMsg, "    > warp")
    print("CheckPlayersArrival.Tiwah : END")

# Minkata + Dereno
def MinDer(player=None, params=[]):
    print("WarpToMe(player={}, params={}".format(player, params))
    try:
        av = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
        so = PtGetLocalAvatar()
        pos = so.getLocalToWorld()
        av.netForce(True)
        av.physics.warp(pos)
    except Exception as ex:
        traceback.print_exc()
    
    ## Minkata : Try to move the fog regions
    print("WarpToMe : Try to move the fog regions")
    mTrans = ptMatrix44()
    mTrans.translate(ptVector3(10000.0, 10000.0, 10000.0))
    so = PtFindSceneobject("FogRegion - Exterior", "Minkata")
    pos = so.getLocalToWorld()
    so.physics.netForce(True)
    so.physics.warp(pos * mTrans)
    so = PtFindSceneobject("FogRegion - Caves", "Minkata")
    pos = so.getLocalToWorld()
    so.physics.netForce(True)
    so.physics.warp(pos * mTrans)
    so = PtFindSceneobject("FogOuterDummy", "Minkata")
    pos = so.getLocalToWorld()
    so.physics.netForce(True)
    so.physics.warp(pos * mTrans)
    
    ## Minkata : "StarGlobe", "SkyDome", "ClearColorCatcher", "Dust", "Fog", "Ground"
    print("WarpToMe : Hide some objects")
    #xBotAge.ToggleSceneObjects("StarGlobe", "Minkata", bDrawOn=False, bPhysicsOn=False)
    xBotAge.ToggleSceneObjects("SkyDome", "Minkata", bDrawOn=False, bPhysicsOn=False)
    #xBotAge.ToggleSceneObjects("ClearColorCatcher", "Minkata", bDrawOn=False, bPhysicsOn=False)
    xBotAge.ToggleSceneObjects("Dust", "Minkata", bDrawOn=False, bPhysicsOn=False)
    xBotAge.ToggleSceneObjects("Fog", "Minkata", bDrawOn=False, bPhysicsOn=False)
    xBotAge.ToggleSceneObjects("Ground", "Minkata", bDrawOn=False, bPhysicsOn=True)
    xBotAge.ToggleSceneObjects("Ladder", "Minkata", bDrawOn=True, bPhysicsOn=False)
    
    ## Dereno : "Pod", "Sky", "Surface", "Mirror"
    print("WarpToMe : Add Dereno")
    AddDereno()
    #xBotAge.ToggleSceneObjects("Pod", "Dereno", bDrawOn=True, bPhysicsOn=False)
    #xBotAge.ToggleSceneObjects("Sky", "Dereno", bDrawOn=True, bPhysicsOn=False)
    #xBotAge.ToggleSceneObjects("Surface", "Dereno", bDrawOn=True, bPhysicsOn=False)
    #xBotAge.ToggleSceneObjects("Mirror", "Dereno", bDrawOn=True, bPhysicsOn=False)
    
    ## 
    #tupmat=((-0.9672924280166626,0.2536635398864746,0.0,1.1919100284576416),(-0.2536635398864746,-0.9672924280166626;0.0,10.312591552734375),(0.0,0.0,1.0,-0.0328427329659462),(0.0,0.0,0.0,1.0))
    try:
        mTrans = ptMatrix44()
        mTrans.translate(ptVector3(1.0, 10.0, 0.0))
        av = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
        av.netForce(True)
        av.physics.warp(mTrans)
    except Exception as ex:
        traceback.print_exc()

    print("WarpToMe : End")

#************************************************************************#
# "1-Sky", "1-WaterSurface", "LowerSky", "Mirror"
#************************************************************************#
#
class AlarmAddPrp:
    _nbFois = 0
    _bPrpLoaded = False
    
    def __init__(self, objectName="FishAClockwise", ageFileName="Dereno", bFirst=False, method=DoNothing, params=[]):
        print("AlarmAddPrp: init")
        self._objectName = objectName
        self._ageFileName = ageFileName
        self._bPrpLoaded = False
        self._bFirst = bFirst
        self._method = method
        self._params = params
        self._so = PtFindSceneobject(self._objectName, self._ageFileName)
    def onAlarm(self, context):
        if context == 0:
            print("AlarmAddPrp: 0 - AddPrp")
            PtConsoleNet("Nav.PageInNode DrnoExterior", True)
            #PhysObjectList(self._ageFileName, ["PanicLinkRgn"], False)
            PtSetAlarm(.25, self, 1)
        elif context == 1:
            print("AlarmAddPrp: 1 - Waitting loop")
            #PhysObjectList(self._ageFileName, ["PanicLinkRgn"], False)
            try:
                pos = self._so.position()
            except:
                print("err so pos")
                return
            print("pos: {}, {}, {}".format(pos.getX(), pos.getY(), pos.getZ()))
            if (pos.getX() == 0 and pos.getY() == 0 and pos.getZ() == 0 and self._nbFois < 20):
                self._nbFois += 1
                print(">>> Attente nb: {}".format(self._nbFois))
                PtSetAlarm(1.0, self, 1)
            else:
                if (self._nbFois < 20):
                    self._bPrpLoaded = True
                    PtSetAlarm(2.0, self, 2)
                else:
                    print("loading prp was too long...")
                    
                self._nbFois = 0
        elif context == 2:
            print("AlarmAddPrp: 2 - The prp is ready")
            if self._bFirst:
                ## Disable physics for some objects
                #names = ["Panic", "Camera", "Field", "Link"
                #    "Start", "Terrain", "Wall0"]
                #PhysObjectList(self._ageFileName, names, False)
                # Hide some objects
                #names = ["Bamboo", "Bone", "Distan",
                #    "Calendar", "Camera", "FarHills", 
                #    "Field", "Flag", "Fog", "Green", 
                #    "LightBase", "moss", "Object",  
                #    "SkyDome01", "SoftRegionMain", 
                #    "Star", "Sun", "Terrain", "Wall0"]
                #ShowObjectList(self._ageFileName, names, False)
                #names = []
                # Dereno : "Pod", "Sky", "Surface", "Mirror"
                #xBotAge.ToggleSceneObjects("Pod", "Dereno", bDrawOn=False, bPhysicsOn=False)
                xBotAge.ToggleSceneObjects("Sky", "Dereno", bDrawOn=False, bPhysicsOn=False)
                xBotAge.ToggleSceneObjects("Surface", "Dereno", bDrawOn=False, bPhysicsOn=False)
                xBotAge.ToggleSceneObjects("Mirror", "Dereno", bDrawOn=False, bPhysicsOn=False)
            #self._method(self._params)
        else:
            pass

#
def AddDereno():
    PtSendKIMessage(kKILocalChatStatusMsg, "Adding Dereno...")
    try:
        PtSetAlarm(0, AlarmAddPrp(), 0)
        PtSendKIMessage(kKILocalChatStatusMsg, "Dereno added!")
        return 1
    except:
        PtSendKIMessage(kKILocalChatErrorMsg, "Error while adding Dereno.")
        return 0

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
            elif fct == "tiwah" or fct == "descent":
                function = Tiwah
            elif fct == "minder":
                function = MinDer
            elif fct == "green":
                function = Green
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
    #checkArrivals.Start(xKiSelf, player, method=function, params=parameters)
    checkArrivals.Start(player, method=function, params=parameters)
