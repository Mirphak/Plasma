# -*- coding: utf-8 -*-

from Plasma import *
from PlasmaGame import *
from PlasmaGameConstants import *
from PlasmaKITypes import *
from PlasmaVaultConstants import *

import math
import datetime

import xBotKiCmds
import xBotAge
import xAnim
import xSave


#Ages de Mirphak (d'autres viendront peut-etre)
import ages

#import note

#----------------------------------------------------------------------------#
#   Attributs globaux
#----------------------------------------------------------------------------#
debugInfo = ""

# liste des instances disponibles pour moi
#linkDic = {
#'fh':('The Fun House', 'Neighborhood', '90938281-2c92-4e16-b959-85fce306f00c'),
#'fhci':('The Fun House - City', 'city', 'abee8828-869d-4756-89d3-5b374b518595'),
#'fhed':('Fun House\'s (1) Eder Delin', 'EderDelin', 'b0512722-ef62-4fc2-a414-7c7d883a0456'),
#'fhga':('Fun House\'s Gahreesen', 'Garrison', '268fc252-6b65-4e06-bb55-ae87869ebd25'),
#'fhte':('Fun House\'s Teledahn', 'Teledahn', '66174cf2-ecf0-4001-969e-ec72092937b0'),
#'gz':('Great Zero', 'GreatZero', '1e309bb5-3548-49f5-afdb-91fe38eb3438'),
#'ki':('Kirel', 'Neighborhood02', '4cfbe95a-1bb2-4cbc-a6c4-87eb28a2aac1'),
#'ki2':('V@Michel\'s D\'ni Kirel', 'Neighborhood02', 'c85db77e-3908-4f37-b115-e62fc0ce6968'),
#'tvh':('TVoltigeur\'s Hood', 'Neighborhood', 'bd519469-f289-4c64-b77d-45c079e18d6c'),
#'wp':('Not Exactly The Watcher\'s Pub', 'GreatTreePub', '71f6ceab-a883-4fe7-9b9a-1fe12e79c731'),
#'mbe':('MagicBot Ercana', 'Ercana', 'eccb9705-60b5-4746-b77c-02a3cf73f6a8'),
#'fhcl':('Fun House\'s Cleft', 'Cleft', 'da475fa8-b810-4310-9193-9bbd73ca3c64'),
#'mcl':('Magic Cleft', 'Cleft', '53c424e2-5922-44e8-be1f-1215ec8d9820'),
#'fhka':('The Fun House - Kadish Tolesa', 'Kadish', '8d17ee0f-a127-4267-90fe-587f5998d520')
#}
linkDic = xBotKiCmds.linkDic

# Authorized age instances
allowedAgeInstanceGuids = {
'The Fun House':'90938281-2c92-4e16-b959-85fce306f00c',
'The Fun House - City':'abee8828-869d-4756-89d3-5b374b518595',
'Fun House\'s (1) Eder Delin':'b0512722-ef62-4fc2-a414-7c7d883a0456',
'The Fun House - Gahreesen':'268fc252-6b65-4e06-bb55-ae87869ebd25',
'The Fun House - Teledahn':'66174cf2-ecf0-4001-969e-ec72092937b0',
'Fun House\'s Cleft':'da475fa8-b810-4310-9193-9bbd73ca3c64',
'The Fun House - Kadish Tolesa':'8d17ee0f-a127-4267-90fe-587f5998d520',
'The Fun House - Eder Gira':'2f21a44c-5a05-45f7-9587-4ca519f55f71',
'The Fun House - Eder Kemo':'b75e5acb-75c1-40e4-bee1-47b0a67d7340',

'MagicBot Ercana':'eccb9705-60b5-4746-b77c-02a3cf73f6a8',
'Magic Cleft':'53c424e2-5922-44e8-be1f-1215ec8d9820',
'Magic Relto':'798cc281-e224-4c60-aba4-5cc43027d069',
'Magic Teledahn':'edb74f4d-e0c5-4867-b8a6-f7f823bbd449',
'Magic Sharper Office':'798cc281-e224-4c60-aba4-5cc43027d069',
'Magic Kveer':'e5738673-08ee-4e8f-8567-4acb982edfff',
'Magic Tolesa':'a99728d2-9d2f-481f-bb9f-02b36709cbcd',
'Magic City':'411e452b-7077-4328-ad5b-4dadc1467a9a',

"Stone5's Cleft":'13fb8323-350c-4f98-90be-50c870450fa6',
#"GoLeaners hood":"e15f2919-9d76-4af4-8ba7-f63f674451e2",

}
#"GoLeaners hood":"e15f2919-9d76-4af4-8ba7-f63f674451e2", "GoLeaners",


def GetMirphakGuids():
    guids = dict()
    for age in ages.MirphakAgeDict:
        key = ages.MirphakAgeDict[age][0]
        value = ages.MirphakAgeDict[age][2]
        guids.update({key:value})
    return guids

MirphakAgeGuids = GetMirphakGuids()

def GetMirobotGuids():
    guids = dict()
    for age in ages.MirobotAgeDict:
        key = ages.MirobotAgeDict[age][0]
        value = ages.MirobotAgeDict[age][2]
        guids.update({key:value})
    return guids

MirobotAgeGuids = GetMirobotGuids()

def GetMagicbotGuids():
    guids = dict()
    for age in ages.MagicbotAgeDict:
        key = ages.MagicbotAgeDict[age][0]
        value = ages.MagicbotAgeDict[age][2]
        guids.update({key:value})
    return guids

MagicbotAgeGuids = GetMagicbotGuids()

        
lastLinkTime = datetime.datetime.now()

#----------------------------------------------------------------------------#
#   Methodes
#----------------------------------------------------------------------------#

def isPlayerInAge(player):
    #self.chatMgr.AddChatLine(None, "> isPlayerInAge", 3)
    agePlayers = PtGetPlayerList()
    ids = map(lambda player: player.getPlayerID(), agePlayers)
    try:
        if player.getPlayerID() in ids:
            return True
        else:
            return False
    except:
        return False

def SearchAvatarNameLike(name):
    #self.chatMgr.AddChatLine(None, "> SearchAvatarNameLike", 3)
    import re
    cond = r"[^a-z1-9*]"
    pat = re.sub(cond, ".", name.lower())
    pat = "^" + pat.replace("*", ".*") + ".*$"
    pattern = re.compile(pat)
    agePlayers = PtGetPlayerList()
    players = filter(lambda player: pattern.match(player.getPlayerName().lower()), agePlayers)
    return players


def GetAgePlayerByName(name):
    #self.chatMgr.AddChatLine(None, "> GetAgePlayerByName", 3)
    players = SearchAvatarNameLike(name)
    if len(players) > 0:
        return players[0]
    else:
        return None


def LinkToPublicAge(self, cFlags, args = []):
    self.chatMgr.AddChatLine(None, "> LinkToPublicAge", 3)
    if len(args) < 2:
        return 0
    linkName = args[1].lower().replace(" ", "").replace("'", "")
    myself = PtGetLocalPlayer()
    player = args[0]
    playerID = player.getPlayerID()
    instanceName = xBotAge.LinkPlayerToPublic(self, linkName, playerID)
    if instanceName:
        msg = "Have fun in " + instanceName + " :)"
    else:
        msg = "I don't know where " + args[1] + " is!"
    PtSendRTChat(myself, [player], msg, 24)
    return 1

# Links the player to the current bot age
#def LinkHere(self, cFlags, player):
def LinkHere(self, cFlags, args = []):
    self.chatMgr.AddChatLine(None, "> LinkHere ", 3)
    if len(args) < 1:
        self.chatMgr.AddChatLine(None, "> LinkHere: len(args) = " + str(len(args)), 3)
        return 0
    elif len(args) > 1:
        LinkToPublicAge(self, cFlags, args)
        return 1
    #else: len(args) == 1
    player = args[0]
    myself = PtGetLocalPlayer()
    botAgeName = xBotAge.GetPlayerAgeInstanceName()
    #if type(player) == list and len(player) > 0:
    #if isPlayerInAge(player[0]):
    #    PtSendRTChat(myself, [player[0]], "You are already in " + botAgeName, 16)
    if isPlayerInAge(player):
        PtSendRTChat(myself, [player], "You are already in " + botAgeName, 16)
    else:
        if len(xBotAge.currentBotAge) < 3:
            xBotAge.currentBotAge = xBotAge.GetBotAge()
        self.chatMgr.AddChatLine(None, ", ".join(xBotAge.currentBotAge), 3)
        #xBotAge.LinkPlayerTo(self, xBotAge.currentBotAge, player[0].getPlayerID())
        #PtSendRTChat(myself, [player[0]], "Welcome to " + botAgeName, 24)
        xBotAge.LinkPlayerTo(self, xBotAge.currentBotAge, player.getPlayerID())
        PtSendRTChat(myself, [player], "Welcome to " + botAgeName, 24)
    return 1
    #else:
    #    return 0

def WarpToMe(self, cFlags, player):
    self.chatMgr.AddChatLine(None, "> WarpToMe", 3)
    myself = PtGetLocalPlayer()
    if type(player) == list and len(player) > 0:
        if isPlayerInAge(player[0]):
            av = PtGetAvatarKeyFromClientID(player[0].getPlayerID()).getSceneObject()
            so = PtGetLocalAvatar()
            pos = so.getLocalToWorld()
            av.netForce(1)
            av.physics.warp(pos)
        else:
            PtSendRTChat(myself, [player[0]], "You must be in my age, use link to join me." , 24)
        return 1
    else:
        return 0

def WarpToPlayer(self, cFlags, player, toPlayer):
    self.chatMgr.AddChatLine(None, "> WarpToPlayer", 3)
    if isPlayerInAge(player):
        av = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
        so = PtGetAvatarKeyFromClientID(toPlayer.getPlayerID()).getSceneObject()
        pos = so.getLocalToWorld()
        av.netForce(1)
        av.physics.warp(pos)
    else:
        PtSendRTChat(myself, [player[0]], "You must be in my age, use link to join me." , 24)
    return 1

def WarpToDefaultLinkInPoint(self, cFlags, player):
    self.chatMgr.AddChatLine(None, "> WarpToDefaultLinkInPoint", 3)
    myself = PtGetLocalPlayer()
    if type(player) == list and len(player) > 0:
        if isPlayerInAge(player[0]):
            av = PtGetAvatarKeyFromClientID(player[0].getPlayerID()).getSceneObject()
            so = PtFindSceneobject('LinkInPointDefault',PtGetAgeName())
            pos = so.getLocalToWorld()
            av.netForce(1)
            av.physics.warp(pos)
        else:
            PtSendRTChat(myself, [player[0]], "You must be in my age, use link to join me." , 24)
        return 1
    else:
        return 0

def WarpToSpawnPoint(self, cFlags, args = []):
    self.chatMgr.AddChatLine(None, "> WarpToSpawnPoint", 3)
    if len(args) < 2:
        return 0
    myself = PtGetLocalPlayer()
    player = args[0]
    try:
        spawnPointNumber = int(args[1])
    except:
        spawnPointNumber = None
    
    if not isPlayerInAge(player):
        PtSendRTChat(myself, [player], "You must be in my age, use link to join me." , 24)
        return 1
    pos = xBotAge.GetSPCoord(spawnPointNumber)
    spName = xBotAge.GetSPName(spawnPointNumber)
    PtSendRTChat(myself, [player], spName , cFlags.flags)
    self.chatMgr.AddChatLine(None, "> " + spName, 3)
    soAvatar = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
    soAvatar.netForce(1)
    soAvatar.physics.warp(pos)
    return 1

def FindSceneObjectPosition(self, name):
    self.chatMgr.AddChatLine(None, "> FindSceneObjectPosition", 3)
    o = list(name + "not found!")
    so = xBotAge.GetFirstSOPosition(name)
    if so:
        pos = so.position()
        o = list(so.getName(), pos.getX(), pos.getY(),  pos.getZ())
    return o

def ShowSceneObjects(self, cFlags, args = []):
    self.chatMgr.AddChatLine(None, "> ShowSceneObjects", 3)
    if len(args) < 2:
        return 0
    myself = PtGetLocalPlayer()
    player = args[0]
    
    if not isPlayerInAge(player):
        PtSendRTChat(myself, [player], "You must be in my age, use link to join me." , 24)
    else:
        name = args[1]
        msg = xBotAge.ShowSOWithCoords(name)
        PtSendRTChat(myself, [player], msg, 16)
    return 1

#
def Red(player):
    #self.chatMgr.AddChatLine(None, "> Red", 3)
    if type(player) == list and len(player) > 0:
        av = PtGetAvatarKeyFromClientID(player[0].getPlayerID()).getSceneObject()
        av.avatar.netForce(1)
        av.avatar.tintSkin(ptColor().red())
        return 1
    else:
        return 0

#Bugs
bugs = PtFindSceneobject("BugFlockingEmitTest", "Garden")
#NE FONCTIONNE PAS...
def Bugs(self, args = []):
    global bugs
    self.chatMgr.AddChatLine(None, "> Bugs", 3)
    if len(args) < 2:
        return 0
    myself = PtGetLocalPlayer()
    player = args[0]
    onOff = args[1].strip().lower()
    av = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
    #av = PtGetLocalAvatar()
    #bugs = PtFindSceneobject("BugFlockingEmitTest", "Garden")
    msg = player.getPlayerName()
    if onOff == "on":
        bugs.draw.netForce(1)
        PtTransferParticlesToObject(bugs.getKey(),av.getKey(),100)
        msg += " calls bugs."
    else:
        PtKillParticles(0,1,av.getKey())
        msg += " has killed bugs."
    PtSendRTChat(myself, [player], msg, 24)

def GetPeople(kind = "buddy", listedPlayers = []):
    #self.chatMgr.AddChatLine(None, "> GetPeople", 3)
    selPlyrList = []
    #agePlayers = PtGetPlayerList()
    vault = ptVault()
    people = None
    if kind == "buddy":
        people = vault.getBuddyListFolder()
    elif kind == "recent":
        people = vault.getPeopleIKnowAboutFolder()
    elif kind == "neighbor":
        try:
            people = vault.getLinkToMyNeighborhood().getAgeInfo().getAgeOwnersFolder()
        except:
            pass
    if type(people) != type(None):
        for bud in people.getChildNodeRefList():
            if isinstance(bud, ptVaultNodeRef):
                # then send to player that might be in another age
                ebud = bud.getChild()
                ebud = ebud.upcastToPlayerInfoNode()
                if type(ebud) != type(None):
                    if ebud.playerIsOnline():
                        player = ptPlayer(ebud.playerGetName(),ebud.playerGetID())
                        if player not in listedPlayers:
                            selPlyrList.append(player)
    return selPlyrList

#
def RemoveCleftLocal(self):
    self.chatMgr.AddChatLine(None, "> RemoveCleftLocal", 3)
    import xCleft
    xCleft.DelPrpLocal()


# link the robot to an age instance
#def LinkBotTo(player, linkName):
def LinkBotTo(self, cFlags, args = []):
    global lastLinkTime
    self.chatMgr.AddChatLine(None, "> LinkBotTo", 3)
    now = datetime.datetime.now()
    minDiff = 10 * 60
    
    if len(args) < 2:
        return 0
    linkName = args[1].lower().replace(" ", "").replace("'", "")
    myself = PtGetLocalPlayer()
    player = args[0]
    msg = "Available links: "
    availableLinks = list()
    for lk  in linkDic.keys():
        if linkDic[lk][2] in allowedAgeInstanceGuids.values():
            availableLinks.append(lk + " : " +linkDic[lk][0])
    msg += ", ".join(availableLinks)
    
    link = None
    # Is the age name in linkDic?
    if (linkName in linkDic.keys()):
        link = linkDic[linkName]
        if not(link[2] in allowedAgeInstanceGuids.values()):
            link = None
    # Trying Mir-o-Bot ages
    elif (linkName in ages.MirobotAgeDict.keys()):
        link = ages.MirobotAgeDict[linkName]
#        xBotAge.currentBotAge = list(link)
#        if len(link) > 4:
#            xBotAge.SetBotAgeSP(link[4])
#            #self.chatMgr.AddChatLine(None, ",".join(xBotAge.currentBotAge), 3)
#        xBotAge.LinkPlayerTo(self, link)
    # Trying MagicBot ages
    elif (linkName in ages.MagicbotAgeDict.keys()):
        link = ages.MagicbotAgeDict[linkName]
#        xBotAge.currentBotAge = list(link)
#        if len(link) > 4:
#            xBotAge.SetBotAgeSP(link[4])
#            #self.chatMgr.AddChatLine(None, ",".join(xBotAge.currentBotAge), 3)
#        xBotAge.LinkPlayerTo(self, link)
    # Definitly not found
    else:
        PtSendRTChat(myself, [player], msg, 16)
        return 0
    #
    if link:
    #if link[2] in allowedAgeInstanceGuids.values():
        if (now - lastLinkTime).total_seconds() > minDiff:
            #prevenir que l'on m'a demander de me lier vers un autre age
            agePlayers = PtGetPlayerList()
            msg = myself.getPlayerName() + " is linking to " + link[0] + " for at least " + str(minDiff / 60) + " minutes... PM me \"link\" to follow me."
            #Garder Cleft peut me faire planter...
            RemoveCleftLocal(self)
            
            xBotAge.currentBotAge = list(link)
            if len(link) > 4:
                xBotAge.SetBotAgeSP(link[4])
                self.chatMgr.AddChatLine(None, ",".join(xBotAge.currentBotAge), 3)
            xBotAge.LinkPlayerTo(self, link)
            lastLinkTime = datetime.datetime.now()
            
            buds = GetPeople("buddy", agePlayers)
            pList = agePlayers + buds
            PtSendRTChat(myself, pList, msg, 24)
        else:
            waitMinutes = int((minDiff - (now - lastLinkTime).total_seconds()) / 60) + 1
            msg = "Please wait " + str(waitMinutes) + " minutes and retry."
            PtSendRTChat(myself, [player], msg, 24)
        return 1
    else:
        PtSendRTChat(myself, [player], msg, 16)
        return 0

def GetCoord(self, cFlags, args = []):
    self.chatMgr.AddChatLine(None, "> GetCoord", 3)
    if len(args) < 1:
        return 0
    myself = PtGetLocalPlayer()
    player = args[0]
    if not isPlayerInAge(player):
        PtSendRTChat(myself, [player], "You must be in my age, use link to join me." , 24)
        return 1
    if len(args) < 2:
        soAvatar = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
        pos = soAvatar.position()
        x = int(round(pos.getX()))
        y = int(round(pos.getY()))
        z = int(pos.getZ()) + 1   
        PtSendRTChat(myself, [player], str(x) + " " + str(y) + " " + str(z) , 16)
        return 1
    else:
        params = args[1].split()
        myself = PtGetLocalPlayer()
        player = args[0]
        if len(params) == 1:
            soName = params[0]
            so = xBotAge.GetFirstSOPosition(soName)
            if so:
                pos = so.position()
                params = [int(round(pos.getX())), int(round(pos.getY())),  int(pos.getZ()) + 1]
                msg = so.getName() + " found at (" + str(params[0]) + ", " + str(params[1]) + ", " + str(params[2]) + ")"
            else:
                msg = soName + " not found!"
            PtSendRTChat(myself, [player], msg, 16)
            return 1
        avatar = GetAgePlayerByName(args[1])
        if avatar:
            soAvatar = PtGetAvatarKeyFromClientID(avatar.getPlayerID()).getSceneObject()
            pos = soAvatar.position()
            params = [int(round(pos.getX())), int(round(pos.getY())),  int(pos.getZ()) + 1]
            msg = soAvatar.getName() + " found at (" + str(params[0]) + ", " + str(params[1]) + ", " + str(params[2]) + ")"
        else:
            msg = str(args[1]) + " not found!"
        PtSendRTChat(myself, [player], msg, 16)
        return 1

def Find(self, cFlags, args = []):
    self.chatMgr.AddChatLine(None, "> Find", 3)
    if len(args) < 1:
        return 0
    myself = PtGetLocalPlayer()
    player = args[0]
    if not isPlayerInAge(player):
        PtSendRTChat(myself, [player], "You must be in my age, use link to join me." , 24)
        return 1
    if len(args) > 1:
        params = args[1].split()
        myself = PtGetLocalPlayer()
        player = args[0]
        bFound = False
        if len(params) == 1:
            soName = params[0]
            so = xBotAge.GetFirstSOPosition(soName)
            if so:
                pos = so.position()
                soPlayer = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
                soPlayer.netForce(1)
                soPlayer.physics.warp(pos)
                msg = so.getName() + " found at (" + str(int(pos.getX())) + ", " + str(int(pos.getY())) + ", " + str(int(pos.getZ())) + ")"
                bFound = True
            else:
                msg = soName + " not found!"
        if not bFound:
            avatar = GetAgePlayerByName(args[1])
            if avatar:
                soAvatar = PtGetAvatarKeyFromClientID(avatar.getPlayerID()).getSceneObject()
                pos = soAvatar.getLocalToWorld()
                soPlayer = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
                soPlayer.netForce(1)
                soPlayer.physics.warp(pos)
                pos = soAvatar.position()
                msg = player.getPlayerName() + " found at (" + str(int(pos.getX())) + ", " + str(int(pos.getY())) + ", " + str(int(pos.getZ())) + ")"
            else:
                msg = args[1] + " not found!"
        PtSendRTChat(myself, [player], msg, 16)
        return 1


def GetRotMat(mat):
    mtr = ptMatrix44()
    matTrans = mat.getTranspose(mtr)
    t = matTrans.getData()
    tr = t[0], t[1], t[2], (0.0, 0.0, 0.0, 1.0)
    mtr.setData(tr)
    rotMat = mtr.getTranspose(ptMatrix44())
    return rotMat

def SetMat(mat, x, y, z):
    mt = ptMatrix44()
    matTrans = mat.getTranspose(mt)
    t = matTrans.getData()
    t2 = t[0], t[1], t[2], (x, y, z, 1.0)
    mt.setData(t2)
    newMat = mt.getTranspose(ptMatrix44())
    return newMat

#
def AutoSaveMat(self, player):
    xSave.WriteMatrix44(self, player, None, "auto")

#
def AutoWarp(self, player):
    xSave.WarpToSaved(self, player, None, "auto")

def AbsoluteGoto(self, cFlags, args = []):
    self.chatMgr.AddChatLine(None, "> AbsoluteGoto", 3)
    if len(args) < 2:
        return 0
    params = args[1].split()
    myself = PtGetLocalPlayer()
    player = args[0]
    if len(params) == 1:
        soName = params[0]
        so = xBotAge.GetFirstSOPosition(soName)
        if so:
            pos = so.position()
            params = [int(round(pos.getX())), int(round(pos.getY())),  int(pos.getZ()) + 1]
            msg = so.getName() + " found at (" + str(params[0]) + ", " + str(params[1]) + ", " + str(params[2]) + ")"
        else:
            msg = soName + " not found!"
            return 1
        PtSendRTChat(myself, [player], msg, 16)
    if len(params) < 3:
        return 0
    if not isPlayerInAge(player):
        PtSendRTChat(myself, [player], "You must be in my age, use link to join me." , 24)
        return 1
    soAvatar = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
    mpos = soAvatar.getLocalToWorld()
    try:
        x = float(params[0])
        y = float(params[1])
        z = float(params[2])
        m = SetMat(mpos, x, y, z)
        soAvatar.netForce(1)
        soAvatar.physics.disable()
        soAvatar.physics.warp(m)
        return 1
    except ValueError:
        return 0

def RelativeGoto(self, cFlags, args = []):
    self.chatMgr.AddChatLine(None, "> RelativeGoto", 3)
    if len(args) < 2:
        return 0
    params = args[1].split()
    if len(params) < 3:
        return 0
    myself = PtGetLocalPlayer()
    player = args[0]
    if not isPlayerInAge(player):
        PtSendRTChat(myself, [player], "You must be in my age, use link to join me." , 24)
        return 1
    soAvatar = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
    pos = soAvatar.getLocalToWorld()
    m = ptMatrix44()
    try:
        m.translate(ptVector3(float(params[0]), float(params[1]), float(params[2])))
        soAvatar.netForce(1)
        soAvatar.physics.disable()
        soAvatar.physics.warp(pos * m)
        soAvatar.physics.enable()
        #AutoSaveMat(self, player)
        #AutoWarp(self, player)
        soAvatar.physics.disable()
        return 1
    except ValueError:
        return 0
    
def Land(self, cFlags, args = []):
    self.chatMgr.AddChatLine(None, "> Land", 3)
    if len(args) < 1:
        return 0
    myself = PtGetLocalPlayer()
    player = args[0]
    if not isPlayerInAge(player):
        PtSendRTChat(myself, [player], "You must be in my age, use link to join me." , 24)
        return 1
    soAvatar = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
    soAvatar.netForce(1)
    soAvatar.physics.enable()
    return 1

def Float(self, cFlags, args = []):
    self.chatMgr.AddChatLine(None, "> Float", 3)
    if len(args) < 1:
        return 0
    elif len(args) < 2:
        return RelativeGoto(self, cFlags, [args[0], "0 0 0"])
    else:
        params = args[1].split()
        if len(params) > 0:
            return RelativeGoto(self, cFlags, [args[0], "0 0 " + str(params[0])])
        else:
            return RelativeGoto(self, cFlags, [args[0], "0 0 0"])

def Jump(self, cFlags, args = []):
    self.chatMgr.AddChatLine(None, "> Jump", 3)
    if len(args) < 2:
        return 0
    params = args[1].split()
    if len(params) == 0:
        return 0
    elif len(params) == 1:
        y = str(0)
        z = str(params[0])
    else:
        y = "-" + str(params[0])
        z = str(params[1])
    if RelativeGoto(self, cFlags, [args[0], "0 " + y + " " + z]):
        return Land(self, cFlags, [args[0]])
    else:
        return 0

def Warp(self, cFlags, args = []):
    self.chatMgr.AddChatLine(None, "> Warp", 3)
    myself = PtGetLocalPlayer()
    player = args[0]
    #PtSendRTChat(myself, [player], str(args) , 1)
    if len(args) == 1:
        return WarpToMe(self, cFlags, [player])
    elif len(args) > 1:
        toPlayer = GetAgePlayerByName(args[1])
        if toPlayer:
            return WarpToPlayer(self, cFlags, args[0], toPlayer)
        else:
            if RelativeGoto(self, cFlags, args) == 0:
                msg = args[1] + " is not a player in this age or it is not coordinates."
                #PtSendRTChat(myself, [player], msg, 16)
                PtSendRTChat(myself, [player], msg, cFlags.flags)
        return 1
    else:
        return 0

def Rotate(self, cFlags, args = []):
    self.chatMgr.AddChatLine(None, "> Rotate", 3)
    if len(args) < 2:
        return 0
    params = args[1].split()
    if len(params) < 2:
        return 0
    myself = PtGetLocalPlayer()
    player = args[0]
    if not isPlayerInAge(player):
        #PtSendRTChat(myself, [player], "You must be in my age, use link to join me." , 24)
        PtSendRTChat(myself, [player], "You must be in my age, use link to join me.", cFlags.flags)
        return 1
    soAvatar = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
    pos = soAvatar.getLocalToWorld()
    m = ptMatrix44()
    axis = 0
    if params[0] == 'x':
        axis = 0
    elif params[0] == 'y':
        axis = 1
    elif params[0] == 'z':
        axis = 2
    else:
        return 0
    try:
        m.rotate(axis, (math.pi * float(params[1])) / 180)
        soAvatar.netForce(1)
        #soAvatar.physics.disable()
        soAvatar.physics.warp(pos * m)
        #AutoSaveMat(self, player)
        #AutoWarp(self, player)
        return 1
    except ValueError:
        return 0

def RotateZ(self, cFlags, args = []):
    self.chatMgr.AddChatLine(None, "> RotateZ", 3)
    #myself = PtGetLocalPlayer()
    #player = args[0]
    #PtSendRTChat(myself, [player], str(args) , 1)
    if len(args) < 2:
        return 0
    params = args[1].split()
    #PtSendRTChat(myself, [player], str(params) , 1)
    if len(params) < 1:
        return 0
    return Rotate(self, cFlags, [args[0], "z " + str(params[0])])

# Save the position of an avatar in a file
def SavePosition(self, cFlags, args = []):
    self.chatMgr.AddChatLine(None, "> SavePosition", 3)
    if len(args) < 1:
        return 0
    myself = PtGetLocalPlayer()
    player = args[0]
    if not isPlayerInAge(player):
        PtSendRTChat(myself, [player], "You must be in my age, use link to join me." , 24)
        return 1
    xSave.WriteMatrix44(self, player)
    PtSendRTChat(myself, [player], "Your position is saved. Use \"ws\" to return to this position." , cFlags.flags)
    return 1

# Warp the avatar to his last saved position
def ReturnToPosition(self, cFlags, args = []):
    self.chatMgr.AddChatLine(None, "> ReturnToPosition", 3)
    if len(args) < 1:
        return 0
    myself = PtGetLocalPlayer()
    player = args[0]
    if not isPlayerInAge(player):
        PtSendRTChat(myself, [player], "You must be in my age, use link to join me." , 24)
        return 1
    ret = xSave.WarpToSaved(self, player)
    if ret:
        PtSendRTChat(myself, [player], "You are at your last saved position." , cFlags.flags)
    else:
        PtSendRTChat(myself, [player], "No saved position found. Did you use \"save\" before?" , cFlags.flags)
    return 1



# Faire faire une animation a l'avatar demandeur
def Animer(self, cFlags, args = []):
    self.chatMgr.AddChatLine(None, "> Animer", 3)
    if len(args) < 2:
        return 0
    myself = PtGetLocalPlayer()
    player = args[0]
    #PtSendRTChat(myself, [player], str(args) , 1)
    params = args[1].split()
    if len(params) < 2:
        return 0
    if not isPlayerInAge(player):
        #PtSendRTChat(myself, [player], "You must be in my age, use link to join me." , 24)
        PtSendRTChat(myself, [player], "You must be in my age, use link to join me.", cFlags.flags)
        return 1
    animName = params[0]
    nbTimes = params[1]
    ret = xAnim.Play(player, animName, nbTimes)
    if ret and animName in travelAnimList:
        AutoSaveMat(self, player)
        AutoWarp(self, player)
    return ret

#**********************************************************************
# Other backend functions. Undocumented.
def RunResponder(key, resp, stateidx = None, netForce = 1, netPropagate = 1, fastforward = 0):
    nt = ptNotify(key)
    nt.addReceiver(resp)
    nt.netPropagate(netPropagate)
    nt.netForce(netForce)
    if stateidx != None:
        nt.addResponderState(stateidx)
    if fastforward:
        nt.setType(PlasmaConstants.PtNotificationType.kResponderFF)
        nt.netPropagate(0)
        nt.netForce(0)
    nt.setActivate(1.0)
    nt.send()
    
def Responder(soName, respName, pfm = None, ageName = None, state = None, ff = False):
    if ageName == None:
        ageName = PtGetAgeName()
    
    so = PtFindSceneobject(soName, ageName)
    respKey = None
    for i in so.getResponders():
        if i.getName() == respName:
            respKey = i
            break
    
    if respKey == None:
        print "Responder():\tResponder not found..."
        return
    
    if pfm == None:
        pms = so.getPythonMods()
        if len(pms) == 0:
            key = respKey
        else:
            key = pms[0]
    else:
        key = PtFindSceneobject(pfm, ageName).getPythonMods()[0]
    
    RunResponder(PtGetLocalAvatar().getKey(), key, stateidx = state, fastforward = ff)

# KiLight(ptPlayer player, int en)
# Activates and deactivates KI light for a player.
def KiLight(self, cFlags, args = []):
    if len(args) < 2:
        return 0
    player = args[0]
    myself = PtGetLocalPlayer()
    if not isPlayerInAge(player):
        PtSendRTChat(myself, [player], "You must be in my age, use link to join me." , cFlags.flags)
        return 1
    soAvatar = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()

    if args[1] == "on":
        en = 1
    elif args[1] == "off":
        en = 0
    else:
        return 0
    for resp in soAvatar.getResponders():
        if (en == 1 and resp.getName() == 'respKILightOn') or (en == 0 and resp.getName() == 'respKILightOff'):
            RunResponder(soAvatar.getKey(), resp)
            break
    return 1

# BugsLight(ptPlayer player, int en)
# Activates and deactivates Eder Kemo bug lights for a player.
def BugsLight(self, cFlags, args = []):
    if len(args) < 2:
        return 0
    player = args[0]
    myself = PtGetLocalPlayer()
    if not isPlayerInAge(player):
        PtSendRTChat(myself, [player], "You must be in my age, use link to join me." , cFlags.flags)
        return 1
    soAvatar = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
    
    if args[1] == "on":
        en = 1
    elif args[1] == "off":
        en = 0
    else:
        return 0
    PtSetLightAnimStart(soAvatar.getKey(), "RTOmni-BugLightTest", en)
    return 1
#**********************************************************************

##
#class AddPrp:
#    global debugInfo
#    def onAlarm(self, context):
#        import xCleft
#        debugInfo = "AddPrp"
#        xCleft.AddPrp()
##
#class EnableAll:
#    global debugInfo
#    def onAlarm(self, context = 0):
#        import xCleft
#        debugInfo = "EnableAll"
#        xCleft.EnableAll(context)
#
#def AddCleft(self, args = []):
#    global debugInfo
#    self.chatMgr.AddChatLine(None, "Adding Cleft...", 3)
#    try:
#        #import xCleft
#        debugInfo = "AddCleft"
#        PtSetAlarm (1,AddPrp(), 0)
#        PtSetAlarm(10, EnableAll(), 0)
#        self.chatMgr.AddChatLine(None, "Cleft added! " + debugInfo, 3)
#    except:
#        self.chatMgr.AddChatLine(None, "Error while adding Cleft.", 3)
#    return 1

#
def AddCleft(self, cFlags, args = []):
    self.chatMgr.AddChatLine(None, "> AddCleft", 3)
    if len(args) < 1:
        return 0
    myself = PtGetLocalPlayer()
    player = args[0]
    if not isPlayerInAge(player):
        #PtSendRTChat(myself, [player], "You must be in my age, use link to join me." , 24)
        PtSendRTChat(myself, [player], "You must be in my age, use link to join me.", cFlags.flags)
        return 1
    import xCleft
    ret = xCleft.AddCleft(self, args)
    if ret:
        PtSetAlarm(5, xBotAge.AlarmDisablePanicLinks(), 0)
        #PtSendRTChat(myself, [player], "I'm loading Cleft for you... Please wait." , 16)
        PtSendRTChat(myself, [player], "I'm loading Cleft for you... Please wait.", cFlags.flags)
    else:
        #PtSendRTChat(myself, [player], "Error while loading Cleft." , 16)
        PtSendRTChat(myself, [player], "Error while loading Cleft.", cFlags.flags)
    return 1

#
def DisablePanicLinks(self, cFlags, args = []):
    myself = PtGetLocalPlayer()
    player = args[0]
    if not isPlayerInAge(player):
        PtSendRTChat(myself, [player], "You must be in my age, use link to join me.", cFlags.flags)
        return 1
    xBotAge.DisablePanicLinks()
    self.chatMgr.AddChatLine(None, "Panic links are disabled!", 3)
    PtSendRTChat(myself, [player], "Panic zones are disabled!", cFlags.flags)

#
def Ring(self, cFlags, args = []):
    if len(args) < 2:
        return 0
    import xHood
    params = args[1].split()
    if len(params) < 2:
        return 0
    myself = PtGetLocalPlayer()
    player = args[0]
    if not isPlayerInAge(player):
        PtSendRTChat(myself, [player], "You must be in my age, use link to join me." , cFlags.flags)
        return 1
    soAvatar = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
    if len(xBotAge.currentBotAge) > 1:
        if xBotAge.currentBotAge[1] == "Neighborhood":
            self.chatMgr.AddChatLine(None, ">Ring ", 3)
            #1st parameter: color
            color = params[0].lower().strip()
            #bOn = bOn.lower()
            #if not (color in ("yellow", "blue", "red", "white", "white2", "white3", "white4")):
            if not (color in ("yellow", "blue", "red", "white")):
                color = "red"
            bOn = 1
            #2nd parameter: on/off
            if params[1].lower().strip() == "off":
                bOn = 0
            dist = 3
            height = 4
            #3rd parameter: height
            if len(params) > 2:
                try:
                    height = float(params[2].lower().strip())
                except:
                    self.chatMgr.AddChatLine(None, "Err: the optional 3rd parameter must be a number!", 3)
                    PtSendRTChat(myself, [player], "The optional 3rd parameter must be a number!" , cFlags.flags)
                    return 1
            #4th parameter: distance
            if len(params) > 3:
                try:
                    dist = float(params[3].lower().strip())
                except:
                    self.chatMgr.AddChatLine(None, "Err: the optional 4th parameter must be a number!", 3)
                    PtSendRTChat(myself, [player], "The optional 4th parameter must be a number!" , cFlags.flags)
                    return 1
            self.chatMgr.AddChatLine(None, "ring " + color + ", " + str(bOn), 3)
            xHood.Entourer(dist, height, color, 9, soAvatar, bOn)
            self.chatMgr.AddChatLine(None, "=> nb clones: " + str(len(xHood.lstClones)), 3)
            PtSendRTChat(myself, [player], "I'm creating a fire marble ring for you, wait a bit ... (tell me if it does'nt work)" , cFlags.flags)
            return 1
        else:
            self.chatMgr.AddChatLine(None, "=> Je ne suis pas dans un Hood!", 3)
            PtSendRTChat(myself, [player], "This command does'nt work here, we must be in a Hood." , cFlags.flags)
            return 1
    else:
        self.chatMgr.AddChatLine(None, "=> Je ne sais pas dans quel age je suis!", 3)
        PtSendRTChat(myself, [player], "Oops, I don't know where I am ..." , cFlags.flags)
        return 1

# Envoyer une note d'aide au demandeur (inspire du script de Michel)
def Help(self, cFlags, args = []):
    self.chatMgr.AddChatLine(None, "> Help", 3)
    if len(args) < 1:
        return 0
    myself = PtGetLocalPlayer()
    player = args[0]
    idAvatar = player.getPlayerID()
    
    # aide sur une commande (en chat prive)
    if len(args) > 1:
        cmdName = args[1]
        HelpCmd(player, cFlags, cmdName)
        return 1
    # si pas de commade specifiee, envoyer le KiMail
    
#    #pour en mettre une copie dans mon journal Nexus
#    journals = ptVault().getAgeJournalsFolder()
#    agefolderRefs = journals.getChildNodeRefList()
#    for agefolderRef in agefolderRefs:
#        agefolder = agefolderRef.getChild()
#        if agefolder.getType() == PtVaultNodeTypes.kFolderNode:
#            agefolder = agefolder.upcastToFolderNode()
#            if agefolder.folderGetName() == 'Nexus':
#                journal = agefolder
#                break

    title = "Mir-o-Bot help"
    msg = "Shorah!\nList of commands available:\n"
    msg += "------------------------------------\n\n"
    msg += "ring [yellow/blue/red/white] [on/off] : Activates and deactivates a ring of Firemarbles (in hood only).\n"
    msg += "    Optionally: ring [color] [on] [height] [radius].\n\n"
    msg += "nopanic : Disables most of the panic zones.\n\n"
    msg += "save : Save your current position.\n\n"
    msg += "ws : Warps you to your last saved position.\n\n"
    msg += "link or meet : links your avatar to Mir-o-Bot's current Age.\n\n"
    msg += "sp [number]: warps you to a spawn point (number between 0 and 20). Only works in city.\n\n"
    msg += "onbot or warp or w : warps your avatar to Mir-o-Bot's current position.\n\n"
    msg += "warp or warp [avatar name] or warp [x] [y] [z] : see onbot, find and rgoto.\n (the avatar name can be incomplete).\n\n"
    msg += "wd : warps your avatar to the default linkin point.\n\n"
    msg += "to {city/greeters/kirel/kveer/watcher/...} : links YOU to a public age\n"
    msg += "or a Mir-o-Bot age {Ae'gura/Ahnonay Cathedral/Cleft/Relto/Eder Gira/Eder Kemo/Er'cana/Gahreesen/Hood/Kadish/Pellet Cave/Teledahn}.\n"
    msg += "or a Magic age: to {MBCity/MBRelto/MBErcana/MBTeledahn/MBOffice/MBCleft/MBKadish/MBKveer/MBHood/MBDereno/MBRudenna}.\n\n"
#    msg += "linkbotto {fh/fhci/fhde/fhga/fhte/fhka/fhgi/fhcl/mbe/mcl/mre/mkv/mka/scl}: links Mir-o-Bot to the specified Age.\n"
#    msg += "   linkto fh   = The Fun House\n"
#    msg += "   linkto fhci = The Fun House - City\n"
#    msg += "   linkto fhde = Fun House\'s (1) Eder Delin\n"
#    msg += "   linkto fhga = The Fun House - Gahreesen\n"
#    msg += "   linkto fhte = The Fun House - Teledahn\n"
#    msg += "   linkto fhcl = Fun House\'s Cleft\n"
#    msg += "   linkto fhka = The Fun House - Kadish Tolesa\n"
#    msg += "   linkto fhgi = The Fun House - Eder Gira\n"
#    msg += "   linkto mbe = MagicBot Ercana\n"
#    msg += "   linkto mcl = Magic Cleft\n"
#    msg += "   linkto mre = Magic Relto\n"
#    msg += "   linkto mkv = Magic Kveer\n"
#    msg += "   linkto mka = Magic Tolesa\n"
#    msg += "   linkto scl = Stone5's Cleft\n\n"
    msg += "coord : returns your current position.\n\n"
    msg += "agoto [x] [y] [z] or teleport [x] [y] [z] : disable physics and warps your avatar to an absolute position.\n\n"
    msg += "rgoto [x] [y] [z] or xwarp [x] [y] [z] or warp [x] [y] [z] : disable physics and warps your avatar relative to your current position.\n\n"
    msg += "rot [axis] [angle] : disables physics and rotates your avatar along the specified x, y or z axis, and following the specified angle in degrees.\n\n"
    msg += "turn [angle] : disables physics and rotates your avatar on Z axis relative to your current position.\n\n"
    msg += "float [height]: disables physics and warps your avatar up or down relative to your current position.\n\n"
    msg += "jump [height] or jump [forward][height]: jump in the air.\n\n"
    msg += "land or normal: enables physics.\n\n"
    msg += "find [object or avatar name]: warps you to the first object or avatar found (use * as any unknown caracters but not only a *), this command is case sensitive.\n\n"
    msg += "show [object name]: shows you the list of object names found (use * as any unknown caracters but not only a *), this command is case sensitive.\n\n"
    msg += "addcleft : Add a partialy invisible Cleft and disable panic links, enjoy!\n\n"
    msg += "Some animations: [animation name] [n] \n"
    msg += "    where [animation name] is in: \n"
    msg += "    {ladderup/ladderdown/climbup/climbdown/stairs\n"
    msg += "    /walk/run/back/moonwalk/swim\n"
    msg += "    /dance/crazy/what/zomby/hammer/wait/laugh/thank/talk}.\n"
    msg += "    and [n] is the number of times you want to do.\n\n"
    msg += "help : sends you this text note.\nhelp [command name]: PM you a specific help on a command.\n"
    msg += "\nThats all for the moment."

    helpNote = None
    # create the note
    try:
        helpNote = ptVaultTextNoteNode(0)
        helpNote.setTextW(msg)
        helpNote.setTitleW(title)
        #BKCurrentContent = journal.addNode(helpNote)
        #journal.addNode(helpNote)
    except:
        msg = "An error occured when creating help note."
        PtSendRTChat(myself, [player], msg, cFlags.flags)

    #note.EnvoyerNote(note='',idavatar=0)
    if helpNote != None:
        try:
            helpNote.sendTo(idAvatar)
            msg = "I send you a Ki-mail..."
        except:
            msg = "An error occured while sending help note."
        PtSendRTChat(myself, [player], msg, cFlags.flags)
    
    msg = "You can also use \"help [command name]\".\n ** Available commands : " + ", ".join(cmdDict.keys())
    PtSendRTChat(myself, [player], msg, cFlags.flags)
    return 1

#
def HelpCmd(player, cFlags, cmdName):
    #self.chatMgr.AddChatLine(None, "> HelpCmd", 3)
    myself = PtGetLocalPlayer()
    try:
        cmdName = RetreaveCmdName(cmdName)
    except:
        pass
    #raccourcis pour les animations (sans taper "anim")
    animCmd = RetreaveAnimCmdName(cmdName)
    if animCmd:
        cmdName = "anim"
    #traitement "normal"
    if cmdName in cmdDict:
        helps = cmdDict[cmdName][1]
        for msg in helps:
            PtSendRTChat(myself, [player], msg, cFlags.flags)    
    else:
        #command not found, PM command list
        msg = "\"" + cmdName + "\" not found."
        PtSendRTChat(myself, [player], msg, cFlags.flags)
        msg = "Available commands: " + ", ".join(cmdDict.keys())
        PtSendRTChat(myself, [player], msg, cFlags.flags)
    return 1

def TestMsg(self, cFlags, args = []):
    self.chatMgr.AddChatLine(None, "> TestMsg", 3)
    if len(args) < 2:
        return 0
    myself = PtGetLocalPlayer()
    player = args[0]
    nFlag = int(args[1])
    PtSendRTChat(myself, [player], "type msg: %i" % (nFlag) , nFlag)
    return 1


#----------------------------------------------------------------------------#
#   Dictionnaire Command/Methode/(help)
#----------------------------------------------------------------------------#
cmdDict = {
'link':(LinkHere,["link or meet : links your avatar to Mir-o-Bot's current Age."]),
'linkbotto':(LinkBotTo,["linkbotto {fh/fhci/fhde/fhga/fhte/fhka/fhgi/fhcl/mbe/mcl/mre/mkv/mka/scl}:", 
    " links Mir-o-Bot to the specified Age."]),
'to':(LinkToPublicAge,["to {city/greeters/kirel/kveer/watcher/...} : links you to a public age or a Mir-o-bot age (aegura/hood/teledahn/...)."]),
#'meet':(LinkHere,[""]),
#'w':(WarpToMe,[""]),
'onbot':(WarpToMe,["onbot or warp or w: warps your avatar to Mir-o-Bot's current position."]),
'wd':(WarpToDefaultLinkInPoint,["wd: warps your avatar to the default linkin point."]),
'warp':(Warp,["warp or warp [avatar name] or warp [x] [y] [z] : see onbot, find and rgoto."]),
'coord':(GetCoord,["coord : returns your current position."]),
'save':(SavePosition,["save : saves your current position."]),
'ws':(ReturnToPosition,["ws : warps you to your last saved position (if exists)."]),
'agoto':(AbsoluteGoto,["agoto [x] [y] [z] or teleport [x] [y] [z] :", 
    " disable physics and warps your avatar to an absolute position."]),
#'teleport':(AbsoluteGoto,[""]),
'rgoto':(RelativeGoto,["rgoto [x] [y] [z] or xwarp [x] [y] [z] or warp [x] [y] [z] :", 
    " disable physics and warps your avatar relative to your current position."]),
#'xwarp':(RelativeGoto,[""]),
'land':(Land,["land or normal: enables physics."]),
#'normal':(Land,[""]),
'turn':(RotateZ,["turn [angle] : disables physics and rotates your avatar on Z axis relative to your current position."]),
'rot':(Rotate,["rot [axis] [angle] : disables physics and rotates your avatar along the specified x, y or z axis,", 
    " and following the specified angle in degrees."]),
'float':(Float,["float [height] or float [forward] [height]: disables physics and warps your avatar up or down relative to your current position."]),
'jump':(Jump,["jump [height] or jump [forward][height]: jump in the air."]),
'find':(Find,["find [object or avatar name]:", 
    " warps you to the avatar", 
    " or the first object found (use * as any unknown caracters but not a * alone), this command is case sensitive.\n\"show [object name]\" will help you to find object names"]),
'show':(ShowSceneObjects,["show [object name]: shows you the list of object names found (use * as any unknown caracters but not a * alone), this command is case sensitive.\nTry \"find [one of the listed objects]\""]),
'anim':(Animer, ["[animation name] [n]:", 
    " where [animation name] is in:", 
    "    {ladderup/ladderdown/climbup/climbdown/stairs", 
    "    /walk/run/back/moonwalk/swim", 
    "    /dance/crazy/what/zomby/hammer/wait/laugh/thank/talk}.", 
    " and [n] is the number of times you want to do."]),
'addcleft':(AddCleft,["addcleft: adds invisible Cleft."]),
'sp':(WarpToSpawnPoint,["sp [number(0-20)]: warps you to a spawn point (works in city)."]),
#'*':(TestMsg,[""]),
#'bugs':(Bugs,["Bugs {on/off} : Bugs on you or not."]),
'ki':(KiLight,["ki {on/off} : Activates and deactivates KI light."]),
'light':(BugsLight,["light {on/off} : Activates and deactivates Eder Kemo bug lights ."]),
'ring':(Ring,["ring [yellow/blue/red/white] [on/off] : Activates and deactivates a ring of Firemarbles (IN HOOD ONLY). Optionally: ring [color] [on] [height] [radius]"]),
'nopanic':(DisablePanicLinks,["Disables most of the panic zones."]),
'help':(Help, ["help: sends you a help text note.", "help [command name]: PM you a specific help on a command."])
}
#'red':Red,
alternatives = {
'link':['link', 'meet', 'linkme', 'lier'],
'linkbotto':['linkbotto', 'botto'],
'to':['to', 'linkmeto'],
'onbot':['w', 'onbot'],
'warp':['warp', 'vers'],
'wd':['wd'],
'coord':['coord', 'locate', 'pos'],
'agoto':['agoto', 'teleport'],
'rgoto':['rgoto', 'xwarp'],
'land':['land', 'normal'],
'turn':['turn'],
'rot':['rot'],
'float':['float', 'fl', 'fly', 'flotte'],
'jump':['jump', 'j', 'runjump', 'rj', 'saut'],
'find':['find', 'fi', 'warpto', 'wt', 'trouve'],
'show':['show', 'search', 's', 'montre'],
'help':['help', 'h', 'elp', 'aide', '?'],
'anim':['anim'],
}

altAnim = {
'danse'     :['danse'     , 'dance'],
'fou'       :['fou'       , 'crazy'],
'echelle'   :['echelle'   , 'climbup', 'climb'],
'ladderup'  :['ladderup'],
'descendre' :['descendre' , 'climbdown'],
'ladderdown':['ladderdown'],
'escalier'  :['escalier'  , 'stairs'],
'quoi'      :['quoi'      , 'what'],
'nage'      :['nage'      , 'swim'],
'moonwalk'  :['moonwalk'],
'zombie'    :['zombie'    , 'zomby'],
'marteau'   :['marteau'   , 'hammer'],
'attente'   :['attente'   , 'wait'],
'rire'      :['rire'      , 'laugh'],
'merci'     :['merci'     , 'thank'],
'marche'    :['marche'    , 'walk'],
'cours'     :['cours'     , 'run'],
'recule'    :['recule'    , 'back'],
'parler'    :['parler'    , 'talk'],
}

travelAnimList = ("echelle", "descendre", "ladderup", "ladderdown", "escalier", "nage", "marche", "cours", "recule")

def RetreaveCmdName(altCmdName):
    for k, v in alternatives.items():
        if altCmdName.lower() in v:
            return str(k)
    return altCmdName

def RetreaveAnimCmdName(altCmdName):
    for k, v in altAnim.items():
        if altCmdName.lower() in v:
            return str(k)
    return None
    

#----------------------------------------------------------------------------#
#   Method to call the desired method
#----------------------------------------------------------------------------#
def CallMethod(self, fromAge, cmdName, cFlags, args = []):
    #traiter les noms de commande alternatifs
    try:
        cmdName = RetreaveCmdName(cmdName)
        #self.chatMgr.DisplayStatusMessage("=> " + cmdName)
    except:
        pass
    #raccourcis pour les animations (sans taper "anim")
    animCmd = RetreaveAnimCmdName(cmdName)
    if animCmd:
        if len(args) > 1:
            args[1] = animCmd + " " + args[1]
        else:
            args.append(animCmd + " 1")
        cmdName = "anim"
    #traitement "normal"
    if cmdName in cmdDict:
        if len(args) == 0:
            return cmdDict[cmdName][0]()
        else:
            return cmdDict[cmdName][0](self, cFlags, args)
    else:
        return 0

