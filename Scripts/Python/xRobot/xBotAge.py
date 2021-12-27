# -*- coding: utf-8 -*-

from Plasma import *
import os
import SpawnPoints
import ages
import xPlayers

currentBotAge = list()

#Instances publiques:
#city	7e0facea-dae1-4aec-a4ca-e76c05fdcfcf	Ae'gura	7e0facea-dae1-4aec-a4ca-e76c05fdcfcf
#kirel	4cfbe95a-1bb2-4cbc-a6c4-87eb28a2aac1	Kirel	4cfbe95a-1bb2-4cbc-a6c4-87eb28a2aac1
#The Watcher's Pub	The Watcher's Pub	75bdd14e-a525-4283-a5a0-579878f7305a	
#Kveer	Kveer	68e219e0-ee25-4df0-b855-0435584e29e2
#GuildPub-Greeters	GuildPub-Greeters	381fb1ba-20a0-45fd-9bcb-fd5922439d05


#
def ChangerNomAge(newAgeName, playerID=None):
    tempNode = ptVaultPlayerInfoNode()
    if not playerID:
        playerID = PtGetLocalPlayer().getPlayerID()
    try:
        playerID = long(playerID.strip())
    except:
        return None
    tempNode.playerSetID(playerID)
    try:
        vault = ptVault()
        vpin = vault.findNode(tempNode).upcastToPlayerInfoNode()
        vpin.playerSetAgeInstanceName(newAgeName)
    except:
        pass

#
def GetPlayerAgeInfo(playerID=None):
    tempNode = ptVaultPlayerInfoNode()
    if not playerID or playerID == "":
        playerID = PtGetLocalPlayer().getPlayerID()
    else:
        try:
            playerID = long(playerID)
        except:
            return None
    tempNode.playerSetID(playerID)
    try:
        ageInfo = ptVault().findNode(tempNode).upcastToPlayerInfoNode()
        return ageInfo
    except:
        return None

#
def GetPlayerAgeInstanceName(playerID=None):
    ageInfo = GetPlayerAgeInfo(playerID)
    if ageInfo:
        return ageInfo.playerGetAgeInstanceName()
    else:
        return None

#
def GetPlayerAgeGUID(playerID=None):
    ageInfo = GetPlayerAgeInfo(playerID)
    if ageInfo:
        return ageInfo.playerGetAgeGuid()
    else:
        return None

#
def GetBotAge():
    ageInfo = PtGetAgeInfo()
    age = [
    ageInfo.getAgeInstanceName(),
    ageInfo.getAgeFilename(),
    ageInfo.getAgeInstanceGuid(),
    ageInfo.getAgeUserDefinedName(),
    ""]
    return age

#
def ShowCurrentBotAge():
    msg = ""
    if len(currentBotAge) == 0:
        msg = "I don't now where I am!"
        return msg
    if len(currentBotAge) > 0:
        msg  = "Instance: {0}".format(currentBotAge[0]) 
    if len(currentBotAge) > 1:
        msg  += " File: {0}".format(currentBotAge[1]) 
    if len(currentBotAge) > 2:
        msg  += " GUID: {0}".format(currentBotAge[2]) 
    if len(currentBotAge) > 3:
        msg  += " UserDefined: {0}".format(currentBotAge[3]) 
    if len(currentBotAge) > 4:
        msg  += " SP: {0}".format(currentBotAge[4]) 
    return msg

#
def SetBotAgeSP(spName = ""):
    global currentBotAge
    if currentBotAge:
        if len(currentBotAge) > 4:
            currentBotAge[4] = spName

#
def GetSPByAlias(spawnPointAlias=None):
    ageInfo = PtGetAgeInfo()
    ageFileName = ageInfo.getAgeFilename().lower()
    pos = None
    spName = None
    if ageFileName == "city":    
        if spawnPointAlias in SpawnPoints.aliasCitySP.keys():
            spName = SpawnPoints.aliasCitySP[spawnPointAlias]
            so = PtFindSceneobject(spName, PtGetAgeName())
            pos = so.getLocalToWorld()
    elif ageFileName == "minkata":    
        if spawnPointAlias in SpawnPoints.aliasMinkataSP.keys():
            spName = SpawnPoints.aliasMinkataSP[spawnPointAlias]
            try:
                so = PtFindSceneobject(spName, PtGetAgeName())
                pos = so.getLocalToWorld()
            except:
                print "sp minkata : spawnPointAlias={0}, spName={1}".format(spawnPointAlias, spName)
                spName = None
    elif ageFileName == "ercana":    
        if spawnPointAlias in SpawnPoints.aliasErcanaSP.keys():
            spName = SpawnPoints.aliasErcanaSP[spawnPointAlias]
            try:
                so = PtFindSceneobject(spName, PtGetAgeName())
                pos = so.getLocalToWorld()
            except:
                print "sp ercana : spawnPointAlias={0}, spName={1}".format(spawnPointAlias, spName)
                spName = None
    elif ageFileName == "kadish":    
        if spawnPointAlias in SpawnPoints.aliasKadishSP.keys():
            spName = SpawnPoints.aliasKadishSP[spawnPointAlias]
            try:
                so = PtFindSceneobject(spName, PtGetAgeName())
                pos = so.getLocalToWorld()
            except:
                print "sp kadish : spawnPointAlias={0}, spName={1}".format(spawnPointAlias, spName)
                spName = None
    elif ageFileName == "teledahn":    
        if spawnPointAlias in SpawnPoints.aliasTeledahnSP.keys():
            spName = SpawnPoints.aliasTeledahnSP[spawnPointAlias]
            try:
                so = PtFindSceneobject(spName, PtGetAgeName())
                pos = so.getLocalToWorld()
            except:
                print "sp teledahn : spawnPointAlias={0}, spName={1}".format(spawnPointAlias, spName)
                spName = None
    elif ageFileName == "garrison":    
        if spawnPointAlias in SpawnPoints.aliasGarrisonSP.keys():
            spName = SpawnPoints.aliasGarrisonSP[spawnPointAlias]
            try:
                so = PtFindSceneobject(spName, PtGetAgeName())
                pos = so.getLocalToWorld()
            except:
                print "sp gahreesen : spawnPointAlias={0}, spName={1}".format(spawnPointAlias, spName)
                spName = None
    if spName is None or spName == "":
        spName = "Spawn point not found!"
    else:
        spName = "You are warping to " + spName
    return (pos, spName)

#
def GetSpawnPoint(spawnPointNumber=None):
    global currentBotAge
    spawnPt = 'LinkInPointDefault'
    #if len(currentBotAge) < 2:
    currentBotAge = GetBotAge()
    SetBotAgeSP(spawnPt)
    ageFileName = currentBotAge[1]
    if currentBotAge[1] in SpawnPoints.spDict.keys():
        if spawnPointNumber >= 0 and spawnPointNumber < len(SpawnPoints.spDict[currentBotAge[1]]):
            spawnPt = SpawnPoints.spDict[currentBotAge[1]][spawnPointNumber]
            SetBotAgeSP(spawnPt)
    return spawnPt

#
def GetSPCoord(spawnPointNumber=None):
    spName = GetSpawnPoint(spawnPointNumber)
    try:
        so = PtFindSceneobject(spName, PtGetAgeName())
    except NameError:
        so = None
    if isinstance(so, ptSceneobject):
        pos = so.getLocalToWorld()
    else:
        pos = None
    return pos

#
def GetSPName(spawnPointNumber=None):
    spName = GetSpawnPoint(spawnPointNumber)
    if spName == None or spName == "":
        spName = "Spawn point not found!"
    else:
        spName = "You are warping to " + spName
    return spName

#
def LinkPlayerTo(self, age, playerID=None, spawnPointNumber=None):
    if not playerID or playerID == "":
        playerID = PtGetLocalPlayer().getPlayerID()
    else:
        try:
            playerID = long(playerID)
        except:
            return "incorrect playerID"
            #pass
    if len(age) < 3:
        #pass
        return "incorrect age"
    ageInstanceName = age[0]
    ageFileName = age[1]
    ageGuid = age[2]
    ageUserDefinedName = ""
    if len(age) > 3:
        ageUserDefinedName = age[3]
    
    ageLink = ptAgeLinkStruct()
    ageInfo = ptAgeInfoStruct()
    #ageLink.setLinkingRules(PtLinkingRules.kBasicLink)
    ageInfo.setAgeFilename(ageFileName)
    ageInfo.setAgeInstanceGuid(ageGuid)
    ageInfo.setAgeInstanceName(ageInstanceName)
    #ageInfo.setAgeUserDefinedName(ageUserDefinedName)
    #ageInfo.setAgeUserDefinedName("Magical's")
    
    ageLink.setAgeInfo(ageInfo)
    
    spawnPt = "LinkInPointDefault"
    if spawnPointNumber:
        spawnPt = GetSpawnPoint(spawnPointNumber)
    else:
        ageSpawPoint = ""
        if len(age) > 4:
            ageSpawPoint = age[4]
        if ageSpawPoint != "":
            spawnPt = ageSpawPoint
    self.chatMgr.AddChatLine(None, "sp=\""+spawnPt+"\"", 3)
    spawnPoint = ptSpawnPointInfo()
    spawnPoint.setName(spawnPt)
    ageLink.setSpawnPoint(spawnPoint)
   
    ptNetLinkingMgr().linkPlayerToAge(ageLink, playerID)
    return ageUserDefinedName + " " + ageInstanceName

#
AmIRobot = 0

#
def LinkPlayerToPublic(self, linkName, playerID=None):
    global currentBotAge
    linkName = linkName.lower()
    linkName = linkName.replace(" ", "")
    linkName = linkName.replace("'", "")
    linkName = linkName.replace("eder", "")
    link = None
    if (linkName in ages.PublicAgeDict.keys() and not (playerID is None or (playerID == PtGetLocalPlayer().getPlayerID()) and AmIRobot)):
        link = ages.PublicAgeDict[linkName]
    elif (linkName in ages.MirobotAgeDict.keys()):
        link = ages.MirobotAgeDict[linkName]
    elif (linkName in ages.MagicbotAgeDict.keys()):
        link = ages.MagicbotAgeDict[linkName]
    elif (playerID == PtGetLocalPlayer().getPlayerID() and linkName in ages.linkDic.keys()):
        link = ages.linkDic[linkName]
    else:
        return None
    if link:
        if playerID == None:
            currentBotAge = link
            if len(link) > 4:
                SetBotAgeSP(link[4])
        return LinkPlayerTo(self, link, playerID)

#
def GetAgeLinkNode(ageFileName):
    vault = ptVault()
    try:
        myAgesFolder = vault.getAgesIOwnFolder()
        listOfMyAgeLinks = myAgesFolder.getChildNodeRefList()
        for myAgeLinkRef in listOfMyAgeLinks:
            myAgeLink = myAgeLinkRef.getChild()
            myAgeLink = myAgeLink.upcastToAgeLinkNode()
            myAge = myAgeLink.getAgeInfo()
            if type(myAge) != type(None):
                if myAge.getAgeFilename() == ageFileName:
                    return myAgeLink
    except AttributeError:
        PtDebugPrint("xBotAge: error finding age folder", level = kErrorLevel)

#
def SetAgeName(ageFileName, newUserDefinedName):
    myAgeLink = GetAgeLinkNode(ageFileName)
    myAge = myAgeLink.getAgeInfo()
    myAge.setAgeUserDefinedName(newUserDefinedName)
    myAge.save()

#
def GetAgeSpawnPointNames(ageLinkNode):
    spawnPointNames = list()
    spawnPoints = ageLinkNode.getSpawnPoints()
    for spawnLink in spawnPoints:
        spawnPointNames.append(spawnLink.getName())
        #spawnLink.getTitle()
    return spawnPointNames

#
def ViewAgeSpawnPointNames(ageFileName):
    str = ", ".join(GetAgeSpawnPointNames(GetAgeLinkNode(ageFileName)))
    return str

# Find scene objects with name like soName in all loaded districts (aka pages or prp files)
# ex.: soName = "Bahro*Stone" will be transformed in regexp "^.*Bahro.*Stone.*$"
def FindSOName(soName):
    import re
    cond = "^.*" + soName.replace("*", ".*") + ".*$"
    try:
        pattern = re.compile(cond, re.IGNORECASE)
    except:
        return list()
    strList = soName.split("*")
    nameList = list()
    for str in strList:
        nameList.extend(map(lambda so: so.getName(), PtFindSceneobjects(str)))
    nameList = list(set(nameList))
    nameList = filter(lambda x: pattern.match(x) is not None, nameList)
    return nameList

# Find scene objects with name like soName in all loaded districts (Warning, it includes GUI)
def FindSOLike(soName):
    nameList = FindSOName(soName)
    soList = list()
    for soName in nameList:
        sol = PtFindSceneobjects(soName)
        soList.extend(sol)
    return soList

# Find scene objects with name like soName in all loaded districts of the specified age
def FindSOInAge(soName, ageFileName):
    nameList = FindSOName(soName)
    soList = list()
    for soName in nameList:
        try:
            so = PtFindSceneobject(soName, ageFileName)
            soList.append(so)
        except NameError:
            continue
    return soList

#
def FindSOWithCoords(name):
    nameList = FindSOName(name)
    soList = list()
    for soName in nameList:
        try:
            so = PtFindSceneobjects(soName)
            pos = so[0].position()
            if pos.getX() != 0.0 or pos.getY() != 0.0 or pos.getZ() != 0.0:
                soList.append(so[0])
        except:
            continue
    return soList

# Find scene objects with name like soName in all loaded districts of the specified age, and with coordinates
def FindSOInAgeWithCoords(soName, ageFileName):
    sol = FindSOWithCoords(soName)
    soList = list()
    for so in sol:
        pos = so.position()
        if pos.getX() != 0.0 or pos.getY() != 0.0 or pos.getZ() != 0.0:
            soList.append(so)
    return soList

# Retourne le premier objet trouve ayant des coordonnees
def GetFirstSoWithCoord(name):
    nameList = FindSOName(name)
    for soName in nameList:
        try:
            sol = PtFindSceneobjects(soName)
            for so in sol:
                pos = so.position()
                if pos.getX() != 0.0 or pos.getY() != 0.0 or pos.getZ() != 0.0:
                    return so
        except:
            continue
    return None

#
def ShowSOWithCoords(name):
    soNames = ""
    if len(name.replace('*', '')) < 3:
        soNames = "Please use more than 3 letters ('*' are not taken into account)" 
    else:
        soList = FindSOWithCoords(name)
        for so in soList:
            soNames += so.getName() + ", "
        if len(soNames) > 2:
            soNames = soNames[:len(soNames) - 2]
        else:
            soNames = "no sceneobject like \"" + name + "\" found. Try something like \"Bahro*Roof\" in city."
    return soNames

# Show the list of scene objects with name like soName in all loaded districts (Warning, it includes GUI)
def ShowSOWithNameLike(name):
    soList = FindSOLike(name)
    soNames = ""
    for so in soList:
        soNames += so.getName() + ", "
    if len(soNames) > 2:
        soNames = soNames[:len(soNames) - 2]
    else:
        soNames = "no sceneobject like \"" + name + "\" found."
    return soNames

# Show the list of scene objects with name like soName in all loaded districts of the specified age
def ShowSOWithNameLikeInAge(name, age):
    soList = FindSOInAge(name, age)
    soNames = ""
    for so in soList:
        soNames += so.getName() + ", "
    if len(soNames) > 2:
        soNames = soNames[:len(soNames) - 2]
    else:
        soNames = "no sceneobject like \"" + name + "\" found."
    return soNames

# Show the list of scene objects with name like soName in all loaded districts of the specified age
def ShowSOWithNameLikeInAgeWithCoords(name, age):
    soList = FindSOInAgeWithCoords(name, age)
    soNames = ""
    for so in soList:
        soNames += so.getName() + ", "
    if len(soNames) > 2:
        soNames = soNames[:len(soNames) - 2]
    else:
        soNames = "no sceneobject like \"" + name + "\" with coords in " + age + " found."
    return soNames

#

def SetFileName(objectName=""):
    ageFileName = PtGetAgeInfo().getAgeFilename()
    if not os.path.exists("Objects"):
        os.mkdir("Objects")
    fileName = "Objects/" + objectName + "_" + ageFileName + ".txt"
    return fileName

#
def SaveSOWithCoords(name):
    soNames = ShowSOWithCoords(name)
    fileName = SetFileName(name)
    try:
        file = open(fileName, "w")
        file.write(soNames)
        file.close()
        return 1
    except:
        print "Error : {0}".format(fileName)
        return 0

#
def ToggleSceneObjects(name, age = None, bDrawOn = True, bPhysicsOn = True):
    soList = None
    if age:
        soList = FindSOInAge(name, age)
    else:
        soList = PtFindSceneobjects(name)
    if soList:
        for so in soList:
            so.netForce(1)
            so.draw.enable(bDrawOn)
            so.physics.enable(bPhysicsOn)

#
soListButtonsJalak = []
soListPositionsJalak = []
bJalakIsOn = 1
isJalakButtonsInit = False

#
def InitJalakButtons():
    global soListButtonsJalak
    global soListPositionsJalak
    global isJalakButtonsInit
    print "InitJalakButtons 1"
    soListButtonsJalak.extend(FindSOInAge("clkDn_", "Jalak"))
    print "InitJalakButtons 2"
    soListButtonsJalak.extend(FindSOInAge("clkUp_", "Jalak"))
    print "InitJalakButtons 3"
    soListButtonsJalak.extend(FindSOInAge("MiniKIJalakIcon", "GUI"))
    print "InitJalakButtons 4"
    soListButtonsJalak.extend(FindSOInAge("JalakButtonsDlgDragBox", "GUI"))
    print "InitJalakButtons 5"
    if soListButtonsJalak:
        for so in soListButtonsJalak:
            print ">> {0}".format(so.getName())
            soListPositionsJalak.append(so.getLocalToWorld())
    
    isJalakButtonsInit = True

#
def ToggleJalakButtons():
    """
        ToggleSceneObjects(name, age, bDrawOn, bPhysicsOn)
        Dans Jalak - jlakArena
            "clkDn_" 00 a 24
            "clkUp_" 00 a 24
        Dans GUI 
            - jalakControlPanel
                "jalak" (jalakAddCubeBtn, ...)
                "Jalak" (JalakButtonsDlgBG, ...)
            - 
    ageSDL = PtGetAgeSDL()
    
    E:\MystOnLineUruLiveAgain\PlClient_Mirphak\Python\jlakField.py (10 hits)
        Line 109: sdlGUILock = "jlakGUIButtonsLocked"
        Line 166:         ageSDL.setFlags(sdlGUILock,1,1)
        Line 174:         ageSDL.sendToClients(sdlGUILock)
        Line 182:         ageSDL.setNotify(self.key,sdlGUILock,0.0)
        Line 195:             ageSDL[sdlGUILock] = (0,)
        Line 198:             boolGUILock = ageSDL[sdlGUILock][0]
        Line 353:         if VARname == sdlGUILock:
        Line 354:             boolGUILock = ageSDL[sdlGUILock][0]
        Line 463:                 ageSDL[sdlGUILock] = (0,)
        Line 470:                         ageSDL[sdlGUILock] = (1,)
    """
    ageFilename = PtGetAgeInfo().getAgeFilename()
    if ageFilename != "Jalak":
        print "You are not in Jalak"
        return 0
    
    global bJalakIsOn
    global soListButtonsJalak
    global soListPositionsJalak
    global isJalakButtonsInit
    if not isJalakButtonsInit:
        InitJalakButtons()
    bJalakIsOn = not bJalakIsOn
    index = 0
    for so in soListButtonsJalak:
        so.netForce(1)
        #so.draw.enable(bJalakIsOn)
        #so.physics.enable(bJalakIsOn)
        if bJalakIsOn:
            so.physics.warp(soListPositionsJalak[index])
        else:
            matTrans = ptMatrix44()
            matTrans.translate(ptVector3(1000.0, 1000.0, -1000.0))
            so.physics.warp(soListPositionsJalak[index] * matTrans)
            #so.physics.warp(ptPoint3(10000, 10000, 10000))
        index = index + 1
    """
    try:
        ageSDL = PtGetAgeSDL()
        sdlGUILock = "jlakGUIButtonsLocked"
        sdlValue = ageSDL[sdlGUILock][0]
    except:
        print "sdl not found"
        return 0
    sdlValue = not sdlValue
    print "sdlValue={}".format(sdlValue)
    try:
        ageSDL[sdlGUILock] = (sdlValue,)
    except:
        print "error while modifying sdl value"
        return 0
    return 0
    """

# First try, I assume that all the panic links contain "Panic" in there names.
def DisablePanicLinks():
    soName = "Panic"
    sol = FindSOLike(soName)
    for so in sol:
        so.netForce(1)
        so.physics.disable()
#
class AlarmDisablePanicLinks:
    def onAlarm(self, context = 0):
        DisablePanicLinks()

#
def NoFog():
    #fy = "Graphics.Renderer.Setyon 10000 "
    fd = "Graphics.Renderer.Fog.SetDefLinear 0 0 0"
    fc = "Graphics.Renderer.Fog.SetDefColor .0 .0 .0"
    cc = "Graphics.Renderer.SetClearColor .0 .0 .0"
    #PtConsoleNet(fy, True)
    PtConsoleNet(fd, True)
    PtConsoleNet(fc, True)
    PtConsoleNet(cc, True)
    ToggleSceneObjects("Fog", age = None, bDrawOn = False, bPhysicsOn = False)

#
def ToggleFog():
    PtConsoleNet("Graphics.SetDebugFlag noFog", True)

# Reads the fni file of an age and returns a list of strings representing the fni settings
def GetFniSettings(ageFilename):
    #self.chatMgr.AddChatLine(None, "> GetFniSettings", 3)
    fileName = "dat/" + ageFilename + ".fni"
    #fniSettings = list()
    dicFniSettings = {
        "fy":"Graphics.Renderer.Setyon 10000",
        "fd":"Graphics.Renderer.Fog.SetDefLinear 0 0 0",
        "fc":"Graphics.Renderer.Fog.SetDefColor .0 .0 .0",
        "cc":"Graphics.Renderer.SetClearColor .0 .0 .0"
    }
    try:
        file = open(fileName, "r")
        content = file.read()
        file.close()
        for strLine in content.split("\n"):
            strLine = strLine.strip(" \t\r")
            if not strLine.startswith("#"):
                #fniSettings.append(strLine)
                if "setyon" in strLine.lower():
                    dicFniSettings["fy"] = strLine
                elif "setdeflinear" in strLine.lower():
                    dicFniSettings["fd"] = strLine
                elif "setdefcolor" in strLine.lower():
                    dicFniSettings["fc"] = strLine
                elif "setclearcolor" in strLine.lower():
                    dicFniSettings["cc"] = strLine
    except:
        # The file does not exist, then use the default dictionary of fni settings
        pass

    return dicFniSettings

# default black fni settings, will containt the last known settings
dicFniSettings = {
    "fy":"Graphics.Renderer.Setyon 10000",
    "fd":"Graphics.Renderer.Fog.SetDefLinear 0 0 0",
    "fc":"Graphics.Renderer.Fog.SetDefColor .0 .0 .0",
    "cc":"Graphics.Renderer.SetClearColor .0 .0 .0",
}

#
def SetRenderer(style = "default", start = None, end = None, density = None, r = None, g = None, b = None, cr = None, cg = None, cb = None):
    print "SetRenderer(style = \"{}\", start = {}, end = {}, density = {}, r = {}, g = {}, b = {}, cr = {}, cg = {}, cb = {})".format(style, start, end, density, r, g, b, cr, cg, cb)
    global dicFniSettings
    #default (see fni settings)
    if style == "default":
        print "default"
        ageFilename = PtGetAgeInfo().getAgeFilename()
        dicFniSettings = GetFniSettings(ageFilename)
    # default values of the current age without fog
    elif style == "nofog":
        print "nofog"
        ageFilename = PtGetAgeInfo().getAgeFilename()
        dicFniSettings = GetFniSettings(ageFilename)
        dicFniSettings["fd"] = "Graphics.Renderer.Fog.SetDefLinear 0 0 0"
    #personalized style without yon
    elif style is None:
        if start is not None and end is not None and density is not None:
            dicFniSettings["fd"] = "Graphics.Renderer.Fog.SetDefLinear %i %i %f" % (start, end, density)
        if r is not None and g is not None and b is not None:
            dicFniSettings["fc"] = "Graphics.Renderer.Fog.SetDefColor %f %f %f" % (r, g, b)
        if cr is not None and cg is not None and cb is not None:
            dicFniSettings["cc"] = "Graphics.Renderer.SetClearColor %f %f %f" % (cr, cg, cb)
    #personalized style with yon
    else:
        print "personalized"
        try:
            yon = int(style)
            dicFniSettings["fy"] = "Graphics.Renderer.Setyon %i" % (yon)
            if start is not None and end is not None and density is not None:
                dicFniSettings["fd"] = "Graphics.Renderer.Fog.SetDefLinear %i %i %f" % (start, end, density)
            if r is not None and g is not None and b is not None:
                dicFniSettings["fc"] = "Graphics.Renderer.Fog.SetDefColor %f %f %f" % (r, g, b)
            if cr is not None and cg is not None and cb is not None:
                dicFniSettings["cc"] = "Graphics.Renderer.SetClearColor %f %f %f" % (cr, cg, cb)
        except:
            #age fni style if style is an ageFilename or black
            dicFniSettings = GetFniSettings(style)
    # 
    for value in dicFniSettings.itervalues():
        PtConsoleNet(value, True)

#
def SetRendererStyle(vstyle = "default"):
    SetRenderer(style = vstyle)

#
def SetRendererFogLinear(vstart = None, vend = None, vdensity = None):
    SetRenderer(style = None, start = vstart, end = vend, density = vdensity)

#
def SetRendererFogColor(vr = None, vg = None, vb = None):
    SetRenderer(style = None, r = vr, g = vg, b = vb)

#
def SetRendererClearColor(vcr = None, vcg = None, vcb = None):
    SetRenderer(style = None, cr = vcr, cg = vcg, cb = vcb)

# =======================================================================================

# 
def LinkAll(self, linkName=""):
    #myself = PtGetLocalPlayer()
    linkName = linkName.lower().replace(" ", "").replace("'", "").replace("eder", "")
    link = None
    if (linkName in ages.PublicAgeDict.keys()):
        link = ages.PublicAgeDict[linkName]
        self.chatMgr.AddChatLine(None, "Age public trouve.", 3)
    elif (linkName in ages.MirobotAgeDict.keys()):
        link = ages.MirobotAgeDict[linkName]
        self.chatMgr.AddChatLine(None, "Age de Mir-o-Bot trouve.", 3)
    elif (linkName in ages.MagicbotAgeDict.keys()):
        link = ages.MagicbotAgeDict[linkName]
        self.chatMgr.AddChatLine(None, "Age magique trouve.", 3)
    elif (linkName in ages.linkDic.keys()):
        link = ages.linkDic[linkName]
        self.chatMgr.AddChatLine(None, "Age de linkDic trouve.", 3)
    else:
        self.chatMgr.AddChatLine(None, "Ages non trouve.", 3)
        return "Age not found"
    if link is not None:
        # Lier tous joueurs dans mon age sauf moi-meme et les robots connus
        self.chatMgr.AddChatLine(None, "Liaison des autres joueurs de l'age.", 3)
        agePlayers = filter(lambda pl: not(pl.getPlayerID() in xPlayers.dicBot.keys()), PtGetPlayerList())
        for player in agePlayers:
            LinkPlayerTo(self, link, playerID=player.getPlayerID(), spawnPointNumber=None)
        # Et me lier. Si je ne suis pas Mir-o-Bot, il se liera par ses propres moyens
        self.chatMgr.AddChatLine(None, "Dois-je me lier aussi? Robot:{}, Public:{}".format(AmIRobot, linkName in ages.PublicAgeDict.keys()), 3)
        #if not (linkName in ages.PublicAgeDict.keys() and AmIRobot):
        # Mmmm, AmIRobot n'est pas mis a jour, en attendant de trouver une solution, je m'interdis les ages publics
        if not (linkName in ages.PublicAgeDict.keys()):
            self.chatMgr.AddChatLine(None, "Liaison de mon avatar.", 3)
            # Supprimer les prp des autres ages pour ne pas planter lors de la liaison. (Jalak, Bugs, City, Relto, Cleft)
            # Meme si je ne m'en sers pas Stone, Michel ou Yoda ont pu les ajouter.
            pages = ["jlakArena", "ItinerantBugCloud", "greatstair", "psnlMYSTII", "Desert", "Cleft", "FemaleCleftDropIn", "MaleCleftDropIn", "clftJCsDesert", "clftJCsChasm"]
            for page in pages:
                PtPageOutNode(page)
            # Enregistrer l'age ou je rend
            currentBotAge = list(link)
            if len(link) > 4:
                SetBotAgeSP(link[4])
                self.chatMgr.AddChatLine(None, ",".join(currentBotAge), 3)
            # Decharger les ages clones
            
            # Liaison
            myPlayerID = PtGetLocalPlayer().getPlayerID()
            LinkPlayerTo(self, link, playerID=myPlayerID, spawnPointNumber=None)
    return "LinkAll to '{0}' done.".format(linkName)

# Warps all players in the age to me or to an object
def WarpAll(where=None):
    #avCentre = PtGetLocalAvatar()
    #mat = avCentre.getLocalToWorld()
    mat = None
    if where is None: #or where not in range(1, 5):
        mat = PtGetLocalAvatar().getLocalToWorld()
    else:
        """
        if where == 1:
            tupPos = ((0.98276501894, 0.184859260917, 0.0, 23.3415126801), (-0.184859260917, 0.98276501894, 0.0, 54.0308570862), (0.0, 0.0, 1.0, -0.0328424945474), (0.0, 0.0, 0.0, 1.0))
        elif where == 2:
            tupPos = ((-0.897078573704, -0.44187015295, 0.0, 649.721862793), (0.44187015295, -0.897078573704, 0.0, -877.984619141), (0.0, 0.0, 1.0, 9445.71386719), (0.0, 0.0, 0.0, 1.0))
        elif where == 3:
            tupPos = ((0.00954949762672, -0.999954581261, 0.0, -102.545890808), (0.999954581261, 0.00954949762672, 0.0, 54.9582672119), (0.0, 0.0, 1.0, 10563.0976562), (0.0, 0.0, 0.0, 1.0))
        elif where == 4:
            tupPos = ((-0.748968303204, 0.662607133389, 0.0, 1560.00488281), (-0.662607133389, -0.748968303204, 0.0, -51.4498291016), (0.0, 0.0, 1.0, 10171.9091797), (0.0, 0.0, 0.0, 1.0))
        elif where == 5:
            tupPos = ((-0.937420606613, -0.3482016325, 0.0, 993.751708984), (0.3482016325, -0.937420606613, 0.0, -455.378509521), (0.0, 0.0, 1.0, 9424.86523438), (0.0, 0.0, 0.0, 1.0))
        mat = ptMatrix44()
        mat.setData(tupPos)
        """
        #objName = "ZandiMobileRegion"
        #ageName = "Cleft"
        #so = PtFindSceneobject(objName, ageName)
        so = GetFirstSoWithCoord(name)
        mat = so.getLocalToWorld()

        #return 0
    
    #recuperer tous les joueurs
    playerList = PtGetPlayerList()
    playerList.append(PtGetLocalPlayer())
    soAvatarList = map(lambda player: PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject(), playerList)
    for soavatar in soAvatarList:
        #faire flotter tout le monde
        soavatar.netForce(1)
        soavatar.physics.disable()
        soavatar.physics.enable(0)
        soavatar.netForce(1)
    for soavatar in soAvatarList:
        #deplacer les gens
        soavatar.physics.warp(mat)
        soavatar.netForce(1)
    for soavatar in soAvatarList:
        #reactiver la physique pour tous
        soavatar.physics.enable(1)
        soavatar.netForce(1)

#
