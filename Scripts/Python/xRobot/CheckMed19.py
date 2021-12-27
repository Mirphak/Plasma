# -*- coding: utf-8 -*-
from Plasma import *
import math


adminList = [
    32319,   # Mir-o-Bot
    31420,   # Mirphak
    2332508, # mob
    11896,  # MagicYoda
    #115763L,  # Willy
    127131,  # tsuno
    #133403L,  # sendlinger
    137998,  # Mabe
    254640,  # Eternal Seeker
    254930,  # Kamikatze
    #966183L,  # y e e s h a
    #2975513L, # Didi
    #1261291L, # Y E E R K
    5667000, # Minasunda
    5710565, # Salirama
    #6725908L, # Raymondo
    #6559861L, # Kawliga
    #6583813L, # Roland (Mav Hungary)
    6682907,  # 
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
    #8068100L,  # NDG Eternal Seeker
    #8315178L,  # Roland (Mav Hungary)
]


#====================================#
# Survey Player in Tsogal Dance Area #
#====================================#
class SurveyPlayerInTsogalDanceArea:
    _running = False
    _pos = ptMatrix44()
    _x0 = -68.0
    _y0 = 98.0
    _r0 = 15.0
    _x1 = -50.4
    _y1 = 103.8
    _r1 = 7.0

    #
    def __init__(self):
        print("SurveyPlayerInTsogalDanceArea : init")
        try:
            so = PtFindSceneobject("HoodLinkingBookPOS", "EderTsogal")
            self._pos = so.getLocalToWorld()
        except:
            print("Error 1")
            try:
                some = PtGetLocalAvatar()
                self._pos = some.getLocalToWorld()
            except:
                print("Error 2")
    #
    def MovePlayersOutsideTsogalDanceArea(self):
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
                    print("SurveyPlayerInTsogalDanceArea : Moving player => {0} => X={1}, Y={2}, Z={3}, x={4}, y={5}, r={6}".format(player.getPlayerName(), posav.getX(), posav.getY(), posav.getZ(), x, y, r))
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
            print("SurveyPlayerInTsogalDanceArea : not running")
            return
        
        #
        if PtGetAgeInfo().getAgeFilename() != "EderTsogal":
            print("SurveyPlayerInTsogalDanceArea : I'm not in Tsogal, stop running")
            self.Stop()
            return
        
        self.MovePlayersOutsideTsogalDanceArea()
        PtSetAlarm(0.25, self, 1)
        
    def Start(self):
        if not self._running:
            self._running = True
            print("SurveyPlayerInTsogalDanceArea : start")
            self.onAlarm()

    def Stop(self):
        print("SurveyPlayerInTsogalDanceArea:stop")
        self._running = False

#
surveille = None

#
def stopchecking():
    global surveille
    if isinstance(surveille, SurveyPlayerInTsogalDanceArea):
        surveille.Stop()
        surveille = None

#
def startchecking():
    global surveille
    stopchecking()
    surveille = SurveyPlayerInTsogalDanceArea()
    surveille.Start()

#
