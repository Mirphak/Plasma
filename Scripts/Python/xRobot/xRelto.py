# -*- coding: utf-8 -*-
# == Commandes specifiques au Relto ==
from Plasma import *
import math

age = "Personal"
pages = ["pnslMYSTII"]

bPagesAdded = False

# Dictionnaire des clones
dicClones = {}
dicClones.update({"FissureStarField":[]})


def AddPrp():
    global bPagesAdded
    for page in pages:
        PtConsoleNet("Nav.PageInNode %s" % (page) , 1)
    bPagesAdded = True

def DelPrp():
    global bPagesAdded
    for page in pages:
        PtConsoleNet("Nav.PageOutNode %s" % (page) , 1)
    bPagesAdded = False

def DelPrpLocal():
    global bPagesAdded
    if bPagesAdded:
        for page in pages:
            PtPageOutNode(page)
        bPagesAdded = False

def ToggleObjects(name, bOn = True):
    pf = PtFindSceneobjects(name)
    for so in pf:
        so.netForce(1)
        so.draw.enable(bOn)

def ToggleObject(name, bOn = True):
    so = PtFindSceneobject(name, age)
    if so is not None:
        so.netForce(1)
        so.draw.enable(bOn)

#
#def Scale(name = "FissureStarField", scale = 2)
#    pf = PtFindSceneobjects(name)
#    scale = ptMatrix44()
#    scale.makeScaleMat(ptVector3(2, 2, 2))

bAlreadyScaled = False
#
def RotateSceneObjects(name = "FissureStarField", strAxis = "x", angle = 0, scale = 1):
    global bAlreadyScaled
    pf = PtFindSceneobjects(name)
    mrot = ptMatrix44()
    axis = 0
    if strAxis == 'x':
        axis = 0
    elif strAxis == 'y':
        axis = 1
    elif strAxis == 'z':
        axis = 2
    else:
        return 0
    try:
        mrot.rotate(axis, (math.pi * float(angle)) / 180)
    except ValueError:
        return 0
    mscale = ptMatrix44()
    if bAlreadyScaled:
        mscale.makeScaleMat(ptVector3(1./scale, 1./scale, 1./scale))
        bAlreadyScaled = False
    else:
        mscale.makeScaleMat(ptVector3(scale, scale, scale))
        bAlreadyScaled = True
    for so in pf:
        try:
            pos = so.getLocalToWorld()
            so.netForce(1)
            so.physics.warp(pos * mscale * mrot)
        except RuntimeError:
            pass
    return 1

bFog = True
bSkyHigh = True
bSkyHighStormy = False
phase = 0
#
def EnableAll(bOn = True):
    global bFog
    global bSkyHigh
    global bSkyHighStormy
    global phase
    ToggleObjects("Floor", bOn)
    ToggleObjects("Library", bOn)
    ToggleObjects("Door", bOn)
    #ToggleObjects("Fog", bOn)
    #ToggleObjects("Fissure", not bOn)
    
    if bOn:
        SetFog("default")
        #ToggleObjects("Fissure", True)
        #ToggleObjects("FissureStarField", False)
        #RotateSceneObjects(name = "FissureStarField", strAxis = "x", angle = 180, scale = 7.5)
    else:
        ##SetFog("", 0, 0, 0)
        SetFog("nofog")
        #ToggleObjects("Fissure", False)
        #ToggleObjects("FissureStarField", True)
        #RotateSceneObjects(name = "FissureStarField", strAxis = "x", angle = -180, scale = 7.5)
        ##ToggleObjects("Fog", bool((phase%5)%2))
        #ToggleObjects("SkyHigh", bool((phase%4)%2))
        #ToggleObjects("SkyHighStormy", bool(((phase%3)+1)%2))
    phase = (phase + 1) % 12

#
def SetFog(style = "default", start = 0, end = 0, density = 0, r = 0.4, g = 0.4, b = 0.5, cr = 0.4, cg = 0.4, cb = 0.5):
    #default (see fni settings)
    if style == "default":
        print "default"
        fy = "Graphics.Renderer.Setyon 10000"
        fd = "Graphics.Renderer.Fog.SetDefLinear 1 900 2"
        fc = "Graphics.Renderer.Fog.SetDefColor .4 .4 .5"
        cc = "Graphics.Renderer.SetClearColor .4 .4 .5"
    elif style == "nofog":
        print "nofog"
        fy = "Graphics.Renderer.Setyon 10000"
        fd = "Graphics.Renderer.Fog.SetDefLinear 0 0 0"
        fc = "Graphics.Renderer.Fog.SetDefColor .4 .4 .5"
        cc = "Graphics.Renderer.SetClearColor .1 .1 .3"
    #personalized style
    else:
        print "personalized"
        try:
            yon = int(style)
            fy = "Graphics.Renderer.Setyon %i" % (yon)
        except:
            fy = "Graphics.Renderer.Setyon 10000"
        #if isinstance(style, int):
        #    fy = "Graphics.Renderer.Setyon %i" % (style)
        #else:
        #    fy = "Graphics.Renderer.Setyon 10000"
        fd = "Graphics.Renderer.Fog.SetDefLinear %i %i %f" % (start, end, density)
        fc = "Graphics.Renderer.Fog.SetDefColor %f %f %f" % (r, g, b)
        #cc = "Graphics.Renderer.SetClearColor .0 .0 .0"
        cc = "Graphics.Renderer.SetClearColor %f %f %f" % (cr, cg, cb)
    PtConsoleNet(fy, True)
    PtConsoleNet(fd, True)
    PtConsoleNet(fc, True)
    PtConsoleNet(cc, True)

#
class AlarmAddPrp:
    def onAlarm(self, context):
        AddPrp()

#
class AlarmEnableAll:
    def onAlarm(self, context = 0):
        EnableAll(context)

# Unload all the clones
def DechargerClones(masterKey):
    #masterKey2 = PtFindSceneobject("FissureStarField", age).getKey()
    cloneKeys = PtFindClones(masterKey)
    for ck in cloneKeys:
        PtCloneKey(ck, 0)

# Reload all the clones
def RechargerClones(masterKey):
    #masterKey2 = PtFindSceneobject("FissureStarField", age).getKey()
    cloneKeys = PtFindClones(masterKey)
    for ck in cloneKeys:
        PtCloneKey(ck, 1)

#
class AlarmCloneFissureStarField:
    _masterKey = PtFindSceneobject("FissureStarField", age).getKey()
    _nombre = 1
    _delais = 1
    _maxAttempts = 5
    _attempts = 1
    def onAlarm(self, context = 0):
        CloneFissureStarField(self._masterKey)

    # Initialisation
    def __init__(self, nombre):
        self._nombre = nombre
        self._delais = 1
        self._attempts = 1
        print "init AlarmCloneFissureStarField(%i)" % self._nombre

    # Clonage general (n clones)
    def Cloner(self, nombre):
        for i in range(nombre):
            PtCloneKey(self._masterKey, 1)

    # Prenons notre temps...
    def onAlarm(self, param):
        if param == 1:
            # partie 1 : clonage
            print "clonage en cours..."
            # Existe-t-il deja des clones?
            n = len(PtFindClones(self._masterKey))
            if n < self._nombre:
                # Il nous en faut (self._nombre - n) en plus
                self.Cloner(self._nombre - n)
            PtSetAlarm(self._delais, self, 2)
        elif param == 2:
            # partie 2 : sauvegarde des clones
            n = len(PtFindClones(self._masterKey))
            # attendre que tous les clones soient crees
            if n < self._nombre:
                print "%i clones trouves sur les %i demandes! (attempt #%i)" % (n, self._nombre, self._attempts)
                if self._attempts < self._maxAttempts:
                    self._attempts = self._attempts + 1
                    PtSetAlarm(self._delais, self, 2)
                else:
                    print "Le clonage met trop de temps!!"
            else:
                print "sauvegarde des %i clones..." % n
                self.saveClones()
        else:
            print "AlarmCloneFissureStarField.onAlarm : param incorrect"

    # Sauvons les clones!
    def saveClones(self):
        global dicClones
        dicClones["FissureStarField"] = PtFindClones(self._masterKey)
        print "nb clones: " + str(len(dicClones["FissureStarField"]))

#
def CloneFissureStarField(nombre):
    print "CloneFissureStarField()"
    PtSetAlarm(1, AlarmCloneFissureStarField(nombre), 1)

#
class AlarmWaittingForClones:
    _nbFois = 0
    _nbClones = 0
    _scale = 1
    #_masterName = "FissureStarField"
    
    def __init__(self, nombre, scale):
        self._nbClones = nombre
        self._scale = scale
    
    def onAlarm(self, param):
        print "> AlarmWaitting.onAlarm"
        if param == 1:
            nbClonesFound = len(dicClones["FissureStarField"])
            print ">> nb de clones de %s %i" % ("FissureStarField", nbClonesFound)
            # Attendre que tous les clones soient crees, mais pas indefiniment au cas ou
            if (nbClonesFound < self._nbClones and self._nbFois < 20):
                self._nbFois += 1
                print ">>> Attente nb: %i" % self._nbFois
                PtSetAlarm(1, self, 1)
            else:
                PtSetAlarm(1, self, 2)
        elif param == 2:
            nbClonesFound = len(dicClones["FissureStarField"])
            print ">> nb de clones de %s %i" % ("FissureStarField", nbClonesFound)
            if (self._nbFois < 20):
                print ">> Les clones sont prets."
                soMaster = PtFindSceneobject("FissureStarField", age)
                # Masquons les clones surnumeraires s'il y en a
                for i in range(0,nbClonesFound - 2):
                    so = dicClones["FissureStarField"][i].getSceneObject()
                    so.draw.netForce(1)
                    so.draw.enable(0)
                # Manipulons les clones
                soTop = dicClones["FissureStarField"][nbClonesFound - 2].getSceneObject()
                soBottom = dicClones["FissureStarField"][nbClonesFound - 1].getSceneObject()
                pos = soMaster.getLocalToWorld()
                mrot = ptMatrix44()
                mrot.rotate(0, math.pi)
                mscale = ptMatrix44()
                mscale.makeScaleMat(ptVector3(self._scale, self._scale, self._scale))
                mtransUp = ptMatrix44()
                mtransUp.translate(ptVector3(.0, .0, 30))
                mtransDown = ptMatrix44()
                mtransDown.translate(ptVector3(.0, .0, -30))
                soTop.draw.netForce(1)
                soTop.physics.netForce(1)
                soBottom.draw.netForce(1)
                soBottom.physics.netForce(1)
                soTop.physics.warp(pos * mtransUp * mscale * mrot)
                soBottom.physics.warp(pos * mtransDown * mscale)
                soTop.draw.enable(1)
                soBottom.draw.enable(1)
                SetFog(style = "10000", start = 0, end = 0, density = 0, r = 0.2, g = 0.2, b = 0.4, cr = 0.4, cg = 0.4, cb = 0.5)
                ToggleObjects("Fog", False)
                ToggleObjects("Surface", False)
                ToggleObjects("Sky", False)
                ToggleObjects("CameraClouds", False)
                print ">> Fin."
            else:
                print ">> Le clonage prend trop de temps!!"
            self._nbFois = 0

# Cree une sphere etoilee complete a partir de 2 clones tete-beche de "FissureStarField" agrandis
def CreateNightSky(scale=7.5, bOn=True):
    #global dicClones
    nb = 2
    if bOn:
        # Combien de clones a-t-on deja?
        nbClones = len(dicClones["FissureStarField"])
        print "CreateNightSky : nb de clones de %s ==> %i" % ("FissureStarField", nbClones)
        # Ajouter des clones si besoin
        if nbClones < nb:
            CloneFissureStarField(nb - nbClones)
        # Attendre que les clones soient pret et les manipuler
        PtSetAlarm(1, AlarmWaittingForClones(nb, scale), 1)
        return "nuit"
    else:
        # Retour a la normale
        for i in range(len(dicClones["FissureStarField"])):
            so = dicClones["FissureStarField"][i].getSceneObject()
            so.draw.netForce(1)
            so.draw.enable(0)
        SetFog(style = "defaulf")
        #ToggleObjects("Fog", True)
        #ToggleObject("FogLayerBill", True)
        ToggleObject("FogLayer", True)
        ToggleObjects("Surface", True)
        ToggleObjects("Sky", True)
        ToggleObjects("CameraClouds", True)
        return "jour"

#
def AddRelto(self, args = []):
    self.chatMgr.AddChatLine(None, "Adding Relto...", 3)
    try:
        PtSetAlarm(1, AlarmAddPrp(), 0)
        PtSetAlarm(5, AlarmEnableAll(), 0)
        self.chatMgr.AddChatLine(None, "Relto added!", 3)
        return 1
    except:
        self.chatMgr.AddChatLine(None, "Error while adding Relto.", 3)
        return 0
