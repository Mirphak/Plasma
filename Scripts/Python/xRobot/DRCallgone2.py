# -*- coding: utf-8 -*-

from Plasma import *

# Toggle BaronCityOffice walls physics
def toggleWalls(bOn=False):
    obj=PtFindSceneobject("CollisionWallsBCO", "BaronCityOffice")
    obj.netForce(True)
    obj.physics.enable(bOn)

# Toggle visibility of all BaronCityOffice DRC objects
def toggleDraw(bOn=False):
    objectNameList = [
        "b_book09",
        "BahroRockBook",
        "BetweenRmsCamRegion",
        "BetweenRmsCamera",
        "BetweenRmsCamera.Target",
        "BookStand",
        "BookStandShadow",
        "CameraPage",
        "Chair",
        "Chart01",
        "Chart02",
        "DRCStamp",
        "DeskLightBillboard",
        "DeskShadow",
        "Desktop",
        "DniCityBackdrop",
        "DniCityBigFogdrop",
        "DniLinkingBookNew",
        "Inkwell",
        "KVeer",
        "KVeerReflection",
        "Lamp02",
        "Lamp08",
        "Lamp11",
        "LampGlare01",
        "LampGlare02",
        "LightBillboard03",
        "LinkingBookCamRegion",
        "LinkingBookRailCamera",
        "LinkingBookRailCamera.Target",
        "LivingRmCameraRegion",
        "LivingRmCircleCamera",
        "LivingRmCircleCamera.Target",
        "Map01",
        "Map02",
        "Map03",
        "MapHolder",
        "Mug+PensGroup",
        "Mug-Kenya",
        "MugShadow",
        "OfficeDeskRailCamera",
        "OfficeDeskRailCamera.Target",
        "OfficeRmCameraRegion",
        "Paper01",
        "Paper02",
        "Pen01",
        "Pen02",
        "Pen03",
        "Pen04",
        "Pencil01",
        "Pencil02",
        "Pencil03",
        "Photo01",
        "Pict01Shadow",
        "Pict02Shadow",
        "Pict03Shadow",
        "RTOmniLight01",
        "Rug01",
        "Rug03",
        "SlvOfcSafeFrame04",
        "SlvOfcSafeFrame05",
        "SlvOfcSafeFrame06",
        "TableLamp",
        "TelescopeBolt01",
        "TelescopeCeilingShadow",
        "TelescopeLens01",
        "TelescopeNew01",
        "WrinkledNote",
        "WrinkledNote01",
        "WrinkledNoteText",
        "YellowNoteBookplane",
        "lowPolyIslandArms01",
        "lowPolyIslandArms02",
        "lowPolyIslandArms03",
        "lowPolyIslandArms04",
        "lowPolyIslandArmsReflect01",
        "lowPolyIslandArmsReflect02",
        "lowPolyIslandArmsReflect03",
        "lowPolyIslandArmsReflect04",
        "nb01CaveBackdropStateMaster",
        "nb01DistantCityFake-Group",
        "nb01LakeLightStateMaster",
        "pad"
    ]
    for objName in objectNameList:
        obj=PtFindSceneobject(objName, "BaronCityOffice")
        obj.netForce(True)
        obj.draw.enable(bOn)

# Toggle physics of all BaronCityOffice DRC objects
def togglePhys(bOn=False):
    objectNameList = [
        "b_book09",
        "BahroRockBook",
        "BetweenRmsCamRegion",
        "blocker",
        "Box01",
        "chairclickableproxy",
        #"ChristmasTreeCollider",
        #"CollisionFloorBCO",
        "CollisionWallsBCO",
        "DniLinkingBookNew",
        "DtctLinkOutBaronCityOffice",
        "GZMarkerDetector",
        "LinkingBookCamRegion",
        "LivingRmCameraRegion",
        "OfficeRmCameraRegion",
        "pad",
        "Paper01",
        "Paper2ClickBox02",
        "SfxRegionSensor-Music01",
        "SfxRegSenFeet-Carpet01",
        "SfxRegSenFeet-Carpet02",
        "SfxRegSenFeet-Stone01",
        "ShroomiePostCamREGION",
        "sitregion",
        "TelescopeCameraRegion",
        "TelescopeNew01",
        "telescoperegion",
        "TreasureBookDetector",
        "WrinkledNote01"
    ]
    for objName in objectNameList:
        obj=PtFindSceneobject(objName, "BaronCityOffice")
        obj.netForce(True)
        obj.physics.enable(bOn)
