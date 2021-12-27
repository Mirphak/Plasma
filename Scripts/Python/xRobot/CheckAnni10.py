# -*- coding: utf-8 -*-
from Plasma import *
import math


adminList = [
    32319,   # Mir-o-Bot
    31420,   # Mirphak
    2332508, # mob
    11896,   # MagicYoda
    115763,  # Willy
    127131,  # tsuno
    #133403L,  # sendlinger
    137998,  # Mabe
    254640,  # Eternal Seeker
    #254930L, # Kamikatze
    #966183L, # y e e s h a
    #2975513L, # Didi
    #1261291L, # Y E E R K
    5667000, # Minasunda
    #5710565L, # Salirama
    6495949, # Lu*
    #6559861L, # Kawliga
    #6583813L, # Roland (Mav Hungary)
    #6670690L, # Billy the Cat
    #6682907L, # LaDeeDah
    #6725908L, # Raymondo
    #6833983L, # malcg
    6961947, # Calisia (= Terry L. Britton)
    7060111, # Aeonihya
    7132841, # Mina Sunda
    #7172637L, # Baeda
    #7227499L, # Lidia (Mav Hungary)
    #7327507L, # artopia
    #7517653L, # ladylora
    #7731330L, # My.St'ro
    #7796072L, # Klaide
    #7881034L, # Yakoso
    7939982, # Claidi Song
    #7965725L, # Z A N D l
    8068100, # NDG Eternal Seeker
    8315178, # Roland (Mav Hungary)
]

"""
    "GreatZero":["LinkInPointDefault", "BigRoomLinkInPoint", "GZIntStart"
"""
#====================================#
# Survey Player in GreatZero Dance Area #
#====================================#
class SurveyPlayerInGreatZeroDanceArea:
    _running = False
    _pos = ptMatrix44()
    _x0 = 0.0
    _y0 = 0.0
    _r0 = 30.0
    _x1 = 0.0
    _y1 = -35.0
    _r1 = 15.0
    _x2 = -10.0
    _y2 = -35.0
    _r2 = 15.0
    _x3 = 10.0
    _y3 = -35.0
    _r3 = 15.0

    #
    def __init__(self):
        print("SurveyPlayerInGreatZeroDanceArea : init")
        try:
            so = PtFindSceneobject("BigRoomLinkInPoint", "GreatZero")
            self._pos = so.getLocalToWorld()
        except:
            print("Error 1")
            try:
                some = PtGetLocalAvatar()
                self._pos = some.getLocalToWorld()
            except:
                print("Error 2")
    #
    def MovePlayersOutsideGreatZeroDanceArea(self):
        agePlayers = PtGetPlayerList()
        agePlayers = [pl for pl in PtGetPlayerList() if not(pl.getPlayerID() in adminList)]
        agePlayers.append(PtGetLocalPlayer())
        for player in agePlayers:
            soav = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
            posav = soav.position()
            rr0 = math.sqrt((posav.getX() - self._x0)**2 + (posav.getY() - self._y0)**2)
            rr1 = math.sqrt((posav.getX() - self._x1)**2 + (posav.getY() - self._y1)**2)
            rr2 = math.sqrt((posav.getX() - self._x2)**2 + (posav.getY() - self._y2)**2)
            rr3 = math.sqrt((posav.getX() - self._x3)**2 + (posav.getY() - self._y3)**2)
            if (rr0 < self._r0 or rr1 < self._r1 or rr2 < self._r2 or rr3 < self._r3) and (posav.getZ() > -50 and posav.getZ() < 20):
                try:
                    print("SurveyPlayerInGreatZeroDanceArea : Moving player => {0} => X={1}, Y={2}, Z={3}, x={4}, y={5}, r={6}".format(player.getPlayerName(), posav.getX(), posav.getY(), posav.getZ(), x, y, r))
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
            print("SurveyPlayerInGreatZeroDanceArea : not running")
            return
        
        #
        if PtGetAgeInfo().getAgeFilename() != "GreatZero":
            print("SurveyPlayerInGreatZeroDanceArea : I'm not in GreatZero, stop running")
            self.Stop()
            return
        
        self.MovePlayersOutsideGreatZeroDanceArea()
        PtSetAlarm(0.25, self, 1)
        
    def Start(self):
        if not self._running:
            self._running = True
            print("SurveyPlayerInGreatZeroDanceArea : start")
            self.onAlarm()

    def Stop(self):
        print("SurveyPlayerInGreatZeroDanceArea:stop")
        self._running = False

#
surveille = None

#
def stopchecking():
    global surveille
    if isinstance(surveille, SurveyPlayerInGreatZeroDanceArea):
        surveille.Stop()
        surveille = None

#
def startchecking():
    global surveille
    stopchecking()
    surveille = SurveyPlayerInGreatZeroDanceArea()
    surveille.Start()

#
