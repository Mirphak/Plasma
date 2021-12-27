# -*- coding: cp1252 -*-

from Plasma import *
    
#def ShowHide(so = PtGetLocalAvatar(), b = True):
#def ShowHide(args = (PtGetLocalAvatar(), True)):
def ShowHide(args = (None, True)):
    if args[0] is None:
        args[0] = PtGetLocalAvatar()
    so = args[0]
    so.draw.netForce(1)
    so.draw.enable(args[1])
    args[1] = not args[1]
    return not b

#------------------------------------------------------------------------
#Classe pour controler a intervale regulier
#------------------------------------------------------------------------
class Ctrl:
    """methode a controler:
    """

    def __init__(self):
        self._running = False
        #delai par defaut: 60 s
        self._delay = 60.0
        self._bOnOff = True
        self._me = PtGetLocalAvatar()

    def onAlarm(self, context=1):
        if not self._running:
            return
        #print str(len(self._params)) + '; ' + str(self._bOnOff)
        if len(self._params) == 0:
            self._bOnOff = self._params[0]()
        elif len(self._params) == 1:
            self._bOnOff = self._params[0](self._params[1])
        else:
            self._running = False
            return
        PtSetAlarm(self._delay, self, 1)

    def Start(self, params = [], delay = None ):
        if params:
            self._params = params
        if delay:
            self._delay = delay
        if not self._running:
            self._running = True
            self.onAlarm()

    def Stop(self):
        self._running = False

#============================================
def pagein(prp = "Jalak", mode = 0):
    if mode == 0:
        PtConsoleNet("Nav.PageInNode {}".format(prp), 1)
    else:
        PtPageInNode(prp, 1)

def pageout(prp = "Jalak", mode = 0):
    if mode == 0:
        PtConsoleNet("Nav.PageOutNode {}".format(prp), 1)
    else:
        PtPageOutNode(prp, 1)

#===========================================


# Methode de deplacement V2 
def Deplacer(so1, so2, dx = 0, dy = 0, dz = 0, bPhys = True):
    """Deplacer le Sceneobject so1 vers so2 + options: decalage et physique"""
    pos2 = so2.getLocalToWorld()
    #vect = ptVector3(dx, dy, dz)
    #pos2.translate(vect)
    tpos2 = pos2.getData()
    x = tpos2[0][3] + dx
    y = tpos2[1][3] + dy
    z = tpos2[2][3] + dz
    tpos2 = ((tpos2[0][0], tpos2[0][1], tpos2[0][2], x), 
            (tpos2[1][0], tpos2[1][1], tpos2[1][2], y), 
            (tpos2[2][0], tpos2[2][1], tpos2[2][2], z), 
            (tpos2[3][0], tpos2[3][1], tpos2[3][2], tpos2[3][3]))
    pos2.setData(tpos2)
    so1.netForce(True)
    so1.physics.warp(pos2)
    if bPhys:
        so1.physics.enable()
    else:
        so1.physics.disable()

#attacher so1 a so2 : attacher(obj, av) ou l'inverse    
def Attacher(so1, so2, dx = 0, dy = 0, dz = 0, bPhys = False):
    """attacher so1 à so2 : attacher(obj, av) ou l'inverse"""
    so1.physics.netForce(1)
    so1.draw.netForce(1)
    Deplacer(so1, so2, dx, dy, dz, bPhys)
    PtAttachObject(so1, so2, 1)

# detacher so1 de so2 : detach(obj, av) ou l'inverse    
def Detacher(so1, so2):
    #so1.physics.netForce(1)
    #so1.draw.netForce(1)
    PtDetachObject(so1, so2, 1)
    #so1.physics.warp(PositionDefaut())
    #so1.physics.enable()
    #so1.physics.netForce(1)
    #so1.draw.netForce(1)

#
def AddPrp(nomAge = "Minkata"):
    if nomAge == "Minkata":
        pages = ["minkCameras"]
        for page in pages:
            PtConsoleNet("Nav.PageInNode %s" % (page) , 1)
    
#
def Soccer(av = None):
    if av is None:
        av = PtGetLocalAvatar()
    #nomAgeCourrant = PtGetAgeName()
    nomAge = "Minkata"
    prp = "minkCameras"
    nomObjet = "SoccerBall"
    so = PtFindSceneobject(nomObjet, nomAge)
    dx = 0
    dy = 0
    dz = 8
    bPhys = True
    Deplacer(so, av, dx, dy, dz, bPhys)
    
