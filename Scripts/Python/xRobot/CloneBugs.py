# -*- coding: utf-8 -*-
# == Script pour generer un clone de lucioles ==
# Mirphak 2014-05-01 version 1

from Plasma import *
import math
import CloneFactory


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

# == FIN ==