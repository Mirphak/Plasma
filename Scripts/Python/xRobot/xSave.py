# -*- coding: utf-8 -*-
#xSave module

import os
from Plasma import *
from PlasmaKITypes import *


def WriteMatrix44(self, player = None, ageFileName = None, prefix = None):
    if player == None:
        player = PtGetLocalPlayer()
    playerID = player.getPlayerID()
    if ageFileName == None:
        ageFileName = PtGetAgeInfo().getAgeFilename()
    if not os.path.exists("Save"):
        os.makedirs("Save")
    fileName = "Save/" + str(playerID) + "_" + ageFileName
    if prefix != None and str(prefix) != "":
        fileName += "_" + str(prefix)
    fileName += ".txt"
    #PtSendKIMessage(kKILocalChatStatusMsg, player.getPlayerName())
    #PtSendKIMessage(kKILocalChatStatusMsg, str(playerID))
    soAvatar = PtGetAvatarKeyFromClientID(playerID).getSceneObject()
    #PtSendKIMessage(kKILocalChatStatusMsg, str(soAvatar))
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
    #PtSendKIMessage(kKILocalChatStatusMsg, player.getPlayerName() + " has been saved his (her) position.")

def WarpToSaved(self, player = None, ageFileName = None, prefix = None):
    #PtSendKIMessage(kKILocalChatStatusMsg, "> WarpToSaved")
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
    #PtSendKIMessage(kKILocalChatStatusMsg, "=> " + player.getPlayerName())
    try:
        file = open(fileName, "r")
        strPos = file.read()
        file.close()
        #PtSendKIMessage(kKILocalChatStatusMsg, "=> Read: " + fileName)
        lstPos = list()
        lstStr = strPos.split("\n")
        for s in lstStr:
            lst = s.split("\t")
            lstVal = list()
            for elm in lst:
                lstVal.append(float(elm))
                #PtSendKIMessage(kKILocalChatStatusMsg, "=> pos elm: " + str(elm))
            lstPos.append(tuple(lstVal))
        #PtSendKIMessage(kKILocalChatStatusMsg, "=> lstPos ok ")
        tuplePos = tuple(lstPos)
        matPos = ptMatrix44()
        matPos.setData(tuplePos)
        soAvatar.netForce(1)
        soAvatar.physics.warp(matPos)
        #PtSendKIMessage(kKILocalChatStatusMsg, player.getPlayerName() + " is going to his (her) saved position.")
        return 1
    except:
        PtSendKIMessage(kKILocalChatStatusMsg, player.getPlayerName() + " has no saved position.")
        return 0