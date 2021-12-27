# -*- coding: utf-8 -*-
# == Script pour generer un clone d'objet au choix ==
# Mirphak 2013-12-15 version 3

from Plasma import *
import math
import CloneFactory

# Default
#objectName = "FissureStarField"
#ageFileName = "Personal"
objectName = "SmokeEmitter02"
ageFileName = "city"
nombre = 1

#Liste d'objets interessants
lstAgeObj = [
    ["Minkata", "SoccerBall"],
    ["Personal", "BlueFiremarble04"],
    ["Personal", "BlueMarble08"],
    ["Personal", "MarblePhys06"],
    ["Personal", "MarblePhys07"],
    ["Personal", "MarblePhys08"],
    ["Personal", "MarblePhys09"],
    ["Personal", "MarblePhys10"],
    ["Personal", "RedFiremarble05"],
    ["Personal", "RedMarble09"],
    ["Personal", "WhiteFiremarble02"],
    ["Personal", "WhiteFiremarble03"],
    ["Personal", "WhiteMarble06"],
    ["Personal", "WhiteMarble07"],
    ["Personal", "YellowFiremarble06"],
    ["Personal", "YellowMarble10"],
    ["Personal", "Yeesh16firemarbles"],
    ["Neighborhood", "BlueFiremarble"],
    ["Neighborhood", "BlueMarble"],
    ["Neighborhood", "MarblePhys01"],
    ["Neighborhood", "MarblePhys02"],
    ["Neighborhood", "MarblePhys03"],
    ["Neighborhood", "MarblePhys04"],
    ["Neighborhood", "MarblePhys06"],
    ["Neighborhood", "MarblePhys07"],
    ["Neighborhood", "MarblePhys08"],
    ["Neighborhood", "RedFiremarble"],
    ["Neighborhood", "RedMarble"],
    ["Neighborhood", "WhiteFiremarble"],
    ["Neighborhood", "WhiteFiremarble02"],
    ["Neighborhood", "WhiteFiremarble03"],
    ["Neighborhood", "WhiteFiremarble04"],
    ["Neighborhood", "WhiteMarble04"],
    ["Neighborhood", "WhiteMarble06"],
    ["Neighborhood", "WhiteMarble07"],
    ["Neighborhood", "WhiteMarble08"],
    ["Neighborhood", "YellowFiremarble"],
    ["Neighborhood", "YellowMarble"],
    ["Neighborhood", "ConesVisMaster"],
    ["Neighborhood", "nb01FireMarbles1VisMaster"],
    ["Neighborhood", "nb01FireMarbles2VisMaster"],
    ["Neighborhood", "OrangeCone01"],
    ["Neighborhood", "OrangeCone04"],
    ["Neighborhood", "OrangeCone05"],
    ["Neighborhood", "OrangeCone11"],
    ["Neighborhood", "OrangeCone12"],
    ["Neighborhood", "OrangeCone15"],
    ["Neighborhood", "OrangeCone16"],
    ["Neighborhood", "OrangeCone17"],
    ["Gira", "FumerolBlastEmit01"],
    ["Gira", "FumerolBlastEmit02"],
    ["Gira", "FumerolBlastEmit03"],
    ["Gira", "FumerolBlastEmit04"],
    ["Gira", "FumerolBlastEmit05"],
    ["Gira", "FumerolBlastEmit06"],
    ["Gira", "FumerolSmokeEmitB01"],
    ["Gira", "FumerolSmokeEmitB02"],
    ["Gira", "FumerolSmokeEmitB03"],
    ["Gira", "FumerolSmokeEmitB04"],
    ["Gira", "FumerolSmokeEmitB05"],
    ["Gira", "FumerolSmokeEmitB06"],
    ["Gira", "FumerolSmokeEmitB07"],
    ["Gira", "FumerolSmokeEmitB08"],
    ["Gira", "FumerolSmokeEmitB09"],
    ["Gira", "FumerolSmokeEmit-Null01"],
    ["Gira", "FumerolSmokeEmit-Null02"],
    ["Gira", "FumerolSmokeEmit-Null03"],
    ["Gira", "FumerolSmokeEmit-Null04"],
    ["Gira", "FumerolSmokeEmit-Null05"],
    ["Gira", "FumerolSmokeEmit-Null06"],
    ["Gira", "fumerolRocksDummy"],
    ["city", "SmokeEmitter01"],
    ["city", "SmokeEmitter02"],
    ]

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

#=========================================
#
def PutAndShow(params=[]):
    print "PutAndShow begin"
    
    #Verifions les parametres
    if len(params) > 1:
        try:
            bShow = bool(params[1])
        except:
            bShow = True
    else:
        bShow = True
    if len(params) > 0:
        masterKey = params[0]
        if not isinstance(masterKey, ptKey):
            print "PutAndShow: first paremeter must be a ptKey"
            return 1
    if len(params) == 0:
        print "PutAndShow: needs 1 or 2 paremeters"
        return 1
    
    print "PutAndShow params ok"
    soMaster = masterKey.getSceneObject()
    print "PutAndShow({}, {})".format(soMaster.getName(), bShow)
    
    # Manipulons les clones
    cloneKeys = PtFindClones(masterKey)
    if len(cloneKeys) < 1:
        print "PutAndShow no clone found!"
    h = 8
    for ck in cloneKeys:
        soTop = ck.getSceneObject()
        pos = PtGetLocalAvatar().getLocalToWorld()
        mtransUp = ptMatrix44()
        mtransUp.translate(ptVector3(.0, .0, h))
        h = h + 5
        soTop.netForce(1)
        soTop.physics.warp(pos * mtransUp)
        if bShow:
            soTop.draw.enable(1)
        else:
            soTop.draw.enable(0)

    print "PutAndShow done"
    return 0

#=========================================
#
def PutAndShow2(params=[]):
    print "PutAndShow2 begin"
    
    #Verifions les parametres
    # au moins 4 parametres
    if len(params) > 3:
        if isinstance(params[3], ptMatrix44):
            pos = params[3]
        else:
            #position par defaut: sur moi
            pos = PtGetLocalAvatar().getLocalToWorld()
    else:
        #position par defaut: sur moi
        pos = PtGetLocalAvatar().getLocalToWorld()
    # au moins 3 parametres
    if len(params) > 2:
        try:
            scale = float(params[2])
        except:
            scale = 1
    else:
        scale = 1
    # au moins 2 parametres
    if len(params) > 1:
        try:
            bShow = bool(params[1])
        except:
            bShow = True
    else:
        bShow = True
    # au moins 1 parametre
    if len(params) > 0:
        masterKey = params[0]
        if not isinstance(masterKey, ptKey):
            print "PutAndShow2: first paremeter must be a ptKey"
            return 1
    # pas de parametre
    if len(params) == 0:
        print "PutAndShow2: needs 1, 2, 3 or 4 paremeters"
        return 1
    
    print "PutAndShow2 params ok"
    soMaster = masterKey.getSceneObject()
    print "PutAndShow2({}, {}, {}, matPos)".format(soMaster.getName(), bShow, scale)
    
    # Manipulons les clones
    cloneKeys = PtFindClones(masterKey)
    if len(cloneKeys) < 1:
        print "PutAndShow2 no clone found!"
    
    ck = cloneKeys[len(cloneKeys) - 1]
    #for ck in cloneKeys:
    soTop = ck.getSceneObject()

    mscale = ptMatrix44()
    mscale.makeScaleMat(ptVector3(scale, scale, scale))

    soTop.netForce(1)
    soTop.physics.warp(pos * mscale)
    if bShow:
        soTop.draw.enable(1)
        try:
            soTop.physics.enable(1)
        except:
            pass
    else:
        soTop.draw.enable(0)
        try:
            soTop.physics.enable(0)
        except:
            pass

    print "PutAndShow2 done"
    return 0

#=========================================
#
def PutAndShow3(params=[]):
    print "PutAndShow3 begin"
    
    #Verifions les parametres
    # au moins 4 parametres
    if len(params) > 3:
        if isinstance(params[3], ptMatrix44):
            pos = params[3]
        else:
            #position par defaut: sur moi
            pos = PtGetLocalAvatar().getLocalToWorld()
    else:
        #position par defaut: sur moi
        pos = PtGetLocalAvatar().getLocalToWorld()
    # au moins 3 parametres
    if len(params) > 2:
        try:
            scale = float(params[2])
        except:
            scale = 1
    else:
        scale = 1
    # au moins 2 parametres
    if len(params) > 1:
        try:
            bShow = bool(params[1])
        except:
            bShow = True
    else:
        bShow = True
    # au moins 1 parametre
    if len(params) > 0:
        masterKey = params[0]
        if not isinstance(masterKey, ptKey):
            print "PutAndShow: first paremeter must be a ptKey"
            return 1
    # pas de parametre
    if len(params) == 0:
        print "PutAndShow3: needs 1, 2, 3 or 4 paremeters"
        return 1
    
    print "PutAndShow3 params ok"
    soMaster = masterKey.getSceneObject()
    print "PutAndShow3({}, {}, {}, matPos)".format(soMaster.getName(), bShow, scale)
    
    # Manipulons les clones
    cloneKeys = PtFindClones(masterKey)
    if len(cloneKeys) < 1:
        print "PutAndShow3 no clone found!"
    
    ck = cloneKeys[len(cloneKeys) - 1]
    #for ck in cloneKeys:
    soTop = ck.getSceneObject()

    mscale = ptMatrix44()
    mscale.makeScaleMat(ptVector3(scale, scale, scale))

    soTop.netForce(1)
    soTop.physics.warp(pos * mscale)
    if bShow:
        soTop.draw.enable(1)
    else:
        soTop.draw.enable(0)

    print "PutAndShow3 done"
    return 0

#=========================================
#
def PutAndShow4(params=[]):
    print "PutAndShow4 begin"
    
    #Verifions les parametres
    # au moins 5 parametres
    if len(params) > 4:
        if isinstance(params[4], ptSceneobject):
            av = params[4]
        else:
            #par defaut: moi
            av = PtGetLocalAvatar()
    else:
        #par defaut: moi
        av = PtGetLocalAvatar()
    # au moins 4 parametres
    if len(params) > 3:
        try:
            bAttach = bool(params[3])
        except:
            bAttach = False
    else:
        bAttach = False
    # au moins 3 parametres
    if len(params) > 2:
        if isinstance(params[2], ptMatrix44):
            pos = params[2]
        else:
            #position par defaut: sur moi
            pos = PtGetLocalAvatar().getLocalToWorld()
    else:
        #position par defaut: sur moi
        pos = PtGetLocalAvatar().getLocalToWorld()
    # au moins 2 parametres
    if len(params) > 1:
        try:
            bShow = bool(params[1])
        except:
            bShow = True
    else:
        bShow = True
    # au moins 1 parametre
    if len(params) > 0:
        masterKey = params[0]
        if not isinstance(masterKey, ptKey):
            print "PutAndShow: first paremeter must be a ptKey"
            return 1
    # pas de parametre
    if len(params) == 0:
        print "PutAndShow4: needs 1, 2, 3 or 4 paremeters"
        return 1
    
    print "PutAndShow4 params ok"
    soMaster = masterKey.getSceneObject()
    print "PutAndShow4 master"
    #print "PutAndShow4({}, {}, {}, matPos, {}, {})".format(soMaster.getName(), bShow, bAttach, av.getName())
    print "PutAndShow4({})".format(soMaster.getName())
    print "PutAndShow4({})".format(bShow)
    print "PutAndShow4({})".format(bAttach)
    print "PutAndShow4({})".format(av.getName())
    
    print "PutAndShow4 manip"
    # Manipulons les clones
    cloneKeys = PtFindClones(masterKey)
    print "PutAndShow4 clones"
    if len(cloneKeys) < 1:
        print "PutAndShow4 no clone found!"
    else:
        print "PutAndShow4 ready"
        ck = cloneKeys[len(cloneKeys) - 1]
        #for ck in cloneKeys:
        so = ck.getSceneObject()

        so.netForce(1)
        so.physics.warp(pos)
        if bShow:
            so.draw.enable(1)
        else:
            so.draw.enable(0)
        if bAttach:
            Attacher(so, av, bPhys=False)
        else:
            Detacher(so, av)

    print "PutAndShow4 done"
    return 0

#=========================================
# Pour remettre dans l'etat d'origine.
def DayTime():
    ageSDL = PtGetAgeSDL()
    ageSDL["islmExplosionRun"] = (0L,)
    return 0

#=========================================
# Cree un clone et le place ou je suis
def Create(bShow=True, bLoad=True):
    masterKey = PtFindSceneobject(objectName, ageFileName).getKey()
    
    ageSDL = PtGetAgeSDL()
    ageSDL["islmExplosionRun"] = (1L,)

    if bLoad:
        # Combien de clones a-t-on deja?
        nbClones = len(PtFindClones(masterKey))
        print "Test : nb de clones de {} ==> {}".format(objectName, nbClones)
        # Ajouter des clones si besoin
        if nbClones < nombre:
            CloneFactory.CloneObject(objectName, ageFileName, nombre - nbClones)
        # Attendre que les clones soient prets et les manipuler
        PtSetAlarm(1, CloneFactory.AlarmWaittingForClones(objectName, ageFileName, nombre, PutAndShow, [masterKey, bShow]), 1)
        return "Clone loaded"
    else:
        # Retour a la normale
        CloneFactory.DechargerClones(masterKey)
        #DayTime()
        return "Clone unloaded"

#*****************************************
#
def TestDesert(params=[]):
    print "TestDesert begin"
    
    #Verifions les parametres
    if len(params) > 3:
        mPosAvatar = params[3]
        if mPosAvatar is not None and not isinstance(mPosAvatar, ptMatrix44):
            print "TestDesert: forth paremeter mPosAvatar must be a ptMatrix44"
            return 1
    else:
        mPosAvatar = None
        print "TestDesert: forth paremeter mPosAvatar is none"
    if len(params) > 2:
        soAvatar = params[2]
        if soAvatar is not None and not isinstance(soAvatar, ptSceneobject):
            print "TestDesert: third paremeter must be a ptSceneobject"
            return 1
    else:
        soAvatar = PtGetLocalAvatar()
    if len(params) > 1:
        try:
            bShow = bool(params[1])
        except:
            bShow = True
    else:
        bShow = True
    if len(params) > 0:
        masterKey = params[0]
        if not isinstance(masterKey, ptKey):
            print "TestDesert: first paremeter must be a ptKey"
            return 1
    if len(params) == 0:
        print "TestDesert: needs 1, 2 or 3 paremeters"
        return 1
    
    print "TestDesert params ok"
    soMaster = masterKey.getSceneObject()
    print "TestDesert({}, {})".format(soMaster.getName(), bShow)
    
    # Manipulons les clones
    cloneKeys = PtFindClones(masterKey)
    if len(cloneKeys) < 1:
        print "TestDesert no clone found!"
    
    soTop = cloneKeys[0].getSceneObject()

    #pos = PtGetLocalAvatar().getLocalToWorld()
    soTop.netForce(1)

    #soTop.physics.warp(pos)
    if bShow:
        soTop.draw.enable(1)
        try:
            soTop.physics.enable(1)
            if mPosAvatar is not None:
                soAvatar.physics.warp(mPosAvatar)
                soAvatar.netForce(1)
        except:
            pass
    else:
        soTop.draw.enable(0)
        try:
            soTop.physics.enable(0)
        except:
            pass

    print "TestDesert done"
    return 0

#=========================================
# Cree un clone du desert
def Desert(bShow=True, bLoad=True):
        
    #masterKey = PtFindSceneobject("DesertPlane", "Cleft").getKey()
    #masterKey = PtFindSceneobject("DesertPlane1", "Cleft").getKey()
    #masterKey = PtFindSceneobject("DesertPlane2", "Cleft").getKey()
    #masterKey = PtFindSceneobject("DesertPlane3", "Cleft").getKey()
    #masterKey = PtFindSceneobject("DesertPlane3", "Cleft").getKey()
    
    nb = 1
    age = "Cleft"
    lstObj = ["DesertPlane", "DesertPlane1", "DesertPlane2", "DesertPlane3", "DesertPlane4"]
    msg = "CloneObject.Desert(): "
    masterkey = None
    for obj in lstObj:
        try:
            masterkey = PtFindSceneobject(obj, age).getKey()
        except:
            print "{} not found in {}".format(obj, age)
            msg += "{} not found in {}\n".format(obj, age)
        if isinstance(masterkey, ptKey):
            if bLoad:
                # Combien de clones a-t-on deja?
                nbClones = len(PtFindClones(masterkey))
                print "Test : nb de clones de {} ==> {}".format(obj, nbClones)
                # Ajouter des clones si besoin
                if nbClones < nb:
                    CloneFactory.CloneObject(obj, age, nb - nbClones)
                # Attendre que les clones soient prets et les manipuler
                PtSetAlarm(1, CloneFactory.AlarmWaittingForClones(obj, age, nb, TestDesert, [masterkey, bShow]), 1)
                print "Clone of {} loaded".format(obj)
                msg += "Clone of {} loaded\n".format(obj)
            else:
                # Retour a la normale
                CloneFactory.DechargerClones(masterkey)
                #DayTime()
                print "Clone of {} unloaded".format(obj)
                msg += "Clone of {} unloaded\n".format(obj)
        else:
            print "not a ptKey!"
            msg += "not a ptKey\n"

    return msg

#=========================================
# Cree un clone du sol de Minkata
def Minkata(bShow=True, bLoad=True, vPosAvatar=None, soPlayer=None, matPos=None):
    nb = 1
    age = "Minkata"
    #lstObj = ["GroundFloorProxy", "GroundPlaneDist", "GroundPlaneVis"]
    lstObj = ["GroundFloorProxy"]
    msg = "CloneObject.Desert(): "
    masterkey = None
    for obj in lstObj:
        try:
            masterkey = PtFindSceneobject(obj, age).getKey()
        except:
            print "{} not found in {}".format(obj, age)
            msg += "{} not found in {}\n".format(obj, age)
        if isinstance(masterkey, ptKey):
            if bLoad:
                # Combien de clones a-t-on deja?
                nbClones = len(PtFindClones(masterkey))
                print "Test : nb de clones de {} ==> {}".format(obj, nbClones)
                # Ajouter des clones si besoin
                if nbClones < nb:
                    CloneFactory.CloneObject(obj, age, nb - nbClones)
                # Attendre que les clones soient prets et les manipuler
                PtSetAlarm(1, CloneFactory.AlarmWaittingForClones(obj, age, nb, TestDesert, [masterkey, bShow, soPlayer, matPos]), 1)
                print "Clone of {} loaded".format(obj)
                msg += "Clone of {} loaded\n".format(obj)
            else:
                # Retour a la normale
                CloneFactory.DechargerClones(masterkey)
                #DayTime()
                print "Clone of {} unloaded".format(obj)
                msg += "Clone of {} unloaded\n".format(obj)
        else:
            print "not a ptKey!"
            msg += "not a ptKey\n"

    return msg

#=========================================
# Cree un clone du sol de Minkata + SandscritRoot + SphereEnviron
def HoodEvent(bShow=True, bLoad=True):
    nb = 1
    age = "Minkata"
    #lstObj = ["GroundFloorProxy", "GroundPlaneDist", "GroundPlaneVis"]
    lstObj = ["GroundFloorProxy"]
    msg = "CloneObject.Desert(): "
    masterkey = None
    for obj in lstObj:
        try:
            masterkey = PtFindSceneobject(obj, age).getKey()
        except:
            print "{} not found in {}".format(obj, age)
            msg += "{} not found in {}\n".format(obj, age)
        if isinstance(masterkey, ptKey):
            if bLoad:
                # Combien de clones a-t-on deja?
                nbClones = len(PtFindClones(masterkey))
                print "Test : nb de clones de {} ==> {}".format(obj, nbClones)
                # Ajouter des clones si besoin
                if nbClones < nb:
                    CloneFactory.CloneObject(obj, age, nb - nbClones)
                # Attendre que les clones soient prets et les manipuler
                PtSetAlarm(1, CloneFactory.AlarmWaittingForClones(obj, age, nb, TestDesert, [masterkey, bShow]), 1)
                print "Clone of {} loaded".format(obj)
                msg += "Clone of {} loaded\n".format(obj)
            else:
                # Retour a la normale
                CloneFactory.DechargerClones(masterkey)
                #DayTime()
                print "Clone of {} unloaded".format(obj)
                msg += "Clone of {} unloaded\n".format(obj)
        else:
            print "not a ptKey!"
            msg += "not a ptKey\n"

    return msg

#=========================================
# Cree des clones V1
def co(lstObj, age, nb, bShow=True, bLoad=True):
    
    #nb = 1
    #age = "Cleft"
    #lstObj = ["DesertPlane", "DesertPlane1", "DesertPlane2", "DesertPlane3", "DesertPlane4"]
    msg = "CloneObject.co(): "
    masterkey = None
    for obj in lstObj:
        try:
            masterkey = PtFindSceneobject(obj, age).getKey()
        except:
            print "{} not found in {}".format(obj, age)
            msg += "{} not found in {}\n".format(obj, age)
        if isinstance(masterkey, ptKey):
            if bLoad:
                # Combien de clones a-t-on deja?
                nbClones = len(PtFindClones(masterkey))
                print "Test : nb de clones de {} ==> {}".format(obj, nbClones)
                # Ajouter des clones si besoin
                if nbClones < nb:
                    CloneFactory.CloneObject(obj, age, nb - nbClones)
                # Attendre que les clones soient prets et les manipuler
                PtSetAlarm(1, CloneFactory.AlarmWaittingForClones(obj, age, nb, PutAndShow, [masterkey, bShow]), 1)
                print "Clone of {} loaded".format(obj)
                msg += "Clone of {} loaded\n".format(obj)
            else:
                # Retour a la normale
                CloneFactory.DechargerClones(masterkey)
                #DayTime()
                print "Clone of {} unloaded".format(obj)
                msg += "Clone of {} unloaded\n".format(obj)
        else:
            print "not a ptKey!"
            msg += "not a ptKey\n"

    return msg

#=========================================
# Cree des clones V2
def co2(lstObj, age, nb, bShow=True, bLoad=True, scale=1, height=8):
    
    #nb = 1
    #age = "Cleft"
    #lstObj = ["DesertPlane", "DesertPlane1", "DesertPlane2", "DesertPlane3", "DesertPlane4"]
    msg = "CloneObject.co(): "
    masterkey = None
    for obj in lstObj:
        try:
            masterkey = PtFindSceneobject(obj, age).getKey()
        except:
            print "{} not found in {}".format(obj, age)
            msg += "{} not found in {}\n".format(obj, age)
        if isinstance(masterkey, ptKey):
            if bLoad:
                # Combien de clones a-t-on deja?
                nbClones = len(PtFindClones(masterkey))
                print "Test : nb de clones de {} ==> {}".format(obj, nbClones)
                # Ajouter des clones si besoin
                if nbClones < nb:
                    CloneFactory.CloneObject(obj, age, nb - nbClones)
                # Attendre que les clones soient prets et les manipuler
                PtSetAlarm(1, CloneFactory.AlarmWaittingForClones(obj, age, nb, PutAndShow2, [masterkey, bShow, scale, height]), 1)
                print "Clone of {} loaded".format(obj)
                msg += "Clone of {} loaded\n".format(obj)
            else:
                # Retour a la normale
                CloneFactory.DechargerClones(masterkey)
                #DayTime()
                print "Clone of {} unloaded".format(obj)
                msg += "Clone of {} unloaded\n".format(obj)
        else:
            print "not a ptKey!"
            msg += "not a ptKey\n"
    return msg

#=========================================
# Cree un clone a la position desiree
def co3(objName, age, bShow=True, bLoad=True, scale=1, matPos=None):
    print "          ** co3 ** 1 begin"
    msg = "CloneObject.co3(): "
    nb = 1
    masterkey = None

    try:
        masterkey = PtFindSceneobject(objName, age).getKey()
    except:
        print "{} not found in {}".format(objName, age)
        msg += "{} not found in {}\n".format(objName, age)
    print "          ** co3 ** 2"
    if isinstance(masterkey, ptKey):
        if bLoad:
            print "          ** co3 ** 3 loading"
            # Combien de clones a-t-on deja?
            nbClones = len(PtFindClones(masterkey))
            print "Test : nb de clones de {} ==> {}".format(objName, nbClones)
            # Ajouter des clones si besoin
            if nbClones < nb:
                CloneFactory.CloneObject(objName, age, nb - nbClones)
            # Attendre que les clones soient prets et les manipuler
            PtSetAlarm(1, CloneFactory.AlarmWaittingForClones(objName, age, nb, PutAndShow3, [masterkey, bShow, scale, matPos]), 1)
            print "Clone of {} loaded".format(objName)
            msg += "Clone of {} loaded\n".format(objName)
        else:
            # Retour a la normale
            CloneFactory.DechargerClones(masterkey)
            #DayTime()
            print "Clone of {} unloaded".format(objName)
            msg += "Clone of {} unloaded\n".format(objName)
    else:
        print "not a ptKey!"
        msg += "not a ptKey\n"
    return msg

#=========================================
# Ajouter un clone et le mettre a la postion desiree
def AddClone(lstObj, age=None, matPos=None):
    # Valeurs par defaut

    bShow = True
    bLoad = True
    scale = 1
    if age is None or age == "":
        #Par defaut, age courrant
        age = PtGetAgeInfo().getAgeFilename()

    msg = "CloneObject.AddClone(): "
    masterkey = None
    for obj in lstObj:
        try:
            masterkey = PtFindSceneobject(obj, age).getKey()
        except:
            print "{} not found in {}".format(obj, age)
            msg += "{} not found in {}\n".format(obj, age)
        if isinstance(masterkey, ptKey):
            if bLoad:
                # Combien de clones a-t-on deja?
                nbClones = len(PtFindClones(masterkey))
                # ajouter un clone
                CloneFactory.CloneObject(obj, age, 1)
                # Attendre que les clones soient prets et les manipuler
                PtSetAlarm(1, CloneFactory.AlarmWaittingForClones(obj, age, 1, PutAndShow2, [masterkey, bShow, scale, matPos]), 1)
                print "Clone of {} loaded".format(obj)
                msg += "Clone of {} loaded\n".format(obj)
            else:
                # Retour a la normale
                CloneFactory.DechargerClones(masterkey)
                #DayTime()
                print "Clone of {} unloaded".format(obj)
                msg += "Clone of {} unloaded\n".format(obj)
        else:
            print "not a ptKey!"
            msg += "not a ptKey\n"
    return msg

#=========================================
# Ajouter un clone et le mettre a ma postion
def AddCloneHere(lstObj, age=None):
    #height = 1
    #scale = 1
    #pos = PtGetLocalAvatar().getLocalToWorld()
    #mtransUp = ptMatrix44()
    #mtransUp.translate(ptVector3(.0, .0, height))
    #mscale = ptMatrix44()
    #mscale.makeScaleMat(ptVector3(scale, scale, scale))
    #matPos = pos * mtransUp * mscale
    matPos = PtGetLocalAvatar().getLocalToWorld()
    AddClone(lstObj, age, matPos)

#=========================================
#
class WaitAndChangeScale:
    def __init__(self, so=None, scale=ptVector3(1, 1, 1)):
        print "WaitAndChangeScale: init"
        self._scale = scale
        self._so = so
    
    def onAlarm(self, param):
        print "WaitAndChangeScale: onAlarm"
        if isinstance(self._so, ptSceneobject):
            pos = self._so.getLocalToWorld()
            mscale = ptMatrix44()
            mscale.makeScaleMat(self._scale)
            self._so.physics.warp(pos * mscale)
            print "WaitAndChangeScale: done"
        else:
            print "WaitAndChangeScale: not a ptSceneobject"


#=========================================
#
def DoStuff(params=[]):
    print "DoStuff begin"
    
    #Verifions les parametres
    # au moins 5 parametres
    if len(params) > 1:
        print "DoStuff params 4"
        try:
            bAttach = bool(params[4])
        except:
            bAttach = True
    else:
        bAttach = True
    # au moins 4 parametres
    if len(params) > 3:
        print "DoStuff params 3"
        if isinstance(params[3], ptMatrix44):
            pos = params[3]
        else:
            #position par defaut: sur moi
            pos = PtGetLocalAvatar().getLocalToWorld()
    else:
        #position par defaut: sur moi
        pos = PtGetLocalAvatar().getLocalToWorld()
    # au moins 3 parametres
    if len(params) > 2:
        print "DoStuff params 2"
        if isinstance(params[2], ptVector3):
            scale = params[2]
        else:
            print "DoStuff scale is not a ptVector3!"
            scale = ptVector3(1, 1, 1)
    else:
        scale = ptVector3(1, 1, 1)
    # au moins 2 parametres
    if len(params) > 1:
        print "DoStuff params 1"
        try:
            bShow = bool(params[1])
        except:
            bShow = True
    else:
        bShow = True
    # au moins 1 parametre
    if len(params) > 0:
        print "DoStuff params 0"
        masterKey = params[0]
        if not isinstance(masterKey, ptKey):
            print "DoStuff: first paremeter must be a ptKey"
            return 1
    # pas de parametre
    if len(params) == 0:
        print "DoStuff: needs 1, 2, 3 or 4 paremeters"
        return 1
    
    print "DoStuff params ok"
    soMaster = masterKey.getSceneObject()
    print "DoStuff({}, {}, {}, matPos)".format(soMaster.getName(), bShow, scale)
    
    # Manipulons les clones
    cloneKeys = PtFindClones(masterKey)
    if len(cloneKeys) < 1:
        print "DoStuff no clone found!"
    else:
        print "DoStuff : the stuff" 
        ck = cloneKeys[len(cloneKeys) - 1]
        #for ck in cloneKeys:
        soTop = ck.getSceneObject()

        #mscale = ptMatrix44()
        #mscale.makeScaleMat(scale)

        soTop.netForce(1)
        soTop.physics.disable()
        soTop.physics.warp(pos)
        #soTop.physics.warp(pos * mscale)
        print "DoStuff : call WaitAndChangeScale" 
        PtSetAlarm(1, WaitAndChangeScale(soTop, scale), 1)
        if bShow:
            soTop.draw.enable(1)
        else:
            soTop.draw.enable(0)
        if bAttach:
            Attacher(soTop, PtGetLocalAvatar(), bPhys=False)
        else:
            Detacher(soTop, PtGetLocalAvatar())

    print "DoStuff done"
    return 0

#=========================================
# Cree un clone a la position desiree
def clone1(objName, age, bShow=True, bLoad=True, color="red", scale=ptVector3(1, 1, 1), matPos=None, bAttach=False, fct=DoStuff):
    print "          ** clone1 ** 1 begin"
    msg = "CloneObject.clone1(): "
    nb = 1
    masterkey = None

    try:
        masterkey = PtFindSceneobject(objName, age).getKey()
    except:
        print "{} not found in {}".format(objName, age)
        msg += "{} not found in {}\n".format(objName, age)
    print "          ** clone1 ** 2"
    if isinstance(masterkey, ptKey):
        marbles = PtFindSceneobjects('MarblePhy')
        marblePhysKey = None
        if color == "yellow":
            marblePhysKey = marbles[0].getKey()
        elif color == "white":
            marblePhysKey = marbles[1].getKey()
        elif color == "blue":
            marblePhysKey = marbles[2].getKey()
        else:
            marblePhysKey = marbles[3].getKey()

        if bLoad:
            print "          ** clone1 ** 3 loading"
            # Combien de clones a-t-on deja?
            nbClones = len(PtFindClones(masterkey))
            print "Test : nb de clones de {} ==> {}".format(objName, nbClones)
            # Ajouter des clones si besoin
            if nbClones < nb:
                CloneFactory.CloneObject(objName, age, nb - nbClones)
            # Attendre que les clones soient prets et les manipuler
            #PtSetAlarm(1, CloneFactory.AlarmWaittingForClones(objName, age, nb, fct, [masterkey, bShow, scale, matPos]), 1)
            PtSetAlarm(1, CloneFactory.AlarmWaittingForClones(objName, age, nb, fct, [marblePhysKey, bShow, scale, matPos, bAttach]), 1)
            print "Clone of {} loaded".format(objName)
            msg += "Clone of {} loaded\n".format(objName)
        else:
            # Retour a la normale
            CloneFactory.DechargerClones(masterkey)
            #DayTime()
            print "Clone of {} unloaded".format(objName)
            msg += "Clone of {} unloaded\n".format(objName)
    else:
        print "not a ptKey!"
        msg += "not a ptKey\n"
    return msg

#=========================================
# Cree un clone a la position desiree
def Clone2(objName, age, bShow=True, bLoad=True, matPos=None, bAttach=False, soAvatar=None):
    print "          ** Clone2 ** 1 begin"
    msg = "CloneObject.Clone2(): "
    nb = 1
    masterkey = None

    try:
        masterkey = PtFindSceneobject(objName, age).getKey()
    except:
        print "{} not found in {}".format(objName, age)
        msg += "{} not found in {}\n".format(objName, age)
    print "          ** Clone2 ** 2"
    if isinstance(masterkey, ptKey):
        if bLoad:
            print "          ** Clone2 ** 3 loading"
            # Combien de clones a-t-on deja?
            nbClones = len(PtFindClones(masterkey))
            print "Test : nb de clones de {} ==> {}".format(objName, nbClones)
            # Ajouter des clones si besoin
            if nbClones < nb:
                CloneFactory.CloneObject(objName, age, nb - nbClones)
            # Attendre que les clones soient prets et les manipuler
            PtSetAlarm(1, CloneFactory.AlarmWaittingForClones(objName, age, nb, PutAndShow4, [masterkey, bShow, matPos, bAttach, soAvatar]), 1)
            print "Clone of {} loaded".format(objName)
            msg += "Clone of {} loaded\n".format(objName)
        else:
            # Retour a la normale
            CloneFactory.DechargerClones(masterkey)
            #DayTime()
            print "Clone of {} unloaded".format(objName)
            msg += "Clone of {} unloaded\n".format(objName)
    else:
        print "not a ptKey!"
        msg += "not a ptKey\n"
    return msg

#=========================================
# Test jouons avec une bille (firemarble)
#def Bille(bOnOff=True, position=0, bAttacher=False):
def Bille(bOnOff=True, x=0, y=0, z=0, bAttacher=False):
    #tuplePos = ((1,0,0,0),(0,1,0,-250),(0,0,1,220),(0,0,0,1))
    
    #if position == 0:
    #    pos = PtGetLocalAvatar().getLocalToWorld()
    #else:
    #    if position == 1:
    #        x=0
    #        y=-2000
    #        z=220
    #    elif position == 2:
    #        x=0
    #        y=-93
    #        z=221
    #    else:
    #        x=0
    #        y=-93
    #        z=294
    #    tuplePos = ((1,0,0,x),(0,1,0,y),(0,0,1,z),(0,0,0,1))
    #    pos = ptMatrix44()
    #    pos.setData(tuplePos)
    tuplePos = ((1,0,0,x),(0,1,0,y),(0,0,1,z),(0,0,0,1))
    pos = ptMatrix44()
    pos.setData(tuplePos)

    mtrans = ptMatrix44()
    #mtrans.translate(ptVector3(0, -5, 5))
    mtrans.translate(ptVector3(0, 0, 0))
    #vScale = ptVector3(.1, .1, 5)
    #vScale = ptVector3(.1, 5, .1)
    #mscale = ptMatrix44()
    #mscale.makeScaleMat(vScale)
    pos = pos * mtrans
    #pos = pos * mtrans * mscale
    #print "vScale=({}, {}, {})".format(vScale.getX(), (vScale.getY(), (vScale.getZ())
    
    #clone1("nb01FireMarbles2VisMaster", "Neighborhood", bShow=True, bLoad=True, color="red", scale=1, matPos=pos, fct=DoStuff)
    #clone1("nb01FireMarbles2VisMaster", "Neighborhood", bShow=True, bLoad=True, color="blue", scale=1, matPos=pos, fct=DoStuff)
    #clone1("nb01FireMarbles2VisMaster", "Neighborhood", bShow=True, bLoad=True, color="yellow", scale=1, matPos=pos, fct=DoStuff)

    #vScale = ptVector3(.5, .5, 5)
    #vColor = "red"
    #clone1("nb01FireMarbles2VisMaster", "Neighborhood", bShow=True, bLoad=True, color=vColor, scale=vScale, matPos=pos, fct=DoStuff)
    #
    #vScale = ptVector3(.5, 5, .5)
    #vColor = "blue"
    #clone1("nb01FireMarbles2VisMaster", "Neighborhood", bShow=True, bLoad=True, color=vColor, scale=vScale, matPos=pos, fct=DoStuff)
    #
    #vScale = ptVector3(5, .5, .5)
    #vColor = "yellow"
    #clone1("nb01FireMarbles2VisMaster", "Neighborhood", bShow=True, bLoad=True, color=vColor, scale=vScale, matPos=pos, fct=DoStuff)

    #vScale = ptVector3(10, 10, 220)
    vScale = ptVector3(10, 10, 200)
    vColor = "red"
    #clone1("nb01FireMarbles2VisMaster", "Neighborhood", bShow=True, bLoad=True, color=vColor, scale=vScale, matPos=pos, fct=DoStuff)
    clone1("nb01FireMarbles2VisMaster", "Neighborhood", bShow=bOnOff, bLoad=bOnOff, color=vColor, scale=vScale, matPos=pos, bAttach=bAttacher, fct=DoStuff)

# =========
#
def Beam(bOn=True, sColor="red", position=None, vScale=ptVector3(10, 10, 200), sAxis="x", fAngle=0):
    # verifying parameters:
    # bOn
    if not isinstance(bOn, bool):
        bOn = True
    # sColor
    if not isinstance(sColor, basestring):
        sColor = "red"
    sColor = sColor.lower()
    if not sColor in ("red", "blue", "yellow", "white"):
        sColor = "red"
    # vScale
    if not isinstance(vScale, ptVector3):
        vScale=ptVector3(10, 10, 200)
    # position
    if isinstance(position, ptVector3):
        #Bille(bOnOff=bOn, x=position.getX(), y=position.getY(), z=position.getZ(), bAttacher=False)
        px = position.getX()
        py = position.getY()
        pz = position.getZ()
    elif isinstance(position, ptMatrix44):
        tuplePos=position.getData()
        #Bille(bOnOff=bOn, x=tuplePos[0][3], y=tuplePos[1][3], z=tuplePos[2][3], bAttacher=False)
        px=tuplePos[0][3]
        py=tuplePos[1][3]
        pz=tuplePos[2][3]
    elif isinstance(position, int):
        if position == 0:
            #pos = PtGetLocalAvatar().getLocalToWorld()
            pos = PtGetLocalAvatar().position()
            #Bille(bOnOff=bOn, x=pos.getX(), y=pos.getY(), z=pos.getZ(), bAttacher=False)
            px=pos.getX()
            py=pos.getY()
            pz=pos.getZ()
        else:
            if position == 1:
                px=0
                py=-2000
                pz=220
            elif position == 2:
                px=0
                py=-93
                pz=221
            else:
                px=0
                py=-93
                pz=294
            #Bille(bOnOff=bOn, x=px, y=py, z=pz, bAttacher=False)
    elif position is None:
        pos = PtGetLocalAvatar().position()
        px=pos.getX()
        py=pos.getY()
        pz=pos.getZ()
    else:
        print "Beam Error: position must be an int or a ptVector3 or a ptMatrix44"
        return
    # rotation:
    # sAxis
    if isinstance(sAxis, basestring):
        sAxis = sAxis.lower()
        if not sAxis in ("x", "y", "z"):
            sAxis = "x"
    else:
        sAxis = "x"
    axis = 0
    if sAxis == "x":
        axis = 0
    elif sAxis == "y":
        axis = 1
    elif sAxis == "z":
        axis = 2
    else:
        pass
    mRot = ptMatrix44()
    mRot.rotate(axis, (math.pi * float(fAngle)) / 180)

    # parameters are set, we can continue
    tuplePos = ((1,0,0,px),(0,1,0,py),(0,0,1,pz),(0,0,0,1))
    mPos = ptMatrix44()
    mPos.setData(tuplePos)
    
    #add rotation
    mPos = mPos * mRot
    
    clone1("nb01FireMarbles2VisMaster", "Neighborhood", bShow=bOn, bLoad=bOn, color=sColor, scale=vScale, matPos=mPos, bAttach=False, fct=DoStuff)

# =========
#
def Bugs(bOn=True, position=None, bTie=False, soPlayer=None):
    # verifying parameters:
    # bOn
    if not isinstance(bOn, bool):
        bOn = True
    # bTie
    if not isinstance(bTie, bool):
        bTie = True
    # position
    if isinstance(position, ptVector3):
        px = position.getX()
        py = position.getY()
        pz = position.getZ()
    elif isinstance(position, ptMatrix44):
        tuplePos=position.getData()
        px=tuplePos[0][3]
        py=tuplePos[1][3]
        pz=tuplePos[2][3]
    elif position is None:
        pos = PtGetLocalAvatar().position()
        px=pos.getX()
        py=pos.getY()
        pz=pos.getZ()
    else:
        print "Bugs Error: position must be an int or a ptVector3 or a ptMatrix44"
        return

    # parameters are set, we can continue
    tuplePos = ((1,0,0,px),(0,1,0,py),(0,0,1,pz),(0,0,0,1))
    mPos = ptMatrix44()
    mPos.setData(tuplePos)
    
    Clone2("BugFlockingEmitTest", "Garden", bShow=bOn, bLoad=bOn, matPos=mPos, bAttach=bTie, soAvatar=soPlayer)

#attacher so1 a so2 : attacher(obj, av) ou l'inverse    
def Attacher(so1, so2, bPhys=False):
    """attacher so1 à so2 : attacher(obj, av) ou l'inverse"""
    so1.physics.netForce(1)
    so1.draw.netForce(1)
    PtAttachObject(so1, so2, 1)

# detacher so1 de so2 : detach(obj, av) ou l'inverse    
def Detacher(so1, so2):
    so1.physics.netForce(1)
    so1.draw.netForce(1)
    PtDetachObject(so1, so2, 1)

#=================================================================

# Find scene objects with name like soName in all loaded districts (aka pages or prp files)
# ex.: soName = "Bahro*Stone" will be transformed in regexp "^.*Bahro.*Stone.*$"
# copie de celle de xBotAge
def FindSOName(soName):
    import re
    cond = "^.*" + soName.replace("*", ".*") + ".*$"
    pattern = re.compile(cond, re.IGNORECASE)
    strList = soName.split("*")
    nameList = list()
    for str in strList:
        nameList.extend(map(lambda so: so.getName(), PtFindSceneobjects(str)))
    nameList = list(set(nameList))
    nameList = filter(lambda x: pattern.match(x) != None, nameList)
    return nameList

# Retourne la position du premier clone trouve ayant des coordonnees
def GetFirstClonePosition(name):
    nameList = FindSOName(name)
    for soName in nameList:
        print "nom: {}".format(soName)
        try:
            sol = PtFindSceneobjects(soName)
            for mso in sol:
                print "mso: {}".format(mso.getName())
                cloneKeys = PtFindClones(mso.getKey())
                print "cloneKeys: {}".format(len(cloneKeys))
                for k in cloneKeys:
                    so = k.getSceneObject()
                    print "so: {}".format(so.getName())
                    pos = so.position()
                    if pos.getX() != 0.0 or pos.getY() != 0.0 or pos.getZ() != 0.0:
                        print "clone trouve"
                        return so
        except:
            continue
    return None

# == FIN ==