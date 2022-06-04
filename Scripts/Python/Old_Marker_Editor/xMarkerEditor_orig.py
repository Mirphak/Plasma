# xMarkerEditor
# Handles all the marker editing stuff.


from Plasma import *
from PlasmaGame import *
from PlasmaGameConstants import *
from PlasmaKITypes import *
from PlasmaVaultConstants import *

import os
import yaml

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
            "creator" : None, 
            "markers" : []
        }
    }
    return editor

def ListGames(self):

    if not os.path.exists("Games"):
        os.makedirs("Games")
    file = open("Games/List.txt", "w")
    file.write("List of marker games\n--------------------")
    for id, game in enumerate(GetList()):
        file.write("\n" + str(id) + ": " + game.getGameName() + "")
    file.close()
    self.chatMgr.DisplayStatusMessage("A list of your games has been saved in \"Games/List.txt\".")

def DownloadGame(self, gameID):

    games = GetList()
    if not os.path.exists("Games"):
        os.makedirs("Games")
    try:
        game = games[gameID]
        name = PtGetLocalPlayer().getPlayerName()
        guid = game.getGameGuid()
        self.editor["downloading"] = True
        self.editor["downloading_id"] = gameID
        self.editor["game"]["name"] = game.getGameName()
        self.editor["game"]["guid"] = guid
        PtCreateMarkerGame(self.key, PtMarkerGameTypes.kMarkerGameQuest, templateId = guid)
        filename = ""
        for c in name:
            if c.isalnum():
                filename += c
        self.chatMgr.DisplayStatusMessage("Your game has been downloaded as \"Games/" + filename + "." + str(gameID) + ".txt\"")
    except IndexError:
        self.chatMgr.DisplayStatusMessage("There is no such marker game.")

def GetList():

    games = []
    journals = ptVault().getAgeJournalsFolder()
    agefolderRefs = journals.getChildNodeRefList()
    for agefolderRef in agefolderRefs:
        agefolder = agefolderRef.getChild()
        if agefolder.getType() == PtVaultNodeTypes.kFolderNode:
            agefolder = agefolder.upcastToFolderNode()
            subs = agefolder.getChildNodeRefList()
            for sub in subs:
                sub = sub.getChild()
                if sub.getType() == PtVaultNodeTypes.kMarkerGameNode:
                    game = sub.upcastToMarkerGameNode()
                    games.append(game)
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
                    if game.getGameGuid() == guid:
                        valid = True
                        self.editor["node"] = game
                if not valid:
                    self.chatMgr.DisplayStatusMessage("Invalid GUID.")
                    return
                # We are editing an existing game.
                try:
                    if not isinstance(self.editor["game"]["markers"], list):
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