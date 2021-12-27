# -*- coding: utf-8 -*-
# == Commandes specifiques de clonage d'objets ==
from Plasma import *
import math

age = "Personal"
pages = ["pnslMYSTII"]

bPagesAdded = False

bAlreadyScaled = False

bFog = True
bSkyHigh = True
bSkyHighStormy = False
phase = 0

# Dictionnaire des clones
dicClones = {}
#dicClones.update({"FissureStarField":[]})
#dicClones.update({"Personal":{"FissureStarField":[]}})


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
class AlarmCloneObject:
    _objectName = ""
    _ageFileName = ""
    _masterKey = None
    _nombre = 1
    _delais = 1
    _maxAttempts = 5
    _attempts = 1

    # Initialisation
    def __init__(self, objectName, ageFileName, nombre):
        self._objectName = objectName
        self._ageFileName = ageFileName
        self._masterKey = PtFindSceneobject(objectName, ageFileName).getKey()
        self._nombre = nombre
        self._delais = 1
        self._attempts = 1
        print "init AlarmCloneObject(%i)" % self._nombre

    # Clonage general (n clones)
    #def Cloner(self, nombre):
    #    for i in range(nombre):
    #        PtCloneKey(self._masterKey)

    # Prenons notre temps...
    def onAlarm(self, param):
        # Verifions d'abord si l'objet maitre a ete trouve (que c'est un ptKey)
        if isinstance(self._masterKey, ptKey):
            if param == 0:
                # partie 0 : dechargeons d'abord les clones s'il y en a
                cloneKeys = PtFindClones(self._masterKey)
                for ck in cloneKeys:
                    PtCloneKey(ck, 0)
                PtSetAlarm(self._delais, self, 1)
            elif param == 1:
                # partie 1 : clonage
                print "clonage en cours..."
                # Existe-t-il deja des clones?
                n = len(PtFindClones(self._masterKey))
                if n < self._nombre:
                    # Il nous en faut (self._nombre - n) en plus
                    #self.Cloner(self._nombre - n)
                    for i in range(self._nombre - n):
                        PtCloneKey(self._masterKey)
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
                    PtSetAlarm(self._delais, self, 3)
            elif param == 3:
                # partie 3 : rechargeons les clones crees
                cloneKeys = PtFindClones(self._masterKey)
                for ck in cloneKeys:
                    PtCloneKey(ck, 1)
            else:
                print "AlarmCloneObject.onAlarm : param incorrect"
        else:
            print "self._masterKey is not a ptKey (object not found)"

    # Sauvons les clones!
    def saveClones(self):
        global dicClones
        #dicClones["FissureStarField"] = PtFindClones(self._masterKey
        if not dicClone.has_key(self._ageFileName):
            dicClones.update({self._ageFileName:{}})
        if not dicClone[self._ageFileName].has_key(self._objectName):
            dicClones[self._ageFileName].update({self._objectName:[]})
        dicClones[self._ageFileName][self._objectName] = PtFindClones(self._masterKey)
        print "nb clones: " + str(len(dicClones[self._ageFileName][self._objectName]))

#=========================================
# Exemple : clonage du FissureStarField
def CloneFissureStarField(nombre):
    #objectName, ageFileName, nombre
    print "CloneFissureStarField()"
    #PtSetAlarm(1, AlarmCloneObject(nombre), 1)
    PtSetAlarm(1, AlarmCloneObject("FissureStarField", "Personal", nombre), 0)

#
class AlarmWaittingForClones:
    _nbFois = 0
    _nbClones = 0
    _scale = 1
    #_masterName = "FissureStarField"
    
    def __init__(self, nombre, scale):
        self._nbClones = nombre
        self._scale = scale
        self._objectName = "FissureStarField"
        self._ageFileName = "Personal"
        self._masterKey = PtFindSceneobject(self._objectName, self._ageFileName).getKey()
    
    def onAlarm(self, param):
        print "> AlarmWaitting.onAlarm"
        if param == 1:
            #nbClonesFound = len(dicClones["FissureStarField"])
            #if !dicClone.has_key(self._ageFileName):
            #    dicClones.update({self._ageFileName:{}})
            #if !dicClone[self._ageFileName].has_key(self._objectName):
            #    dicClones[self._ageFileName].update({self._objectName:[]})
            #nbClonesSaved = len(dicClones["Personal"]["FissureStarField"])
            nbClonesFound = len(PtFindClones(self._masterKey))
            print ">> nb de clones de %s %i" % ("FissureStarField", nbClonesFound)
            # Attendre que tous les clones soient crees, mais pas indefiniment au cas ou
            if (nbClonesFound < self._nbClones and self._nbFois < 20):
                self._nbFois += 1
                print ">>> Attente nb: %i" % self._nbFois
                PtSetAlarm(1, self, 1)
            else:
                PtSetAlarm(1, self, 2)
        elif param == 2:
            #nbClonesFound = len(dicClones["FissureStarField"])
            cloneKeys = PtFindClones(self._masterKey)
            nbClonesFound = len(cloneKeys)
            #print ">> nb de clones de %s %i" % ("FissureStarField", nbClonesFound)
            print ">> nb de clones de {} {}".format(self._objectName, nbClonesFound)
            if (self._nbFois < 20):
                print ">> Les clones sont prets."
                soMaster = PtFindSceneobject(self._objectName, self._ageFileName)
                ## Masquons les clones surnumeraires s'il y en a
                #for i in range(0, nbClonesFound - 2):
                #    so = dicClones["FissureStarField"][i].getSceneObject()
                #    so.draw.netForce(1)
                #    so.draw.enable(0)
                
                # Manipulons les clones
                #soTop = dicClones["FissureStarField"][nbClonesFound - 2].getSceneObject()
                #soBottom = dicClones["FissureStarField"][nbClonesFound - 1].getSceneObject()
                soTop = cloneKeys[0].getSceneObject()
                soBottom = cloneKeys[1].getSceneObject()
                pos = soMaster.getLocalToWorld()
                mrot = ptMatrix44()
                mrot.rotate(0, math.pi)
                mscale = ptMatrix44()
                mscale.makeScaleMat(ptVector3(self._scale, self._scale, self._scale))
                mtransUp = ptMatrix44()
                mtransUp.translate(ptVector3(.0, .0, 32))
                mtransDown = ptMatrix44()
                mtransDown.translate(ptVector3(.0, .0, -32))
                soTop.netForce(1)
                soBottom.netForce(1)
                soTop.physics.warp(pos * mtransUp * mscale * mrot)
                soBottom.physics.warp(pos * mtransDown * mscale)
                soTop.draw.enable(1)
                soBottom.draw.enable(1)
                SetFog(style = "10000", start = 0, end = 0, density = 0, r = 0.2, g = 0.2, b = 0.4, cr = 0.4, cg = 0.4, cb = 0.5)
                ToggleObjects("Fog", False)
                ToggleObjects("Surface", False)
                ToggleObjects("Sky", False)
                ToggleObjects("CameraClouds", False)
                #Attendre un peu avant de recharger les clones
                PtSetAlarm(1, self, 3)
            elif param == 3:
                #Si on n'a pas cree de nouveaux clones et qu'on les a decharges, il faut les recharger
                #Mais il faut que je lance la commande deux fois, pourquoi?
                #Test en temporisant
                RechargerClones(self._masterKey)
                print ">> Fin."
            else:
                print ">> Le clonage prend trop de temps!!"
            self._nbFois = 0

# Cree une sphere etoilee complete a partir de 2 clones tete-beche de "FissureStarField" agrandis
def CreateNightSky(scale=7.5, bOn=True):
    #global dicClones
    nb = 2
    masterKey = PtFindSceneobject("FissureStarField", "Personal").getKey()
    if bOn:
        # Combien de clones a-t-on deja?
        #nbClones = len(dicClones["FissureStarField"])
        nbClones = len(PtFindClones(masterKey))
        print "CreateNightSky : nb de clones de %s ==> %i" % ("FissureStarField", nbClones)
        # Ajouter des clones si besoin
        if nbClones < nb:
            CloneFissureStarField(nb - nbClones)
        # Attendre que les clones soient prets et les manipuler
        PtSetAlarm(1, AlarmWaittingForClones(nb, scale), 1)
        return "nuit"
    else:
        # Retour a la normale
        #for i in range(len(dicClones["FissureStarField"])):
        #    so = dicClones["FissureStarField"][i].getSceneObject()
        #    so.draw.netForce(1)
        #    so.draw.enable(0)
        DechargerClones(masterKey)
        SetFog(style = "defaulf")
        #ToggleObjects("Fog", True)
        #ToggleObject("FogLayerBill", True)
        ToggleObject("FogLayer", True)
        ToggleObjects("Surface", True)
        ToggleObjects("Sky", True)
        ToggleObjects("CameraClouds", True)
        return "jour"

#=========================================
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

#=========================================
# Test : clonage d'un object (nom de l'objet, nom fichier age et nombre de clones en parametre)
def CloneObject(objectName, ageFileName, nombre):
    print "CloneObject({}, {}, {})".format(objectName, ageFileName, nombre)
    PtSetAlarm(1, AlarmCloneObject(objectName, ageFileName, nombre), 0)

#methode par defaut de manipulation d'objet
def DoNothing(params=[]):
    print "DoNothing()"
#
class AlarmWaittingForClones_v2:
    _nbFois = 0
    _nbClones = 0
    #_method = DoNothing
    #_masterName = "FissureStarField"
    
    def __init__(self, objectName="BeachBall", ageFileName="Neighborhood", nombre=1, method=DoNothing, params=[]):
        self._objectName = objectName
        self._ageFileName = ageFileName
        self._nbClones = nombre
        self._method = method
        self._params = params
        self._masterKey = PtFindSceneobject(self._objectName, self._ageFileName).getKey()
    
    def onAlarm(self, param):
        print "> AlarmWaitting.onAlarm"
        if param == 1:
            nbClonesFound = len(PtFindClones(self._masterKey))
            print ">> nb de clones de %s %i" % (self._objectName, nbClonesFound)
            # Attendre que tous les clones soient crees, mais pas indefiniment au cas ou
            if (nbClonesFound < self._nbClones and self._nbFois < 20):
                self._nbFois += 1
                print ">>> Attente nb: %i" % self._nbFois
                PtSetAlarm(1, self, 1)
            else:
                PtSetAlarm(1, self, 2)
        elif param == 2:
            cloneKeys = PtFindClones(self._masterKey)
            nbClonesFound = len(cloneKeys)
            print ">> nb de clones de {} {}".format(self._objectName, nbClonesFound)
            if (self._nbFois < 20):
                print ">> Les clones sont prets."
                soMaster = PtFindSceneobject(self._objectName, self._ageFileName)
                # Manipulons les clones
                self._method(self._params)
                #Attendre un peu avant de recharger les clones
                PtSetAlarm(1, self, 3)
            elif param == 3:
                RechargerClones(self._masterKey)
                print ">> Fin."
            else:
                print ">> Le clonage prend trop de temps!!"
            self._nbFois = 0

# Faire quelque chose avec des clones
def Test(objectName="BeachBall", ageFileName="Neighborhood", nb=2, bOn=True):
    masterKey = PtFindSceneobject(objectName, ageFileName).getKey()
    if bOn:
        # Combien de clones a-t-on deja?
        nbClones = len(PtFindClones(masterKey))
        print "Test : nb de clones de {} ==> {}".format(objectName, nbClones)
        # Ajouter des clones si besoin
        if nbClones < nb:
            CloneObject(objectName, ageFileName, nb - nbClones)
        # Attendre que les clones soient prets et les manipuler
        PtSetAlarm(1, AlarmWaittingForClones_v2(objectName, ageFileName, nb, DoNothing, []), 1)
        return "Test on"
    else:
        # Retour a la normale
        DechargerClones(masterKey)
        # Undo something
        #...
        return "Test off"

#