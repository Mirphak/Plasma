# -*- coding: utf-8 -*-
# == Commandes specifiques de clonage d'objets ==
from Plasma import *


def ToggleObjects(name, bOn = True):
    pf = PtFindSceneobjects(name)
    for so in pf:
        so.netForce(1)
        so.draw.enable(bOn)

def ToggleObject(name, age, bOn = True):
    so = PtFindSceneobject(name, age)
    if so is not None:
        so.netForce(1)
        so.draw.enable(bOn)


def ToggleDrawClone(cloneKey, bOn = True):
    so = cloneKey.getSceneObject()
    if so is not None:
        so.netForce(1)
        so.draw.enable(bOn)

def ToggleDrawClones(masterKey, bOn = True):
    cloneKeys = PtFindClones(masterKey)
    for ck in cloneKeys:
        so = ck.getSceneObject()
        if so is not None:
            so.netForce(1)
            so.draw.enable(bOn)



# Unload all the clones
def DechargerClones(masterKey):
    print ">> DechargerClones() <<"
    cloneKeys = PtFindClones(masterKey)
    for ck in cloneKeys:
        PtCloneKey(ck, 0)

# Reload all the clones
def RechargerClones(masterKey):
    print ">> RechargerClones() <<"
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
                    for i in range(self._nombre - n):
                        PtCloneKey(self._masterKey)
                PtSetAlarm(self._delais, self, 2)
            elif param == 2:
                # partie 2 : attendre que tous les clones soient crees
                n = len(PtFindClones(self._masterKey))
                if n < self._nombre:
                    print "%i clones trouves sur les %i demandes! (attempt #%i)" % (n, self._nombre, self._attempts)
                    if self._attempts < self._maxAttempts:
                        self._attempts = self._attempts + 1
                        PtSetAlarm(self._delais, self, 2)
                    else:
                        print "Le clonage met trop de temps!!"
                else:
                    #attendre avant de recharger les clones
                    PtSetAlarm(self._delais, self, 3)
            elif param == 3:
                # partie 3 : rechargeons les clones crees
                cloneKeys = PtFindClones(self._masterKey)
                print "rechargement des {} clones...".format(len(cloneKeys))
                for ck in cloneKeys:
                    PtCloneKey(ck, 1)
            else:
                print "AlarmCloneObject.onAlarm : param incorrect"
        else:
            print "self._masterKey is not a ptKey (object not found)"

#=========================================
#
#=========================================
# Clonage d'un object (nom de l'objet, nom fichier age et nombre de clones en parametre)
def CloneObject(objectName, ageFileName, nombre):
    print "CloneObject({}, {}, {})".format(objectName, ageFileName, nombre)
    PtSetAlarm(1, AlarmCloneObject(objectName, ageFileName, nombre), 0)

#methode par defaut de manipulation d'objet
def DoNothing(params=[]):
    print "DoNothing()"

# Test : montrer les clones
def ShowClones(params=[]):
    print "ShowClones()"
    if len(params) > 1:
        bOn = params[1]
    else:
        bOn = True
    if len(params) > 0:
        masterKey = params[0]
        if not isinstance(masterKey, ptKey):
            print "ShowClones: first paremeter must be a ptKey"
            return 0
    if len(params) == 0:
        print "ShowClones: needs 1 or 2 paremeters"
        return 0
    ToggleDrawClones(masterKey, bOn)

#
class AlarmWaittingForClones:
    _nbFois = 0
    _nbClones = 0
    
    def __init__(self, objectName="BeachBall", ageFileName="Neighborhood", nombre=1, method=DoNothing, params=[]):
        self._objectName = objectName
        self._ageFileName = ageFileName
        self._nbClones = nombre
        self._method = method
        self._params = params
        self._masterKey = PtFindSceneobject(self._objectName, self._ageFileName).getKey()
    
    def onAlarm(self, param):
        print "> AlarmWaittingForClones.onAlarm({})".format(param)
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
                #soMaster = PtFindSceneobject(self._objectName, self._ageFileName)
                # Manipulons les clones
                self._method(self._params)
                #Attendre un peu avant de recharger les clones
                print ">> Attente avant recharge clones."
                PtSetAlarm(1, self, 3)
            self._nbFois = 0
        elif param == 3:
            print ">> recharge des clones."
            RechargerClones(self._masterKey)
            print ">> Fin."
        else:
            print ">> Le clonage prend trop de temps!!"

# Faire quelque chose avec des clones
def Test(objectName="BeachBall", ageFileName="Neighborhood", nb=1, bOn=True):
    masterKey = PtFindSceneobject(objectName, ageFileName).getKey()
    if bOn:
        # Combien de clones a-t-on deja?
        nbClones = len(PtFindClones(masterKey))
        print "Test : nb de clones de {} ==> {}".format(objectName, nbClones)
        # Ajouter des clones si besoin
        if nbClones < nb:
            CloneObject(objectName, ageFileName, nb - nbClones)
        # Attendre que les clones soient prets et les manipuler
        PtSetAlarm(1, AlarmWaittingForClones(objectName, ageFileName, nb, DoNothing, []), 1)
        return "Test on"
    else:
        # Retour a la normale
        DechargerClones(masterKey)
        # Undo something
        #...
        return "Test off"

# Faire quelque chose avec des clones
def Test2(objectName="BeachBall", ageFileName="Neighborhood", nb=1, bOn=True):
    masterKey = PtFindSceneobject(objectName, ageFileName).getKey()
    if bOn:
        # Combien de clones a-t-on deja?
        nbClones = len(PtFindClones(masterKey))
        print "Test : nb de clones de {} ==> {}".format(objectName, nbClones)
        # Ajouter des clones si besoin
        if nbClones < nb:
            CloneObject(objectName, ageFileName, nb - nbClones)
        # Attendre que les clones soient prets et les manipuler
        PtSetAlarm(1, AlarmWaittingForClones(objectName, ageFileName, nb, ShowClones, [masterKey]), 1)
        return "Test on"
    else:
        # Retour a la normale
        DechargerClones(masterKey)
        # Undo something
        #...
        return "Test off"

#