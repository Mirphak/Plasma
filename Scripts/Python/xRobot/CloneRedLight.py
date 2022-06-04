# -*- coding: utf-8 -*-

from Plasma import *
import math
from . import CloneFactory

#=========================================
# Parameters: masterkey, bShow, iCurClone, matPos, bPhys
def PutItHere(params=[]):
    print("PutItHere begin")
    
    #Verifions les parametres
    # au moins 5 parametres
    if len(params) > 4:
        print("PutItHere params 4")
        try:
            bPhys = bool(params[4])
        except:
            bPhys = False
    else:
        bPhys = False
    # au moins 4 parametres
    if len(params) > 3:
        print("PutItHere params 2")
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
        print("PutItHere params 2")
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
        print("PutItHere params 1")
        try:
            bShow = bool(params[1])
        except:
            bShow = True
    else:
        bShow = True
    # au moins 1 parametre
    if len(params) > 0:
        print("PutItHere params 0")
        masterKey = params[0]
        if not isinstance(masterKey, ptKey):
            print("PutItHere: first paremeter must be a ptKey")
            return 1
    # pas de parametre
    if len(params) == 0:
        print("PutItHere: needs 1, 2, 3 or 4 paremeters")
        return 1
    
    print("PutItHere params ok")
    soMaster = masterKey.getSceneObject()
    print("PutItHere({}, {}, matPos)".format(soMaster.getName(), bShow))
    
    # Manipulons les clones
    cloneKeys = PtFindClones(masterKey)
    if len(cloneKeys) < 1:
        print("PutItHere no clone found!")
    else:
        print("PutItHere : the stuff") 
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

    print("PutItHere done")
    return 0

#=========================================
# Create N clones and put the choosen one somewhere
def CloneThem(objName, age, bShow=True, bLoad=True, iNbClones=10, iCurClone=0, matPos=None, fct=PutItHere):
    print("          ** cloneit ** 1 begin")
    msg = "CloneObject.cloneit(): "
    nb = iNbClones
    masterkey = None

    try:
        masterkey = PtFindSceneobject(objName, age).getKey()
    except:
        print("{} not found in {}".format(objName, age))
        msg += "{} not found in {}\n".format(objName, age)
    print("          ** cloneit ** 2")
    if isinstance(masterkey, ptKey):
        if bLoad:
            print("          ** clone1 ** 3 loading")
            # Combien de clones a-t-on deja?
            nbClones = len(PtFindClones(masterkey))
            print("Test : nb de clones de {} ==> {}".format(objName, nbClones))
            # Ajouter des clones si besoin
            if nbClones < nb:
                CloneFactory.CloneObject(objName, age, nb - nbClones)
            # Attendre que les clones soient prets et les manipuler
            PtSetAlarm(1, CloneFactory.AlarmWaittingForClones(objName, age, nb, fct, [masterkey, bShow, iCurClone, matPos, False]), 1)
            print("Clone of {} loaded".format(objName))
            msg += "Clone of {} loaded\n".format(objName)
        else:
            # Retour a la normale
            CloneFactory.DechargerClones(masterkey)
            #DayTime()
            print("Clone of {} unloaded".format(objName))
            msg += "Clone of {} unloaded\n".format(objName)
    else:
        print("not a ptKey!")
        msg += "not a ptKey\n"
    return msg

# Clones of Red Pulsing Light of Testsonot for dance floor in pyramid of Kadish
def RedFloor(bShowOn=True, bLoadOn=True):
    #Default values
    ageName = "Tetsonot"
    obj = "RTWindowOmni03"
    #bOnOff = True
    nb = 34
    num = 0
    x = 0
    y = 0
    z = -48
    bAttacher = False
    # List of the 34 positions [x, y]
    """
        1   2   3   4   5   6   7
    1               12
    2           6       19
    3       2       13      25
    4   0       7       20      30
    5       3       14      26
    6   1       8       21      31
    7       4       15      27
    8   -       9       22      32
    9       5       16      28
    10  -       10      23      33
    11      -       17      29
    12          11      24
    13              18
    """
    positions = [
        [687, -122], #  0
        [687, -114], #  1
        [695, -134], #  2
        [695, -126], #  3
        [695, -118], #  4
        [695, -110], #  5
        [703, -150], #  [703, -146], #  6 
        [703, -138], #  7
        [703, -130], #  8
        [703, -122], #  9
        [703, -114], # 10
        [703, -106], # 11
        [712, -154], # [711, -150], # 12 
        [711, -142], # 13
        [711, -134], # 14
        [711, -126], # 15
        [711, -118], # 16
        [711, -110], # 17
        [711, -102], # 18
        [719, -146], # 19
        [719, -138], # 20
        [719, -130], # 21
        [719, -122], # 22
        [719, -114], # 23
        [719, -106], # 24
        [727, -145], # [727, -142], # 25 
        [727, -134], # 26
        [727, -126], # 27
        [727, -118], # 28
        [727, -110], # 29
        [735, -140], # [735, -138], # 30 
        [735, -130], # 31
        [735, -122], # 32
        [735, -114]  # 33
    ]
    #
    for num in range(0, 34):
        pos = ptMatrix44()
        pos.translate(ptVector3(positions[num][0], positions[num][1], z))
        CloneThem(objName=obj, age=ageName, bShow=bShowOn, bLoad=bLoadOn, iNbClones=nb, iCurClone=num, matPos=pos, fct=PutItHere)

# Clones of Red Pulsing Light of Testsonot for dance floor in pyramid of Kadish
def RedFloor2(bShowOn=True, bLoadOn=True):
    #Default values
    ageName = "Tetsonot"
    obj = "RTWindowOmni03"
    #bOnOff = True
    nb = 34
    num = 0
    x = 0
    y = 0
    z = -48
    bAttacher = False
    # List of the 34 positions [x, y]
    """
        1   2   3   4   5   6   7
    1               12
    2           6       19
    3       2       13      25
    4   0       7       20      30
    5       3       14      26
    6   1       8       21      31
    7       4       15      27
    8   -       9       22      32
    9       5       16      28
    10  -       10      23      33
    11      -       17      29
    12          11      24
    13              18
    """
    positions = [
        [687, -122], #  0
        [687, -114], #  1
        [695, -134], #  2
        [695, -126], #  3
        [695, -118], #  4
        [695, -110], #  5
        [703, -150], #  [703, -146], #  6 
        [703, -138], #  7
        [703, -130], #  8
        [703, -122], #  9
        [703, -114], # 10
        [703, -106], # 11
        [712, -154], # [711, -150], # 12 
        [711, -142], # 13
        [711, -134], # 14
        [711, -126], # 15
        [711, -118], # 16
        [711, -110], # 17
        [711, -102], # 18
        [719, -146], # 19
        [719, -138], # 20
        [719, -130], # 21
        [719, -122], # 22
        [719, -114], # 23
        [719, -106], # 24
        [727, -145], # [727, -142], # 25 
        [727, -134], # 26
        [727, -126], # 27
        [727, -118], # 28
        [727, -110], # 29
        [735, -140], # [735, -138], # 30 
        [735, -130], # 31
        [735, -122], # 32
        [735, -114]  # 33
    ]
    #
    for num in range(0, 34):
        pos = ptMatrix44()
        pos.translate(ptVector3(positions[num][0]-233, positions[num][1]-87, z-13))
        CloneThem(objName=obj, age=ageName, bShow=bShowOn, bLoad=bLoadOn, iNbClones=nb, iCurClone=num, matPos=pos, fct=PutItHere)

# test
def test(n=0):
    motifs = [
        # 0     1      2      3      4      5      6      7      8      9      10     11     12     13     14     15     16     17     18     19     20
        [False, True, True , False, False, True , True , False, False, False, False, False, False, False, False, True , False, False, False, True , False], #  0
        [False, True, False, True , False, True , True , False, False, False, False, False, False, False, False, False, True , False, False, False, True ], #  1
        [False, True, False, True , False, True , False, True , False, False, False, False, False, False, True , False, False, True , False, False, False], #  2
        [False, True, True , False, True , False, False, True , False, False, False, False, False, False, False, True , False, False, True , False, False], #  3
        [False, True, False, True , True , False, False, True , False, False, False, False, False, False, False, False, True , False, False, False, False], #  4
        [False, True, True , False, True , False, False, True , False, False, False, False, False, False, False, True , False, False, False, True , True ], #  5
        [False, True, False, True , False, True , False, False, True , False, False, False, False, True , False, False, False, False, False, True , False], #  6 
        [False, True, True , False, True , False, False, False, True , False, False, False, False, False, True , False, False, False, True , False, False], #  7
        [False, True, False, True , False, True , False, False, True , False, False, False, False, False, False, True , False, True , False, False, False], #  8
        [False, True, True , False, False, True , False, False, True , False, False, False, False, False, False, False, True , False, True , False, False], #  9
        [False, True, False, True , True , False, False, False, True , False, False, False, False, False, False, True , False, False, False, True , False], # 10
        [False, True, True , False, False, True , False, False, True , False, False, False, False, False, True , False, False, False, False, False, True ], # 11
        [False, True, False, True , False, True , False, False, False, True , False, False, False, True , False, False, False, False, False, False, True ], # 12 
        [False, True, True , False, True , False, False, False, False, True , False, False, False, False, True , False, False, False, False, True , False], # 13
        [False, True, False, True , False, True , False, False, False, True , False, False, False, False, False, True , False, False, True , False, False], # 14
        [False, True, True , False, True , False, False, False, False, True , False, False, False, False, False, False, True , True , False, False, False], # 15
        [False, True, False, True , False, True , False, False, False, True , False, False, False, False, False, True , False, False, True , False, False], # 16
        [False, True, True , False, True , False, False, False, False, True , False, False, False, False, True , False, False, False, False, True , False], # 17
        [False, True, False, True , False, True , False, False, False, True , False, False, False, True , False, False, False, False, False, False, True ], # 18
        [False, True, True , False, False, True , False, False, False, False, True , False, False, False, True , False, False, False, False, False, True ], # 19
        [False, True, False, True , True , False, False, False, False, False, True , False, False, False, False, True , False, False, False, True , False], # 20
        [False, True, True , False, False, True , False, False, False, False, True , False, False, False, False, False, True , False, True , False, False], # 21
        [False, True, False, True , False, True , False, False, False, False, True , False, False, False, False, True , False, True , False, False, False], # 22
        [False, True, True , False, True , False, False, False, False, False, True , False, False, False, True , False, False, False, True , False, False], # 23
        [False, True, False, True , False, True , False, False, False, False, True , False, False, True , False, False, False, False, False, True , False], # 24
        [False, True, True , False, False, True , False, False, False, False, False, True , False, False, False, True , False, False, False, False, True ], # 25 
        [False, True, False, True , True , False, False, False, False, False, False, True , False, False, False, False, True , False, False, True , False], # 26
        [False, True, True , False, True , False, False, False, False, False, False, True , False, False, False, True , False, False, True , False, False], # 27
        [False, True, False, True , True , False, False, False, False, False, False, True , False, False, True , False, False, True , False, False, False], # 28
        [False, True, True , False, False, True , False, False, False, False, False, True , False, True , False, False, False, False, True , False, False], # 29
        [False, True, False, True , False, True , False, False, False, False, False, False, True , False, False, False, True , False, False, False, True ], # 30 
        [False, True, True , False, False, True , False, False, False, False, False, False, True , False, False, True , False, False, False, True , False], # 31
        [False, True, False, True , False, True , False, False, False, False, False, False, True , False, True , False, False, False, True , False, False], # 32
        [False, True, True , False, False, True , False, False, False, False, False, False, True , True , False, False, False, True , False, False, False]  # 33
    ]
    
    masterKey = PtFindSceneobject("RTWindowOmni03", "Tetsonot").getKey()
    cloneKeys = PtFindClones(masterKey)
    for iCurClone in range(0, min(len(cloneKeys) - 1, 34)):
        ck = cloneKeys[iCurClone]
        soTop = ck.getSceneObject()
        soTop.netForce(1)
        soTop.draw.enable(motifs[iCurClone][n])

# test un seul
def testun(n=0):
    masterKey = PtFindSceneobject("RTWindowOmni03", "Tetsonot").getKey()
    cloneKeys = PtFindClones(masterKey)
    for iCurClone in range(0, min(len(cloneKeys) - 1, 34)):
        ck = cloneKeys[iCurClone]
        so = ck.getSceneObject()
        so.netForce(1)
        so.draw.enable(iCurClone==n)

#
class AutoLight:
    _running = False
    _motifs = [
        # 0     1      2      3      4      5      6      7      8      9      10     11     12     13     14     15     16     17     18     19     20
        [False, True, True , False, False, True , True , False, False, False, False, False, False, False, False, True , False, False, False, True , False], #  0
        [False, True, False, True , False, True , True , False, False, False, False, False, False, False, False, False, True , False, False, False, True ], #  1
        [False, True, False, True , False, True , False, True , False, False, False, False, False, False, True , False, False, True , False, False, False], #  2
        [False, True, True , False, True , False, False, True , False, False, False, False, False, False, False, True , False, False, True , False, False], #  3
        [False, True, False, True , True , False, False, True , False, False, False, False, False, False, False, False, True , False, False, False, False], #  4
        [False, True, True , False, True , False, False, True , False, False, False, False, False, False, False, True , False, False, False, True , True ], #  5
        [False, True, False, True , False, True , False, False, True , False, False, False, False, True , False, False, False, False, False, True , False], #  6 
        [False, True, True , False, True , False, False, False, True , False, False, False, False, False, True , False, False, False, True , False, False], #  7
        [False, True, False, True , False, True , False, False, True , False, False, False, False, False, False, True , False, True , False, False, False], #  8
        [False, True, True , False, False, True , False, False, True , False, False, False, False, False, False, False, True , False, True , False, False], #  9
        [False, True, False, True , True , False, False, False, True , False, False, False, False, False, False, True , False, False, False, True , False], # 10
        [False, True, True , False, False, True , False, False, True , False, False, False, False, False, True , False, False, False, False, False, True ], # 11
        [False, True, False, True , False, True , False, False, False, True , False, False, False, True , False, False, False, False, False, False, True ], # 12 
        [False, True, True , False, True , False, False, False, False, True , False, False, False, False, True , False, False, False, False, True , False], # 13
        [False, True, False, True , False, True , False, False, False, True , False, False, False, False, False, True , False, False, True , False, False], # 14
        [False, True, True , False, True , False, False, False, False, True , False, False, False, False, False, False, True , True , False, False, False], # 15
        [False, True, False, True , False, True , False, False, False, True , False, False, False, False, False, True , False, False, True , False, False], # 16
        [False, True, True , False, True , False, False, False, False, True , False, False, False, False, True , False, False, False, False, True , False], # 17
        [False, True, False, True , False, True , False, False, False, True , False, False, False, True , False, False, False, False, False, False, True ], # 18
        [False, True, True , False, False, True , False, False, False, False, True , False, False, False, True , False, False, False, False, False, True ], # 19
        [False, True, False, True , True , False, False, False, False, False, True , False, False, False, False, True , False, False, False, True , False], # 20
        [False, True, True , False, False, True , False, False, False, False, True , False, False, False, False, False, True , False, True , False, False], # 21
        [False, True, False, True , False, True , False, False, False, False, True , False, False, False, False, True , False, True , False, False, False], # 22
        [False, True, True , False, True , False, False, False, False, False, True , False, False, False, True , False, False, False, True , False, False], # 23
        [False, True, False, True , False, True , False, False, False, False, True , False, False, True , False, False, False, False, False, True , False], # 24
        [False, True, True , False, False, True , False, False, False, False, False, True , False, False, False, True , False, False, False, False, True ], # 25 
        [False, True, False, True , True , False, False, False, False, False, False, True , False, False, False, False, True , False, False, True , False], # 26
        [False, True, True , False, True , False, False, False, False, False, False, True , False, False, False, True , False, False, True , False, False], # 27
        [False, True, False, True , True , False, False, False, False, False, False, True , False, False, True , False, False, True , False, False, False], # 28
        [False, True, True , False, False, True , False, False, False, False, False, True , False, True , False, False, False, False, True , False, False], # 29
        [False, True, False, True , False, True , False, False, False, False, False, False, True , False, False, False, True , False, False, False, True ], # 30 
        [False, True, True , False, False, True , False, False, False, False, False, False, True , False, False, True , False, False, False, True , False], # 31
        [False, True, False, True , False, True , False, False, False, False, False, False, True , False, True , False, False, False, True , False, False], # 32
        [False, True, True , False, False, True , False, False, False, False, False, False, True , True , False, False, False, True , False, False, False]  # 33
    ]
    _masterKey = PtFindSceneobject("RTWindowOmni03", "Tetsonot").getKey()
    _n = 0
    
    def __init__(self):
        pass
    
    def onAlarm(self, param=1):
        if not self._running:
            return
        if PtGetAgeInfo().getAgeFilename() != "Kadish":
            self.Stop()
            return
        cloneKeys = PtFindClones(self._masterKey)
        for iCurClone in range(0, min(len(cloneKeys) - 1, 34)):
            ck = cloneKeys[iCurClone]
            so = ck.getSceneObject()
            so.netForce(1)
            so.draw.enable(self._motifs[iCurClone][self._n])
        self._n = (self._n + 1) % len(self._motifs[iCurClone])
        PtSetAlarm(1, self, 1)
    
    def Start(self):
        if not self._running:
            self._running = True
            self.onAlarm()
    
    def Stop(self):
        self._running = False
#
