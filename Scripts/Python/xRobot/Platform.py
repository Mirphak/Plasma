# -*- coding: utf-8 -*-
# == Script pour faire une plateforme avec les colonnes de Jalak Dador en chargeant le prp ==
# Mirphak 2015-11-01 version 1

from Plasma import *
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
    
    def __init__(self, objectName="columnPhys_00", ageFileName="Jalak", bFirst=False, method=DoNothing, params=[]):
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
                    #PtSetAlarm(0, self, 2)
                    PtSetAlarm(.25, self, 2)
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
                PtSetAlarm(5, self, 3)
            else:
                PtSetAlarm(.25, self, 3)
        elif context == 3:
            print "AlarmAddPrp: 3 - Execute the method"
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
    names = ["Camera", "Field", "Link"
        "Start", "Terrain", "Wall0"]
    PhysObjectList("Jalak", names, False)

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

#=========================================
# detacher so1 de so2 : detach(obj, av) ou l'inverse    
def Detacher(so1, so2):
    so1.physics.netForce(1)
    so1.draw.netForce(1)
    PtDetachObject(so1, so2, 1)

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
            ## Attendre que les clones soient prets et les manipuler
            print "objName={}, age={}, nb={}, fct={}, so={}, bShow={}, iCurClone={}, matPos={}, bPhys={}, bAttach={}, soAvatar={}".format(objName, age, nb, fct, so, bShow, iCurClone, matPos, True, bAttach, soAvatar)
            PtSetAlarm (0, AlarmAddPrp(objectName="columnPhys_00", ageFileName="Jalak", bFirst=bFirstCol, method=fct, params=[so, bShow, iCurClone, matPos, True, bAttach, soAvatar]), 0)
            print "Clone of {} loaded".format(objName)
            msg += "Clone of {} loaded\n".format(objName)
        else:
            # Retour a la normale
            print "Clone of {} unloaded".format(objName)
            msg += "Clone of {} unloaded\n".format(objName)
    else:
        print "not a ptSceneobject!"
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
    print "Player is myself"

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
    print "Player is myself"

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
            print "{} not found in {}".format(objName, age)
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

#=========================================
# Move object where I am
def Move(objectName="PillarLower01", ageName="Ahnonay", bShow=True, matAv=None, bAttach=False):
    #objNameBase = "columnPhys_"
    #ageName = "Jalak"
    playerID = PtGetLocalPlayer().getPlayerID()
    soAvatar = PtGetLocalAvatar()
    print "Player is myself"

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

#
