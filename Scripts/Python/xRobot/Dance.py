# -*- coding: utf-8 -*-
#Dance module

from Plasma import *
from PlasmaKITypes import *

import os

#===========================================================================================================
"""
    ** Cette partie est a supprimer **
"""

#
def SetFileName(self, playerID, ageFileName = None, prefix = None):
    #PtSendKIMessage(kKILocalChatStatusMsg, "> SetFileName")
    if ageFileName == None:
        ageFileName = PtGetAgeInfo().getAgeFilename()
    if not os.path.exists("Save"):
        os.mkdir("Save")
    fileName = "Save/" + str(playerID) + "_" + ageFileName
    if prefix != None and str(prefix) != "":
        fileName += "_" + str(prefix)
    fileName += ".txt"
    #PtSendKIMessage(kKILocalChatStatusMsg, "==> " + fileName)
    return fileName

# Reads the file and returns a list of strings representing the saved positions
def ReadFile(fileName):
    #PtSendKIMessage(kKILocalChatStatusMsg, "> ReadFile")
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
    #PtSendKIMessage(kKILocalChatStatusMsg, "> WriteFile")
    try:
        file = open(fileName, "w")
        file.write(content)
        file.close()
        return 1
    except:
        return 0

#Returns the tuple of the n-th position from a list of strings representing the saved positions
def GetPosition(positions, n = None):
    #PtSendKIMessage(kKILocalChatStatusMsg, "> GetPosition")
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
                #PtSendKIMessage(kKILocalChatStatusMsg, "=> pos elm: " + str(elm))
            lstPos.append(tuple(lstVal))
        #PtSendKIMessage(kKILocalChatStatusMsg, "=> lstPos ok ")
        tuplePos = tuple(lstPos)
        return tuplePos
    else:
        return None

def WriteMatrix44(self, n = None, player = None, ageFileName = None, prefix = None):
    #PtSendKIMessage(kKILocalChatStatusMsg, "> WriteMatrix44")
    if n == None:
        #n = len(positions)
        n = 0
    try:
        n = int(n)
    except:
        PtSendKIMessage(kKILocalChatStatusMsg, "==> n must be an integer in [0, 9]")
        return 1
    # Get the playerID
    if player == None:
        player = PtGetLocalPlayer()
    playerID = player.getPlayerID()
    # Get the already known positions for this player and age (if none, it'll return an empty list)
    fileName = SetFileName(self, playerID, ageFileName, prefix)
    positions = ReadFile(fileName)
    #PtSendKIMessage(kKILocalChatStatusMsg, "==> " + str(len(positions)) + " position(s) found")
    if n < 0 or n >= len(positions):
        PtSendKIMessage(kKILocalChatStatusMsg, "==> n must be an integer in [0, " + str(len(positions) - 1) + "]")
        return 1
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
    #PtSendKIMessage(kKILocalChatStatusMsg, "==> content length : "+str(len(content)))
    #if WriteFile(fileName, content) == 1:
    #    PtSendKIMessage(kKILocalChatStatusMsg, player.getPlayerName() + " has been saved his (her) position.")
    #else:
    #    PtSendKIMessage(kKILocalChatStatusMsg, player.getPlayerName() + " - Error while saving position!")
    WriteFile(fileName, content)

def WarpToSaved(self, n = None, player = None, ageFileName = None, prefix = None):
    #PtSendKIMessage(kKILocalChatStatusMsg, "> WarpToSaved(n='"+str(n)+"', ...)")
    if player == None:
        player = PtGetLocalPlayer()
    playerID = player.getPlayerID()
    soAvatar = PtGetAvatarKeyFromClientID(playerID).getSceneObject()
    #PtSendKIMessage(kKILocalChatStatusMsg, "=> " + player.getPlayerName())
    try:
        # Get the already known positions for this player and age (if none, it'll return an empty list)
        fileName = SetFileName(self, playerID, ageFileName, prefix)
        positions = ReadFile(fileName)
        tuplePos = GetPosition(positions, n)
        matPos = ptMatrix44()
        matPos.setData(tuplePos)
        soAvatar.netForce(1)
        soAvatar.physics.warp(matPos)
        #PtSendKIMessage(kKILocalChatStatusMsg, player.getPlayerName() + " is going to his (her) saved position.")
        return 1
    except:
        PtSendKIMessage(kKILocalChatStatusMsg, player.getPlayerName() + " has no saved position.")
        return 0

#===========================================================================================================
"""
    A brief example of the script for Michel:
        motion|number|pause sec

        group|137998,254640,5667000,132492,133403,2975513,4884667,4082721
        stepleft|1|0|begin raindance
        stepright|1|0
        stepleft|1|0
        stepright|1|0
        stepleft|1|0
        stepright|1|0
        cheer|1|0
        ...
        groundimpact|1|0
        cheer|1|0
        groundimpact|1|0
        PAUSE

    Example of dance file from "1 Paartanz.txt"
        Dance 1 "Paartanz"
        group|5667000
        agoto|94|-1067|1010|0
        land|0
        ...
        group|2975513
        agoto|78|-1092|1010|0
        land|0
        group|132492
        agoto|94|-1092|1011|0
        land
        ENDE

    Line 1 => Name of the dance info, nothing to do with this line, ignore it!
    A line begining with END is the end of the file dance.
    A line begining with GROUP tels witch payers will be commanded
    Other lines are command lines :
        <CmdName>|<arg1>|[...|<argN>]|<WaitDurationInSecondsBeforeNextCmd>
"""

"""
#
def SetDanceFileName(self, danceFileName=""):
    #PtSendKIMessage(kKILocalChatStatusMsg, "> SetFileName")
    subdir = "Dance"
    if not os.path.exists(subdir):
        os.mkdir(subdir)
    fileName = subdir + "/" + danceFileName + ".txt"
    #PtSendKIMessage(kKILocalChatStatusMsg, "==> " + fileName)
    return fileName
"""

# Reads the file dance and returns a list of strings representing the actions the bot has to do
def ReadDanceFile(danceFileName):
    #PtSendKIMessage(kKILocalChatStatusMsg, "> ReadDanceFile")
    subdir = "Dance"
    if not os.path.exists(subdir):
        os.mkdir(subdir)
    fileName = "{0}/{1}.txt".format(subdir, danceFileName)
    actions = list()
    try:
        file = open(fileName, "r")
        content = file.read()
        file.close()
        content.replace("\r\n", "\n")
        content.replace("\r", "\n")
        content.replace("\t", "")
        for strAct in content.split("\n"):
            strAct = strAct.strip()
            if strAct != "" :
                actions.append(strAct.strip())
    except:
        # The file does not exist, send an error message.
        print("The {} file does not exist.".format(fileName))
    return actions

# Converts an action string line into a command line.
# To use it in : result = xPlayerKiCmds.CallMethod(self, cmdName, cFlags, amIRobot, args)
# <CmdName>|<arg1>|[...|<argN>]|<WaitDurationInSecondsBeforeNextCmd>
# [<CmdName>, [<arg1>, ..., <argN>], <WaitDurationInSecondsBeforeNextCmd>]
def ConvertActionToCommand(strAct):
    actLine = strAct.split("|")
    cmdName = None
    cmdArgs = ""
    waitArg = 0.0
    
    if len(actLine) > 0:
        #cmdName = actLine[0].strip()
        #waitArg = actLine[len(actLine) - 1].strip()
        #if len(actLine) > 2:
        #    for arg in actLine[1, len(actLine) - 2]:
        #        cmdArgs.append(arg.strip())
        #else:
        #    print "Bad action line!"
        cmdName = actLine.pop(0).strip()
        if len(actLine) > 0:
            try:
                waitArg = float(actLine.pop(len(actLine) - 1).strip())
            except:
                waitArg = 0.0
            #for arg in actLine:
            #    cmdArgs = " " + arg.strip()
            cmdArgs = " ".join(map(str.strip, actLine))
        else:
            print("Bad action line!")
    else:
        print("Empty action line!")
    cmdLine = [cmdName, cmdArgs, waitArg]
    print("ConvertActionToCommand : {}".format(cmdLine))
    return cmdLine

#
#lstIdDancers = []

# Changes the players the bot has to execute the command for. 
# group|137998,254640,5667000,132492,133403,2975513,4884667,4082721
def GetIdDancerList(strAct):
    #global lstIdDancers
    print("SetIdDancerList('{}')".format(strAct))
    grpLine = strAct.split("|")
    lstIdPlayers = []
    if len(grpLine) > 1:
        lstStrIds = grpLine[1].split(",")
        # Case for all players in age : group|all
        if len(lstStrIds) == 1:
            if lstStrIds[0].lower().strip() == "all":
                return lstIdPlayers, True
        # Normal case with a liste of player ids
        for strId in lstStrIds:
            strId = strId.strip()
            try:
                id = int(strId)
                try:
                    lstIdPlayers.append(id)
                except:
                    print("Error in SetIdDancerList : lstIdPlayers.append({})".format(id))
            except:
                print("SetIdDancerList : '{}' is not a player id, skip it.".format(strId))
    #lstIdDancers = lstIdPlayers
    return lstIdPlayers, False

# Define the group of dancers
# This is dictionary of alais names and ids
# definegroup|alias1:254640,alias2:132492,alias3:2975513,alias4:4082721
def DefineGroup(strAct):
    print("DefineGroup('{}')".format(strAct))
    grpLine = strAct.split("|")
    dictDancers = dict()
    if len(grpLine) > 1:
        lstStr = grpLine[1].split(",")
        for strDancer in lstStr:
            strDancer = strDancer.strip()
            strAliasId = strDancer.split(":")
            if len(strAliasId) == 2:
                alias = strAliasId[0]
                strId = strAliasId[1]
                try:
                    id = int(strId)
                    try:
                        dictDancers.update({alias:id})
                    except:
                        print("Error in DefineGroup : dictDancers.update(\"{}\":{})".format(alias, id))
                except:
                    print("DefineGroup : '{}' is not a player id, skip it.".format(strId))
    return dictDancers

# Changes the players the bot has to execute the command for. 
# group|alias1,alias2,alias3,alias4
def GetIdDancerListFromAlias(strAct, dictDancers=dict()):
    print("GetIdDancerListFromAlias('{}')".format(strAct))
    grpLine = strAct.split("|")
    lstAlias = []
    lstIdPlayers = []
    if len(grpLine) > 1:
        lstAlias = grpLine[1].split(",")
        for alias in lstAlias:
            #alias = alias.strip()
            try:
                id = int(dictDancers[alias])
                try:
                    lstIdPlayers.append(id)
                except:
                    print("Error in GetIdDancerListFromAlias : lstIdPlayers.append({})".format(id))
            except KeyError:
                print("GetIdDancerListFromAlias - KeyError: unknown alias '{}', skip it.".format(alias))
            except:
                print("GetIdDancerListFromAlias : '{}' is not a player id, skip it.".format(dictDancers[alias]))
    #lstIdDancers = lstIdPlayers
    return lstIdPlayers

"""
    agePlayers = filter(lambda pl: not(pl.getPlayerID() in dicBot.keys()), PtGetPlayerList())
    agePlayers.append(PtGetLocalPlayer())
    playerIdList = map(lambda player: player.getPlayerID(), agePlayers)
    
    avatar = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
    
    in Plasma:
        class ptPlayer:
        '''And optionally __init__(name,playerID)'''
        def __init__(self,avkey,name,playerID,distanceSq):
            '''None'''
            pass

"""

"""
# What kind of line is it?
# Dance, group, end, <action line>
def PrepareDance(lstActions):
    for strAct in lstActions:
        if strAct.lower.startswith("dance "):
            print strAct
        elif strAct.lower.startswith("end"):
            print "This is the end!"
        elif strAct.lower.startswith("group"):
            print "New group of dancers."
            SetIdDancerList(strAct)
        else:
            print "Command line"
            cmdLine = ConvertActionToCommand(strAct)
"""

#