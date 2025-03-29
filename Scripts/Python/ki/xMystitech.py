# -*- coding: utf-8 -*-
"""
# xMystitech.py : To use the mystitech commands in the chat.
# From mystitech.py (edit: 2018-08-04 by Cesare)
# Update 2018-11-18 from edit 2018-11-17 by Cesare
# Update 2020-09-10 from edit 2020-04-14 or 2020-05-08 by Cesare
# Update 2023-11-16
"""

from Plasma import *
from . import xBoat
import Shroomie
import Avatars

# Find the KI number of a player you know his exact name (case insensitive)
def FindPlayerByName(playerName):
    tempNode = ptVaultPlayerInfoNode()
    tempNode.playerSetName(playerName)
    try:
        vault = ptVault()
        playerID = vault.findNode(tempNode).upcastToPlayerInfoNode().playerGetID()
    except:
        playerID = 0
    return playerID

# Find the KI number of a player you know his ID
def FindPlayerById(playerId):
    tempNode = ptVaultPlayerInfoNode()
    tempNode.playerSetID(playerId)
    try:
        vault = ptVault()
        playerID = vault.findNode(tempNode).upcastToPlayerInfoNode().playerGetID()
    except:
        playerID = 0
    return playerID

# Get the KI of a player knowing his name / verify kiNumOrName is a long integer
def GetKiNumber(kiNumOrName):
    kiNum = 0
    if isinstance(kiNumOrName, str):
        kiNum = FindPlayerByName(kiNumOrName)
    if kiNum == 0:
        try:
            kiNum = int(kiNumOrName)
            kiNum = FindPlayerById(kiNum)
        except ValueError:
            pass
    return kiNum

# Get the avatar's scene object
def GetAvatarSceneObject(kiNumOrName):
    kiNum = GetKiNumber(kiNumOrName)
    avKey = PtGetAvatarKeyFromClientID(kiNum)
    if isinstance(avKey, ptKey):
        return avKey.getSceneObject()
    else:
        return None

# To modify the coordinates but not the orientation
def SetMat(mat, x, y, z):
    mt = ptMatrix44()
    matTrans = mat.getTranspose(mt)
    t = matTrans.getData()
    t2 = t[0], t[1], t[2], (x, y, z, 1.0)
    mt.setData(t2)
    newMat = mt.getTranspose(ptMatrix44())
    return newMat

# Move a player to an absolute position without modifying the orientation
def WarpPlayerToXyz(kiNumOrName, x, y, z):
    if kiNumOrName is None:
        soAvatar = PtGetLocalAvatar()
    else:
        soAvatar = GetAvatarSceneObject(kiNumOrName)
    if not isinstance(soAvatar, ptSceneobject):
        return None
    mpos = soAvatar.getLocalToWorld()
    try:
        x = float(x)
        y = float(y)
        z = float(z)
        m = SetMat(mpos, x, y, z)
        soAvatar.netForce(True)
        #soAvatar.physics.disable()
        soAvatar.physics.warp(m)
        return soAvatar
    except ValueError:
        return None

""" Methods to change your avatar gender or into NPC """

# AVATAR CHANGE

# Bahro1, Blake, Cate, DrWatson, Engberg, Kodama, Quab, RandMiller,
# Sutherland, Victor, Yeesha, YeeshaNoGlow, Zandi, Male, Female

# Change your avatar to male
def MaleMe():
    PtChangeAvatar("Male")
    RemoveReltoBook()
    
# Change your avatar to female
def FemaleMe():
    PtChangeAvatar("Female")
    RemoveReltoBook()

# Change your avatar to Bahro
def BahroMe():
    PtChangeAvatar("Bahro1")

# Change your avatar to Yeesha (glow version)
def YeeshaMe():
    PtChangeAvatar("Yeesha")
    RemoveReltoBook()

# Change your avatar to Kodama
def KodamaMe():
    PtChangeAvatar("Kodama")
    RemoveReltoBook()

def EngbergMe():
    PtChangeAvatar("Engberg")
    RemoveReltobook()

def SutherMe():
    PtChangeAvatar("Sutherland")
    RemoveReltobook()

def VictorMe():
    PtChangeAvatar("Victor")
    RemoveReltobook()

def WatsonMe():
    PtChangeAvatar("DrWatson")
    RemoveReltobook()

def ZandiMe():
    PtChangeAvatar("Zandi")
    RemoveReltobook()

## Change your avatar to Sharper (He does not exist)
#def SharperMe():
#    PtChangeAvatar("Sharper")
#    removeReltobook()

# Turn your avatar into Male, Female or NPC :
# Bahro1, Blake, Cate, DrWatson, Engberg, Kodama, RandMiller,
# Sutherland, Victor, Yeesha, YeeshaNoGlow, Zandi
# /!\ Quab : Do not try to become a Quab, you will crash and corrupt your avatar!
# For the Yeesha's versions, you can type "glow" or "noglow"
def Change(name):
    name = name.lower()
    if name.startswith("m"):
        name = "Male"
    elif name.startswith("f"):
        name = "Female"
    elif name.startswith("ba"):
        name = "Bahro1"
    elif name.startswith("bl"):
        name = "Blake"
    elif name.startswith("c"):
        name = "Cate"
    elif name.startswith("d") or name.startswith("w"):
        name = "DrWatson"
    elif name.startswith("e"):
        name = "Engberg"
    elif name.startswith("k"):
        name = "Kodama"
    elif name.startswith("r"):
        name = "RandMiller"
    elif name.startswith("s"):
        name = "Sutherland"
    elif name.startswith("v"):
        name = "Victor"
    elif name.startswith("y") or name.endswith("glow"):
        if name.endswith("noglow"):
            name = "YeeshaNoGlow"
        else:
            name = "Yeesha"
    elif name.startswith("z"):
        name = "Zandi"
    PtChangeAvatar(name)
    try:
        RemoveReltoBook()
    except:
        pass

""" Methods to change my size, in TLA we use it for bahro """

def Shorty():
    Avatars.ChangeSize(1.3, "me")

def BabyBahro():
    Avatars.ChangeSize(0.5, "me")

def YoungBahro():
    Avatars.ChangeSize(0.7, "me")

def AdultBahro():
    Avatars.ChangeSize(2, "me")


""" Methods to add or remove avatar's clothin item like Relto book, KI, helmet, ... """

def WearClothingItem(outfitName, prefix="", kiNumOrName=None):
    #name = f"{prefix}{('M', 'F')[PtGetLocalAvatar().avatar.getAvatarClothingGroup()]}{outfitName}"
    #PtGetLocalAvatar().avatar.wearClothingItem(name)
    if kiNumOrName is None:
        #so = PtGetLocalAvatar()
        name = f"{prefix}{('M', 'F')[PtGetLocalAvatar().avatar.getAvatarClothingGroup()]}{outfitName}"
        PtGetLocalAvatar().avatar.wearClothingItem(name)
    else:
        so = GetAvatarSceneObject(kiNumOrName)
        if not isinstance(so, ptSceneobject):
            return
        so.netForce(True) # so the camera operator can see the effect
        name = f"{prefix}{('M', 'F')[so.avatar.getAvatarClothingGroup()]}{outfitName}"
        so.avatar.wearClothingItem(name)

def RemoveClothingItem(outfitName, prefix="", kiNumOrName=None):
    #name = f"{prefix}{('M', 'F')[PtGetLocalAvatar().avatar.getAvatarClothingGroup()]}{outfitName}"
    #PtGetLocalAvatar().avatar.removeClothingItem(name)
    if kiNumOrName is None:
        #so = PtGetLocalAvatar()
        name = f"{prefix}{('M', 'F')[PtGetLocalAvatar().avatar.getAvatarClothingGroup()]}{outfitName}"
        PtGetLocalAvatar().avatar.removeClothingItem(name)
    else:
        so = GetAvatarSceneObject(kiNumOrName)
        if not isinstance(so, ptSceneobject):
            return
        so.netForce(True) # so the camera operator can see the effect
        name = f"{prefix}{('M', 'F')[so.avatar.getAvatarClothingGroup()]}{outfitName}"
        so.avatar.removeClothingItem(name)

# Remove your Relto book
def RemoveReltoBook():
    #name = ("M", "F")[PtGetLocalAvatar().avatar.getAvatarClothingGroup()] + "AccPlayerBook"
    #PtGetLocalAvatar().avatar.removeClothingItem(name)
    RemoveClothingItem(outfitName="AccPlayerBook")

# Wear your Relto book
def WearReltoBook():
    #name = ("M", "F")[PtGetLocalAvatar().avatar.getAvatarClothingGroup()] + "AccPlayerBook"
    #PtGetLocalAvatar().avatar.wearClothingItem(name)
    WearClothingItem(outfitName="AccPlayerBook")

# Remove your KI
def RemoveKI():
    #name = ("M", "F")[PtGetLocalAvatar().avatar.getAvatarClothingGroup()] + "AccKI"
    #PtGetLocalAvatar().avatar.removeClothingItem(name)
    RemoveClothingItem(outfitName="AccKI")

# Wear your KI
def WearKI():
    #name = ("M", "F")[PtGetLocalAvatar().avatar.getAvatarClothingGroup()] + "AccKI"
    #PtGetLocalAvatar().avatar.wearClothingItem(name)
    WearClothingItem(outfitName="AccKI")

def Helmet():
    WearClothingItem(outfitName="HAcc_SuitHelmet", prefix="03_")

def CityGuard():
    outfitNames = [
        "HAcc_DniFace", "Torso_Suit", "RHand_Suit", "LHand_Suit", 
        "Legs_Suit", "RFoot_Suit", "LFoot_Suit"
    ]
    for name in outfitNames:
        WearClothingItem(outfitName=name, prefix="03_")

# Remove your Suit Helmet
def RemoveSuitHelmet():
    #name = ("M", "F")[PtGetLocalAvatar().avatar.getAvatarClothingGroup()] + "HAcc_SuitHelmet"
    #PtGetLocalAvatar().avatar.removeClothingItem(name)
    RemoveClothingItem(outfitName="HAcc_SuitHelmet")

# Wear your Suit Helmet
def WearSuitHelmet():
    #name = ("M", "F")[PtGetLocalAvatar().avatar.getAvatarClothingGroup()] + "HAcc_SuitHelmet"
    #PtGetLocalAvatar().avatar.wearClothingItem(name)
    WearClothingItem(outfitName="HAcc_SuitHelmet")

# Remove other player Relto book knowing his name or KI number
def RemoveOtherRelto(kiNumOrName):
    #x = GetAvatarSceneObject(kiNumOrName)
    #if not isinstance(x, ptSceneobject):
    #    return
    #x.netForce(True) # so the camera operator can see the effect
    #name = ("M", "F")[x.avatar.getAvatarClothingGroup()] + "AccPlayerBook"
    #x.avatar.removeClothingItem(name)
    RemoveClothingItem(outfitName="AccPlayerBook", kiNumOrName=kiNumOrName)

# Wear other player Relto book knowing his name or KI number
def WearOtherRelto(kiNumOrName):
    #x = GetAvatarSceneObject(kiNumOrName)
    #if not isinstance(x, ptSceneobject):
    #    return
    #x.netForce(True) # so the camera operator can see the effect
    #name = ("M", "F")[x.avatar.getAvatarClothingGroup()] + "AccPlayerBook"
    #x.avatar.wearClothingItem(name)
    WearClothingItem(outfitName="AccPlayerBook", kiNumOrName=kiNumOrName)

# Remove other player KI knowing his name or KI number
def RemoveOtherKI(kiNumOrName):
    #x = GetAvatarSceneObject(kiNumOrName)
    #if not isinstance(x, ptSceneobject):
    #    return
    #x.netForce(True) # so the camera operator can see the effect
    #name = ("M", "F")[x.avatar.getAvatarClothingGroup()] + "AccKI"
    #x.avatar.removeClothingItem(name)
    RemoveClothingItem(outfitName="AccKI", kiNumOrName=kiNumOrName)

# Wear other player KI knowing his name or KI number
def WearOtherKI(kiNumOrName):
    #x = GetAvatarSceneObject(kiNumOrName)
    #if not isinstance(x, ptSceneobject):
    #    return
    #x.netForce(True) # so the camera operator can see the effect
    #name = ("M", "F")[x.avatar.getAvatarClothingGroup()] + "AccKI"
    #x.avatar.wearClothingItem(name)
    WearClothingItem(outfitName="AccKI", kiNumOrName=kiNumOrName)

""" Method to avoid panic """

# Avoid panic link to Relto, warp to the default spawn point instead
def DontPanic():
    PtConsoleNet("Avatar.Spawn.DontPanic", True)

""" Methods to move avatar """

# Link a player in my age knowing his name or KI number
def LinkHere(kiNumOrName):
    kiNum = GetKiNumber(kiNumOrName)
    PtConsoleNet(f"Net.LinkPlayerHere {kiNum}", True)

# Link me in a player's age knowing his name or KI number
def LinkMeThere(kiNumOrName):
    kiNum = GetKiNumber(kiNumOrName)
    PtConsoleNet(f"Net.LinkToPlayersAge {kiNum}", True)

# Move a player to my position (we must be in the same age) knowing his name or KI number
def WarpHere(kiNumOrName):
    soMe = PtGetLocalAvatar()
    soAv = GetAvatarSceneObject(kiNumOrName)
    if not isinstance(soAv, ptSceneobject):
        return
    myPos = soMe.getLocalToWorld()
    soAv.netForce(True)
    soAv.physics.warp(myPos)

# Move me to a player's position (we must be in the same age) knowing his name or KI number
def WarpMeThere(kiNumOrName):
    soMe = PtGetLocalAvatar()
    soAv = GetAvatarSceneObject(kiNumOrName)
    if not isinstance(soAv, ptSceneobject):
        return
    avPos = soAv.getLocalToWorld()
    soMe.netForce(True)
    soMe.physics.warp(avPos)

# Move me to an absolute position (orientation unchanged)
def WarpMeTo(strParams):
    x = 0
    y = 0
    z = 0
    strParams = strParams.replace("  ", " ")
    strParams = strParams.replace("- ", "-")
    params = strParams.split(",")
    args = []
    for param in params:
        param = param.strip()
        if param != "":
            args.extend(param.split(" "))
    if len(args) > 0:
        x = args[0].strip()
    if len(args) > 1:
        y = args[1].strip()
    if len(args) > 2:
        z = args[2].strip()
    WarpPlayerToXyz(None, x, y, z)

""" Methods to add or remove prp """

# Page in the GoMePub 
def PageInGome():
    #PtConsoleNet("Nav.PageInNode GoMePubNew_Default", True)
    PtConsoleNet("Nav.PageInNode GoMePubNew_Alcoves", True)
    PtConsoleNet("Nav.PageInNode GoMePubNew_Entry", True)
    PtConsoleNet("Nav.PageInNode GoMePubNew_GoMeConfRoom", True)
    PtConsoleNet("Nav.PageInNode GoMePubNew_GoMePub", True)
    PtConsoleNet("Nav.PageInNode GoMePubNew_StoreRoom", True)
    WarpPlayerToXyz(None, -0.92, 39.41, 20.00)

# Page out the GoMePub 
def PageOutGome():
    #PtConsoleNet("Nav.PageOutNode GoMePubNew_Default", True)
    PtConsoleNet("Nav.PageOutNode GoMePubNew_Alcoves", True)
    PtConsoleNet("Nav.PageOutNode GoMePubNew_Entry", True)
    PtConsoleNet("Nav.PageOutNode GoMePubNew_GoMeConfRoom", True)
    PtConsoleNet("Nav.PageOutNode GoMePubNew_GoMePub", True)
    PtConsoleNet("Nav.PageOutNode GoMePubNew_StoreRoom", True)

# Page in the Secret Room
def PageInRoom():
    PtConsoleNet("Nav.PageInNode Secretroom_Default", True)
    WarpPlayerToXyz(None, -18.89, 2.74, 0.60)

# Page out the Secret Room
def PageOutRoom():
    PtConsoleNet("Nav.PageOutNode Secretroom_Default", True)

# Page in the Alt Secret Room
def PageInAltRoom():
    PtConsoleNet("Nav.PageInNode AltSecretRoom_Default", True)
    WarpPlayerToXyz(None, -18.89, 2.74, 0.60)

# Page out the Alt Secret Room
def PageOutAltRoom():
    PtConsoleNet("Nav.PageOutNode AltSecretRoom_Default", True)
	
# Page in the Mystitech's Cafe
def PageInCafe():
    #PtConsoleNet("Nav.PageInNode MTPCafe_Default", True)
    PtConsoleNet("Nav.PageInNode TLACafe_Default", True)
    WarpPlayerToXyz(None, 46.94, -39.01, 49999.35)

# Page out the Mystitech's Cafe
def PageOutCafe():
    #PtConsoleNet("Nav.PageOutNode MTPCafe_Default", True)
    PtConsoleNet("Nav.PageOutNode TLACafe_Default", True)
	
# Page in the Mystitech's Cafe
def PageInRedCafe():
    PtConsoleNet("Nav.PageInNode TLACafeRed_Default", True)
    WarpPlayerToXyz(None, 46.94, -39.01, 49999.35)

# Page out the Mystitech's Cafe
def PageOutRedCafe():
    PtConsoleNet("Nav.PageOutNode TLACafeRed_Default", True)

# Page in the Mystitech's Office (old version)
def PageInOffice():
    PtConsoleNet("Nav.PageInNode MTPOffice_Default", True)
    WarpPlayerToXyz(None, 22.23, -0.53, 0.00)

# Page out the Mystitech's Office (old version)
def PageOutOffice():
    PtConsoleNet("Nav.PageOutNode MTPOffice_Default", True)

# Page in the Mystitech's Office Red
def PageInOfficeRed():
    PtConsoleNet("Nav.PageInNode TLAOfficeRed_Default", True)
    WarpPlayerToXyz(None, 22.23, -0.53, 0.00)

# Page out the Mystitech's Office Red
def PageOutOfficeRed():
    PtConsoleNet("Nav.PageOutNode TLAOfficeRed_Default", True)

# Page in the Mystitech's TLALoft
def PageInTLALoft():
    PtConsoleNet("Nav.PageInNode TLALoft_Default", True)
    #WarpPlayerToXyz(None, 22.23, -0.53, 0.00)
    WarpPlayerToXyz(None, 492.08, -796.92, 79.00)

# Page out the Mystitech's TLALoft
def PageOutTLALoft():
    PtConsoleNet("Nav.PageOutNode TLALoft_Default", True)

# Page in the Mystitech's TLALoft Edit
def PageInTLALoftEdit():
    PtConsoleNet("Nav.PageInNode TLALoftEdit_Default", True)
    #WarpPlayerToXyz(None, 22.23, -0.53, 0.00)
    WarpPlayerToXyz(None, 492.08, -796.92, 79.00)

# Page out the Mystitech's TLALoft EDit
def PageOutTLALoftEdit():
    PtConsoleNet("Nav.PageOutNode TLALoftEdit_Default", True)

# Page in the Mystitech's TLATestChamber
def PageInTLATestChamber():
    PtConsoleNet("Nav.PageInNode TLATestChamber_Default", True)
    WarpPlayerToXyz(None, -39.00, -3.00, 0.00)

# Page out the Mystitech's TLALoft
def PageOutTLATestChamber():
    PtConsoleNet("Nav.PageOutNode TLATestChamber_Default", True)

# Page in the cityofdimensions Boat
def PageInBoat():
    xBoat.AddCoDBoat()

# Page out the cityofdimensions Boat
def PageOutBoat():
    PtConsoleNet("Nav.PageOutNode cityofdimensions_Boat", True)

# Page in the Mystitech's GameRoom
def PageInGameRoom():
    PtConsoleNet("Nav.PageInNode GameRoom_mainRoom", True)
    WarpPlayerToXyz(None, 211.09, -849.12, 49946.63)

# Page out the Mystitech's GameRoom
def PageOutGameRoom():
    PtConsoleNet("Nav.PageOutNode GameRoom_mainRoom", True)

def GameRoomUp():
    WarpPlayerToXyz(None, 222.37, -801.80, 49980.93)

def GameRoomDown():
    WarpPlayerToXyz(None, 209.41, -854.58, 49946.63)

def PageInMonitor():
    PtConsoleNet("Nav.PageInNode TLABahroRoom_mainRoom", True)
    WarpPlayerToXyz(None, 18.50, 7.33, 15.69)

def PageOutMonitor():     # !! CRASHES THE CLIENT !!
    PtConsoleNet("Avatar.Spawn.Go 2", True)
    PtConsoleNet("Nav.PageOutNode TLABahroRoom_mainRoom", True)

def PageInPlanet():
    PtConsoleNet("Nav.PageInNode TLAPlanet_mainRoom", True)
    WarpPlayerToXyz(None, -109.90, -17.58, 3001.20)

def PageOutPlanet():
    PtConsoleNet("Avatar.Spawn.Go 2", True)
    PtConsoleNet("Nav.PageOutNode TLAPlanet_mainRoom", True)

def MiniPlanet():
    WarpPlayerToXyz(None, 18.08, -145.56, -4962.47)

def BigPlanet():
    WarpPlayerToXyz(None, -109.90, -17.58, 3001.20)

def PageInBasement():
    PtConsoleNet("Nav.PageInNode TLABasement_Default", True)
    WarpPlayerToXyz(None, 4.55, -2.41, -13.04)

def PageOutBasement():
    PtConsoleNet("Avatar.Spawn.Go 2", True)
    PtConsoleNet("Nav.PageOutNode TLABasement_Default", True)

""" Methods for Mintata """

# Hide Minkata ground and dust
def MinkataHide():
    PtFindSceneobject("GroundPlaneVis","Minkata").draw.disable()
    PtFindSceneobject("DustPlaneParticle01","Minkata").draw.disable()
    PtFindSceneobject("DustPlaneParticle02","Minkata").draw.disable()
    PtFindSceneobject("DustPlaneParticle03","Minkata").draw.disable()
    PtFindSceneobject("DustPlaneParticle04","Minkata").draw.disable()
    PtFindSceneobject("DustPlaneParticle05","Minkata").draw.disable()
    PtFindSceneobject("DustPlaneParticle06","Minkata").draw.disable()
    PtFindSceneobject("DustPlaneParticle07","Minkata").draw.disable()

# Show Minkata ground and dust
def MinkataRestore():
    PtFindSceneobject("GroundPlaneVis","Minkata").draw.enable()
    PtFindSceneobject("DustPlaneParticle01","Minkata").draw.enable()
    PtFindSceneobject("DustPlaneParticle02","Minkata").draw.enable()
    PtFindSceneobject("DustPlaneParticle03","Minkata").draw.enable()
    PtFindSceneobject("DustPlaneParticle04","Minkata").draw.enable()
    PtFindSceneobject("DustPlaneParticle05","Minkata").draw.enable()
    PtFindSceneobject("DustPlaneParticle06","Minkata").draw.enable()
    PtFindSceneobject("DustPlaneParticle07","Minkata").draw.enable()

# To move you to Kiva4
def WarpMeToKiva4():
    WarpPlayerToXyz(None, -883.98, -523.17, 0.12)

# To move you to Kiva soccer ball default position
def WarpMeToKivaBall():
    WarpPlayerToXyz(None, -894.06, -1062.67, -0.03)

""" Methods for camera(wo)man """

# To add a green Screen 
def GreenScreen():
    PtConsoleNet("Graphics.Renderer.SetClearColor 0 0.8 0", True)
    PtConsoleNet("Graphics.Renderer.SetYon 50", True)

# To change the distance of the green screen 
def GreensDist(dist):
    PtConsoleNet("Graphics.Renderer.SetYon {}".format(dist), True)

# Change the "sky" color and distance
def Minkatags():
    PtConsoleNet("Graphics.Renderer.SetClearColor 0 1 1", True)
    PtConsoleNet("Graphics.Renderer.SetYon 50", True)

# CUSTOM EMOTES

# Tap KI
def TapKi():
    PtEmoteAvatar("KITap")

# To talk while seatting
def TalkSeat():
    name = ("Male", "Female")[PtGetLocalAvatar().avatar.getAvatarClothingGroup()] + "Talk"
    PtGetLocalAvatar().avatar.playSimpleAnimation(name)
                        
def KneelLink():
    name = ("Male", "Female")[PtGetLocalAvatar().avatar.getAvatarClothingGroup()] + "FishBookLinkOut"
    PtGetLocalAvatar().avatar.playSimpleAnimation(name)

def BookOffer():
    name = ("Male", "Female")[PtGetLocalAvatar().avatar.getAvatarClothingGroup()] + "BookOffer"
    PtGetLocalAvatar().avatar.playSimpleAnimation(name)

def BookOfferIdle():
    name = ("Male", "Female")[PtGetLocalAvatar().avatar.getAvatarClothingGroup()] + "BookOfferIdle"
    PtGetLocalAvatar().avatar.playSimpleAnimation(name)

# CAMERA SPEED

# To show the locations of the age players 
def ShowLocation():
    PtConsoleNet("Avatar.ShowLocations", True)

# To have a slower camera movement 
def SlowerCamera():
    PtConsoleNet("Camera.UseSpeedOverrides True", True)
    PtConsoleNet("Camera.SetGlobalVelocity 2", True)

# To have a slow camera movement 
def SlowCamera():
    PtConsoleNet("Camera.UseSpeedOverrides True", True)
    PtConsoleNet("Camera.SetGlobalVelocity 4", True)

# To adjust the camera speed to that of walking
def WalkCamera():
    PtConsoleNet("Camera.UseSpeedOverrides True", True)
    PtConsoleNet("Camera.SetGlobalVelocity 8", True)

# To adjust the camera speed
def CameraSpeed(speed):
    PtConsoleNet("Camera.UseSpeedOverrides True", True)
    PtConsoleNet("Camera.SetGlobalVelocity {}".format(speed), True)

# To reset the camera
def ResetCamera():
    PtConsoleNet("Camera.SetFOV 87 70", True)

# To hide your cursor 
def HideCursor():
    PtForceCursorHidden()

# To link a group of players knowing their names or KI numbers (you can mix)
# Usage : linkGroup("xxxx,yyyy")
def LinkGroup(strParams):
    strParams = strParams.replace(", ", ",")
    params = strParams.split(",")
    for kiNumOrName in params:
        playerId = GetKiNumber(kiNumOrName)
        if playerId != 0:
            PtConsoleNet("Net.LinkPlayerHere {}".format(playerId), True)

# UTILITIES

# Toggle blue beam
def ToggleBlueBeam():
    sdl = PtGetAgeSDL()
    sdl["islmGZBeamVis"] = (not sdl["islmGZBeamVis"][0],)

# Show how many people are in the current Age
def PopCount():
    print(1 + len(PtGetPlayerList()), " avatars present")

# Commands to kick out trolls
def KickOut(kiNumOrName):
    playerId = GetKiNumber(kiNumOrName)
    if playerId != 0:
        PtConsoleNet("Net.LinkPlayerToPrevAge {}".format(playerId), True)

# Rotate Ahnonay spheres
def RotAhny(sphere):
    sdl = PtGetAgeSDL()
    if sphere > 0 and sphere < 5 :
        sdl["ahnyCurrentSphere"] = (sphere,)

# Get the GUID of the current Age
def GuidInfo():
    age = ptDniInfoSource()
    print("GUID of this Age: ", age.getAgeGuid())

# Get some info about the current Age
def AgeInfo():
    age = ptDniInfoSource()
    guid = age.getAgeGuid()
    print("GUID of this Age: ", guid)
    PlayerList = PtGetPlayerList()
    idList = map(lambda player:player.getPlayerID(), PlayerList)
    nbavi = 1 + PtGetNumRemotePlayers()
    print(str(nbavi), " avatars present")
    for playerId in idList:
        key = PtGetAvatarKeyFromClientID(playerId)
        name = PtGetClientName(key)
        print("Avatars in this Age: ", str(playerId), name)

# Simple tool for setting SDLs (look in the SDL folder for the values)
def SetSDL(name, value):
    sdl = PtGetAgeSDL()
    sdl[name] = (value,)

# Enable KI-GPS coord
def GetKiGPS():
    import Plasma
    import PlasmaKITypes
    vault = Plasma.ptVault()
    psnlSDL = vault.getPsnlAgeSDL()
    if psnlSDL:
        GPSVar = psnlSDL.findVar('GPSEnabled')
        GPSVar.setBool(1)
        vault.updatePsnlAgeSDL(psnlSDL)

""" Methods to link to specific age instances """

# Visit The Fun House
def ToFunHouse():
    PtConsole("Net.LinkToAgeInstance Neighborhood 33a235b1-9fe0-47f0-a73e-6fbd0044717a")

# Visit The Fun House City (GUID unknown)
#def ToFunCity():
#    PtConsole("Net.LinkToAgeInstance City abee8828-869d-4756-89d3-5b374b518595")

# Visit the Hood of Illusions
def ToIllusions():
    PtConsole("Net.LinkToAgeInstance Neighborhood 3cc44d4b-31e1-4dec-b6e6-4b63c72becc3")

# Following age instances have been created for MystiTech The Lost Art usage
def ToMTGome():
    PtConsole("Net.LinkToAgeInstance GoMePubNew 28a73c56-949c-4327-ad56-7df8753933e6")

def ToKGome():
    PtConsole("Net.LinkToAgeInstance GoMePubNew 19a3b778-fac7-4f2a-8795-316dffd292df")

def ToKWatcher():
    PtConsole("Net.LinkToAgeInstance GreatTreePub 8ff0504c-3433-4b02-ae6c-79b824edb715")

def ToKChiso():
    PtConsole("Net.LinkToAgeInstance ChisoPreniv 28e65caa-f0c5-46c7-ac95-3b2a1dc08b7a")

def ToKVothol():
    PtConsole("Net.LinkToAgeInstance Vothol f3693cc1-c795-4895-94e6-aa40b232e34a")
    
def ToKBavanter():
    PtConsole("Net.LinkToAgeInstance EderBahvahnter 901be94d-b342-468f-8542-53d67572825d")

def ToKElonin():
    PtConsole("Net.LinkToAgeInstance Elonin a6caa200-c138-41d7-b85b-05832d1a501c")

def ToKalamee():
    PtConsole("Net.LinkToAgeInstance Kalamee e679fc83-81a9-4b34-9780-686398491b6b")

def ToKVeelay():
    PtConsole("Net.LinkToAgeInstance VeeTsah 1324bd33-acb3-4faf-b49e-378ab52c4003")

def ToKMemorial():
    PtConsole("Net.LinkToAgeInstance MemorialIsland 6f3aa89d-14b0-46b4-be45-1b389e32db60")

# I can't get shroosummon(type) to work, s.WarpToPlayer("Me") is not
# understood if inside a function. Typing the lines manually should work.
def shroosummon(type):  # type: 1-3
    s = Shroomie.Shroomie()
    s.WarpToPlayer("me")
    s.MakeVisible()
    s.RunBehavior(format(type))

