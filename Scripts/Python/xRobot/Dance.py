#xSave module

from Plasma import *
import os

#===========================================================================================================
"""
    ** Cette partie est a supprimer **
"""

#
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
        self.chatMgr.AddChatLine(None, "==> n must be an integer in [0, 9]", 3)
        return 1
    # Get the playerID
    if player == None:
        player = PtGetLocalPlayer()
    playerID = player.getPlayerID()
    # Get the already known positions for this player and age (if none, it'll return an empty list)
    fileName = SetFileName(self, playerID, ageFileName, prefix)
    positions = ReadFile(fileName)
    #self.chatMgr.AddChatLine(None, "==> " + str(len(positions)) + " position(s) found", 3)
    if n < 0 or n >= len(positions):
        self.chatMgr.AddChatLine(None, "==> n must be an integer in [0, " + str(len(positions) - 1) + "]", 3)
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
    #self.chatMgr.AddChatLine(None, "> SetFileName", 3)
    subdir = "Dance"
    if not os.path.exists(subdir):
        os.mkdir(subdir)
    fileName = subdir + "/" + danceFileName + ".txt"
    #self.chatMgr.AddChatLine(None, "==> " + fileName, 3)
    return fileName
"""

# Reads the file dance and returns a list of strings representing the actions the bot has to do
def ReadDanceFile(danceFileName):
    #self.chatMgr.AddChatLine(None, "> ReadDanceFile", 3)
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
        print "The {} file does not exist.".format(fileName)
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
            print "Bad action line!"
    else:
        print "Empty action line!"
    cmdLine = [cmdName, cmdArgs, waitArg]
    print "ConvertActionToCommand : {}".format(cmdLine)
    return cmdLine

#
#lstIdDancers = []

# Changes the players the bot has to execute the command for. 
# group|137998,254640,5667000,132492,133403,2975513,4884667,4082721
def GetIdDancerList(strAct):
    global lstIdDancers
    print "SetIdDancerList('{}')".format(strAct)
    grpLine = strAct.split("|")
    lstIdPlayers = []
    if len(grpLine) > 1:
        lstStrIds = grpLine[1].split(",")
        for strId in lstStrIds:
            strId = strId.strip()
            try:
                id = long(strId)
                try:
                    lstIdPlayers.append(id)
                except:
                    print "Error in SetIdDancerList : lstIdPlayers.append({})".format(id)
            except:
                print "SetIdDancerList : '{}' is not a player id, skip it.".format(strId)
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