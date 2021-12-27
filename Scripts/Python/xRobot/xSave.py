#xSave module

from Plasma import *


def WriteMatrix44(self, player = None, ageFileName = None, prefix = None):
    if player == None:
        player = PtGetLocalPlayer()
    playerID = player.getPlayerID()
    if ageFileName == None:
        ageFileName = PtGetAgeInfo().getAgeFilename()
    fileName = "Save/" + str(playerID) + "_" + ageFileName
    if prefix != None and str(prefix) != "":
        fileName += "_" + str(prefix)
    fileName += ".txt"
    #self.chatMgr.DisplayStatusMessage(player.getPlayerName())
    #self.chatMgr.DisplayStatusMessage(str(playerID))
    soAvatar = PtGetAvatarKeyFromClientID(playerID).getSceneObject()
    #self.chatMgr.DisplayStatusMessage(str(soAvatar))
    matPos = soAvatar.getLocalToWorld()
    tuplePos = matPos.getData()
    strPos = ""
    for t in tuplePos:
        for e in t:
            strPos += str(e) + "\t"
        strPos = strPos[:len(strPos) - 1]
        strPos += "\n"
    strPos = strPos[:len(strPos) - 1]
    file = open(fileName, "w")
    #for id, game in enumerate(getList()):
    #    file.write(str(id) + ": \"" + game.getGameName() + "\"\n")
    file.write(strPos)
    file.close()
    self.chatMgr.AddChatLine(None, player.getPlayerName() + " has been saved his (her) position.", 3)

def WarpToSaved(self, player = None, ageFileName = None, prefix = None):
    #self.chatMgr.AddChatLine(None, "> WarpToSaved", 3)
    if player == None:
        player = PtGetLocalPlayer()
    playerID = player.getPlayerID()
    if ageFileName == None:
        ageFileName = PtGetAgeInfo().getAgeFilename()
    fileName = "Save/" + str(playerID) + "_" + ageFileName
    if prefix != None and str(prefix) != "":
        fileName += "_" + str(prefix)
    fileName += ".txt"
    soAvatar = PtGetAvatarKeyFromClientID(playerID).getSceneObject()
    #self.chatMgr.AddChatLine(None, "=> " + player.getPlayerName(), 3)
    try:
        file = open(fileName, "r")
        strPos = file.read()
        file.close()
        #self.chatMgr.AddChatLine(None, "=> Read: " + fileName, 3)
        lstPos = list()
        lstStr = strPos.split("\n")
        for s in lstStr:
            lst = s.split("\t")
            lstVal = list()
            for elm in lst:
                lstVal.append(float(elm))
                #self.chatMgr.AddChatLine(None, "=> pos elm: " + str(elm), 3)
            lstPos.append(tuple(lstVal))
        #self.chatMgr.AddChatLine(None, "=> lstPos ok ", 3)
        tuplePos = tuple(lstPos)
        matPos = ptMatrix44()
        matPos.setData(tuplePos)
        soAvatar.netForce(1)
        soAvatar.physics.warp(matPos)
        self.chatMgr.AddChatLine(None, player.getPlayerName() + " is going to his (her) saved position.", 3)
        return 1
    except:
        self.chatMgr.AddChatLine(None, player.getPlayerName() + " has no saved position.", 3)
        return 0