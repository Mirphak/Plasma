# -*- coding: utf-8 -*-

#Import des modules Plasma (tous ne seront peut-etre pas utiles)
from Plasma import *
#from PlasmaGame import *
#from PlasmaGameConstants import *
#from PlasmaKITypes import *
#from PlasmaVaultConstants import *

# Modules du robot
import sys
import re

from xRobot import *

# Greetings list
greetings = ["shorah", "hi", "hello", "bonjour", "bonsoir", "salut", "hallo", "allo", "privet"]

# Execute a player's command
def Do(self, player, message, cFlags):
    if not IsAllowed():
        # I can't be a bot in this age, so I do nothing
        self.chatMgr.AddChatLine(None, "I can't be a bot in this age, so I do nothing".format(message), 3)
        return
    #ne pas repondre aux robots
    #if (player.getPlayerID() in dicBot.keys()):
    myself = PtGetLocalPlayer()
    #if (player.getPlayerID() in xPlayers.dicBot.keys() and player.getPlayerID() != myself.getPlayerID()):
    #if player.getPlayerID() != myself.getPlayerID():
    #    return

    plist = [player]
    playerName = player.getPlayerName()

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
            msg = U"Shorah " + player.getPlayerName()
        elif nbWords > 1:
            if words[1] in ("morning", "afternoon"):
                msg = U"Shorah " + player.getPlayerName()
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
            nbPlayers = len(filter(lambda pl: not(pl.getPlayerID() in xPlayers.dicBot.keys()), PtGetPlayerList()))
            if nbPlayers == 0:
                msg += ". I'm alone."
            elif nbPlayers == 1:
                msg += ". There is one player with me."
            else:
                msg += ". There is " + str(len(PtGetPlayerList())) + " players with me."
        #msg += "\n Latest commands: 'cms', 'to dakotah', 'night', 'save [n]' and 'ws [n]'."
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
                self.chatMgr.AddChatLine(None, "** Command \"{}\" not found! **".format(message), 3)
                print("** Command \"{}\" not found! **".format(message))
                try:
                    #envoi d'un message d'aide si possible
                    args = [player]
                    cmdName = "help"
                    if len(cmd) > 0:
                        args.append(cmd[0].lower())
                    else:
                        args.append("?")
                    if message.strip() != "" or message.strip() != U"":
                        xPlayerKiCmds.CallMethod(self, cmdName, cFlags, amIRobot, args)
                except Exception as e:
                    self.chatMgr.AddChatLine(None, "** Error in {}, {}, {}: {} **".format(cmdName, player.getPlayerName(), args[1], e), 3)
                    print("** Error in {}, {}, {}: {} **".format(cmdName, player.getPlayerName(), args[1], e))
            else:
                self.chatMgr.AddChatLine(None, "** Command \"{}\" executed. **".format(message), 3)
                print("** Command \"{}\" executed. **".format(message))


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
            if myself.getPlayerID() == 32319L:
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
    if (not amIRobot and playerName != "Mir-o-Bot") or not (linkName in ages.PublicAgeDict.keys()):
        instanceName = xBotAge.LinkPlayerToPublic(self, linkName)
        if instanceName:
            msg = "I'm linking to " + instanceName + " ..."
        else:
            msg = "I don't know where " + linkName + " is!"
    else:
        msg = "I can't go to public!"
    self.chatMgr.AddChatLine(None, msg, 3)

# Write the age guid
def GetPlayerAgeGUID(self, playerID = None):
    guid = xBotAge.GetPlayerAgeGUID(playerID)
    if guid:
        #self.chatMgr.DisplayStatusMessage(guid)
        self.chatMgr.AddChatLine(None, guid, 3)
    else:
        #self.chatMgr.DisplayStatusMessage("age GUID not found")
        self.chatMgr.AddChatLine(None, "Age GUID not found", 3)

# Write some age infos
def GetPlayerAgeInfo(self, playerID = None):
    #try:
    #    playerID = int(playerID)
    #except:
    #    self.chatMgr.AddChatLine(None, "KI number needed!", 3)
    ageInfo = xBotAge.GetPlayerAgeInfo(playerID)
    if ageInfo:
        msg = ageInfo.playerGetAgeInstanceName()
        msg += " " + ageInfo.playerGetAgeGuid()
        self.chatMgr.AddChatLine(None, msg, 3)
    else:
        self.chatMgr.AddChatLine(None, "Age not found", 3)

#
def WarpToSpawnPoint(self, spNum = None):
    xBotKiCmds.WarpToSpawnPoint(self, spNum)

#
def WarpToPlayerOrSceneObject(self, name):
    ret = xBotKiCmds.WarpToPlayer(self, name)
    if ret[0] == 1:
        self.chatMgr.AddChatLine(None, ret[1], 3)
    else:
        ret = xBotKiCmds.WarpToPlayer(self, name)
        if ret[0] == 0:
            ret = xBotKiCmds.WarpToSceneObject(self, name)
        self.chatMgr.AddChatLine(None, ret[1], 3)

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
    #self.chatMgr.AddChatLine(None, "Adding Cleft...", 3)
    #try:
    #    xBotKiCmds.AddCleft()
    #    self.chatMgr.AddChatLine(None, "Cleft added!", 3)
    #except:
    #    self.chatMgr.AddChatLine(None, "Error while adding Cleft.", 3)
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
        print "SurveyBotAge:"
        
    def WhereAmI(self):
        #print "SurveyBotAge:"
        myCurrentAgeInstanceGuid = PtGetAgeInfo().getAgeInstanceGuid()
        # Am I in one of Mir-o-Bot's age?
        for val in ages.MirobotAgeDict.values():
            if val[2] == myCurrentAgeInstanceGuid:
                # I am in a Mir-o-Bot age, it's ok.
                #print "SurveyBotAge:ok mob"
                self._nbTry = 0
                return
        # Am I in one of MagicBot age?
        for val in ages.MagicbotAgeDict.values():
            if val[2] == myCurrentAgeInstanceGuid:
                # I am in a Mir-o-Bot age, it's ok.
                #print "SurveyBotAge:ok magic"
                self._nbTry = 0
                return
        # Am I in one of my own private age?
        myAges = ptVault().getAgesIOwnFolder().getChildNodeRefList()
        for age in myAges:
            ageInfo = age.getChild().upcastToAgeLinkNode().getAgeInfo()
            if ageInfo.getAgeInstanceGuid() == myCurrentAgeInstanceGuid:
                # OK
                #print "SurveyBotAge:ok own"
                self._nbTry = 0
                return
        print "This age is not allowed for the bot: {0}, {1}".format(PtGetAgeInfo().getAgeFilename(), myCurrentAgeInstanceGuid)
        # I am not welcome here, link myself in an allowed age
        if self._xKiSelf is None:
            print "SurveyBotAge:Error: self._xKiSelf is none, quit MOULa"
            PtConsole("App.Quit")
        else:
            self._nbTry += 1
            print "SurveyBotAge:try link (#{})".format(self._nbTry)
            if self._nbTry > 8:
                PtConsole("App.Quit")
            try:
                LinkToPublicAge(self._xKiSelf, "hood")
            except:
                print "SurveyBotAge:error linking"
                PtConsole("App.Quit")
        
    def onAlarm(self, param=1):
        #print "SurveyBotAge:onalarm"
        if not self._running:
            print "SurveyBotAge:not running"
            return
        #print "SurveyBotAge:call WhereAmI"
        self.WhereAmI()
        PtSetAlarm(15, self, 1)
        
    def Start(self, xKiSelf):
        self._xKiSelf = xKiSelf
        if not self._running:
            self._running = True
            print "SurveyBotAge:start"
            self.onAlarm()

    def Stop(self):
        print "SurveyBotAge:stop"
        self._running = False

surveyBot = SurveyBotAge()
#************************************************************************#
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

# Toggle robot mode
# type [startChar]bot in chat
def ToggleRobotMode(self):
    global amIRobot
    amIRobot = not amIRobot
    if amIRobot:
        if not IsAllowed():
            amIRobot = False
        else:
            self.chatMgr.DisplayStatusMessage(PtGetLocalPlayer().getPlayerName() + " is in robot mode.", 1)
            surveyBot.Start(self)
    else:
        self.chatMgr.DisplayStatusMessage(PtGetLocalPlayer().getPlayerName() + " is in human mode.", 1)
        surveyBot.Stop()

# 
def ToggleBlockCmds(self):
    xPlayerKiCmds.bBlockCmds = not xPlayerKiCmds.bBlockCmds
    msg = "Users commands are "
    if xPlayerKiCmds.bBlockCmds:
        msg = msg + "LOCKED"
    else:
        msg = msg + "UNLOCKED"
    self.chatMgr.DisplayStatusMessage(msg, 1)

# 
def ResetAdminList(self):
    xPlayerKiCmds.adminList = ['32319L', '31420L']
    msg = "Administrators list is reseted."
    self.chatMgr.DisplayStatusMessage(msg, 1)

# 
def AddAdminitrators(self, strArg):
    playerIdList = re.sub("[^\d]", " ",  strArg).split()
    xPlayerKiCmds.adminList.append(playerIdList)
    msg = "Administrators list is uddated."
    self.chatMgr.DisplayStatusMessage(msg, 1)

# Me.ToggleStealth(int en)
# Toggles the visibility and clickability of the avatar.
def ToggleVisibility(en = False):
    if not IsAllowed():
        en = True
    me = PtGetLocalAvatar()
    me.draw.netForce(1)
    me.draw.enable(en)
    PtToggleAvatarClickability(en)

# Pour executer une commande envoyee par le robot lui-meme
# Appele par xKI.py (ligne 6837)
def SetCommand(self, chatmessage):
    #if IsAllowed() and :
    # (un)robotify your avatar
    if chatmessage.lower() == "bot":
        ToggleRobotMode(self)
        return None
    # (un)lock bot commands for users (but W/ONBOT)
    if chatmessage.lower() == "lock":
        ToggleBlockCmds(self)
        return None
    # toggles your avatar visibility and clickability
    if chatmessage.lower().startswith("vis "):
        words = chatmessage.split(" ", 1)
        if len(words) > 0:
            #self.chatMgr.AddChatLine(None, "\"%s\""%(words[1]), 3)
            if int(words[1]) == 0:
               status = False
            else:
                status = True
            ToggleVisibility(status)
        else:
            msg = "vis [1/0]"
            self.chatMgr.AddChatLine(None, msg, 3)
        return None
    # link myself to : [startChar]linkto <short age name> (ex: !linkto fh)
    if chatmessage.lower().startswith("linkto "):
        words = chatmessage.split(" ", 1)
        if len(words) > 0:
            ageName = words[1]
            LinkToAge(self, ageName)
        else:
            msg = "Please specify the name of the age you want to link."
            self.chatMgr.AddChatLine(None, msg, 3)
        return None
    # link myself to public instance: [startChar]to <age name> (ex: !to city)
    if chatmessage.lower().startswith("to "):
        words = chatmessage.split(" ", 1)
        if len(words) > 0:
            ageName = words[1]
            LinkToPublicAge(self, ageName)
        else:
            msg = "Please specify the name of the age you want to link."
            self.chatMgr.AddChatLine(None, msg, 3)
        return None
    # Display some player's age infos
    if chatmessage.lower().startswith("age"):
        words = chatmessage.split(" ", 1)
        if len(words) > 1:
            playerID = words[1].strip()
            GetPlayerAgeInfo(self, playerID)
        else:
            GetPlayerAgeInfo(self)
        return None
    # Display the age GUID of a player or yours
    if chatmessage.lower().startswith("guid"):
        words = chatmessage.split(" ", 1)
        if len(words) > 1:
            playerID = words[1].strip()
            GetPlayerAgeGUID(self, playerID)
        else:
            GetPlayerAgeGUID(self)
        return None
    # Display the current bot age infos
    if chatmessage.lower() == "current":
        msg = xBotAge.ShowCurrentBotAge()
        self.chatMgr.AddChatLine(None, msg, 3)
        return None
    # warp to a spawn point defined by a int
    if IsAllowed() and chatmessage.lower().startswith("sp"):
        words = chatmessage.split(" ", 1)
        if len(words) > 1:
            spNum = words[1].strip()
            WarpToSpawnPoint(self, spNum)
        else:
            WarpToSpawnPoint(self)
        return None
    # warp to a scene object position
    if IsAllowed() and (chatmessage.lower() == "w" or chatmessage.lower().startswith("w ")):
        words = chatmessage.split(" ", 1)
        if len(words) > 1:
            name = words[1].strip()
            WarpToPlayerOrSceneObject(self, name)
        return None
    # show scene object name list (all)
    if chatmessage.lower().startswith("so "):
        words = chatmessage.split(" ", 1)
        if len(words) > 1:
            name = words[1].strip()
            ShowSceneObjects(self, name)
        return None
    # show scene object name list (in age)
    if chatmessage.lower().startswith("soa "):
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
    if chatmessage.lower().startswith("soc "):
        words = chatmessage.split(" ", 1)
        if len(words) > 1:
            name = words[1].strip()
            ShowSceneObjectsWithCoords(self, name)
        return None
    # show scene object name list (with coords)
    if chatmessage.lower().startswith("soca "):
        words = chatmessage.split(" ", 2)
        if len(words) > 1:
            name = words[1].strip()
            if len(words) > 2:
                age = words[2].strip()
            else:
                age = PtGetAgeInfo().getAgeFilename()
            xBotKiCmds.ShowSceneObjectsInAgeWithCoords(self, name, age)
        return None
    # Add Cleft
    if IsAllowed() and chatmessage.lower() == "addcleft":
        AddCleft(self)
        return None
    # Add Hood
    if IsAllowed() and chatmessage.lower() == "addhood":
        AddHood(self)
        return None
    # Add Relto
    if IsAllowed() and chatmessage.lower() == "addrelto":
        AddRelto(self)
        return None
    # Load newdesert
    if IsAllowed() and chatmessage.lower() == "load":
        xBotKiCmds.LoadNewDesert(self)
        return None
    # Disable some panic links
    if IsAllowed() and chatmessage.lower() == "nopanic":
        xBotKiCmds.DisablePanicLinks(self)
        return None
    # show or hide and/or (en/dis)able physics of an object list (optionnaly in age)
    if IsAllowed() and chatmessage.lower().startswith("toggle "):
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
                    self.chatMgr.AddChatLine(None, "Err: the 3rd parameter must be a boolean! (0 = False, 1 = True)", 3)
                    return
            if bPhysicsOn == "":
                bPhysicsOn = False
            else:
                try:
                    bPhysicsOn = bool(int(bPhysicsOn))
                except:
                    self.chatMgr.AddChatLine(None, "Err: the 4th parameter must be a boolean! (0 = False, 1 = True)", 3)
                    return
            self.chatMgr.AddChatLine(None, "toggle %s %s %s %s" % (name, age, str(bDrawOn), str(bPhysicsOn)), 3)
            xBotAge.ToggleSceneObjects(name, age, bDrawOn, bPhysicsOn)
        return None
    # Toggle Jalak buttons
    if chatmessage.lower() == "jalak":
        self.chatMgr.AddChatLine(None, "toggle jalak buttons", 3)
        xBotAge.ToggleJalakButtons()
        return None
    # Save my position
    if chatmessage.lower() == "save1":
        xSave.WriteMatrix44(self)
        return None
    # Return to my last saved position
    if IsAllowed() and chatmessage.lower() == "tosaved1":
        self.chatMgr.AddChatLine(None, "tosaved command found", 3)
        xSave.WarpToSaved(self)
        return None
    # Save my position (V2)
    if chatmessage.lower().startswith("save"):
        words = chatmessage.split(" ", 2)
        self.chatMgr.AddChatLine(None, str(words), 3)
        if len(words) > 1:
            n = words[1].strip()
            #self.chatMgr.AddChatLine(None, "n='"+str(n)+"'", 3)
            xSave2.WriteMatrix44(self, n)
        else:
            xSave2.WriteMatrix44(self)
        return None
    # Return to my last saved position (V2)
    if IsAllowed() and chatmessage.lower().startswith("tosaved"):
        words = chatmessage.split(" ", 2)
        self.chatMgr.AddChatLine(None, str(words), 3)
        if len(words) > 1:
            n = words[1].strip()
            #self.chatMgr.AddChatLine(None, "n='"+str(n)+"'", 3)
            xSave2.WarpToSaved(self, n)
        else:
            xSave2.WarpToSaved(self)
        return None
    # draw a circle of Firemarbles
    if IsAllowed() and chatmessage.lower().startswith("ring "):
        #words = chatmessage.split(" ", 2)
        words = chatmessage.split(" ", 4)
        if len(words) > 3:
            color = words[1].strip()
            bOn = words[2].strip()
            height = words[3].strip()
            dist = words[4].strip()
            self.chatMgr.AddChatLine(None, "ring " + color + ", " + bOn + ", " + height + ", " + dist, 3)
            xBotKiCmds.Ring(self, color, bOn, height, dist)
        elif len(words) > 3:
            color = words[1].strip()
            bOn = words[2].strip()
            height = words[3].strip()
            self.chatMgr.AddChatLine(None, "ring " + color + ", " + bOn + ", " + height, 3)
            xBotKiCmds.Ring(self, color, bOn, height)
        elif len(words) > 2:
            color = words[1].strip()
            bOn = words[2].strip()
            self.chatMgr.AddChatLine(None, "ring " + color + ", " + bOn, 3)
            xBotKiCmds.Ring(self, color, bOn)
        else:
            self.chatMgr.AddChatLine(None, "ring len(words)=" + str(len(words)), 3)
        return None
    # Find palyer id in the vault by his name
    if chatmessage.lower().startswith("ki "):
        words = chatmessage.split(" ", 1)
        if len(words) > 1:
            name = words[1].strip()
            id = Find.FindPlayerByName(name)
            self.chatMgr.AddChatLine(None, str(id), 3)
        return None
    # init score (hood only)
    if IsAllowed() and chatmessage.lower() == "init":
        xScore.InitScore()
        return None
    # change le score (hood only)
    if IsAllowed() and chatmessage.lower().startswith("score "):
        words = chatmessage.split(" ", 2)
        if len(words) > 2:
            score1 = words[1].strip()
            score2 = words[2].strip()
            self.chatMgr.AddChatLine(None, "score " + score1 + ", " + score2, 3)
            xScore.SetScore(score1, score2)
        else:
            self.chatMgr.AddChatLine(None, "score len(words)=" + str(len(words)), 3)
        return None
    # deplace le panneau (hood only)
    if IsAllowed() and chatmessage.lower().startswith("move "):
        words = chatmessage.split(" ", 4)
        if len(words) > 4:
            x = words[1].strip()
            y = words[2].strip()
            z = words[3].strip()
            rz = words[4].strip()
            self.chatMgr.AddChatLine(None, "move (>4) " + x + ", " + y + ", " + z + ", " + rz, 3)
            xScore.SetPosScore(x, y, z, rz)
        elif len(words) == 4:
            x = words[1].strip()
            y = words[2].strip()
            z = words[3].strip()
            rz = "0"
            self.chatMgr.AddChatLine(None, "move (=4) " + x + ", " + y + ", " + z + ", " + rz, 3)
            xScore.SetPosScore(x, y, z, rz)
        elif len(words) == 2:
            x = "58"
            y = "-999"
            z = "991"
            rz = words[1].strip()
            if rz == "":
                rz = "0"
            self.chatMgr.AddChatLine(None, "move " + x + ", " + y + ", " + z + ", " + rz, 3)
            xScore.SetPosScore(x, y, z, rz)
        else:
            self.chatMgr.AddChatLine(None, "move len(words)=" + str(len(words)), 3)
        return None
    # (reprise de Michel)
    if IsAllowed() and (chatmessage.lower() == "board on"):
        xScore.InitScore()
        xScore.panneauTournant.start(1.0)
        PtSetAlarm(8,xScore.Board("0", "0"), 1)
        return None
    # (reprise de Michel)
    if IsAllowed() and (chatmessage.lower() == "board off"):
        xScore.panneauTournant.stop()
        return None
    # (reprise de Michel)
    if IsAllowed() and (chatmessage.lower() == "board"):
        #xScore.InitScoreJ()
        xScore.InitScore()
        PtSetAlarm(8, xScore.Board(xScore.scoreActuel[0], xScore.scoreActuel[1]), 1)
        return None
    # Open Bahro Door
    if IsAllowed() and (chatmessage.lower() == "open"):
        xBotKiCmds.OpenOrCloseBahroDoor(self, "open")
        return None
    # Close Bahro Door
    if IsAllowed() and (chatmessage.lower() == "close"):
        xBotKiCmds.OpenOrCloseBahroDoor(self, "close")
        return None
    # Show age players list (excepted myself)
    if (chatmessage.lower() == "players"):
        joueurs = "["
        for p in PtGetPlayerList():
            joueurs += "["+str(p.getPlayerID())+"L,\""+p.getPlayerName()+"\"],"
        joueurs += "]"
        self.chatMgr.AddChatLine(None, joueurs, 3)
        return None
    # Show how many players are in my age (excepted myself)
    if (chatmessage.lower() == "count"):
        nb = len(PtGetPlayerList())
        self.chatMgr.AddChatLine(None, "Joueurs dans mon age : {0}".format(nb), 3)
        return None

    # Return the position of a player in current age
    if chatmessage.lower().startswith("coord"):
        words = chatmessage.split(" ", 2)
        #self.chatMgr.AddChatLine(None, str(words), 3)
        if len(words) > 1:
            name = words[1].strip()
            #self.chatMgr.AddChatLine(None, "n='"+str(n)+"'", 3)
            xBotKiCmds.GetCoord(self, name)
        else:
            xBotKiCmds.GetCoord(self)
        return None
        
    # Set no fog (and black background color)
    if IsAllowed() and chatmessage.lower() == "nofog":
        xBotAge.NoFog()
        self.chatMgr.AddChatLine(None, "nofog done.", 3)
        return None


    # 
    #'night':(ReltoNight,["night [on/off]: To see the Relto by night."]),
    if IsAllowed() and chatmessage.lower().startswith("night"):
        words = chatmessage.split(" ", 2)
        #self.chatMgr.AddChatLine(None, str(words), 3)
        if len(words) > 2:
            scale = words[2].strip()
            try:
                scale = float(scale)
            except:
                scale = None
            onoff = words[1].strip()
            xBotKiCmds.ReltoNight(self, onoff, scale)
            self.chatMgr.AddChatLine(None, "night {} {} done.".format(onoff, scale), 3)
        elif len(words) > 1:
            onoff = words[1].strip()
            xBotKiCmds.ReltoNight(self, onoff)
            self.chatMgr.AddChatLine(None, "night {} done.".format(onoff), 3)
        else:
            xBotKiCmds.ReltoNight(self, True)
            #self.chatMgr.AddChatLine(None, "!! len(words)=" + str(len(words)), 3)
            self.chatMgr.AddChatLine(None, "night True done.", 3)
        return None
        
    # 
    #'day':(ReltoDay,["day [on/off]: Opposite of 'night'."]),
    if chatmessage.lower().startswith("day"):
        words = chatmessage.split(" ", 1)
        #self.chatMgr.AddChatLine(None, str(words), 3)
        if len(words) > 1:
            params = words[1].strip()
            xBotKiCmds.ReltoDay(self, params)
            self.chatMgr.AddChatLine(None, " done.", 3)
        else:
            xBotKiCmds.ReltoDay(self, True)
            #self.chatMgr.AddChatLine(None, "!! len(words)=" + str(len(words)), 3)
        return None
        
    # 
    #'style':(SetRendererStyle,["style [value] : Changes the \"style\". Where value can be default or an age file name (i.e. city for Ae'gura)"]),
    if IsAllowed() and chatmessage.lower().startswith("style"):
        words = chatmessage.split(" ", 1)
        #self.chatMgr.AddChatLine(None, str(words), 3)
        if len(words) > 1:
            params = words[1].strip()
            xBotKiCmds.SetRendererStyle(self, params)
            self.chatMgr.AddChatLine(None, " done.", 3)
        else:
            xBotKiCmds.SetRendererStyle(self, "default")
            #self.chatMgr.AddChatLine(None, "!! len(words)=" + str(len(words)), 3)
        return None
        
    # 
    #'fogshape':(SetRendererFogLinear,["fogshape [start end density]: Changes the \"shape\" of the fog. Where start, end and density are integers."]),
    if IsAllowed() and chatmessage.lower().startswith("fogshape"):
        words = chatmessage.split(" ", 1)
        #self.chatMgr.AddChatLine(None, str(words), 3)
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
            self.chatMgr.AddChatLine(None, " done.", 3)
        else:
            xBotKiCmds.SetRendererFogLinear(self, vstart=None, vend=None, vdensity=None)
            #self.chatMgr.AddChatLine(None, "!! len(words)=" + str(len(words)), 3)
        return None
        
    # 
    #'fogcolor':(SetRendererFogColor,["fogcolor [r v b]: Changes the fog color. Where r, v and b (red, green and blue) are numbers between 0.0 and 1.0."]),
    if IsAllowed() and chatmessage.lower().startswith("fogcolor"):
        words = chatmessage.split(" ", 1)
        #self.chatMgr.AddChatLine(None, str(words), 3)
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
            self.chatMgr.AddChatLine(None, " done.", 3)
        else:
            xBotKiCmds.SetRendererFogColor(self, vr=None, vg=None, vb=None)
            #self.chatMgr.AddChatLine(None, "!! len(words)=" + str(len(words)), 3)
        return None
        
    # 
    #'skycolor':(SetRendererClearColor,["skycolor [r v b]: Changes the clear background color. Where r, v and b (red, green and blue) are numbers between 0.0 and 1.0."]),
    if IsAllowed() and chatmessage.lower().startswith("skycolor"):
        words = chatmessage.split(" ", 1)
        #self.chatMgr.AddChatLine(None, str(words), 3)
        if len(words) > 1:
            vr = None
            vg = None
            vb = None
            params = words[1].lower().split()
            if len(params) > 0:
                self.chatMgr.AddChatLine(None, "R:{}".format(params[0]), 3)
                try:
                    vr = float(params[0])
                except:
                    vr = params[0]
            if len(params) > 1:
                self.chatMgr.AddChatLine(None, "V:{}".format(params[1]), 3)
                try:
                    vg = float(params[1])
                except:
                    vg = None
            if len(params) > 2:
                self.chatMgr.AddChatLine(None, "B:{}".format(params[2]), 3)
                try:
                    vb = float(params[2])
                except:
                    vb = None
            xBotKiCmds.SetRendererClearColor(self, vr, vg, vb)
            self.chatMgr.AddChatLine(None, " done.", 3)
        else:
            xBotKiCmds.SetRendererClearColor(self, vr=None, vg=None, vb=None)
            #self.chatMgr.AddChatLine(None, "!! len(words)=" + str(len(words)), 3)
        return None

    # 
    #'sky':(SkyOnOff,["sky [on/off]: Adds or removes the sky layers."]),
    if IsAllowed() and chatmessage.lower().startswith("sky"):
        words = chatmessage.split(" ", 2)
        #self.chatMgr.AddChatLine(None, str(words), 3)
        if len(words) > 1:
            params = words[1].strip()
            xBotKiCmds.SkyOnOff(self, params)
            self.chatMgr.AddChatLine(None, " done.", 3)
        else:
            xBotKiCmds.SkyOnOff(self, True)
            #self.chatMgr.AddChatLine(None, "!! len(words)=" + str(len(words)), 3)
        return None
        
    # 
    #'nosky':(DisableSky,["Disables the sky."]),        
    if IsAllowed() and chatmessage.lower().startswith("nosky"):
        words = chatmessage.split(" ", 2)
        #self.chatMgr.AddChatLine(None, str(words), 3)
        if len(words) > 1:
            params = words[1].strip()
            xBotKiCmds.DisableSky(self, params)
            self.chatMgr.AddChatLine(None, " done.", 3)
        else:
            xBotKiCmds.DisableSky(self, False)
            #self.chatMgr.AddChatLine(None, "!! len(words)=" + str(len(words)), 3)
        return None

    # 
    #'dust':(DustOnOff,["dust [on/off]: Adds or removes the dust layers."]),
    if IsAllowed() and chatmessage.lower().startswith("dust"):
        words = chatmessage.split(" ", 2)
        #self.chatMgr.AddChatLine(None, str(words), 3)
        if len(words) > 1:
            params = words[1].strip()
            xBotKiCmds.DustOnOff(self, params)
            self.chatMgr.AddChatLine(None, " done.", 3)
        else:
            xBotKiCmds.DustOnOff(self, True)
            #self.chatMgr.AddChatLine(None, "!! len(words)=" + str(len(words)), 3)
        return None
        
    #'nodust':(DisableDust,["Disables the dust."]),        
    if IsAllowed() and chatmessage.lower().startswith("nodust"):
        words = chatmessage.split(" ", 2)
        #self.chatMgr.AddChatLine(None, str(words), 3)
        if len(words) > 1:
            params = words[1].strip()
            xBotKiCmds.DisableDust(self, params)
            self.chatMgr.AddChatLine(None, " done.", 3)
        else:
            xBotKiCmds.DisableDust(self, False)
            #self.chatMgr.AddChatLine(None, "!! len(words)=" + str(len(words)), 3)
        return None
        
    #'linkall <age name>' :        
    if IsAllowed() and chatmessage.lower().startswith("linkall"):
        words = chatmessage.split(" ", 1)
        if len(words) > 1:
            self.chatMgr.AddChatLine(None, "{0}, {1}, {2}".format(words, len(words), words[1].strip()), 3)
            params = words[1].strip()
            msg = xBotAge.LinkAll(self, params)
            self.chatMgr.AddChatLine(None, msg, 3)
        else:
            self.chatMgr.AddChatLine(None, "{0}!! len(words)={1}".format(words, len(words)), 3)
        return None
        
    #'warpall' or 'warpall <object name>' :        
    if IsAllowed() and chatmessage.lower().startswith("warpall"):
        print "warpall"
        words = chatmessage.split(" ", 1)
        #self.chatMgr.AddChatLine(None, str(words), 3)
        #print "{0}, {1}, {2}".format(words, len(words), words[1].strip())
        #self.chatMgr.AddChatLine(None, "{0}, {1}, {2}".format(words, len(words), words[1].strip()), 3)
        print "{0}, {1}".format(words, len(words))
        #self.chatMgr.AddChatLine(None, "{0}, {1}".format(words, len(words)), 3)
        if len(words) > 1:
            params = words[1].strip()
            msg = xBotAge.WarpAll(params)
            msg = " done"
            self.chatMgr.AddChatLine(None, msg, 3)
        else:
            #self.chatMgr.AddChatLine(None, "{0}!! len(words)={1}".format(words, len(words)), 3)
            msg = xBotAge.WarpAll()
            msg = " done"
            self.chatMgr.AddChatLine(None, msg, 3)
        return None

    #'hideall <on|off>' :        
    if IsAllowed() and chatmessage.lower().startswith("hideall"):
        print "hidepall"
        words = chatmessage.split(" ", 2)
        print "{0}, {1}".format(words, len(words))
        self.chatMgr.AddChatLine(None, "{0}, {1}".format(words, len(words)), 3)
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
        self.chatMgr.AddChatLine(None, msg, 3)
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
            self.chatMgr.AddChatLine(None, msg, 3)
        return None
    """
    #Commande inconnue
    msg = "I don't know how to \"" + chatmessage.lower() + "\""
    self.chatMgr.AddChatLine(None, msg, 3)

