# -*- coding: utf-8 -*-
# == Script pour generer un clone d'objet au choix ==
# Mirphak 2013-12-15 version 3

from Plasma import *
import math
import CloneFactory


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
#
class WaitAndChangeScale:
    def __init__(self, so=None, scale=ptVector3(1, 1, 1), bPhys=False):
        print "WaitAndChangeScale: init"
        self._scale = scale
        self._so = so
        self._bPhys = bPhys
    
    def onAlarm(self, param):
        print "WaitAndChangeScale: onAlarm"
        if isinstance(self._so, ptSceneobject):
            pos = self._so.getLocalToWorld()
            mscale = ptMatrix44()
            mscale.makeScaleMat(self._scale)
            self._so.physics.warp(pos * mscale)
            if self._bPhys:
                self._so.physics.enable(1)
            else:
                self._so.physics.enable(0)
            print "WaitAndChangeScale: done"
        else:
            print "WaitAndChangeScale: not a ptSceneobject"

#=========================================
#
def DoStuff(params=[]):
    print "DoStuff begin"
    
    #Verifions les parametres
    # au moins 6 parametres
    if len(params) > 1:
        print "DoStuff params 5"
        try:
            bPhys = bool(params[5])
        except:
            bPhys = False
    else:
        bPhys = False
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
            #scale = ptVector3(1, 1, 1)
            scale = None
    else:
        #scale = ptVector3(1, 1, 1)
        scale = None
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
        if bShow:
            soTop.draw.enable(1)
        else:
            soTop.draw.enable(0)
        if bAttach:
            Attacher(soTop, PtGetLocalAvatar(), bPhys=False)
        else:
            Detacher(soTop, PtGetLocalAvatar())
        if scale is None:
            if bPhys:
                soTop.physics.enable(1)
            else:
                soTop.physics.enable(0)
        else:
            print "DoStuff : call WaitAndChangeScale" 
            PtSetAlarm(1, WaitAndChangeScale(soTop, scale, bPhys), 1)

    print "DoStuff done"
    return 0

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
            #PtSetAlarm(1, CloneFactory.AlarmWaittingForClones(objName, age, nb, DoStuff, [masterkey, bShow, scale, matPos, False]), 1)
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

#

#=========================================
# Cree un clone a la position desiree
def cloneit(objName, age, bShow=True, bLoad=True, scale=ptVector3(1, 1, 1), matPos=None, fct=DoStuff):
    print "          ** cloneit ** 1 begin"
    msg = "CloneObject.cloneit(): "
    nb = 1
    masterkey = None

    try:
        masterkey = PtFindSceneobject(objName, age).getKey()
    except:
        print "{} not found in {}".format(objName, age)
        msg += "{} not found in {}\n".format(objName, age)
    print "          ** cloneit ** 2"
    if isinstance(masterkey, ptKey):
        if bLoad:
            print "          ** clone1 ** 3 loading"
            # Combien de clones a-t-on deja?
            nbClones = len(PtFindClones(masterkey))
            print "Test : nb de clones de {} ==> {}".format(objName, nbClones)
            # Ajouter des clones si besoin
            if nbClones < nb:
                CloneFactory.CloneObject(objName, age, nb - nbClones)
            # Attendre que les clones soient prets et les manipuler
            PtSetAlarm(1, CloneFactory.AlarmWaittingForClones(objName, age, nb, fct, [masterkey, bShow, scale, matPos, False, True]), 1)
            #PtSetAlarm(1, CloneFactory.AlarmWaittingForClones(objName, age, nb, fct, [marblePhysKey, bShow, scale, matPos, bAttach]), 1)
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

#
def Rect(objName, age, bOn=True, position=None, vScale=ptVector3(1, 1, 1), fXAngle=0, fYAngle=0, fZAngle=0):
    posType = -1
    # verifying parameters:
    # bOn
    if not isinstance(bOn, bool):
        bOn = True
    # vScale
    if not isinstance(vScale, ptVector3):
        #vScale = ptVector3(10, 10, 200)
        vScale = None
    # position
    if isinstance(position, ptVector3):
        px = position.getX()
        py = position.getY()
        pz = position.getZ()
    elif isinstance(position, ptMatrix44):
        tuplePos=position.getData()
        px = tuplePos[0][3]
        py = tuplePos[1][3]
        pz = tuplePos[2][3]
    elif isinstance(position, int):
        if position == 0:
            #pos = PtGetLocalAvatar().position()
            #px = pos.getX()
            #py = pos.getY()
            #pz = pos.getZ()
            matAv = PtGetLocalAvatar().getLocalToWorld()
            #tuplePos = matAv.getData()
            #px = tuplePos[0][3]
            #py = tuplePos[1][3]
            #pz = tuplePos[2][3]
            posType = 0
        elif position == 1:
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
    elif position is None:
        pos = PtGetLocalAvatar().position()
        px=pos.getX()
        py=pos.getY()
        pz=pos.getZ()
        #py=pos.getY() - 30.0
        #pz=pos.getZ() - 3.25
    else:
        print "Rect Error: position must be an int or a ptVector3 or a ptMatrix44"
        return
    # rotations:
    """
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
    """
    mRotX = ptMatrix44()
    fXAngle = float(fXAngle) - 90.0
    mRotX.rotate(0, (math.pi * float(fXAngle)) / 180)
    
    mRotY = ptMatrix44()
    #fYAngle = float(fYAngle) - 90.0
    mRotY.rotate(1, (math.pi * float(fYAngle)) / 180)
    
    mRotZ = ptMatrix44()
    mRotZ.rotate(2, (math.pi * float(fZAngle)) / 180)
    
    # parameters are set, we can continue
    if posType == 0:
        mPos = matAv
    else:
        tuplePos = ((1,0,0,px),(0,1,0,py),(0,0,1,pz),(0,0,0,1))
        mPos = ptMatrix44()
        mPos.setData(tuplePos)
    
    #add rotations
    mPos = mPos * mRotZ
    mPos = mPos * mRotY
    mPos = mPos * mRotX
    
    mTrans = ptMatrix44()
    #mTrans.translate(ptVector3(-3.25, 0.0, 30.0))
    mTrans.translate(ptVector3(0.0, -3.25, 30.0))
    mPos = mPos * mTrans

    #cloneit("Rect0", "Jalak", bShow=bOn, bLoad=bOn, scale=vScale, matPos=mPos, fct=DoStuff)
    #CloneObject.co3("Rect0", "Jalak", bShow=bOn, bLoad=bOn)
    cloneit(objName, age, bShow=bOn, bLoad=bOn, scale=vScale, matPos=mPos, fct=DoStuff)

#
def colonne(bOn=True, fXAngle=0, fYAngle=0, fZAngle=0):
    objName = "columnPhys_24"
    age = "Jalak"
    #position = None
    position = 0
    #vScale = ptVector3(1, 1, 1)
    vScale = None
    #, fXAngle=0, fYAngle=0, fZAngle=0
    Rect(objName, age, bOn, position, vScale, fXAngle, fYAngle, fZAngle)
