from Plasma import *

def classdesks(bOn=False):
    nameList = [
        "DRCBoardGoToGrsn",
        "DRCBoardWelcomeToDni",
        "DRCGrsnBook",
        "DRCnotice01",
        "DRCnotice02",
        "Desk",
        "Desk1",
        "Desk2",
        "Desk3",
        "Desk4",
        "Desk5",
        "Desk6",
        "Desk7",
        "Desk8",
        "DniPaper",
        "KiNexusJournal",
        "MapBoard02",
        "MapBoardTextDecal09",
        "MapBoardTextDecal10",
        "MapBoardTextDecal11",
        "MapBoardTextDecal12",
        "MapBoardTextDecal13",
        "MapBoardTextDecal14",
        #"MapBoard",
        #"MapBoard01",
        #"MapBoard03",
    ]
    for soName in nameList:
        try:
            so = PtFindSceneobject(soName, "Neighborhood")
            so.netForce(True)
            so.draw.enable(bOn)
            so.physics.enable(bOn)
        except:
            PtSendKIMessage(26, f"ClassDesks.classdesks : Error with {soName}")
            continue
