# -*- coding: utf-8 -*-
from Plasma import *
import math

adminList = [
    32319,   # Mir-o-Bot
    31420,   # Mirphak
    2332508, # mob
    11243,   # Luluberlu
    11896,   # MagicYoda
    #115763,  # Willy
    127131,  # tsuno
    #133403,  # sendlinger
    137998,  # Mabe
    254640,  # Eternal Seeker
    254930, # Kamikatze
    #966183, # y e e s h a
    2975513, # Didi
    #1261291, # Y E E R K
    #1474572, # Fog_man
    5667000, # Minasunda
    #5710565, # Salirama
    6362551, # vony
    6495949, # Lu*
    6551797, # ondine
    #6559861, # Kawliga
    #6583813, # Roland (Mav Hungary)
    #6670690, # Billy the Cat
    6682907, # LaDeeDah
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
    #9843955, # CatYoh
    9995228, # NDGSeeker
    #10287894, # Thallan
    #10360615, # Thallane
]


#====================================#
# Survey Player in Serene Dance Area #
#====================================#
class SurveyPlayerInSereneDanceArea:
    _running = False
    _pos = ptMatrix44()
    _x0 = 46.0
    _y0 = 35.0
    _r0 = 21.0
    #_x1 = 60.0
    #_y1 = -11.0
    #_r1 = 12.0

    #
    def __init__(self):
        print("SurveyPlayerInSereneDanceArea : init")
        try:
            #so = PtFindSceneobject("LinkInPointDefault", "Serene")
            so = PtFindSceneobject("Plane02", "Serene")
            self._pos = so.getLocalToWorld()
        except:
            print("Error 1")
            try:
                some = PtGetLocalAvatar()
                self._pos = some.getLocalToWorld()
            except:
                print("Error 2")
    #
    def MovePlayersOutsideSereneDanceArea(self):
        agePlayers = PtGetPlayerList()
        agePlayers = [pl for pl in PtGetPlayerList() if not(pl.getPlayerID() in adminList)]
        agePlayers.append(PtGetLocalPlayer())
        for player in agePlayers:
            soav = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
            posav = soav.position()
            x = posav.getX() - self._x0
            y = posav.getY() - self._y0
            r = math.sqrt(x**2 + y**2)
            #xx = posav.getX() - self._x1
            #yy = posav.getY() - self._y1
            #rr = math.sqrt(xx**2 + yy**2)
            #if (r < self._r0 or rr < self._r1) and (posav.getZ() > -10 and posav.getZ() < 30):
            if (r < self._r0) and (posav.getZ() > -10 and posav.getZ() < 30):
                try:
                    print("SurveyPlayerInSereneDanceArea : Moving player => {0} => X={1}, Y={2}, Z={3}, x={4}, y={5}, r={6}".format(player.getPlayerName(), posav.getX(), posav.getY(), posav.getZ(), x, y, r))
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
            print("SurveyPlayerInSereneDanceArea : not running")
            return
        
        #
        if PtGetAgeInfo().getAgeFilename() != "Serene":
            print("SurveyPlayerInSereneDanceArea : I'm not in Serene, stop running")
            self.Stop()
            return
        
        self.MovePlayersOutsideSereneDanceArea()
        PtSetAlarm(0.25, self, 1)
        
    def Start(self):
        if not self._running:
            self._running = True
            print("SurveyPlayerInSereneDanceArea : start")
            self.onAlarm()

    def Stop(self):
        print("SurveyPlayerInSereneDanceArea:stop")
        self._running = False

#
surveille = None

#
def stopchecking():
    global surveille
    if isinstance(surveille, SurveyPlayerInSereneDanceArea):
        surveille.Stop()
        surveille = None

#
def startchecking():
    global surveille
    stopchecking()
    surveille = SurveyPlayerInSereneDanceArea()
    surveille.Start()

#
