# -*- coding: utf-8 -*-
# == Script pour generer un ciel etoile avec l'objet FissureStarField du Relto ==
# Mirphak 2013-12-15 version 3

from Plasma import *
import math
import CloneFactory
import xBotAge
import Objects

#objectName = "FissureStarField"
#ageFileName = "Personal"
#nombre = 2

#
def ToggleObjects(name, bOn=True):
    pf = PtFindSceneobjects(name)
    for so in pf:
        so.netForce(1)
        so.draw.enable(bOn)

#
def ToggleObject(name, age, bOn=True):
    so = PtFindSceneobject(name, age)
    if so is not None:
        so.netForce(1)
        so.draw.enable(bOn)

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
        fd = "Graphics.Renderer.Fog.SetDefLinear %i %i %f" % (start, end, density)
        fc = "Graphics.Renderer.Fog.SetDefColor %f %f %f" % (r, g, b)
        cc = "Graphics.Renderer.SetClearColor %f %f %f" % (cr, cg, cb)
    PtConsoleNet(fy, True)
    PtConsoleNet(fd, True)
    PtConsoleNet(fc, True)
    PtConsoleNet(cc, True)

#=========================================
#
def NightTime(params=[]):
    print "NightTime begin"
    
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
    #TODO: peut-etre mettre des echelles differentes en X, Y ou Z si on cree la nuit dans un autre age que le Relto
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
    
    # Arrangeons le Relto pour profiter de la nuit etoilee
    """
    SetFog(style = "10000", start = 0, end = 0, density = 0, r = 0.2, g = 0.2, b = 0.4, cr = 0.4, cg = 0.4, cb = 0.5)
    ToggleObjects("Fog", False)
    ToggleObjects("Surface", False)
    ToggleObjects("Sky", False)
    ToggleObjects("CameraClouds", False)
    
    #En ville, enlever CityBackDrop et CloudLayer (dans harbor)
    #Pour avoir avoir des etoiles bien visibles mettre du brouillard
    #style Personal et fogshape 0 10000 2
    """
    
    ageFileName = PtGetAgeInfo().getAgeFilename()
    print ">> NightTime: ageFileName = '{}'".format(ageFileName)
    #xBotAge.SetRenderer(style = "Personal")
    xBotAge.SetRenderer(style = "100000", start = 0, end = 0, density = 0, r = 0.2, g = 0.2, b = 0.4, cr = 0.4, cg = 0.4, cb = 0.5)
    for objName in Objects.dicObjectsShowHide[ageFileName]["SingleHide"]:
        print ">> NightTime: ToggleObject({}, {}, False)".format(objName, ageFileName)
        try:
            ToggleObject(objName, ageFileName, False)
        except NameError: 
            print ">> NightTime: SceneObject {} not found in {}".format(objName, ageFileName)
    for objName in Objects.dicObjectsShowHide[ageFileName]["GroupHide"]:
        print ">> NightTime: ToggleObjects({}, False)".format(objName)
        ToggleObjects(objName, False)

    print "NightTime done"
    return 0


#
#dicStyles = {
#    "default":xBotAge.SetRenderer(style = "100000", start = 0, end = 0, density = 0, r = 0.2, g = 0.2, b = 0.4, cr = 0.4, cg = 0.4, cb = 0.5),
#    "crimsom":xBotAge.SetRenderer(style = "100000", start = 0, end = 10000, density = 1., r = .5, g = 0, b = 0, cr = 0.4, cg = 0.4, cb = 0.5),
#    }

#
dicStyles = {
    "default":{"style":"100000", "start":0, "end":0, "density":0, "r":0.2, "g":0.2, "b":0.4, "cr":0.4, "cg":0.4, "cb":0.5},
    "crimsom":{"style":"100000", "start":0, "end":10000, "density":1., "r":.5, "g":0, "b":0, "cr":0.4, "cg":0.4, "cb":0.5},
    "red":{"style":"100000", "start":0, "end":10000, "density":1., "r":.5, "g":0, "b":0, "cr":0.4, "cg":0.4, "cb":0.5},
    "r":{"style":"100000", "start":1000, "end":10000, "density":1., "r":.3, "g":0, "b":0, "cr":0.8, "cg":0.8, "cb":0.8},
    "g":{"style":"100000", "start":1000, "end":10000, "density":1., "r":0, "g":.3, "b":0, "cr":0.8, "cg":0.8, "cb":0.8},
    "b":{"style":"100000", "start":1000, "end":10000, "density":1., "r":0, "g":0, "b":.3, "cr":0.8, "cg":0.8, "cb":0.8},
    }

#
def NightTime2(params=[]):
    print "NightTime2 begin"
    
    #Verifions les parametres
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
    #TODO: peut-etre mettre des echelles differentes en X, Y ou Z si on cree la nuit dans un autre age que le Relto
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
    
    # Arrangeons le Relto pour profiter de la nuit etoilee
    
    ageFileName = PtGetAgeInfo().getAgeFilename()
    print ">> NightTime2: ageFileName = '{}'".format(ageFileName)

    #xBotAge.SetRenderer(style = "100000", start = 0, end = 0, density = 0, r = 0.2, g = 0.2, b = 0.4, cr = 0.4, cg = 0.4, cb = 0.5)
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

    for objName in Objects.dicObjectsShowHide[ageFileName]["SingleHide"]:
        print ">> NightTime: ToggleObject({}, {}, False)".format(objName, ageFileName)
        try:
            ToggleObject(objName, ageFileName, False)
        except NameError: 
            print ">> NightTime: SceneObject {} not found in {}".format(objName, ageFileName)
    for objName in Objects.dicObjectsShowHide[ageFileName]["GroupHide"]:
        print ">> NightTime: ToggleObjects({}, False)".format(objName)
        ToggleObjects(objName, False)

    print "NightTime done"
    return 0

#=========================================
# Pour remettre le Relto dans sont etat d'origine.
def DayTime_v1():
    #SetFog(style = "default")
    xBotAge.SetRenderer(style = "default")
    # objets a remettre en fonction de l'age
    ageFilename = PtGetAgeInfo().getAgeFilename()
    if ageFilename == "Personal":
        #TODO: jouer avec les SDL (page relto des iles) pour savoir laquelle des deux couches de brouillards remettre (FogLayer ou FogLayerBill)
        #ToggleObject("FogLayerBill", True)
        ToggleObject("FogLayer", ageFileName, True)
        #Sol du Relto
        ToggleObjects("Surface", True)
        #Les ciels
        ToggleObjects("Sky", True)
        #Couche de brouillard superieure
        ToggleObjects("CameraClouds", True)
        print ">> DayTime: {} is restored.".format(ageFilename)
    elif ageFilename == "Ahnonay":
        print "{} is restored.".format(ageFilename)
    elif ageFilename == "AhnonayCathedral":
        print "{} is restored.".format(ageFilename)
    elif ageFilename == "BahroCave":
        print "{} is restored.".format(ageFilename)
    elif ageFilename == "BaronCityOffice":
        print "{} is restored.".format(ageFilename)
    elif ageFilename == "city":
        #CityBackDrop et CloudLayer
        ToggleObject("CityBackDrop", ageFileName, True)
        ToggleObject("CloudLayer", ageFileName, True)
        print "{} is restored.".format(ageFilename)
    elif ageFilename == "Cleft":
        print "{} is restored.".format(ageFilename)
    elif ageFilename == "Dereno":
        print "{} is restored.".format(ageFilename)
    elif ageFilename == "Descent":
        print "{} is restored.".format(ageFilename)
    elif ageFilename == "EderDelin":
        print "{} is restored.".format(ageFilename)
    elif ageFilename == "EderTsogal":
        print "{} is restored.".format(ageFilename)
    elif ageFilename == "Ercana":
        print "{} is restored.".format(ageFilename)
    elif ageFilename == "ErcanaCitySilo":
        print "{} is restored.".format(ageFilename)
    elif ageFilename == "Garden":
        print "{} is restored.".format(ageFilename)
    elif ageFilename == "Garrison":
        print "{} is restored.".format(ageFilename)
    elif ageFilename == "Gira":
        print "{} is restored.".format(ageFilename)
    elif ageFilename == "GreatTreePub":
        print "{} is restored.".format(ageFilename)
    elif ageFilename == "GreatZero":
        print "{} is restored.".format(ageFilename)
    elif ageFilename == "GuildPub-Cartographers":
        print "{} is restored.".format(ageFilename)
    elif ageFilename == "GuildPub-Greeters":
        print "{} is restored.".format(ageFilename)
    elif ageFilename == "GuildPub-Maintainers":
        print "{} is restored.".format(ageFilename)
    elif ageFilename == "GuildPub-Messengers":
        print "{} is restored.".format(ageFilename)
    elif ageFilename == "GuildPub-Writers":
        print "{} is restored.".format(ageFilename)
    elif ageFilename == "Jalak":
        print "{} is restored.".format(ageFilename)
    elif ageFilename == "Kadish":
        print "{} is restored.".format(ageFilename)
    elif ageFilename == "Kveer":
        print "{} is restored.".format(ageFilename)
    elif ageFilename == "LiveBahroCaves":
        print "{} is restored.".format(ageFilename)
    elif ageFilename == "Minkata":
        print "{} is restored.".format(ageFilename)
    elif ageFilename == "Myst":
        print "{} is restored.".format(ageFilename)
    elif ageFilename == "Negilahn":
        print "{} is restored.".format(ageFilename)
    elif ageFilename == "Neighborhood":
        print "{} is restored.".format(ageFilename)
    elif ageFilename == "Neighborhood02":
        print "{} is restored.".format(ageFilename)
    elif ageFilename == "Payiferen":
        print "{} is restored.".format(ageFilename)
    elif ageFilename == "PelletBahroCave":
        print "{} is restored.".format(ageFilename)
    elif ageFilename == "philRelto":
        print "{} is restored.".format(ageFilename)
    elif ageFilename == "spyroom":
        print "{} is restored.".format(ageFilename)
    elif ageFilename == "Teledahn":
        print "{} is restored.".format(ageFilename)
    elif ageFilename == "Tetsonot":
        print "{} is restored.".format(ageFilename)
    else:
        print "Unknown age"
    return 0

# Pour remettre le Relto dans sont etat d'origine.
def DayTime():
    #SetFog(style = "default")
    xBotAge.SetRenderer(style = "default")
    # objets a remettre en fonction de l'age
    ageFileName = PtGetAgeInfo().getAgeFilename()
    #for objName in Objects.dicObjectsShowHide[ageFilename]["SingleShow"]:
    #    ToggleObject(objName, ageFileName, True)
    #for objName in Objects.dicObjectsShowHide[ageFilename]["GroupShow"]:
    #    ToggleObjects(objName, True)
    for objName in Objects.dicObjectsShowHide[ageFileName]["SingleShow"]:
        print ">> DayTime: ToggleObject({}, {}, True)".format(objName, ageFileName)
        try:
            ToggleObject(objName, ageFileName, True)
        except NameError: 
            print ">> DayTime: SceneObject {} not found in {}".format(objName, ageFileName)
    for objName in Objects.dicObjectsShowHide[ageFileName]["GroupShow"]:
        print ">> DayTime: ToggleObjects({}, True)".format(objName)
        ToggleObjects(objName, True)

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
        return "Nuit"
    else:
        # Retour a la normale
        CloneFactory.DechargerClones(masterKey)
        DayTime()
        return "Jour"


# Cree une sphere etoilee complete a partir de 2 clones tete-beche de "FissureStarField" agrandis
# Avec changement de fog et/ou clear
def CreateNightSky2(scale=400, bOn=True, style="default"):
    objectName = "FissureStarField"
    ageFileName = "Personal"
    nombre = 2
    masterKey = PtFindSceneobject(objectName, ageFileName).getKey()
    if bOn:
        # Changeons le fond ciel et le brouillard ici
        #if style in dicStyles:
        #    dicStyles[style]()
        #else:
        #    dicStyles["default"]()
        
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
