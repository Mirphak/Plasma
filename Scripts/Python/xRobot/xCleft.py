# -*- coding: utf-8 -*-
# == Commandes specifiques a Cleft ==

"""
    V1 - 27/12/2014
    V2 - 12/02/2016 : Ajouts pour le Cavern Tour 2015-2016
    V3 - 12/11/2016 : Ajouts pour le Cavern Tour 2016-2017
    V4 - 05/01/2020 : Ajouts pour le Cavern Tour 2020-2021
    V5 - 25/06/2022 : Ajouts pour le Cavern Tour 2022-2024
        La visite du Cleft n'a pas besoin de beaucoup d'effets. 
        Il s'agit surtout de se promener en parlant de l'histoire et des personnages. 
        Nous avons surtout besoin de la déformation habituelle des avatars pour empêcher les gens de monter sur les échelles. 
        Nous n'irons pas dans la grotte sous l'arbre, puisque cela fait partie de la visite de la grotte de Bahro.

        Lorsque nous parlerons de la Fente elle-même, nous voudrons faire descendre le groupe dans la salle de la bibliothèque. 
        Je montrerai une carte étiquetée des pièces pour expliquer à quoi chacune d'elles sert.

        Je parlerai du Zandoni comme d'habitude, donc nous devrons nous y rendre à ce moment-là. 
        Si nous trouvons un moyen de le faire fonctionner, ce sera quelque chose que nous n'avons jamais fait auparavant.

        Une autre chose que nous n'avons jamais faite auparavant est de chevaucher les faucons lorsqu'ils volent, 
        bien que je ne sois pas sûr que cela en vaille la peine puisqu'ils ne font que voler en petits cercles.

        Comme les âges de Myst V n'ont pas encore été convertis pour le Live, 
        la visite de la caldeira du volcan devra se faire en streaming uniquement, 
        donc aucun effet n'est nécessaire pour cela.

        Je ne sais pas combien de temps la conférence va prendre, mais je prévois qu'elle va probablement utiliser deux dates de visite. 
        Je n'ai pas eu de nouvelles de R'Tay concernant des ajouts qu'il souhaiterait faire. 
        Je lui ai envoyé une copie de mes notes pour qu'il les examine.
        
        !to cleft 1
        !lock
        !check noladder
        
        !sp 5
"""

from math import *

from Plasma import *
from PlasmaTypes import *
from PlasmaKITypes import *
from xPsnlVaultSDL import *

from . import Ride

age = "Cleft"

"""
### pages in python.Cleft.py ###
        pages = []

        # Add the age specific pages
        if loadTomahna:
            pages += ["Cleft","tmnaDesert","MaleShortIdle","FemaleShortIdle","YeeshaFinalEncounter","FemaleTurnRight180","MaleTurnRight180","clftSndLogTracks","clftAtrusGoggles"]
        else:
            pages += ["Desert","Cleft","FemaleCleftDropIn","MaleCleftDropIn","clftJCsDesert","clftJCsChasm"]
        if loadZandi:
            pages += ["clftZandiVis","ZandiCrossLegs","ZandiDirections","ZandiDirections01","ZandiDirections02","ZandiDirections03"]
            pages += ["ZandiIdle","ZandiRubNose","ZandiScratchHead","ZandiTurnPage","ZandiAllFace","ZandiOpen01Face"]
            pages += ["ZandiOpen02Face","ZandiRand01Face","ZandiRand02Face","ZandiRand03Face","ZandiRand04Face","ZandiRand05Face"]
            pages += ["ZandiRes01aFace","ZandiRes01bFace","ZandiRes02aFace","ZandiRes02bFace","ZandiRes03aFace","ZandiRes03bFace"]
            pages += ["ZandiJC01aFace","ZandiJC01bFace","ZandiJC02aFace","ZandiJC02bFace","ZandiJC03aFace","ZandiJC03bFace"]
            pages += ["ZandiJC04aFace","ZandiJC04bFace","ZandiJC05aFace","ZandiJC05bFace","ZandiJC06aFace","ZandiJC06bFace"]
            pages += ["ZandiJC07aFace","ZandiJC07bFace"]
        else:
            print "Zandi seems to have stepped away from the Airstream. Hmmm..."
        if loadBook:
            pages += ["clftYeeshaBookVis","FemaleGetPersonalBook","MaleGetPersonalBook"]
        else:
            print "Zandi seems to have stepped away from the Airstream. Hmmm..."

        # Put in all the common pages
        pages += ["BookRoom","clftAtrusNote"]
        pages += ["FemaleClimbOffTreeLadder","FemaleGetOnTreeLadder","FemaleWindmillLockedCCW","FemaleWindmillLockedCW","FemaleWindmillStart"]
        pages += ["MaleClimbOffTreeLadder","MaleGetOnTreeLadder","MaleWindmillLockedCCW","MaleWindmillLockedCW","MaleWindmillStart"]
        pages += ["YeeshaVisionBlocked","YeeshaFinalVision"]
"""

pages = ["Desert","Cleft","FemaleCleftDropIn","MaleCleftDropIn","clftJCsDesert","clftJCsChasm"]

bCleftAdded = False

def AddPrp():
    global bCleftAdded
    #pages = ["Desert","Cleft","FemaleCleftDropIn","MaleCleftDropIn","clftJCsDesert","clftJCsChasm"]
    for page in pages:
        PtConsoleNet("Nav.PageInNode %s" % (page) , 1)
    bCleftAdded = True

def DelPrp():
    global bCleftAdded
    #pages = ["Desert","Cleft","FemaleCleftDropIn","MaleCleftDropIn","clftJCsDesert","clftJCsChasm"]
    for page in pages:
        PtConsoleNet("Nav.PageOutNode %s" % (page) , 1)
    bCleftAdded = False

def DelPrpLocal():
    global bCleftAdded
    if bCleftAdded:
        #pages = ["Desert","Cleft","FemaleCleftDropIn","MaleCleftDropIn","clftJCsDesert","clftJCsChasm"]
        for page in pages:
            PtPageOutNode(page)
        bCleftAdded = False

def ToggleObjects(name, bOn = True):
    pf = PtFindSceneobjects(name)
    for so in pf:
        so.netForce(1)
        so.draw.enable(bOn)

def ToggleFences(bOn = True):
    so = PtFindSceneobject("ProxyPropertyLine", age)
    so.netForce(1)
    so.physics.enable(bOn)
    ToggleObjects("PropertyFence", bOn)

def EnableAll(bOn = True):
    ToggleObjects("Grass", bOn)
    ToggleObjects("Shrub", bOn)
    ToggleObjects("scrubBillboard", bOn)
    ToggleObjects("PostBarbed", bOn)
    ToggleObjects("DangerSign", bOn)
    ToggleObjects("Sign", bOn)
    ToggleObjects("Plate", bOn)
    ToggleObjects("keepout", bOn)
    ToggleObjects("Desert", bOn)
    ToggleObjects("Mountain", bOn)
    ToggleObjects("skyDome", bOn)
    ToggleFences(bOn)

#
class AlarmAddPrp:
    def onAlarm(self, context):
        AddPrp()
#
class AlarmEnableAll:
    def onAlarm(self, context = 0):
        EnableAll(context)
#
def AddCleft(self, args = []):
    PtSendKIMessage(kKILocalChatStatusMsg, "Adding Cleft...")
    try:
        PtSetAlarm (1, AlarmAddPrp(), 0)
        PtSetAlarm(5, AlarmEnableAll(), 0)
        PtSendKIMessage(kKILocalChatStatusMsg, "Cleft added!")
        return 1
    except:
        PtSendKIMessage(kKILocalChatErrorMsg, "Error while adding Cleft.")
        return 0

# ============================================================================
"""
# dans xLinkingBookGUIPopup.py
# 1
                vault = ptVault()
                entry = vault.findChronicleEntry("TomahnaLoad")
                if type(entry) != type(None):
                    entry.setValue("yes")
                    entry.save()
                    PtDebugPrint("Chronicle entry TomahnaLoad already added, setting to yes")
                else:
                    sdl = xPsnlVaultSDL()
                    sdl["CleftVisited"] = (1,)
                    vault.addChronicleEntry("TomahnaLoad",1,"yes")
                    PtDebugPrint("Chronicle entry TomahnaLoad not present, adding entry and setting to yes")
                respLinkResponder.run(self.key,avatar=PtGetLocalAvatar())
# 2
                                        vault = ptVault()
                                        entry = vault.findChronicleEntry("TomahnaLoad")
                                        if type(entry) != type(None):
                                            if linkTitle == "Tomahna":
                                                entry.setValue("yes")
                                            else:
                                                entry.setValue("no")
"""
# Toggle Cleft or Tomahna
def tct():
    # recherche de l'entree de chronique "TomahnaLoad" dans ma voute
    vault = ptVault()
    entry = vault.findChronicleEntry("TomahnaLoad")
    # si elle n'existe pas, la creer. ce doit etre un ptVaultNode of type kNodeTypeChronicle
    # et on la met a "yes"
    if entry is None:
        sdl = xPsnlVaultSDL()
        sdl["CleftVisited"] = (1,)
        vault.addChronicleEntry("TomahnaLoad",1,"yes")
        PtDebugPrint("Chronicle entry TomahnaLoad not present, adding entry and setting to yes")
    else:
        entryTomahnaValue = entry.getValue()
        if entryTomahnaValue == "yes":
            entry.setValue("no")
            entry.save()
            PtDebugPrint("Chronicle entry TomahnaLoad already added, setting to no")
        else:
            entry.setValue("yes")
            entry.save()
            PtDebugPrint("Chronicle entry TomahnaLoad already added, setting to yes")

#
def tmna():
    global bCleftAdded
    pages = ["clftSndLogTracks"]
    for page in pages:
        PtConsoleNet("Nav.PageInNode %s" % (page) , 1)
    #pages = ["Desert"]
    #for page in pages:
    #    PtConsoleNet("Nav.PageOutNode %s" % (page) , 1)
    bCleftAdded = True

# =========================================================================


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
    soAvatarList = [PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject() for player in playerList]
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
def page(what="zandoni", bIn=True):
    #global bCleftAdded
    #pages = ["clftSndLogTracks"]
    pages = []
    if what == "zandoni":
        pages += ["clftSndLogTracks"]
    if what == "bahro":
        pages += ["clftSceneBahro"]
    elif what == "tomahna":
        #pages += ["Cleft","tmnaDesert","MaleShortIdle","FemaleShortIdle","YeeshaFinalEncounter","FemaleTurnRight180","MaleTurnRight180","clftSndLogTracks","clftAtrusGoggles"]
        pages += ["tmnaDesert","MaleShortIdle","FemaleShortIdle","YeeshaFinalEncounter","FemaleTurnRight180","MaleTurnRight180","clftSndLogTracks","clftAtrusGoggles"]
    elif what == "cleft":
        #pages += ["Desert","Cleft","FemaleCleftDropIn","MaleCleftDropIn","clftJCsDesert","clftJCsChasm"]
        pages += ["Desert","FemaleCleftDropIn","MaleCleftDropIn","clftJCsDesert","clftJCsChasm"]
    elif what == "zandi":
        pages += ["clftZandiVis","ZandiCrossLegs","ZandiDirections","ZandiDirections01","ZandiDirections02","ZandiDirections03"]
        pages += ["ZandiIdle","ZandiRubNose","ZandiScratchHead","ZandiTurnPage","ZandiAllFace","ZandiOpen01Face"]
        pages += ["ZandiOpen02Face","ZandiRand01Face","ZandiRand02Face","ZandiRand03Face","ZandiRand04Face","ZandiRand05Face"]
        pages += ["ZandiRes01aFace","ZandiRes01bFace","ZandiRes02aFace","ZandiRes02bFace","ZandiRes03aFace","ZandiRes03bFace"]
        pages += ["ZandiJC01aFace","ZandiJC01bFace","ZandiJC02aFace","ZandiJC02bFace","ZandiJC03aFace","ZandiJC03bFace"]
        pages += ["ZandiJC04aFace","ZandiJC04bFace","ZandiJC05aFace","ZandiJC05bFace","ZandiJC06aFace","ZandiJC06bFace"]
        pages += ["ZandiJC07aFace","ZandiJC07bFace"]
    elif what == "book":
        pages += ["clftYeeshaBookVis","FemaleGetPersonalBook","MaleGetPersonalBook"]
    else:
        return 0

    if bIn:
        for page in pages:
            PtConsoleNet("Nav.PageInNode %s" % (page) , 1)
    else:
        for page in pages:
            PtConsoleNet("Nav.PageOutNode %s" % (page) , 1)
    #bCleftAdded = True

#
"""
def ToggleFences(bOn = True):
    so = PtFindSceneobject("ProxyPropertyLine", age)
    so.netForce(1)
    so.physics.enable(bOn)
    pf = PtFindScenobjects("PropertyFence")
    for so in pf:
        so.netForce(1)
        so.draw.enable(bOn)

#Grass
#Shrub
#scrubBillboard
#PostBarbed
#DangerSign
#Sign
#Plate
#keepout

#Desert
#Mountain
#skyDome
#
"""


# Find scene objects with name like soName in all loaded districts (aka pages or prp files)
# ex.: soName = "Bahro*Stone" will be transformed in regexp "^.*Bahro.*Stone.*$"
def FindSOName(soName):
    import re
    cond = "^.*" + soName.replace("*", ".*") + ".*$"
    try:
        pattern = re.compile(cond, re.IGNORECASE)
    except:
        return list()
    strList = soName.split("*")
    nameList = list()
    for str in strList:
        nameList.extend([so.getName() for so in PtFindSceneobjects(str)])
    nameList = list(set(nameList))
    nameList = [x for x in nameList if pattern.match(x) != None]
    return nameList

# Find scene objects with name like soName in all loaded districts (Warning, it includes GUI)
def FindSOLike(soName):
    nameList = FindSOName(soName)
    soList = list()
    for soName in nameList:
        sol = PtFindSceneobjects(soName)
        soList.extend(sol)
    return soList

# Remove the panic regions, I assume that all the panic links contain "Panic" or "panic" in there names.
def DisablePanicLinks():
    #sol = FindSOLike("Panic")
    #sol = sol.append(FindSOLike("panic"))
    sol = FindSOLike("anic")
    for so in sol:
        so.netForce(1)
        so.physics.disable()

# Remove the Fences Proxy Blockers.
def DisableFences():
    sol = []
    sol = sol.append(FindSOLike("Blocker"))
    sol = sol.append(FindSOLike("Proxy"))
    for so in sol:
        so.netForce(1)
        so.physics.disable()

# Remove some objects.
def Remove():
    sol = FindSOLike("sky")
    sol = sol.append(FindSOLike("Mount"))
    sol = sol.append(FindSOLike("Rain"))
    for so in sol:
        so.netForce(1)
        so.physics.disable()

# Remove the Zandi Mobile Region.
def DisableZMB():
    sol = []
    sol = sol.append(FindSOLike("ZandiMobileRegion"))
    for so in sol:
        so.netForce(1)
        so.physics.disable()

#Cette fonction ne s'utilise pas seule
def RunResp(key, resp, stateidx = None, netForce = 1, netPropagate = 1, fastforward = 0):
    nt = ptNotify(key)
    nt.addReceiver(resp)
    nt.netPropagate(netPropagate)
    nt.netForce(netForce)
    if stateidx != None:
        nt.addResponderState(stateidx)
    if fastforward:
        nt.setType(PtNotificationType.kResponderFF)
        nt.netPropagate(0)
        nt.netForce(0)
    nt.setActivate(1.0)
    nt.send()

# Run Zandoni (don't know what actions are available...)
def Zandoni(action = 0):
    objName = "ZandiMobileRegion"
    ageName = "Cleft"
    so = PtFindSceneobject(objName, ageName)
    responders = so.getResponders()
    RunResp(key = so.getKey(), resp = responders[0], stateidx = action, netForce = 1, netPropagate = 1, fastforward = 0)

# Attach so1 to so2
def Attach(so1, so2, bOn=True):
    so1.netForce(1)
    so2.netForce(1)
    so1.physics.enable(bOn)
    if (bOn):
        PtAttachObject(so1, so2)
        so1.physics.enable()
        so1.physics.netForce(1)
    else:
        PtDetachObject(so1, so2)
        so1.physics.disable()
        so1.physics.netForce(1)
    so1.netForce(1)
    so2.netForce(1)

# Zandoni "ride"
def RideZ(bOn=True):
    #objName = "ZandiMobileRegion"
    ageName = "Cleft"
    #objName = "ZandiMobile-Root"
    objName = "ZandiTrailerPlayerWarp"
    objNames = ["ZandiMobile-Root", "ZMWheel01", "ZMWheel02", "ZMWheel03", "ZMWheel04"]
    so = PtFindSceneobject(objName, ageName)
    for oName in objNames:
        Attach(PtFindSceneobject(oName, ageName), so, bOn)
    me = PtGetLocalAvatar()
    #attacher la zandoni a moi
    Attach(so, me, bOn)
    me.physics.netForce(1)
    me.physics.enable()
    so.physics.netForce(1)
    so.physics.disable()
    ##recuperer tous les joueurs
    #playerList = PtGetPlayerList()
    #soAvatarList = [PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject() for player in playerList]
    #for soavatar in soAvatarList:
    #    #cacher tout le monde
    #    #soavatar.draw.enable(0)
    #    #soavatar.netForce(1)
    #    #faire flotter tout le monde
    #    #soavatar.physics.disable()
    #    #soavatar.netForce(1)
    #    Attach(soavatar, me, bOn)
    #    soavatar.netForce(1)
    #    soavatar.draw.enable(1)

    """
    #et les roues? ... no physics for them!
    # => need to see the wheels animations
    objName = "ZMWheel01"
    so = PtFindSceneobject(objName, ageName)
    Attach(so, me, bOn)
    objName = "ZMWheel02"
    so = PtFindSceneobject(objName, ageName)
    Attach(so, me, bOn)
    objName = "ZMWheel03"
    so = PtFindSceneobject(objName, ageName)
    Attach(so, me, bOn)
    objName = "ZMWheel04"
    so = PtFindSceneobject(objName, ageName)
    Attach(so, me, bOn)
    """

#
def ToggleBoolSDL(name="clftSceneBahroUnseen"):
    sdl=PtGetAgeSDL()
    sdl[name]=(not sdl[name][0],)


#========================================================
dicBot = {}
#
def CercleV(coef=2.0, avCentre=None):
    if avCentre is None:
        avCentre = PtGetLocalAvatar()
    #agePlayers = GetAllAgePlayers()
    # ne pas tenir compte des robots
    agePlayers = [pl for pl in PtGetPlayerList() if not(pl.getPlayerID() in list(dicBot.keys()))]
    i = 0
    n = len(agePlayers)
    print("nb de joueurs: %s" % (n))
    dist = float(coef * n) / (2.0 * math.pi)
    print("distance: %s" % (dist))
    for i in range(n):
        player = agePlayers[i]
        avatar = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
        angle = (float(i) * 2.0 * math.pi) / float(n)
        print("angle(%s): %s" % (i, angle))
        dx = float(dist)*math.cos(angle)
        #dy = float(dist)*math.sin(angle)
        dy = 0
        dz = float(dist)*math.sin(angle)
        matrix = avCentre.getLocalToWorld()
        matrix.translate(ptVector3(dx, dy, dz))
        avatar.netForce(1)
        avatar.physics.warp(matrix)

#
class CircleAlarm:
    def onAlarm(self, en):
        CercleV(coef=2.0, avCentre=None)


# In Cleft we can ride:
# "oiseauc1", "oiseauc2" or "bahroc1", "bahroc2", "bahroc3", "bahroc4", "bahroc5"
def ride(soName="oiseauc1", t=30.0):
    #recuperer tous les joueurs
    playerList = PtGetPlayerList()
    #playerList.append(PtGetLocalPlayer())
    for player in playerList:
        playerName = player.getPlayerName()
        Ride.Suivre(objet=soName, Avatar=playerName, duree=t)
    #CercleV(coef=2.0, avCentre=None)
    PtSetAlarm(2, CircleAlarm(), 0)
