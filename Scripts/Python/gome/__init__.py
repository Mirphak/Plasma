# -*- coding: utf-8 -*-

# GoMe
# Handles GoMe-specific commands.

"""
GoMe special commands:
/nexus : Link to your Nexus.
/city : Link to the public City, optional parameter concert|ferry|library|palace|tokotah.
/pub : Link to the Guild of Messengers Pub.
/kirel : Link to Kirel.
/hood : Link to the Guild of Messengers' Hood, only if you are a member of this hood.
/bump : Bump the Guild of Messengers' Hood, only if you are a member of this hood.
/shirt : Toggle Guild of Messengers' Shirt, parameter on|off.
/agm : Process AGM, you must be defined as moderator in python\gome\agm.py to use this command.
    parameters :
        on : Start the AGM.
        The AGM must be started before using other parameters.
        off : Stop the AGM.
        l : List questions.
        d<ID> : Delete a question by its ID.
        a<ID> : Ask a question by its ID.
        n : Ask the next question in the queue.
        +<player name> : Add a speaker to the list.
        -<player name> : Remove a speaker from the list.
        ls : List speakers.
        c queue : Clear the question queue.
        c speakers : Clear the speaker list.
"""

from Plasma import *
from PlasmaNetConstants import *

from .agm import *

kHoodGuid = "34ac88e0-14e3-4eb2-87b7-984725875e44"
kPubGuid = "9420324e-11f8-41f9-b30b-c896171a8712"
kKirelGuid = "4cfbe95a-1bb2-4cbc-a6c4-87eb28a2aac1"
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