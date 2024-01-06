# -*- coding: utf-8 -*-

# GoMe
# Handles GoMe-specific commands.

from Plasma import *
from PlasmaNetConstants import *

from agm import *

kHoodGuid = "6624fb8a-ebec-40ff-b1e2-4f51588e2db5"
kPubGuid = "9420324e-11f8-41f9-b30b-c896171a8712"
kShirt = ("MTorso_GuildYellow", "FTorso_GuildYellow")
kSpawnPoints = {
    "concert": "LinkInPointConcertHallFoyer",
    "ferry": "LinkInPointFerry",
    "library": "LinkInPointLibrary",
    "palace": "LinkInPointPalace",
    "tokotah": "LinkInPointDakotahAlley"
}
        
## Links the player to the specified Age.
def LinkTo(ageFilename, linkingRule=PtLinkingRules.kBasicLink, guid=None):

    ageLink = ptAgeLinkStruct()
    ageLink.setLinkingRules(linkingRule)
    ageInfo = ptAgeInfoStruct()
    ageInfo.setAgeFilename(ageFilename)
    if guid:
        ageInfo.setAgeInstanceGuid(guid)
    ageLink.setAgeInfo(ageInfo)
    ptNetLinkingMgr().linkToAge(ageLink)