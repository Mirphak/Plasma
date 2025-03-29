# -*- coding: utf-8 -*-
"""
STATEDESC Kalamee
{
    VERSION 1

    VAR BOOL    allJourneyClothsVisited[1]        DEFAULT=0
    VAR INT     sluiceGatePuzzleButtonsPushed[1]  DEFAULT=0
    VAR BOOL    sluiceGatePuzzleUnlocked[1]       DEFAULT=0
    VAR INT     journeyClothGateClosed[1]         DEFAULT=1
    VAR BOOL    trapGateUnlocked01[1]             DEFAULT=0
    VAR BOOL    trapGateUnlocked02[1]             DEFAULT=0
    VAR BOOL    trapGateUnlocked03[1]             DEFAULT=0
}
"""

"""
    "JourneyClothOneShot_A",
    "JourneyClothOneShot_B",
    "JourneyClothOneShot_C",
    "JourneyClothOneShot_D",
    "JourneyClothOneShot_E",
    "JourneyClothOneShot_F",
    "JourneyClothOneShot_G",
"""
from Plasma import *
from PlasmaKITypes import *

# Get an SDL value.
def GetSDL(name):
	sdl = PtGetAgeSDL()
	value = sdl[name][0]
	return value

def ShowSdls():
    sdlNames = [
        "allJourneyClothsVisited",
        "sluiceGatePuzzleButtonsPushed",
        "sluiceGatePuzzleUnlocked",
        "journeyClothGateClosed",
        "trapGateUnlocked01",
        "trapGateUnlocked02",
        "trapGateUnlocked03",
    ]
    for name in sdlNames:
        PtSendKIMessage(kKILocalChatStatusMsg, f"{name} = {GetSDL(name)}")
