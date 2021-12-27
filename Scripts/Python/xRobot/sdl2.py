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
        print "sdl not found"
        return 0
    sdlValue = bOn
    print "sdlValue={}".format(sdlValue)
    try:
        SetSDL(name, sdlValue)
    except:
        pass


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
