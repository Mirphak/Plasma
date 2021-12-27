# -*- coding: utf-8 -*-
# == Script pour generer un clone d'objet au choix ==
# Mirphak 2013-12-15 version 3

from Plasma import *
import math
import CloneFactory


#=========================================
#
def DoStuff(params=[]):
    print "DoStuff begin"
    
    #Verifions les parametres
    # au moins 4 parametres
    if len(params) > 3:
        print "DoStuff params 3"
        try:
            bPhys = bool(params[3])
        except:
            bPhys = False
    else:
        bPhys = False
    # au moins 3 parametres
    if len(params) > 2:
        print "DoStuff params 2"
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
    print "DoStuff({}, {}, matPos)".format(soMaster.getName(), bShow)
    
    # Manipulons les clones
    cloneKeys = PtFindClones(masterKey)
    if len(cloneKeys) < 1:
        print "DoStuff no clone found!"
    else:
        print "DoStuff : the stuff" 
        #use the last clone by default
        ck = cloneKeys[len(cloneKeys) - 1]
        #for ck in cloneKeys:
        soTop = ck.getSceneObject()

        soTop.netForce(1)
        soTop.physics.disable()
        soTop.physics.warp(pos)
        #
        if bShow:
            soTop.draw.enable(1)
        else:
            soTop.draw.enable(0)
        #
        if bPhys:
            soTop.physics.enable(1)
        else:
            soTop.physics.enable(0)

    print "DoStuff done"
    return 0

#
def DoStuff2(params=[]):
    print "DoStuff2 begin"
    
    #Verifions les parametres
    """
    # au moins 6 parametres
    if len(params) > 5:
        print "DoStuff params 5"
        try:
            bAttach = bool(params[5])
        except:
            bAttach = False
    else:
        bAttach = False
    """
    # au moins 5 parametres
    if len(params) > 4:
        print "DoStuff2 params 4"
        try:
            bAttach = bool(params[4])
        except:
            bAttach = False
    else:
        bAttach = False
    # au moins 4 parametres
    if len(params) > 3:
        print "DoStuff2 params 3"
        try:
            bPhys = bool(params[3])
        except:
            bPhys = False
    else:
        bPhys = False
    # au moins 3 parametres
    if len(params) > 2:
        print "DoStuff2 params 2"
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
        print "DoStuff2 params 1"
        try:
            bShow = bool(params[1])
        except:
            bShow = True
    else:
        bShow = True
    # au moins 1 parametre
    if len(params) > 0:
        print "DoStuff2 params 0"
        masterKey = params[0]
        if not isinstance(masterKey, ptKey):
            print "DoStuff2: first paremeter must be a ptKey"
            return 1
    # pas de parametre
    if len(params) == 0:
        print "DoStuff2: needs 1, 2, 3 or 4 paremeters"
        return 1
    
    print "DoStuff2 params ok"
    soMaster = masterKey.getSceneObject()
    print "DoStuff2({}, {}, matPos)".format(soMaster.getName(), bShow)
    
    # Manipulons les clones
    cloneKeys = PtFindClones(masterKey)
    if len(cloneKeys) < 1:
        print "DoStuff2 no clone found!"
    else:
        print "DoStuff2 : the stuff" 
        #use the last clone by default
        ck = cloneKeys[len(cloneKeys) - 1]
        #for ck in cloneKeys:
        soTop = ck.getSceneObject()

        soTop.netForce(1)
        soTop.physics.disable()
        soTop.physics.warp(pos)
        #
        if bShow:
            soTop.draw.enable(1)
        else:
            soTop.draw.enable(0)
        #
        if bPhys:
            soTop.physics.enable(1)
        else:
            soTop.physics.enable(0)
        #
        if bAttach:
            print "Attach"
            Attacher(soTop, PtGetLocalAvatar(), bPhys=True)
        else:
            print "Detach"
            Detacher(soTop, PtGetLocalAvatar())

    print "DoStuff2 done"
    return 0

#=========================================
# Parameters: masterkey, bShow, iCurClone, matPos, bPhys
def PutItHere(params=[]):
    print "PutItHere begin"
    
    #Verifions les parametres
    # au moins 5 parametres
    if len(params) > 4:
        print "PutItHere params 4"
        try:
            bPhys = bool(params[4])
        except:
            bPhys = False
    else:
        bPhys = False
    # au moins 4 parametres
    if len(params) > 3:
        print "PutItHere params 2"
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
        print "PutItHere params 2"
        if isinstance(params[2], int):
            iCurClone = params[2]
        else:
            #par defaut: le premier clone
            iCurClone = 0
    else:
        #par defaut: le premier clone
        iCurClone = 0
    # au moins 2 parametres
    if len(params) > 1:
        print "PutItHere params 1"
        try:
            bShow = bool(params[1])
        except:
            bShow = True
    else:
        bShow = True
    # au moins 1 parametre
    if len(params) > 0:
        print "PutItHere params 0"
        masterKey = params[0]
        if not isinstance(masterKey, ptKey):
            print "PutItHere: first paremeter must be a ptKey"
            return 1
    # pas de parametre
    if len(params) == 0:
        print "PutItHere: needs 1, 2, 3 or 4 paremeters"
        return 1
    
    print "PutItHere params ok"
    soMaster = masterKey.getSceneObject()
    print "PutItHere({}, {}, matPos)".format(soMaster.getName(), bShow)
    
    # Manipulons les clones
    cloneKeys = PtFindClones(masterKey)
    if len(cloneKeys) < 1:
        print "PutItHere no clone found!"
    else:
        print "PutItHere : the stuff" 
        #use the iCurClone-th clone
        ck = cloneKeys[iCurClone]
        soTop = ck.getSceneObject()

        soTop.netForce(1)
        soTop.physics.disable()
        soTop.physics.warp(pos)
        #
        if bShow:
            soTop.draw.enable(1)
        else:
            soTop.draw.enable(0)
        #
        if bPhys:
            soTop.physics.enable(1)
        else:
            soTop.physics.enable(0)

    print "PutItHere done"
    return 0

#=========================================
# Parameters: masterkey, bShow, iCurClone, matPos, bPhys, bAttach, soAvatar
def PutItHere2(params=[]):
    print "PutItHere2 begin"
    
    #Verifions les parametres
    # au moins 7 parametres
    if len(params) > 6:
        print "PutItHere2 params 6"
        if isinstance(params[6], ptSceneobject):
            soAvatar = params[6]
            print "soAvatar is a ptSceneobject"
        else:
            soAvatar = PtGetLocalAvatar()
    else:
        soAvatar = PtGetLocalAvatar()
    print "soAvatar Name={}".format(soAvatar.getName())
    # au moins 6 parametres
    if len(params) > 5:
        print "PutItHere2 params 5"
        try:
            bAttach = bool(params[5])
        except:
            bAttach = False
    else:
        bAttach = False
    print "PutItHere2 : bAttach={}".format(bAttach)
    # au moins 5 parametres
    if len(params) > 4:
        print "PutItHere2 params 4"
        try:
            bPhys = bool(params[4])
        except:
            bPhys = False
    else:
        bPhys = False
    # au moins 4 parametres
    if len(params) > 3:
        print "PutItHere2 params 2"
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
        print "PutItHere2 params 2"
        if isinstance(params[2], int):
            iCurClone = params[2]
        else:
            #par defaut: le premier clone
            iCurClone = 0
    else:
        #par defaut: le premier clone
        iCurClone = 0
    # au moins 2 parametres
    if len(params) > 1:
        print "PutItHere2 params 1"
        try:
            bShow = bool(params[1])
        except:
            bShow = True
    else:
        bShow = True
    # au moins 1 parametre
    if len(params) > 0:
        print "PutItHere2 params 0"
        masterKey = params[0]
        if not isinstance(masterKey, ptKey):
            print "PutItHere: first paremeter must be a ptKey"
            return 1
    # pas de parametre
    if len(params) == 0:
        print "PutItHere2: needs 1 to 6 paremeters"
        return 1
    
    print "PutItHere2 params ok"
    soMaster = masterKey.getSceneObject()
    print "PutItHere2(objName={}, bShow={}, ...)".format(soMaster.getName(), bShow)
    
    # Manipulons les clones
    cloneKeys = PtFindClones(masterKey)
    if len(cloneKeys) < 1:
        print "PutItHere2 no clone found!"
    else:
        print "PutItHere2 : the stuff" 
        #use the iCurClone-th clone
        ck = cloneKeys[iCurClone]
        soTop = ck.getSceneObject()

        soTop.netForce(1)
        soTop.physics.disable()
        soTop.physics.warp(pos)
        #
        if bShow:
            soTop.draw.enable(1)
        else:
            soTop.draw.enable(0)
        #
        if bPhys:
            soTop.physics.enable(1)
        else:
            soTop.physics.enable(0)
        #
        if bAttach:
            print "Attach"
            Attacher(soTop, soAvatar, bPhys=True)
        else:
            print "Detach"
            Detacher(soTop, soAvatar)

    print "PutItHere2 done"
    return 0

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
            PtSetAlarm(1, CloneFactory.AlarmWaittingForClones(objName, age, nb, fct, [masterkey, bShow, matPos, True]), 1)
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
def cloneit2(objName, age, bShow=True, bLoad=True, bAttach=True, scale=ptVector3(1, 1, 1), matPos=None, fct=DoStuff2):
    print "          ** cloneit ** 1 begin"
    print "bAttach={}".format(bAttach)
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
            PtSetAlarm(1, CloneFactory.AlarmWaittingForClones(objName, age, nb, fct, [masterkey, bShow, matPos, True, True]), 1)
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
# Create N clones and put the choosen one somewhere
def CloneThem(objName, age, bShow=True, bLoad=True, iNbClones=10, iCurClone=0, matPos=None, fct=PutItHere):
    print "          ** cloneit ** 1 begin"
    msg = "CloneObject.cloneit(): "
    nb = iNbClones
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
            PtSetAlarm(1, CloneFactory.AlarmWaittingForClones(objName, age, nb, fct, [masterkey, bShow, iCurClone, matPos, True]), 1)
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
# Create N clones and put the choosen one somewhere
def CloneThem2(objName, age, bShow=True, bLoad=True, iNbClones=10, iCurClone=0, matPos=None, fct=PutItHere2, bAttach=True, soAvatar=None):
    print "          ** CloneThem2 ** 1 begin"
    msg = "Columnst.CloneThem2(): "
    nb = iNbClones
    masterkey = None

    try:
        masterkey = PtFindSceneobject(objName, age).getKey()
    except:
        print "{} not found in {}".format(objName, age)
        msg += "{} not found in {}\n".format(objName, age)
    print "          ** CloneThem2 ** 2"
    if isinstance(masterkey, ptKey):
        if bLoad:
            print "          ** CloneThem2 ** 3 loading"
            # Combien de clones a-t-on deja?
            nbClones = len(PtFindClones(masterkey))
            print "Test : nb de clones de {} ==> {}".format(objName, nbClones)
            # Ajouter des clones si besoin
            if nbClones < nb:
                CloneFactory.CloneObject(objName, age, nb - nbClones)
            # Attendre que les clones soient prets et les manipuler
            print "objName={}, age={}, nb={}, fct={}, masterkey={}, bShow={}, iCurClone={}, matPos={}, bPhys={}, bAttach={}, soAvatar={}".format(objName, age, nb, fct, masterkey, bShow, iCurClone, matPos, True, bAttach, soAvatar)
            PtSetAlarm(1, CloneFactory.AlarmWaittingForClones(objName, age, nb, fct, [masterkey, bShow, iCurClone, matPos, True, bAttach, soAvatar]), 1)
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
def CloneOneColumn(objName, age, bOn=True, matAv=None, mTrans=None, fXAngle=0, fYAngle=0, fZAngle=0):
    # verifying parameters:
    # bOn
    if not isinstance(bOn, bool):
        bOn = True
    # avatar's position
    if isinstance(matAv, ptMatrix44):
        mPos = matAv
    elif position is None:
        mPos = PtGetLocalAvatar().getLocalToWorld()
    else:
        print "Rect Error: matAv must be a ptMatrix44"
        return 0
    
    # parameters are set, we can continue
    
    # rotations:
    mRotX = ptMatrix44()
    fXAngle = float(fXAngle) - 90.0
    mRotX.rotate(0, (math.pi * float(fXAngle)) / 180.0)
    mRotY = ptMatrix44()
    mRotY.rotate(1, (math.pi * float(fYAngle)) / 180.0)
    mRotZ = ptMatrix44()
    mRotZ.rotate(2, (math.pi * float(fZAngle)) / 180.0)
    #apply the rotations
    mPos = mPos * mRotZ
    mPos = mPos * mRotY
    mPos = mPos * mRotX
    
    if not isinstance(mTrans, ptMatrix44):
        mTrans = ptMatrix44()
        mTrans.translate(ptVector3(0.0, -3.25, 30.0))
    #apply the translation
    mPos = mPos * mTrans

    ret = cloneit(objName, age, bShow=bOn, bLoad=bOn, matPos=mPos, fct=DoStuff)
    return ret

#
def CloneOneColumn2(objName, age, bOn=True, matAv=None, mTrans=None, fXAngle=0, fYAngle=0, fZAngle=0, bAttach=True):
    # verifying parameters:
    # bOn
    if not isinstance(bOn, bool):
        bOn = True
    # avatar's position
    if isinstance(matAv, ptMatrix44):
        mPos = matAv
    elif position is None:
        mPos = PtGetLocalAvatar().getLocalToWorld()
    else:
        print "Rect Error: matAv must be a ptMatrix44"
        return 0
    
    # parameters are set, we can continue
    
    # rotations:
    mRotX = ptMatrix44()
    fXAngle = float(fXAngle) - 90.0
    mRotX.rotate(0, (math.pi * float(fXAngle)) / 180.0)
    mRotY = ptMatrix44()
    mRotY.rotate(1, (math.pi * float(fYAngle)) / 180.0)
    mRotZ = ptMatrix44()
    mRotZ.rotate(2, (math.pi * float(fZAngle)) / 180.0)
    #apply the rotations
    mPos = mPos * mRotZ
    mPos = mPos * mRotY
    mPos = mPos * mRotX
    
    if not isinstance(mTrans, ptMatrix44):
        mTrans = ptMatrix44()
        mTrans.translate(ptVector3(0.0, -3.25, 30.0))
    #apply the translation
    mPos = mPos * mTrans

    ret = cloneit2(objName, age, bShow=bOn, bLoad=bOn, bAttach=bOn, matPos=mPos, fct=DoStuff2)
    return ret

# Clone iNbCol and put the iCurCol-th one where you want
def CloneColumns(objName, age, bOn=True, iNbCol=10, iCurCol=0, matAv=None, mTrans=None, fXAngle=0, fYAngle=0, fZAngle=0):
    # verifying parameters:
    # bOn
    if not isinstance(bOn, bool):
        bOn = True
    # avatar's position
    if isinstance(matAv, ptMatrix44):
        mPos = matAv
    elif position is None:
        mPos = PtGetLocalAvatar().getLocalToWorld()
    else:
        print "Rect Error: matAv must be a ptMatrix44"
        return 0
    
    # parameters are set, we can continue
    print "objName={}, age={}".format(objName, age)
    print "iCurCol={}, iNbCol={}".format(iCurCol, iNbCol)
    print "fXAngle={}, fYAngle={}, fZAngle={}".format(fXAngle, fYAngle, fZAngle)
    
    # rotations:
    mRotX = ptMatrix44()
    fXAngle = float(fXAngle) - 90.0
    mRotX.rotate(0, (math.pi * float(fXAngle)) / 180.0)
    mRotY = ptMatrix44()
    mRotY.rotate(1, (math.pi * float(fYAngle)) / 180.0)
    mRotZ = ptMatrix44()
    mRotZ.rotate(2, (math.pi * float(fZAngle)) / 180.0)
    #apply the rotations
    mPos = mPos * mRotZ
    mPos = mPos * mRotY
    mPos = mPos * mRotX
    
    if not isinstance(mTrans, ptMatrix44):
        mTrans = ptMatrix44()
        mTrans.translate(ptVector3(0.0, -3.25, 30.0))
    #apply the translation
    mPos = mPos * mTrans

    ret = CloneThem(objName, age, iNbClones=iNbCol, iCurClone=iCurCol, bShow=bOn, bLoad=bOn, matPos=mPos, fct=PutItHere)
    return ret

# Clone iNbCol and put the iCurCol-th one where you want
def CloneColumns2(objName, age, bLoadOn=True, bShowOn=True, iNbCol=10, iCurCol=0, matAv=None, mTrans=None, fXAngle=0, fYAngle=0, fZAngle=0, bAttachOn=True, soAv=None):
    # verifying parameters:
    # bLoadOn
    if not isinstance(bLoadOn, bool):
        bLoadOn = True
    # bShowOn
    if not isinstance(bShowOn, bool):
        bShowOn = True
    # bAttachOn
    if not isinstance(bAttachOn, bool):
        bAttachOn = True
    # avatar's position
    if isinstance(matAv, ptMatrix44):
        mPos = matAv
    elif position is None:
        mPos = PtGetLocalAvatar().getLocalToWorld()
    else:
        print "Rect Error: matAv must be a ptMatrix44"
        return 0
    
    # parameters are set, we can continue
    print "objName={}, age={}".format(objName, age)
    print "iCurCol={}, iNbCol={}".format(iCurCol, iNbCol)
    print "fXAngle={}, fYAngle={}, fZAngle={}".format(fXAngle, fYAngle, fZAngle)
    
    # rotations:
    mRotX = ptMatrix44()
    fXAngle = float(fXAngle) - 90.0
    mRotX.rotate(0, (math.pi * float(fXAngle)) / 180.0)
    mRotY = ptMatrix44()
    mRotY.rotate(1, (math.pi * float(fYAngle)) / 180.0)
    mRotZ = ptMatrix44()
    mRotZ.rotate(2, (math.pi * float(fZAngle)) / 180.0)
    #apply the rotations
    mPos = mPos * mRotZ
    mPos = mPos * mRotY
    mPos = mPos * mRotX
    
    if not isinstance(mTrans, ptMatrix44):
        mTrans = ptMatrix44()
        mTrans.translate(ptVector3(0.0, -3.25, 30.0))
    #apply the translation
    mPos = mPos * mTrans
    
    print "objName={}, age={}, bLoadOn={}, bShowOn={}, iNbCol={}, iCurCol={}, matAv={}, mTrans={}, fXAngle={}, fYAngle={}, fZAngle={}, bAttachOn={}, soAv={}".format(objName, age, bLoadOn, bShowOn, iNbCol, iCurCol, matAv, mTrans, fXAngle, fYAngle, fZAngle, bAttachOn, soAv)

    ret = CloneThem2(objName, age, iNbClones=iNbCol, iCurClone=iCurCol, bShow=bShowOn, bLoad=bLoadOn, matPos=mPos, fct=PutItHere2, bAttach=bAttachOn, soAvatar=soAv)
    return ret

# TestColonneDevantMoi
def TestColonneDevantMoi(bOn=True, fXAngle=0, fYAngle=0, fZAngle=0):
    objName = "columnPhys_24"
    age = "Jalak"
    matAv = PtGetLocalAvatar().getLocalToWorld()
    mTrans = ptMatrix44()
    mTrans.translate(ptVector3(0.0, -3.25, 30.0))    
    ret = CloneOneColumn(objName, age, bOn, matAv, mTrans, fXAngle, fYAngle, fZAngle)
    return ret

# TestColonneSousMoi
def TestColonneSousMoi(bOn=True):
    objName = "columnPhys_23"
    age = "Jalak"
    matAv = PtGetLocalAvatar().getLocalToWorld()
    mTrans = ptMatrix44()
    mTrans.translate(ptVector3(0.0, -3.25, 0.0))    
    ret = CloneOneColumn2(objName, age, bOn, matAv, mTrans, 0, 0, 0, bOn)
    return ret

# Save the couples of (columnNumber, playerID)
nbCol = 10
dicCol = {}
for i in range(0, nbCol):
    dicCol.update({i: 0})
# ColumnUnderPlayer
def ColumnUnderPlayer(bOn=True, player=None):
    global nbCol
    global dicCol
    #objName = "columnPhys_22"
    #age = "Jalak"
    #objName = "bridge"
    ##objName = "bridgeproxy"
    #age = "GreatTreePub"
    #objName = "BenchTmp"
    #age = "Personal"
    #objName = "DesertPlane"
    #age = "Cleft"
    objName = "SmallBarricade02"
    age = "city"
    bIsInAge = False
    playerID = 0
    soAvatar = None
    matAv = ptMatrix44()
    try:
        playerID = player.getPlayerID()
    except:
        print "player not found"
        return 0
    if playerID == PtGetLocalPlayer().getPlayerID():
        soAvatar = PtGetLocalAvatar()
        bIsInAge = True
        print "Player is myself"
    else:
        pass
    agePlayers = PtGetPlayerList()
    ids = map(lambda player: playerID, agePlayers)
    if playerID in ids:
        soAvatar = PtGetAvatarKeyFromClientID(playerID).getSceneObject()
        bIsInAge = True
    else:
        pass
    # search player/column couple
    bPlayerHasColumn = False
    iCurCol = -1
    for k, v in dicCol.iteritems():
        if v == playerID:
            bPlayerHasColumn = True
            iCurCol = k
            if not bIsInAge:
                dicCol[k] = 0
                matAv = ptMatrix44()
            else:
                matAv = soAvatar.getLocalToWorld()
            break
    #if the player has no column yet
    if not bPlayerHasColumn:
        bFreeColumnFound = False
        #find the first free column
        for k, v in dicCol.iteritems():
            if v == 0:
                bFreeColumnFound = True
                iCurCol = k
                dicCol[k] = playerID
                matAv = soAvatar.getLocalToWorld()
                bPlayerHasColumn = True
            break
        
    #soAvatar = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
    #matAv = PtGetLocalAvatar().getLocalToWorld()
    #matAv = soAvatar.getLocalToWorld()
    
    mTrans = ptMatrix44()
    #mTrans.translate(ptVector3(0.0, -3.25, 0.0)) 
    mTrans.translate(ptVector3(0.0, 0, -0.5)) 
    
    #ret = CloneOneColumn2(objName, age, bOn, matAv, mTrans, 0, 0, 0, bOn)
    #ret = CloneColumns(objName, age, bOn, nbCol, iCurCol, matAv, mTrans, 0, 0, 0)
    #ret = CloneColumns2(objName, age, bOn, False, nbCol, iCurCol, matAv, mTrans, 0, 0, 0, bOn, soAvatar)
    ret = CloneColumns2(objName, age, bOn, True, nbCol, iCurCol, matAv, mTrans, 90, 0, 0, bOn, soAvatar)
    return ret

# PutOneColumnInFrontOfPlayer:
# Create one clone of a Jalak column
# Load and show it in front of the player
# With a slope angle (fXAngle in degrees [e.g.: 0=horizontal, 30=montee a 30 degres, -30=descente a 30 degres])
def PutOneColumnInFrontOfPlayer(bOn=True, fXAngle=0.0, soAvatar=None):
    objName = "columnPhys_21"
    age = "Jalak"
    fYAngle = 0.0
    fZAngle = 0.0
    # deplacement a appliquer a la colonne pour q'elle soit devant le joueur
    mTrans = ptMatrix44()
    mTrans.translate(ptVector3(0.0, -3.25, 30.0))
    # matrice de position du joueur
    if soAvatar is None:
        matAv = PtGetLocalAvatar().getLocalToWorld()
    elif isinstance(soAvatar, ptSceneobject):
        matAv = soAvatar.getLocalToWorld()
    else:
        print "PutOneColumnInFrontOfPlayer: soAvatar is not a ptSceneobject"
        return 0
    #
    ret = CloneOneColumn(objName, age, bOn, matAv, mTrans, fXAngle, fYAngle, fZAngle)
    return ret

# Initialize the number of columns and the next column to put it in fromt of you
iNbCol = 10
iCurCol = -1
# PutNextColumnInFrontOfPlayer:
# Create N clones of a Jalak column
# Load and show one of them in front of the player
# With a slope angle (fXAngle in degrees [e.g.: 0=horizontal, 30=montee a 30 degres, -30=descente a 30 degres])
def PutNextColumnInFrontOfPlayer(bOn=True, fXAngle=0.0, soAvatar=None):
    global iNbCol
    global iCurCol
    
    objName = "columnPhys_20"
    age = "Jalak"
    fYAngle = 0.0
    fZAngle = 0.0
    # deplacement a appliquer a la colonne pour q'elle soit devant le joueur
    mTrans = ptMatrix44()
    mTrans.translate(ptVector3(0.0, -3.25, 30.0))
    # matrice de position du joueur
    if soAvatar is None:
        matAv = PtGetLocalAvatar().getLocalToWorld()
    elif isinstance(soAvatar, ptSceneobject):
        matAv = soAvatar.getLocalToWorld()
    else:
        print "PutOneColumnInFrontOfPlayer: soAvatar is not a ptSceneobject"
        return 0
    
    iCurCol = (iCurCol + 1) % iNbCol
    print "iCurCol={}, iNbCol={}".format(iCurCol, iNbCol)
    #
    ret = CloneColumns(objName, age, bOn, iNbCol, iCurCol, matAv, mTrans, fXAngle, fYAngle, fZAngle)
    return ret

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
