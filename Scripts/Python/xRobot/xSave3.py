#xSave module

from Plasma import *
import os

def SetFileName(self, playerID, ageFileName = None, prefix = None):
    #self.chatMgr.AddChatLine(None, "> SetFileName", 3)
    if ageFileName == None:
        ageFileName = PtGetAgeInfo().getAgeFilename()
    if not os.path.exists("Save"):
        os.mkdir("Save")
    fileName = "Save/" + str(playerID) + "_" + ageFileName
    if prefix != None and str(prefix) != "":
        fileName += "_" + str(prefix)
    fileName += ".txt"
    #self.chatMgr.AddChatLine(None, "==> " + fileName, 3)
    return fileName

# Reads the file and returns a list of strings representing the saved positions
def ReadFile(fileName):
    #self.chatMgr.AddChatLine(None, "> ReadFile", 3)
    positions = list()
    try:
        file = open(fileName, "r")
        content = file.read()
        file.close()
        for strPos in content.split("\n"):
            positions.append(strPos)
    except:
        # The file does not exist yet, then creating a default list of positions
        positions = [""] * 10
    return positions

def WriteFile(fileName, content):
    #self.chatMgr.AddChatLine(None, "> WriteFile", 3)
    try:
        file = open(fileName, "w")
        file.write(content)
        file.close()
        return 1
    except:
        return 0

#Returns the tuple of the n-th position from a list of strings representing the saved positions
def GetPosition(positions, n = None):
    #self.chatMgr.AddChatLine(None, "> GetPosition", 3)
    if type(positions) != list:
        return None
    if positions == list():
        return None
    if n == None:
        #n = len(positions)
        n = 0
    try:
        n = int(n)
    except:
        return None
    #if n > 0 and n <= len(positions):
    if n >= 0 and n < len(positions):
        lstPos = list()
        #lstStr = positions[n-1].split("|")
        lstStr = positions[n].split("|")
        for s in lstStr:
            lst = s.split(";")
            lstVal = list()
            for elm in lst:
                lstVal.append(float(elm))
                #self.chatMgr.AddChatLine(None, "=> pos elm: " + str(elm), 3)
            lstPos.append(tuple(lstVal))
        #self.chatMgr.AddChatLine(None, "=> lstPos ok ", 3)
        tuplePos = tuple(lstPos)
        return tuplePos
    else:
        return None

def WriteMatrix44(self, n = None, player = None, ageFileName = None, prefix = None):
    #self.chatMgr.AddChatLine(None, "> WriteMatrix44", 3)
    if n == None:
        #n = len(positions)
        n = 0
    try:
        n = int(n)
    except:
        #self.chatMgr.AddChatLine(None, "==> n must be an integer in [0, 9]", 3)
        self.chatMgr.AddChatLine(None, "==> n must be a positive integer.", 3)
        return 1
    # Get the playerID
    if player == None:
        player = PtGetLocalPlayer()
    playerID = player.getPlayerID()
    # Get the already known positions for this player and age (if none, it'll return an empty list)
    fileName = SetFileName(self, playerID, ageFileName, prefix)
    positions = ReadFile(fileName)
    #self.chatMgr.AddChatLine(None, "==> " + str(len(positions)) + " position(s) found", 3)
    """
    if n < 0 or n >= len(positions):
        self.chatMgr.AddChatLine(None, "==> n must be an integer in [0, " + str(len(positions) - 1) + "]", 3)
        return 1
    """
    if n < 0:
        self.chatMgr.AddChatLine(None, "==> n must be a positive integer.", 3)
        return 1
    elif n >= len(positions):
        #self.chatMgr.AddChatLine(None, "==> n must be an integer in [0, " + str(len(positions) - 1) + "]", 3)
        #return 1
        # I need to increase the number of positions in the list
        newPositions = [""] * (n - len(positions) + 1)
        positions.extend(newPositions)
    
    # Get new position
    soAvatar = PtGetAvatarKeyFromClientID(playerID).getSceneObject()
    matPos = soAvatar.getLocalToWorld()
    tuplePos = matPos.getData()
    strPos = ""
    for t in tuplePos:
        for e in t:
            strPos += str(e) + ";"
        strPos = strPos[:len(strPos) - 1]
        strPos += "|"
    #strPos += "\n"
    strPos = strPos[:len(strPos) - 1]
    ## Add it to the list of positions
    #positions.append(strPos)
    # Replace the n-th position by the new one
    positions[n] = strPos
    # Stringify the list of positions
    content = ""
    for strPos in positions:
        content += strPos + "\n"
    content = content[:len(content) - 1]
    # Edit the file
    #self.chatMgr.AddChatLine(None, "==> content length : "+str(len(content)), 3)
    if WriteFile(fileName, content) == 1:
        self.chatMgr.AddChatLine(None, player.getPlayerName() + " has been saved his (her) position.", 3)
    else:
        self.chatMgr.AddChatLine(None, player.getPlayerName() + " - Error while saving position!", 3)

def WarpToSaved(self, n = None, player = None, ageFileName = None, prefix = None):
    #self.chatMgr.AddChatLine(None, "> WarpToSaved(n='"+str(n)+"', ...)", 3)
    if player == None:
        player = PtGetLocalPlayer()
    playerID = player.getPlayerID()
    soAvatar = PtGetAvatarKeyFromClientID(playerID).getSceneObject()
    #self.chatMgr.AddChatLine(None, "=> " + player.getPlayerName(), 3)
    try:
        # Get the already known positions for this player and age (if none, it'll return an empty list)
        fileName = SetFileName(self, playerID, ageFileName, prefix)
        positions = ReadFile(fileName)
        tuplePos = GetPosition(positions, n)
        matPos = ptMatrix44()
        matPos.setData(tuplePos)
        soAvatar.netForce(1)
        soAvatar.physics.warp(matPos)
        self.chatMgr.AddChatLine(None, player.getPlayerName() + " is going to his (her) saved position.", 3)
        return 1
    except:
        self.chatMgr.AddChatLine(None, player.getPlayerName() + " has no saved position.", 3)
        return 0