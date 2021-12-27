# -*- coding: utf-8 -*-
from Plasma import *
import math

adminList = [
    32319,   # Mir-o-Bot
    31420,   # Mirphak
    2332508, # mob
    11896,  # MagicYoda
    115763,  # Willy
    #127131L,  # tsuno
    #133403L,  # sendlinger
    #137998L,  # Mabe
    #254640L,  # Eternal Seeker
    #254930L,  # Kamikatze
    #966183L,  # y e e s h a
    #2975513L, # Didi
    #1261291L, # Y E E R K
    5667000, # Minasunda
    #5710565L, # Salirama
    #6725908L, # Raymondo
    #6559861L, # Kawliga
    #6583813L, # Roland (Mav Hungary)
    #6682907L,  # 
    #6833983L, # malcg
    6961947, # Calisia (= Terry L. Britton)
    7060111, # Aeonihya
    7132841, # Mina Sunda
    #7172637L, # Baeda
    #7227499L, # Lidia (Mav Hungary)
    #7327507L, # artopia
    #7517653L, # ladylora
    #7881034L, # Yakoso
    7939982, # Claidi Song
    #7965725L, # Z A N D l
    8068100,  # NDG Eternal Seeker
    8315178,  # Roland (Mav Hungary)
]


#====================================#
# Survey Player in Gira Dance Area #
#====================================#
class SurveyPlayerInGiraDanceArea:
    _running = False
    _pos = ptMatrix44()
    _x0 = 87.0
    _y0 = -20.0
    _r0 = 22.0
    _x1 = 60.0
    _y1 = -11.0
    _r1 = 12.0

    #
    def __init__(self):
        print("SurveyPlayerInGiraDanceArea : init")
        try:
            so = PtFindSceneobject("LinkInPointFromKemo", "Gira")
            self._pos = so.getLocalToWorld()
        except:
            print("Error 1")
            try:
                some = PtGetLocalAvatar()
                self._pos = some.getLocalToWorld()
            except:
                print("Error 2")
    #
    def MovePlayersOutsideGiraDanceArea(self):
        agePlayers = PtGetPlayerList()
        agePlayers = [pl for pl in PtGetPlayerList() if not(pl.getPlayerID() in adminList)]
        agePlayers.append(PtGetLocalPlayer())
        for player in agePlayers:
            soav = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
            posav = soav.position()
            x = posav.getX() - self._x0
            y = posav.getY() - self._y0
            r = math.sqrt(x**2 + y**2)
            xx = posav.getX() - self._x1
            yy = posav.getY() - self._y1
            rr = math.sqrt(xx**2 + yy**2)
            if (r < self._r0 or rr < self._r1) and (posav.getZ() > -10 and posav.getZ() < 30):
                try:
                    print("SurveyPlayerInGiraDanceArea : Moving player => {0} => X={1}, Y={2}, Z={3}, x={4}, y={5}, r={6}".format(player.getPlayerName(), posav.getX(), posav.getY(), posav.getZ(), x, y, r))
                except:
                    print("Error 4")
                soav.netForce(1)
                try:
                    soav.physics.warp(self._pos)
                except:
                    print("Error 5")
    
    #
    def onAlarm(self, param=1):
        if not self._running:
            print("SurveyPlayerInGiraDanceArea : not running")
            return
        
        #
        if PtGetAgeInfo().getAgeFilename() != "Gira":
            print("SurveyPlayerInGiraDanceArea : I'm not in Gira, stop running")
            self.Stop()
            return
        
        self.MovePlayersOutsideGiraDanceArea()
        PtSetAlarm(0.25, self, 1)
        
    def Start(self):
        if not self._running:
            self._running = True
            print("SurveyPlayerInGiraDanceArea : start")
            self.onAlarm()

    def Stop(self):
        print("SurveyPlayerInGiraDanceArea:stop")
        self._running = False

#
surveille = None

#
def stopchecking():
    global surveille
    if isinstance(surveille, SurveyPlayerInGiraDanceArea):
        surveille.Stop()
        surveille = None

#
def startchecking():
    global surveille
    stopchecking()
    surveille = SurveyPlayerInGiraDanceArea()
    surveille.Start()

#
