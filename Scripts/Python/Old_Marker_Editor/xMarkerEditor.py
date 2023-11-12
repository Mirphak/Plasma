# -*- coding: utf-8 -*-
# xMarkerEditor
# Handles all the marker editing stuff.


from Plasma import *
from PlasmaGame import *
from PlasmaGameConstants import *
from PlasmaKITypes import *
from PlasmaVaultConstants import *

import os
import yaml
import codecs
###import unicodedata ### ce module n'exite pas!!

kCharSet = "cp1252"

def GetEditor():

    editor = {
        "client" : None, 
        "downloading" : False, 
        "downloading_id" : None,
        "uploading" : False,
        "uploadedGame" : False,
        "uploadedGamesMarkers" : 0,
        "uploadedGamesMarkersTotal" : 0,
        "node" : None,
        "game" : {
            "name" : None, 
            "guid" : None,
            "creatorID" : None, 
            "creator" : None, 
            "markers" : []
        }
    }
    return editor

#
#def ListGames(self):
def ListGames_1(self):
    if not os.path.exists("Games"):
        os.makedirs("Games")
    sPlayerID = str(PtGetLocalPlayer().getPlayerID())
    file = open("Games/List_" + sPlayerID + ".csv", "w")
    #file = codecs.open("Games/List_" + sPlayerID + ".csv", "w", "utf8")
    file.write("List of marker games\n--------------------")
    file.write("\n\"#\";\"Game Id\";\"Creator Id\";\"Game Name\";\"Folder Name\"")
    for id, game in enumerate(GetList()):
        #file.write("\n" + str(id) + ": " + game.getGameName() + "")
        #file.write("\n" + str(id) + ": \"" + str(game.getID()) + "\"\t\"" + game.getGameName() + "\"")
        #file.write("\n" + str(id) + ";\"" + str(game.getID()) + "\";\"" + str(game.getCreatorNodeID()) + "\";\"" + game.getGameName() + "\";\"" + game.getCreateAgeName() + "\"")
        #file.write("\n" + str(id) + ";\"" + str(game[0].getID()) + "\";\"" + str(game[0].getCreatorNodeID()) + "\";\"" + game[0].getGameName() + "\";\"" + game[1] + "\"")
        try:
            file.write("\n" + str(id) + ";\"" + str(game[0].getID()) + "\";\"" + str(game[0].getCreatorNodeID()) + "\";\"" + game[0].getGameName() + "\";\"" + game[1] + "\"")
        except UnicodeDecodeError:
            gameName = "".join([x if ord(x) < 128 else '?' for x in game[0].getGameName()])
            self.chatMgr.DisplayStatusMessage("There is a non ascii character in the name of this game! (game id:{0}, game name: \"{1}\")".format(self.editor["downloading_id"], gameName))
            file.write("\n" + str(id) + ";\"" + str(game[0].getID()) + "\";\"" + str(game[0].getCreatorNodeID()) + "\";\"" + gameName + "\";\"" + game[1] + "\"")
    file.close()
    self.chatMgr.DisplayStatusMessage("A list of your games has been saved in \"Games/List_" + sPlayerID + ".csv\".")

#
def GetGameByGuid(gameGuid):
    tempNode = ptVaultMarkerGameNode()
    tempNode.setGameGuid(gameGuid)

    try:
        node = ptVault().findNode(tempNode)
        if node.getType() == PtVaultNodeTypes.kMarkerGameNode:
            game = node.upcastToMarkerGameNode()
            return game
        else:
            return None
    except:
        return None

#
#def ListGames2(self):
def ListGames(self):
    if not os.path.exists("Games"):
        os.makedirs("Games")
    sPlayerID = str(PtGetLocalPlayer().getPlayerID())
    file = open("Games/List_" + sPlayerID + ".csv", "w")
    file.write("List of marker games\n--------------------")
    file.write("\n#;Game Id;Creator Id;Game Guid;Folder Name;State;Game Name")
    for id, game in enumerate(GetList()):
        line = "\n" + str(id) 
        line += ";" + str(game[0].getID()) 
        line += ";" + str(game[0].getCreatorNodeID()) 
        line += ";" + str(game[0].getGameGuid())
        line += ";" + game[1]
        """ *** TEST *** """
        # Determine which mode we're in.
        if self.markerGameManager.gameLoaded():
            # A game is in progress, restrict access.
            if self.markerGameManager.gameData.data["svrGameTemplateID"] == self.editor["game"]["guid"]:
                fline += ";" + "Playing"
            else:
                line += ";" + "Overview"
        else:
            line += ";"
        try:
            line += ";" + game[0].getGameName() 
            file.write(line)
        except UnicodeDecodeError:
            gameName = "".join([x if ord(x) < 128 else '?' for x in game[0].getGameName()])
            line += ";" + gameName
            self.chatMgr.DisplayStatusMessage("There is a non ascii character in the name of this game! (game id:{0}, game name: \"{1}\")".format(self.editor["downloading_id"], gameName))
            file.write(line)
    file.close()
    self.chatMgr.DisplayStatusMessage("A list of your games has been saved in \"Games/List_" + sPlayerID + ".csv\".")

#
def GetCreatorName(creatorID):
    #creatorID = game.getCreatorNodeID()
    #creatorID = element.getCreatorNodeID()
    tempNode = ptVaultPlayerInfoNode()
    tempNode.playerSetID(creatorID)

    try:
        vault = ptVault()
        creatorName = vault.findNode(tempNode).upcastToPlayerInfoNode().playerGetName()
        if creatorName is None:
            creatorName = ""
    except:
        creatorName = ""
    return creatorName

#
def DownloadGame(self, gameID):

    games = GetList()
    if not os.path.exists("Games"):
        os.makedirs("Games")
    try:
        game = games[gameID][0]
        creatorID = game.getCreatorNodeID()
        guid = game.getGameGuid()
        gameName = "".join([x if ord(x) < 128 else '?' for x in game.getGameName()])
        self.editor["downloading"] = True
        self.editor["downloading_id"] = game.getID()
        #self.editor["game"]["name"] = unicode(game.getGameName(), kCharSet)
        self.editor["game"]["name"] = gameName
        self.editor["game"]["guid"] = guid
        self.editor["game"]["creatorID"] = str(creatorID) 
        self.editor["game"]["creator"] = GetCreatorName(creatorID) 
        PtCreateMarkerGame(self.key, PtMarkerGameTypes.kMarkerGameQuest, templateId = guid)
        filename = ""

        for c in self.editor["game"]["creator"]:
            if c.isalnum():
                filename += c
        filename += "_" + str(game.getID())
        self.chatMgr.DisplayStatusMessage("Your game #" + str(gameID) + " has been downloaded as \"Games/" + filename + ".txt\"")
    except UnicodeEncodeError:
        self.chatMgr.DisplayStatusMessage("There is wrong character in this game (#{}).".format(gameID))
    except IndexError:
        self.chatMgr.DisplayStatusMessage("There is no such marker game (#{}).".format(gameID))

#
def GetList():

    games = []
    journals = ptVault().getAgeJournalsFolder()
    agefolderRefs = journals.getChildNodeRefList()
    for agefolderRef in agefolderRefs:
        agefolder = agefolderRef.getChild()
        if agefolder.getType() == PtVaultNodeTypes.kFolderNode:
            agefolder = agefolder.upcastToFolderNode()
            ageFolderName = agefolder.getFolderName()
            subs = agefolder.getChildNodeRefList()
            for sub in subs:
                sub = sub.getChild()
                if sub.getType() == PtVaultNodeTypes.kMarkerGameNode:
                    game = sub.upcastToMarkerGameNode()
                    games.append([game, ageFolderName])
    #return games
    #Add games from Inbox folder
    inbox = ptVault().getInbox()
    if inbox.getType() == PtVaultNodeTypes.kFolderNode:
        subs = inbox.getChildNodeRefList()
        #id = 0
        for sub in subs:
            sub = sub.getChild()
            if sub.getType() == PtVaultNodeTypes.kMarkerGameNode:
                game = sub.upcastToMarkerGameNode()
                games.append([game, "Inbox"])
    return games

def UploadGame(self, gameFileName):

    if not os.path.exists("Games"):
        os.makedirs("Games")
    try:
        file = open("Games/" + gameFileName, "r")
        content = file.read()
        file.close()
        try:
            self.editor["game"] = yaml.load(content)
            try:
                guid = self.editor["game"]["guid"]
                valid = False
                for game in GetList():
                    game = game[0]
                    if game.getGameGuid() == guid:
                        valid = True
                        self.editor["node"] = game
                if not valid:
                    self.chatMgr.DisplayStatusMessage("Invalid GUID.")
                    return
                # We are editing an existing game.
                self.chatMgr.DisplayStatusMessage("GUID found ==> This is an existing game.")
                try:
                    if not isinstance(self.editor["game"]["markers"], list):
                        self.chatMgr.DisplayStatusMessage("The file is not a valid Marker Game file: invalid parameters.")
                        return
                    for marker in self.editor["game"]["markers"]:
                        try:
                            if not isinstance(marker["text"], str):
                                try:
                                    self.chatMgr.DisplayStatusMessage("Marker : text='{}'".format(marker["text"]))
                                except:
                                    self.chatMgr.DisplayStatusMessage("I can't read the marker text!")
                            if not isinstance(marker["age"], str):
                                try:
                                    self.chatMgr.DisplayStatusMessage("Marker : age='{}'".format(marker["age"]))
                                except:
                                    self.chatMgr.DisplayStatusMessage("I can't read the marker age!")
                            if not isinstance(marker["coords"], list) or len(marker["coords"]) != 3:
                                try:
                                    self.chatMgr.DisplayStatusMessage("Marker : coords={}".format(marker["coords"]))
                                except:
                                    self.chatMgr.DisplayStatusMessage("I can't read the marker coords!")
                            if not isinstance(marker["text"], str) or not isinstance(marker["age"], str) or not isinstance(marker["coords"], list) or len(marker["coords"]) != 3:
                                self.chatMgr.DisplayStatusMessage("The file is not a valid Marker Game file: incorrect markers.")
                                return
                            for coord in marker["coords"]:
                                if not isinstance(coord, float) and not isinstance(coord, int):
                                    self.chatMgr.DisplayStatusMessage("The file is not a valid Marker Game file: incorrect marker coordinates.")
                                    return
                        except KeyError:
                            self.chatMgr.DisplayStatusMessage("The file is not a valid Marker Game file: incorrect markers.")
                            return
                        if len(marker["text"]) >= 128:
                            self.chatMgr.DisplayStatusMessage("The file is not a valid Marker Game file: marker description too long.")
                            return
                except KeyError:
                    self.chatMgr.DisplayStatusMessage("The file is not a valid Marker Game file: missing parameters.")
                    return
                try:
                    if len(self.editor["game"]["name"]) >= 128:
                        self.chatMgr.DisplayStatusMessage("The file is not a valid Marker Game file: name too long.")
                        return
                except KeyError:
                    pass
                self.editor["uploading"] = True
                PtCreateMarkerGame(self.key, PtMarkerGameTypes.kMarkerGameQuest, self.editor["game"]["name"], templateId = guid)
            except KeyError:
                # We are creating a new game.
                try:
                    self.chatMgr.DisplayStatusMessage("No GUID ==> This is a new game.")
                    if not isinstance(self.editor["game"]["name"], str):
                        self.chatMgr.DisplayStatusMessage("> error in name.{}".format(self.editor["game"]["name"]))
                    if not isinstance(self.editor["game"]["markers"], list):
                        self.chatMgr.DisplayStatusMessage("> error in markers.{}".format(self.editor["game"]["markers"]).getType())
                    if not isinstance(self.editor["game"]["creator"], str):
                        self.chatMgr.DisplayStatusMessage("> error in creator.{}".format(self.editor["game"]["creator"]))
                    if not isinstance(self.editor["game"]["name"], str) or not isinstance(self.editor["game"]["markers"], list) or not isinstance(self.editor["game"]["creator"], str):
                        self.chatMgr.DisplayStatusMessage("The file is not a valid Marker Game file: invalid parameters.")
                        return
                    for marker in self.editor["game"]["markers"]:
                        try:
                            if not isinstance(marker["text"], str) or not isinstance(marker["age"], str) or not isinstance(marker["coords"], list) or len(marker["coords"]) != 3:
                                self.chatMgr.DisplayStatusMessage("The file is not a valid Marker Game file: incorrect markers.")
                                return
                            for coord in marker["coords"]:
                                if not isinstance(coord, float) and not isinstance(coord, int):
                                    self.chatMgr.DisplayStatusMessage("The file is not a valid Marker Game file: incorrect marker coordinates.")
                                    return
                        except KeyError:
                            self.chatMgr.DisplayStatusMessage("The file is not a valid Marker Game file: incorrect markers.")
                            return
                        if len(marker["text"]) >= 128:
                            self.chatMgr.DisplayStatusMessage("The file is not a valid Marker Game file: marker description too long.")
                            return
                except KeyError:
                    self.chatMgr.DisplayStatusMessage("The file is not a valid Marker Game file: missing parameters.")
                    return
                if len(self.editor["game"]["name"]) >= 128:
                    self.chatMgr.DisplayStatusMessage("The file is not a valid Marker Game file: name too long.")
                    return
                self.editor["uploading"] = True
                PtCreateMarkerGame(self.key, PtMarkerGameTypes.kMarkerGameQuest, self.editor["game"]["name"])
        except ValueError:
            self.chatMgr.DisplayStatusMessage("The file is not a valid Marker Game file: incorrect format.")
            return   
    except IOError:
        self.chatMgr.DisplayStatusMessage("Could not open file.")
        return

#
def DownloadGame2(self, game, gameID):
    if not os.path.exists("Games"):
        os.makedirs("Games")
    try:
        creatorID = game.getCreatorNodeID()
        creatorName = GetCreatorName(creatorID)
        creatorNameA = ""
        """
        if creatorID is not None and creatorID > 0:
            #for c in PtGetAvatarKeyFromClientID(creatorID).getPlayerName():
            for c in creatorName:
                if c.isalnum():
                    creatorNameA += c
        """
        for c in creatorName:
            if c.isalnum():
                creatorNameA += c


        guid = game.getGameGuid()
        gameName = "".join([x if ord(x) < 128 else '?' for x in game.getGameName()])
        ageName = game.getCreateAgeName()
        self.editor["downloading"] = True
        self.editor["downloading_id"] = game.getID()
        #self.editor["game"]["name"] = unicode(game.getGameName(), kCharSet)
        self.editor["game"]["name"] = gameName
        self.editor["game"]["guid"] = guid
        self.editor["game"]["creatorID"] = str(creatorID) 
        #self.editor["game"]["creator"] = creatorName 
        self.editor["game"]["creator"] = creatorNameA 
        PtCreateMarkerGame(self.key, PtMarkerGameTypes.kMarkerGameQuest, templateId = guid)
        """
        foldername = str(creatorID) + "_"
        for c in self.editor["game"]["creator"]:
            if c.isalnum():
                foldername += c
        """
        foldername = str(creatorID) + "_" + creatorNameA

        filename = str(game.getID()) + "_"
        for c in self.editor["game"]["name"]:
            if c.isalnum():
                filename += c
        
        if not os.path.exists("Games/" + foldername):
            os.makedirs("Games/" + foldername)

        self.chatMgr.DisplayStatusMessage("Your game #" + str(gameID) + " has been downloaded as \"Games/" + foldername + "/" + filename + ".txt\"")
    except UnicodeEncodeError:
        self.chatMgr.DisplayStatusMessage("There is wrong character in this game (#{}).".format(gameID))
    except IndexError:
        self.chatMgr.DisplayStatusMessage("There is no such marker game (#{}).".format(gameID))

# Classe pour gerer attente entre les telechargements
class DownloadGames():
    running = False
    games = []
    delay = 1
    gameID = 0
    KIchatMgr = None
    folderName = None
    waiting = 0
    
    #
    def __init__(self):
        pass
    
    #
    def onAlarm(self, param):
        if not self.running:
            return
        if self.KIchatMgr.editor["downloading"] == True:
            self.waiting += 1
            self.KIchatMgr.chatMgr.DisplayStatusMessage("... Still downloading game (#{}) {}s ...".format(self.gameID, self.waiting))
            if self.waiting < 60:
                PtSetAlarm(self.delay, self, 1)
            else:
                self.KIchatMgr.chatMgr.DisplayStatusMessage("... Unable to complete downloading the game (#{})!".format(self.gameID))
                #cancel
                self.KIchatMgr.editor["downloading"] == False
                #try the next one
                self.gameID += 1
        else:
            if self.gameID < len(self.games):
                if self.folderName == None or self.games[self.gameID][1] == self.folderName:
                    game = self.games[self.gameID][0]
                    DownloadGame2(self.KIchatMgr, game, self.gameID)
                PtSetAlarm(self.delay, self, 1)
                self.gameID += 1
            else:
                self.running = False

    # Starts downloading
    def Start(self, KIchatMgr, folderName=None, delay=None):
        self.games = GetList()
        self.KIchatMgr = KIchatMgr
        if folderName:
            self.folderName = folderName
        if delay:
            self.delay = delay
        if not self.running:
            self.KIchatMgr.chatMgr.DisplayStatusMessage("Start downloading {} games ...".format(len(self.games)))
            self.running = True
            self.gameID = 0
            self.onAlarm(1)

    def Stop(self):
        self.running = False
        if self.KIchatMgr is not None:
            self.KIchatMgr.chatMgr.DisplayStatusMessage("Stop downloading games.")

# init : get an instance of the DownloadGames class
downloadGames = DownloadGames()

#
def StartDownloadAllGames(self, folderName=None):
    downloadGames.Start(self, folderName, 2)

#
def StopDownloadAllGames(self):
    downloadGames.Stop(self)

#