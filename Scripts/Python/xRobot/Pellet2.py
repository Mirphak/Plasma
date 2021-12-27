# -*- coding: utf-8 -*-

"""
    Version 1 : 15/11/2014
    Version 2 : 04/06/2016
    Version 3 : 03/11/2019
"""
from Plasma import *
from . import xBotAge
from . import Sky

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
        print("Responder():\tResponder not found...")
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

#**********************************************************************

# BahroSymbolDecal + (N E S W) + _0 + (1 à 7)
soNameSymbols = [
    "BahroSymbolDecalN_01", 
    "BahroSymbolDecalE_01", 
    "BahroSymbolDecalS_01", 
    "BahroSymbolDecalW_01", 
    "BahroSymbolDecalN_02", 
    "BahroSymbolDecalE_02", 
    "BahroSymbolDecalS_02", 
    "BahroSymbolDecalW_02", 
    "BahroSymbolDecalN_03", 
    "BahroSymbolDecalE_03", 
    "BahroSymbolDecalS_03", 
    "BahroSymbolDecalW_03", 
    "BahroSymbolDecalN_04", 
    "BahroSymbolDecalE_04", 
    "BahroSymbolDecalS_04", 
    "BahroSymbolDecalW_04", 
    "BahroSymbolDecalN_05", 
    "BahroSymbolDecalE_05", 
    "BahroSymbolDecalS_05", 
    "BahroSymbolDecalW_05", 
    "BahroSymbolDecalN_06", 
    "BahroSymbolDecalE_06", 
    "BahroSymbolDecalS_06", 
    "BahroSymbolDecalW_06", 
    "BahroSymbolDecalN_07", 
    "BahroSymbolDecalE_07", 
    "BahroSymbolDecalS_07", 
    "BahroSymbolDecalW_07", 
    ]

# cRepSolutionSymbols + (On Off) + (N E S W)
symbolResps = [
    "cRepSolutionSymbolsOnN", 
    "cRepSolutionSymbolsOffN", 
    "cRepSolutionSymbolsOnE", 
    "cRepSolutionSymbolsOffE", 
    "cRepSolutionSymbolsOnS", 
    "cRepSolutionSymbolsOffS", 
    "cRepSolutionSymbolsOnW", 
    "cRepSolutionSymbolsOffW", 
    ]

# entree en haut avec un pellet
liwp={"LinkInWithPellet":["cRespFadeInPellet", "cRespDropPellet"]}

age = "PelletBahroCave"

#def RunResponder(key, resp, stateidx = None, netForce = 1, netPropagate = 1, fastforward = 0):
def pellet(respnum=0):
    so = PtFindSceneobject("LinkInWithPellet", age)
    sok = so.getKey()
    rn = liwp["LinkInWithPellet"][respnum]
    for resp in so.getResponders():
        if resp.getName() == rn:
            RunResponder(sok, resp)
            break

#def RunResponder(key, resp, stateidx = None, netForce = 1, netPropagate = 1, fastforward = 0):
def symbol(quad="N", n=1, bOn=True):
    quad = quad.upper()
    if quad not in ("N", "E", "S", "W"):
        quad = "N"
    if n not in list(range(1, 7)):
        n = 1
    #soName = "BahroSymbolDecal" + quad + "_0" + str(n)
    soName = "BahroSymbolDecal" + quad + "_01"
    so = PtFindSceneobject(soName, age)
    print("so {} found".format(soName))
    sok = so.getKey()
    OnOff = "Off"
    if bOn:
        OnOff = "On"
    rn = "cRespSolutionSymbols" + OnOff + quad
    print("resp {} search...".format(rn))
    for resp in so.getResponders():
        print("= resp {} ?".format(resp.getName()))
        if resp.getName() == rn:
            print("resp {} found".format(rn))
            RunResponder(sok, resp, n)
            break

#def RunResponder(key, resp, stateidx = None, netForce = 1, netPropagate = 1, fastforward = 0):
def machine(n=0):
    if n not in list(range(0, 6)):
        n = 0
    soName = "MachineCamRespDummy"
    so = PtFindSceneobject(soName, age)
    #print "so {} found".format(soName)
    sok = so.getKey()
    #rn = "cRespSolutionSymbols" + OnOff + quad
    #print "resp {} search...".format(rn)
    """
    for resp in so.getResponders():
        print "= resp {} ?".format(resp.getName())
        if resp.getName() == rn:
            print "resp {} found".format(rn)
            RunResponder(sok, resp)
            break
    """
    RunResponder(sok, so.getResponders()[n])

#
def drop():
    pellet(0)
    pellet(1)
    machine(4)
    symbol("N", 2, True)
    symbol("E", 4, True)
    symbol("S", 3, True)
    symbol("W", 7, True)

# =====================================================================

# A TESTER la machine a pellet de ErcanaCitySilo
# Faire 5 + (0, 1, 2, 3, 4 ou 6)
# !toggle Walls  0 1
#toggle Caustic  1 1
def silomachine(n=0):
    if n not in list(range(0, 9)):
        n = 0
    soName = "MachineCamRespDummy"
    so = PtFindSceneobject(soName, "ErcanaCitySilo")
    #print "so {} found".format(soName)
    sok = so.getKey()
    #rn = "cRespSolutionSymbols" + OnOff + quad
    #print "resp {} search...".format(rn)
    """
    for resp in so.getResponders():
        print "= resp {} ?".format(resp.getName())
        if resp.getName() == rn:
            print "resp {} found".format(rn)
            RunResponder(sok, resp)
            break
    """
    RunResponder(sok, so.getResponders()[n])

# =====================================================================

"""
    * A FAIRE :
        - Classe AutoDropPelettes():
            Appeler machine(n=0 a 5) aleatoirement avec tempo
            0 : explosion <= 1s   , n'eclaire pas
            1 : bulles 23s env    , n'eclaire pas
            2 : fumée 10s env     , n'eclaire pas
            3 : orange 18s env    , illumine
            4 : blanche 18s env   , illumine bien
            5 : plouf pellet < 1s , n'eclaire pas
            
            => il faut que je lance alternativement 3 et 4 a 9s d'intervalle
            
        - Montrer un petroglyphe a la fois
            * PelletBahroCave paintings :
                - Painting01
                - Painting02
                - Painting03
                - Painting04
                - Painting05
                - Painting06
                - Painting07
                - Painting08
                - Painting09
                - Painting10
                - Painting11
                - Painting12
                - Painting13
                - Painting14
                - Painting15
                - Painting16
                - Painting17
        - Cacher les murs et le CircleGrid (le brouillard et le ciel c'est inutile)
            => !toggle Wall  0 1
            => !toggle CircleGrid  0 1
        - Faire un ciel uni changeant de couleur
            xRobot.Sky as s
            s.Start(0.5)
            s.Stop()
"""

# Auto drop pellets alternatively orange and white
class AutoPellet:
    running = False
    #delay   = 18.6
    delay   = 19.0
    ageGuid = None

    def __init__(self):
        pass

    def onAlarm(self, context=1):
        if self.ageGuid != PtGetAgeInfo().getAgeInstanceGuid():
            self.running = False
        if not self.running:
            return
        # On illumine
        if context == 1 :
            #print "1 => 3"
            machine(n=3)
            # on rappelle set alarm
            PtSetAlarm(self.delay, self, 2)
        else :
            #print "autre => 4"
            machine(n=4)
            # on rappelle set alarm
            PtSetAlarm(self.delay, self, 1)

# Auto drop pellets
class AutoDropPellets:
    running = False
    delay   = 19.0
    ageGuid = None
    pelletType = 4
    """
        Pellet types :
            - 0 : explosion <= 1s   , n'eclaire pas
            - 1 : bulles 23s env    , n'eclaire pas
            - 2 : fumée 10s env     , n'eclaire pas
            - 3 : orange 18s env    , illumine
            - 4 : blanche 18s env   , illumine bien
            - 5 : plouf pellet < 1s , n'eclaire pas
    """

    def __init__(self):
        pass

    def onAlarm(self, context=1):
        if self.ageGuid != PtGetAgeInfo().getAgeInstanceGuid():
            self.running = False
        if not self.running:
            return
        # Drop a pellet of choosen pellet type
        machine(n=self.pelletType)
        # Wait loop
        PtSetAlarm(self.delay, self, 1)

# init classes
autoPellet = AutoPellet()
autoDropPellets = AutoDropPellets()

# Start AutoPellet.
def Start(delay=None):
    autoPellet.ageGuid = PtGetAgeInfo().getAgeInstanceGuid()
    if isinstance(delay, float):
        autoPellet.delay = delay
    if not autoPellet.running:
        autoPellet.running = True
        autoPellet.onAlarm()

# Stop AutoPellet.
def Stop():
    autoPellet.running = False

# Start AutoDropPellets (default : drops a white pellet every 19s).
def StartDropPellets(type=4, delay=19.0):
    global autoDropPellets
    if not isinstance(autoDropPellets, AutoDropPellets):
        autoDropPellets = AutoDropPellets()
    autoDropPellets.ageGuid = PtGetAgeInfo().getAgeInstanceGuid()
    if isinstance(delay, int):
        autoDropPellets.pelletType = type
    else:
        autoDropPellets.pelletType = 4
    if isinstance(delay, float):
        autoDropPellets.delay = delay
    else:
        autoDropPellets.delay = 19.0
    if not autoDropPellets.running:
        autoDropPellets.running = True
        autoDropPellets.onAlarm()

# Stop AutoDropPellets.
def StopDropPellets():
    global autoDropPellets
    #if isinstance(autoDropPellets, AutoDropPellets):
    autoDropPellets.running = False
    autoDropPellets = None

# 
class AutoPelletSilo:
    running = False
    #delay   = 18.6
    delay   = 19.0
    ageGuid = None
    n = 0

    def __init__(self):
        pass

    def onAlarm(self, context=1):
        if self.ageGuid != PtGetAgeInfo().getAgeInstanceGuid():
            self.running = False
        if not self.running:
            return
        # On illumine
        if context == 1 :
            #print "1 => 3"
            silomachine(n=5)
            # on rappelle set alarm
            PtSetAlarm(3, self, 2)
        else :
            #print "autre => 4"
            machine(n=self.n)
            self.n = self.n + 1
            if self.n == 5 :
                self.n = 6
            elif self.n > 6 :
                self.n = 0
            # on rappelle set alarm
            PtSetAlarm(self.delay, self, 1)

# init class
autoPelletSilo = AutoPelletSilo()

# Start AutoPelletSilo.
def StartSilo(delay=None):
    autoPelletSilo.ageGuid = PtGetAgeInfo().getAgeInstanceGuid()
    if isinstance(delay, float):
        autoPelletSilo.delay = delay
    if not autoPelletSilo.running:
        autoPelletSilo.running = True
        autoPelletSilo.onAlarm()

# Stop AutoPelletSilo.
def StopSilo():
    autoPelletSilo.running = False

# Afficher un seul petroglyphe, et cacher le reste
def Show(n=-1):
    ageFileName = "PelletBahroCave"
    objNameBase = "Painting"
    """
    lstPetro = [
        "Painting01", 
        "Painting02", 
        "Painting03", 
        "Painting04", 
        "Painting05", 
        "Painting06", 
        "Painting07", 
        "Painting08", 
        "Painting09", 
        "Painting10", 
        "Painting11", 
        "Painting12", 
        "Painting13", 
        "Painting14", 
        "Painting15", 
        "Painting16", 
        "Painting17" 
    ]
    """
    xBotAge.ToggleSceneObjects(name="CircleGrid", age=ageFileName, bDrawOn=False, bPhysicsOn=True)
    xBotAge.ToggleSceneObjects(name="Wall", age=ageFileName, bDrawOn=False, bPhysicsOn=True)
    xBotAge.ToggleSceneObjects(name="HoleCollider", age=ageFileName, bDrawOn=False, bPhysicsOn=False)
    xBotAge.ToggleSceneObjects(name="Caustics", age=ageFileName, bDrawOn=False, bPhysicsOn=True)
    xBotAge.ToggleSceneObjects(name=objNameBase, age=ageFileName, bDrawOn=False, bPhysicsOn=True)
    """
    obj = PtFindSceneobject(self._obj, ageFileName)
    obj.netForce(1)
    obj.draw.enable(1)
    """
    if 1 <= n <= 17 :
        objName = objNameBase + str(n).zfill(2)
        print("Showing painting #{0} : {1}".format(n, objName))
        xBotAge.ToggleSceneObjects(name=objName, age=ageFileName, bDrawOn=True, bPhysicsOn=True)
    elif n == 0 :
        print("Showing all paintings")
        xBotAge.ToggleSceneObjects(name=objNameBase, age=ageFileName, bDrawOn=True, bPhysicsOn=True)
    else :
        print("Normal cave")
        xBotAge.ToggleSceneObjects(name="CircleGrid", age=ageFileName, bDrawOn=True, bPhysicsOn=True)
        xBotAge.ToggleSceneObjects(name="CaveWall", age=ageFileName, bDrawOn=True, bPhysicsOn=True)
        xBotAge.ToggleSceneObjects(name="HoleCollider", age=ageFileName, bDrawOn=True, bPhysicsOn=True)
        xBotAge.ToggleSceneObjects(name="Caustics", age=ageFileName, bDrawOn=True, bPhysicsOn=True)
        xBotAge.ToggleSceneObjects(name=objNameBase, age=ageFileName, bDrawOn=True, bPhysicsOn=True)

#************************************************

# Set the sky color in RGV (0-255) without fog
def SetSkyColor(r, g, b):
    xBotAge.NoFog()
    xBotAge.SetRendererClearColor(vcr=r/255.0, vcg=g/255.0, vcb=b/255.0)
 
#
def ChangeSky(bOn=True):
    if bOn:
        Sky.Start(delay=0.5, start=0, end=0, density=0)
    else:
        Sky.Stop()

#
def DropPellets(bOn=True, type=4, delay=19.0):
    if bOn:
        StartDropPellets(type, delay)
    else:
        StopDropPellets()

#
def AutoDropWhitePellets(bOn=True):
    if bOn:
        StartDropPellets(type=4, delay=19.0)
    else:
        StopDropPellets()

#
def ShowPaintings(nb=-1):
    Show(n=nb)
    
    if nb >= -1 and nb <= 17:
        StartDropPellets(type=4, delay=19.0)
    else:
        StopDropPellets()
    """
    if nb == 0 :
        #Sky.Start(delay=0.5, start=0, end=0, density=0)
        ChangeSky(bOn=True)
    else :
        #Sky.Stop()
        ChangeSky(bOn=False)
    """
    if nb == 1 :
        SetSkyColor(r=144.69, g=135.15, b=131.79)
    elif nb == 2 :
        SetSkyColor(r=144.69, g=135.15, b=131.79)
    elif nb == 3 :
        SetSkyColor(r=144.69, g=135.15, b=131.79)
    elif nb == 4 :
        SetSkyColor(r=144.69, g=135.15, b=131.79)
    elif nb == 5 :
        SetSkyColor(r=144.69, g=135.15, b=131.79)
    elif nb == 6 :
        SetSkyColor(r=144.69, g=135.15, b=131.79)
    elif nb == 7 :
        SetSkyColor(r=144.69, g=135.15, b=131.79)
    elif nb == 8 :
        SetSkyColor(r=144.69, g=135.15, b=131.79)
    elif nb == 9 :
        SetSkyColor(r=144.69, g=135.15, b=131.79)
    elif nb == 10 :
        SetSkyColor(r=144.69, g=135.15, b=131.79)
    elif nb == 11 :
        SetSkyColor(r=144.69, g=135.15, b=131.79)
    elif nb == 12 :
        SetSkyColor(r=144.69, g=135.15, b=131.79)
    elif nb == 13 :
        SetSkyColor(r=144.69, g=135.15, b=131.79)
    elif nb == 14 :
        SetSkyColor(r=144.69, g=135.15, b=131.79)
    elif nb == 15 :
        SetSkyColor(r=144.69, g=135.15, b=131.79)
    elif nb == 16 :
        SetSkyColor(r=144.69, g=135.15, b=131.79)
    elif nb == 17 :
        SetSkyColor(r=144.69, g=135.15, b=131.79)
    else:
        SetSkyColor(r=48.23, g=45.05, b=43.93)

# Auto show paintings
class AutoShowPaintings:
    running = False
    delay   = 1.0
    ageGuid = None
    nb = 1
    
    def __init__(self):
        pass
    
    def onAlarm(self, context=1):
        #if self.ageGuid != PtGetAgeInfo().getAgeInstanceGuid():
        #    self.running = False
        if not self.running:
            return
        if context == 1:
            # Start and accelerate
            Show(n=self.nb)
            if self.nb > 17:
                self.nb = 1
                if self.delay > 0.0625:
                    self.delay = self.delay - 0.0625
                else:
                    self.nb = 0
            elif self.nb > 0:
                self.nb = self.nb + 1
            else:
                pass
            # Wait loop
            PtSetAlarm(self.delay, self, 1)
        else:
            # Decelarate and stop
            Show(n=self.nb)
            if self.nb > 17:
                self.nb = 1
                if self.delay < 1:
                    self.delay = self.delay + 0.0625
                else:
                    self.nb = -1
            elif self.nb > 0:
                self.nb = self.nb + 1
            else:
                #pass
                self.running = False
            # Wait loop
            PtSetAlarm(self.delay, self, 2)

# init classe
autoShowPaintings = AutoShowPaintings()

# Start AutoShowPaintings.
def StartShowPaintings(delay=None):
    autoShowPaintings.ageGuid = PtGetAgeInfo().getAgeInstanceGuid()
    if isinstance(delay, float):
        autoShowPaintings.delay = delay
    if not autoPellet.running:
        autoShowPaintings.running = True
        autoShowPaintings.onAlarm()

# Stop AutoShowPaintings.
def StopShowPaintings():
    #autoShowPaintings.running = False
    PtSetAlarm(0, autoShowPaintings, 2)

# 
def Faster():
    if autoShowPaintings.delay > 0.0625:
        autoShowPaintings.delay = autoShowPaintings.delay - 0.0625

#
def Slower():
    autoShowPaintings.delay = autoShowPaintings.delay + 0.0625

#

def pageinPellet():
    PtConsoleNet("Nav.PageInNode PelletBahroCave_Cave", True)

#