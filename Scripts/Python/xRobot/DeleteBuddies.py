# -*- coding: utf-8 -*-

#Import du module Plasma
from Plasma import *

# Remove a player in my buddies list
def RemoveBud(idplayer):
    vault = ptVault()
    buddies = vault.getBuddyListFolder()
    try:
        localPlayer = PtGetLocalPlayer()
        if idplayer != localPlayer.getPlayerID():
            if buddies.playerlistHasPlayer(idplayer):
                buddies.playerlistRemovePlayer(idplayer)
                return True
    except:
        return False

# Get buddies id list (voir Buddies.py)

# Get buddy list
def GetBuddyList():
    vault = ptVault()
    if not isinstance(vault, ptVault):
        print("vault not found!")
        return None
    buddiesFolder = vault.getBuddyListFolder()
    if not isinstance(buddiesFolder, ptVaultPlayerInfoListNode):
        print("buddiesFolder not found!")
        return None
    lst = []
    for buddyVaultNodeRef in buddiesFolder.getChildNodeRefList():
        if not isinstance(buddyVaultNodeRef, ptVaultNodeRef):
            print("buddyVaultNodeRef not found!")
            return None
        buddyVaultNode = buddyVaultNodeRef.getChild()
        if not isinstance(buddyVaultNode, ptVaultNode):
            print("buddyVaultNode not found!")
            return None
        # On peut deja recuperer la date de creation du noeud ici
        #buddyVaultNode.getCreateTime()
        
        buddyPlayerInfoNode = buddyVaultNode.upcastToPlayerInfoNode()
        if not isinstance(buddyPlayerInfoNode, ptVaultPlayerInfoNode):
            print("buddyVaultNode not found!")
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

# Get buddy KI list
def GetBuddyKiList():
    vault = ptVault()
    if not isinstance(vault, ptVault):
        print("vault not found!")
        return None
    buddiesFolder = vault.getBuddyListFolder()
    if not isinstance(buddiesFolder, ptVaultPlayerInfoListNode):
        print("buddiesFolder not found!")
        return None
    lst = []
    for buddyVaultNodeRef in buddiesFolder.getChildNodeRefList():
        if not isinstance(buddyVaultNodeRef, ptVaultNodeRef):
            print("buddyVaultNodeRef not found!")
            return None
        buddyVaultNode = buddyVaultNodeRef.getChild()
        if not isinstance(buddyVaultNode, ptVaultNode):
            print("buddyVaultNode not found!")
            return None
        
        buddyPlayerInfoNode = buddyVaultNode.upcastToPlayerInfoNode()
        if not isinstance(buddyPlayerInfoNode, ptVaultPlayerInfoNode):
            print("buddyVaultNode not found!")
            return None
        # On peut recuperer les infos du joueur ici
        playerId = buddyPlayerInfoNode.playerGetID()
        
        lst.append(playerId)
    return lst

# Remove all player in my buddies list
def RemoveAllBuddies():
    vault = ptVault()
    buddies = vault.getBuddyListFolder()
    try:
        lst = GetBuddyKiList()
        for idplayer in lst:
            #print "removing buddy : {}".format(idplayer)
            if buddies.playerlistHasPlayer(idplayer):
                buddies.playerlistRemovePlayer(idplayer)
                #print "RemoveAllBuddies : buddy is removed : {}".format(idplayer)
                #return True
    except:
        print("RemoveAllBuddies : Error")
        #return False

#

"""
    ## xKIChat : Remove a player from this player's buddies.
    def RemoveBuddy(self, player):

        pID = self.GetPID(player)
        vault = ptVault()
        buddies = vault.getBuddyListFolder()
        if buddies is None:
            return

        # Is it a number?
        if pID:
            if buddies.playerlistHasPlayer(pID):
                buddies.playerlistRemovePlayer(pID)
                self.chatMgr.DisplayStatusMessage(PtGetLocalizedString("KI.Player.Removed"))
            else:
                self.chatMgr.AddChatLine(None, PtGetLocalizedString("KI.Player.NotFound"), kChat.SystemMessage)
        # Or is it a username?
        else:
            buddyRefs = buddies.getChildNodeRefList()
            for plyr in buddyRefs:
                if isinstance(plyr, ptVaultNodeRef):
                    PLR = plyr.getChild()
                    PLR = PLR.upcastToPlayerInfoNode()
                    if PLR is not None and PLR.getType() == PtVaultNodeTypes.kPlayerInfoNode:
                        if player == PLR.playerGetName():
                            buddies.playerlistRemovePlayer(PLR.playerGetID())
                            self.chatMgr.DisplayStatusMessage(PtGetLocalizedString("KI.Player.Removed"))
                            return
            self.chatMgr.AddChatLine(None, PtGetLocalizedString("KI.Player.NumberOnly"), kChat.SystemMessage)
"""