# -*- coding: utf-8 -*-

#Import des modules Plasma (tous ne seront peut-etre pas utiles)
from Plasma import *
#from PlasmaGame import *
#from PlasmaGameConstants import *
from PlasmaKITypes import *
#from PlasmaVaultConstants import *

# Modules du robot
import sys
import re

from xRobot import *

import xRobot.CheckPlayersArrival as CheckPlayersArrival

# Greetings list
greetings = ["shorah", "hi", "hello", "bonjour", "bonsoir", "salut", "hallo", "allo", "privet"]

# Execute a player's command
#def Do(self, player, message, cFlags):
def Do(player, message, cFlags):
    # En attendant de supprimer tous les self, je le met à None
    self = None
    
    if not IsAllowed():
        # I can't be a bot in this age, so I do nothing
        PtSendKIMessage(kKILocalChatStatusMsg, "I can't be a bot in this age, so I do nothing".format(message))
        return
    #ne pas repondre aux robots
    #if (player.getPlayerID() in dicBot.keys()):
    myself = PtGetLocalPlayer()
    #if (player.getPlayerID() in xPlayers.dicBot.keys() and player.getPlayerID() != myself.getPlayerID()):
    #if player.getPlayerID() != myself.getPlayerID():
    #    return

    plist = [player]
    playerName = player.getPlayerName()
    playerId = player.getPlayerID()
    if playerId == 0:
        print("Error : Player Id = 0 !")
        PtSendKIMessage(kKILocalChatStatusMsg, "Error : Player Id = 0 !")
        return
    
    myAge = PtGetAgeInfo().getDisplayName()
    myAgeInstanceGuid = PtGetAgeInfo().getAgeInstanceGuid()
    
    # remplacer les caracteres non ascii pour eviter les erreur du type UnicodeDecodeError ou UnicodeEncodeError
    message = "".join([x if ord(x) < 128 else '?' for x in message])
    
    # decomposition du message si chat interage
    if message[:2] == "<<":
        try:
            idx = message.index(">>")
            message = message[idx+2:]
        except ValueError:
            pass

    # pour repondre a une salutation
    words = message.lower().split(" ")
    nbWords = len(words)
    msg = ""
    if nbWords > 0:
        if words[0] in greetings:
            msg = "Shorah " + playerName
        elif nbWords > 1:
            if words[1] in ("morning", "afternoon"):
                msg = "Shorah " + playerName
    if msg != "":
        #Je reponds aux gens polis
        #xBotAge.currentBotAge = xBotAge.GetBotAge()
        if len(xBotAge.currentBotAge) > 3:
            msg += ", I am in " + xBotAge.currentBotAge[3] + " " + xBotAge.currentBotAge[0]
            #if len(PtGetPlayerList()) == 0:
            #    msg += ". I'm alone."
            #elif len(PtGetPlayerList()) == 1:
            #    msg += ". There is one player with me."
            #else:
            #    msg += ". There is " + str(len(PtGetPlayerList())) + " players with me."
            # Comptons les joueurs presents sauf les robots
            nbPlayers = len([pl for pl in PtGetPlayerList() if not(pl.getPlayerID() in list(xPlayers.dicBot.keys()))])
            if nbPlayers == 0:
                msg += ". I'm alone."
            elif nbPlayers == 1:
                msg += ". There is one player with me."
            else:
                msg += ". There is " + str(len(PtGetPlayerList())) + " players with me."
        #msg += "\n Latest commands: 'cms', 'to dakotah', 'night', 'save [n]' and 'ws [n]'."
        #Mister Magic inform you that bots will rest Thursday 2 and Friday 3 April.They will be back in the cave on Saturday April 4th. Thanks.
        #msg += "Mirphak's holydays will begin on Thursday April 2nd, I will rest until Sunday April 12th. Thanks."
        #msg += "Mirphak informs you that Mir-o-Bot will rest from Thursday September 9th to Wednesday September 22nd. Thanks."
        #msg += "Mirphak informs you that Mir-o-Bot will rest from Saturday Jully 2nd to Sunday Jully 17th. Thanks."
        #C'est mieux d'envoyer un message en statut interage plutot qu'en prive
        PtSendRTChat(myself, plist, msg, 24)
    else:
        #Ne pas repondre aux messages AFK ou vides
        if not (message.strip() == "" or PtGetLocalizedString("KI.Chat.AFK") in message):
            cmdName = ""
            args = [player]
            result = 0
            cmd = message.split(" ", 1)
            if len(cmd) > 0:
                cmdName = cmd[0].lower()
                if len(cmd) > 1:
                    args.append(cmd[1])
                else:
                    pass
                #Traitement de la demande du joueur
                result = xPlayerKiCmds.CallMethod(self, cmdName, cFlags, amIRobot, args)
        
            if not result:
                msg = 'Sorry, I don\'t understand \"' + message + '\"'
                if message.strip() != "":
                    #PtSendRTChat(myself, plist, msg, cFlags.flags)
                    PtSendRTChat(myself, plist, msg, 24)
                PtSendKIMessage(kKILocalChatStatusMsg, "** Command \"{}\" not found! **".format(message))
                print(("** Command \"{}\" not found! **".format(message)))
                try:
                    #envoi d'un message d'aide si possible
                    args = [player]
                    cmdName = "help"
                    if len(cmd) > 0:
                        args.append(cmd[0].lower())
                    else:
                        args.append("?")
                    if message.strip() != "" or message.strip() != "":
                        xPlayerKiCmds.CallMethod(self, cmdName, cFlags, amIRobot, args)
                except Exception as e:
                    PtSendKIMessage(kKILocalChatStatusMsg, "** Error in {}, {}, {}: {} **".format(cmdName, playerName, args[1], e))
                    print(("** Error in {}, {}, {}: {} **".format(cmdName, playerName, args[1], e)))
            else:
                PtSendKIMessage(kKILocalChatStatusMsg, "** Command \"{}\" executed. **".format(message))
                print(("** Command \"{}\" executed. **".format(message)))
                
                if CheckPlayersArrival.isActive and cmdName in ("link", "meet"):
                    #CheckPlayersArrival.StartChecking(self, player, method=DoNothing, params=[])
                    #CheckPlayersArrival.StartChecking(self, player)
                    CheckPlayersArrival.StartChecking(player)
                    PtSendKIMessage(kKILocalChatStatusMsg, "** CheckPlayersArrival executed. **")
                    print("** CheckPlayersArrival executed. **")

# If I receave a command when I'm not in robot mode
def Info(self, player, message, cFlags):
    myself = PtGetLocalPlayer()
    cmdName = ""
    plist = [player]
    #result = 0
    
    # decomposition du message si chat interage
    if message[:2] == "<<":
        try:
            idx = message.index(">>")
            message = message[idx+2:]
        except ValueError:
            pass
    
    cmd = message.split(" ", 1)
    if len(cmd) > 0:
        cmdName = cmd[0].lower()
        if cmdName in xPlayerKiCmds.cmdDict:
            if myself.getPlayerID() == 32319:
                msg = "Sorry, I\'m not in robot mode, try later."
                #PtSendRTChat(myself, plist, msg, cFlags.flags)
                PtSendRTChat(myself, plist, msg, 24)
            #else:
            #    msg = "Sorry, I\'m not Mir-o-Bot (KI 19542524) ..."
            #PtSendRTChat(myself, plist, msg, cFlags.flags)
            #PtSendRTChat(myself, plist, msg, 24)


# link yourself to an age instance
# type /linkto <ageName> in chat
#(the message is transformed in lowercase in xKI.py near line 7000)
def LinkToAge(self, linkName):
    xBotKiCmds.LinkToAge(self, linkName)

def LinkToPublicAge(self, linkName):
    myself = PtGetLocalPlayer()
    playerName = myself.getPlayerName()
    msg = ""
    linkName = linkName.lower().replace(" ", "").replace("'", "").replace("eder", "")
    if (not amIRobot and playerName != "Mir-o-Bot") or not (linkName in list(ages.PublicAgeDict.keys())):
        instanceName = xBotAge.LinkPlayerToPublic(self, linkName)
        if instanceName:
            msg = "I'm linking to " + instanceName + " ..."
        else:
            msg = "I don't know where " + linkName + " is!"
    else:
        msg = "I can't go to public!"
    PtSendKIMessage(kKILocalChatStatusMsg, msg)

# Write the age guid
def GetPlayerAgeGUID(self, playerID = None):
    guid = xBotAge.GetPlayerAgeGUID(playerID)
    if guid:
        PtSendKIMessage(kKILocalChatStatusMsg, guid)
    else:
        PtSendKIMessage(kKILocalChatStatusMsg, "Age GUID not found")

# Write some age infos
def GetPlayerAgeInfo(self, playerID = None):
    #try:
    #    playerID = int(playerID)
    #except:
    #    PtSendKIMessage(kKILocalChatStatusMsg, "KI number needed!")
    ageInfo = xBotAge.GetPlayerAgeInfo(playerID)
    if ageInfo:
        msg = ageInfo.playerGetAgeInstanceName()
        msg += " " + ageInfo.playerGetAgeGuid()
        PtSendKIMessage(kKILocalChatStatusMsg, msg)
    else:
        PtSendKIMessage(kKILocalChatStatusMsg, "Age not found")

#
def WarpToSpawnPoint(self, spNum = None):
    xBotKiCmds.WarpToSpawnPoint(self, spNum)

#
def WarpToPlayerOrSceneObject(self, name):
    ret = xBotKiCmds.WarpToPlayer(self, name)
    if ret[0] == 1:
        PtSendKIMessage(kKILocalChatStatusMsg, ret[1])
    else:
        ret = xBotKiCmds.WarpToPlayer(self, name)
        if ret[0] == 0:
            ret = xBotKiCmds.WarpToSceneObject(self, name)
        PtSendKIMessage(kKILocalChatStatusMsg, ret[1])

#
def ShowSceneObjects(self, name):
    xBotKiCmds.ShowSceneObjects(self, name)

#
def ShowSceneObjectsInAge(self, name, age):
    xBotKiCmds.ShowSceneObjectsInAge(self, name, age)

#
def ShowSceneObjectsWithCoords(self, name):
    xBotKiCmds.ShowSceneObjectsWithCoords(self, name)

#
def AddCleft(self):
    #PtSendKIMessage(kKILocalChatStatusMsg, "Adding Cleft...")
    #try:
    #    xBotKiCmds.AddCleft()
    #    PtSendKIMessage(kKILocalChatStatusMsg, "Cleft added!")
    #except:
    #    PtSendKIMessage(kKILocalChatStatusMsg, "Error while adding Cleft.")
    xBotKiCmds.AddCleft(self)

#
def AddHood(self):
    xBotKiCmds.AddHood(self)

#
def AddRelto(self):
    xBotKiCmds.AddRelto(self)

#************************************************************************#
#----------------#
# Robot commands #
#----------------#

#Premier caractere pour reconnaitre une commande de robot
startChar = "!"

# Variable pour savoir si le mode robot est actif
amIRobot = 0

#==========================#
# Survey Bot Age
#==========================#
class SurveyBotAge:
    _running = False
    _xKiSelf = None
    _nbTry   = 0

    def __init__(self):
        print("SurveyBotAge:")
        
    def WhereAmI(self):
        print("SurveyBotAge:")
        myCurrentAgeInstanceGuid = PtGetAgeInfo().getAgeInstanceGuid()
        # Am I in one of Mir-o-Bot's age?
        for val in list(ages.MirobotAgeDict.values()):
            if val[2] == myCurrentAgeInstanceGuid:
                # I am in a Mir-o-Bot age, it's ok.
                print("SurveyBotAge:ok mob")
                self._nbTry = 0
                return
        # Am I in one of MagicBot age?
        for val in list(ages.MagicbotAgeDict.values()):
            if val[2] == myCurrentAgeInstanceGuid:
                # I am in a Mir-o-Bot age, it's ok.
                print("SurveyBotAge:ok magic")
                self._nbTry = 0
                return
        # Am I in one of my own private age?
        myAges = ptVault().getAgesIOwnFolder().getChildNodeRefList()
        for age in myAges:
            ageInfo = age.getChild().upcastToAgeLinkNode().getAgeInfo()
            if ageInfo.getAgeInstanceGuid() == myCurrentAgeInstanceGuid:
                # OK
                print("SurveyBotAge:ok own")
                self._nbTry = 0
                return
        # Am I in a Public Age ?
        #if not PtGetAgeInfo().isPublic(): # This does not work => AttributeError: 'Plasma.ptAgeInfoStruct' object has no attribute 'isPublic'
        #    #print "IsAllowed : {0} is public => I can't stay here as a bot!".format(msg)
        #    return
        infoNode = ptAgeVault().getAgeInfo()
        if not infoNode.isPublic():
            print("SurveyBotAge:ok, I am in a private age.")
            return
        print("This age is not allowed for the bot: {0}, {1}".format(PtGetAgeInfo().getAgeFilename(), myCurrentAgeInstanceGuid))
        # I am not welcome here, link myself in an allowed age
        if self._xKiSelf is None:
            print("SurveyBotAge:Error: self._xKiSelf is none, quit MOULa")
            PtConsole("App.Quit")
        else:
            self._nbTry += 1
            print("SurveyBotAge:try link (#{})".format(self._nbTry))
            if self._nbTry > 8:
                PtConsole("App.Quit")
            try:
                LinkToPublicAge(self._xKiSelf, "hood")
            except:
                print("SurveyBotAge:error linking")
                PtConsole("App.Quit")
        
    def onAlarm(self, param=1):
        print("SurveyBotAge:onalarm")
        if not self._running:
            print("SurveyBotAge:not running")
            return
        print("SurveyBotAge:call WhereAmI")
        self.WhereAmI()
        #Check age player positions to see why I have Collision error crash
        agePlayers = PtGetPlayerList()
        for player in agePlayers:
            so = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
            pos = so.position()
            #PtDebugPrint(f">> Check position of {so.getName()}: {round(pos.getX(), 2)}, {round(pos.getY(), 2)}, {round(pos.getZ())}")
            print(f">> Check position of {player.getPlayerName()}: {round(pos.getX(), 2)}, {round(pos.getY(), 2)}, {round(pos.getZ())}")
        #
        PtSetAlarm(15, self, 1)
        
    def Start(self, xKiSelf):
        self._xKiSelf = xKiSelf
        if not self._running:
            self._running = True
            print("SurveyBotAge:start")
            self.onAlarm()

    def Stop(self):
        print("SurveyBotAge:stop")
        self._running = False

surveyBot = SurveyBotAge()


#==========================#
# CheckPos
#==========================#
class CheckPos:
    _running = False
    _xKiSelf = None
    _nbTry   = 0
    
    def __init__(self):
        print("CheckPos:")
    
    def onAlarm(self, param=1):
        #print("CheckPos:onalarm")
        if not self._running:
            print("CheckPos:not running")
            return
        #Check age player positions to see why I have Collision error crash
        agePlayers = PtGetPlayerList()
        #print(f"CheckPos : Nb players = {len(agePlayers)}")
        PtDebugPrint(f"CheckPos : Nb players = {len(agePlayers)}")
        
        for player in agePlayers:
            so = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
            pos = so.position()
            #PtDebugPrint(f">> Check position of {so.getName()}: {round(pos.getX(), 2)}, {round(pos.getY(), 2)}, {round(pos.getZ())}")
            #print(f">> Check position of {so.getName()}: {round(pos.getX(), 2)}, {round(pos.getY(), 2)}, {round(pos.getZ())}")
            PtDebugPrint(f">> Check position of {player.getPlayerName()}: {round(pos.getX(), 2)}, {round(pos.getY(), 2)}, {round(pos.getZ())}")
        
        PtSetAlarm(5, self, 1)
    
    def Start(self, xKiSelf):
        self._xKiSelf = xKiSelf
        if not self._running:
            self._running = True
            print("CheckPos:start")
            self.onAlarm()
    
    def Stop(self):
        print("CheckPos:stop")
        self._running = False

checkPos = CheckPos()

#************************************************************************#
"""
# IsAllowed Version 1
def IsAllowed():
    myCurrentAgeInstanceGuid = PtGetAgeInfo().getAgeInstanceGuid()
    # Am I in one of Mir-o-Bot's age?
    for val in ages.MirobotAgeDict.values():
        if val[2] == myCurrentAgeInstanceGuid:
            # I am in a Mir-o-Bot age, it's ok.
            print "IsAllowed : I am in a Mir-o-Bot age, it's ok."
            return True
    # Am I in one of Mir-o-Bot age?
    for val in ages.MagicbotAgeDict.values():
        if val[2] == myCurrentAgeInstanceGuid:
            # I am in a Mir-o-Bot age, it's ok.
            print "IsAllowed : I am in a Mir-o-Bot age, it's ok."
            return True
    # Am I in one of my own private age?
    myAges = ptVault().getAgesIOwnFolder().getChildNodeRefList()
    for age in myAges:
        ageInfo = age.getChild().upcastToAgeLinkNode().getAgeInfo()
        if ageInfo.getAgeInstanceGuid() == myCurrentAgeInstanceGuid:
            # OK
            print "IsAllowed : Am I in one of my own private age, it's ok."
            return True
    # I am not welcome here, link myself in an allowed age
    print "IsAllowed : I am not welcome here, link myself in an allowed age"
    return False
"""
# IsAllowed Version 2 : 
def IsAllowed():
    #
    infoNode = ptAgeVault().getAgeInfo()
    #infoNode.getAgeFilename()
    #infoNode.getAgeInstanceGuid()
    #infoNode.getAgeInstanceName()
    #infoNode.getAgeSequenceNumber()
    #infoNode.getAgeUserDefinedName()
    msg = "{0} {1} ({2})".format(infoNode.getAgeUserDefinedName(), infoNode.getAgeFilename(), infoNode.getAgeSequenceNumber())
    if infoNode.isPublic():
        print("IsAllowed : {0} is public => I can't stay here as a bot!".format(msg))
        return False
    else:
        print("IsAllowed : {0} is private => OK.".format(msg))
        return True

#
def IsCurrentAgePublic():
    infoNode = ptAgeVault().getAgeInfo()
    if infoNode.isPublic():
        return "This age is Public"
    else:
        return "This age is Private"


# Toggle robot mode
# type [startChar]bot in chat
def ToggleRobotMode(self):
    global amIRobot
    amIRobot = not amIRobot
    if amIRobot:
        if not IsAllowed():
            amIRobot = False
            msg = f"{PtGetLocalPlayer().getPlayerName()} is in a public age and can not stay in robot mode! Returning to human mode."
            PtSendKIMessage(kKILocalChatStatusMsg, msg)
        else:
            msg = f"{PtGetLocalPlayer().getPlayerName()} is in robot mode."
            PtSendKIMessage(kKIChatStatusMsg, msg)
            surveyBot.Start(self)
    else:
        msg = f"{PtGetLocalPlayer().getPlayerName()} is in human mode."
        PtSendKIMessage(kKIChatStatusMsg, msg)
        surveyBot.Stop()

# 
def ToggleBlockCmds(self):
    xPlayerKiCmds.bBlockCmds = not xPlayerKiCmds.bBlockCmds
    msg = f"{PtGetLocalPlayer().getPlayerName()} : Users commands are "
    if xPlayerKiCmds.bBlockCmds:
        msg = f"{msg}LOCKED"
    else:
        msg = f"{msg}UNLOCKED"
    PtSendKIMessage(kKIChatStatusMsg, msg)

bCheckPos = False
# checkPos
def ToggleCheckPos(self):
    global bCheckPos
    bCheckPos = not bCheckPos
    msg = f"{PtGetLocalPlayer().getPlayerName()} : CheckPos is "
    if bCheckPos:
        msg = f"{msg}ON"
        checkPos.Start(self)
    else:
        msg = f"{msg}OFF"
        checkPos.Stop()
    PtSendKIMessage(kKIChatStatusMsg, msg)

# 
def ResetAdminList(self):
    xPlayerKiCmds.adminList = ['32319L', '31420L']
    msg = "Administrators list is reseted."
    #PtSendKIMessage(kKIChatStatusMsg, msg)
    PtSendKIMessage(kKILocalChatStatusMsg, msg)

# 
def AddAdminitrators(self, strArg):
    playerIdList = re.sub("[^\d]", " ",  strArg).split()
    xPlayerKiCmds.adminList.append(playerIdList)
    msg = "Administrators list is uddated."
    #PtSendKIMessage(kKIChatStatusMsg, msg)
    PtSendKIMessage(kKILocalChatStatusMsg, msg)

# Me.ToggleStealth(int en)
# Toggles the visibility and clickability of the avatar.
def ToggleVisibility(en = False):
    if not IsAllowed():
        en = True
    me = PtGetLocalAvatar()
    me.draw.netForce(1)
    me.draw.enable(en)
    PtToggleAvatarClickability(en)

#
def ToggleCheckPlayersArrival(self, strArgs):
    CheckPlayersArrival.isActive = not CheckPlayersArrival.isActive
    #self, player, method=DoNothing, params=[]
    msg = "CheckPlayersArrival is "
    if CheckPlayersArrival.isActive:
        #CheckPlayersArrival.strArgs = strArgs
        CheckPlayersArrival.stringToMethodParams(strArgs)
        msg += "enabled with {}({}).".format(CheckPlayersArrival.function.__name__, CheckPlayersArrival.parameters)
    else:
        CheckPlayersArrival.StopChecking()
        msg += "disabled."
    print(msg)
    #PtSendKIMessage(kKIChatStatusMsg, msg) # Status message net propagated
    PtSendKIMessage(kKILocalChatStatusMsg, msg)

# Pour executer une commande envoyee par le robot lui-meme
# Appele par xKI.py (ligne 6837)
def SetCommand(self, chatmessage):
    # (un)robotify your avatar
    if chatmessage.lower() == "bot":
        ToggleRobotMode(self)
        return None
    
    # (un)lock bot commands for users (but W/ONBOT)
    elif chatmessage.lower() == "lock":
        ToggleBlockCmds(self)
        return None
    
    # start/stop check pos
    elif chatmessage.lower() == "checkpos":
        ToggleCheckPos(self)
        return None
    
    # (un)check player's arrival, optionaly method name, parameters
    elif chatmessage.lower().startswith("check"):
        words = chatmessage.split(" ", 1)
        params = ""
        print("Calling ToggleCheckPlayersArrival {}, taille {}".format(words, len(words)))
        if len(words) > 1:
            params = words[1]
        ToggleCheckPlayersArrival(self, params)
        return None
    
    # toggles your avatar visibility and clickability
    elif chatmessage.lower().startswith("vis "):
        words = chatmessage.split(" ", 1)
        if len(words) > 0:
            #PtSendKIMessage(kKILocalChatStatusMsg, "\"%s\""%(words[1]))
            if int(words[1]) == 0:
               status = False
            else:
                status = True
            ToggleVisibility(status)
        else:
            msg = "vis [1/0]"
            PtSendKIMessage(kKILocalChatStatusMsg, msg)
        return None
    
    # link myself to : [startChar]linkto <short age name> (ex: !linkto fh)
    elif chatmessage.lower().startswith("linkto "):
        words = chatmessage.split(" ", 1)
        if len(words) > 0:
            ageName = words[1]
            LinkToAge(self, ageName)
        else:
            msg = "Please specify the name of the age you want to link."
            PtSendKIMessage(kKILocalChatStatusMsg, msg)
        return None
    
    # link myself to public instance: [startChar]to <age name> (ex: !to city)
    elif chatmessage.lower().startswith("to "):
        words = chatmessage.split(" ", 1)
        if len(words) > 0:
            ageName = words[1]
            LinkToPublicAge(self, ageName)
        else:
            msg = "Please specify the name of the age you want to link."
            PtSendKIMessage(kKILocalChatStatusMsg, msg)
        return None
    
    # Display some player's age infos
    elif chatmessage.lower().startswith("age"):
        words = chatmessage.split(" ", 1)
        if len(words) > 1:
            playerID = words[1].strip()
            GetPlayerAgeInfo(self, playerID)
        else:
            GetPlayerAgeInfo(self)
        return None
    
    # Display the age GUID of a player or yours
    elif chatmessage.lower().startswith("guid"):
        words = chatmessage.split(" ", 1)
        if len(words) > 1:
            playerID = words[1].strip()
            GetPlayerAgeGUID(self, playerID)
        else:
            GetPlayerAgeGUID(self)
        return None
    
    # Display the current bot age infos
    elif chatmessage.lower() == "current":
        msg = xBotAge.ShowCurrentBotAge()
        PtSendKIMessage(kKILocalChatStatusMsg, msg)
        return None
    
    # Display the state of the current age (Public or Private)
    elif chatmessage.lower() == "ispublic":
        msg = IsCurrentAgePublic()
        PtSendKIMessage(kKILocalChatStatusMsg, msg)
        return None
    
    # show scene object name list (all)
    elif chatmessage.lower().startswith("so "):
        words = chatmessage.split(" ", 1)
        if len(words) > 1:
            name = words[1].strip()
            ShowSceneObjects(self, name)
        return None
    
    # show scene object name list (in age)
    elif chatmessage.lower().startswith("soa "):
        words = chatmessage.split(" ", 2)
        if len(words) > 1:
            name = words[1].strip()
            if len(words) > 2:
                age = words[2].strip()
            else:
                age = PtGetAgeInfo().getAgeFilename()
            ShowSceneObjectsInAge(self, name, age)
        return None
    
    # show scene object name list (with coords)
    elif chatmessage.lower().startswith("soc "):
        words = chatmessage.split(" ", 1)
        if len(words) > 1:
            name = words[1].strip()
            ShowSceneObjectsWithCoords(self, name)
        return None
    
    # show scene object name list (with coords)
    elif chatmessage.lower().startswith("soca "):
        words = chatmessage.split(" ", 2)
        if len(words) > 1:
            name = words[1].strip()
            if len(words) > 2:
                age = words[2].strip()
            else:
                age = PtGetAgeInfo().getAgeFilename()
            xBotKiCmds.ShowSceneObjectsInAgeWithCoords(self, name, age)
        return None
    
    # Toggle Jalak buttons
    elif chatmessage.lower() == "jalak":
        PtSendKIMessage(kKILocalChatStatusMsg, "toggle jalak buttons")
        xBotAge.ToggleJalakButtons()
        return None
    
    # Save my position
    elif chatmessage.lower() == "save1":
        xSave.WriteMatrix44(self)
        return None
    
    # Save my position (V2)
    elif chatmessage.lower().startswith("save"):
        words = chatmessage.split(" ", 2)
        PtSendKIMessage(kKILocalChatStatusMsg, str(words))
        if len(words) > 1:
            n = words[1].strip()
            #PtSendKIMessage(kKILocalChatStatusMsg, "n='"+str(n)+"'")
            xSave2.WriteMatrix44(self, n)
        else:
            xSave2.WriteMatrix44(self)
        return None
    
    # Find player id in the vault by his name
    elif chatmessage.lower().startswith("ki "):
        words = chatmessage.split(" ", 1)
        if len(words) > 1:
            name = words[1].strip()
            id = Find.FindPlayerByName(name)
            PtSendKIMessage(kKILocalChatStatusMsg, str(id))
        return None
    
    # Show age players list (excepted myself)
    elif (chatmessage.lower() == "players"):
        joueurs = "["
        for p in PtGetPlayerList():
            joueurs += "["+str(p.getPlayerID())+"L,\""+p.getPlayerName()+"\"],"
        joueurs += "]"
        PtSendKIMessage(kKILocalChatStatusMsg, joueurs)
        return None
    
    # Show how many players are in my age (excepted myself)
    elif (chatmessage.lower() == "count"):
        nb = len(PtGetPlayerList())
        PtSendKIMessage(kKILocalChatStatusMsg, "Joueurs dans mon age : {0}".format(nb))
        return None

    # Return the position of a player in current age
    elif chatmessage.lower().startswith("coord"):
        words = chatmessage.split(" ", 2)
        #PtSendKIMessage(kKILocalChatStatusMsg, str(words))
        if len(words) > 1:
            name = words[1].strip()
            #PtSendKIMessage(kKILocalChatStatusMsg, "n='"+str(n)+"'")
            xBotKiCmds.GetCoord(self, name)
        else:
            xBotKiCmds.GetCoord(self)
        return None
    
    # The following commands must not be used in public ages
    elif IsAllowed():
        # warp to a spawn point defined by a int
        if chatmessage.lower().startswith("sp"):
            words = chatmessage.split(" ", 1)
            if len(words) > 1:
                spNum = words[1].strip()
                WarpToSpawnPoint(self, spNum)
            else:
                WarpToSpawnPoint(self)
            return None
        
        # warp to a scene object position
        elif (chatmessage.lower() == "w" or chatmessage.lower().startswith("w ")):
            words = chatmessage.split(" ", 1)
            if len(words) > 1:
                name = words[1].strip()
                WarpToPlayerOrSceneObject(self, name)
            return None
        
        # Add Cleft
        elif chatmessage.lower() == "addcleft":
            AddCleft(self)
            return None
        
        # Add Hood
        elif chatmessage.lower() == "addhood":
            AddHood(self)
            return None
        
        # Add Relto
        elif chatmessage.lower() == "addrelto":
            AddRelto(self)
            return None
        
        # Load newdesert
        elif chatmessage.lower() == "load":
            xBotKiCmds.LoadNewDesert(self)
            return None
        
        # Disable some panic links
        elif chatmessage.lower() == "nopanic":
            xBotKiCmds.DisablePanicLinks(self)
            return None
        
        # show or hide and/or (en/dis)able physics of an object list (optionnaly in age)
        elif chatmessage.lower().startswith("toggle "):
            chatmessage += "    "
            words = chatmessage.split(" ", 4)
            if len(words) > 4:
                name = words[1].strip()
                age = words[2].strip()
                bDrawOn = words[3].strip()
                bPhysicsOn = words[4].strip()
                if age == "":
                    #age = None
                    age = PtGetAgeInfo().getAgeFilename()
                if bDrawOn == "":
                    bDrawOn = False
                else:
                    try:
                        bDrawOn = bool(int(bDrawOn))
                    except:
                        PtSendKIMessage(kKILocalChatStatusMsg, "Err: the 3rd parameter must be a boolean! (0 = False, 1 = True)")
                        return
                if bPhysicsOn == "":
                    bPhysicsOn = False
                else:
                    try:
                        bPhysicsOn = bool(int(bPhysicsOn))
                    except:
                        PtSendKIMessage(kKILocalChatStatusMsg, "Err: the 4th parameter must be a boolean! (0 = False, 1 = True)")
                        return
                PtSendKIMessage(kKILocalChatStatusMsg, "toggle %s %s %s %s" % (name, age, str(bDrawOn), str(bPhysicsOn)))
                xBotAge.ToggleSceneObjects(name, age, bDrawOn, bPhysicsOn)
            return None
        
        # Return to my last saved position
        elif chatmessage.lower() == "tosaved1":
            PtSendKIMessage(kKILocalChatStatusMsg, "tosaved command found")
            xSave.WarpToSaved(self)
            return None
        
        # Return to my last saved position (V2)
        elif chatmessage.lower().startswith("tosaved"):
            words = chatmessage.split(" ", 2)
            PtSendKIMessage(kKILocalChatStatusMsg, str(words))
            if len(words) > 1:
                n = words[1].strip()
                #PtSendKIMessage(kKILocalChatStatusMsg, "n='"+str(n)+"'")
                xSave2.WarpToSaved(self, n)
            else:
                xSave2.WarpToSaved(self)
            return None
        
        # draw a circle of Firemarbles
        elif chatmessage.lower().startswith("ring "):
            #words = chatmessage.split(" ", 2)
            words = chatmessage.split(" ", 4)
            if len(words) > 3:
                color = words[1].strip()
                bOn = words[2].strip()
                height = words[3].strip()
                dist = words[4].strip()
                PtSendKIMessage(kKILocalChatStatusMsg, "ring " + color + ", " + bOn + ", " + height + ", " + dist)
                xBotKiCmds.Ring(self, color, bOn, height, dist)
            elif len(words) > 3:
                color = words[1].strip()
                bOn = words[2].strip()
                height = words[3].strip()
                PtSendKIMessage(kKILocalChatStatusMsg, "ring " + color + ", " + bOn + ", " + height)
                xBotKiCmds.Ring(self, color, bOn, height)
            elif len(words) > 2:
                color = words[1].strip()
                bOn = words[2].strip()
                PtSendKIMessage(kKILocalChatStatusMsg, "ring " + color + ", " + bOn)
                xBotKiCmds.Ring(self, color, bOn)
            else:
                PtSendKIMessage(kKILocalChatStatusMsg, "ring len(words)=" + str(len(words)))
            return None
        
        # init score (hood only)
        elif chatmessage.lower() == "init":
            xScore.InitScore()
            return None
        
        # change le score (hood only)
        elif chatmessage.lower().startswith("score "):
            words = chatmessage.split(" ", 2)
            if len(words) > 2:
                score1 = words[1].strip()
                score2 = words[2].strip()
                PtSendKIMessage(kKILocalChatStatusMsg, "score " + score1 + ", " + score2)
                xScore.SetScore(score1, score2)
            else:
                PtSendKIMessage(kKILocalChatStatusMsg, "score len(words)=" + str(len(words)))
            return None
        
        # deplace le panneau (hood only)
        elif chatmessage.lower().startswith("move "):
            words = chatmessage.split(" ", 4)
            if len(words) > 4:
                x = words[1].strip()
                y = words[2].strip()
                z = words[3].strip()
                rz = words[4].strip()
                PtSendKIMessage(kKILocalChatStatusMsg, "move (>4) " + x + ", " + y + ", " + z + ", " + rz)
                xScore.SetPosScore(x, y, z, rz)
            elif len(words) == 4:
                x = words[1].strip()
                y = words[2].strip()
                z = words[3].strip()
                rz = "0"
                PtSendKIMessage(kKILocalChatStatusMsg, "move (=4) " + x + ", " + y + ", " + z + ", " + rz)
                xScore.SetPosScore(x, y, z, rz)
            elif len(words) == 2:
                x = "58"
                y = "-999"
                z = "991"
                rz = words[1].strip()
                if rz == "":
                    rz = "0"
                PtSendKIMessage(kKILocalChatStatusMsg, "move " + x + ", " + y + ", " + z + ", " + rz)
                xScore.SetPosScore(x, y, z, rz)
            else:
                PtSendKIMessage(kKILocalChatStatusMsg, "move len(words)=" + str(len(words)))
            return None
        
        # (reprise de Michel)
        elif (chatmessage.lower() == "board on"):
            xScore.InitScore()
            xScore.panneauTournant.start(1.0)
            PtSetAlarm(8,xScore.Board("0", "0"), 1)
            return None
        
        # (reprise de Michel)
        elif (chatmessage.lower() == "board off"):
            xScore.panneauTournant.stop()
            return None
        
        # (reprise de Michel)
        elif (chatmessage.lower() == "board"):
            #xScore.InitScoreJ()
            xScore.InitScore()
            PtSetAlarm(8, xScore.Board(xScore.scoreActuel[0], xScore.scoreActuel[1]), 1)
            return None
        
        # Open Bahro Door
        elif (chatmessage.lower() == "open"):
            xBotKiCmds.OpenOrCloseBahroDoor(self, "open")
            return None
        
        # Close Bahro Door
        elif (chatmessage.lower() == "close"):
            xBotKiCmds.OpenOrCloseBahroDoor(self, "close")
            return None
            
        # Set no fog (and black background color)
        elif chatmessage.lower() == "nofog":
            xBotAge.NoFog()
            PtSendKIMessage(kKILocalChatStatusMsg, "nofog done.")
            return None

        # 'night':(ReltoNight,["night [on/off]: To see the Relto by night."]),
        elif chatmessage.lower().startswith("night"):
            words = chatmessage.split(" ", 2)
            #PtSendKIMessage(kKILocalChatStatusMsg, str(words))
            if len(words) > 2:
                scale = words[2].strip()
                try:
                    scale = float(scale)
                except:
                    scale = None
                onoff = words[1].strip()
                xBotKiCmds.ReltoNight(self, onoff, scale)
                PtSendKIMessage(kKILocalChatStatusMsg, "night {} {} done.".format(onoff, scale))
            elif len(words) > 1:
                onoff = words[1].strip()
                xBotKiCmds.ReltoNight(self, onoff)
                PtSendKIMessage(kKILocalChatStatusMsg, "night {} done.".format(onoff))
            else:
                xBotKiCmds.ReltoNight(self, True)
                #PtSendKIMessage(kKILocalChatStatusMsg, "!! len(words)=" + str(len(words)))
                PtSendKIMessage(kKILocalChatStatusMsg, "night True done.")
            return None
            
        # 
        #'day':(ReltoDay,["day [on/off]: Opposite of 'night'."]),
        elif chatmessage.lower().startswith("day"):
            words = chatmessage.split(" ", 1)
            #PtSendKIMessage(kKILocalChatStatusMsg, str(words))
            if len(words) > 1:
                params = words[1].strip()
                xBotKiCmds.ReltoDay(self, params)
                PtSendKIMessage(kKILocalChatStatusMsg, " done.")
            else:
                xBotKiCmds.ReltoDay(self, True)
                #PtSendKIMessage(kKILocalChatStatusMsg, "!! len(words)=" + str(len(words)))
            return None
            
        # 
        #'style':(SetRendererStyle,["style [value] : Changes the \"style\". Where value can be default or an age file name (i.e. city for Ae'gura)"]),
        elif chatmessage.lower().startswith("style"):
            words = chatmessage.split(" ", 1)
            #PtSendKIMessage(kKILocalChatStatusMsg, str(words))
            if len(words) > 1:
                params = words[1].strip()
                xBotKiCmds.SetRendererStyle(self, params)
                PtSendKIMessage(kKILocalChatStatusMsg, " done.")
            else:
                xBotKiCmds.SetRendererStyle(self, "default")
                #PtSendKIMessage(kKILocalChatStatusMsg, "!! len(words)=" + str(len(words)))
            return None
            
        # 
        #'fogshape':(SetRendererFogLinear,["fogshape [start end density]: Changes the \"shape\" of the fog. Where start, end and density are integers."]),
        elif chatmessage.lower().startswith("fogshape"):
            words = chatmessage.split(" ", 1)
            #PtSendKIMessage(kKILocalChatStatusMsg, str(words))
            if len(words) > 1:
                vstart = None
                vend = None
                vdensity = None
                params = words[1].split()
                if len(params) > 0:
                    try:
                        vstart = int(params[0])
                    except:
                        vstart = None
                if len(params) > 1:
                    try:
                        vend = int(params[1])
                    except:
                        vend = None
                if len(params) > 2:
                    try:
                        vdensity = float(params[2])
                    except:
                        vdensity = None
                xBotKiCmds.SetRendererFogLinear(self, vstart, vend, vdensity)
                PtSendKIMessage(kKILocalChatStatusMsg, " done.")
            else:
                xBotKiCmds.SetRendererFogLinear(self, vstart=None, vend=None, vdensity=None)
                #PtSendKIMessage(kKILocalChatStatusMsg, "!! len(words)=" + str(len(words)))
            return None
            
        # 
        #'fogcolor':(SetRendererFogColor,["fogcolor [r v b]: Changes the fog color. Where r, v and b (red, green and blue) are numbers between 0.0 and 1.0."]),
        elif chatmessage.lower().startswith("fogcolor"):
            words = chatmessage.split(" ", 1)
            #PtSendKIMessage(kKILocalChatStatusMsg, str(words))
            if len(words) > 1:
                vr = None
                vg = None
                vb = None
                params = words[1].lower().split()
                if len(params) > 0:
                    try:
                        vr = float(params[0])
                    except:
                        vr = None
                if len(params) > 1:
                    try:
                        vg = float(params[1])
                    except:
                        vg = None
                if len(params) > 2:
                    try:
                        vb = float(params[2])
                    except:
                        vb = None
                xBotKiCmds.SetRendererFogColor(self, vr, vg, vb)
                PtSendKIMessage(kKILocalChatStatusMsg, " done.")
            else:
                xBotKiCmds.SetRendererFogColor(self, vr=None, vg=None, vb=None)
                #PtSendKIMessage(kKILocalChatStatusMsg, "!! len(words)=" + str(len(words)))
            return None
            
        # 
        #'skycolor':(SetRendererClearColor,["skycolor [r v b]: Changes the clear background color. Where r, v and b (red, green and blue) are numbers between 0.0 and 1.0."]),
        elif chatmessage.lower().startswith("skycolor"):
            words = chatmessage.split(" ", 1)
            #PtSendKIMessage(kKILocalChatStatusMsg, str(words))
            if len(words) > 1:
                vr = None
                vg = None
                vb = None
                params = words[1].lower().split()
                if len(params) > 0:
                    PtSendKIMessage(kKILocalChatStatusMsg, "R:{}".format(params[0]))
                    try:
                        vr = float(params[0])
                    except:
                        vr = params[0]
                if len(params) > 1:
                    PtSendKIMessage(kKILocalChatStatusMsg, "V:{}".format(params[1]))
                    try:
                        vg = float(params[1])
                    except:
                        vg = None
                if len(params) > 2:
                    PtSendKIMessage(kKILocalChatStatusMsg, "B:{}".format(params[2]))
                    try:
                        vb = float(params[2])
                    except:
                        vb = None
                xBotKiCmds.SetRendererClearColor(self, vr, vg, vb)
                PtSendKIMessage(kKILocalChatStatusMsg, " done.")
            else:
                xBotKiCmds.SetRendererClearColor(self, vr=None, vg=None, vb=None)
                #PtSendKIMessage(kKILocalChatStatusMsg, "!! len(words)=" + str(len(words)))
            return None

        # 
        #'sky':(SkyOnOff,["sky [on/off]: Adds or removes the sky layers."]),
        elif chatmessage.lower().startswith("sky"):
            words = chatmessage.split(" ", 2)
            #PtSendKIMessage(kKILocalChatStatusMsg, str(words))
            if len(words) > 1:
                params = words[1].strip()
                xBotKiCmds.SkyOnOff(self, params)
                PtSendKIMessage(kKILocalChatStatusMsg, " done.")
            else:
                xBotKiCmds.SkyOnOff(self, True)
                #PtSendKIMessage(kKILocalChatStatusMsg, "!! len(words)=" + str(len(words)))
            return None
            
        # 
        #'nosky':(DisableSky,["Disables the sky."]),        
        elif chatmessage.lower().startswith("nosky"):
            words = chatmessage.split(" ", 2)
            #PtSendKIMessage(kKILocalChatStatusMsg, str(words))
            if len(words) > 1:
                params = words[1].strip()
                xBotKiCmds.DisableSky(self, params)
                PtSendKIMessage(kKILocalChatStatusMsg, " done.")
            else:
                xBotKiCmds.DisableSky(self, False)
                #PtSendKIMessage(kKILocalChatStatusMsg, "!! len(words)=" + str(len(words)))
            return None

        # 
        #'dust':(DustOnOff,["dust [on/off]: Adds or removes the dust layers."]),
        elif chatmessage.lower().startswith("dust"):
            words = chatmessage.split(" ", 2)
            #PtSendKIMessage(kKILocalChatStatusMsg, str(words))
            if len(words) > 1:
                params = words[1].strip()
                xBotKiCmds.DustOnOff(self, params)
                PtSendKIMessage(kKILocalChatStatusMsg, " done.")
            else:
                xBotKiCmds.DustOnOff(self, True)
                #PtSendKIMessage(kKILocalChatStatusMsg, "!! len(words)=" + str(len(words)))
            return None
            
        #'nodust':(DisableDust,["Disables the dust."]),        
        elif chatmessage.lower().startswith("nodust"):
            words = chatmessage.split(" ", 2)
            #PtSendKIMessage(kKILocalChatStatusMsg, str(words))
            if len(words) > 1:
                params = words[1].strip()
                xBotKiCmds.DisableDust(self, params)
                PtSendKIMessage(kKILocalChatStatusMsg, " done.")
            else:
                xBotKiCmds.DisableDust(self, False)
                #PtSendKIMessage(kKILocalChatStatusMsg, "!! len(words)=" + str(len(words)))
            return None
            
        #'linkall <age name>' :        
        elif chatmessage.lower().startswith("linkall"):
            words = chatmessage.split(" ", 1)
            if len(words) > 1:
                PtSendKIMessage(kKILocalChatStatusMsg, "{0}, {1}, {2}".format(words, len(words), words[1].strip()))
                params = words[1].strip()
                msg = xBotAge.LinkAll(self, params)
                PtSendKIMessage(kKILocalChatStatusMsg, msg)
            else:
                PtSendKIMessage(kKILocalChatStatusMsg, "{0}!! len(words)={1}".format(words, len(words)))
            return None
            
        #'warpall' or 'warpall <object name>' :        
        elif chatmessage.lower().startswith("warpall"):
            print("warpall")
            words = chatmessage.split(" ", 1)
            #PtSendKIMessage(kKILocalChatStatusMsg, str(words))
            #print "{0}, {1}, {2}".format(words, len(words), words[1].strip())
            #PtSendKIMessage(kKILocalChatStatusMsg, "{0}, {1}, {2}".format(words, len(words), words[1].strip()))
            print("{0}, {1}".format(words, len(words)))
            #PtSendKIMessage(kKILocalChatStatusMsg, "{0}, {1}".format(words, len(words)))
            if len(words) > 1:
                params = words[1].strip()
                msg = xBotAge.WarpAll(params)
                msg = " done"
                PtSendKIMessage(kKILocalChatStatusMsg, msg)
            else:
                #PtSendKIMessage(kKILocalChatStatusMsg, "{0}!! len(words)={1}".format(words, len(words)))
                msg = xBotAge.WarpAll()
                msg = " done"
                PtSendKIMessage(kKILocalChatStatusMsg, msg)
            return None

        #'hideall <on|off>' :        
        elif chatmessage.lower().startswith("hideall"):
            print("hidepall")
            words = chatmessage.split(" ", 2)
            print("{0}, {1}".format(words, len(words)))
            PtSendKIMessage(kKILocalChatStatusMsg, "{0}, {1}".format(words, len(words)))
            bOn = False
            if len(words) > 1:
                params = words[1].strip()
                if params == "off":
                    bOn = True
            agePlayers = PtGetPlayerList()
            for player in agePlayers:
                avatar = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
                avatar.draw.netForce(1)
                avatar.draw.enable(bOn)
            msg = "hideall done"
            PtSendKIMessage(kKILocalChatStatusMsg, msg)
            return None
        #

        #--> Tu peux ajouter les commandes que tu veux ici
        """
        #Exemple de commande sans parametre
        # dans le chat ton robot ecrit "!maCommande"
        # Appellera la fonction maFonction_1 du module monModule (doit etre defini dans ./xRobot/__init__.py)
        # rmq.: self permet d'acceder aux fonction de la classe xKI de xKI.py
        if chatmessage.lower() == "macommande":
            monModule.maFonction_1(self)
            return None
        #Exemple de commande avec des parametres
        # dans le chat ton robot ecrit "!maCommande param1 param2 ... paramN"
        # Appellera la fonction maFonction du module monModule (doit etre defini dans ./xRobot/__init__.py)
        # rmq.: self permet d'acceder aux fonction de la classe xKI de xKI.py
        if chatmessage.lower().startswith("macommande "):
            #decoupage au niveau des espaces (tu peux choisir un autre seperateur)
            params = chatmessage.split(" ")
            #test si on a assez de parametres
            if len(words) > nombreDeParametres:
                monModule.maFonction_2(self, params[0], params[1], ..., params[N])
            else:
                msg = "Il manque des parametres!"
                PtSendKIMessage(kKILocalChatStatusMsg, msg)
            return None
        """
    else:
        #Commande inconnue
        msg = "I don't know how to \"" + chatmessage.lower() + "\""
        PtSendKIMessage(kKILocalChatStatusMsg, msg)

