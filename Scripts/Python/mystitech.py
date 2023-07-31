# -*- coding: utf-8 -*-
# Last edit: 2023-02-18
 
from Plasma   import *
from Basic    import *
from Kirel    import *
from Boat     import *
import Shroomie
import Avatars

# AVATAR CHANGE

# Bahro1, Blake, Cate, DrWatson, Engberg, Kodama, Quab, RandMiller,
# Sutherland, Victor, Yeesha, YeeshaNoGlow, Zandi, Male, Female

def maleMe():
    PtChangeAvatar("Male")
    removeReltobook()

def femaleMe():
    PtChangeAvatar("Female")
    removeReltobook()

def bahroMe():
    PtChangeAvatar("Bahro1")
    removeReltobook()

def yeeshaMe():
    PtChangeAvatar("Yeesha")
    removeReltobook()

def kodamaMe():
    PtChangeAvatar("Kodama")
    removeReltobook()

def engbergMe():
    PtChangeAvatar("Engberg")
    removeReltobook()

def sutherMe():
    PtChangeAvatar("Sutherland")
    removeReltobook()

def victorMe():
    PtChangeAvatar("Victor")
    removeReltobook()

def watsonMe():
    PtChangeAvatar("DrWatson")
    removeReltobook()

def zandiMe():
    PtChangeAvatar("Zandi")
    removeReltobook()

def sharperMe():
    PtChangeAvatar("Sharper")
    removeReltobook()

def shorty():
    Avatars.ChangeSize(1.3, "me")

def babybahro():
    Avatars.ChangeSize(0.5, "me")

def adultbahro():
    Avatars.ChangeSize(2, "me")

def helmet():
    name = "03_" + ("M", "F")[PtGetLocalAvatar().avatar.getAvatarClothingGroup()] + "HAcc_SuitHelmet"
    PtGetLocalAvatar().avatar.wearClothingItem(name)

def cityguard():
    name = "03_" + ("M", "F")[PtGetLocalAvatar().avatar.getAvatarClothingGroup()] + "HAcc_DniFace"
    PtGetLocalAvatar().avatar.wearClothingItem(name)
    name = "03_" + ("M", "F")[PtGetLocalAvatar().avatar.getAvatarClothingGroup()] + "Torso_Suit"
    PtGetLocalAvatar().avatar.wearClothingItem(name)
    name = "03_" + ("M", "F")[PtGetLocalAvatar().avatar.getAvatarClothingGroup()] + "RHand_Suit"
    PtGetLocalAvatar().avatar.wearClothingItem(name)
    name = "03_" + ("M", "F")[PtGetLocalAvatar().avatar.getAvatarClothingGroup()] + "LHand_Suit"
    PtGetLocalAvatar().avatar.wearClothingItem(name)
    name = "03_" + ("M", "F")[PtGetLocalAvatar().avatar.getAvatarClothingGroup()] + "Legs_Suit"
    PtGetLocalAvatar().avatar.wearClothingItem(name)
    name = "03_" + ("M", "F")[PtGetLocalAvatar().avatar.getAvatarClothingGroup()] + "RFoot_Suit"
    PtGetLocalAvatar().avatar.wearClothingItem(name)
    name = "03_" + ("M", "F")[PtGetLocalAvatar().avatar.getAvatarClothingGroup()] + "LFoot_Suit"
    PtGetLocalAvatar().avatar.wearClothingItem(name)

# RELTO BOOK & KI UN/WEAR

def removeReltobook():
    name = ("M", "F")[PtGetLocalAvatar().avatar.getAvatarClothingGroup()] + "AccPlayerBook"
    PtGetLocalAvatar().avatar.removeClothingItem(name)

def wearReltobook():
    name = ("M", "F")[PtGetLocalAvatar().avatar.getAvatarClothingGroup()] + "AccPlayerBook"
    PtGetLocalAvatar().avatar.wearClothingItem(name)

def removeKI():
    name = ("M", "F")[PtGetLocalAvatar().avatar.getAvatarClothingGroup()] + "AccKI"
    PtGetLocalAvatar().avatar.removeClothingItem(name)
    
def wearKI():
    name = ("M", "F")[PtGetLocalAvatar().avatar.getAvatarClothingGroup()] + "AccKI"
    PtGetLocalAvatar().avatar.wearClothingItem(name)

def removeOtherrelto(kinum):
    y = PtGetAvatarKeyFromClientID(kinum)
    x = y.getSceneObject()
    x.netForce(True) # so the camera operator can see the effect
    name = ("M", "F")[x.avatar.getAvatarClothingGroup()] + "AccPlayerBook"
    x.avatar.removeClothingItem(name)

def wearOtherrelto(kinum):
    y = PtGetAvatarKeyFromClientID(kinum)
    x = y.getSceneObject()
    x.netForce(True) # so the camera operator can see the effect
    name = ("M", "F")[x.avatar.getAvatarClothingGroup()] + "AccPlayerBook"
    x.avatar.wearClothingItem(name)

def removeOtherKI(kinum):
    y = PtGetAvatarKeyFromClientID(kinum)
    x = y.getSceneObject()
    x.netForce(True) # so the camera operator can see the effect
    name = ("M", "F")[x.avatar.getAvatarClothingGroup()] + "AccKI"
    x.avatar.removeClothingItem(name)

def wearOtherKI(kinum):
    y = PtGetAvatarKeyFromClientID(kinum)
    x = y.getSceneObject()
    x.netForce(True) # so the camera operator can see the effect
    name = ("M", "F")[x.avatar.getAvatarClothingGroup()] + "AccKI"
    x.avatar.wearClothingItem(name)

# LINK & WARP FUNCTIONS

def dontpanic():
    PtConsoleNet("Avatar.Spawn.DontPanic", True)

def warpHere(kinum):
    PtConsoleNet("Avatar.Warp.WarpPlayerHere {}".format(kinum), True)

def warpmeThere(kinum):
    PtConsoleNet("Avatar.Warp.WarpToPlayer {}".format(kinum), True)

def linkHere(kinum):
    PtConsoleNet("Net.LinkPlayerHere {}".format(kinum), True)

def linkmeThere(kinum):
    PtConsoleNet("Net.LinkToPlayersAge {}".format(kinum), True)

def showLocation():
    PtConsoleNet("Avatar.ShowLocations", True)

def warpmeTo(x_coord, y_coord, z_coord):
    PtConsoleNet("Avatar.Warp.WarpToXYZ {} {} {}".format(x_coord, y_coord, z_coord), True)

def warpmeTokiva4():
    PtConsoleNet("Avatar.Warp.WarpToXYZ -883.98, -523.17, 0.12", True)

def warpmeTokivaball():
    PtConsoleNet("Avatar.Warp.WarpToXYZ -894.06, -1062.67, -0.03", True)

def toMTGomePub():
    PtConsole("Net.LinkToAgeInstance GoMePubNew 28a73c56-949c-4327-ad56-7df8753933e6")

def toKGomePub():
    PtConsole("Net.LinkToAgeInstance GoMePubNew 19a3b778-fac7-4f2a-8795-316dffd292df")

def toKWatcher():
    PtConsole("Net.LinkToAgeInstance GreatTreePub 8ff0504c-3433-4b02-ae6c-79b824edb715")

def toKChiso():
    PtConsole("Net.LinkToAgeInstance ChisoPreniv 28e65caa-f0c5-46c7-ac95-3b2a1dc08b7a")

def toKVothol():
    PtConsole("Net.LinkToAgeInstance Vothol f3693cc1-c795-4895-94e6-aa40b232e34a")

# CUSTOM LOCATION PAGE-IN

# I can't get shroosummon(type) to work, s.WarpToPlayer("Me") is not
# understood if inside a function. Typing the lines manually should work.
def shroosummon(type):  # type: 1-3
    s = Shroomie.Shroomie()
    s.WarpToPlayer("me")
    s.MakeVisible()
    s.RunBehavior(format(type))

def pageinRoom():
    PtConsoleNet("Nav.PageInNode Secretroom_Default", True)
    PtConsoleNet("Avatar.Warp.WarpToXYZ -18.89, 2.74, 0.60", True)

def pageoutRoom():
    PtConsoleNet("Avatar.Spawn.Go 2", True)
    PtConsoleNet("Nav.PageOutNode Secretroom_Default", True)

def pageinCafeRed():
    PtConsoleNet("Nav.PageInNode TLACafeRed_Default", True)
    PtConsoleNet("Avatar.Warp.WarpToXYZ 46.94, -39.01, 49999.35", True)

def pageoutCafeRed():
    PtConsoleNet("Avatar.Spawn.Go 2", True)
    PtConsoleNet("Nav.PageOutNode TLACafeRed_Default", True)

def pageinCafe():
    PtConsoleNet("Nav.PageInNode TLACafe_Default", True)
    PtConsoleNet("Avatar.Warp.WarpToXYZ 46.94, -39.01, 49999.35", True)

def pageoutCafe():
    PtConsoleNet("Avatar.Spawn.Go 2", True)
    PtConsoleNet("Nav.PageOutNode TLACafe_Default", True)

def pageinCafeOld():
    PtConsoleNet("Nav.PageInNode MTPCafe_Default", True)
    PtConsoleNet("Avatar.Warp.WarpToXYZ 46.94, -39.01, 49999.35", True)

def pageoutCafeOld():
    PtConsoleNet("Avatar.Spawn.Go 2", True)
    PtConsoleNet("Nav.PageOutNode MTPCafe_Default", True)

def pageinOfficeRed():
    PtConsoleNet("Nav.PageInNode TLAOfficeRed_Default", True)
    PtConsoleNet("Avatar.Warp.WarpToXYZ 22.23, -0.53, 0.10", True)

def pageoutOfficeRed():
    PtConsoleNet("Avatar.Spawn.Go 2", True)
    PtConsoleNet("Nav.PageOutNode TLAOfficeRed_Default", True)

def pageinOfficeOld():
    PtConsoleNet("Nav.PageInNode MTPOffice_Default", True)
    PtConsoleNet("Avatar.Warp.WarpToXYZ 22.23, -0.53, 0.10", True)

def pageoutOfficeOld():
    PtConsoleNet("Avatar.Spawn.Go 2", True)
    PtConsoleNet("Nav.PageOutNode MTPOffice_Default", True)

def pageinTlaloft():
    PtConsoleNet("Nav.PageInNode TLALoft_Default", True)
    PtConsoleNet("Avatar.Warp.WarpToXYZ 492.08, -796.92, 79.00", True)

def pageoutTlaloft():
    PtConsoleNet("Avatar.Spawn.Go 2", True)
    PtConsoleNet("Nav.PageOutNode TLALoft_Default", True)

def pageinTlaloftedit():
    PtConsoleNet("Nav.PageInNode TLALoftEdit_Default", True)
    PtConsoleNet("Avatar.Warp.WarpToXYZ 492.08, -796.92, 79.00", True)

def pageoutTlaloftedit():
    PtConsoleNet("Avatar.Spawn.Go 2", True)
    PtConsoleNet("Nav.PageOutNode TLALoftEdit_Default", True)

def pageinAltroom():
    PtConsoleNet("Nav.PageInNode AltSecretRoom_Default", True)
    PtConsoleNet("Avatar.Warp.WarpToXYZ -18.03, -6.22, 0.00", True)

def pageoutAltroom():
    PtConsoleNet("Avatar.Spawn.Go 2", True)
    PtConsoleNet("Nav.PageOutNode AltSecretRoom_Default", True)

def pageinTestroom():
    PtConsoleNet("Nav.PageInNode TLATestChamber_Default", True)
    #PtConsoleNet("Nav.PageInNode TLATestChamber_Textures", True)
    PtConsoleNet("Avatar.Warp.WarpToXYZ -21.44, 4.12, 0.36", True)

def pageoutTestroom():
    PtConsoleNet("Avatar.Spawn.Go 2", True)
    #PtConsoleNet("Nav.PageOutNode TLATestChamber_Textures", True)
    PtConsoleNet("Nav.PageOutNode TLATestChamber_Default", True)

def pageinGameroom():
    PtConsoleNet("Nav.PageInNode GameRoom_mainRoom", True)
    PtConsoleNet("Nav.PageInNode GameRoom_Textures", True)
    PtConsoleNet("Avatar.Warp.WarpToXYZ 222.37, -801.80, 49980.93", True)

def pageoutGameroom():
    PtConsoleNet("Avatar.Spawn.Go 2", True)
    #PtConsoleNet("Nav.PageOutNode GameRoom_Textures", True)
    PtConsoleNet("Nav.PageOutNode GameRoom_mainRoom", True)

def gameroomup():
    PtConsoleNet("Avatar.Warp.WarpToXYZ 222.37, -801.80, 49980.93", True)

def gameroomdown():
    PtConsoleNet("Avatar.Warp.WarpToXYZ 209.41, -854.58, 49946.63", True)

def pageinMonitor():
    PtConsoleNet("Nav.PageInNode TLABahroRoom_mainRoom", True)
    #PtConsoleNet("Nav.PageInNode TLABahroRoom_Textures", True)
    PtConsoleNet("Avatar.Warp.WarpToXYZ 18.50, 7.33, 15.69", True)

def pageoutMonitor():     # !! CRASHES THE CLIENT !!
    PtConsoleNet("Avatar.Spawn.Go 2", True)
    #PtConsoleNet("Nav.PageOutNode TLABahroRoom_Textures", True)
    PtConsoleNet("Nav.PageOutNode TLABahroRoom_mainRoom", True)

def pageinPlanet():
    PtConsoleNet("Nav.PageInNode TLAPlanet_mainRoom", True)
    #PtConsoleNet("Nav.PageInNode TLAPlanet_Textures", True)
    PtConsoleNet("Avatar.Warp.WarpToXYZ -109.90, -17.58, 3001.20", True)

def pageoutPlanet():
    PtConsoleNet("Avatar.Spawn.Go 2", True)
    #PtConsoleNet("Nav.PageOutNode TLAPlanet_Textures", True)
    PtConsoleNet("Nav.PageOutNode TLAPlanet_mainRoom", True)

def miniplanet():
    PtConsoleNet("Avatar.Warp.WarpToXYZ 18.08, -145.56, -4962.47", True)

def bigplanet():
    PtConsoleNet("Avatar.Warp.WarpToXYZ -109.90, -17.58, 3001.20", True)

# NOT NEEDED ANYMORE

def pageinGome():
    PtConsoleNet("Nav.PageInNode GoMePubNew_Alcoves", True)
    PtConsoleNet("Nav.PageInNode GoMePubNew_Entry", True)
    PtConsoleNet("Nav.PageInNode GoMePubNew_GoMeConfRoom", True)
    PtConsoleNet("Nav.PageInNode GoMePubNew_GoMePub", True)
    PtConsoleNet("Nav.PageInNode GoMePubNew_StoreRoom", True)
    #PtConsoleNet("Nav.PageInNode GoMePubNew_Textures", True)
    PtConsoleNet("Avatar.Warp.WarpToXYZ 1.93, 96.17, 19.99", True)

def pageoutGome():
    PtConsoleNet("Avatar.Spawn.Go 2", True)
    #PtConsoleNet("Nav.PageOutNode GoMePubNew_Textures", True)
    PtConsoleNet("Nav.PageOutNode GoMePubNew_StoreRoom", True)
    PtConsoleNet("Nav.PageOutNode GoMePubNew_GoMePub", True)
    PtConsoleNet("Nav.PageOutNode GoMePubNew_GoMeConfRoom", True)
    PtConsoleNet("Nav.PageOutNode GoMePubNew_Entry", True)
    PtConsoleNet("Nav.PageOutNode GoMePubNew_Alcoves", True)

def pageinChiso():
    PtConsoleNet("Nav.PageInNode ChisoPreniv_Chiso", True)
    #PtConsoleNet("Nav.PageInNode ChisoPreniv_Textures", True)

def pageoutChiso():
    PtConsoleNet("Avatar.Spawn.Go 2", True)
    PtConsoleNet("Nav.PageOutNode ChisoPreniv_Textures", True)
    PtConsoleNet("Nav.PageOutNode ChisoPreniv_Chiso", True)

def pageinVeelay():
    PtConsoleNet("Nav.PageInNode VeeTsah_Temple", True)
    #PtConsoleNet("Nav.PageInNode VeeTsah_Textures", True)

def pageoutVeelay():
    PtConsoleNet("Avatar.Spawn.Go 2", True)
    #PtConsoleNet("Nav.PageOutNode VeeTsah_Textures", True)
    PtConsoleNet("Nav.PageOutNode VeeTsah_Temple", True)

def pageinSerene():
    PtConsoleNet("Nav.PageInNode Serene_mainRoom", True)
    #PtConsoleNet("Nav.PageInNode Serene_Textures", True)
    PtConsoleNet("Avatar.Warp.WarpToXYZ -46.27, -46.03, 0.23", True)

def pageoutSerene():
    PtConsoleNet("Avatar.Spawn.Go 2", True)
    #PtConsoleNet("Nav.PageOutNode Serene_Textures", True)
    PtConsoleNet("Nav.PageOutNode Serene_mainRoom", True)

def pageinVothol():
    PtConsoleNet("Nav.PageInNode Vothol_visitorlink", True)
    #PtConsoleNet("Nav.PageInNode Vothol_Textures", True)
    PtConsoleNet("Avatar.Warp.WarpToXYZ -103.88, -15.68, -0.01", True)

def pageoutVothol():
    PtConsoleNet("Avatar.Spawn.Go 2", True)
    #PtConsoleNet("Nav.PageOutNode Vothol_Textures", True)
    PtConsoleNet("Nav.PageOutNode Vothol_visitorlink", True)

def pageinTrebiv():
    PtConsoleNet("Nav.PageInNode trebivdil_mainRoom", True)
    #PtConsoleNet("Nav.PageInNode trebivdil_Textures", True)
    PtConsoleNet("Avatar.Warp.WarpToXYZ -17.09, 8.60, 22.53", True)

def pageoutTrebiv():
    PtConsoleNet("Avatar.Spawn.Go 2", True)
    #PtConsoleNet("Nav.PageOutNode trebivdil_Textures", True)
    PtConsoleNet("Nav.PageOutNode trebivdil_mainRoom", True)

def pageinNaybree():
    PtConsoleNet("Nav.PageInNode EderNaybree_garden", True)
    PtConsoleNet("Nav.PageInNode EderNaybree_GardenGround", True)
    #PtConsoleNet("Nav.PageInNode EderNaybree_Textures", True)
    PtConsoleNet("Avatar.Warp.WarpToXYZ 52.47, -265.22, -5.27", True)

def pageoutNaybree():     # !! CRASHES THE CLIENT !!
    PtConsoleNet("Avatar.Spawn.Go 2", True)
    #PtConsoleNet("Nav.PageOutNode EderNaybree_Textures", True)
    PtConsoleNet("Nav.PageOutNode EderNaybree_GardenGround", True)
    PtConsoleNet("Nav.PageOutNode EderNaybree_garden", True)

def pageinHighgarden():
    PtConsoleNet("Nav.PageInNode FahetsHighgarden_Default", True)
    #PtConsoleNet("Nav.PageInNode FahetsHighgarden_Textures", True)
    PtConsoleNet("Avatar.Warp.WarpToXYZ -78.52, 43.27, 42.35", True)

def pageoutHighgarden():     # !! CRASHES THE CLIENT !!
    PtConsoleNet("Avatar.Spawn.Go 2", True)
    #PtConsoleNet("Nav.PageOutNode FahetsHighgarden_Textures", True)
    PtConsoleNet("Nav.PageOutNode FahetsHighgarden_Default", True)

# GREENSCREENS

def greenscreen():
    PtConsoleNet("Graphics.Renderer.SetClearColor 0 0.8 0", True)
    PtConsoleNet("Graphics.Renderer.SetYon 50", True)

def greensdist(dist):
    PtConsoleNet("Graphics.Renderer.SetYon {}".format(dist), True)

def minkatags():
    PtConsoleNet("Graphics.Renderer.SetClearColor 0 1 1", True)
    PtConsoleNet("Graphics.Renderer.SetYon 50", True)

def minkataHide():
    PtFindSceneobject("GroundPlaneVis","Minkata").draw.disable()
    PtFindSceneobject("DustPlaneParticle01","Minkata").draw.disable()
    PtFindSceneobject("DustPlaneParticle02","Minkata").draw.disable()
    PtFindSceneobject("DustPlaneParticle03","Minkata").draw.disable()
    PtFindSceneobject("DustPlaneParticle04","Minkata").draw.disable()
    PtFindSceneobject("DustPlaneParticle05","Minkata").draw.disable()
    PtFindSceneobject("DustPlaneParticle06","Minkata").draw.disable()
    PtFindSceneobject("DustPlaneParticle07","Minkata").draw.disable()

def minkataRestore():
    PtFindSceneobject("GroundPlaneVis","Minkata").draw.enable()
    PtFindSceneobject("DustPlaneParticle01","Minkata").draw.enable()
    PtFindSceneobject("DustPlaneParticle02","Minkata").draw.enable()
    PtFindSceneobject("DustPlaneParticle03","Minkata").draw.enable()
    PtFindSceneobject("DustPlaneParticle04","Minkata").draw.enable()
    PtFindSceneobject("DustPlaneParticle05","Minkata").draw.enable()
    PtFindSceneobject("DustPlaneParticle06","Minkata").draw.enable()
    PtFindSceneobject("DustPlaneParticle07","Minkata").draw.enable()

# CUSTOM EMOTES

def tapki():
    PtEmoteAvatar("KITap")

def talkseat():
    name = ("M", "F")[PtGetLocalAvatar().avatar.getAvatarClothingGroup()]
    if name == "M":
        PtGetLocalAvatar().avatar.playSimpleAnimation("MaleTalk")
    elif name == "F":
        PtGetLocalAvatar().avatar.playSimpleAnimation("FemaleTalk")

def kneellink():
    name = ("M", "F")[PtGetLocalAvatar().avatar.getAvatarClothingGroup()]
    if name == "M":
        PtGetLocalAvatar().avatar.playSimpleAnimation("MaleFishBookLinkOut")
    elif name == "F":
        PtGetLocalAvatar().avatar.playSimpleAnimation("FemaleFishBookLinkOut")

def bookoffer():
    name = ("M", "F")[PtGetLocalAvatar().avatar.getAvatarClothingGroup()]
    if name == "M":
        PtGetLocalAvatar().avatar.playSimpleAnimation("MaleBookOffer")
    elif name == "F":
        PtGetLocalAvatar().avatar.playSimpleAnimation("FemaleBookOffer")

def bookofferidle():
    name = ("M", "F")[PtGetLocalAvatar().avatar.getAvatarClothingGroup()]
    if name == "M":
        PtGetLocalAvatar().avatar.playSimpleAnimation("MaleBookOfferIdle")
    elif name == "F":
        PtGetLocalAvatar().avatar.playSimpleAnimation("FemaleBookOfferIdle")

# CAMERA SPEED

def slowerCamera():
    PtConsoleNet("Camera.UseSpeedOverrides True", True)
    PtConsoleNet("Camera.SetGlobalVelocity 2", True)

def slowCamera():
    PtConsoleNet("Camera.UseSpeedOverrides True", True)
    PtConsoleNet("Camera.SetGlobalVelocity 4", True)

def walkCamera():
    PtConsoleNet("Camera.UseSpeedOverrides True", True)
    PtConsoleNet("Camera.SetGlobalVelocity 8", True)

def cameraspeed(speed):
    PtConsoleNet("Camera.UseSpeedOverrides True", True)
    PtConsoleNet("Camera.SetGlobalVelocity {}".format(speed), True)

def hidecursor():
    PtForceCursorHidden()

def resetcamera():
    PtConsoleNet("Camera.SetFOV 87 70", True)

# UTILITIES

# Show how many people are in the current Age
def popcount():
    print(1 + len(PtGetPlayerList()), " avatars present")

# Kick out trolls
def kickout(kinum):
    PtConsoleNet("Net.LinkPlayerToPrevAge {}".format(kinum), True)

# Rotate Ahnonay spheres
def rotahny(sphere):
    sdl = PtGetAgeSDL()
    if sphere > 0 and sphere < 5 :
        sdl["ahnyCurrentSphere"] = (sphere,)

# Get the GUID of the current Age
def guidinfo():
    age = ptDniInfoSource()
    print("GUID of this Age: ", age.getAgeGuid() )

# Get some info about the current Age
def ageinfo():
    age = ptDniInfoSource()
    guid = age.getAgeGuid()
    print("GUID of this Age: ", guid)
    PlayerList = PtGetPlayerList()
    idList = map(lambda player:player.getPlayerID(), PlayerList)
    nbavi=1 + PtGetNumRemotePlayers()
    print(str(nbavi), " avatars present")
    for playerId in idList:
        key = PtGetAvatarKeyFromClientID(playerId)
        name = PtGetClientName(key)
        print("Avatars in this Age: ", str(playerId), name)

# Simple tool for setting SDLs (look in the SDL folder for the values)
def setsdl(name, value):
    sdl = PtGetAgeSDL()
    sdl[name] = (value,)

# To the Fun House
def tofunhouse():
    PtConsole("Net.LinkToAgeInstance Neighborhood 33a235b1-9fe0-47f0-a73e-6fbd0044717a")

## To the Fun House Ae'gura (wrong GUID)
#def tofuncity():
#    PtConsole("Net.LinkToAgeInstance City abee8828-869d-4756-89d3-5b374b518595")

# To the Hood of Illusions
def toillusions():
    PtConsole("Net.LinkToAgeInstance Neighborhood 3cc44d4b-31e1-4dec-b6e6-4b63c72becc3")

# Enable KI-GPS coord
def getkigps():
    import Plasma
    import PlasmaKITypes
    vault = Plasma.ptVault()
    psnlSDL = vault.getPsnlAgeSDL()
    if psnlSDL:
        GPSVar = psnlSDL.findVar('GPSEnabled')
        GPSVar.setBool(1)
        vault.updatePsnlAgeSDL(psnlSDL)
