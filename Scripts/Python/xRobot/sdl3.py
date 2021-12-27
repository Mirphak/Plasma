# -*- coding: utf-8 -*-
"""
TEST 1
"""

from Plasma import *
from PlasmaTypes import *

from PlasmaVaultConstants import *

###########
#   SDL   #
###########

# Get an SDL value.
def GetSDL(name):
	sdl = PtGetAgeSDL()
	value = sdl[name][0]
	return value

# Set an SDL value.
def SetSDL(name, value):
	sdl = PtGetAgeSDL()
	sdl[name] = (value,)

# Toggle Bool SDL.
def ToggleBoolSDL(name, bOn):
    try:
        sdlValue = GetSDL(name)
    except:
        print("sdl not found")
        return 0
    sdlValue = bOn
    print("sdlValue={}".format(sdlValue))
    try:
        SetSDL(name, sdlValue)
    except:
        pass

# Toggle Integer SDL.
def ToggleIntSDL(name, minValue, maxValue):
    try:
        sdlValue = GetSDL(name)
    except:
        print("sdl not found")
        return 0
    sdlValue = (sdlValue + 1 - minValue) % (maxValue - minValue + 1)
    sdlValue = sdlValue + minValue
    print("sdlValue={}".format(sdlValue))
    try:
        SetSDL(name, sdlValue)
    except:
        pass

# Hood SDL list
hsl = [
    "nb01Ayhoheek5Man1State", 
    "nb01AyhoheekAccountingFunc", 
    "nb01BahroBoatsChance", 
    "nb01BahroBoatsEnabled", 
    "nb01BahroBoatsProximity", 
    "nb01BahroBoatsRun", 
    "nb01BahroPedestalShoutRun", 
    "nb01BahroStonePedestalVis", 
    "nb01BeachBallVis", 
    "nb01BlueLightOn", 
    "nb01BulletinBoardVis", 
    "nb01CallSoundChance", 
    "nb01CityLightsArchState", 
    "nb01CityLightsBlueVis", 
    "nb01CityLightsConstruction01Vis", 
    "nb01CityLightsConstruction02Vis", 
    "nb01CityLightsConstruction03Vis", 
    "nb01CityLightsConstruction04Vis", 
    "nb01CityLightsGreatZeroVis", 
    "nb01CityLightsHarborVis", 
    "nb01CityLightsMoving01Vis", 
    "nb01CityLightsMoving02Vis", 
    "nb01CityLightsMoving03Vis", 
    "nb01ClassroomDoorClosed", 
    "nb01ClockFunc", 
    "nb01ClockVis", 
    "nb01CommunityAreaConstructionVis", 
    "nb01CommunityAreaState", 
    "nb01ConesVis", 
    #"nb01DRCImagerInbox", 
    "nb01DRCImagerVis", 
    "nb01DRCInfoBoardsVis", 
    "nb01DarkShapeSwimsChance", 
    "nb01DarkShapeSwimsEnabled", 
    "nb01DarkShapeSwimsProximity", 
    "nb01DarkShapeSwimsRun", 
    "nb01DestructionCracksVis", 
    "nb01DniPaperVis", 
    "nb01FansFunc", 
    "nb01FireMarbles1Vis", 
    "nb01FireMarbles2Vis", 
    "nb01FireworksOnBalcony", 
    "nb01FireworksOnBanner", 
    "nb01FireworksOnFountain", 
    "nb01FountainWaterVis", 
    "nb01GZMarkerVis", 
    "nb01GardenBugsVis", 
    "nb01GardenFungusVis", 
    "nb01GardenLightsFunc", 
    "nb01GardenLightsVis", 
    "nb01GreenLightOn", 
    "nb01HappyNewYearVis", 
    "nb01HoodInfoImagerVis", 
    "nb01JourneyCloth1Vis", 
    "nb01JourneyCloth2Vis", 
    "nb01KiNexusJournalVis", 
    "nb01LakeLightState", 
    "nb01LampOption01Vis", 
    "nb01LanternsVis", 
    "nb01LinkBookEderToggle", 
    "nb01LinkBookEderVis", 
    "nb01LinkBookGZVis", 
    "nb01LinkBookGarrisonVis", 
    "nb01LinkBookNexusVis", 
    "nb01LinkBookTeledahnVis", 
    "nb01LinkRoomDoor01Closed", 
    "nb01LinkRoomDoor02Closed", 
    "nb01LinkRoomDoorFunc", 
    "nb01OldImager01Vis", 
    "nb01OldImager02Vis", 
    "nb01OrangeLightOn", 
    "nb01PelletImagerScores", 
    "nb01PlayerImagerVis", 
    "nb01Poetry1JournalVis", 
    "nb01PrivateRoom01Closed", 
    "nb01PrivateRoom02Closed", 
    "nb01PrivateRoom03Closed", 
    "nb01PrivateRoom04Closed", 
    "nb01PrivateRoom05Closed", 
    "nb01PrivateRoomsOuterDoorClosed", 
    "nb01PrivateRoomsOuterDoorEnabled", 
    "nb01PrivateRoomsState", 
    "nb01PuzzleWallState", 
    "nb01RatCreatureVis", 
    "nb01ReaderBoardVis", 
    "nb01ResidenceAdditionsVis", 
    "nb01StainedGlassEders", 
    "nb01StainedGlassGZ", 
    "nb01StainedWindowOption", 
    "nb01TelescopeVis", 
    "nb01ThanksgivingVis", 
    #"nb01TimeOfDay", 
    "nb01WaterfallTorchesVis", 
    "nb01WaterfallVis", 
    "nb01WebCamVis", 
    "nb01YeeshaPage07Chance", 
    "nb01YeeshaPage07Enabled", 
    "nb01YeeshaPage07Proximity", 
    "nb01YeeshaPage07Vis"
]

# Get all Hood SDL values
def ListHoodSdl():
    print("Hood SDL list (name, value) :")
    for name in hsl:
        print("'{}';'{}'".format(name, GetSDL(name)))

"""
Hood SDL list (name, value) :
'nb01Ayhoheek5Man1State'...........: '2'
'nb01AyhoheekAccountingFunc'.......: '1'
'nb01BahroBoatsChance'.............: '0'
'nb01BahroBoatsEnabled'............: '0'
'nb01BahroBoatsProximity'..........: '0'
'nb01BahroBoatsRun'................: '0'
'nb01BahroPedestalShoutRun'........: '0'
'nb01BahroStonePedestalVis'........: '1'
'nb01BeachBallVis'.................: '1'
'nb01BlueLightOn'..................: '1'
'nb01BulletinBoardVis'.............: '1'
'nb01CallSoundChance'..............: '0'
'nb01CityLightsArchState'..........: '0'
'nb01CityLightsBlueVis'............: '1'
'nb01CityLightsConstruction01Vis'..: '0'
'nb01CityLightsConstruction02Vis'..: '0'
'nb01CityLightsConstruction03Vis'..: '0'
'nb01CityLightsConstruction04Vis'..: '0'
'nb01CityLightsGreatZeroVis'.......: '1'
'nb01CityLightsHarborVis'..........: '1'
'nb01CityLightsMoving01Vis'........: '1'
'nb01CityLightsMoving02Vis'........: '1'
'nb01CityLightsMoving03Vis'........: '1'
'nb01ClassroomDoorClosed'..........: '1'
'nb01ClockFunc'....................: '0'
'nb01ClockVis'.....................: '1'
'nb01CommunityAreaConstructionVis'.: '0'
'nb01CommunityAreaState'...........: '2'
'nb01ConesVis'.....................: '1'
'nb01DRCImagerVis'.................: '1'
'nb01DRCInfoBoardsVis'.............: '1'
'nb01DarkShapeSwimsChance'.........: '0'
'nb01DarkShapeSwimsEnabled'........: '0'
'nb01DarkShapeSwimsProximity'......: '0'
'nb01DarkShapeSwimsRun'............: '0'
'nb01DestructionCracksVis'.........: '1'
'nb01DniPaperVis'..................: '1'
'nb01FansFunc'.....................: '1'
'nb01FireMarbles1Vis'..............: '1'
'nb01FireMarbles2Vis'..............: '1'
'nb01FireworksOnBalcony'...........: '0'
'nb01FireworksOnBanner'............: '0'
'nb01FireworksOnFountain'..........: '0'
'nb01FountainWaterVis'.............: '1'
'nb01GZMarkerVis'..................: '1'
'nb01GardenBugsVis'................: '1'
'nb01GardenFungusVis'..............: '0'
'nb01GardenLightsFunc'.............: '1'
'nb01GardenLightsVis'..............: '1'
'nb01GreenLightOn'.................: '1'
'nb01HappyNewYearVis'..............: '0'
'nb01HoodInfoImagerVis'............: '1'
'nb01JourneyCloth1Vis'.............: '0'
'nb01JourneyCloth2Vis'.............: '0'
'nb01KiNexusJournalVis'............: '1'
'nb01LakeLightState'...............: '1'
'nb01LampOption01Vis'..............: '1'
'nb01LanternsVis'..................: '0'
'nb01LinkBookEderToggle'...........: '2'
'nb01LinkBookEderVis'..............: '1'
'nb01LinkBookGZVis'................: '1'
'nb01LinkBookGarrisonVis'..........: '1'
'nb01LinkBookNexusVis'.............: '1'
'nb01LinkBookTeledahnVis'..........: '0'
'nb01LinkRoomDoor01Closed'.........: '0'
'nb01LinkRoomDoor02Closed'.........: '0'
'nb01LinkRoomDoorFunc'.............: '1'
'nb01OldImager01Vis'...............: '1'
'nb01OldImager02Vis'...............: '1'
'nb01OrangeLightOn'................: '1'
'nb01PelletImagerScores'...........: '""'
'nb01PlayerImagerVis'..............: '1'
'nb01Poetry1JournalVis'............: '1'
'nb01PrivateRoom01Closed'..........: '0'
'nb01PrivateRoom02Closed'..........: '0'
'nb01PrivateRoom03Closed'..........: '0'
'nb01PrivateRoom04Closed'..........: '0'
'nb01PrivateRoom05Closed'..........: '0'
'nb01PrivateRoomsOuterDoorClosed'..: '1'
'nb01PrivateRoomsOuterDoorEnabled'.: '1'
'nb01PrivateRoomsState'............: '2'
'nb01PuzzleWallState'..............: '0'
'nb01RatCreatureVis'...............: '0'
'nb01ReaderBoardVis'...............: '0'
'nb01ResidenceAdditionsVis'........: '1'
'nb01StainedGlassEders'............: '1'
'nb01StainedGlassGZ'...............: '2'
'nb01StainedWindowOption'..........: '2'
'nb01TelescopeVis'.................: '1'
'nb01ThanksgivingVis'..............: '0'
'nb01WaterfallTorchesVis'..........: '0'
'nb01WaterfallVis'.................: '1'
'nb01WebCamVis'....................: '0'
'nb01YeeshaPage07Chance'...........: '50'
'nb01YeeshaPage07Enabled'..........: '1'
'nb01YeeshaPage07Proximity'........: '0'
'nb01YeeshaPage07Vis'..............: '1'
"""

# Toggle all Hood Bool SDL.
def HoodBoolSDL(bOn):
    ToggleBoolSDL("nb01AyhoheekAccountingFunc", bOn)
    ToggleBoolSDL("nb01BulletinBoardVis", bOn)
    ToggleBoolSDL("nb01CityLightsBlueVis", bOn)
    ToggleBoolSDL("nb01CityLightsConstruction01Vis", bOn)
    ToggleBoolSDL("nb01CityLightsConstruction02Vis", bOn)
    ToggleBoolSDL("nb01CityLightsConstruction03Vis", bOn)
    ToggleBoolSDL("nb01CityLightsConstruction04Vis", bOn)
    ToggleBoolSDL("nb01CityLightsGreatZeroVis", bOn)
    ToggleBoolSDL("nb01CityLightsHarborVis", bOn)
    ToggleBoolSDL("nb01CityLightsMoving01Vis", bOn)
    ToggleBoolSDL("nb01CityLightsMoving02Vis", bOn)
    ToggleBoolSDL("nb01CityLightsMoving03Vis", bOn)
    ToggleBoolSDL("nb01ClockFunc", bOn)
    ToggleBoolSDL("nb01CommunityAreaConstructionVis", bOn)
    ToggleBoolSDL("nb01ConesVis", bOn)
    ToggleBoolSDL("nb01DniPaperVis", bOn)
    ToggleBoolSDL("nb01FansFunc", bOn)
    ToggleBoolSDL("nb01FireMarbles1Vis", bOn)
    ToggleBoolSDL("nb01FireMarbles2Vis", bOn)
    ToggleBoolSDL("nb01FountainWaterVis", bOn)
    ToggleBoolSDL("nb01GardenBugsVis", bOn)
    ToggleBoolSDL("nb01GardenLightsFunc", bOn)
    ToggleBoolSDL("nb01JourneyCloth1Vis", bOn)
    ToggleBoolSDL("nb01JourneyCloth2Vis", bOn)
    ToggleBoolSDL("nb01LinkBookEderVis", bOn)
    ToggleBoolSDL("nb01LinkBookGarrisonVis", bOn)
    ToggleBoolSDL("nb01LinkBookTeledahnVis", bOn)
    ToggleBoolSDL("nb01LinkBookGZVis", bOn)
    ToggleBoolSDL("nb01LinkRoomDoorFunc", bOn)
    ToggleBoolSDL("nb01RatCreatureVis", bOn)
    ToggleBoolSDL("nb01TelescopeVis", bOn)
    ToggleBoolSDL("nb01WaterfallVis", bOn)
    ToggleBoolSDL("nb01DRCInfoBoardsVis", bOn)
    ToggleBoolSDL("nb01YeeshaPage07Vis", bOn)
    ToggleBoolSDL("nb01PlayerImagerVis", bOn)
    ToggleBoolSDL("nb01DRCImagerVis", bOn)
    ToggleBoolSDL("nb01HappyNewYearVis", bOn)
    ToggleBoolSDL("nb01WebCamVis", bOn)
    ToggleBoolSDL("nb01HoodInfoImagerVis", bOn)
    ToggleBoolSDL("nb01ThanksgivingVis", bOn)
    ToggleBoolSDL("nb01LinkBookNexusVis", bOn)
    ToggleBoolSDL("nb01Poetry1JournalVis", bOn)
    ToggleBoolSDL("nb01KiNexusJournalVis", bOn)
    ToggleBoolSDL("nb01BahroStonePedestalVis", bOn)
    ToggleBoolSDL("nb01BahroPedestalShoutRun", bOn)
    ToggleBoolSDL("nb01ReaderBoardVis", bOn)	
    ToggleBoolSDL("nb01BahroBoatsRun", bOn)
    ToggleBoolSDL("nb01DarkShapeSwimsRun", bOn)
    ToggleBoolSDL("nb01BlueLightOn", bOn)
    ToggleBoolSDL("nb01GreenLightOn", bOn)
    ToggleBoolSDL("nb01OrangeLightOn", bOn)
    ToggleBoolSDL("nb01LinkRoomDoor01Closed", bOn)
    ToggleBoolSDL("nb01LinkRoomDoor02Closed", bOn)
    ToggleBoolSDL("nb01ClassroomDoorClosed", bOn)
    ToggleBoolSDL("nb01PrivateRoomsOuterDoorClosed", bOn)
    ToggleBoolSDL("nb01PrivateRoomsOuterDoorEnabled", bOn)
    ToggleBoolSDL("nb01PrivateRoom01Closed", bOn)
    ToggleBoolSDL("nb01PrivateRoom02Closed", bOn)
    ToggleBoolSDL("nb01PrivateRoom03Closed", bOn)
    ToggleBoolSDL("nb01PrivateRoom04Closed", bOn)
    ToggleBoolSDL("nb01PrivateRoom05Closed", bOn)
    ToggleBoolSDL("nb01FireworksOnBalcony", bOn)
    ToggleBoolSDL("nb01FireworksOnBanner", bOn)
    ToggleBoolSDL("nb01FireworksOnFountain", bOn)
    ToggleBoolSDL("nb01BeachBallVis", bOn)
    ToggleBoolSDL("nb01ClockVis", bOn)
    ToggleBoolSDL("nb01GardenFungusVis", bOn)
    ToggleBoolSDL("nb01GardenLightsVis", bOn)
    ToggleBoolSDL("nb01DestructionCracksVis", bOn)
    ToggleBoolSDL("nb01LanternsVis", bOn)
    ToggleBoolSDL("nb01LampOption01Vis", bOn)
    ToggleBoolSDL("nb01OldImager01Vis", bOn)
    ToggleBoolSDL("nb01OldImager02Vis", bOn)
    ToggleBoolSDL("nb01WaterfallTorchesVis", bOn)
    ToggleBoolSDL("nb01ResidenceAdditionsVis", bOn)
    ToggleBoolSDL("nb01GZMarkerVis", bOn)
    ToggleBoolSDL("nb01YeeshaPage07Enabled", bOn)
    ToggleBoolSDL("nb01YeeshaPage07Proximity", bOn)
    ToggleBoolSDL("nb01DarkShapeSwimsEnabled", bOn)
    ToggleBoolSDL("nb01DarkShapeSwimsProximity", bOn)
    ToggleBoolSDL("nb01BahroBoatsEnabled", bOn)
    ToggleBoolSDL("nb01BahroBoatsProximity", bOn)

"""
** 1. Make the tredfish visible (it appears as a shadow in the lake below the telescope balcony)
	==> Yes, I've seen it last time I visited the Mir-o-Bot's hood.
	
** 2. Make the ferry boats visible (they appear as shapes moving between the islands in the distance from the balcony)
	==> No. I thought yes, but I have not seen it.
	
3. Cycle the seasonal decorations (fall, new year, etcetera)
	==> Yes, I can add and remove them on demand. AFAIK, there is only New year and Halloween (called Thansgiving).
	
4. Make the bahro appear (in the linking book room)
	==> Yes, it appears each time somebody is linking in Mir-o-Bot's hood. I may try to find out a way to call it on demand.
	
5. Cycle the stained glass mosaics in the linking book room
	==> Yes, I have done that in previous seasons.

6. Cycle the lamp covers between the hand-tree and bee in the fountain courtyard
	==> Yes, I have done that in previous seasons.

7. Find a way to light up the dark corners of the classroom to see the door into the cavern wall
	==> Yes, I have different projectors for that. Yeesha glow light seems good.

8. Make the objects that can be found on the shelves in the meditation chambers appear. 
	I’ve seen Bahro stones and clue papers in different forms of the game.
	==> ???
	
** 9. Up until now, I’ve just been talking about the Bahro tablet that’s up on 
	the balcony of the big home. I never thought of it before, 
	but can you move that tablet down to the fountain courtyard? 
	If you can place it next to the easel that tells explorers to go to the classroom, 
	that would be great.
	==> Unfortunately it's not possible, the upper balcony Bahro stone can't be moved.
	==> We will have to go on the upper balcony (-> sp 3)
    
** 10. Another hidden item I’d like to turn on if you can is the video camera and notebook computer that sat in the fountain courtyard.
	==> Yes, already visible in Mir-o-Bot's hood.

For requests 1, 2, 9 and 10, please have them turned on when we link to the bot’s neighborhood.
	==> 1, 2 and 10 are Okay, but not 9.
"""
# Have them turned on when we link to the bot’s neighborhood.
# 1. Make the tredfish visible (it appears as a shadow in the lake below the telescope balcony)
# 2. Make the ferry boats visible (they appear as shapes moving between the islands in the distance from the balcony)
# 10. Another hidden item I’d like to turn on if you can is the video camera and notebook computer that sat in the fountain courtyard.
def VisibleAtTourStart():    
    # 1. Make the tredfish visible
    SetSDL('nb01DarkShapeSwimsChance', 100)
    SetSDL('nb01DarkShapeSwimsEnabled', 1)
    SetSDL('nb01DarkShapeSwimsProximity', 1)
    SetSDL('nb01DarkShapeSwimsRun', 1)
    # 2. Make the ferry boats visible
    SetSDL('nb01BahroBoatsChance', 100)
    SetSDL('nb01BahroBoatsEnabled', 1)
    SetSDL('nb01BahroBoatsProximity', 1)
    SetSDL('nb01BahroBoatsRun', 1)
    # 10. Make the video camera and notebook computer visible
    SetSDL('nb01WebCamVis', 1)
    # Bahro
    SetSDL('nb01BahroPedestalShoutRun', 1)
    SetSDL('nb01CallSoundChance', 100)
    # City
    SetSDL('nb01CityLightsBlueVis', 1)
    SetSDL('nb01CityLightsConstruction01Vis', 1)
    SetSDL('nb01CityLightsConstruction02Vis', 1)
    SetSDL('nb01CityLightsConstruction03Vis', 1)
    SetSDL('nb01CityLightsConstruction04Vis', 1)
    SetSDL('nb01CityLightsGreatZeroVis', 1)
    SetSDL('nb01CityLightsHarborVis', 1)
    SetSDL('nb01CityLightsMoving01Vis', 1)
    SetSDL('nb01CityLightsMoving02Vis', 1)
    SetSDL('nb01CityLightsMoving03Vis', 1)


"""
## 3. Cycle the seasonal decorations (fall, new year, etcetera)
## Dans les SDL je ne trouve que HappyNewYear et Thanksgiving
##
#def_hny(bOn):
#    ToggleBoolSDL("nb01HappyNewYearVis", bOn)
##
#def_tg(bOn):
#    ToggleBoolSDL("nb01ThanksgivingVis", bOn)
"""

# 3. Cycle the seasonal decorations (fall, new year, etcetera) : HappyNewYear and Thanksgiving, others ?
# 5. Cycle the stained glass mosaics in the linking book room
# 6. Cycle the lamp covers between the hand-tree and bee in the fountain courtyard
# Changing the Stained Glass Panels
# ga   : 0, 1, 2            # Gahreesen Stained Glasses
# ed   : 1, 2, 3, 4, 5, 6   # Eder Delin and Eder Tsogal Stained Glasses
# gz   : 1, 2, 3            # Great Zero Stained Glasses
# lamp : 0, 1               # Lamps (hand / bee)
# hny  : 0, 1               # Happy New Year
# tg/ha: 0, 1               # Thanksgiving, in fact it's Halloween!
# lls  : 0, 1, 2, 3, 4      # Lake Light State 
# fw   : 0, 1               # Fireworks
# jc   : 0, 1               # Journey Clothes
# bl   : 0, 1               # Blue Light
# gl   : 0, 1               # Green Light
# ol   : 0, 1               # Orange Light
# Changing some of the Hood SDL
def ToggleHoodSDL(name):
    ageInfo = PtGetAgeInfo()
    if (ageInfo.getAgeFilename() != "Neighborhood"):
        return 0
    name = name.lower()
    #
    if name.startswith("ga"):
        try:
            ToggleIntSDL("nb01StainedWindowOption", 0, 2)
        except:
            print("wrong sdl value")
    elif name.startswith("ed"):
        try:
            ToggleIntSDL("nb01StainedGlassEders", 1, 6)
        except:
            print("wrong sdl value")
    elif name.startswith("gr") or name == "gz":
        try:
            ToggleIntSDL("nb01StainedGlassGZ", 1, 3)
        except:
            print("wrong sdl value")
    elif name == "lls":
        try:
            ToggleIntSDL("nb01LakeLightState", 0, 4)
            #ToggleIntSDL("nb01CityLightsArchState", 0, 4)
            #ToggleIntSDL("nb01CommunityAreaState", 0, 4)
        except:
            print("wrong sdl value")
    elif name == "lamp":
        try:
            ToggleIntSDL("nb01LampOption01Vis", 0, 1)
        except:
            print("wrong sdl value")
    elif name == "hny":
        try:
            ToggleIntSDL("nb01HappyNewYearVis", 0, 1)
        except:
            print("wrong sdl value")
    elif name == "tg" or name == "ha":
        try:
            ToggleIntSDL("nb01ThanksgivingVis", 0, 1)
        except:
            print("wrong sdl value")
    elif name == "fw":
        try:
            ToggleIntSDL("nb01FireworksOnBalcony", 0, 1)
            ToggleIntSDL("nb01FireworksOnBanner", 0, 1)
            ToggleIntSDL("nb01FireworksOnFountain", 0, 1)
        except:
            print("wrong sdl value")
    elif name == "jc":
        try:
            ToggleIntSDL("nb01JourneyCloth1Vis", 0, 1)
            ToggleIntSDL("nb01JourneyCloth2Vis", 0, 1)
        except:
            print("wrong sdl value")
    elif name == "bl":
        try:
            ToggleIntSDL("nb01BlueLightOn", 0, 1)
        except:
            print("wrong sdl value")
    elif name == "gl":
        try:
            ToggleIntSDL("nb01GreenLightOn", 0, 1)
        except:
            print("wrong sdl value")
    elif name == "ol":
        try:
            ToggleIntSDL("nb01OrangeLightOn", 0, 1)
        except:
            print("wrong sdl value")
    else:
        print("name <> 'ga' or 'ed' or 'gz', or 'lamp'; 'hny'; 'tg'")
        return 0

#

#
