# -*- coding: utf-8 -*-
from Plasma import *
import time
import os
import csv

"""
    ptVault().getBuddyListFolder() : Returns a ptVaultPlayerInfoListNode of the current player's buddy list folder.


class ptVaultPlayerInfoListNode(ptVaultFolderNode):
    #Plasma vault player info list node#
    def __init__(self,n=0):
        #None#
        pass

    def addNode(self,node,cb=None,cbContext=0):
        #Adds 'node'(ptVaultNode) as a child to this node.#
        pass

    def addPlayer(self,playerID):
        #Adds playerID player to this player info list node.#
        pass

    def findNode(self,templateNode):
        #Returns ptVaultNode if child node found matching template, or None#
        pass

    def folderGetName(self):
        #LEGACY
Returns the folder's name#
        pass

    def folderGetType(self):
        #LEGACY
Returns the folder type (of the standard folder types)#
        pass

    def folderSetName(self,name):
        #LEGACY
Set the folder name#
        pass

    def folderSetType(self,type):
        #LEGACY
Set the folder type#
        pass

    def getChildNodeCount(self):
        #Returns how many children this node has.#
        pass

    def getChildNodeRefList(self):
        #Returns a list of ptVaultNodeRef that are the children of this node.#
        pass

    def getClientID(self):
        #Returns the client's ID.#
        pass

    def getCreateAgeCoords(self):
        #Returns the location in the Age where this node was created.#
        pass

    def getCreateAgeGuid(self):
        #Returns the guid as a string of the Age where this node was created.#
        pass

    def getCreateAgeName(self):
        #Returns the name of the Age where this node was created.#
        pass

    def getCreateAgeTime(self):
        #Returns the time in the Age that the node was created...(?)#
        pass

    def getCreateTime(self):
        #Returns the when this node was created, that is useable by python's time library.#
        pass

    def getCreatorNode(self):
        #Returns the creator's node#
        pass

    def getCreatorNodeID(self):
        #Returns the creator's node ID#
        pass

    def getFolderName(self):
        #Returns the folder's name#
        pass

    def getFolderNameW(self):
        #Unicode version of getFolerName#
        pass

    def getFolderType(self):
        #Returns the folder type (of the standard folder types)#
        pass

    def getID(self):
        #Returns the unique ID of this ptVaultNode.#
        pass

    def getModifyTime(self):
        #Returns the modified time of this node, that is useable by python's time library.#
        pass

    def getNode(self,id):
        #Returns ptVaultNodeRef if is a child node, or None#
        pass

    def getOwnerNode(self):
        #Returns a ptVaultNode of the owner of this node#
        pass

    def getOwnerNodeID(self):
        #Returns the node ID of the owner of this node#
        pass

    def getPlayer(self,playerID):
        #Gets the player info node for the specified player.#
        pass

    def getType(self):
        #Returns the type of ptVaultNode this is.
See PlasmaVaultTypes.py#
        pass

    def hasNode(self,id):
        #Returns true if node if a child node#
        pass

    def hasPlayer(self,playerID):
        #Returns whether the 'playerID' is a member of this player info list node.#
        pass

    def linkToNode(self,nodeID,cb=None,cbContext=0):
        #Adds a link to the node designated by nodeID#
        pass

    def playerlistAddPlayer(self,playerID):
        #LEGACY: Adds playerID player to this player info list node.#
        pass

    def playerlistGetPlayer(self,playerID):
        #LEGACY: Gets the player info node for the specified player.#
        pass

    def playerlistHasPlayer(self,playerID):
        #LEGACY: Returns whether the 'playerID' is a member of this player info list node.#
        pass

    def playerlistRemovePlayer(self,playerID):
        #LEGACY: Removes playerID player from this player info list node.#
        pass

    def removeAllNodes(self):
        #Removes all the child nodes on this node.#
        pass

    def removeNode(self,node,cb=None,cbContext=0):
        #Removes the child 'node'(ptVaultNode) from this node.#
        pass

    def removePlayer(self,playerID):
        #Removes playerID player from this player info list node.#
        pass

    def save(self,cb=None,cbContext=0):
        #Save the changes made to this node.#
        pass

    def saveAll(self,cb=None,cbContext=0):
        #Saves this node and all its children nodes.#
        pass

    def sendTo(self,destID,cb=None,cbContext=0):
        #Send this node to inbox at 'destID'#
        pass

    def setCreateAgeGuid(self,guid):
        #Set guid as a string of the Age where this node was created.#
        pass

    def setCreateAgeName(self,name):
        #Set name of the Age where this node was created.#
        pass

    def setCreatorNodeID(self,id):
        #Set creator's node ID#
        pass

    def setFolderName(self,name):
        #Set the folder name#
        pass

    def setFolderNameW(self,name):
        #Unicode version of setFolderName#
        pass

    def setFolderType(self,type):
        #Set the folder type#
        pass

    def setID(self,id):
        #Sets ID of this ptVaultNode.#
        pass

    def setOwnerNodeID(self,id):
        #Set node ID of the owner of this node#
        pass

    def setType(self,type):
        #Set the type of ptVaultNode this is.#
        pass

    def sort(self):
        #Sorts the player list by some means...?#
        pass

    def upcastToAgeInfoListNode(self):
        #Returns this ptVaultNode as ptVaultAgeInfoListNode#
        pass

    def upcastToAgeInfoNode(self):
        #Returns this ptVaultNode as ptVaultAgeInfoNode#
        pass

    def upcastToAgeLinkNode(self):
        #Returns this ptVaultNode as ptVaultAgeLinkNode#
        pass

    def upcastToChronicleNode(self):
        #Returns this ptVaultNode as ptVaultChronicleNode#
        pass

    def upcastToFolderNode(self):
        #Returns this ptVaultNode as ptVaultFolderNode#
        pass

    def upcastToImageNode(self):
        #Returns this ptVaultNode as ptVaultImageNode#
        pass

    def upcastToMarkerGameNode(self):
        #Returns this ptVaultNode as ptVaultMarkerNode#
        pass

    def upcastToPlayerInfoListNode(self):
        #Returns this ptVaultNode as ptVaultPlayerInfoListNode#
        pass

    def upcastToPlayerInfoNode(self):
        #Returns this ptVaultNode as ptVaultPlayerInfoNode#
        pass

    def upcastToPlayerNode(self):
        #Returns this ptVaultNode as a ptVaultPlayerNode#
        pass

    def upcastToSDLNode(self):
        #Returns this ptVaultNode as a ptVaultSDLNode#
        pass

    def upcastToSystemNode(self):
        #Returns this ptVaultNode as a ptVaultSystemNode#
        pass

    def upcastToTextNoteNode(self):
        #Returns this ptVaultNode as ptVaultTextNoteNode#
        pass

"""

# Add player in buddies folder (from xPlayers)
def AddBud(idplayer):
    vault = ptVault()
    buddies = vault.getBuddyListFolder()
    try:
        localPlayer = PtGetLocalPlayer()
        if idplayer != localPlayer.getPlayerID():
            if not buddies.playerlistHasPlayer(idplayer):
                buddies.playerlistAddPlayer(idplayer)
                return True
    except:
        return False

# Get buddies (from xPlayerKiCmds)
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
        selPlyrList = filter(lambda pl: not(pl.getPlayerID() in xPlayers.dicBot.keys()), selPlyrList)
    return selPlyrList

# Get buddy list
def GetBuddyList():
    vault = ptVault()
    if not isinstance(vault, ptVault):
        print "vault not found!"
        return None
    buddiesFolder = vault.getBuddyListFolder()
    if not isinstance(buddiesFolder, ptVaultPlayerInfoListNode):
        print "buddiesFolder not found!"
        return None
    lst = []
    for buddyVaultNodeRef in buddiesFolder.getChildNodeRefList():
        if not isinstance(buddyVaultNodeRef, ptVaultNodeRef):
            print "buddyVaultNodeRef not found!"
            return None
        buddyVaultNode = buddyVaultNodeRef.getChild()
        if not isinstance(buddyVaultNode, ptVaultNode):
            print "buddyVaultNode not found!"
            return None
        # On peut deja recuperer la date de creation du noeud ici
        #buddyVaultNode.getCreateTime()
        
        buddyPlayerInfoNode = buddyVaultNode.upcastToPlayerInfoNode()
        if not isinstance(buddyPlayerInfoNode, ptVaultPlayerInfoNode):
            print "buddyVaultNode not found!"
            return None
        # On peut recuperer les infos du joueur ici
        playerId = buddyPlayerInfoNode.playerGetID()
        playerName = buddyPlayerInfoNode.playerGetName()
        playerCcrLevel = buddyPlayerInfoNode.playerGetCCRLevel()
        playerAgeGuid = buddyPlayerInfoNode.playerGetAgeGuid()
        playerAgeInstanceName = buddyPlayerInfoNode.playerGetAgeInstanceName()
        playerIsOnline = buddyPlayerInfoNode.playerIsOnline()
        #createTime = buddyPlayerInfoNode.getCreateTime()
        #tupTime = time.gmtime(PtGMTtoDniTime(buddyPlayerInfoNode.getModifyTime()))
        #curTime = time.strftime(PtGetLocalizedString("Global.Formats.Date"), tupTime)
        tupTime = time.gmtime(buddyPlayerInfoNode.getModifyTime())
        curTime = time.strftime("%Y-%m-%d %H:%M:%S", tupTime)
        
        lst.append([curTime, playerId, playerName, playerCcrLevel, playerIsOnline, playerAgeGuid, playerAgeInstanceName])
        
        # Pas tres utile
        #player = ptPlayer(buddyPlayerInfoNode.playerGetName(), buddyPlayerInfoNode.playerGetID())
    return lst

#
def SaveBuddyList():
    if not os.path.exists("Buddies"):
        os.makedirs("Buddies")
    now = time.strftime("%Y-%m-%d_%H-%M-%S")
    me = PtGetLocalPlayer()
    #myName = me.getPlayerName()
    myId = me.getPlayerID()
    fileName = "{0}_{1}".format(myId, now)
    with open('Buddies/' + fileName + '.csv', 'wb') as f:
        #yaml.dump(obj, f, default_flow_style=None, default_style='"')
        wr = csv.writer(f, quoting=csv.QUOTE_ALL)
        #for bud in GetBuddyList():
        #    wr.writerow(bud)
        #wr.writeheader()
        wr.writerows(GetBuddyList())

# Write buddy KI list
def SaveBuddyKiList():
    vault = ptVault()
    if not isinstance(vault, ptVault):
        print "vault not found!"
        return 0
    buddiesFolder = vault.getBuddyListFolder()
    if not isinstance(buddiesFolder, ptVaultPlayerInfoListNode):
        print "buddiesFolder not found!"
        return 0
    if not os.path.exists("Buddies"):
        os.makedirs("Buddies")
    now = time.strftime("%Y-%m-%d")
    fileName = "Buddies/KI_{0}.txt".format(now)
    i = 0
    with open(fileName, 'w') as f:
        for buddyVaultNodeRef in buddiesFolder.getChildNodeRefList():
            if not isinstance(buddyVaultNodeRef, ptVaultNodeRef):
                print "buddyVaultNodeRef not found!"
                continue
            buddyVaultNode = buddyVaultNodeRef.getChild()
            if not isinstance(buddyVaultNode, ptVaultNode):
                print "buddyVaultNode not found!"
                continue
            buddyPlayerInfoNode = buddyVaultNode.upcastToPlayerInfoNode()
            if not isinstance(buddyPlayerInfoNode, ptVaultPlayerInfoNode):
                print "buddyVaultNode not found!"
                continue
            playerId = buddyPlayerInfoNode.playerGetID()
            f.write("{0}\n".format(playerId))
            i += 1
    return i

#


#

