# -*- coding: utf-8 -*-
# == Script pour generer un ciel etoile avec l'objet FissureStarField du Relto ==
# Mirphak 2014-02-22 version 4

from Plasma import *
import math
import CloneFactory
import xBotAge
import Objects2
import Fog
import Rotation

#init autoRotationTop and autoRotationBottom
autoRotationTop = None
autoRotationBottom = None

#=========================================
# Methodes de base 

# Montrer ou cacher des groupes d'objets
def ToggleObjects(name, bOn=True):
    pf = PtFindSceneobjects(name)
    for so in pf:
        so.netForce(1)
        so.draw.enable(bOn)

# Montrer ou cacher un objet
def ToggleObject(name, age, bOn=True):
    so = PtFindSceneobject(name, age)
    if so is not None:
        so.netForce(1)
        so.draw.enable(bOn)


#=========================================
#
def NightTime(params=[]):
    print "NightTime begin"
    global autoRotationTop
    global autoRotationBottom
    
    #Verifions les parametres
    if len(params) > 1:
        scale = params[1]
    else:
        scale = 7.5
    if len(params) > 0:
        masterKey = params[0]
        if not isinstance(masterKey, ptKey):
            print "NightTime: first paremeter must be a ptKey"
            return 1
    if len(params) == 0:
        print "NightTime: needs 1 or 2 paremeters"
        return 1
    
    print "NightTime params ok"
    soMaster = masterKey.getSceneObject()
    print "NightTime({}, {})".format(soMaster.getName(), scale)
    
    # Manipulons les clones
    cloneKeys = PtFindClones(masterKey)
    soTop = cloneKeys[0].getSceneObject()
    soBottom = cloneKeys[1].getSceneObject()
    pos = soMaster.getLocalToWorld()
    mrot = ptMatrix44()
    mrot.rotate(0, math.pi)
    mscale = ptMatrix44()

    mscale.makeScaleMat(ptVector3(scale, scale, scale))
    mtransUp = ptMatrix44()
    #TODO: ajouter eventuellement des decalages en X et/ou Y si on cree la nuit dans un autre age que le Relto
    mtransUp.translate(ptVector3(.0, .0, 64*scale/15))
    mtransDown = ptMatrix44()
    mtransDown.translate(ptVector3(.0, .0, -64*scale/15))
    soTop.netForce(1)
    soBottom.netForce(1)
    soTop.physics.warp(pos * mtransUp * mscale * mrot)
    soBottom.physics.warp(pos * mtransDown * mscale)
    soTop.draw.enable(1)
    soBottom.draw.enable(1)
    
    # Arrangeons l'age pour profiter de la nuit etoilee
    ageFileName = PtGetAgeInfo().getAgeFilename()
    print ">> NightTime: ageFileName = '{}'".format(ageFileName)
    # le style de rendu
    xBotAge.SetRenderer(style = "100000", start = 0, end = 0, density = 0, r = 0.2, g = 0.2, b = 0.4, cr = 0.4, cg = 0.4, cb = 0.5)
    # les objets a cacher
    for objName in Objects2.dicObjectsShowHide[ageFileName]["SingleHide"]["Night"]:
        print ">> NightTime: ToggleObject({}, {}, False)".format(objName, ageFileName)
        try:
            ToggleObject(objName, ageFileName, False)
        except NameError: 
            print ">> NightTime: SceneObject {} not found in {}".format(objName, ageFileName)
    for objName in Objects2.dicObjectsShowHide[ageFileName]["GroupHide"]["Night"]:
        print ">> NightTime: ToggleObjects({}, False)".format(objName)
        ToggleObjects(objName, False)
    # les objets a montrer
    for objName in Objects2.dicObjectsShowHide[ageFileName]["SingleShow"]["Night"]:
        print ">> NightTime: ToggleObject({}, {}, True)".format(objName, ageFileName)
        try:
            ToggleObject(objName, ageFileName, True)
        except NameError: 
            print ">> NightTime: SceneObject {} not found in {}".format(objName, ageFileName)
    for objName in Objects2.dicObjectsShowHide[ageFileName]["GroupShow"]["Night"]:
        print ">> NightTime: ToggleObjects({}, True)".format(objName)
        ToggleObjects(objName, True)

    # Ajoutons le fog a couleur changeante
    #Fog.Start()
    Fog.Start(delay=2., start=None, end=None, density=None)
    
    # rotation du ciel
    posTop = soTop.getLocalToWorld()
    posBottom = soBottom.getLocalToWorld()
    m = ptMatrix44()
    # rotation de 45 degres en x
    m.rotate(0, (math.pi * float(45)) / 180)
    soTop.netForce(1)
    soBottom.netForce(1)
    soTop.physics.warp(posTop * m)
    soBottom.physics.warp(posBottom * m)
    #init autoRotationTop and autoRotationBottom
    if autoRotationTop is None:
        print "autoRotationTop is None"
        autoRotationTop = Rotation.AutoRotation(delay=1., so=soTop, stepZ=.05)
        #autoRotationTop = Rotation.AutoRotation(delay=4., so=soTop, stepZ=.4)
    if autoRotationBottom is None:
        print "autoRotationBottom is None"
        autoRotationBottom = Rotation.AutoRotation(delay=1., so=soBottom, stepZ=-.05)
        #autoRotationBottom = Rotation.AutoRotation(delay=4., so=soBottom, stepZ=-.4)
    # start rotations
    if autoRotationTop is not None:
        print "start rot top"
        autoRotationTop.Start()
    if autoRotationBottom is not None:
        print "start rot bottom"
        autoRotationBottom.Start()
    
    print "NightTime done"
    return 0

#=========================================
# dictionnaire de styles de rendus
dicStyles = {
    "default":{"style":"100000", "start":0, "end":0, "density":0, "r":0.2, "g":0.2, "b":0.4, "cr":0.4, "cg":0.4, "cb":0.5},
    "crimson":{"style":"100000", "start":0, "end":10000, "density":1., "r":.5, "g":0, "b":0, "cr":0.4, "cg":0.4, "cb":0.5},
    "red":{"style":"100000", "start":0, "end":10000, "density":1., "r":.5, "g":0, "b":0, "cr":0.4, "cg":0.4, "cb":0.5},
    }

#
def NightTime2(params=[]):
    print "NightTime2 begin"
    
    #Verifions les parametres
    #if len(params) > 3:
    #    duration = params[3]
    #else:
    #    duration = 30
    if len(params) > 2:
        style = params[2]
    else:
        style = "default"
    if len(params) > 1:
        scale = params[1]
    else:
        scale = 7.5
    if len(params) > 0:
        masterKey = params[0]
        if not isinstance(masterKey, ptKey):
            print "NightTime2: first paremeter must be a ptKey"
            return 1
    if len(params) == 0:
        print "NightTime2: needs 1 or 2 paremeters"
        return 1
    
    print "NightTime2 params ok"
    soMaster = masterKey.getSceneObject()
    print "NightTime2({}, {}, {})".format(soMaster.getName(), scale, style)
    
    # Manipulons les clones
    cloneKeys = PtFindClones(masterKey)
    soTop = cloneKeys[0].getSceneObject()
    soBottom = cloneKeys[1].getSceneObject()
    pos = soMaster.getLocalToWorld()
    mrot = ptMatrix44()
    mrot.rotate(0, math.pi)
    mscale = ptMatrix44()

    mscale.makeScaleMat(ptVector3(scale, scale, scale))
    mtransUp = ptMatrix44()
    #TODO: ajouter eventuellement des decalages en X et/ou Y si on cree la nuit dans un autre age que le Relto
    mtransUp.translate(ptVector3(.0, .0, 64*scale/15))
    mtransDown = ptMatrix44()
    mtransDown.translate(ptVector3(.0, .0, -64*scale/15))
    soTop.netForce(1)
    soBottom.netForce(1)
    soTop.physics.warp(pos * mtransUp * mscale * mrot)
    soBottom.physics.warp(pos * mtransDown * mscale)
    soTop.draw.enable(1)
    soBottom.draw.enable(1)
    
    # Arrangeons l'age pour profiter de la nuit etoilee
    ageFileName = PtGetAgeInfo().getAgeFilename()
    print ">> NightTime2: ageFileName = '{}'".format(ageFileName)

    # Changeons le fond ciel et le brouillard ici
    print ">> NightTime2: style=\"{}\"".format(style)
    dicParamsStyle = {"style":"100000", "start":0, "end":0, "density":0, "r":0.2, "g":0.2, "b":0.4, "cr":0.4, "cg":0.4, "cb":0.5}
    if style in dicStyles:
        dicParamsStyle = dicStyles[style]
    #else:
    #    dicParamsStyle = dicStyles["default"]
    xBotAge.SetRenderer(
        style   = dicParamsStyle["style"],
        start   = dicParamsStyle["start"],
        end     = dicParamsStyle["end"],
        density = dicParamsStyle["density"],
        r       = dicParamsStyle["r"],
        g       = dicParamsStyle["g"],
        b       = dicParamsStyle["b"],
        cr      = dicParamsStyle["cr"],
        cg      = dicParamsStyle["cg"],
        cb      = dicParamsStyle["cb"]
        )

    # les objets a cacher
    for objName in Objects2.dicObjectsShowHide[ageFileName]["SingleHide"]["Night"]:
        print ">> NightTime2: ToggleObject({}, {}, False)".format(objName, ageFileName)
        try:
            ToggleObject(objName, ageFileName, False)
        except NameError: 
            print ">> NightTime2: SceneObject {} not found in {}".format(objName, ageFileName)
    for objName in Objects2.dicObjectsShowHide[ageFileName]["GroupHide"]["Night"]:
        print ">> NightTime2: ToggleObjects({}, False)".format(objName)
        ToggleObjects(objName, False)
    # les objets a montrer
    for objName in Objects2.dicObjectsShowHide[ageFileName]["SingleShow"]["Night"]:
        print ">> NightTime2: ToggleObject({}, {}, True)".format(objName, ageFileName)
        try:
            ToggleObject(objName, ageFileName, True)
        except NameError: 
            print ">> NightTime2: SceneObject {} not found in {}".format(objName, ageFileName)
    for objName in Objects2.dicObjectsShowHide[ageFileName]["GroupShow"]["Night"]:
        print ">> NightTime2: ToggleObjects({}, True)".format(objName)
        ToggleObjects(objName, True)

    print "NightTime2 done"
    #PtSetAlarm(duration, AlarmDayTime(masterKey), 1)
    return 0

#=========================================
# Pour remettre le Relto dans sont etat d'origine.
#def DayTime():
def DayTime(masterKey):
    # arretons le fog a couleur changeante
    Fog.Stop()
    # arretons les rotations
    if autoRotationTop is not None:
        print "stop rot top"
        autoRotationTop.Stop()
    if autoRotationBottom is not None:
        print "stop rot bottom"
        autoRotationBottom.Stop()

    CloneFactory.DechargerClones(masterKey)
    
    # rendu normal de l'age
    xBotAge.SetRenderer(style = "default")
    # objets a remettre en fonction de l'age
    ageFileName = PtGetAgeInfo().getAgeFilename()

    # les objets a cacher
    for objName in Objects2.dicObjectsShowHide[ageFileName]["SingleShow"]["Day"]:
        print ">> DayTime: ToggleObject({}, {}, True)".format(objName, ageFileName)
        try:
            ToggleObject(objName, ageFileName, True)
        except NameError: 
            print ">> DayTime: SceneObject {} not found in {}".format(objName, ageFileName)
    for objName in Objects2.dicObjectsShowHide[ageFileName]["GroupShow"]["Day"]:
        print ">> DayTime: ToggleObjects({}, True)".format(objName)
        ToggleObjects(objName, True)
    # les objets a montrer
    for objName in Objects2.dicObjectsShowHide[ageFileName]["SingleHide"]["Day"]:
        print ">> DayTime: ToggleObject({}, {}, False)".format(objName, ageFileName)
        try:
            ToggleObject(objName, ageFileName, False)
        except NameError: 
            print ">> DayTime: SceneObject {} not found in {}".format(objName, ageFileName)
    for objName in Objects2.dicObjectsShowHide[ageFileName]["GroupHide"]["Day"]:
        print ">> DayTime: ToggleObjects({}, False)".format(objName)
        ToggleObjects(objName, False)

#
class AlarmDayTime:
    _masterKey = None
    def __init__(self, masterKey=None):
        print "> AlarmDayTime.__init__({})".format(masterKey)
        self._masterKey = masterKey
    
    def onAlarm(self, param):
        print "> AlarmDayTime.onAlarm({})".format(param)
        if param == 0:
            if len(PtGetPlayerList()) == 0:
                try:
                    DayTime(self._masterKey)
                except:
                    print "> Error in AlarmDayTime.onAlarm (0)"
            else:
                #PtSetAlarm(300, self(self._masterKey), 1)
                PtSetAlarm(300, self, 1)
        else:
            try:
                DayTime(self._masterKey)
            except:
                print "> Error in AlarmDayTime.onAlarm (1)"

#=========================================
### myCurrentAgeInstanceGuid = None

#=========================================
# Cree une sphere etoilee complete a partir de 2 clones tete-beche de "FissureStarField" agrandis
def CreateNightSky(scale=7.5, bOn=True):
    objectName = "FissureStarField"
    ageFileName = "Personal"
    nombre = 2
    masterKey = PtFindSceneobject(objectName, ageFileName).getKey()
    if bOn:
        # Combien de clones a-t-on deja?
        nbClones = len(PtFindClones(masterKey))
        print "Test : nb de clones de {} ==> {}".format(objectName, nbClones)
        # Ajouter des clones si besoin
        if nbClones < nombre:
            CloneFactory.CloneObject(objectName, ageFileName, nombre - nbClones)
        # Attendre que les clones soient prets et les manipuler
        PtSetAlarm(1, CloneFactory.AlarmWaittingForClones(objectName, ageFileName, nombre, NightTime, [masterKey, scale]), 1)
        # Arreter le tout apres 5 minutes
        PtSetAlarm(300, AlarmDayTime(masterKey), 0)
        return "Nuit"
    else:
        ## A - Retour a la normale V1
        #CloneFactory.DechargerClones(masterKey)
        #DayTime()
        #DayTime(masterKey)
        
        ## B - Arret des changements sans retour au jour
        ## 1 - arretons le fog a couleur changeante
        #Fog.Stop()
        ## 2 - arretons les rotations
        #if autoRotationTop is not None:
        #    print "stop rot top"
        #    autoRotationTop.Stop()
        #if autoRotationBottom is not None:
        #    print "stop rot bottom"
        #    autoRotationBottom.Stop()
        
        # C - Retour a la normale V2 (arret immediat et retour jour)
        PtSetAlarm(0, AlarmDayTime(masterKey), 1)
        
        return "Jour"


# Cree une sphere etoilee complete a partir de 2 clones tete-beche de "FissureStarField" agrandis
# Avec changement de fog et/ou clear
def CreateNightSky2(scale=400, bOn=True, style="default"):
    objectName = "FissureStarField"
    ageFileName = "Personal"
    nombre = 2
    masterKey = PtFindSceneobject(objectName, ageFileName).getKey()
    if bOn:
        # Combien de clones a-t-on deja?
        nbClones = len(PtFindClones(masterKey))
        print "Test : nb de clones de {} ==> {}".format(objectName, nbClones)
        # Ajouter des clones si besoin
        if nbClones < nombre:
            CloneFactory.CloneObject(objectName, ageFileName, nombre - nbClones)
        # Attendre que les clones soient prets et les manipuler
        PtSetAlarm(1, CloneFactory.AlarmWaittingForClones(objectName, ageFileName, nombre, NightTime2, [masterKey, scale, style]), 1)
        return "Nuit"
    else:
        # Retour a la normale
        CloneFactory.DechargerClones(masterKey)
        DayTime()
        return "Jour"

# == FIN ==
