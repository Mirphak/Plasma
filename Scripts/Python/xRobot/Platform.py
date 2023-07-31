# -*- coding: utf-8 -*-
# == Script pour faire une plateforme avec les colonnes de Jalak Dador en chargeant le prp ==
# Mirphak 2015-11-01 version 1

from Plasma import *
from PlasmaKITypes import *
import math

age = "Jalak"
bJalakAdded = False

"""
# A Teledahn:
# - Montagne, cascade, soleil : -1188 -1138 221
# - Sommet Shroom : -78 -179 159
"""

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
        nameList.extend([so.getName() for so in PtFindSceneobjects(str)])
    nameList = list(set(nameList))
    nameList = [x for x in nameList if pattern.match(x) != None]
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
    print("DoNothing (just a default method)")

#
class AlarmAddPrp:
    _nbFois = 0
    _bPrpLoaded = False
    
    def __init__(self, objectName="columnPhys_00", ageFileName="Jalak", bFirst=False, method=DoNothing, params=[]):
        print("AlarmAddPrp: init")
        self._objectName = objectName
        self._ageFileName = ageFileName
        self._bPrpLoaded = False
        self._bFirst = bFirst
        self._method = method
        self._params = params
        self._so = PtFindSceneobject(self._objectName, self._ageFileName)
    def onAlarm(self, context):
        if context == 0:
            print("AlarmAddPrp: 0 - AddPrp")
            AddPrp()
            PhysObjectList(self._ageFileName, ["PanicLinkRgn"], False)
            PtSetAlarm(.25, self, 1)
        elif context == 1:
            print("AlarmAddPrp: 1 - Waitting loop")
            PhysObjectList(self._ageFileName, ["PanicLinkRgn"], False)
            try:
                pos = self._so.position()
            except:
                print("err so pos")
                return
            print("pos: {}, {}, {}".format(pos.getX(), pos.getY(), pos.getZ()))
            if (pos.getX() == 0 and pos.getY() == 0 and pos.getZ() == 0 and self._nbFois < 20):
                self._nbFois += 1
                print(">>> Attente nb: {}".format(self._nbFois))
                PtSetAlarm(.25, self, 1)
            else:
                if (self._nbFois < 20):
                    self._bPrpLoaded = True
                    #PtSetAlarm(0, self, 2)
                    PtSetAlarm(.25, self, 2)
                else:
                    print("loading prp was too long...")
                    
                self._nbFois = 0
        elif context == 2:
            print("AlarmAddPrp: 2 - The prp is ready")
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
                PtSetAlarm(5, self, 3)
            else:
                PtSetAlarm(.25, self, 3)
        elif context == 3:
            print("AlarmAddPrp: 3 - Execute the method")
            self._method(self._params)
        else:
            pass

# en cas de besoin
def HideJalak():
    # Hide some objects
    names = ["Bamboo", "Bone", "Distan",
        "Calendar", "Camera", "FarHills", 
        "Field", "Flag", "Fog", "Green", 
        "LightBase", "moss", "Object",  
        "SkyDome01", "SoftRegionMain", 
        "Star", "Sun", "Terrain", "Wall0"]
    ShowObjectList("Jalak", names, False)
    # Disable physics for some objects
    names = ["Panic", "Camera", "Field", "Link"
        "Start", "Terrain", "Wall0"]
    PhysObjectList("Jalak", names, False)

#
def AddJalak(self, args = []):
    PtSendKIMessage(kKILocalChatStatusMsg, "Adding Jalak...")
    try:
        PtSetAlarm (0, AlarmAddPrp(), 0)
        PtSendKIMessage(kKILocalChatStatusMsg, "Jalak added!")
        return 1
    except:
        PtSendKIMessage(kKILocalChatErrorMsg, "Error while adding Jalak.")
        return 0

#=========================================
#attacher so1 a so2 : attacher(obj, av) ou l'inverse    
def Attacher(so1, so2, bPhys=False):
    """attacher so1 à so2 : attacher(obj, av) ou l'inverse"""
    so1.physics.netForce(1)
    so1.draw.netForce(1)
    PtAttachObject(so1, so2, 1)

#=========================================
# detacher so1 de so2 : detach(obj, av) ou l'inverse    
def Detacher(so1, so2):
    so1.physics.netForce(1)
    so1.draw.netForce(1)
    PtDetachObject(so1, so2, 1)

#=========================================
# Parameters: ptSceneobject, bShow, iCurClone, matPos, bPhys, bAttach, soAvatar
def PutItHere2(params=[]):
    print("PutItHere2 begin")
    
    #Verifions les parametres
    # au moins 7 parametres
    if len(params) > 6:
        print("PutItHere2 params 6")
        if isinstance(params[6], ptSceneobject):
            soAvatar = params[6]
            print("soAvatar is a ptSceneobject")
        else:
            soAvatar = PtGetLocalAvatar()
    else:
        soAvatar = PtGetLocalAvatar()
    print("soAvatar Name={}".format(soAvatar.getName()))
    # au moins 6 parametres
    if len(params) > 5:
        print("PutItHere2 params 5")
        try:
            bAttach = bool(params[5])
        except:
            bAttach = False
    else:
        bAttach = False
    print("PutItHere2 : bAttach={}".format(bAttach))
    # au moins 5 parametres
    if len(params) > 4:
        print("PutItHere2 params 4")
        try:
            bPhys = bool(params[4])
        except:
            bPhys = False
    else:
        bPhys = False
    # au moins 4 parametres
    if len(params) > 3:
        print("PutItHere2 params 2")
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
        print("PutItHere2 params 2")
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
        print("PutItHere2 params 1")
        try:
            bShow = bool(params[1])
        except:
            bShow = True
    else:
        bShow = True
    # au moins 1 parametre
    if len(params) > 0:
        print("PutItHere2 params 0")
        so = params[0]
        if not isinstance(so, ptSceneobject):
            print("PutItHere: first paremeter must be a ptKey")
            return 1
    # pas de parametre
    if len(params) == 0:
        print("PutItHere2: needs 1 to 6 paremeters")
        return 1
    
    print("PutItHere2 params ok")
    #soMaster = masterKey.getSceneObject()
    print("PutItHere2(objName={}, bShow={}, ...)".format(so.getName(), bShow))

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
        print("Attach")
        Attacher(so, soAvatar, bPhys=True)
    else:
        print("Detach")
        Detacher(so, soAvatar)
    print("PutItHere2 done")
    return 0

#=========================================
# Create N clones and put the choosen one somewhere
def CloneThem2(objName, age, bShow=True, bLoad=True, iNbClones=10, iCurClone=0, matPos=None, fct=PutItHere2, bAttach=True, soAvatar=None, bFirstCol=True):
    print("          ** CloneThem2 ** 1 begin")
    msg = "Columnst.CloneThem2(): "
    nb = iNbClones
    so = None

    try:
        so = PtFindSceneobject(objName, age)
    except:
        print("{} not found in {}".format(objName, age))
        msg += "{} not found in {}\n".format(objName, age)
    print("          ** CloneThem2 ** 2")
    if isinstance(so, ptSceneobject):
        if bLoad:
            print("          ** CloneThem2 ** 3 loading")
            ## Attendre que les clones soient prets et les manipuler
            print("objName={}, age={}, nb={}, fct={}, so={}, bShow={}, iCurClone={}, matPos={}, bPhys={}, bAttach={}, soAvatar={}".format(objName, age, nb, fct, so, bShow, iCurClone, matPos, True, bAttach, soAvatar))
            PtSetAlarm (0, AlarmAddPrp(objectName="columnPhys_00", ageFileName="Jalak", bFirst=bFirstCol, method=fct, params=[so, bShow, iCurClone, matPos, True, bAttach, soAvatar]), 0)
            print("Clone of {} loaded".format(objName))
            msg += "Clone of {} loaded\n".format(objName)
        else:
            # Retour a la normale
            print("Clone of {} unloaded".format(objName))
            msg += "Clone of {} unloaded\n".format(objName)
    else:
        print("not a ptSceneobject!")
        msg += "not a ptSceneobject\n"
    return msg

#=========================================
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
        print("Rect Error: matAv must be a ptMatrix44")
        return 0
    
    # parameters are set, we can continue
    print("objName={}, age={}".format(objName, age))
    print("iCurCol={}, iNbCol={}".format(iCurCol, iNbCol))
    print("fXAngle={}, fYAngle={}, fZAngle={}".format(fXAngle, fYAngle, fZAngle))
    
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
    
    print("objName={}, age={}, bLoadOn={}, bShowOn={}, iNbCol={}, iCurCol={}, matAv={}, mTrans={}, fXAngle={}, fYAngle={}, fZAngle={}, bAttachOn={}, soAv={}".format(objName, age, bLoadOn, bShowOn, iNbCol, iCurCol, matAv, mTrans, fXAngle, fYAngle, fZAngle, bAttachOn, soAv))

    #ret = CloneThem2(objName, age, iNbClones=iNbCol, iCurClone=iCurCol, bShow=bShowOn, bLoad=bLoadOn, matPos=mPos, fct=PutItHere2, bAttach=bAttachOn, soAvatar=soAv)
    ret = CloneThem2(objName, age, iNbClones=iNbCol, iCurClone=iCurCol, bShow=False, bLoad=bLoadOn, matPos=mPos, fct=PutItHere2, bAttach=bAttachOn, soAvatar=soAv, bFirstCol=bFirst)
    return 1
    #return ret

"""
    #=========================================
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
"""

#=========================================
# CreatePlatform : Create a platform under me with 8 columns of Jalak (mixo)
#def CreatePlatform(bShow=False, matAv=None):
def CreatePlatform(bShow=False, matAv=None):
    #global nbCol
    #global dicCol
    objNameBase = "columnPhys_"
    ageName = "Jalak"
    #bIsInAge = False
    #playerID = 0
    #soAvatar = None
    #matAv = ptMatrix44()
    #bFirstCol = False
    playerID = PtGetLocalPlayer().getPlayerID()
    soAvatar = PtGetLocalAvatar()
    #bIsInAge = True
    print("Player is myself")

    # Initialization
    curCol = 25
    # avatar's position
    #matAvatar = soAvatar.getLocalToWorld()
    if isinstance(matAv, ptMatrix44):
        matAvatar = matAv
    else:
        matAvatar = soAvatar.getLocalToWorld()
    
    """
    matTrans = ptMatrix44()
    #                            X    Z      Y
    matTrans.translate(ptVector3(0.0, -3.25, 0.0)) 
    
    #iCurCol = (iCurCol + 1) % iNbCol
    #print "iCurCol={}, iNbCol={}".format(iCurCol, iNbCol)
    objectName = objNameBase + str(iCurCol).zfill(2)
    
    #CloneColumns2(objName, age, bLoadOn=True, bShowOn=True, iNbCol=10, iCurCol=0, matAv=None, mTrans=None, fXAngle=0, fYAngle=0, fZAngle=0, bAttachOn=True, soAv=None, bFirst=True)
    ret = CloneColumns2(objName=objectName, age=ageName, bLoadOn=True, bShowOn=True, iNbCol=0, iCurCol=curCol, matAv=matAvatar, mTrans=matTrans, fXAngle=0, fYAngle=0, fZAngle=0, bAttachOn=False, soAv=soAvatar, bFirst=True)
    """
    
    #
    curCol = curCol - 1
    matTrans = ptMatrix44()
    matTrans.translate(ptVector3(33.75, 4.25, 0.0)) 
    objectName = objNameBase + str(curCol).zfill(2)
    ret = CloneColumns2(objName=objectName, age=ageName, bLoadOn=True, bShowOn=bShow, iNbCol=0, iCurCol=curCol, matAv=matAvatar, mTrans=matTrans, fXAngle=0, fYAngle=0, fZAngle=0, bAttachOn=False, soAv=soAvatar, bFirst=True)
    #
    curCol = curCol - 1
    matTrans = ptMatrix44()
    matTrans.translate(ptVector3(26.25, -3.25, 0.0)) 
    objectName = objNameBase + str(curCol).zfill(2)
    ret = CloneColumns2(objName=objectName, age=ageName, bLoadOn=True, bShowOn=bShow, iNbCol=0, iCurCol=curCol, matAv=matAvatar, mTrans=matTrans, fXAngle=0, fYAngle=0, fZAngle=0, bAttachOn=False, soAv=soAvatar, bFirst=False)
    #
    curCol = curCol - 1
    matTrans = ptMatrix44()
    matTrans.translate(ptVector3(18.75, -3.25, 0.0)) 
    objectName = objNameBase + str(curCol).zfill(2)
    ret = CloneColumns2(objName=objectName, age=ageName, bLoadOn=True, bShowOn=bShow, iNbCol=0, iCurCol=curCol, matAv=matAvatar, mTrans=matTrans, fXAngle=0, fYAngle=0, fZAngle=0, bAttachOn=False, soAv=soAvatar, bFirst=False)
    #
    curCol = curCol - 1
    matTrans = ptMatrix44()
    matTrans.translate(ptVector3(11.25, -3.25, 0.0)) 
    objectName = objNameBase + str(curCol).zfill(2)
    ret = CloneColumns2(objName=objectName, age=ageName, bLoadOn=True, bShowOn=bShow, iNbCol=0, iCurCol=curCol, matAv=matAvatar, mTrans=matTrans, fXAngle=0, fYAngle=0, fZAngle=0, bAttachOn=False, soAv=soAvatar, bFirst=False)
    #
    curCol = curCol - 1
    matTrans = ptMatrix44()
    matTrans.translate(ptVector3(3.75, -3.25, 0.0)) 
    objectName = objNameBase + str(curCol).zfill(2)
    ret = CloneColumns2(objName=objectName, age=ageName, bLoadOn=True, bShowOn=bShow, iNbCol=0, iCurCol=curCol, matAv=matAvatar, mTrans=matTrans, fXAngle=0, fYAngle=0, fZAngle=0, bAttachOn=False, soAv=soAvatar, bFirst=False)
    #
    curCol = curCol - 1
    matTrans = ptMatrix44()
    matTrans.translate(ptVector3(-3.75, -3.25, 0.0)) 
    objectName = objNameBase + str(curCol).zfill(2)
    ret = CloneColumns2(objName=objectName, age=ageName, bLoadOn=True, bShowOn=bShow, iNbCol=0, iCurCol=curCol, matAv=matAvatar, mTrans=matTrans, fXAngle=0, fYAngle=0, fZAngle=0, bAttachOn=False, soAv=soAvatar, bFirst=False)
    #
    curCol = curCol - 1
    matTrans = ptMatrix44()
    matTrans.translate(ptVector3(-11.25, -3.25, 0.0)) 
    objectName = objNameBase + str(curCol).zfill(2)
    ret = CloneColumns2(objName=objectName, age=ageName, bLoadOn=True, bShowOn=bShow, iNbCol=0, iCurCol=curCol, matAv=matAvatar, mTrans=matTrans, fXAngle=0, fYAngle=0, fZAngle=0, bAttachOn=False, soAv=soAvatar, bFirst=False)
    #
    curCol = curCol - 1
    matTrans = ptMatrix44()
    matTrans.translate(ptVector3(-18.75, -3.25, 0.0)) 
    objectName = objNameBase + str(curCol).zfill(2)
    ret = CloneColumns2(objName=objectName, age=ageName, bLoadOn=True, bShowOn=bShow, iNbCol=0, iCurCol=curCol, matAv=matAvatar, mTrans=matTrans, fXAngle=0, fYAngle=0, fZAngle=0, bAttachOn=False, soAv=soAvatar, bFirst=False)
    #
    curCol = curCol - 1
    matTrans = ptMatrix44()
    matTrans.translate(ptVector3(-26.25, -3.25, 0.0)) 
    objectName = objNameBase + str(curCol).zfill(2)
    ret = CloneColumns2(objName=objectName, age=ageName, bLoadOn=True, bShowOn=bShow, iNbCol=0, iCurCol=curCol, matAv=matAvatar, mTrans=matTrans, fXAngle=0, fYAngle=0, fZAngle=0, bAttachOn=False, soAv=soAvatar, bFirst=False)
    #
    curCol = curCol - 1
    matTrans = ptMatrix44()
    matTrans.translate(ptVector3(-33.75, 4.25, 0.0)) 
    objectName = objNameBase + str(curCol).zfill(2)
    ret = CloneColumns2(objName=objectName, age=ageName, bLoadOn=True, bShowOn=bShow, iNbCol=0, iCurCol=curCol, matAv=matAvatar, mTrans=matTrans, fXAngle=0, fYAngle=0, fZAngle=0, bAttachOn=False, soAv=soAvatar, bFirst=False)
    #
    curCol = curCol - 1
    matTrans = ptMatrix44()
    matTrans.translate(ptVector3(33.75, 4.25, 0.0)) 
    objectName = objNameBase + str(curCol).zfill(2)
    ret = CloneColumns2(objName=objectName, age=ageName, bLoadOn=True, bShowOn=bShow, iNbCol=0, iCurCol=curCol, matAv=matAvatar, mTrans=matTrans, fXAngle=0, fYAngle=0, fZAngle=90, bAttachOn=False, soAv=soAvatar, bFirst=False)
    #
    curCol = curCol - 1
    matTrans = ptMatrix44()
    matTrans.translate(ptVector3(-33.75, 4.25, 0.0)) 
    objectName = objNameBase + str(curCol).zfill(2)
    ret = CloneColumns2(objName=objectName, age=ageName, bLoadOn=True, bShowOn=bShow, iNbCol=0, iCurCol=curCol, matAv=matAvatar, mTrans=matTrans, fXAngle=0, fYAngle=0, fZAngle=90, bAttachOn=False, soAv=soAvatar, bFirst=True)
    
    #return ret
    return 1


#=========================================
# CreatePlatformSpy : Create a platform under me with 8 columns of Jalak (mixo)
#def CreatePlatform(bShow=False, matAv=None):
def CreatePlatformSpy(bShow=False, matAv=None):
    objNameBase = "columnPhys_"
    ageName = "Jalak"

    playerID = PtGetLocalPlayer().getPlayerID()
    soAvatar = PtGetLocalAvatar()
    print("Player is myself")

    # Initialization
    curCol = 25
    # avatar's position
    if isinstance(matAv, ptMatrix44):
        matAvatar = matAv
    else:
        matAvatar = soAvatar.getLocalToWorld()
        
    #
    curCol = curCol - 1
    matTrans = ptMatrix44()
    #matTrans.translate(ptVector3(26.25, -3.25, 0.0)) 
    #matTrans.translate(ptVector3(32.00, 15.00, 0.0)) 
    #matTrans.translate(ptVector3(21.53, 10.00, 0.0)) 
    matTrans.translate(ptVector3(22.00, 10.00, 0.0)) 
    objectName = objNameBase + str(curCol).zfill(2)
    ret = CloneColumns2(objName=objectName, age=ageName, bLoadOn=True, bShowOn=bShow, iNbCol=0, iCurCol=curCol, matAv=matAvatar, mTrans=matTrans, fXAngle=0, fYAngle=35, fZAngle=0, bAttachOn=False, soAv=soAvatar, bFirst=False)
    #
    curCol = curCol - 1
    matTrans = ptMatrix44()
    matTrans.translate(ptVector3(18.75, -3.25, 0.0)) 
    objectName = objNameBase + str(curCol).zfill(2)
    ret = CloneColumns2(objName=objectName, age=ageName, bLoadOn=True, bShowOn=bShow, iNbCol=0, iCurCol=curCol, matAv=matAvatar, mTrans=matTrans, fXAngle=0, fYAngle=0, fZAngle=0, bAttachOn=False, soAv=soAvatar, bFirst=False)
    #
    curCol = curCol - 1
    matTrans = ptMatrix44()
    matTrans.translate(ptVector3(11.25, -3.25, 0.0)) 
    objectName = objNameBase + str(curCol).zfill(2)
    ret = CloneColumns2(objName=objectName, age=ageName, bLoadOn=True, bShowOn=bShow, iNbCol=0, iCurCol=curCol, matAv=matAvatar, mTrans=matTrans, fXAngle=0, fYAngle=0, fZAngle=0, bAttachOn=False, soAv=soAvatar, bFirst=False)
    #
    curCol = curCol - 1
    matTrans = ptMatrix44()
    matTrans.translate(ptVector3(3.75, -3.25, 0.0)) 
    objectName = objNameBase + str(curCol).zfill(2)
    ret = CloneColumns2(objName=objectName, age=ageName, bLoadOn=True, bShowOn=bShow, iNbCol=0, iCurCol=curCol, matAv=matAvatar, mTrans=matTrans, fXAngle=0, fYAngle=0, fZAngle=0, bAttachOn=False, soAv=soAvatar, bFirst=False)
    #
    curCol = curCol - 1
    matTrans = ptMatrix44()
    matTrans.translate(ptVector3(-3.75, -3.25, 0.0)) 
    objectName = objNameBase + str(curCol).zfill(2)
    ret = CloneColumns2(objName=objectName, age=ageName, bLoadOn=True, bShowOn=bShow, iNbCol=0, iCurCol=curCol, matAv=matAvatar, mTrans=matTrans, fXAngle=0, fYAngle=0, fZAngle=0, bAttachOn=False, soAv=soAvatar, bFirst=False)
    #
    curCol = curCol - 1
    matTrans = ptMatrix44()
    matTrans.translate(ptVector3(-11.25, -3.25, 0.0)) 
    objectName = objNameBase + str(curCol).zfill(2)
    ret = CloneColumns2(objName=objectName, age=ageName, bLoadOn=True, bShowOn=bShow, iNbCol=0, iCurCol=curCol, matAv=matAvatar, mTrans=matTrans, fXAngle=0, fYAngle=0, fZAngle=0, bAttachOn=False, soAv=soAvatar, bFirst=False)
    #
    curCol = curCol - 1
    matTrans = ptMatrix44()
    matTrans.translate(ptVector3(-18.75, -3.25, 0.0)) 
    objectName = objNameBase + str(curCol).zfill(2)
    ret = CloneColumns2(objName=objectName, age=ageName, bLoadOn=True, bShowOn=bShow, iNbCol=0, iCurCol=curCol, matAv=matAvatar, mTrans=matTrans, fXAngle=0, fYAngle=0, fZAngle=0, bAttachOn=False, soAv=soAvatar, bFirst=False)
    #
    curCol = curCol - 1
    matTrans = ptMatrix44()
    matTrans.translate(ptVector3(-26.25, -3.25, 0.0)) 
    objectName = objNameBase + str(curCol).zfill(2)
    ret = CloneColumns2(objName=objectName, age=ageName, bLoadOn=True, bShowOn=bShow, iNbCol=0, iCurCol=curCol, matAv=matAvatar, mTrans=matTrans, fXAngle=0, fYAngle=0, fZAngle=0, bAttachOn=False, soAv=soAvatar, bFirst=False)
    #
    curCol = curCol - 1
    matTrans = ptMatrix44()
    matTrans.translate(ptVector3(-33.75, 4.25, 0.0)) 
    objectName = objNameBase + str(curCol).zfill(2)
    ret = CloneColumns2(objName=objectName, age=ageName, bLoadOn=True, bShowOn=bShow, iNbCol=0, iCurCol=curCol, matAv=matAvatar, mTrans=matTrans, fXAngle=0, fYAngle=0, fZAngle=0, bAttachOn=False, soAv=soAvatar, bFirst=False)
    #
    curCol = curCol - 1
    matTrans = ptMatrix44()
    matTrans.translate(ptVector3(-33.75, 4.25, 0.0)) 
    objectName = objNameBase + str(curCol).zfill(2)
    ret = CloneColumns2(objName=objectName, age=ageName, bLoadOn=True, bShowOn=bShow, iNbCol=0, iCurCol=curCol, matAv=matAvatar, mTrans=matTrans, fXAngle=0, fYAngle=0, fZAngle=90, bAttachOn=False, soAv=soAvatar, bFirst=False)
    
    # Rampe depuis la place
    # 24
    curCol = curCol - 1
    matTrans = ptMatrix44()
    #matTrans.translate(ptVector3(26.25, -3.25, -55.35)) 
    matTrans.translate(ptVector3(27.00, 10.00, -55.35)) 
    objectName = objNameBase + str(curCol).zfill(2)
    ret = CloneColumns2(objName=objectName, age=ageName, bLoadOn=True, bShowOn=bShow, iNbCol=0, iCurCol=curCol, matAv=matAvatar, mTrans=matTrans, fXAngle=35, fYAngle=0, fZAngle=90, bAttachOn=False, soAv=soAvatar, bFirst=False)
    # 14
    curCol = curCol - 1
    matTrans = ptMatrix44()
    #matTrans.translate(ptVector3(18.75, -3.25, -67.50)) 
    matTrans.translate(ptVector3(20.25, 10.00, -55.35)) 
    objectName = objNameBase + str(curCol).zfill(2)
    ret = CloneColumns2(objName=objectName, age=ageName, bLoadOn=True, bShowOn=bShow, iNbCol=0, iCurCol=curCol, matAv=matAvatar, mTrans=matTrans, fXAngle=35, fYAngle=0, fZAngle=90, bAttachOn=False, soAv=soAvatar, bFirst=False)
    
    # Rampe depuis la spyroom
    # 14
    curCol = curCol - 1
    matTrans = ptMatrix44()
    matTrans.translate(ptVector3(-8.75, 0.50, 60.0)) 
    objectName = objNameBase + str(curCol).zfill(2)
    ret = CloneColumns2(objName=objectName, age=ageName, bLoadOn=True, bShowOn=bShow, iNbCol=0, iCurCol=curCol, matAv=matAvatar, mTrans=matTrans, fXAngle=-7, fYAngle=0, fZAngle=0, bAttachOn=False, soAv=soAvatar, bFirst=False)
    # 24
    curCol = curCol - 1
    matTrans = ptMatrix44()
    matTrans.translate(ptVector3(-1.25, 0.50, 60.0)) 
    objectName = objNameBase + str(curCol).zfill(2)
    ret = CloneColumns2(objName=objectName, age=ageName, bLoadOn=True, bShowOn=bShow, iNbCol=0, iCurCol=curCol, matAv=matAvatar, mTrans=matTrans, fXAngle=-7, fYAngle=0, fZAngle=0, bAttachOn=False, soAv=soAvatar, bFirst=False)
    # 14
    curCol = curCol - 1
    matTrans = ptMatrix44()
    matTrans.translate(ptVector3(6.25, 0.50, 60.0)) 
    objectName = objNameBase + str(curCol).zfill(2)
    ret = CloneColumns2(objName=objectName, age=ageName, bLoadOn=True, bShowOn=bShow, iNbCol=0, iCurCol=curCol, matAv=matAvatar, mTrans=matTrans, fXAngle=-7, fYAngle=0, fZAngle=0, bAttachOn=False, soAv=soAvatar, bFirst=False)
    
    #return ret
    return 1


#=========================================
# CreatePlatform : Create a platform under me with 22 (16 + 6) columns of Jalak (mixo)
def CreatePlatform2(bShow=False, matAv=None, bAttach=False):
    objNameBase = "columnPhys_"
    ageName = "Jalak"
    playerID = PtGetLocalPlayer().getPlayerID()
    soAvatar = PtGetLocalAvatar()
    print("Player is myself")

    # Initialization
    curCol = 25
    # avatar's position
    if isinstance(matAv, ptMatrix44):
        matAvatar = matAv
    else:
        matAvatar = soAvatar.getLocalToWorld()
    
    # B 1
    curCol = curCol - 1
    matTrans = ptMatrix44()
    matTrans.translate(ptVector3(-3.75 + (7.50 * 9), 4.25, 0.0)) 
    objectName = objNameBase + str(curCol).zfill(2)
    ret = CloneColumns2(objName=objectName, age=ageName, bLoadOn=True, bShowOn=bShow, iNbCol=0, iCurCol=curCol, matAv=matAvatar, mTrans=matTrans, fXAngle=0, fYAngle=0, fZAngle=0, bAttachOn=bAttach, soAv=soAvatar, bFirst=True)

    # plancher = 16 colonnes
    for i in range(1, 9):
        curCol = 24 - i
        matTrans = ptMatrix44()
        matTrans.translate(ptVector3(-3.75 + (7.50 * i), -3.25, 0.0)) 
        objectName = objNameBase + str(curCol).zfill(2)
        ret = CloneColumns2(objName=objectName, age=ageName, bLoadOn=True, bShowOn=bShow, iNbCol=0, iCurCol=curCol, matAv=matAvatar, mTrans=matTrans, fXAngle=0, fYAngle=0, fZAngle=0, bAttachOn=bAttach, soAv=soAvatar, bFirst=False)
        curCol = 25 - i - 9
        matTrans = ptMatrix44()
        matTrans.translate(ptVector3(3.75 - (7.50 * i), -3.25, 0.0)) 
        objectName = objNameBase + str(curCol).zfill(2)
        ret = CloneColumns2(objName=objectName, age=ageName, bLoadOn=True, bShowOn=bShow, iNbCol=0, iCurCol=curCol, matAv=matAvatar, mTrans=matTrans, fXAngle=0, fYAngle=0, fZAngle=0, bAttachOn=bAttach, soAv=soAvatar, bFirst=False)

    # B 2
    curCol = curCol - 1
    matTrans = ptMatrix44()
    matTrans.translate(ptVector3(3.75 - (7.50 * 9), 4.25, 0.0)) 
    objectName = objNameBase + str(curCol).zfill(2)
    ret = CloneColumns2(objName=objectName, age=ageName, bLoadOn=True, bShowOn=bShow, iNbCol=0, iCurCol=curCol, matAv=matAvatar, mTrans=matTrans, fXAngle=0, fYAngle=0, fZAngle=0, bAttachOn=bAttach, soAv=soAvatar, bFirst=False)
    
    # B 3 a
    curCol = curCol - 1
    matTrans = ptMatrix44()
    matTrans.translate(ptVector3(33.75, 4.25, 30.00)) 
    objectName = objNameBase + str(curCol).zfill(2)
    ret = CloneColumns2(objName=objectName, age=ageName, bLoadOn=True, bShowOn=bShow, iNbCol=0, iCurCol=curCol, matAv=matAvatar, mTrans=matTrans, fXAngle=0, fYAngle=0, fZAngle=90, bAttachOn=bAttach, soAv=soAvatar, bFirst=False)
    # B 3 b
    curCol = curCol - 1
    matTrans = ptMatrix44()
    matTrans.translate(ptVector3(33.75, 4.25, -30.00)) 
    objectName = objNameBase + str(curCol).zfill(2)
    ret = CloneColumns2(objName=objectName, age=ageName, bLoadOn=True, bShowOn=bShow, iNbCol=0, iCurCol=curCol, matAv=matAvatar, mTrans=matTrans, fXAngle=0, fYAngle=0, fZAngle=90, bAttachOn=bAttach, soAv=soAvatar, bFirst=False)
    # B 4 a
    curCol = curCol - 1
    matTrans = ptMatrix44()
    matTrans.translate(ptVector3(-33.75, 4.25, 30.00)) 
    objectName = objNameBase + str(curCol).zfill(2)
    ret = CloneColumns2(objName=objectName, age=ageName, bLoadOn=True, bShowOn=bShow, iNbCol=0, iCurCol=curCol, matAv=matAvatar, mTrans=matTrans, fXAngle=0, fYAngle=0, fZAngle=90, bAttachOn=bAttach, soAv=soAvatar, bFirst=False)
    # B 4 b
    curCol = curCol - 1
    matTrans = ptMatrix44()
    matTrans.translate(ptVector3(-33.75, 4.25, -30.00)) 
    objectName = objNameBase + str(curCol).zfill(2)
    ret = CloneColumns2(objName=objectName, age=ageName, bLoadOn=True, bShowOn=bShow, iNbCol=0, iCurCol=curCol, matAv=matAvatar, mTrans=matTrans, fXAngle=0, fYAngle=0, fZAngle=90, bAttachOn=bAttach, soAv=soAvatar, bFirst=False)
    
    #return ret
    return 1

# 
def AttachColumnsToMe(bOn=True):
    objNameBase = "columnPhys_"
    ageName = "Jalak"
    soAvatar = PtGetLocalAvatar()
    for i in (0, 24):
        objectName = objNameBase + str(curCol).zfill(2)
        try:
            so = PtFindSceneobject(objectName, age)
        except:
            print("{} not found in {}".format(objName, age))
            #msg += "{} not found in {}\n".format(objName, age)
        if isinstance(so, ptSceneobject):
            if bOn:
                Attacher(so, soAvatar, True)
            else:
                Detacher(so, soAvatar)

# 

"""
    Plateforme pour "Tokotah 2" : 
    C'est une copie de ce qu'a fait Stone.
    
    sol = PtFindSceneobjects("column")
    sos = map(lambda so : [so.getName(), so.getLocalToWorld().getData()], sol)
    for o in sos:
        print"[\"{0}\", {1}], ".format(o[0], o[1])

    lstColumns = [
        ["columnPhys_00", ((0.9997363090515137, -0.01317062508314848, -0.018809599801898003, -64.35488891601562), (-0.022962283343076706, -0.5734251737594604, -0.8189359903335571, -268.5778503417969), (0.0, 0.8191519975662231, -0.5735764503479004, 213.96299743652344), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_01", ((0.9997363090515137, -0.01317062508314848, -0.018809599801898003, -69.67179107666016), (-0.022962283343076706, -0.5734251737594604, -0.8189359903335571, -268.4556884765625), (0.0, 0.8191519975662231, -0.5735764503479004, 213.95558166503906), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_02", ((0.999790608882904, 0.011737348511815071, 0.016762670129537582, -64.15877532958984), (0.02046344242990017, -0.573456346988678, -0.8189804553985596, -301.0745849609375), (0.0, 0.8191519975662231, -0.5735764503479004, 193.88372802734375), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_03", ((0.999790608882904, 0.011737348511815071, 0.016762670129537582, -68.27245330810547), (0.02046344242990017, -0.573456346988678, -0.8189804553985596, -301.15863037109375), (0.0, 0.8191519975662231, -0.5735764503479004, 193.8787841796875), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_04", ((-0.9999516606330872, 0.0, -0.009771088138222694, -74.02998352050781), (-0.009771088138222694, 4.370927442209904e-08, 0.9999516606330872, -235.1581573486328), (0.0, 1.0, -4.371138828673793e-08, 229.978759765625), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_05", ((-0.9999516606330872, 0.0, -0.009771088138222694, -79.8988265991211), (-0.009771088138222694, 4.370927442209904e-08, 0.9999516606330872, -235.21556091308594), (0.0, 1.0, -4.371138828673793e-08, 229.978759765625), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_06", ((-0.9999516606330872, 0.0, -0.009771088138222694, -85.31847381591797), (-0.009771088138222694, 4.370927442209904e-08, 0.9999516606330872, -235.26856994628906), (0.0, 1.0, -4.371138828673793e-08, 229.978759765625), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_07", ((-0.9999516606330872, 0.0, -0.009771088138222694, -59.47984313964844), (-0.009771088138222694, 4.370927442209904e-08, 0.9999516606330872, -235.0160675048828), (0.0, 1.0, -4.371138828673793e-08, 229.978759765625), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_08", ((-0.9999516606330872, 0.0, -0.009771088138222694, -53.952754974365234), (-0.009771088138222694, 4.370927442209904e-08, 0.9999516606330872, -234.9620819091797), (0.0, 1.0, -4.371138828673793e-08, 229.978759765625), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_09", ((-0.9999516606330872, 0.0, -0.009771088138222694, -48.14331817626953), (-0.009771088138222694, 4.370927442209904e-08, 0.9999516606330872, -230.82310485839844), (0.0, 1.0, -4.371138828673793e-08, 229.978759765625), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_10", ((-0.9999516606330872, 0.0, -0.009771088138222694, -43.582984924316406), (-0.009771088138222694, 4.370927442209904e-08, 0.9999516606330872, -217.7897491455078), (0.0, 1.0, -4.371138828673793e-08, 229.978759765625), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_11", ((-0.9999516606330872, 0.0, -0.009771088138222694, -37.48951721191406), (-0.009771088138222694, 4.370927442209904e-08, 0.9999516606330872, -214.73208618164062), (0.0, 1.0, -4.371138828673793e-08, 229.978759765625), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_12", ((-0.9999878406524658, 0.0, -0.003929780796170235, -64.91851043701172), (-0.003929780796170235, 4.371085537968611e-08, 0.9999878406524658, -214.74356079101562), (0.0, 1.0, -4.371138828673793e-08, 229.978759765625), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_13", ((-0.9999878406524658, 0.0, -0.003929780796170235, -70.12432098388672), (-0.003929780796170235, 4.371085537968611e-08, 0.9999878406524658, -214.56869506835938), (0.0, 1.0, -4.371138828673793e-08, 229.978759765625), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_14", ((-0.9999927282333374, 0.002113570226356387, 0.0030184907373040915, -73.3476333618164), (0.0036848969757556915, 0.5735722780227661, 0.8191460371017456, -289.87774658203125), (0.0, 0.8191519975662231, -0.5735764503479004, 180.4309539794922), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_15", ((-0.9999927282333374, 0.002113570226356387, 0.0030184907373040915, -78.9335708618164), (0.0036848969757556915, 0.5735722780227661, 0.8191460371017456, -289.85711669921875), (0.0, 0.8191519975662231, -0.5735764503479004, 180.4309539794922), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_16", ((0.028779180720448494, 0.0, -0.9995610117912292, -86.94892883300781), (-0.9995610117912292, -1.2579779440358152e-09, -0.028779180720448494, -261.5871276855469), (0.0, 1.0, -4.371138828673793e-08, 163.9554443359375), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_17", ((0.028779180720448494, 0.0, -0.9995610117912292, -87.11503601074219), (-0.9995610117912292, -1.2579779440358152e-09, -0.028779180720448494, -255.81809997558594), (0.0, 1.0, -4.371138828673793e-08, 163.9554443359375), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_18", ((0.9998344779014587, 0.0, 0.016580400988459587, -112.17644500732422), (0.016580400988459587, -4.370415140897421e-08, -0.9998344779014587, -295.18890380859375), (0.0, 1.0, -4.371138828673793e-08, 163.9554443359375), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_19", ((0.9998344779014587, 0.0, 0.016580400988459587, -106.3375473022461), (0.016580400988459587, -4.370415140897421e-08, -0.9998344779014587, -295.0919494628906), (0.0, 1.0, -4.371138828673793e-08, 163.9554443359375), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_20", ((0.0030144453048706055, 0.12186886370182037, 0.9925417304039001, -85.90312957763672), (0.9999955296516418, -0.0003673686587717384, -0.0029919759836047888, -328.1044006347656), (0.0, 0.9925461411476135, -0.12186940759420395, 161.42770385742188), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_21", ((0.0030144453048706055, 0.12186886370182037, 0.9925417304039001, -85.92120361328125), (0.9999955296516418, -0.0003673686587717384, -0.0029919759836047888, -334.1004943847656), (0.0, 0.9925461411476135, -0.12186940759420395, 161.42770385742188), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_22", ((-0.010072540491819382, 0.0, 0.9999488592147827, -64.9786148071289), (0.9999488592147827, 4.4028472534485275e-10, 0.010072540491819382, -202.37376403808594), (0.0, 1.0, -4.371138828673793e-08, 229.95863342285156), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_23", ((-0.010072540491819382, 0.0, 0.9999488592147827, -65.03800964355469), (0.9999488592147827, 4.4028472534485275e-10, 0.010072540491819382, -196.4756317138672), (0.0, 1.0, -4.371138828673793e-08, 229.95863342285156), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_24", ((-0.9894455671310425, 0.14411106705665588, -0.015146682970225811, -85.88858795166016), (-0.14490486681461334, -0.9840252995491028, 0.10342522710561752, -250.65289306640625), (0.0, 0.10452846437692642, 0.9945219159126282, 262.7247009277344), (0.0, 0.0, 0.0, 1.0))], 
    ]
"""

#

#=========================================
# CreatePlatformForTokotah2
def CreatePlatformForTokotah2():
    #objNameBase = "columnPhys_"
    ageName = "Jalak"
    
    """
    playerID = PtGetLocalPlayer().getPlayerID()
    soAvatar = PtGetLocalAvatar()
    print "Player is myself"

    # Initialization
    curCol = 25
    # avatar's position
    if isinstance(matAv, ptMatrix44):
        matAvatar = matAv
    else:
        matAvatar = soAvatar.getLocalToWorld()
    
    # B 1
    curCol = curCol - 1
    matTrans = ptMatrix44()
    matTrans.translate(ptVector3(-3.75 + (7.50 * 9), 4.25, 0.0)) 
    objectName = objNameBase + str(curCol).zfill(2)
    ret = CloneColumns2(objName=objectName, age=ageName, bLoadOn=True, bShowOn=bShow, iNbCol=0, iCurCol=0, matAv=matAvatar, mTrans=matTrans, fXAngle=0, fYAngle=0, fZAngle=0, bAttachOn=bAttach, soAv=soAvatar, bFirst=True)
    """
    
    lstColNamePos = [
        ["columnPhys_00", ((0.9997363090515137, -0.01317062508314848, -0.018809599801898003, -64.35488891601562), (-0.022962283343076706, -0.5734251737594604, -0.8189359903335571, -268.5778503417969), (0.0, 0.8191519975662231, -0.5735764503479004, 213.96299743652344), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_01", ((0.9997363090515137, -0.01317062508314848, -0.018809599801898003, -69.67179107666016), (-0.022962283343076706, -0.5734251737594604, -0.8189359903335571, -268.4556884765625), (0.0, 0.8191519975662231, -0.5735764503479004, 213.95558166503906), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_02", ((0.999790608882904, 0.011737348511815071, 0.016762670129537582, -64.15877532958984), (0.02046344242990017, -0.573456346988678, -0.8189804553985596, -301.0745849609375), (0.0, 0.8191519975662231, -0.5735764503479004, 193.88372802734375), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_03", ((0.999790608882904, 0.011737348511815071, 0.016762670129537582, -68.27245330810547), (0.02046344242990017, -0.573456346988678, -0.8189804553985596, -301.15863037109375), (0.0, 0.8191519975662231, -0.5735764503479004, 193.8787841796875), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_04", ((-0.9999516606330872, 0.0, -0.009771088138222694, -74.02998352050781), (-0.009771088138222694, 4.370927442209904e-08, 0.9999516606330872, -235.1581573486328), (0.0, 1.0, -4.371138828673793e-08, 229.978759765625), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_05", ((-0.9999516606330872, 0.0, -0.009771088138222694, -79.8988265991211), (-0.009771088138222694, 4.370927442209904e-08, 0.9999516606330872, -235.21556091308594), (0.0, 1.0, -4.371138828673793e-08, 229.978759765625), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_06", ((-0.9999516606330872, 0.0, -0.009771088138222694, -85.31847381591797), (-0.009771088138222694, 4.370927442209904e-08, 0.9999516606330872, -235.26856994628906), (0.0, 1.0, -4.371138828673793e-08, 229.978759765625), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_07", ((-0.9999516606330872, 0.0, -0.009771088138222694, -59.47984313964844), (-0.009771088138222694, 4.370927442209904e-08, 0.9999516606330872, -235.0160675048828), (0.0, 1.0, -4.371138828673793e-08, 229.978759765625), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_08", ((-0.9999516606330872, 0.0, -0.009771088138222694, -53.952754974365234), (-0.009771088138222694, 4.370927442209904e-08, 0.9999516606330872, -234.9620819091797), (0.0, 1.0, -4.371138828673793e-08, 229.978759765625), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_09", ((-0.9999516606330872, 0.0, -0.009771088138222694, -48.14331817626953), (-0.009771088138222694, 4.370927442209904e-08, 0.9999516606330872, -230.82310485839844), (0.0, 1.0, -4.371138828673793e-08, 229.978759765625), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_10", ((-0.9999516606330872, 0.0, -0.009771088138222694, -43.582984924316406), (-0.009771088138222694, 4.370927442209904e-08, 0.9999516606330872, -217.7897491455078), (0.0, 1.0, -4.371138828673793e-08, 229.978759765625), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_11", ((-0.9999516606330872, 0.0, -0.009771088138222694, -37.48951721191406), (-0.009771088138222694, 4.370927442209904e-08, 0.9999516606330872, -214.73208618164062), (0.0, 1.0, -4.371138828673793e-08, 229.978759765625), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_12", ((-0.9999878406524658, 0.0, -0.003929780796170235, -64.91851043701172), (-0.003929780796170235, 4.371085537968611e-08, 0.9999878406524658, -214.74356079101562), (0.0, 1.0, -4.371138828673793e-08, 229.978759765625), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_13", ((-0.9999878406524658, 0.0, -0.003929780796170235, -70.12432098388672), (-0.003929780796170235, 4.371085537968611e-08, 0.9999878406524658, -214.56869506835938), (0.0, 1.0, -4.371138828673793e-08, 229.978759765625), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_14", ((-0.9999927282333374, 0.002113570226356387, 0.0030184907373040915, -73.3476333618164), (0.0036848969757556915, 0.5735722780227661, 0.8191460371017456, -289.87774658203125), (0.0, 0.8191519975662231, -0.5735764503479004, 180.4309539794922), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_15", ((-0.9999927282333374, 0.002113570226356387, 0.0030184907373040915, -78.9335708618164), (0.0036848969757556915, 0.5735722780227661, 0.8191460371017456, -289.85711669921875), (0.0, 0.8191519975662231, -0.5735764503479004, 180.4309539794922), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_16", ((0.028779180720448494, 0.0, -0.9995610117912292, -86.94892883300781), (-0.9995610117912292, -1.2579779440358152e-09, -0.028779180720448494, -261.5871276855469), (0.0, 1.0, -4.371138828673793e-08, 163.9554443359375), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_17", ((0.028779180720448494, 0.0, -0.9995610117912292, -87.11503601074219), (-0.9995610117912292, -1.2579779440358152e-09, -0.028779180720448494, -255.81809997558594), (0.0, 1.0, -4.371138828673793e-08, 163.9554443359375), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_18", ((0.9998344779014587, 0.0, 0.016580400988459587, -112.17644500732422), (0.016580400988459587, -4.370415140897421e-08, -0.9998344779014587, -295.18890380859375), (0.0, 1.0, -4.371138828673793e-08, 163.9554443359375), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_19", ((0.9998344779014587, 0.0, 0.016580400988459587, -106.3375473022461), (0.016580400988459587, -4.370415140897421e-08, -0.9998344779014587, -295.0919494628906), (0.0, 1.0, -4.371138828673793e-08, 163.9554443359375), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_20", ((0.0030144453048706055, 0.12186886370182037, 0.9925417304039001, -85.90312957763672), (0.9999955296516418, -0.0003673686587717384, -0.0029919759836047888, -328.1044006347656), (0.0, 0.9925461411476135, -0.12186940759420395, 161.42770385742188), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_21", ((0.0030144453048706055, 0.12186886370182037, 0.9925417304039001, -85.92120361328125), (0.9999955296516418, -0.0003673686587717384, -0.0029919759836047888, -334.1004943847656), (0.0, 0.9925461411476135, -0.12186940759420395, 161.42770385742188), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_22", ((-0.010072540491819382, 0.0, 0.9999488592147827, -64.9786148071289), (0.9999488592147827, 4.4028472534485275e-10, 0.010072540491819382, -202.37376403808594), (0.0, 1.0, -4.371138828673793e-08, 229.95863342285156), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_23", ((-0.010072540491819382, 0.0, 0.9999488592147827, -65.03800964355469), (0.9999488592147827, 4.4028472534485275e-10, 0.010072540491819382, -196.4756317138672), (0.0, 1.0, -4.371138828673793e-08, 229.95863342285156), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_24", ((-0.9894455671310425, 0.14411106705665588, -0.015146682970225811, -85.88858795166016), (-0.14490486681461334, -0.9840252995491028, 0.10342522710561752, -250.65289306640625), (0.0, 0.10452846437692642, 0.9945219159126282, 262.7247009277344), (0.0, 0.0, 0.0, 1.0))], 
    ]
    
    for colNamePos in lstColNamePos:
        objectName = colNamePos[0]
        tuplePos = colNamePos[1]
        mPos = ptMatrix44()
        mPos.setData(tuplePos)
        bFirst = (objectName == "columnPhys_00")
        ret = CloneThem2(objName=objectName, age=ageName, iNbClones=0, iCurClone=0, bShow=False, bLoad=True, matPos=mPos, fct=PutItHere2, bAttach=False, soAvatar=None, bFirstCol=bFirst)
    
    #return ret
    return 1

#------------------------------------------------------------------------------
"""
    V1 :
        ["columnPhys_00", ((4.37113882867e-08, -0.73963111639, -0.673012495041, 80), (1.0, 3.23303019911e-08, 0.0, -81.5), (0.0, -0.673012495041, 0.73963111639, 219.59619894132), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_01", ((4.37113882867e-08, -0.73963111639, -0.673012495041, 80), (1.0, 3.23303019911e-08, 0.0, -89), (0.0, -0.673012495041, 0.73963111639, 219.59619894132), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_02", ((4.37113882867e-08, -0.73963111639, -0.673012495041, 80), (1.0, 3.23303019911e-08, 0.0, -96.5), (0.0, -0.673012495041, 0.73963111639, 219.59619894132), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_03", ((1.0, 0.0, 0.0, 116), (0.0, 1.0, 0.0, -89), (0.0, 0.0, 1.0, 238.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_04", ((1.0, 0.0, 0.0, 124), (0.0, 1.0, 0.0, -89), (0.0, 0.0, 1.0, 238.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_05", ((4.37113882867e-08, -0.83195412159, -0.55484443903, 125.2), (1.0, 1.98941005891e-08, 0.0, -81.5), (0.0, -0.55484443903, 0.83195412159, 238.696149103076), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_06", ((4.37113882867e-08, -0.83195412159, -0.55484443903, 125.2), (1.0, 1.98941005891e-08, 0.0, -89), (0.0, -0.55484443903, 0.83195412159, 238.696149103076), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_07", ((4.37113882867e-08, -0.83195412159, -0.55484443903, 125.2), (1.0, 1.98941005891e-08, 0.0, -96.5), (0.0, -0.55484443903, 0.83195412159, 238.696149103076), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_08", ((-0.269724786282, -0.802051961422, -0.532881975174, 309.7), (0.96293848753, -0.224659517407, -0.14926341176, -42.75), (0.0, -0.553391516209, 0.832921266556, 254.696149103076), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_09", ((-0.269724786282, -0.802051961422, -0.532881975174, 309.7), (0.96293848753, -0.224659517407, -0.14926341176, -50.25), (0.0, -0.553391516209, 0.832921266556, 254.696149103076), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_10", ((-0.515038013458, -0.857167363167, 0.0, 280), (0.857167363167, -0.515038013458, 0.0, -44.25), (0.0, 0.0, 1.0, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_11", ((-0.515038013458, -0.857167363167, 0.0, 280), (0.857167363167, -0.515038013458, 0.0, -51.75), (0.0, 0.0, 1.0, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_12", ((-0.515038013458, -0.857167363167, 0.0, 219), (0.857167363167, -0.515038013458, 0.0, -44.25), (0.0, 0.0, 1.0, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_13", ((-0.515038013458, -0.857167363167, 0.0, 219), (0.857167363167, -0.515038013458, 0.0, -51.75), (0.0, 0.0, 1.0, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_14", ((-0.515038013458, -0.857167363167, 0.0, 158), (0.857167363167, -0.515038013458, 0.0, -44.25), (0.0, 0.0, 1.0, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_15", ((-0.515038013458, -0.857167363167, 0.0, 158), (0.857167363167, -0.515038013458, 0.0, -51.75), (0.0, 0.0, 1.0, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_16", ((-0.515038013458, -0.857167363167, 0.0, 219), (0.857167363167, -0.515038013458, 0.0, -36.75), (0.0, 0.0, 1.0, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_17", ((-0.515038013458, -0.857167363167, 0.0, 219), (0.857167363167, -0.515038013458, 0.0, -59.25), (0.0, 0.0, 1.0, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_18", ((-0.515038013458, -0.857167363167, 0.0, 158), (0.857167363167, -0.515038013458, 0.0, -36.75), (0.0, 0.0, 1.0, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_19", ((-0.515038013458, -0.857167363167, 0.0, 158), (0.857167363167, -0.515038013458, 0.0, -59.25), (0.0, 0.0, 1.0, 254.75), (0.0, 0.0, 0.0, 1.0))], 
    V2 :
        ["columnPhys_00", ((1.0, 0.0, 0.0, 80.0), (0.0, -4.371138828673793e-08, -1.0, -89.0), (0.0, 1.0, -4.371138828673793e-08, 218.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_01", ((4.172325134277344e-07, -0.5519368648529053, 0.8338857889175415, 89.63523864746094), (0.9999998807907104, -1.5577120553189085e-14, 0.0, -88.9984130859375), (0.0, 0.833885908126831, 0.5519368052482605, 222.5917205810547), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_02", ((4.172325134277344e-07, -0.5519368648529053, 0.8338857889175415, 89.63523864746094), (0.9999998807907104, -1.5577120553189085e-14, 0.0, -81.4984130859375), (0.0, 0.833885908126831, 0.5519368052482605, 222.5917205810547), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_03", ((4.172325134277344e-07, -0.5519368648529053, 0.8338857889175415, 89.63523864746094), (0.9999998807907104, -1.5577120553189085e-14, 0.0, -96.4984130859375), (0.0, 0.833885908126831, 0.5519368052482605, 222.5917205810547), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_04", ((1.0, 0.0, 0.0, 116.25), (0.0, -4.371138828673793e-08, -1.0, -89.0), (0.0, 1.0, -4.371138828673793e-08, 218.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_05", ((1.0, 0.0, 0.0, 123.75), (0.0, -4.371138828673793e-08, -1.0, -89.0), (0.0, 1.0, -4.371138828673793e-08, 218.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_06", ((4.172325134277344e-07, -0.5519368648529053, 0.8338857889175415, 129.63523864746094), (0.9999998807907104, -1.5577120553189085e-14, 0.0, -88.9984130859375), (0.0, 0.833885908126831, 0.5519368052482605, 240.5917205810547), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_07", ((4.172325134277344e-07, -0.5519368648529053, 0.8338857889175415, 129.63523864746094), (0.9999998807907104, -1.5577120553189085e-14, 0.0, -81.4984130859375), (0.0, 0.833885908126831, 0.5519368052482605, 240.5917205810547), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_08", ((4.172325134277344e-07, -0.5519368648529053, 0.8338857889175415, 129.63523864746094), (0.9999998807907104, -1.5577120553189085e-14, 0.0, -96.4984130859375), (0.0, 0.833885908126831, 0.5519368052482605, 240.5917205810547), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_09", ((0.0, -1.0, 0.0, 182.5), (1.0, 0.0, 0.0, -81.5), (0.0, 0.0, 1.0, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_10", ((0.0, -1.0, 0.0, 182.5), (1.0, 0.0, 0.0, -89.0), (0.0, 0.0, 1.0, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_11", ((0.0, -1.0, 0.0, 182.5), (1.0, 0.0, 0.0, -96.5), (0.0, 0.0, 1.0, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_12", ((0.0, -1.0, 0.0, 243.5), (1.0, 0.0, 0.0, -81.5), (0.0, 0.0, 1.0, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_13", ((0.0, -1.0, 0.0, 243.5), (1.0, 0.0, 0.0, -89.0), (0.0, 0.0, 1.0, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_14", ((0.0, -1.0, 0.0, 197.5), (1.0, 0.0, 0.0, -74.0), (0.0, 0.0, 1.0, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_15", ((0.0, -1.0, 0.0, 258.5), (1.0, 0.0, 0.0, -74.0), (0.0, 0.0, 1.0, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_16", ((0.0, -1.0, 0.0, 212.5), (1.0, 0.0, 0.0, -66.5), (0.0, 0.0, 1.0, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_17", ((0.0, -1.0, 0.0, 273.5), (1.0, 0.0, 0.0, -66.5), (0.0, 0.0, 1.0, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_18", ((0.0, -1.0, 0.0, 282.5), (1.0, 0.0, 0.0, -58.0), (0.0, 0.0, 1.0, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_19", ((0.0, -1.0, 0.0, 282.5), (1.0, 0.0, 0.0, -50.5), (0.0, 0.0, 1.0, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_20", ((0.0, -1.0, 0.0, 282.5), (1.0, 0.0, 0.0, -43.0), (0.0, 0.0, 1.0, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_21", ((0.0, -1.0, 0.0, 221.5), (1.0, 0.0, 0.0, -58.0), (0.0, 0.0, 1.0, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_22", ((0.0, -1.0, 0.0, 192.5), (1.0, 0.0, 0.0, -104.0), (0.0, 0.0, 1.0, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_23", ((4.172325134277344e-07, -0.5519368648529053, 0.8338857889175415, 310.63523864746094), (0.9999998807907104, -1.5577120553189085e-14, 0.0, -34.25), (0.0, 0.833885908126831, 0.5519368052482605, 254.5917205810547), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_24", ((4.172325134277344e-07, -0.5519368648529053, 0.8338857889175415, 310.63523864746094), (0.9999998807907104, -1.5577120553189085e-14, 0.0, -41.75), (0.0, 0.833885908126831, 0.5519368052482605, 254.5917205810547), (0.0, 0.0, 0.0, 1.0))], 

"""
# Mystitech secret passage in city (behind palace)
def SecretPath():
    ageName = "Jalak"
    lstColNamePos = [
        ["columnPhys_00", ((1.0, 0.0, 0.0, 80.0), (0.0, -4.371138828673793e-08, -1.0, -89.0), (0.0, 1.0, -4.371138828673793e-08, 218.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_01", ((4.172325134277344e-07, -0.5519368648529053, 0.8338857889175415, 89.63523864746094), (0.9999998807907104, -1.5577120553189085e-14, 0.0, -88.9984130859375), (0.0, 0.833885908126831, 0.5519368052482605, 222.5917205810547), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_02", ((4.172325134277344e-07, -0.5519368648529053, 0.8338857889175415, 89.63523864746094), (0.9999998807907104, -1.5577120553189085e-14, 0.0, -81.4984130859375), (0.0, 0.833885908126831, 0.5519368052482605, 222.5917205810547), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_03", ((4.172325134277344e-07, -0.5519368648529053, 0.8338857889175415, 89.63523864746094), (0.9999998807907104, -1.5577120553189085e-14, 0.0, -96.4984130859375), (0.0, 0.833885908126831, 0.5519368052482605, 222.5917205810547), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_04", ((1.0, 0.0, 0.0, 116.75), (0.0, -4.371138828673793e-08, -1.0, -89.0), (0.0, 1.0, -4.371138828673793e-08, 238.59), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_05", ((1.0, 0.0, 0.0, 124.25), (0.0, -4.371138828673793e-08, -1.0, -89.0), (0.0, 1.0, -4.371138828673793e-08, 238.59), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_06", ((4.172325134277344e-07, -0.5519368648529053, 0.8338857889175415, 129.63523864746094), (0.9999998807907104, -1.5577120553189085e-14, 0.0, -88.9984130859375), (0.0, 0.833885908126831, 0.5519368052482605, 238.8317205810547), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_07", ((4.172325134277344e-07, -0.5519368648529053, 0.8338857889175415, 129.63523864746094), (0.9999998807907104, -1.5577120553189085e-14, 0.0, -81.4984130859375), (0.0, 0.833885908126831, 0.5519368052482605, 238.8317205810547), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_08", ((4.172325134277344e-07, -0.5519368648529053, 0.8338857889175415, 129.63523864746094), (0.9999998807907104, -1.5577120553189085e-14, 0.0, -96.4984130859375), (0.0, 0.833885908126831, 0.5519368052482605, 238.8317205810547), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_09", ((0.0, 0.0, 1.0, 182.5), (1.0, 0.0, 0.0, -81.5), (0.0, 1.0, 0.0, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_10", ((0.0, 0.0, 1.0, 182.5), (1.0, 0.0, 0.0, -89.0), (0.0, 1.0, 0.0, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_11", ((0.0, 0.0, 1.0, 182.5), (1.0, 0.0, 0.0, -96.5), (0.0, 1.0, 0.0, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_12", ((0.0, 0.0, 1.0, 243.5), (1.0, 0.0, 0.0, -81.5), (0.0, 1.0, 0.0, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_13", ((0.0, 0.0, 1.0, 243.5), (1.0, 0.0, 0.0, -89.0), (0.0, 1.0, 0.0, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_14", ((0.0, 0.0, 1.0, 197.5), (1.0, 0.0, 0.0, -74.0), (0.0, 1.0, 0.0, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_15", ((0.0, 0.0, 1.0, 258.5), (1.0, 0.0, 0.0, -74.0), (0.0, 1.0, 0.0, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_16", ((0.0, 0.0, 1.0, 212.5), (1.0, 0.0, 0.0, -66.5), (0.0, 1.0, 0.0, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_17", ((0.0, 0.0, 1.0, 273.5), (1.0, 0.0, 0.0, -66.5), (0.0, 1.0, 0.0, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_18", ((0.0, 0.0, 1.0, 221.5), (1.0, 0.0, 0.0, -59.0), (0.0, 1.0, 0.0, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_19", ((0.0, 0.0, 1.0, 282.5), (1.0, 0.0, 0.0, -59.0), (0.0, 1.0, 0.0, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_20", ((0.0, 0.0, 1.0, 282.5), (1.0, 0.0, 0.0, -51.5), (0.0, 1.0, 0.0, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_21", ((0.0, 0.0, 1.0, 282.5), (1.0, 0.0, 0.0, -44.0), (0.0, 1.0, 0.0, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_22", ((0.0, 0.0, 1.0, 282.5), (1.0, 0.0, 0.0, -36.5), (0.0, 1.0, 0.0, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_23", ((0.521885573864, -0.318852335215, 0.791182041168, 313.026641846), (0.184063658118, 0.947755277157, 0.260539084673, -48.8581619263), (-0.832920372486, 0.00965646654367, 0.553308904171, 254.139271851), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_24", ((0.521885573864, -0.318852335215, 0.791182041168, 310.635253906), (0.184063658118, 0.947755277157, 0.260539084673, -41.75), (-0.832920372486, 0.00965646654367, 0.553308904171, 254.211705322), (0.0, 0.0, 0.0, 1.0))], 
    ]
    
    for colNamePos in lstColNamePos:
        objectName = colNamePos[0]
        tuplePos = colNamePos[1]
        mPos = ptMatrix44()
        mPos.setData(tuplePos)
        bFirst = (objectName == "columnPhys_00")
        ret = CloneThem2(objName=objectName, age=ageName, iNbClones=0, iCurClone=0, bShow=False, bLoad=True, matPos=mPos, fct=PutItHere2, bAttach=False, soAvatar=None, bFirstCol=bFirst)
    
    #return ret
    return 1

# Mystitech secret passage in city (behind palace) V2
"""
        ["columnPhys_00", ((1.0, 0.0, 0.0, 80.0), (0.0, -4.371138828673793e-08, -1.0, -89.0), (0.0, 1.0, -4.371138828673793e-08, 218.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_01", ((4.172325134277344e-07, -0.5519368648529053, 0.8338857889175415, 89.63523864746094), (0.9999998807907104, -1.5577120553189085e-14, 0.0, -88.9984130859375), (0.0, 0.833885908126831, 0.5519368052482605, 222.5917205810547), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_02", ((4.172325134277344e-07, -0.5519368648529053, 0.8338857889175415, 89.63523864746094), (0.9999998807907104, -1.5577120553189085e-14, 0.0, -81.4984130859375), (0.0, 0.833885908126831, 0.5519368052482605, 222.5917205810547), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_03", ((4.172325134277344e-07, -0.5519368648529053, 0.8338857889175415, 89.63523864746094), (0.9999998807907104, -1.5577120553189085e-14, 0.0, -96.4984130859375), (0.0, 0.833885908126831, 0.5519368052482605, 222.5917205810547), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_04", ((1.0, 0.0, 0.0, 116.75), (0.0, -4.371138828673793e-08, -1.0, -89.0), (0.0, 1.0, -4.371138828673793e-08, 238.59), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_05", ((1.0, 0.0, 0.0, 124.25), (0.0, -4.371138828673793e-08, -1.0, -89.0), (0.0, 1.0, -4.371138828673793e-08, 238.59), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_06", ((4.172325134277344e-07, -0.5519368648529053, 0.8338857889175415, 129.63523864746094), (0.9999998807907104, -1.5577120553189085e-14, 0.0, -88.9984130859375), (0.0, 0.833885908126831, 0.5519368052482605, 238.8317205810547), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_07", ((4.172325134277344e-07, -0.5519368648529053, 0.8338857889175415, 129.63523864746094), (0.9999998807907104, -1.5577120553189085e-14, 0.0, -81.4984130859375), (0.0, 0.833885908126831, 0.5519368052482605, 238.8317205810547), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_08", ((4.172325134277344e-07, -0.5519368648529053, 0.8338857889175415, 129.63523864746094), (0.9999998807907104, -1.5577120553189085e-14, 0.0, -96.4984130859375), (0.0, 0.833885908126831, 0.5519368052482605, 238.8317205810547), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_09", ((0.30901697278, 0.0, -0.951056540012, 182.5), (-0.951056540012, 1.91068546516e-15, -0.309017002583, -81.5), (0.0, 1.0, -4.15720009528e-08, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_10", ((0.30901697278, 0.0, -0.951056540012, 182.5), (-0.951056540012, 1.91068546516e-15, -0.309017002583, -89.0), (0.0, 1.0, -4.15720009528e-08, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_11", ((0.30901697278, 0.0, -0.951056540012, 182.5), (-0.951056540012, 1.91068546516e-15, -0.309017002583, -96.5), (0.0, 1.0, -4.15720009528e-08, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_12", ((0.30901697278, 0.0, -0.951056540012, 243.5), (-0.951056540012, 1.91068546516e-15, -0.309017002583, -81.5), (0.0, 1.0, -4.15720009528e-08, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_13", ((0.30901697278, 0.0, -0.951056540012, 243.5), (-0.951056540012, 1.91068546516e-15, -0.309017002583, -89.0), (0.0, 1.0, -4.15720009528e-08, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_14", ((0.30901697278, 0.0, -0.951056540012, 197.5), (-0.951056540012, 1.91068546516e-15, -0.309017002583, -74.0), (0.0, 1.0, -4.15720009528e-08, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_15", ((0.30901697278, 0.0, -0.951056540012, 258.5), (-0.951056540012, 1.91068546516e-15, -0.309017002583, -74.0), (0.0, 1.0, -4.15720009528e-08, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_16", ((0.30901697278, 0.0, -0.951056540012, 212.5), (-0.951056540012, 1.91068546516e-15, -0.309017002583, -66.5), (0.0, 1.0, -4.15720009528e-08, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_17", ((0.30901697278, 0.0, -0.951056540012, 273.5), (-0.951056540012, 1.91068546516e-15, -0.309017002583, -66.5), (0.0, 1.0, -4.15720009528e-08, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_18", ((0.30901697278, 0.0, -0.951056540012, 221.5), (-0.951056540012, 1.91068546516e-15, -0.309017002583, -59.0), (0.0, 1.0, -4.15720009528e-08, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_19", ((0.30901697278, 0.0, -0.951056540012, 282.5), (-0.951056540012, 1.91068546516e-15, -0.309017002583, -59.0), (0.0, 1.0, -4.15720009528e-08, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_20", ((0.30901697278, 0.0, -0.951056540012, 282.5), (-0.951056540012, 1.91068546516e-15, -0.309017002583, -51.5), (0.0, 1.0, -4.15720009528e-08, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_21", ((0.30901697278, 0.0, -0.951056540012, 282.5), (-0.951056540012, 1.91068546516e-15, -0.309017002583, -44.0), (0.0, 1.0, -4.15720009528e-08, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_22", ((0.30901697278, 0.0, -0.951056540012, 282.5), (-0.951056540012, 1.91068546516e-15, -0.309017002583, -36.5), (0.0, 1.0, -4.15720009528e-08, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_23", ((0.521885573864, -0.318852335215, 0.791182041168, 313.026641846), (0.184063658118, 0.947755277157, 0.260539084673, -48.8581619263), (-0.832920372486, 0.00965646654367, 0.553308904171, 254.139271851), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_24", ((0.521885573864, -0.318852335215, 0.791182041168, 310.635253906), (0.184063658118, 0.947755277157, 0.260539084673, -41.75), (-0.832920372486, 0.00965646654367, 0.553308904171, 254.211705322), (0.0, 0.0, 0.0, 1.0))], 
"""
"""
        ["columnPhys_09", ((0.0, 0.0, 1.0, 182.5), (1.0, 0.0, 0.0, -81.5), (0.0, 1.0, 0.0, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_10", ((0.0, 0.0, 1.0, 182.5), (1.0, 0.0, 0.0, -89.0), (0.0, 1.0, 0.0, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_11", ((0.0, 0.0, 1.0, 182.5), (1.0, 0.0, 0.0, -96.5), (0.0, 1.0, 0.0, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_12", ((0.0, 0.0, 1.0, 243.5), (1.0, 0.0, 0.0, -81.5), (0.0, 1.0, 0.0, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_13", ((0.0, 0.0, 1.0, 243.5), (1.0, 0.0, 0.0, -89.0), (0.0, 1.0, 0.0, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_14", ((0.0, 0.0, 1.0, 197.5), (1.0, 0.0, 0.0, -74.0), (0.0, 1.0, 0.0, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_15", ((0.0, 0.0, 1.0, 258.5), (1.0, 0.0, 0.0, -74.0), (0.0, 1.0, 0.0, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_16", ((0.0, 0.0, 1.0, 212.5), (1.0, 0.0, 0.0, -66.5), (0.0, 1.0, 0.0, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_17", ((0.0, 0.0, 1.0, 273.5), (1.0, 0.0, 0.0, -66.5), (0.0, 1.0, 0.0, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_18", ((0.0, 0.0, 1.0, 221.5), (1.0, 0.0, 0.0, -59.0), (0.0, 1.0, 0.0, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_19", ((0.0, 0.0, 1.0, 282.5), (1.0, 0.0, 0.0, -59.0), (0.0, 1.0, 0.0, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_20", ((0.0, 0.0, 1.0, 282.5), (1.0, 0.0, 0.0, -51.5), (0.0, 1.0, 0.0, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_21", ((0.0, 0.0, 1.0, 282.5), (1.0, 0.0, 0.0, -44.0), (0.0, 1.0, 0.0, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_22", ((0.0, 0.0, 1.0, 282.5), (1.0, 0.0, 0.0, -36.5), (0.0, 1.0, 0.0, 254.75), (0.0, 0.0, 0.0, 1.0))], 
"""
def SecretPath2(attach=False):
    ageName = "Jalak"
    lstColNamePos = [
        ["columnPhys_00", ((1.0, 0.0, 0.0, 80.0), (0.0, -4.371138828673793e-08, -1.0, -89.0), (0.0, 1.0, -4.371138828673793e-08, 218.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_01", ((4.172325134277344e-07, -0.5519368648529053, 0.8338857889175415, 89.63523864746094), (0.9999998807907104, -1.5577120553189085e-14, 0.0, -88.9984130859375), (0.0, 0.833885908126831, 0.5519368052482605, 222.5917205810547), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_02", ((4.172325134277344e-07, -0.5519368648529053, 0.8338857889175415, 89.63523864746094), (0.9999998807907104, -1.5577120553189085e-14, 0.0, -81.4984130859375), (0.0, 0.833885908126831, 0.5519368052482605, 222.5917205810547), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_03", ((4.172325134277344e-07, -0.5519368648529053, 0.8338857889175415, 89.63523864746094), (0.9999998807907104, -1.5577120553189085e-14, 0.0, -96.4984130859375), (0.0, 0.833885908126831, 0.5519368052482605, 222.5917205810547), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_04", ((1.0, 0.0, 0.0, 116.75), (0.0, -4.371138828673793e-08, -1.0, -89.0), (0.0, 1.0, -4.371138828673793e-08, 238.59), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_05", ((1.0, 0.0, 0.0, 124.25), (0.0, -4.371138828673793e-08, -1.0, -89.0), (0.0, 1.0, -4.371138828673793e-08, 238.59), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_06", ((4.172325134277344e-07, -0.5519368648529053, 0.8338857889175415, 129.63523864746094), (0.9999998807907104, -1.5577120553189085e-14, 0.0, -88.9984130859375), (0.0, 0.833885908126831, 0.5519368052482605, 238.8317205810547), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_07", ((4.172325134277344e-07, -0.5519368648529053, 0.8338857889175415, 129.63523864746094), (0.9999998807907104, -1.5577120553189085e-14, 0.0, -81.4984130859375), (0.0, 0.833885908126831, 0.5519368052482605, 238.8317205810547), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_08", ((4.172325134277344e-07, -0.5519368648529053, 0.8338857889175415, 129.63523864746094), (0.9999998807907104, -1.5577120553189085e-14, 0.0, -96.4984130859375), (0.0, 0.833885908126831, 0.5519368052482605, 238.8317205810547), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_09", ((-0.2756371796131134, 0.0, 0.9612616300582886, 187.9775390625), (0.9612616300582886, 1.2048483988280623e-08, 0.2756371796131134, -63.82964324951172), (0.0, 1.0, -4.371138828673793e-08, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_10", ((1.0, 0.0, 0.0, 156.5728759765625), (0.0, -4.371138828673793e-08, -1.0, -88.9984130859375), (0.0, 1.0, -4.371138828673793e-08, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_11", ((-0.27563735842704773, 0.0, 0.9612616896629333, 188.26702880859375), (0.9612616896629333, 1.20484919818864e-08, 0.27563735842704773, -79.35110473632812), (0.0, 1.0, -4.371138828673793e-08, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_12", ((-0.27563735842704773, 0.0, 0.9612616896629333, 188.12228393554688), (0.9612616896629333, 1.20484919818864e-08, 0.27563735842704773, -71.59036254882812), (0.0, 1.0, -4.371138828673793e-08, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_13", ((-0.27563735842704773, 0.0, 0.9612616896629333, 188.4117889404297), (0.9612616896629333, 1.20484919818864e-08, 0.27563735842704773, -87.11184692382812), (0.0, 1.0, -4.371138828673793e-08, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_14", ((-0.27563735842704773, 0.0, 0.9612616896629333, 246.75924682617188), (0.9612616896629333, 1.20484919818864e-08, 0.27563735842704773, -54.776493072509766), (0.0, 1.0, -4.371138828673793e-08, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_15", ((-0.27563735842704773, 0.0, 0.9612616896629333, 246.90399169921875), (0.9612616896629333, 1.20484919818864e-08, 0.27563735842704773, -62.537227630615234), (0.0, 1.0, -4.371138828673793e-08, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_16", ((-0.27563735842704773, 0.0, 0.9612616896629333, 247.0487518310547), (0.9612616896629333, 1.20484919818864e-08, 0.27563735842704773, -70.29796600341797), (0.0, 1.0, -4.371138828673793e-08, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_17", ((-0.2756371796131134, 0.0, 0.9612616300582886, 305.3962097167969), (0.9612616300582886, 1.2048483988280623e-08, 0.2756371796131134, -37.96263885498047), (0.0, 1.0, -4.371138828673793e-08, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_18", ((-0.2756371796131134, 0.0, 0.9612616300582886, 305.54095458984375), (0.9612616300582886, 1.2048483988280623e-08, 0.2756371796131134, -45.7233772277832), (0.0, 1.0, -4.371138828673793e-08, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_19", ((-0.2756371796131134, 0.0, 0.9612616300582886, 305.68572998046875), (0.9612616300582886, 1.2048483988280623e-08, 0.2756371796131134, -53.48411178588867), (0.0, 1.0, -4.371138828673793e-08, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_20", ((-0.2756371796131134, 0.0, 0.9612616300582886, 246.61448669433594), (0.9612616300582886, 1.2048483988280623e-08, 0.2756371796131134, -47.015769958496094), (0.0, 1.0, -4.371138828673793e-08, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_21", ((-0.2756371796131134, 0.0, 0.9612616300582886, 190.47906494140625), (0.9612616300582886, 1.2048483988280623e-08, 0.2756371796131134, -94.3213119506836), (0.0, 1.0, -4.371138828673793e-08, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_22", ((-0.2756371796131134, 0.0, 0.9612616300582886, 249.11602783203125), (0.9612616300582886, 1.2048483988280623e-08, 0.2756371796131134, -77.50743865966797), (0.0, 1.0, -4.371138828673793e-08, 254.75), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_23", ((0.521885573864, -0.318852335215, 0.791182041168, 313.026641846), (0.184063658118, 0.947755277157, 0.260539084673, -48.8581619263), (-0.832920372486, 0.00965646654367, 0.553308904171, 254.139271851), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_24", ((0.521885573864, -0.318852335215, 0.791182041168, 310.635253906), (0.184063658118, 0.947755277157, 0.260539084673, -41.75), (-0.832920372486, 0.00965646654367, 0.553308904171, 254.211705322), (0.0, 0.0, 0.0, 1.0))], 
    ]
    # 0.30901697278, 0.0, 0.951056540012, 282.5|0.951056540012, 1.91068546516e-15, -0.309017002583, -44.0|0.0, 1.0, -4.15720009528e-08, 254.75|0.0, 0.0, 0.0, 1.0
    for colNamePos in lstColNamePos:
        objectName = colNamePos[0]
        tuplePos = colNamePos[1]
        mPos = ptMatrix44()
        mPos.setData(tuplePos)
        bFirst = (objectName == "columnPhys_00")
        ret = CloneThem2(objName=objectName, age=ageName, iNbClones=0, iCurClone=0, bShow=False, bLoad=True, matPos=mPos, fct=PutItHere2, bAttach=attach, soAvatar=None, bFirstCol=bFirst)
    
    #return ret
    return 1

#------------------------------------------------------------------------------
"""
        #["columnPhys_04", ((0.28653037548065186, 0.0, 0.9580711722373962, 21.59333610534668), (0.9580711722373962, -1.2524640879973958e-08, -0.28653037548065186, 16.015239715576172), (0.0, 1.0, -4.371138828673793e-08, -4.454285144805908), (0.0, 0.0, 0.0, 1.0))], 
        #["columnPhys_05", ((0.28757917881011963, 0.0, 0.9577568769454956, 23.636314392089844), (0.9577568769454956, -1.25704850972852e-08, -0.28757917881011963, 22.048690795898438), (0.0, 1.0, -4.371138828673793e-08, -4.483102321624756), (0.0, 0.0, 0.0, 1.0))], 
        #["columnPhys_06", ((0.2913311719894409, 0.0, 0.956622302532196, 21.298192977905273), (0.956622302532196, -1.2734489907018087e-08, -0.2913311719894409, 9.792718887329102), (0.0, 1.0, -4.371138828673793e-08, -4.460986137390137), (0.0, 0.0, 0.0, 1.0))], 
        #["columnPhys_07", ((8.434057235717773e-05, 0.0, -1.0000001192092896, 15.191699028015137), (-1.0000001192092896, -3.686643438444159e-12, -8.434057235717773e-05, 12.870185852050781), (0.0, 1.0, -4.371138828673793e-08, -4.511136054992676), (0.0, 0.0, 0.0, 1.0))], 
        #["columnPhys_08", ((-0.0024155378341674805, 0.0, -0.999997079372406, 15.182741165161133), (-0.999997079372406, 1.0558651175607281e-10, 0.0024155378341674805, 20.503223419189453), (0.0, 1.0, -4.371138828673793e-08, -4.049295425415039), (0.0, 0.0, 0.0, 1.0))], 
        #["columnPhys_09", ((-0.08959567546844482, 0.0, 0.9959782361984253, 14.112927436828613), (0.9959782361984253, 3.916351243304916e-09, 0.08959567546844482, 18.960460662841797), (0.0, 1.0, -4.371138828673793e-08, -3.259999990463257), (0.0, 0.0, 0.0, 1.0))], 
        #["columnPhys_10", ((-0.06205892562866211, 0.0, 0.9980725646018982, 14.192145347595215), (0.9980725646018982, 2.712681856920085e-09, 0.06205892562866211, 13.573762893676758), (0.0, 1.0, -4.371138828673793e-08, -3.2668375968933105), (0.0, 0.0, 0.0, 1.0))], 
        #["columnPhys_11", ((0.9982282519340515, 0.0, -0.05950065329670906, 11.800867080688477), (-0.05950065329670906, -4.363394268125376e-08, -0.9982282519340515, 18.277984619140625), (0.0, 1.0, -4.371138828673793e-08, -3.2599997520446777), (0.0, 0.0, 0.0, 1.0))], 
        #["columnPhys_12", ((0.9602987766265869, 0.0, -0.2789737284183502, 21.367231369018555), (-0.2789737284183502, -4.197599423605425e-08, -0.9602987766265869, 16.011592864990234), (0.0, 1.0, -4.371138828673793e-08, -4.411989212036133), (0.0, 0.0, 0.0, 1.0))], 
        #["columnPhys_13", ((0.9602987766265869, 0.0, -0.2789737284183502, 24.56766700744629), (-0.2789737284183502, -4.197599423605425e-08, -0.9602987766265869, 15.081841468811035), (0.0, 1.0, -4.371138828673793e-08, -3.077113151550293), (0.0, 0.0, 0.0, 1.0))], 
        #["columnPhys_14", ((0.6368906497955322, -0.6368906497955322, -0.4344429075717926, 26.637561798095703), (-0.30719754099845886, 0.3071975111961365, -0.9006993770599365, 14.083449363708496), (0.7071068286895752, 0.7071067094802856, -3.0908616110991716e-08, -2.1252100467681885), (0.0, 0.0, 0.0, 1.0))], 
        #["columnPhys_15", ((0.43444302678108215, 0.0, 0.9006993770599365, 25.84137535095215), (0.9006993770599365, -1.899010726447159e-08, -0.43444299697875977, 14.46748161315918), (0.0, 1.0, -4.371138828673793e-08, -1.6629798412322998), (0.0, 0.0, 0.0, 1.0))], 
        #["columnPhys_16", ((0.43444302678108215, 0.45034971833229065, 0.7800285220146179, 47.778594970703125), (0.9006993770599365, -0.21722151339054108, -0.3762386739253998, 3.88629150390625), (0.0, 0.8660253882408142, -0.5000000596046448, -16.227561950683594), (0.0, 0.0, 0.0, 1.0))], 
        #["columnPhys_17", ((0.43444302678108215, 0.45034971833229065, 0.7800285220146179, 44.52027130126953), (0.9006993770599365, -0.21722151339054108, -0.3762386739253998, -2.8689537048339844), (0.0, 0.8660253882408142, -0.5000000596046448, -16.227561950683594), (0.0, 0.0, 0.0, 1.0))], 
        #["columnPhys_18", ((0.43444302678108215, 0.45034971833229065, 0.7800285220146179, 51.03691864013672), (0.9006993770599365, -0.21722151339054108, -0.3762386739253998, 10.641536712646484), (0.0, 0.8660253882408142, -0.5000000596046448, -16.227561950683594), (0.0, 0.0, 0.0, 1.0))], 
"""
# Mystitech platform for Baron city office
def Office(attach=False):
    ageName = "Jalak"
    lstColNamePos = [
        ["columnPhys_00", ((-1.0, 0.0, 0.0, -8.20), (0.0, 0.0, 1.0, 0.0), (0.0, 1.0, 0.0, -3.26), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_01", ((-1.0, 0.0, 0.0, -1.70), (0.0, 0.0, 1.0, 0.0), (0.0, 1.0, 0.0, -3.26), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_02", ((-1.0, 0.0, 0.0, 4.80), (0.0, 0.0, 1.0, 0.0), (0.0, 1.0, 0.0, -3.26), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_03", ((-1.0, 0.0, 0.0, 11.30), (0.0, 0.0, 1.0, 0.0), (0.0, 1.0, 0.0, -3.26), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_04", ((-1.0, 0.0, 0.0, 17.80), (0.0, 0.0, 1.0, 0.0), (0.0, 1.0, 0.0, -4.41), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_05", ((0.8667780756950378, -0.4041852653026581, -0.29212144017219543, 23.916330337524414), (-0.26475194096565247, 0.12345582246780396, -0.9563837647438049, 15.55703353881836), (0.4226182699203491, 0.9063077569007874, -3.961596917179122e-08, -3.447439193725586), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_06", ((0.47819069027900696, 0.8282506465911865, -0.2921215295791626, 21.725067138671875), (-0.1460607349872589, -0.2529846727848053, -0.9563813209533691, 16.226341247558594), (-0.866025447845459, 0.4999999701976776, -2.1855692367012125e-08, -4.414736270904541), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_07", ((0.29299914836883545, 0.32700982689857483, 0.8984520435333252, 50.934906005859375), (0.9561127424240112, -0.10021162033081055, -0.2753291130065918, 4.625577449798584), (0.0, 0.9396926164627075, -0.342020183801651, -12.512524604797363), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_08", ((0.29299914836883545, 0.32700982689857483, 0.8984520435333252, 52.83940124511719), (0.9561127424240112, -0.10021162033081055, -0.2753291130065918, 10.840309143066406), (0.0, 0.9396926164627075, -0.342020183801651, -12.512524604797363), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_09", ((0.29299914836883545, 0.32700982689857483, 0.8984520435333252, 54.743896484375), (0.9561127424240112, -0.10021163523197174, -0.2753291130065918, 17.055042266845703), (0.0, 0.9396926164627075, -0.342020183801651, -12.512524604797363), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_10", ((0.29299914836883545, 0.32700982689857483, 0.8984520435333252, 49.03041458129883), (0.9561127424240112, -0.10021163523197174, -0.2753291130065918, -1.5891566276550293), (0.0, 0.9396926164627075, -0.342020183801651, -12.512524604797363), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_11", ((-1.0, 0.0, 0.0, -16.303787231445312), (0.0, 4.371138828673793e-08, 1.0, 0.0), (0.0, 1.0, -4.371138828673793e-08, 3.237534523010254), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_12", ((-1.0, 0.0, 0.0, 16.196212768554688), (0.0, 4.371138828673793e-08, 1.0, -25.0), (0.0, 1.0, -4.371138828673793e-08, 3.237534523010254), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_13", ((4.371138828673793e-08, 0.0, 1.0, -0.05378689616918564), (1.0, -1.910685465164705e-15, 0.0, -34.27540588378906), (0.0, 1.0, -4.371138828673793e-08, 3.237534523010254), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_14", ((4.371138828673793e-08, 0.0, 1.0, -0.05378399044275284), (1.0, -1.910685465164705e-15, 0.0, 32.22459411621094), (0.0, 1.0, -4.371138828673793e-08, 3.237534523010254), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_15", ((0.8881563544273376, 0.0, -0.4595389664173126, -62.701786041259766), (-0.4595389664173126, -3.882254873133206e-08, -0.8881563544273376, 42.60573196411133), (0.0, 1.0, -4.371138828673793e-08, -5.344709873199463), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_16", ((0.8881563544273376, 0.0, -0.4595389664173126, -62.701786041259766), (-0.4595389664173126, -3.882254873133206e-08, -0.8881563544273376, 42.60573196411133), (0.0, 1.0, -4.371138828673793e-08, -5.344709873199463), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_17", ((0.8881563544273376, 0.0, -0.4595389664173126, -62.701786041259766), (-0.4595389664173126, -3.882254873133206e-08, -0.8881563544273376, 42.60573196411133), (0.0, 1.0, -4.371138828673793e-08, -5.344709873199463), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_18", ((0.8881563544273376, 0.0, -0.4595389664173126, -62.701786041259766), (-0.4595389664173126, -3.882254873133206e-08, -0.8881563544273376, 42.60573196411133), (0.0, 1.0, -4.371138828673793e-08, -5.344709873199463), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_19", ((0.8881563544273376, 0.0, -0.4595389664173126, -62.701786041259766), (-0.4595389664173126, -3.882254873133206e-08, -0.8881563544273376, 42.60573196411133), (0.0, 1.0, -4.371138828673793e-08, -5.344709873199463), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_20", ((0.8881563544273376, 0.0, -0.4595389664173126, -62.701786041259766), (-0.4595389664173126, -3.882254873133206e-08, -0.8881563544273376, 42.60573196411133), (0.0, 1.0, -4.371138828673793e-08, -5.344709873199463), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_21", ((0.8881563544273376, 0.0, -0.4595389664173126, -62.701786041259766), (-0.4595389664173126, -3.882254873133206e-08, -0.8881563544273376, 42.60573196411133), (0.0, 1.0, -4.371138828673793e-08, -5.344709873199463), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_22", ((0.8881563544273376, 0.0, -0.4595389664173126, -62.701786041259766), (-0.4595389664173126, -3.882254873133206e-08, -0.8881563544273376, 42.60573196411133), (0.0, 1.0, -4.371138828673793e-08, -5.344709873199463), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_23", ((0.8881563544273376, 0.0, -0.4595389664173126, -62.701786041259766), (-0.4595389664173126, -3.882254873133206e-08, -0.8881563544273376, 42.60573196411133), (0.0, 1.0, -4.371138828673793e-08, -5.344709873199463), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_24", ((0.8881563544273376, 0.0, -0.4595389664173126, -62.701786041259766), (-0.4595389664173126, -3.882254873133206e-08, -0.8881563544273376, 42.60573196411133), (0.0, 1.0, -4.371138828673793e-08, -5.344709873199463), (0.0, 0.0, 0.0, 1.0))], 
    ]
    for colNamePos in lstColNamePos:
        objectName = colNamePos[0]
        tuplePos = colNamePos[1]
        mPos = ptMatrix44()
        mPos.setData(tuplePos)
        bFirst = (objectName == "columnPhys_00")
        ret = CloneThem2(objName=objectName, age=ageName, iNbClones=0, iCurClone=0, bShow=False, bLoad=True, matPos=mPos, fct=PutItHere2, bAttach=attach, soAvatar=None, bFirstCol=bFirst)
    #return ret
    return 1

#------------------------------------------------------------------------------

# Cavern Tour Platform for Ahnonay Sphere 4 - Walkway from Statue to Maintenance Room
def StatueMaintRoom(attach=False):
    ageName = "Jalak"
    lstColNamePos = [
        ["columnPhys_00", ((-0.9969649314880371, 0.0, 0.07785340398550034, -29.85672378540039), (0.07785340398550034, 4.357872285254416e-08, 0.9969649314880371, 149.868896484375), (0.0, 1.0, -4.371138828673793e-08, 79.80290222167969), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_01", ((-0.9969649314880371, 0.0, 0.07785340398550034, -23.37645149230957), (0.07785340398550034, 4.357872285254416e-08, 0.9969649314880371, 149.36285400390625), (0.0, 1.0, -4.371138828673793e-08, 79.80290222167969), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_02", ((-0.9969649314880371, 0.0, 0.07785340398550034, -18.70524787902832), (0.07785340398550034, 4.357872285254416e-08, 0.9969649314880371, 209.18075561523438), (0.0, 1.0, -4.371138828673793e-08, 79.80289459228516), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_03", ((-0.9969649314880371, 0.0, 0.07785340398550034, -14.034042358398438), (0.07785340398550034, 4.357872285254416e-08, 0.9969649314880371, 268.9986572265625), (0.0, 1.0, -4.371138828673793e-08, 79.80289459228516), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_04", ((-0.9969649314880371, 0.0, 0.07785340398550034, -9.362838745117188), (0.07785340398550034, 4.357872285254416e-08, 0.9969649314880371, 328.8165283203125), (0.0, 1.0, -4.371138828673793e-08, 79.80289459228516), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_05", ((-0.9969649314880371, 0.0, 0.07785340398550034, -4.6916351318359375), (0.07785340398550034, 4.357872285254416e-08, 0.9969649314880371, 388.63446044921875), (0.0, 1.0, -4.371138828673793e-08, 79.80288696289062), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_06", ((-0.9969649314880371, 0.0, 0.07785340398550034, -0.020429611206054688), (0.07785340398550034, 4.357872285254416e-08, 0.9969649314880371, 448.45233154296875), (0.0, 1.0, -4.371138828673793e-08, 79.80288696289062), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_07", ((-0.9969649314880371, 0.0, 0.07785340398550034, 4.650774002075195), (0.07785340398550034, 4.357872285254416e-08, 0.9969649314880371, 508.27020263671875), (0.0, 1.0, -4.371138828673793e-08, 79.80288696289062), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_08", ((-0.9969649314880371, 0.0, 0.07785340398550034, -25.18552017211914), (0.07785340398550034, 4.357872285254416e-08, 0.9969649314880371, 209.68679809570312), (0.0, 1.0, -4.371138828673793e-08, 79.80289459228516), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_09", ((-0.9969649314880371, 0.0, 0.07785340398550034, -20.514314651489258), (0.07785340398550034, 4.357872285254416e-08, 0.9969649314880371, 269.50469970703125), (0.0, 1.0, -4.371138828673793e-08, 79.80289459228516), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_10", ((-0.9969649314880371, 0.0, 0.07785340398550034, -15.843111038208008), (0.07785340398550034, 4.357872285254416e-08, 0.9969649314880371, 329.32257080078125), (0.0, 1.0, -4.371138828673793e-08, 79.80289459228516), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_11", ((-0.9969649314880371, 0.0, 0.07785340398550034, -11.171907424926758), (0.07785340398550034, 4.357872285254416e-08, 0.9969649314880371, 389.1405029296875), (0.0, 1.0, -4.371138828673793e-08, 79.80288696289062), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_12", ((-0.9969649314880371, 0.0, 0.07785340398550034, -6.500701904296875), (0.07785340398550034, 4.357872285254416e-08, 0.9969649314880371, 448.9583740234375), (0.0, 1.0, -4.371138828673793e-08, 79.80288696289062), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_13", ((-0.9969649314880371, 0.0, 0.07785340398550034, -1.829498291015625), (0.07785340398550034, 4.357872285254416e-08, 0.9969649314880371, 508.7762451171875), (0.0, 1.0, -4.371138828673793e-08, 79.80288696289062), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_14", ((-0.2847384214401245, 0.27191635966300964, -0.919231116771698, -3.5654807090759277), (-0.9582924246788025, -0.056239958852529526, 0.28020167350769043, 528.9560546875), (0.02449386566877365, 0.9606760740280151, 0.276589035987854, 79.93170928955078), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_15", ((-0.2847384214401245, 0.27191635966300964, -0.919231116771698, -1.714680790901184), (-0.9582924246788025, -0.056239958852529526, 0.28020167350769043, 535.1849365234375), (0.02449386566877365, 0.9606760740280151, 0.276589035987854, 79.77249908447266), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_16", ((0.08542925119400024, 0.6404377818107605, 0.7632439732551575, -448.31494140625), (0.996344268321991, -0.05491286888718605, -0.06544256210327148, -862.4940795898438), (0.0, 0.7660444378852844, -0.6427876949310303, -891.3477783203125), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_17", ((0.08542925119400024, 0.6404377818107605, 0.7632439732551575, -448.9556579589844), (0.996344268321991, -0.05491286888718605, -0.06544256210327148, -869.9666748046875), (0.0, 0.7660444378852844, -0.6427876949310303, -891.3477783203125), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_18", ((0.08542925119400024, 0.6404377818107605, 0.7632439732551575, -449.59637451171875), (0.996344268321991, -0.05491286888718605, -0.06544256210327148, -877.4392700195312), (0.0, 0.7660444378852844, -0.6427876949310303, -891.3477783203125), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_19", ((0.08542925119400024, 0.6404377818107605, 0.7632439732551575, -450.2370910644531), (0.996344268321991, -0.05491286888718605, -0.06544256210327148, -884.911865234375), (0.0, 0.7660444378852844, -0.6427876949310303, -891.3477783203125), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_20", ((0.08542925119400024, 0.6404377818107605, 0.7632439732551575, -450.8778076171875), (0.996344268321991, -0.05491286888718605, -0.06544256210327148, -892.3843994140625), (0.0, 0.7660444378852844, -0.6427876949310303, -891.3477783203125), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_21", ((0.08542925119400024, 0.6404377818107605, 0.7632439732551575, -451.5185241699219), (0.996344268321991, -0.05491286888718605, -0.06544256210327148, -899.8569946289062), (0.0, 0.7660444378852844, -0.6427876949310303, -891.3477783203125), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_22", ((0.08542925119400024, 0.6404377818107605, 0.7632439732551575, -452.15924072265625), (0.996344268321991, -0.05491286888718605, -0.06544256210327148, -907.32958984375), (0.0, 0.7660444378852844, -0.6427876949310303, -891.3477783203125), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_23", ((0.08542925119400024, 0.6404377818107605, 0.7632439732551575, -452.79998779296875), (0.996344268321991, -0.05491286888718605, -0.06544256210327148, -914.8021850585938), (0.0, 0.7660444378852844, -0.6427876949310303, -891.3477783203125), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_24", ((0.08542925119400024, 0.6404377818107605, 0.7632439732551575, -442.8709411621094), (0.996344268321991, -0.05491286888718605, -0.06544256210327148, -855.433349609375), (0.0, 0.7660444378852844, -0.6427876949310303, -885.6024780273438), (0.0, 0.0, 0.0, 1.0))], 
    ]
    for colNamePos in lstColNamePos:
        objectName = colNamePos[0]
        tuplePos = colNamePos[1]
        mPos = ptMatrix44()
        mPos.setData(tuplePos)
        bFirst = (objectName == "columnPhys_00")
        ret = CloneThem2(objName=objectName, age=ageName, iNbClones=0, iCurClone=0, bShow=False, bLoad=True, matPos=mPos, fct=PutItHere2, bAttach=attach, soAvatar=None, bFirstCol=bFirst)
    #return ret
    return 1

#------------------------------------------------------------------------------

# Cavern Tour Platform for City Guild Hall corridor
def CreatePlatformForGuildHall(attach=False):
    ageName = "Jalak"
    lstColNamePos = [
        ["columnPhys_00", ((0.9999816417694092, 0.0, 0.0060677179135382175, 5.227876663208008), (0.0060677179135382175, -4.371058537344652e-08, -0.9999816417694092, 261.6741027832031), (0.0, 1.0, -4.371138828673793e-08, 217.6826171875), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_01", ((0.9999816417694092, 0.0, 0.0060677179135382175, -0.43932634592056274), (0.0060677179135382175, -4.371058537344652e-08, -0.9999816417694092, 261.6398620605469), (0.0, 1.0, -4.371138828673793e-08, 217.6826171875), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_02", ((0.9999816417694092, 0.0, 0.0060677179135382175, -5.773810863494873), (0.0060677179135382175, -4.371058537344652e-08, -0.9999816417694092, 261.6076354980469), (0.0, 1.0, -4.371138828673793e-08, 217.6826171875), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_03", ((0.9999816417694092, 0.0, 0.0060677179135382175, -5.417803764343262), (0.0060677179135382175, -4.371058537344652e-08, -0.9999816417694092, 202.93580627441406), (0.0, 1.0, -4.371138828673793e-08, 217.6826171875), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_04", ((0.9999816417694092, 0.0, 0.0060677179135382175, 0.5837239623069763), (0.0060677179135382175, -4.371058537344652e-08, -0.9999816417694092, 202.9722900390625), (0.0, 1.0, -4.371138828673793e-08, 217.6826171875), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_05", ((0.9999816417694092, 0.0, 0.0060677179135382175, 4.917374134063721), (0.0060677179135382175, -4.371058537344652e-08, -0.9999816417694092, 202.99862670898438), (0.0, 1.0, -4.371138828673793e-08, 217.6826171875), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_06", ((0.9999816417694092, 0.0, 0.0060677179135382175, 5.276102066040039), (0.0060677179135382175, -4.371058537344652e-08, -0.9999816417694092, 143.99224853515625), (0.0, 1.0, -4.371138828673793e-08, 217.6826171875), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_07", ((0.9999816417694092, 0.0, 0.0060677179135382175, 0.27513039112091064), (0.0060677179135382175, -4.371058537344652e-08, -0.9999816417694092, 143.96185302734375), (0.0, 1.0, -4.371138828673793e-08, 217.6826171875), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_08", ((0.9999816417694092, 0.0, 0.0060677179135382175, -5.39499044418335), (0.0060677179135382175, -4.371058537344652e-08, -0.9999816417694092, 143.9274444580078), (0.0, 1.0, -4.371138828673793e-08, 217.6826171875), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_09", ((0.9999816417694092, 0.0, 0.0060677179135382175, -5.032904148101807), (0.0060677179135382175, -4.371058537344652e-08, -0.9999816417694092, 84.25447845458984), (0.0, 1.0, -4.371138828673793e-08, 217.6826171875), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_10", ((0.9999816417694092, 0.0, 0.0060677179135382175, -0.03189775347709656), (0.0060677179135382175, -4.371058537344652e-08, -0.9999816417694092, 84.2848129272461), (0.0, 1.0, -4.371138828673793e-08, 217.6826171875), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_11", ((0.9999816417694092, 0.0, 0.0060677179135382175, 5.968896865844727), (0.0060677179135382175, -4.371058537344652e-08, -0.9999816417694092, 84.32120513916016), (0.0, 1.0, -4.371138828673793e-08, 217.6826171875), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_12", ((0.9999816417694092, 0.0, 0.0060677179135382175, 6.333001613616943), (0.0060677179135382175, -4.371058537344652e-08, -0.9999816417694092, 24.3153018951416), (0.0, 1.0, -4.371138828673793e-08, 217.6826171875), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_13", ((0.9999816417694092, 0.0, 0.0060677179135382175, 0.3326256573200226), (0.0060677179135382175, -4.371058537344652e-08, -0.9999816417694092, 24.278894424438477), (0.0, 1.0, -4.371138828673793e-08, 217.6826171875), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_14", ((0.9999816417694092, 0.0, 0.0060677179135382175, -5.667873382568359), (0.0060677179135382175, -4.371058537344652e-08, -0.9999816417694092, 24.24248695373535), (0.0, 1.0, -4.371138828673793e-08, 217.6826171875), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_15", ((-0.9999816417694092, 0.0, -0.006067630369216204, -11.145983695983887), (-0.006067630369216204, 4.371058537344652e-08, 0.9999816417694092, 102.54813385009766), (0.0, 1.0, -4.371138828673793e-08, 217.6826171875), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_16", ((-0.9999816417694092, 0.0, -0.006067630369216204, -11.506025314331055), (-0.006067630369216204, 4.371058537344652e-08, 0.9999816417694092, 161.88485717773438), (0.0, 1.0, -4.371138828673793e-08, 217.6826171875), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_17", ((-0.9999816417694092, 0.0, -0.006067630369216204, -11.864089012145996), (-0.006067630369216204, 4.371058537344652e-08, 0.9999816417694092, 220.89492797851562), (0.0, 1.0, -4.371138828673793e-08, 217.6826171875), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_18", ((-0.9999816417694092, 0.0, -0.006067630369216204, -11.560931205749512), (-0.006067630369216204, 4.371058537344652e-08, 0.9999816417694092, 280.9142761230469), (0.0, 1.0, -4.371138828673793e-08, 217.6826171875), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_19", ((0.9999816417694092, 0.0, 0.00606754282489419, 11.104362487792969), (0.00606754282489419, -4.371058537344652e-08, -0.9999816417694092, 281.7207336425781), (0.0, 1.0, -4.371138828673793e-08, 217.6826171875), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_20", ((0.9999816417694092, 0.0, 0.00606754282489419, 11.462421417236328), (0.00606754282489419, -4.371058537344652e-08, -0.9999816417694092, 222.7094268798828), (0.0, 1.0, -4.371138828673793e-08, 217.6826171875), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_21", ((0.9999816417694092, 0.0, 0.00606754282489419, 11.82415771484375), (0.00606754282489419, -4.371058537344652e-08, -0.9999816417694092, 163.0362548828125), (0.0, 1.0, -4.371138828673793e-08, 217.6826171875), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_22", ((0.9999816417694092, 0.0, 0.00606754282489419, 12.182174682617188), (0.00606754282489419, -4.371058537344652e-08, -0.9999816417694092, 104.03250122070312), (0.0, 1.0, -4.371138828673793e-08, 217.6826171875), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_23", ((0.9999816417694092, 0.0, 0.00606754282489419, 12.542203903198242), (0.00606754282489419, -4.371058537344652e-08, -0.9999816417694092, 44.697105407714844), (0.0, 1.0, -4.371138828673793e-08, 217.6826171875), (0.0, 0.0, 0.0, 1.0))], 
        ["columnPhys_24", ((0.9999816417694092, 0.0, 0.00606754282489419, -10.455595970153809), (0.00606754282489419, -4.371058537344652e-08, -0.9999816417694092, 43.557167053222656), (0.0, 1.0, -4.371138828673793e-08, 217.6826171875), (0.0, 0.0, 0.0, 1.0))], 
    ]
    for colNamePos in lstColNamePos:
        objectName = colNamePos[0]
        tuplePos = colNamePos[1]
        mPos = ptMatrix44()
        mPos.setData(tuplePos)
        bFirst = (objectName == "columnPhys_00")
        ret = CloneThem2(objName=objectName, age=ageName, iNbClones=0, iCurClone=0, bShow=False, bLoad=True, matPos=mPos, fct=PutItHere2, bAttach=attach, soAvatar=None, bFirstCol=bFirst)
    #return ret
    return 1

#------------------------------------------------------------------------------



#=========================================
# Move object where I am
def Move(objectName="PillarLower01", ageName="Ahnonay", bShow=True, matAv=None, bAttach=False):
    #objNameBase = "columnPhys_"
    #ageName = "Jalak"
    playerID = PtGetLocalPlayer().getPlayerID()
    soAvatar = PtGetLocalAvatar()
    print("Player is myself")

    # Initialization
    #curCol = 25
    # avatar's position
    if isinstance(matAv, ptMatrix44):
        matAvatar = matAv
    else:
        matAvatar = soAvatar.getLocalToWorld()
    
    # B 1
    #curCol = curCol - 1
    matTrans = ptMatrix44()
    #matTrans.translate(ptVector3(-3.75 + (7.50 * 9), 4.25, 0.0)) 
    #objectName = objNameBase + str(curCol).zfill(2)
    ret = CloneColumns2(objName=objectName, age=ageName, bLoadOn=True, bShowOn=bShow, iNbCol=0, iCurCol=0, matAv=matAvatar, mTrans=matTrans, fXAngle=0, fYAngle=0, fZAngle=0, bAttachOn=bAttach, soAv=soAvatar, bFirst=False)
    
    #return ret
    return 1

#------------------------------------------------------------------------------

#=========================================
# CreatePlatform1 : Create a platform under me with 1 column of Jalak (mixo)
def CreatePlatform1(bShow=True, matAv=None):
    objNameBase = "columnPhys_"
    ageName = "Jalak"
    playerID = PtGetLocalPlayer().getPlayerID()
    soAvatar = PtGetLocalAvatar()
    print("Player is myself")

    # Initialization
    curCol = 25
    # avatar's position
    if isinstance(matAv, ptMatrix44):
        matAvatar = matAv
    else:
        matAvatar = soAvatar.getLocalToWorld()
    
    #
    curCol = curCol - 1
    matTrans = ptMatrix44()
    matTrans.translate(ptVector3(0.0, -3.25, 0.0)) 
    objectName = objNameBase + str(curCol).zfill(2)
    ret = CloneColumns2(objName=objectName, age=ageName, bLoadOn=True, bShowOn=bShow, iNbCol=0, iCurCol=curCol, matAv=matAvatar, mTrans=matTrans, fXAngle=0, fYAngle=0, fZAngle=0, bAttachOn=False, soAv=soAvatar, bFirst=False)
    #
    
    #return ret
    return 1

# Scale : Stretch the column
def Scale(bShow=True, matAv=None, scale=[1, 1, 1]):
    objNameBase = "columnPhys_"
    ageName = "Jalak"
    playerID = PtGetLocalPlayer().getPlayerID()
    soAvatar = PtGetLocalAvatar()
    print("Player is myself")

    # Initialization
    curCol = 25
    # avatar's position
    if isinstance(matAv, ptMatrix44):
        matAvatar = matAv
    else:
        matAvatar = soAvatar.getLocalToWorld()
    
    #
    curCol = curCol - 1
    objectName = objNameBase + str(curCol).zfill(2)
    #
    try:
        so = PtFindSceneobject(objectName, ageName)
    except:
        print("{} not found in {}".format(objName, ageName))
        return 0
    if isinstance(so, ptSceneobject):
        # rotations:
        mRotX = ptMatrix44()
        fXAngle = -90.0
        mRotX.rotate(0, (math.pi * float(fXAngle)) / 180.0)
        mPos = matAvatar * mRotX
        
        mTrans = ptMatrix44()
        mTrans.translate(ptVector3(0.0, -3.25, 30.0))
        mPos = mPos * mTrans

        mscale = ptMatrix44()
        mscale.makeScaleMat(ptVector3(scale[0], scale[1], scale[2]))
        so.netForce(True)
        so.physics.warp(mPos * mscale)
        so.physics.enable(True)
    #
    
    #return ret
    return 1
