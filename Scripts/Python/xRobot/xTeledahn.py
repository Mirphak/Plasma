# -*- coding: utf-8 -*-

"""
    Version 1 : 07/11/2015

    Version 2 : 14/01/2017
        Je voudrais savoir comment tout le monde dernière tournée est allé et 
        si vos vacances ont été un certain temps mais je vais être mentionner 
        les visites Cavern et des histoires à toutes les guildes réunion ce samedi.

        Was était se demander ce que vous les gars voudrais faire pour des effets spéciaux 
        ou même mélanger tour un peu sur cette prochaine tournée la semaine prochaine 
        pas demain le vendredi suivant /

        C'est Teledahn.

        =======================

        Nous saluons le retour.

        Nous sommes arrivés à travers les visites sans beaucoup de hangups, je dirais. 
        Peu d'autre chose peut être dit - Relto est un âge où il ya très peu à explorer.

        Teledahn est l'un des endroits où j'aime sortir de la grille autant que possible. 
        Sur l'autre île, ou du moins sur le dessus de la tour de bureau pour le voir. 
        Vers le bord de l'île où le ruisseau descend pour former la cascade. 
        Vers le bas sur l'eau pour voir le seau d'ascenseur. 
        Ce genre de chose.

        De l'expérience passée, nous savons aussi que nous devons nous téléporter autant que 
        possible pour éviter les ascenseurs et les échelles, car ils nous ralentissent beaucoup.

        Si une voie peut être trouvée pour mettre en évidence ou de contraste les glyphes dans 
        le tunnel d'admission d'eau, ce serait bien. 
        Nous avons toujours eu des problèmes avec les gens qui les voyaient clairement de tous 
        les postes.

        Le véritable problème est sur la fin de la conférence, cependant. 
        Garder les choses à une simple session de deux heures de visite est difficile!

        =======================
        Message d'avertissement sur le fait de se coincer sur les échelles.
        Préparez les chaînes. Nous ne sommes donc pas coincé dans les échelles.
        KI lumière, Invisibilité.

        Par la suite ...
        Minkata étage
        Shroomie

        Ne pense pas que je dois ajouter beaucoup. 
        Si autre que le ci-dessus, je vais avoir mes mains plein de gens se perdre ou collé.
"""

"""
    "t0":"LinkInPointDefault",        # = sp 0  = La hutte
        # tldnHarvest :                         
    "t1":"tldnJourneyCloth03POS",     # = sp 1  = Etoffe plage
    "t2":"Perf-SpawnPointExterior01", # = sp 2  = Generateur solaire
    "t3":"Perf-SpawnPointExterior02", # = sp 3  = Plage
    "t4":"DockStartPoint",            # = sp 4  = Ponton isole
    "t5":"StumpStartPoint",           # = sp 5  = Ilot isole
        # tldnLowerShroom :                     
    "t6":"tldnJourneyCloth06POS",     # = sp 6  = Etoffe hutte
    "t7":"Perf-SpawnPointInShroom",   # = sp 7  = La hutte
    "t8":"LinkInPointDefault",        # = sp 8  = La hutte = sp 0
    "t9":"LinkInPointUnderCabin",     # = sp 9  = Tuyau
        # tldnNoxiousCave :                     
    "t10":"tldnJourneyCloth02POS",    # = sp 10 = Etoffe porte bahro
    "t11":"NoxiousStart",             # = sp 11 = Porte Bahro
        # tldnSlaveCave :                       
    "t12":"tldnJourneyCloth01POS",    # = sp 12 = Etoffe Prison
    "t13":"Perf-SpawnPointSlaveCave", # = sp 13 = Prison
        # tldnSlaveShroom :                     
    "t14":"tldnJourneyCloth04POS",    # = sp 14 = Etoffe Bureau plage
    "t15":"LinkInWarshroomUpstairs",  # = sp 15 = Entrepot plage
        # tldnUpperShroom :                     
    "t16":"tldnJourneyCloth05POS",    # = sp 16 = Etoffe bureau shroom haut
    "t17":"LinkInPointUpperRoom",     # = sp 17 = Bureau shroom haut
        # tldnWorkroom :                        
    "t18":"tldnJourneyCloth07POS",    # = sp 18 = Etoffe Control Room
    "t19":"Perf-SpawnPointWorkroom",  # = sp 19 =  Control Room

"""

from Plasma import *

import Ride
import Platform
import math
import CloneFactory

"""
- ** onlake
- ** warp all
- ** platform
    . on the roof of the factory mushroom stalk
    . on the top of the mountain that the river flows down
- ** shroomie
- ** allowing avatars to fly along the buggaro routes
- Any additional effects you'd like to experiment with are welcome
    . ** !toggle Gate
    . ** night
    . ** cms (sans limite de temps)
    . mixo => event 2
    . ?? laser show ??
"""
# platform(name="sun") platform(name="roof")
def platform(name="sun"):
    matPos = None
    if name == "roof":
        tupPos = ((-0.931317865849, -0.364206343889, 0.0, -77.659538269), (0.364206343889, -0.931317865849, 0.0, -178.524871826), (0.0, 0.0, 1.0, 159.332183838), (0.0, 0.0, 0.0, 1.0)) 
        matPos = ptMatrix44()
        matPos.setData(tupPos)
    elif name == "sun":
        tupPos = ((-0.624134302139, -0.78131711483, 0.0, -1188.0), (0.78131711483, -0.624134302139, 0.0, -1138.0), (0.0, 0.0, 1.0, 221.0), (0.0, 0.0, 0.0, 1.0))
        matPos = ptMatrix44()
        matPos.setData(tupPos)
    else:
        pass
    Platform.CreatePlatform(bShow=False, matAv=matPos)

#
def panic():
    PtConsoleNet("Avatar.Spawn.DontPanic" , 1)

# wa(n="sun") wa(n="roof")
def wa(n=0):
    # les points de warp
    ws = { 
        "1": ((-0.444342970848, 0.895856797695, 0.0, -213.294143677), (-0.895856797695, -0.444342970848, 0.0, -322.820526123), (0.0, 0.0, 1.0, 13.7166614532), (0.0, 0.0, 0.0, 1.0)), 
        "2": ((-0.444342970848, 0.895856797695, 0.0, -104.294143677), (-0.895856797695, -0.444342970848, 0.0, -177.820526123), (0.0, 0.0, 1.0, 89.7166614532), (0.0, 0.0, 0.0, 1.0)), 
        "roof": ((-0.931317865849, -0.364206343889, 0.0, -77.659538269), (0.364206343889, -0.931317865849, 0.0, -178.524871826), (0.0, 0.0, 1.0, 159.332183838), (0.0, 0.0, 0.0, 1.0)), 
        "top": ((-0.212570428848, 0.977145791054, 0.0, -68.1296081543), (-0.977145791054, -0.212570428848, 0.0, -224.025436401), (0.0, 0.0, 1.0, 267.009216309), (0.0, 0.0, 0.0, 1.0)), 
        "sun": ((-0.624134302139, -0.78131711483, 0.0, -1188.0), (0.78131711483, -0.624134302139, 0.0, -1138.0), (0.0, 0.0, 1.0, 221.0), (0.0, 0.0, 0.0, 1.0))
        }
    #desactiver les zones de panique
    
    #recuperer tous les joueurs
    playerList = PtGetPlayerList()
    playerList.append(PtGetLocalPlayer())
    for player in playerList:
        objKey = PtGetAvatarKeyFromClientID(player.getPlayerID())
        soavatar = objKey.getSceneObject()
        
        #faire flotter tout le monde
        soavatar.physics.enable(0)
        soavatar.netForce(1)
        
        #deplacer les gens
        mat = ptMatrix44()
        try:
            mat.setData(ws[str(n)])
        except:
            mat = PtGetLocalAvatar().getLocalToWorld()
        soavatar.physics.warp(mat)
        soavatar.netForce(1)
        
        #reactiver la physique pour tous
        if n != 8:
            soavatar.physics.enable(1)
            soavatar.netForce(1)

""" shroomie
    shroomie(act="visible")
    shroomie(act="cache")
    shroomie(act="plonge")
    shroomie(act="surface")
    shroomie(act="avance")
    shroomie(act="tourne")
    shroomie(act="gauche")
    shroomie(act="centre")
    shroomie(act="droite")
    shroomie(act="sortie")
    shroomie(act="entree")
    shroomie(act="sur moi")
"""
# shroomie(act="visible")
# shroomie(act="gauche")
# shroomie(act="surface")
# shroomie(act="avance")
# shroomie(act="tourne")
# shroomie(act="plonge")
# shroomie(act="sur moi")
def shroomie(act="sur moi"):
    Ride.Action(animal="shroomie", action=act)

""" ride
    ride(soName="oiseaut1", t=60.0)
    ride(soName="oiseaut2", t=60.0)
    ride(soName="shooter1", t=60.0)
    ride(soName="shooter2", t=60.0)
    ride(soName="shooter3", t=60.0)
    ride(soName="shooter4", t=60.0)
    ride(soName="shooter5", t=60.0)
    ride(soName="shroomie", t=60.0)
"""
#
def ride(soName="oiseaut1", t=60.0):
    #recuperer tous les joueurs
    playerList = PtGetPlayerList()
    playerList.append(PtGetLocalPlayer())
    for player in playerList:
        """
        objKey = PtGetAvatarKeyFromClientID(player.getPlayerID())
        soavatar = objKey.getSceneObject()
        
        #faire flotter tout le monde
        soavatar.physics.enable(0)
        soavatar.netForce(1)
        """
        #
        playerName = player.getPlayerName()
        Ride.Suivre(objet=soName, Avatar=playerName, duree=t)

#
def shroomifyAll(bOn=True):
    #recuperer tous les joueurs
    playerList = PtGetPlayerList()
    playerList.append(PtGetLocalPlayer())
    for player in playerList:
        #objKey = PtGetAvatarKeyFromClientID(player.getPlayerID())
        #soAv = objKey.getSceneObject()
        #pos = soAv.getLocalToWorld()
        #CloneObject.co3("SandscritRoot", "Payiferen", bShow=bOn, bLoad=bOn, scale=0.2, matPos=mat)
        #CloneObject.Clone2(objName, age, bShow=True, bLoad=True, matPos=None, bAttach=False, soAvatar=None)
        #shro2 = PtFindSceneobject('LakeShoomieHandle','Teledahn')
        #Clone2("LakeShoomieHandle", "Teledahn", bShow=bOn, bLoad=bOn, matPos=pos, bAttach=bOn, soAvatar=soAv)
        #ColumnUnderPlayer(bOn=True, player=None)
        ColumnUnderPlayer(bOn, player)


"""
    elif (objet.lower()) == 'oiseaut1' :
    # oiseau 1 de Teledahn    
        defobjet = ("Teledahn,tldnHarvest,BBHead,0,0,-90")
    elif (objet.lower()) == 'oiseaut2' :
    # oiseau 2 de Teledahn    
        defobjet = ("Teledahn,tldnHarvest,BBHead01,0,0,-90")
    elif (objet.lower()) == 'shooter1' :
    # Shooter 1 de Teledahn    
        defobjet = ("Teledahn,tldnHarvest,ShooterB-Master,0,0,0")
    elif (objet.lower()) == 'shooter2' :
    # Shooter 2 de Teledahn    
        defobjet = ("Teledahn,tldnHarvest,ShooterC-Master,0,0,90")
    elif (objet.lower()) == 'shooter3' :
    # Shooter 3 de Teledahn     
        defobjet = ("Teledahn,tldnHarvest,ShooterD-Master,0,0,0")
    elif (objet.lower()) == 'shooter4' :
    # Shooter 4 de Teledahn    
        defobjet = ("Teledahn,tldnHarvest,ShooterF-Master,0,0,0")
    elif (objet.lower()) == 'shooter5' :
    # Shooter 5 de Teledahn    
        defobjet = ("Teledahn,tldnHarvest,ShooterH-Master,0,0,0")
    elif (objet.lower()) == 'shroomie' :
    # Shroomie de Teledahn    
        defobjet = ("Teledahn,tldnHarvest,Sniff_SB_Spine01,0,0,0")
"""
"""
        shro1 = PtFindSceneobject('MasterShroomie','Teledahn')
        shro2 = PtFindSceneobject('LakeShoomieHandle','Teledahn')
        spwn1 = PtFindSceneobject('SpawnPtNear01','Teledahn').getLocalToWorld()
        spwn2 = PtFindSceneobject('SpawnPtNear02','Teledahn').getLocalToWorld()
        spwn3 = PtFindSceneobject('SpawnPtNear03','Teledahn').getLocalToWorld()
        spwn4 = PtFindSceneobject('SpawnPtNear04','Teledahn').getLocalToWorld()
        spwn5 = PtFindSceneobject('SpawnPtNear05','Teledahn').getLocalToWorld()
"""

#=====================================================================
# clonage

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
    #fXAngle = float(fXAngle) - 90.0
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

# Save the couples of (columnNumber, playerID)
nbCol = 5
dicCol = {}
for i in range(0, nbCol):
    dicCol.update({i: 0})
# ColumnUnderPlayer
def ColumnUnderPlayer(bOn=True, player=None):
    global nbCol
    global dicCol
    objName = "LakeShoomieHandle"
    age = "Teledahn"
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
        
    mTrans = ptMatrix44()
    mTrans.translate(ptVector3(0.0, 0.0, 0.0)) 
    
    ret = CloneColumns2(objName, age, bOn, True, nbCol, iCurCol, matAv, mTrans, 0, 0, 0, bOn, soAvatar)
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

