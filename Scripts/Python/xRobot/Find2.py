# ** Test de recherche d'un joueur **
from Plasma import *
from PlasmaVaultConstants import *

import datetime

#PtGetAvatarKeyFromClientID(clientID)
#PtGetClientName(avatarKey=None)

#
def FindPlayerByID(playerID):
    tempNode = ptVaultPlayerInfoNode()
    tempNode.playerSetID(playerID)

    try:
        vault = ptVault()
        playerName = vault.findNode(tempNode).upcastToPlayerInfoNode().playerGetName()
    except:
        playerName = ""
    return playerName

#
def FindPlayerByName(playerName):
    tempNode = ptVaultPlayerInfoNode()
    tempNode.playerSetName(playerName)

    try:
        vault = ptVault()
        playerID = vault.findNode(tempNode).upcastToPlayerInfoNode().playerGetID()
    except:
        playerID = 0L
    return playerID

#
def GetPlayerByName(playerName):
    tempNode = ptVaultPlayerInfoNode()
    tempNode.playerSetName(playerName)

    try:
        vault = ptVault()
        pin = vault.findNode(tempNode).upcastToPlayerInfoNode()
        return pin
    except:
        return None

#
def GetPlayerTimeByName(playerName):
    pin = GetPlayerByName(playerName)
    if pin is not None:
        timeFormat = "%Y-%m-%d %H:%I:%S"
        modifyTime = pin.getModifyTime()
        modifyTime = datetime.datetime.fromtimestamp(modifyTime)
        modifyTime = modifyTime.strftime(timeFormat)
        return modifyTime
    else:
        return None

### Ca ne marche pas, setID ne fonctionne pas
### par contre setGameGuid et setGameName oui
##def GetGameByID(gameID):
##    tempNode = ptVaultMarkerGameNode()
##    tempNode.setID(gameID)
##
##    try:
##        node = ptVault().findNode(tempNode)
##        if node.getType() == PtVaultNodeTypes.kMarkerGameNode:
##            game = node.upcastToMarkerGameNode()
##            return game
##        else:
##            return None
##    except:
##        return None

# Recherche un jeu de marqueur par son Guid
def GetGameByGuid(gameGuid):
    tempNode = ptVaultMarkerGameNode()
    tempNode.setGameGuid(gameGuid)

    try:
        node = ptVault().findNode(tempNode)
        if node.getType() == PtVaultNodeTypes.kMarkerGameNode:
            game = node.upcastToMarkerGameNode()
            print "game found"
            return game
        else:
            print "game not found"
            return None
    except:
        print "error in GetGameByGuid"
        return None


# *** TESTS ***

##
def GetHoodByName(hoodName):
    tempNode = ptVaultAgeInfoNode()
    tempNode.setAgeFilename("Neighborhood")
    tempNode.setAgeInstanceName(hoodName)

    try:
        vault = ptVault()
        ain = vault.findNode(tempNode).upcastToAgeInfoNode()
        return ain
    except:
        return None

#
def GetDRCHoodByNum(hoodNum):
    tempNode = ptVaultAgeInfoNode()
    tempNode.setAgeFilename("Neighborhood")
    tempNode.setAgeSequenceNumber(hoodNum)

    try:
        vault = ptVault()
        ain = vault.findNode(tempNode).upcastToAgeInfoNode()
        return ain
    except:
        return None

## fonctions du KI
#def IGetNeighborhood(self):
#    "find the neighborhood for this player"
#    try:
#        return ptVault().getLinkToMyNeighborhood().getAgeInfo()
#    except AttributeError:
#        PtDebugPrint("xKI: neighborhood was not found",level=kDebugDumpLevel)
#        return None
#
##
#def IGetNeighbors(self):
#    "find our lovely neighbors"
#    try:
#        return self.IGetNeighborhood().getAgeOwnersFolder()
#    except AttributeError:
#        PtDebugPrint("xKI: list of neighbors was not found",level=kDebugDumpLevel)
#        return None

#Lister les Journaux
def GetJournals():
    journals = ptVault().getAgeJournalsFolder()
    ageFolderRefs = journals.getChildNodeRefList()
    print "ChildNodeCount\tClientID\tCreateAgeGuid\tCreateAgeName\tCreateAgeTime\tCreateTime\tCreatorNodeID\tFolderName\tFolderType\tID\tModifyTime\tOwnerNodeID\tType"
    for ageFolderRef in ageFolderRefs:
        ageFolder = ageFolderRef.getChild()
        if ageFolder.getType() == PtVaultNodeTypes.kFolderNode:
            ageFolder = ageFolder.upcastToFolderNode()
            print "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{10}\t{11}\t{12}".format(
            ageFolder.getChildNodeCount(), 
            ageFolder.getClientID(), 
            ageFolder.getCreateAgeGuid(), 
            ageFolder.getCreateAgeName(), 
            ageFolder.getCreateAgeTime(), 
            ageFolder.getCreateTime(), 
            ageFolder.getCreatorNodeID(), 
            ageFolder.getFolderName(), 
            ageFolder.getFolderType(), 
            ageFolder.getID(), 
            ageFolder.getModifyTime(), 
            ageFolder.getOwnerNodeID(), 
            ageFolder.getType()
            )

#
def GetMyHoodLink():
    hood = ptVault().getLinkToMyNeighborhood()
    print "getChildNodeCount    = " + str(hood.getChildNodeCount())
    print "getClientID          = " + str(hood.getClientID())
    print "getCreateAgeGuid     = " + str(hood.getCreateAgeGuid())
    print "getCreateAgeName     = " + str(hood.getCreateAgeName())
    print "getCreateAgeTime     = " + str(hood.getCreateAgeTime())
    print "getCreateTime        = " + str(hood.getCreateTime())
    print "getCreatorNodeID     = " + str(hood.getCreatorNodeID())
    print "getID                = " + str(hood.getID())
    print "getLocked            = " + str(hood.getLocked())
    print "getModifyTime        = " + str(hood.getModifyTime())
    print "getOwnerNodeID       = " + str(hood.getOwnerNodeID())
    print "getType              = " + str(hood.getType())
    print "getVolatile          = " + str(hood.getVolatile())

#
def GetMyHoodInfo():
    hood = ptVault().getLinkToMyNeighborhood().getAgeInfo()
    print "getAgeDescription        = " + str(hood.getAgeDescription())
    print "getAgeFilename           = " + str(hood.getAgeFilename())
    #print "getAgeID                 = " + str(hood.getAgeID())
    print "getAgeInstanceGuid       = " + str(hood.getAgeInstanceGuid())
    print "getAgeInstanceName       = " + str(hood.getAgeInstanceName())
    #print "getAgeLanguage           = " + str(hood.getAgeLanguage())
    #print "getAgeOwnersFolder       = " + str(hood.getAgeOwnersFolder())
    #print "getAgeSDL                = " + str(hood.getAgeSDL())
    print "getAgeSequenceNumber     = " + str(hood.getAgeSequenceNumber())
    print "getAgeUserDefinedName    = " + str(hood.getAgeUserDefinedName())
    #print "getCanVisitFolder        = " + str(hood.getCanVisitFolder())
    #print "getChildAgesFolder       = " + str(hood.getChildAgesFolder())
    print "getChildNodeCount        = " + str(hood.getChildNodeCount())
    #print "getChildNodeRefList      = " + str(hood.getChildNodeRefList())
    #print "getClientID              = " + str(hood.getClientID())
    #print "getCreateAgeCoords       = " + str(hood.getCreateAgeCoords())
    #print "getCreateAgeGuid         = " + str(hood.getCreateAgeGuid())
    #print "getCreateAgeName         = " + str(hood.getCreateAgeName())
    #print "getCreateAgeTime         = " + str(hood.getCreateAgeTime())
    print "getCreateTime            = " + str(hood.getCreateTime())
    #print "getCreatorNode           = " + str(hood.getCreatorNode())
    print "getCreatorNodeID         = " + str(hood.getCreatorNodeID())
    #print "getCzar                  = " + str(hood.getCzar())
    #print "getCzarID                = " + str(hood.getCzarID())
    print "getDisplayName           = " + str(hood.getDisplayName())
    print "getID                    = " + str(hood.getID())
    print "getModifyTime            = " + str(hood.getModifyTime())
    #print "getNode(id))             = " + str(hood.getNode(id))
    #print "getOwnerNode             = " + str(hood.getOwnerNode())
    #print "getOwnerNodeID           = " + str(hood.getOwnerNodeID())
    #print "getParentAgeLink         = " + str(hood.getParentAgeLink())
    print "getType                  = " + str(hood.getType())
    #print "hasNode(id))             = " + str(hood.hasNode(id))
    print "isPublic                 = " + str(hood.isPublic())

#playerID = FindPlayerByName(playerName)
def Hood():
    #hood = ptVault().getLinkToMyNeighborhood().getAgeInfo()
    tempNode = ptVaultAgeInfoNode()
    #tempNode.setCreatorNodeID(11139429L)
    ##tempNode.setCreatorNodeID(15112638L)
    #tempNode.setType(33)
    
    tempNode.setAgeFilename("Neighborhood")
    #tempNode.setAgeInstanceName("Hood")
    #tempNode.setAgeInstanceName("Bevin")
    #tempNode.setAgeInstanceGuid("0e28e00d-6a4e-4131-8ed8-95bfcec2631b")
    tempNode.setAgeUserDefinedName("MagicBot's")
    #tempNode.setAgeSequenceNumber(0)

    try:
        vault = ptVault()
        hood = vault.findNode(tempNode).upcastToAgeInfoNode()
    except:
        hood = tempNode

    print "getAgeDescription        = " + str(hood.getAgeDescription())
    print "getAgeFilename           = " + str(hood.getAgeFilename())
    print "getAgeInstanceGuid       = " + str(hood.getAgeInstanceGuid())
    print "getAgeInstanceName       = " + str(hood.getAgeInstanceName())
    print "getAgeSequenceNumber     = " + str(hood.getAgeSequenceNumber())
    print "getAgeUserDefinedName    = " + str(hood.getAgeUserDefinedName())
    print "getChildNodeCount        = " + str(hood.getChildNodeCount())
    print "getCreateTime            = " + str(hood.getCreateTime())
    print "getCreatorNodeID         = " + str(hood.getCreatorNodeID())
    print "getDisplayName           = " + str(hood.getDisplayName())
    print "getID                    = " + str(hood.getID())
    print "getModifyTime            = " + str(hood.getModifyTime())
    print "getType                  = " + str(hood.getType())
    print "isPublic                 = " + str(hood.isPublic())

#
def TestHood():
    tempNode = ptVaultAgeInfoNode()
    tempNode.setAgeFilename("Neighborhood")
    #tempNode.setAgeInstanceName("Hood")
    #tempNode.setAgeInstanceName("Bevin")
    #tempNode.setAgeInstanceGuid("0e28e00d-6a4e-4131-8ed8-95bfcec2631b")
    tempNode.setAgeUserDefinedName("MagicBot's")
    #tempNode.setAgeSequenceNumber(0)
    
    #modifie dans pyVaultAgeInfoNode.cpp (n'etaient pas implementes)
    #SetAgeFilename
    #SetAgeInstanceName
    #SetAgeUserDefinedName
    #Set(Age)SequenceNumber

    print "getAgeDescription        = " + str(tempNode.getAgeDescription())
    print "getAgeFilename           = " + str(tempNode.getAgeFilename())
    print "getAgeInstanceGuid       = " + str(tempNode.getAgeInstanceGuid())
    print "getAgeInstanceName       = " + str(tempNode.getAgeInstanceName())
    print "getAgeSequenceNumber     = " + str(tempNode.getAgeSequenceNumber())
    print "getAgeUserDefinedName    = " + str(tempNode.getAgeUserDefinedName())
    print "getChildNodeCount        = " + str(tempNode.getChildNodeCount())
    print "getCreateTime            = " + str(tempNode.getCreateTime())
    print "getCreatorNodeID         = " + str(tempNode.getCreatorNodeID())
    print "getDisplayName           = " + str(tempNode.getDisplayName())
    print "getID                    = " + str(tempNode.getID())
    print "getModifyTime            = " + str(tempNode.getModifyTime())
    print "getType                  = " + str(tempNode.getType())
    print "isPublic                 = " + str(tempNode.isPublic())

# Ex: GetHood("MagicBot's") or GetHood("DRC", 5000)
def GetHood(ageUserDefinedName, ageSequenceNumber=0):
    tempNode = ptVaultAgeInfoNode()
    tempNode.setAgeFilename("Neighborhood")
    tempNode.setAgeUserDefinedName(ageUserDefinedName)
    tempNode.setAgeSequenceNumber(ageSequenceNumber)
    try:
        hood = ptVault().findNode(tempNode).upcastToAgeInfoNode()
        return hood
    except:
        return None

#
def GetNeighbors(ageUserDefinedName, ageSequenceNumber=0):
    hood = GetHood(ageUserDefinedName, ageSequenceNumber)
    if hood is None:
        return None
    else:
        neighbors = hood.getAgeOwnersFolder()
        if neighbors is not None:
            playerlist = neighbors.getChildNodeRefList()
            onlineList = []
            for plyr in playerlist:
                if isinstance(plyr, ptVaultNodeRef):
                    PLR = plyr.getChild()
                    PLR = PLR.upcastToPlayerInfoNode()
                    if PLR is not None and PLR.getType() == PtVaultNodeTypes.kPlayerInfoNode:
                        #onlineList.append(PLR)
                        onlineList.append([PLR.playerGetName(), PLR.playerGetID()])
            return onlineList
        else:
            return None

#
def GetHoodChilds(ageUserDefinedName, ageSequenceNumber=0):
    hood = GetHood(ageUserDefinedName, ageSequenceNumber)
    if hood is None:
        return None
    else:
        nodeRefList = hood.getChildNodeRefList()
        if nodeRefList is not None:
            nodeList = []
            for nodeRef in nodeRefList:
                if isinstance(nodeRef, ptVaultNodeRef):
                    node = nodeRef.getChild()
                    nodeList.append(node)
            return nodeList

#
def piln():
    tempNode = ptVaultPlayerInfoListNode()
    #tempNode.setCreatorNodeID(11139429L)
    tempNode.setCreatorNodeID(11139429L)
    tempNode.setFolderType(19)
    tempNode.setType(30)

    try:
        vault = ptVault()
        node = vault.findNode(tempNode).upcastToPlayerInfoListNode()
    except:
        node = None
#
    #hood = ptVault().getLinkToMyNeighborhood().getAgeInfo()
    #node = hood.getAgeOwnersFolder()
    
    print "folderGetName       = " + str(node.folderGetName())
    print "folderGetType       = " + str(node.folderGetType())
    print "getChildNodeCount   = " + str(node.getChildNodeCount())
    print "getChildNodeRefList = " + str(node.getChildNodeRefList())
    print "getClientID         = " + str(node.getClientID())
    print "getCreateAgeCoords  = " + str(node.getCreateAgeCoords())
    print "getCreateAgeGuid    = " + str(node.getCreateAgeGuid())
    print "getCreateAgeName    = " + str(node.getCreateAgeName())
    print "getCreateAgeTime    = " + str(node.getCreateAgeTime())
    print "getCreateTime       = " + str(node.getCreateTime())
    print "getCreatorNode      = " + str(node.getCreatorNode())
    print "getCreatorNodeID    = " + str(node.getCreatorNodeID())
    print "getFolderName       = " + str(node.getFolderName())
    print "getFolderNameW      = " + str(node.getFolderNameW())
    print "getFolderType       = " + str(node.getFolderType())
    print "getID               = " + str(node.getID())
    print "getModifyTime       = " + str(node.getModifyTime())
    print "getOwnerNode        = " + str(node.getOwnerNode())
    print "getOwnerNodeID      = " + str(node.getOwnerNodeID())
    print "getType             = " + str(node.getType())
#

