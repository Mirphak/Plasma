# -*- coding: utf-8 -*-

# ============ V 0 =============
import os
import sys
import time

#import yaml
import pickle

from Plasma import *
from PlasmaVaultConstants import *


# Get new games in my inbox folder
def GetNewInboxGames():
    gamesDic = LoadGamesDic()
    nbNewGames = 0
    nbRemovedGames = 0
    
    # Remove known borked games
    for gameId in borkedGameIdList:
        strGameId = str(gameId)
        if strGameId in list(gamesDic.keys()):
            del gamesDic[strGameId]
            nbRemovedGames += 1
            print("The borked game #{0} is removed.".format(strGameId))
    
    inbox = ptVault().getInbox()
    if inbox is not None:
        if inbox.getType() == PtVaultNodeTypes.kFolderNode:
            subs = inbox.getChildNodeRefList()
            for sub in subs:
                sub = sub.getChild()
                if sub.getType() == PtVaultNodeTypes.kMarkerGameNode:
                    game = sub.upcastToMarkerGameNode()
                    if game is not None:
                        strGameId = str(game.getID())
                        if strGameId not in list(gamesDic.keys()):
                            if game.getID() not in borkedGameIdList:
                                tupTime = time.gmtime(game.getModifyTime())
                                #formatTime = PtGetLocalizedString("Global.Formats.Date")
                                formatTime = '%m/%d/%y'
                                modifyTime = time.strftime(formatTime, tupTime)
                                gamesDic.update({strGameId: [game.getGameName(), modifyTime, game.getGameGuid()]})
                                nbNewGames += 1
                                print("New game added : #{}, {}, {}, {}".format(strGameId, game.getGameName(), game.getModifyTime(), game.getGameGuid()))
                            else:
                                print("The game #{0} is borked and not added.".format(strGameId))
                        """
                        else:
                            if game.getID() in borkedGameIdList:
                                del gamesDic[strGameId]
                                nbRemovedGames += 1
                                print "The borked game #{0} is removed.".format(strGameId)
                        """
            print("=> {0} new games added and {1} borked games removed.".format(nbNewGames, nbRemovedGames))
            if nbNewGames > 0 or nbRemovedGames > 0:
                SaveGamesDic(gamesDic)
                SaveGameList(gamesDic)
        else:
            print("inbox is not a folder node!")
    else:
        print("your vault indox was not found!")
    return gamesDic

# Get nodes in my inbox folder (images, notes, games)
def GetInboxNodes():
    nbGames = 0
    nbNotes = 0
    nbImages = 0
    gamesDic = {}
    notesDic = {}
    imagesDic = {}
    inbox = ptVault().getInbox()
    if inbox is not None:
        if inbox.getType() == PtVaultNodeTypes.kFolderNode:
            subs = inbox.getChildNodeRefList()
            for ref in subs:
                element = ref.getChild()
                # Marker games
                if element.getType() == PtVaultNodeTypes.kMarkerGameNode:
                    game = element.upcastToMarkerGameNode()
                    if game is not None:
                        strGameId = str(game.getID())
                        tupTime = time.gmtime(game.getModifyTime())
                        formatTime = '%m/%d/%y'
                        modifyTime = time.strftime(formatTime, tupTime)
                        gamesDic.update({strGameId: [game.getGameName(), modifyTime]})
                        nbGames += 1
                        print("Game infos : #{}, {}, {}, {}".format(strGameId, game.getGameName(), game.getModifyTime(), game.getCreatorNodeID()))
                # Text notes
                elif element.getType() == PtVaultNodeTypes.kTextNoteNode:
                    note = element.upcastToTextNoteNode()
                    if note is not None:
                        strNoteId = str(note.getID())
                        tupTime = time.gmtime(note.getModifyTime())
                        formatTime = '%m/%d/%y'
                        modifyTime = time.strftime(formatTime, tupTime)
                        notesDic.update({strNoteId: [note.getTitle(), modifyTime, note.getCreatorNodeID()]})
                        nbNotes += 1
                        print("Note infos : #{}, {}, {}, {}".format(strNoteId, note.getTitle(), note.getModifyTime(), note.getCreatorNodeID()))
                # Images
                elif element.getType() == PtVaultNodeTypes.kImageNode:
                    image = element.upcastToImageNode()
                    if image is not None:
                        strImageId = str(image.getID())
                        tupTime = time.gmtime(image.getModifyTime())
                        formatTime = '%m/%d/%y'
                        modifyTime = time.strftime(formatTime, tupTime)
                        notesDic.update({strImageId: [image.getTitle(), modifyTime, image.getCreatorNodeID()]})
                        nbImages += 1
                        print("Image infos : #{}, {}, {}, {}".format(strImageId, image.getTitle(), image.getModifyTime(), image.getCreatorNodeID()))
            print("=> {0} games found.".format(nbGames))
            print("=> {0} notes found.".format(nbNotes))
            print("=> {0} images found.".format(nbImages))
        else:
            print("My inbox is not a folder node!")
    else:
        print("My vault indox was not found!")
    return gamesDic, notesDic, imagesDic

# Remove all images from my Inbox folder
def RemoveAllImagesFromMyInbox():
    inbox = ptVault().getInbox()
    if inbox is not None:
        if inbox.getType() == PtVaultNodeTypes.kFolderNode:
            subs = inbox.getChildNodeRefList()
            for ref in subs:
                element = ref.getChild()
                if element.getType() == PtVaultNodeTypes.kImageNode:
                    inbox.removeNode(element)

# Remove all text notes from my Inbox folder
def RemoveAllTextNotesFromMyInbox():
    inbox = ptVault().getInbox()
    if inbox is not None:
        if inbox.getType() == PtVaultNodeTypes.kFolderNode:
            subs = inbox.getChildNodeRefList()
            for ref in subs:
                element = ref.getChild()
                if element.getType() == PtVaultNodeTypes.kTextNoteNode:
                    inbox.removeNode(element)

#
"""
        self.BKContentList = []
self.BKContentList = folder.getChildNodeRefList()
                ref = self.BKContentList[idx]
                if ref is not None:
                            # Remove from inbox (how will this work?).
                            element = ref.getChild()
                            inbox.removeNode(element)
"""
