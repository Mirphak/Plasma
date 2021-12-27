"""
    Version 1 : 26/03/2016
        ** Cavern Tour du 26/03/2016 **
            - JALAK   :
                + onlake pour pouvoir se deplacer au niveau du sol.
                + plateforme au-dessus d'une des structures qui entourent l'arene.
            - MINKATA : 
                + jour/nuit
            - DESCENT :
                + plateforme aux 2 niveaux du bas.
                + je veux essayer de faire un ascenseur
                
    Version 2 : 08/04/2014
        ** Cavern Tour du 08/04/2014 **
            - MINKATA : 
                + jour/nuit (appuyer sur une pierre)
                + deplacer tout le monde dans les kivas (K1 a K5)
            - DESCENT :
                + plateforme aux 2 niveaux du bas.
                + je veux essayer de faire un ascensseur
                =>  import xRobot.xJMD as d
                    !toggle Cam  0 0
                    !nopanic
                    d.platform(4, False)
                    d.block(4)
                    !ws 2
                    //float .4
                    F10
                    faire qq pas a droite
                    !warpall
                    d.block(5)
                    d.platform(4, True)
                    F10
                    d.block(6)
"""

from Plasma import *
import Platform
import math
import Columns2

#
def LinkPlayerTo(age, playerID=None, spawnPointNumber=None):
    if not playerID or playerID == "":
        playerID = PtGetLocalPlayer().getPlayerID()
    else:
        try:
            playerID = long(playerID)
        except:
            return "incorrect playerID"
            #pass
    if len(age) < 3:
        #pass
        return "incorrect age"
    ageInstanceName = age[0]
    ageFileName = age[1]
    ageGuid = age[2]
    ageUserDefinedName = ""
    if len(age) > 3:
        ageUserDefinedName = age[3]
    
    ageLink = ptAgeLinkStruct()
    ageInfo = ptAgeInfoStruct()
    ageInfo.setAgeFilename(ageFileName)
    ageInfo.setAgeInstanceGuid(ageGuid)
    ageInfo.setAgeInstanceName(ageInstanceName)
    
    ageLink.setAgeInfo(ageInfo)
    """
    spawnPt = "LinkInPointDefault"
    if spawnPointNumber:
        spawnPt = GetSpawnPoint(spawnPointNumber)
    else:
        ageSpawPoint = ""
        if len(age) > 4:
            ageSpawPoint = age[4]
        if ageSpawPoint != "":
            spawnPt = ageSpawPoint
    #self.chatMgr.AddChatLine(None, "sp=\""+spawnPt+"\"", 3)
    spawnPoint = ptSpawnPointInfo()
    spawnPoint.setName(spawnPt)
    ageLink.setSpawnPoint(spawnPoint)
    """
    ptNetLinkingMgr().linkPlayerToAge(ageLink, playerID)
    return ageUserDefinedName + " " + ageInstanceName

# minkata, jalak, tiwah
def LinkAll(ageName="dereno"):
    ages = {
        "hi":["Hood of Illusions", "Neighborhood", "3cc44d4b-31e1-4dec-b6e6-4b63c72becc3", "The", ""],
        "minkata":["Minkata", "Minkata", "125c7c98-9c18-49df-acce-ddc3f8108bd6", "Mir-o-Bot's", ""], 
        "jalak":["Jalak", "Jalak", "1269ee23-baff-4ca2-a3bc-f80df29fe978", "Mir-o-Bot's", ""], 
        "tiwah":["Descent", "Descent", "4543f4e3-aa4b-4c4b-b6f4-eaa1aee4c440", "Mir-o-Bot's", ""],
    }
    
    ageName = ageName.lower()
    if (ageName in ages.keys()):
        age = ages[ageName]
    else:
        return
    
    #les autre joueurs dans mon age
    for player in PtGetPlayerList():
        LinkPlayerTo(age, playerID = player.getPlayerID(), spawnPointNumber = None)
    # link myself
    #LinkPlayerTo(age, playerID = None, spawnPointNumber = None)

#
def wa(where=None):
    #avCentre = PtGetLocalAvatar()
    #mat = avCentre.getLocalToWorld()
    mat = None
    if where is None: #or where not in range(1, 5):
        mat = PtGetLocalAvatar().getLocalToWorld()
    else:
        """
        if where == 1:
            tupPos = ((0.98276501894, 0.184859260917, 0.0, 23.3415126801), (-0.184859260917, 0.98276501894, 0.0, 54.0308570862), (0.0, 0.0, 1.0, -0.0328424945474), (0.0, 0.0, 0.0, 1.0))
        elif where == 2:
            tupPos = ((-0.897078573704, -0.44187015295, 0.0, 649.721862793), (0.44187015295, -0.897078573704, 0.0, -877.984619141), (0.0, 0.0, 1.0, 9445.71386719), (0.0, 0.0, 0.0, 1.0))
        elif where == 3:
            tupPos = ((0.00954949762672, -0.999954581261, 0.0, -102.545890808), (0.999954581261, 0.00954949762672, 0.0, 54.9582672119), (0.0, 0.0, 1.0, 10563.0976562), (0.0, 0.0, 0.0, 1.0))
        elif where == 4:
            tupPos = ((-0.748968303204, 0.662607133389, 0.0, 1560.00488281), (-0.662607133389, -0.748968303204, 0.0, -51.4498291016), (0.0, 0.0, 1.0, 10171.9091797), (0.0, 0.0, 0.0, 1.0))
        elif where == 5:
            tupPos = ((-0.937420606613, -0.3482016325, 0.0, 993.751708984), (0.3482016325, -0.937420606613, 0.0, -455.378509521), (0.0, 0.0, 1.0, 9424.86523438), (0.0, 0.0, 0.0, 1.0))
        mat = ptMatrix44()
        mat.setData(tupPos)
        """
        objName = "ZandiMobileRegion"
        ageName = "Cleft"
        so = PtFindSceneobject(objName, ageName)
        mat = so.getLocalToWorld()

        #return 0
    
    #recuperer tous les joueurs
    playerList = PtGetPlayerList()
    playerList.append(PtGetLocalPlayer())
    soAvatarList = map(lambda player: PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject(), playerList)
    for soavatar in soAvatarList:
        #faire flotter tout le monde
        soavatar.netForce(1)
        soavatar.physics.disable()
        soavatar.physics.enable(0)
        soavatar.netForce(1)
    for soavatar in soAvatarList:
        #deplacer les gens
        soavatar.physics.warp(mat)
        soavatar.netForce(1)
    for soavatar in soAvatarList:
        #reactiver la physique pour tous
        soavatar.physics.enable(1)
        soavatar.netForce(1)

#

#========================================================
dicBot = {}

#
def Cercle(coef=5.0, h=10.0, avCentre=None):
    if avCentre is None:
        avCentre = PtGetLocalAvatar()
    #agePlayers = GetAllAgePlayers()
    # ne pas tenir compte des robots
    agePlayers = filter(lambda pl: not(pl.getPlayerID() in dicBot.keys()), PtGetPlayerList())
    i = 0
    n = len(agePlayers)
    print "nb de joueurs: %s" % (n)
    dist = float(coef * n) / (2.0 * math.pi)
    print "distance: %s" % (dist)
    for i in range(n):
        player = agePlayers[i]
        avatar = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
        angle = (float(i) * 2.0 * math.pi) / float(n)
        print "angle(%s): %s" % (i, angle)
        dx = float(dist)*math.cos(angle)
        dy = float(dist)*math.sin(angle)
        matrix = avCentre.getLocalToWorld()
        matrix.translate(ptVector3(dx, dy, float(h)))
        avatar.netForce(1)
        avatar.physics.warp(matrix)

#========================================================
# long platform(where=1)
# DESCENT V2 :
#    => en haut devant la porte = platform(4)
#    => arret intermediaire     = platform(5)
#    => arret tout en bas       = platform(6)
def platform(where=None, bAttachOn=False):
    matPos = None
    #if where is None or where not in range(1, 5):
    if where is None or where not in range(1, 6):
        matPos = PtGetLocalAvatar().getLocalToWorld()
    else:
        """
        #Ahnonay
        if where == 1:
            tupPos = ((0.98276501894, 0.184859260917, 0.0, 23.3415126801), (-0.184859260917, 0.98276501894, 0.0, 54.0308570862), (0.0, 0.0, 1.0, -0.0328424945474), (0.0, 0.0, 0.0, 1.0))
        elif where == 2:
            tupPos = ((-0.897078573704, -0.44187015295, 0.0, 649.721862793), (0.44187015295, -0.897078573704, 0.0, -877.984619141), (0.0, 0.0, 1.0, 9445.71386719), (0.0, 0.0, 0.0, 1.0))
        elif where == 3:
            tupPos = ((0.00954949762672, -0.999954581261, 0.0, -102.545890808), (0.999954581261, 0.00954949762672, 0.0, 54.9582672119), (0.0, 0.0, 1.0, 10563.0976562), (0.0, 0.0, 0.0, 1.0))
        elif where == 4:
            tupPos = ((-0.748968303204, 0.662607133389, 0.0, 1560.00488281), (-0.662607133389, -0.748968303204, 0.0, -51.4498291016), (0.0, 0.0, 1.0, 10171.9091797), (0.0, 0.0, 0.0, 1.0))
        elif where == 5:
            tupPos = ((-0.937420606613, -0.3482016325, 0.0, 993.751708984), (0.3482016325, -0.937420606613, 0.0, -455.378509521), (0.0, 0.0, 1.0, 9424.86523438), (0.0, 0.0, 0.0, 1.0))
        """
        """
        # Descent V1
        if where == 1:
            tupPos = ((-0.0784590244293, 0.996917307377, 0.0, 789.132202148), (-0.996917307377, -0.0784590244293, 0.0, -583.487670898), (0.0, 0.0, 1.0, 1151.59057617), (0.0, 0.0, 0.0, 1.0))
        elif where == 2:
            tupPos = ((0.859911203384, 0.510443627834, 0.0, 785.749572754), (-0.510443627834, 0.859911203384, 0.0, -574.134643555), (0.0, 0.0, 1.0, 1151.59057617), (0.0, 0.0, 0.0, 1.0))
        elif where == 3:
            tupPos = ((-0.398735255003, 0.91706776619, 0.0, 766.0), (-0.91706776619, -0.398735255003, 0.0, -699.0), (0.0, 0.0, 1.0, 715.0), (0.0, 0.0, 0.0, 1.0))
        elif where == 4:
        """
        # Descent V2
        if where == 1:
            tupPos = ((0.722353339195, -0.691524147987, 0.0, 766.198181152), (0.691524147987, 0.722353339195, 0.0, -698.65826416), (0.0, 0.0, 1.0, 608.855895996), (0.0, 0.0, 0.0, 1.0))
        elif where == 2:
            tupPos = ((1.0, -0.0, 0.0, 769.0), (0.0, 1.0, 0.0, -610.0), (0.0, 0.0, 1.0, 1152.0), (0.0, 0.0, 0.0, 1.0))
        elif where == 3:
            tupPos = ((0.0, -1.0, 0.0, 766.0), (1.0, 0.0, 0.0, -699.0), (0.0, 0.0, 1.0, 1146.0), (0.0, 0.0, 0.0, 1.0))
        elif where == 4:
            tupPos = ((0.0, -1.0, 0.0, 766.0), (1.0, 0.0, 0.0, -680.0), (0.0, 0.0, 1.0, 1140.0), (0.0, 0.0, 0.0, 1.0))
        elif where == 5:
            tupPos = ((0.0, -1.0, 0.0, 766.0), (1.0, 0.0, 0.0, -680.0), (0.0, 0.0, 1.0, 715.0), (0.0, 0.0, 0.0, 1.0))
        elif where == 6:
            tupPos = ((0.0, -1.0, 0.0, 766.0), (1.0, 0.0, 0.0, -680.0), (0.0, 0.0, 1.0, 610.0), (0.0, 0.0, 0.0, 1.0))

        matPos = ptMatrix44()
        matPos.setData(tupPos)
        
    Platform.CreatePlatform2(bShow=False, matAv=matPos, bAttach=bAttachOn)

#
def attach(bOn=True):
    Platform.AttachColumnsToMe(bOn)

# positionner une colonne pour bloquer la plateforme attachee a moi
# CloneColumns2(objName, age, bLoadOn=True, bShowOn=True, iNbCol=10, iCurCol=0, matAv=None, mTrans=None, fXAngle=0, fYAngle=0, fZAngle=0, bAttachOn=True, soAv=None, bFirst=True)
# Columns2.CloneOneColumn(objName, age, bOn=True, matAv=None, mTrans=None, fXAngle=0, fYAngle=0, fZAngle=0)
def block(where=4, h=0.0):
    """
    nbCol = 25
    age = "Jalak"
    objNameBase = "columnPhys_"
    iCurCol = 1
    objName = objNameBase + str(iCurCol).zfill(2)
    bOn=True
    bShow=True
    player=None
    fXAngle=0.0
    fYAngle=0.0
    fZAngle=0.0
    bAttach=False
    soAvatar=None
    bFirstCol=False
    h=0.0
    Columns2.CloneColumns2(objName, age, bOn, bShow, nbCol, iCurCol, matAv, mTrans, fXAngle, fYAngle, fZAngle, bAttach, soAvatar, bFirstCol)
    """
    objNameBase = "columnPhys_"
    iCurCol = 1
    objName = objNameBase + str(iCurCol).zfill(2)
    age = "Jalak"
    bOn=True
    bShow=True
    nbCol = 25
    player=None
    mTrans = ptMatrix44()
    mTrans.translate(ptVector3(0.0, -3.25, 30.0))
    #mTrans.translate(ptVector3(0.0, -9.75, 30.0))
    mTrans.translate(ptVector3(0.0, -3.25, -27.0 + h))
    fXAngle=0.0
    fYAngle=0.0
    fZAngle=0.0
    
    if where == 1:
        tupPos = ((0.722353339195, -0.691524147987, 0.0, 766.198181152), (0.691524147987, 0.722353339195, 0.0, -698.65826416), (0.0, 0.0, 1.0, 608.855895996), (0.0, 0.0, 0.0, 1.0))
    elif where == 2:
        tupPos = ((1.0, -0.0, 0.0, 769.0), (0.0, 1.0, 0.0, -610.0), (0.0, 0.0, 1.0, 1152.0), (0.0, 0.0, 0.0, 1.0))
    elif where == 3:
        tupPos = ((0.0, -1.0, 0.0, 766.0), (1.0, 0.0, 0.0, -699.0), (0.0, 0.0, 1.0, 1146.0), (0.0, 0.0, 0.0, 1.0))
    elif where == 4:
        tupPos = ((0.0, -1.0, 0.0, 766.0), (1.0, 0.0, 0.0, -680.0), (0.0, 0.0, 1.0, 1140.0), (0.0, 0.0, 0.0, 1.0))
    elif where == 5:
        tupPos = ((0.0, -1.0, 0.0, 766.0), (1.0, 0.0, 0.0, -680.0), (0.0, 0.0, 1.0, 715.0), (0.0, 0.0, 0.0, 1.0))
    elif where == 6:
        tupPos = ((0.0, -1.0, 0.0, 766.0), (1.0, 0.0, 0.0, -680.0), (0.0, 0.0, 1.0, 610.0), (0.0, 0.0, 0.0, 1.0))
    matPos = ptMatrix44()
    matPos.setData(tupPos)
    matAv = matPos * mTrans
    bAttach=False
    soAvatar=None
    bFirstCol=False
    
    #Columns2.CloneOneColumn(objName, age, bOn, matAv, mTrans, fXAngle, fYAngle, fZAngle)
    Columns2.CloneColumns2(objName, age, bOn, bShow, nbCol, iCurCol, matAv, mTrans, fXAngle, fYAngle, fZAngle, bAttach, soAvatar, bFirstCol)

#
