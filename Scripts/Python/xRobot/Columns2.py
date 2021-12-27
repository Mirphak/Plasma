# -*- coding: utf-8 -*-
# == Script pour jouer avec les colonnes de Jalak Dador en chargeant le prp ==
# Mirphak 2014-11-07 version 1

from Plasma import *
import math
#import CloneFactory

age = "Jalak"

bJalakAdded = False

def AddPrp():
    global bJalakAdded
    pages = ["jlakArena"]
    for page in pages:
        PtConsoleNet("Nav.PageInNode %s" % (page) , 1)
    bJalakAdded = True

def DelPrp():
    global bJalakAdded
    pages = ["jlakArena"]
    for page in pages:
        PtConsoleNet("Nav.PageOutNode %s" % (page) , 1)
    bJalakAdded = False

def DelPrpLocal():
    global bJalakAdded
    if bJalakAdded:
        pages = ["jlakArena"]
        for page in pages:
            PtPageOutNode(page)
        bJalakAdded = False

# Find scene objects with name like soName in all loaded districts (aka pages or prp files)
# ex.: soName = "Bahro*Stone" will be transformed in regexp "^.*Bahro.*Stone.*$"
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

# Find scene objects with name like soName in all loaded districts of the specified age
def FindSOInAge(soName, ageFileName):
    nameList = FindSOName(soName)
    soList = list()
    for soName in nameList:
        try:
            so = PtFindSceneobject(soName, ageFileName)
            soList.append(so)
        except NameError:
            continue
    return soList

#
def ShowObjectList(age, names=[], bOn = True):
    for name in names:
        #pf = PtFindSceneobjects(name)
        pf = FindSOInAge(name, age)
        for so in pf:
            so.netForce(1)
            so.draw.enable(bOn)

#
def PhysObjectList(age, names=[], bOn = True):
    for name in names:
        #pf = PtFindSceneobjects(name)
        pf = FindSOInAge(name, age)
        for so in pf:
            so.netForce(1)
            try:
                so.physics.enable(bOn)
            except:
                pass

#
def DoNothing(params=[]):
    print "DoNothing (just a default method)"

#
class AlarmAddPrp:
    _nbFois = 0
    _bPrpLoaded = False
    
    #def __init__(self, objectName="columnPhys_00", ageFileName="Jalak", bFirst=False, method=DoNothing, params=[]):
    def __init__(self, objectName="Flag04_Master", ageFileName="Jalak", bFirst=False, method=DoNothing, params=[]):
        print "AlarmAddPrp: init"
        self._objectName = objectName
        self._ageFileName = ageFileName
        self._bPrpLoaded = False
        self._bFirst = bFirst
        self._method = method
        self._params = params
        self._so = PtFindSceneobject(self._objectName, self._ageFileName)
    def onAlarm(self, context):
        if context == 0:
            print "AlarmAddPrp: 0 - AddPrp"
            AddPrp()
            PtSetAlarm(.25, self, 1)
        elif context == 1:
            print "AlarmAddPrp: 1 - Waitting loop"
            try:
                pos = self._so.position()
            except:
                print "err so pos"
                return
            print "pos: {}, {}, {}".format(pos.getX(), pos.getY(), pos.getZ())
            if (pos.getX() == 0 and pos.getY() == 0 and pos.getZ() == 0 and self._nbFois < 20):
                self._nbFois += 1
                print ">>> Attente nb: {}".format(self._nbFois)
                PtSetAlarm(.25, self, 1)
            else:
                if (self._nbFois < 20):
                    self._bPrpLoaded = True
                    PtSetAlarm(0, self, 2)
                else:
                    print "loading prp was too long..."
                    
                self._nbFois = 0
        elif context == 2:
            print "AlarmAddPrp: 2 - The prp is ready"
            if self._bFirst:
                # Hide some objects
                names = ["Bamboo", "Bone", "Distan",
                    "Calendar", "Camera", "FarHills", 
                    "Field", "Flag", "Fog", "Green", 
                    "LightBase", "moss", "Object",  
                    "SkyDome01", "SoftRegionMain", 
                    "Star", "Sun", "Terrain", "Wall0"]
                ShowObjectList(self._ageFileName, names, False)
                # Disable physics for some objects
                names = ["Camera", "Field", "Link"
                    "Start", "Terrain", "Wall0"]
                PhysObjectList(self._ageFileName, names, False)
            self._method(self._params)
        else:
            pass

#
def AddJalak(self, args = []):
    self.chatMgr.AddChatLine(None, "Adding Jalak...", 3)
    try:
        PtSetAlarm (0, AlarmAddPrp(), 0)
        
        self.chatMgr.AddChatLine(None, "Jalak added!", 3)
        return 1
    except:
        self.chatMgr.AddChatLine(None, "Error while adding Jalak.", 3)
        return 0

#=========================================

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
# Parameters: ptSceneobject, bShow, iCurClone, matPos, bPhys
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
        so = params[0]
        if not isinstance(so, ptSceneobject):
            print "PutItHere: first paremeter must be a ptSceneobject"
            return 1
    # pas de parametre
    if len(params) == 0:
        print "PutItHere: needs 1, 2, 3 or 4 paremeters"
        return 1
    
    print "PutItHere params ok"
    #soMaster = masterKey.getSceneObject()
    print "PutItHere({}, {}, matPos)".format(so.getName(), bShow)
    
    # Manipulons l'objet
    """
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
    """
    print "PutItHere : the stuff" 
    so.netForce(1)
    so.physics.disable()
    so.physics.warp(pos)
    #
    if bShow:
        so.draw.enable(1)
    else:
        so.draw.enable(0)
    #
    if bPhys:
        so.physics.enable(1)
    else:
        so.physics.enable(0)

    print "PutItHere done"
    return 0

#=========================================
# Parameters: ptSceneobject, bShow, iCurClone, matPos, bPhys, bAttach, soAvatar
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
        so = params[0]
        if not isinstance(so, ptSceneobject):
            print "PutItHere: first paremeter must be a ptKey"
            return 1
    # pas de parametre
    if len(params) == 0:
        print "PutItHere2: needs 1 to 6 paremeters"
        return 1
    
    print "PutItHere2 params ok"
    #soMaster = masterKey.getSceneObject()
    print "PutItHere2(objName={}, bShow={}, ...)".format(so.getName(), bShow)
    """
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
    """
    so.netForce(1)
    so.physics.disable()
    so.physics.warp(pos)
    #
    if bShow:
        so.draw.enable(1)
    else:
        so.draw.enable(0)
    #
    if bPhys:
        so.physics.enable(1)
    else:
        so.physics.enable(0)
    #
    if bAttach:
        print "Attach"
        Attacher(so, soAvatar, bPhys=True)
    else:
        print "Detach"
        Detacher(so, soAvatar)
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
def CloneThem(objName, age, bShow=True, bLoad=True, iNbClones=10, iCurClone=0, matPos=None, fct=PutItHere, bFirstCol=True):
    print "          ** cloneit ** 1 begin"
    msg = "CloneObject.cloneit(): "
    nb = iNbClones
    so = None

    try:
        so = PtFindSceneobject(objName, age)
    except:
        print "{} not found in {}".format(objName, age)
        msg += "{} not found in {}\n".format(objName, age)
    print "          ** cloneit ** 2"
    if isinstance(so, ptSceneobject):
        if bLoad:
            print "          ** clone1 ** 3 loading"
            ## Combien de clones a-t-on deja?
            #nbClones = len(PtFindClones(masterkey))
            #print "Test : nb de clones de {} ==> {}".format(objName, nbClones)
            ## Ajouter des clones si besoin
            #if nbClones < nb:
            #    CloneFactory.CloneObject(objName, age, nb - nbClones)
            # Attendre que les clones soient prets et les manipuler
            #PtSetAlarm(1, CloneFactory.AlarmWaittingForClones(objName, age, nb, fct, [masterkey, bShow, iCurClone, matPos, True]), 1)
            PtSetAlarm (0, AlarmAddPrp(objectName="columnPhys_00", ageFileName="Jalak", bFirst=bFirstCol, method=fct, params=[so, bShow, iCurClone, matPos, True]), 0)
            print "Clone of {} loaded".format(objName)
            msg += "Clone of {} loaded\n".format(objName)
        else:
            # Retour a la normale
            #CloneFactory.DechargerClones(masterkey)
            #DayTime()
            print "Clone of {} unloaded".format(objName)
            msg += "Clone of {} unloaded\n".format(objName)
    else:
        print "not a ptSceneobject!"
        msg += "not a ptSceneobject\n"
    return msg

#=========================================
# Create N clones and put the choosen one somewhere
def CloneThem2(objName, age, bShow=True, bLoad=True, iNbClones=10, iCurClone=0, matPos=None, fct=PutItHere2, bAttach=True, soAvatar=None, bFirstCol=True):
    print "          ** CloneThem2 ** 1 begin"
    msg = "Columnst.CloneThem2(): "
    nb = iNbClones
    so = None

    try:
        so = PtFindSceneobject(objName, age)
    except:
        print "{} not found in {}".format(objName, age)
        msg += "{} not found in {}\n".format(objName, age)
    print "          ** CloneThem2 ** 2"
    if isinstance(so, ptSceneobject):
        if bLoad:
            print "          ** CloneThem2 ** 3 loading"
            ## Combien de clones a-t-on deja?
            #nbClones = len(PtFindClones(so))
            #print "Test : nb de clones de {} ==> {}".format(objName, nbClones)
            ## Ajouter des clones si besoin
            #if nbClones < nb:
            #    CloneFactory.CloneObject(objName, age, nb - nbClones)
            ## Attendre que les clones soient prets et les manipuler
            print "objName={}, age={}, nb={}, fct={}, so={}, bShow={}, iCurClone={}, matPos={}, bPhys={}, bAttach={}, soAvatar={}".format(objName, age, nb, fct, so, bShow, iCurClone, matPos, True, bAttach, soAvatar)
            #PtSetAlarm(1, CloneFactory.AlarmWaittingForClones(objName, age, nb, fct, [so, bShow, iCurClone, matPos, True, bAttach, soAvatar]), 1)
            PtSetAlarm (0, AlarmAddPrp(objectName="columnPhys_00", ageFileName="Jalak", bFirst=bFirstCol, method=fct, params=[so, bShow, iCurClone, matPos, True, bAttach, soAvatar]), 0)
            print "Clone of {} loaded".format(objName)
            msg += "Clone of {} loaded\n".format(objName)
        else:
            # Retour a la normale
            #CloneFactory.DechargerClones(masterkey)
            #DayTime()
            print "Clone of {} unloaded".format(objName)
            msg += "Clone of {} unloaded\n".format(objName)
    else:
        print "not a ptSceneobject!"
        msg += "not a ptSceneobject\n"
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
def CloneColumns(objName, age, bOn=True, iNbCol=10, iCurCol=0, matAv=None, mTrans=None, fXAngle=0, fYAngle=0, fZAngle=0, bFirstCol=True, bFirst=True):
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

    ret = CloneThem(objName, age, iNbClones=iNbCol, iCurClone=iCurCol, bShow=bOn, bLoad=bOn, matPos=mPos, fct=PutItHere, bFirstCol=bFirst)
    return ret

# Clone iNbCol and put the iCurCol-th one where you want
def CloneColumns2(objName, age, bLoadOn=True, bShowOn=True, iNbCol=10, iCurCol=0, matAv=None, mTrans=None, fXAngle=0, fYAngle=0, fZAngle=0, bAttachOn=True, soAv=None, bFirst=True):
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

    #ret = CloneThem2(objName, age, iNbClones=iNbCol, iCurClone=iCurCol, bShow=bShowOn, bLoad=bLoadOn, matPos=mPos, fct=PutItHere2, bAttach=bAttachOn, soAvatar=soAv)
    ret = CloneThem2(objName, age, iNbClones=iNbCol, iCurClone=iCurCol, bShow=False, bLoad=bLoadOn, matPos=mPos, fct=PutItHere2, bAttach=bAttachOn, soAvatar=soAv, bFirstCol=bFirst)
    return 1
    #return ret

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
def TestColonneSousMoi(n=23, bOn=True):
    #objName = "columnPhys_23"
    objName = "columnPhys_" + str(n)
    age = "Jalak"
    matAv = PtGetLocalAvatar().getLocalToWorld()
    mTrans = ptMatrix44()
    mTrans.translate(ptVector3(0.0, -3.25, 0.0))    
    #ret = CloneOneColumn2(objName, age, bOn, matAv, mTrans, 0, 0, 0, bOn)
    ret = CloneColumns(objName, age, bOn, iNbCol, iCurCol, matAv, mTrans, fXAngle, fYAngle, fZAngle, True)
    return ret

# Save the couples of (columnNumber, playerID)
nbCol = 25
dicCol = {}
for i in range(0, nbCol):
    dicCol.update({i: 0})

# ColumnUnderPlayer
def ColumnUnderPlayer(bOn=True, bShow=True, player=None):
    global nbCol
    global dicCol
    objNameBase = "columnPhys_"
    age = "Jalak"
    bIsInAge = False
    playerID = 0
    soAvatar = None
    matAv = ptMatrix44()
    bFirstCol = False
    try:
        playerID = player.getPlayerID()
    except:
        print "player not found"
        return 1
    if playerID == PtGetLocalPlayer().getPlayerID():
        soAvatar = PtGetLocalAvatar()
        bIsInAge = True
        print "Player is myself"
    else:
        #pass
        agePlayers = PtGetPlayerList()
        ids = map(lambda player: playerID, agePlayers)
        if playerID in ids:
            playerKey = PtGetAvatarKeyFromClientID(playerID)
            if isinstance(playerKey, ptKey):
                soAvatar = playerKey.getSceneObject()
                bIsInAge = True
                print "{} is in current age!".format(player.getPlayerName())
            else:
                print "{} not found in current age!".format(player.getPlayerName())
        else:
            print "{} is not in current age.".format(player.getPlayerName())
            return 1
    # search player/column couple
    bPlayerHasColumn = False
    iCurCol = -1
    for k, v in dicCol.iteritems():
        if v == playerID:
            bPlayerHasColumn = True
            print "{} has column #{}".format(player.getPlayerName(), k)
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
        print "{} has no column yet, searching a free one ...".format(player.getPlayerName())
        #find the first free column
        for k, v in dicCol.iteritems():
            if v == 0:
                bFreeColumnFound = True
                print "column #{} is free".format(k)
                iCurCol = k
                dicCol[k] = playerID
                matAv = soAvatar.getLocalToWorld()
                bPlayerHasColumn = True
                bFirstCol = True
                break
            else:
                print "column #{} taken by {}".format(k, v)
        
    #soAvatar = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
    #matAv = PtGetLocalAvatar().getLocalToWorld()
    #matAv = soAvatar.getLocalToWorld()
    
    mTrans = ptMatrix44()
    mTrans.translate(ptVector3(0.0, -3.25, 0.0)) 
    #mTrans.translate(ptVector3(0.0, -3.26, 0.0)) 
    #mTrans.translate(ptVector3(0.0, 0, -0.5)) 
    
    #iCurCol = (iCurCol + 1) % iNbCol
    print "iCurCol={}, iNbCol={}".format(iCurCol, iNbCol)
    objName = objNameBase + str(iCurCol).zfill(2)
    
    #ret = CloneOneColumn2(objName, age, bOn, matAv, mTrans, 0, 0, 0, bOn)
    #ret = CloneColumns(objName, age, bOn, nbCol, iCurCol, matAv, mTrans, 0, 0, 0)
    ret = CloneColumns2(objName, age, bOn, bShow, nbCol, iCurCol, matAv, mTrans, 0, 0, 0, bOn, soAvatar, bFirstCol)
    #ret = CloneColumns2(objName, age, bOn, True, nbCol, iCurCol, matAv, mTrans, 90, 0, 0, bOn, soAvatar)
    #return ret
    return 1

# ColumnUnderPlayer2
def ColumnUnderPlayer2(bOn=True, bShow=True, player=None, fXAngle=0.0, fYAngle=0.0, fZAngle=0.0, bAttach=True, h=0.0):
    global nbCol
    global dicCol
    objNameBase = "columnPhys_"
    age = "Jalak"
    bIsInAge = False
    playerID = 0
    soAvatar = None
    matAv = ptMatrix44()
    bFirstCol = False
    try:
        playerID = player.getPlayerID()
    except:
        print "player not found"
        return 1
    if playerID == PtGetLocalPlayer().getPlayerID():
        soAvatar = PtGetLocalAvatar()
        bIsInAge = True
        print "Player is myself"
    else:
        #pass
        agePlayers = PtGetPlayerList()
        ids = map(lambda player: playerID, agePlayers)
        if playerID in ids:
            playerKey = PtGetAvatarKeyFromClientID(playerID)
            if isinstance(playerKey, ptKey):
                soAvatar = playerKey.getSceneObject()
                bIsInAge = True
                print "{} is in current age!".format(player.getPlayerName())
            else:
                print "{} not found in current age!".format(player.getPlayerName())
        else:
            print "{} is not in current age.".format(player.getPlayerName())
            return 1
    # search player/column couple
    bPlayerHasColumn = False
    iCurCol = -1
    for k, v in dicCol.iteritems():
        if v == playerID:
            bPlayerHasColumn = True
            print "{} has column #{}".format(player.getPlayerName(), k)
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
        print "{} has no column yet, searching a free one ...".format(player.getPlayerName())
        #find the first free column
        for k, v in dicCol.iteritems():
            if v == 0:
                bFreeColumnFound = True
                print "column #{} is free".format(k)
                iCurCol = k
                dicCol[k] = playerID
                matAv = soAvatar.getLocalToWorld()
                bPlayerHasColumn = True
                bFirstCol = True
                break
            else:
                print "column #{} taken by {}".format(k, v)
    
    # height correction
    height = 0.26 * abs(math.tan(fXAngle * math.pi / 180.0))
    if height > 1.0:
        height = 1.0
    height = height + h
    
    mTrans = ptMatrix44()
    #mTrans.translate(ptVector3(0.0, -3.25, 0.0)) # avatar a la surface de la colonne si horizontale
    #mTrans.translate(ptVector3(0.0, -3.40, -28.0)) # avatar a la surface de la colonne si fXAngle = 30
    #mTrans.translate(ptVector3(0.0, -3.35, -28.0)) # compromis acceptable
    mTrans.translate(ptVector3(0.0, -3.25 - height, -28.0))
    
    print "iCurCol={}, iNbCol={}".format(iCurCol, iNbCol)
    objName = objNameBase + str(iCurCol).zfill(2)
    print "ColumnUnderPlayer2 : angles = [{}, {}, {}]".format(fXAngle, fYAngle, fZAngle)
    ret = CloneColumns2(objName, age, bOn, bShow, nbCol, iCurCol, matAv, mTrans, fXAngle, fYAngle, fZAngle, bAttach, soAvatar, bFirstCol)
    return 1

# ColumnInFrontOfPlayer
# With a slope angle (fXAngle in degrees [e.g.: 0=horizontal, 30=montee a 30 degres, -30=descente a 30 degres])
def ColumnInFrontOfPlayer(bOn=True, fXAngle=0.0, player=None):
    global nbCol
    global dicCol
    objNameBase = "columnPhys_"
    age = "Jalak"
    bIsInAge = False
    playerID = 0
    soAvatar = None
    matAv = ptMatrix44()
    bFirstCol = False
    try:
        playerID = player.getPlayerID()
    except:
        print "player not found"
        return 1
    if playerID == PtGetLocalPlayer().getPlayerID():
        soAvatar = PtGetLocalAvatar()
        bIsInAge = True
        print "Player is myself"
    else:
        #pass
        agePlayers = PtGetPlayerList()
        ids = map(lambda player: playerID, agePlayers)
        if playerID in ids:
            playerKey = PtGetAvatarKeyFromClientID(playerID)
            if isinstance(playerKey, ptKey):
                soAvatar = playerKey.getSceneObject()
                bIsInAge = True
                print "{} is in current age!".format(player.getPlayerName())
            else:
                print "{} not found in current age!".format(player.getPlayerName())
        else:
            print "{} is not in current age.".format(player.getPlayerName())
            return 1
    # search player/column couple
    bPlayerHasColumn = False
    iCurCol = -1
    for k, v in dicCol.iteritems():
        if v == playerID:
            bPlayerHasColumn = True
            print "{} has column #{}".format(player.getPlayerName(), k)
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
        print "{} has no column yet, searching a free one ...".format(player.getPlayerName())
        #find the first free column
        for k, v in dicCol.iteritems():
            if v == 0:
                bFreeColumnFound = True
                print "column #{} is free".format(k)
                iCurCol = k
                dicCol[k] = playerID
                matAv = soAvatar.getLocalToWorld()
                bPlayerHasColumn = True
                bFirstCol = True
                break
            else:
                print "column #{} taken by {}".format(k, v)
    
    mTrans = ptMatrix44()
    #mTrans.translate(ptVector3(0.0, -3.25, 30.0)) 
    mTrans.translate(ptVector3(0.0, -3.25, 28.0)) 
    
    print "iCurCol={}, iNbCol={}".format(iCurCol, iNbCol)
    objName = objNameBase + str(iCurCol).zfill(2)
    
    #ret = CloneColumns2(objName, age, bOn, bShow, nbCol, iCurCol, matAv, mTrans, 0, 0, 0, bOn, soAvatar)
    #ret = CloneOneColumn(objName, age, bOn, matAv, mTrans, fXAngle, fYAngle, fZAngle)
    ret = CloneColumns2(objName, age, bOn, False, nbCol, iCurCol, matAv, mTrans, fXAngle, 0.0, 0.0, False, soAvatar, bFirstCol)
    #return ret
    return 1

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

# Initialize the number of columns and the next column to put it in front of you
iNbCol = 25
iCurCol = -1
# PutNextColumnInFrontOfPlayer:
# Create N clones of a Jalak column
# Load and show one of them in front of the player
# With a slope angle (fXAngle in degrees [e.g.: 0=horizontal, 30=montee a 30 degres, -30=descente a 30 degres])
def PutNextColumnInFrontOfPlayer(bOn=True, fXAngle=0.0, soAvatar=None):
    global iNbCol
    global iCurCol
    
    objNameBase = "columnPhys_"
    age = "Jalak"
    fYAngle = 0.0
    fZAngle = 0.0
    # deplacement a appliquer a la colonne pour q'elle soit devant le joueur
    mTrans = ptMatrix44()
    #mTrans.translate(ptVector3(0.0, -3.25, 30.0))
    mTrans.translate(ptVector3(0.0, -3.25, 29.0))
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
    objName = objNameBase + str(iCurCol).zfill(2)
    #
    ret = CloneColumns(objName, age, bOn, iNbCol, iCurCol, matAv, mTrans, fXAngle, fYAngle, fZAngle, True)
    return ret

# ColumnUnderPlayer
def ColumnUnderMe(n=0, bLoadJalak=False):
    global nbCol
    global dicCol
    objNameBase = "columnPhys_"
    age = "Jalak"
    bIsInAge = False
    playerID = 0
    soAvatar = None
    matAv = ptMatrix44()
    bFirstCol = False
    playerID = PtGetLocalPlayer().getPlayerID()
    soAvatar = PtGetLocalAvatar()
    bIsInAge = True
    print "Player is myself"

    # search player/column couple
    bPlayerHasColumn = False
    iCurCol = n
    matAv = soAvatar.getLocalToWorld()
    """
    #if the player has no column yet
    if not bPlayerHasColumn:
        bFreeColumnFound = False
        print "{} has no column yet, searching a free one ...".format(player.getPlayerName())
        #find the first free column
        for k, v in dicCol.iteritems():
            if v == 0:
                bFreeColumnFound = True
                print "column #{} is free".format(k)
                iCurCol = k
                dicCol[k] = playerID
                matAv = soAvatar.getLocalToWorld()
                bPlayerHasColumn = True
                bFirstCol = True
                break
            else:
                print "column #{} taken by {}".format(k, v)
    """
    #soAvatar = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
    #matAv = PtGetLocalAvatar().getLocalToWorld()
    #matAv = soAvatar.getLocalToWorld()
    
    mTrans = ptMatrix44()
    mTrans.translate(ptVector3(0.0, -3.25, 0.0)) 
    #mTrans.translate(ptVector3(0.0, -3.26, 0.0)) 
    #mTrans.translate(ptVector3(0.0, 0, -0.5)) 
    
    #iCurCol = (iCurCol + 1) % iNbCol
    print "iCurCol={}, iNbCol={}".format(iCurCol, iNbCol)
    objName = objNameBase + str(iCurCol).zfill(2)
    
    #ret = CloneOneColumn2(objName, age, bOn, matAv, mTrans, 0, 0, 0, bOn)
    #ret = CloneColumns(objName, age, bOn, nbCol, iCurCol, matAv, mTrans, 0, 0, 0)
    ret = CloneColumns2(objName, age, True, True, nbCol, iCurCol, matAv, mTrans, 0, 0, 0, False, soAvatar, bLoadJalak)
    #ret = CloneColumns2(objName, age, bOn, True, nbCol, iCurCol, matAv, mTrans, 90, 0, 0, bOn, soAvatar)
    #return ret
    return 1

