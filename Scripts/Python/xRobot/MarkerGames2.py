# -*- coding: utf8 -*-

# ============ V 1 =============
import os
import sys
import time

#import yaml
import pickle

from Plasma import *
from PlasmaVaultConstants import *

# List of known borked game ids
#borkedGameIdList = [2630615]
# List of known borked game ids (updated 2019-07-20)
#borkedGameIdList = [2630615, 114361, 6430535, 6376815, 7962098, 7442358, 2706501, 7136536]
# Suppression temporaire des quetes "Super Sleuth"
"""
borkedGameIdList = [
    2630615, 
    114361, 6430535, 6376815, 7962098, 7442358, 2706501, 7136536, 
    3127780, 3188218, 3327082, 3205258
    ]
"""
# List of known borked game ids (updated 2021-09-25)
borkedGameIdList = [
    2630615, 
    114361, 6430535, 6376815, 
    7962098, 7442358, 
    2706501, 
    7136536, 
    3127780, 3188218, 3327082, 3205258,
    # 2021-09-25
    477912, 
    1925811, 
    4950303, 
    5359888, 
    5360256, 
    5360329, 
    5360487, 
    7256427, 
    7332018, 
    7413192, 
    7425176, 
    8594212, 
    8989468, 
    9026086, 
    9114149, 
    9805061, 
    10285296, 
    10440268, 
    10500194, 
    10502572, 
    10800192, 
    10801032, 
    ]

# Sauvegarde les quetes mise dans un dictionnaire dans un fichier (exple: games.yaml)
def SaveGamesDic(obj, fileName="games"):
    if not os.path.exists("Games"):
        os.makedirs("Games")
    #with open('Games/' + fileName + '.yaml', 'w') as f:
    #    yaml.dump(obj, f, default_flow_style=None, default_style='"')
    with open('Games/' + fileName + '.txt', 'wb') as f:
        pickle.dump(obj, f, 2)

# Charge les quetes d'un fichier (exple: games.yaml) dans un dictionnaire
def LoadGamesDic(fileName="games"):
    obj = None
    try:
        #with open('Games/' + fileName + '.yaml', 'r') as f:
        #    obj = yaml.load(f)
        with open('Games/' + fileName + '.txt', 'rb') as f:
            obj = pickle.load(f)
    except:
        #IOError
        obj = {}
    return obj

# Sauvegarde la liste des quetes dans un fichier 
def SaveGameList(gamesDic, fileName="BotGameList"):
    message = "List of markers games\n--------------------------------\n" #ecriture de la liste des marqueurs sur disque pour envoyer au joueur
    if not os.path.exists("Games"):
        os.makedirs("Games")
    if gamesDic is None or not isinstance(gamesDic, dict):
        gamesDic = LoadGamesDic()
    # dict => sorted list
    gameNameList = []
    for val in list(gamesDic.values()):
        gameNameList.append(val[0])
    gameNameList = sorted(gameNameList) # tri aphabetique des jeux
    for name in gameNameList:
        for key, val in list(gamesDic.items()):
            if val[0] == name:
                message += key + ": " + val[0] + " " + val[1] + "\n"
                break
    message += "To get a game, PM again SENDME folowed by the #id of the game"
    with open('Games/' + fileName + '.txt', 'w') as f:
        f.write(message)

## retourne le fichier liste des fichiers ( la methode qui appelle cette routine, envoie le texte sous forme d'un kimail. Voir module divers.py)
def LoadGameList(fileName="BotGameList"):
    message = ""
    with open('Games/' + fileName + '.txt','r') as f:
        message = f.read()
    return message

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
                                #gamesDic.update({strGameId: [game.getGameName(), modifyTime, game.getGameGuid()]})
                                gamesDic.update({strGameId: [game.getGameName(), modifyTime]})
                                nbNewGames += 1
                                #print "New game added : #{}, {}, {}, {}".format(strGameId, game.getGameName(), game.getModifyTime(), game.getGameGuid())
                                print("New game added : #{}, {}, {}".format(strGameId, game.getGameName(), game.getModifyTime()))
                            else:
                                print("The game #{0} is borked and not added.".format(strGameId))
            print("=> {0} new games added and {1} borked games removed.".format(nbNewGames, nbRemovedGames))
            if nbNewGames > 0 or nbRemovedGames > 0:
                SaveGamesDic(gamesDic)
                SaveGameList(gamesDic)
        else:
            print("inbox is not a folder node!")
    else:
        print("your vault indox was not found!")
    return gamesDic

# Recherche un jeu de marqueur par son ID
def GetGameByID(gameID):
    tempNode = ptVaultMarkerGameNode()
    tempNode.setID(gameID)

    try:
        node = ptVault().findNode(tempNode)
        if node.getType() == PtVaultNodeTypes.kMarkerGameNode:
            game = node.upcastToMarkerGameNode()
            print("GetGameByID : game found")
            return game
        else:
            print("GetGameByID : game not found")
            return None
    except:
        print("GetGameByID : ERROR")
        return None

# variable globale pour le test => faire une classe
#gamesDic = LoadGamesDic()

# Recupere une quete chargee dans gamesDic
def GetGameFromGamesDic(gamesDic, gameId=0):
    #global gamesDic
    #gamesDic = GetNewInboxGames()
    if gamesDic is None or not isinstance(gamesDic, dict):
        gamesDic = LoadGamesDic()
    strGameId = ""
    try:
        strGameId = str(int(gameId))
    except:
        print("Error in GetGameFromGamesDic: gameId must be an integer or a long")
        return None

    strGameId.lstrip("0")
    if strGameId in list(gamesDic.keys()):
        #gameGuid = gamesDic[strGameId][2]
        #game = GetGameByGuid(gameGuid)
        game = GetGameByID(int(strGameId))
        if game is not None:
            print("GetGameFromGamesDic: Game found => #{}".format(game.getID()))
            print("> Name:{}".format(game.getGameName()))
            #print "> CreateDate:{}".format(game.getCreateTime())
            tupTime = time.gmtime(game.getModifyTime())
            #formatTime = PtGetLocalizedString("Global.Formats.Date")
            formatTime = '%m/%d/%y'
            modifyTime = time.strftime(formatTime, tupTime)
            print("> ModifyDate:{}".format(modifyTime))
            #print "> Guid:{}".format(game.getGameGuid())
            print("> CreatorID:{}".format(game.getCreatorNodeID()))
            #print "> Age:{}".format(game.getCreateAgeName())
        else:
            print("GetGameFromGamesDic: Game #{} not found in the vault!".format(strGameId))
        return game
    else:
        print("Error in GetGameFromGamesDic: gameId {} not found".format(strGameId))
        return None

# variable globale pour le test
iNextGame = 0

# Test de recuperation de quete
def GetNextGame():
    global iNextGame
    gamesDic = GetNewInboxGames()
    iLastGame = len(list(gamesDic.keys())) - 1
    if iNextGame >= 0 and iNextGame <= iLastGame:
        gameId = list(gamesDic.keys())[iNextGame]
        game = GetGameFromGamesDic(gameId)
        iNextGame = iNextGame + 1
    else:
        print("no more games")

# Envoie une quete a un joueur
def SendGame(gameId, playerId=None):
    if playerId is None:
        playerId = PtGetLocalPlayer().getPlayerID()
    elif not isinstance(playerId, int) and not isinstance(playerId, int):
        print("Error in SendGame : playerId must be an integer")
        return [0, ""]
    gamesDic = GetNewInboxGames()
    game = GetGameFromGamesDic(gamesDic, gameId)
    if game is not None:
        # Envoyer la quete
        try:
            game.sendTo(playerId)
            msgGame = "{} ({})".format(game.getGameName(), time.strftime('%m/%d/%y', time.gmtime(game.getModifyTime())))
            print("SendGame : game #{} [{}] sent to #{}".format(game.getID(), msgGame, playerId))
            return [1, msgGame]
        except:
            print("SendGame : Error while sending game")
            return [0, "Error while sending game"]
    else:
        return [0, "Game not found"]

#
class Games:
    # declaration des variables pour le test
    iSendNextGame = 0
    gamesDic = {}
    
    #
    def __init__():
        iSendNextGame = 0
        gamesDic = GetNewInboxGames()
    
    # Test d'envoi de quete
    def SendNextGameTo(playerId):
        global iSendNextGame
        iLastGame = len(list(gamesDic.keys())) - 1
        if iSendNextGame >= 0 and iSendNextGame <= iLastGame:
            gameId = list(gamesDic.keys())[iSendNextGame]
            SendGame(gameId, playerId)
            iSendNextGame = iSendNextGame + 1
        else:
            print("no more games")

# Envoie la liste des quetes a un joueur
# Titre = "%s Markersgames"%(nomrobot)
def SendGameList(title, playerId=None):
    if playerId is None:
        playerId = PtGetLocalPlayer().getPlayerID()
    elif not isinstance(playerId, int) and not isinstance(playerId, int):
        print("Error in SendGameList : playerId must be an integer")
        return 0
    GetNewInboxGames()
    message = LoadGameList()
    # Envoyer le ki-mail
    try:
        note = ptVaultTextNoteNode(0)
        note.setText(message)
        note.setTitle(title) 
        note.sendTo(playerId)
        print("SendGameList : game list sent to #{}".format(playerId))
        return 1
    except:
        print("SendGameList : Error while sending game")
        return 0

#


"""
** Suppression d'une quete **
Dans ki.__ini__.py, ligne 6763:

    ## Process notifications originating from a YesNo dialog.
    # Yes/No dialogs are omnipresent throughout Uru. Those processed here are:
    # - Quitting dialog (quit/logout/cancel).
    # - Deleting dialog (yes/no); various such dialogs.
    # - Link offer dialog (yes/no).
    # - Outside sender dialog (?).
    # - KI Full dialog (OK); just a notification.
    def ProcessNotifyYesNo(self, control, event):

        if event == kAction or event == kValueChanged:
            ynID = control.getTagID()
            ...
            elif self.YNWhatReason == kGUI.YNDelete:
                if ynID == kGUI.YesButtonID:
                    # Remove the current element
                    if self.BKCurrentContent is not None:
                        delFolder = self.BKCurrentContent.getParent()
                        delElem = self.BKCurrentContent.getChild()
                        if delFolder is not None and delElem is not None:
                            ...
                            # See if this is a Marker Game folder that is being deleted.
                                if delElem.getType() == PtVaultNodeTypes.kMarkerGameNode:
                                    # Delete all markers from the Marker Manager display.
                                    mrkrDisplay = ptMarkerMgr()
                                    if not self.markerGameManager.gameLoaded():
                                        mrkrDisplay.removeAllMarkers()
                                    # Delete the game.
                                    if self.markerGameDisplay is None:
                                        PtDebugPrint(u"xKI.ProcessNotifyYesNo(): Cannot delete Marker Game as it is not loaded.", level=kErrorLevel)
                                        return
                                    self.markerGameDisplay.deleteGame()
                                    # Reset the game in case it was being played.
                                    if self.markerGameDisplay.gameData.data["svrGameTemplateID"] == self.markerGameManager.gameData.data["svrGameTemplateID"]:
                                        self.markerGameManager.deleteGame()

                                self.BKCurrentContent = None
                                delFolder.removeNode(delElem)
                                PtDebugPrint(u"xKI.ProcessNotifyYesNo(): Deleting element from folder.", level=kDebugDumpLevel)
                        else:
                            PtDebugPrint(u"xKI.ProcessNotifyYesNo(): Tried to delete bad Vault node or delete from bad folder.", level=kErrorLevel)
                        self.ChangeBigKIMode(kGUI.BKListMode)
                        self.RefreshPlayerList()
"""
"""
# test de suppression d'une quete presente dans Inbox
def DeleteGame(self, id):
    inbox = ptVault().getInbox()
    if inbox is not None:
        if inbox.getType() == PtVaultNodeTypes.kFolderNode:
            subs = inbox.getChildNodeRefList()
            for sub in subs:
                sub = sub.getChild()
                if sub.getType() == PtVaultNodeTypes.kMarkerGameNode:
                    game = sub.upcastToMarkerGameNode()
                    if game is not None:
                        if game.getID() == id:
                            # Delete all markers from the Marker Manager display.
                            mrkrDisplay = ptMarkerMgr()
                            if not self.markerGameManager.gameLoaded():
                                mrkrDisplay.removeAllMarkers()
                            # Delete the game.
                            if self.markerGameDisplay is None:
                                PtDebugPrint(u"xKI.ProcessNotifyYesNo(): Cannot delete Marker Game as it is not loaded.", level=kErrorLevel)
                                return
                            self.markerGameDisplay.deleteGame()
                            # Reset the game in case it was being played.
                            if self.markerGameDisplay.gameData.data["svrGameTemplateID"] == self.markerGameManager.gameData.data["svrGameTemplateID"]:
                                self.markerGameManager.deleteGame()

                        self.BKCurrentContent = None
                        delFolder.removeNode(delElem)
                        PtDebugPrint(u"xKI.ProcessNotifyYesNo(): Deleting element from folder.", level=kDebugDumpLevel)
"""

#