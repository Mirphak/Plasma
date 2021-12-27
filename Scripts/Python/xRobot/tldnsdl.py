# -*- coding: utf-8 -*-

"""

STATEDESC Teledahn
{
	VERSION 33

# Boolean variables
    VAR BOOL    tldnJourneyCloth01Vis[1]    DEFAULT=1 DEFAULTOPTION=VAULT
    VAR BOOL    tldnJourneyCloth02Vis[1]    DEFAULT=1 DEFAULTOPTION=VAULT
    VAR BOOL    tldnJourneyCloth04Vis[1]    DEFAULT=1 DEFAULTOPTION=VAULT
    VAR BOOL    tldnJourneyCloth05Vis[1]    DEFAULT=1 DEFAULTOPTION=VAULT
    VAR BOOL    tldnJourneyCloth06Vis[1]    DEFAULT=1 DEFAULTOPTION=VAULT
    VAR BOOL    tldnJourneyCloth07Vis[1]    DEFAULT=1 DEFAULTOPTION=VAULT

    VAR BOOL    tldnTreasureBook07Vis[1]    DEFAULT=1 DEFAULTOPTION=VAULT
    VAR BOOL    tldnYeeshaPage04Vis[1]    DEFAULT=1 DEFAULTOPTION=VAULT
    VAR BOOL    tldnYeeshaPage06Vis[1]    DEFAULT=1 DEFAULTOPTION=VAULT
    VAR BOOL    tldnPumpSwitchFunc[1]    DEFAULT=1 DEFAULTOPTION=VAULT # Makes the center lever disappear at the WRCC.

    VAR BOOL    tldnCalendarSpark09[1]    DEFAULT=0 DEFAULTOPTION=VAULT

# State variables
    VAR BYTE	tldnHarpoonState[1]    DEFAULT=0 DEFAULTOPTION=VAULT # 0 = No harpoons pages loaded. 1 = tldnHarpoonState01a Loaded. 2 = tldnHarpoonState01b Loaded

## Age Mechanics ##

# Power Tower
    VAR BYTE     tldnPwrTwrPumpCount[1] DEFAULT=0 DISPLAYOPTION=red # 0-3, 3 = tower raised
    VAR BOOL    tldnMainPowerOn[1]      DEFAULT=0 DISPLAYOPTION=red
    VAR BOOL    tldnWorkroomShaftOn[1]      DEFAULT=0 DISPLAYOPTION=red
    VAR BOOL    tldnWorkroomPowerOn[1]      DEFAULT=0 DISPLAYOPTION=hidden DISPLAYOPTION=red
    VAR BOOL    tldnShroomieGateShaftOn[1]      DEFAULT=0 DISPLAYOPTION=red
    VAR BOOL    tldnShroomieGatePowerOn[1]      DEFAULT=0 DISPLAYOPTION=hidden DISPLAYOPTION=red
    
# Buckets
    VAR BOOL    tldnBucketContinuousLoopMode[1]   DEFAULT=1 DISPLAYOPTION=red
    VAR BOOL    tldnBucketLowerLeverPulled[1]   DEFAULT=0 DISPLAYOPTION=red
    VAR BYTE    tldnBucketState[2]      DEFAULT=0 DISPLAYOPTION=hidden
    # tldnBucketState[0] = State, tldnBucketState[1] = fastforward
    # States:
    #   1=Stop, 2=QRun, 3=QBoardQRun, 4=Run, 5=Dump, 6=QStop, 7=DumpQBoard, 8=DumpQStop, 9=DumpQBoardQStop, 10=QBoard, 11=Boarded
    VAR INT     tldnRiders[4]           DEFAULT=0  DISPLAYOPTION=hidden
    VAR INT     tldnBucketAtEntry[1]    DEFAULT=0  DISPLAYOPTION=hidden
    VAR BOOL    tldnShrmDoorOpen[1]     DEFAULT=0  DISPLAYOPTION=hidden
    VAR INT     tldnBucketAtDump[1]     DEFAULT=-1  DISPLAYOPTION=hidden


# Elevator
    VAR BOOL    tldnElevatorLocked[1]       DEFAULT=1 DISPLAYOPTION=red
    VAR BYTE    tldnElevatorCurrentFloor[1]       DEFAULT=2 DISPLAYOPTION=red DISPLAYOPTION=hidden
    VAR BOOL    tldnElevatorIdle[1]       DEFAULT=1 DISPLAYOPTION=red DISPLAYOPTION=hidden

# Workroom
    VAR BOOL    tldnWorkRmLightSwitch01On[1]   DEFAULT=0 DISPLAYOPTION=red
    VAR BOOL    tldnWorkRmLightSwitch02On[1]   DEFAULT=0 DISPLAYOPTION=red
    VAR BOOL    tldnWorkRmLightSwitch03On[1]   DEFAULT=0 DISPLAYOPTION=red

# InShroom
    VAR BOOL    tldnCabinDrained[1]     DEFAULT=0 DISPLAYOPTION=red
    VAR BOOL    tldnHatchOpen[1]        DEFAULT=0 DISPLAYOPTION=red
    VAR BOOL    tldnHatchLocked[1]      DEFAULT=1 DISPLAYOPTION=red
    
# Uppershroom
    VAR BOOL    tldnAquariumOpen[1]     DEFAULT=0 DISPLAYOPTION=red
    VAR BOOL    tldnAquariumLightOn[1]      DEFAULT=0 DISPLAYOPTION=red
    VAR BOOL    tldnShuttersOpen[1]     DEFAULT=0 DISPLAYOPTION=red
    VAR BOOL    tldnNexusStationVis[1]    DEFAULT=1 DEFAULTOPTION=VAULT
    
# WarShroom
    VAR BOOL    tldnOuterDoorClosed[1]     DEFAULT=1 DISPLAYOPTION=red
    VAR BOOL    tldnCatwalkDoorClosed[1]    DEFAULT=1 DISPLAYOPTION=red
    
# ShroomieGate
    VAR BOOL    tldnShroomieGateUp[1]   DEFAULT=1 DISPLAYOPTION=red
    VAR BOOL    tldnBrokenBridgeLowered[1]      DEFAULT=0 DISPLAYOPTION=red

# Bahro Door
    VAR BOOL    tldnBahroDoorClosed[1]    DEFAULT=1 DISPLAYOPTION=red

# SlaveOffice
    VAR BOOL    tldnSecretDoorOpen[1]    DEFAULT=0 DISPLAYOPTION=red
    VAR BOOL    tldnTieDyeVis[1]    DEFAULT=0 DEFAULTOPTION=VAULT


# Vapor Miner Hits
    VAR BOOL    tldnRockAVaporHit[1]    DEFAULT=0 DISPLAYOPTION=red
    VAR BOOL    tldnRockBVaporHit[1]    DEFAULT=0 DISPLAYOPTION=red
    VAR BOOL    tldnRockCVaporHit[1]    DEFAULT=0 DISPLAYOPTION=red
    VAR BOOL    tldnRockDVaporHit[1]    DEFAULT=0 DISPLAYOPTION=red

# Slave Cave - Control Panels
    VAR BOOL    tldnSlaveActivePanel01[1]    DEFAULT=1 DISPLAYOPTION=red
    VAR BOOL    tldnSlaveActivePanel02[1]    DEFAULT=0 DISPLAYOPTION=red
    VAR BOOL    tldnSlaveActivePanel03[1]    DEFAULT=1 DISPLAYOPTION=red
    VAR BOOL    tldnSlaveActivePanel04[1]    DEFAULT=0 DISPLAYOPTION=red
    VAR BOOL    tldnSlaveActivePanel05[1]    DEFAULT=1 DISPLAYOPTION=red
    VAR BOOL    tldnSlaveActivePanel06[1]    DEFAULT=0 DISPLAYOPTION=red
    VAR BOOL    tldnSlaveActivePanel07[1]    DEFAULT=0 DISPLAYOPTION=red
    
# Bump Bridge 
    VAR BOOL    tldnLagoonBridgeStuck[1] DEFAULT=1 DISPLAYOPTION=red  
    VAR BOOL    tldnLagoonBridgeRaised[1] DEFAULT=1 DISPLAYOPTION=red 

# Shroomie Creature
    VAR INT    ShroomieTotalTimesSeen[1] DEFAULT=0 DISPLAYOPTION=hidden
    VAR INT    ShroomieTimeLastSeen[1] DEFAULT=0 DISPLAYOPTION=hidden
    
# More Slave Cave - Pressure Plates
    VAR BOOL    tldnSlaveActivePlate01[1]    DEFAULT=0 DISPLAYOPTION=red
    VAR BOOL    tldnSlaveActivePlate02[1]    DEFAULT=0 DISPLAYOPTION=red
    VAR BOOL    tldnSlaveActivePlate03[1]    DEFAULT=0 DISPLAYOPTION=red
    VAR BOOL    tldnSlaveActivePlate04[1]    DEFAULT=0 DISPLAYOPTION=red
    VAR BOOL    tldnSlaveActivePlate05[1]    DEFAULT=0 DISPLAYOPTION=red
    VAR BOOL    tldnSlaveActivePlate06[1]    DEFAULT=0 DISPLAYOPTION=red
    VAR BOOL    tldnSlaveActivePlate07[1]    DEFAULT=0 DISPLAYOPTION=red

    VAR BOOL    tldnSlaveCaveSecretDoorVis[1]    DEFAULT=0 DEFAULTOPTION=VAULT
    VAR BOOL    tldnSlaveCaveSecretDoorOpen[1]    DEFAULT=0 DEFAULTOPTION=red

}

"""


from Plasma import *
from PlasmaTypes import *
from PlasmaVaultConstants import *

lstSdlOne = [
    ["tldnJourneyCloth01Vis", 1, 1], 
    ["tldnJourneyCloth02Vis", 1, 1], 
    ["tldnJourneyCloth04Vis", 1, 1], 
    ["tldnJourneyCloth05Vis", 1, 1], 
    ["tldnJourneyCloth06Vis", 1, 1], 
    ["tldnJourneyCloth07Vis", 1, 1], 
    ["tldnTreasureBook07Vis", 1, 1], 
    ["tldnYeeshaPage04Vis", 1, 1], 
    ["tldnYeeshaPage06Vis", 1, 1], 
    ["tldnPumpSwitchFunc", 1, 1], 
    ["tldnCalendarSpark09", 1, 0], 
    ["tldnHarpoonState", 1, 0], 
    ["tldnPwrTwrPumpCount", 1, 0], 
    ["tldnMainPowerOn", 1, 0], 
    ["tldnWorkroomShaftOn", 1, 0], 
    ["tldnWorkroomPowerOn", 1, 0], 
    ["tldnShroomieGateShaftOn", 1, 0], 
    ["tldnShroomieGatePowerOn", 1, 0], 
    ["tldnBucketContinuousLoopMode", 1, 1], 
    ["tldnBucketLowerLeverPulled", 1, 0], 
    ["tldnBucketAtEntry", 1, 0], 
    ["tldnShrmDoorOpen", 1, 0], 
    ["tldnBucketAtDump", 1, -1], 
    ["tldnElevatorLocked", 1, 1], 
    ["tldnElevatorCurrentFloor", 1, 2], 
    ["tldnElevatorIdle", 1, 1], 
    ["tldnWorkRmLightSwitch01On", 1, 0], 
    ["tldnWorkRmLightSwitch02On", 1, 0], 
    ["tldnWorkRmLightSwitch03On", 1, 0], 
    ["tldnCabinDrained", 1, 0], 
    ["tldnHatchOpen", 1, 0], 
    ["tldnHatchLocked", 1, 1], 
    ["tldnAquariumOpen", 1, 0], 
    ["tldnAquariumLightOn", 1, 0], 
    ["tldnShuttersOpen", 1, 0], 
    ["tldnNexusStationVis", 1, 1], 
    ["tldnOuterDoorClosed", 1, 1], 
    ["tldnCatwalkDoorClosed", 1, 1], 
    ["tldnShroomieGateUp", 1, 1], 
    ["tldnBrokenBridgeLowered", 1, 0], 
    ["tldnBahroDoorClosed", 1, 1], 
    ["tldnSecretDoorOpen", 1, 0], 
    ["tldnTieDyeVis", 1, 0], 
    ["tldnRockAVaporHit", 1, 0], 
    ["tldnRockBVaporHit", 1, 0], 
    ["tldnRockCVaporHit", 1, 0], 
    ["tldnRockDVaporHit", 1, 0], 
    ["tldnSlaveActivePanel01", 1, 1], 
    ["tldnSlaveActivePanel02", 1, 0], 
    ["tldnSlaveActivePanel03", 1, 1], 
    ["tldnSlaveActivePanel04", 1, 0], 
    ["tldnSlaveActivePanel05", 1, 1], 
    ["tldnSlaveActivePanel06", 1, 0], 
    ["tldnSlaveActivePanel07", 1, 0], 
    ["tldnLagoonBridgeStuck", 1, 1], 
    ["tldnLagoonBridgeRaised", 1, 1], 
    ["ShroomieTotalTimesSeen", 1, 0], 
    ["ShroomieTimeLastSeen", 1, 0], 
    ["tldnSlaveActivePlate01", 1, 0], 
    ["tldnSlaveActivePlate02", 1, 0], 
    ["tldnSlaveActivePlate03", 1, 0], 
    ["tldnSlaveActivePlate04", 1, 0], 
    ["tldnSlaveActivePlate05", 1, 0], 
    ["tldnSlaveActivePlate06", 1, 0], 
    ["tldnSlaveActivePlate07", 1, 0], 
    ["tldnSlaveCaveSecretDoorVis", 1, 0], 
    ["tldnSlaveCaveSecretDoorOpen", 1, 0], 
]

lstSdlTwo = [
    ["tldnBucketState", 2, 0], 
    ["tldnRiders", 4, 0], 
]

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

# 
def ShowAllSdl():
    ageSdl = PtGetAgeSDL()
    for s in lstSdlOne:
        print "SDL '{0}' : {1}".format(s[0], ageSdl[s[0]])
    for s in lstSdlTwo:
        print "SDL '{0}' : {1}".format(s[0], ageSdl[s[0]])

#
def ResetAge():
    ageSdl = PtGetAgeSDL()
    for s in lstSdlOne:
        name = s[0]
        value = s[2]
        ageSdl[name] = (value,)
    ageSdl["tldnBucketState"] = (0, 0)
    ageSdl["tldnRiders"] = (-1, -1, -1, 0)


#

"""
(02/25 13:53:35) SDL 'tldnBucketState' : (0, 1)
(02/25 13:53:35) SDL 'tldnRiders' : (-1, -1, -1, -1)

"""