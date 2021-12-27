# -*- coding: cp1252 -*-

"""
    V1 : 27/02/2016
        ** Zeke's and Larry's wish lists **
            ...
            
    V2 : 08/07/2017
        ** Larry's wish lists (First part) **
            Guild Hall: 
                We’ll want to go up on top to see the structures up there. 
                Not in the little space around the capital structure, 
                but alongside so that they can see the entire building that sits atop the rock face. 
                An invisible Jalak pillar platform should do for that.

            Palace: 
                We want to show all of the different buildings that make up the palace, 
                including the rooftop at the back with the four angled spikes on it. 
                We also want to show the palace courtyard, which is at the top of the stairs behind the locked gate.

            Library: 
                Any unusual angles we can show will be good, 
                but the main trick there will be taking the guests down farther than they can normally go into 
                the lower floors. 
                The tarpaulin level will do, but if you can take us lower than that, so much the better.

            Canyon Bridge: 
                No special effects needed.

            Concert Hall: 
                we want to show them as much of it as we can. 
                The stage structure in the canyon has a solid surface on the lower level, 
                but if we can stand outside and see the whole thing, that would be better for the tour. 
                We also want to show them the outside of the foyer from over the lake, 
                so they can see how much detail it has. 
                Finally, an overhead view of the building and the ridge it is set in would be great, 
                so that the guests can get an idea of its size and shape. 
                We want them to see both ends of the building at the same time from above.

            Canyon Mall: 
                I can’t think of anything there that requires a special effect.


    V3 : 15/07/2017
        ** Larry's wish lists (Second part) **
            Museum: 
                I’d like to take the guests down to the lower floor, but that’s not essential. 
                Remove the barricades at the end of the room to allow the guests to get to the stairs. 
                It’s a small thing, but not being able to go there frustrated me for years, 
                and I imagine other people may feel the same.

            Tokotah I: 
                Remove the DRC tent, boxes, and table from in front of it so the guests can see an 
                unobstructed view of the building.

            Tokotah II: 
                There are many features on the roof of the building that cannot be seen from the 
                Great Stairs. 
                There are two or three small courtyards, one above the side entrance to the Kahlo Pub, 
                one at the lower end of the building above the DRC tent with the generator, and IIRC, 
                there’s a third next to that last one. 
                Above the courtyard over the side entrance, there is a staircase that leads from the 
                interior of the building up through another balcony, and on to a balcony and door 
                into the highest part of the building, the part under the Tokotah Rooftop. 
                Anything that can be done to view those features would be good.

            We’ve never included the Tokotah rooftop in the tours before. Should we do that this time?

            The Kahlo Pub: 
                If you can remove the rubble blocking in the corridor, that would make it easier for 
                a group to get into the pub. 
                It would be a nice touch if you can page in the wreaths around the Explorer Memorial viewer.

            The Ferry Terminal: 
                Page in the light meter on the Ferry docks. If you can remove the barricade from the 
                front of the terminal, so we can get to the door, so much the better. 
                The same can be said for the rubble along the wall on the front side of the terminal 
                – cleaning that up would be a novel experience for the guests. 
                We will want to take the tour group out on the lake in front of the terminal to show 
                the damage to the building at some point, as well as over to the main harbor entrance 
                near the library. 
                A platform in the air above the lake in front of the main terminal building high enough 
                to see the lens on top of the tower would be something we’ve never done before. 
                We’ll also want to take the group up on top of the back end of the main terminal 
                building to see some of the structures there.

            The Waterfront: 
                Please remove the gate on the other side of the little cave past the Nexus terminal, 
                the one that blocks us from the curved walkway.

        ** Guild of Instructors wish **
            If the floor behind the rubble inside the Kahlo Pub is solid (and not phantom), 
            remove that rubble to allow the guests to see the room on the other side.

"""
from Plasma import *
#from PlasmaTypes import *
#from xPsnlVaultSDL import *
#import time

import math
import sdl
import Platform
import Ride

"""
    STATEDESC city
    {
    # This version has been updated in build UruTap
        VERSION 43

    # Boolean variables
        VAR BOOL    islmCityBlocker01Vis[1]    DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL    islmCityBlocker02Vis[1]    DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL    islmCityBlocker03Vis[1]    DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL    islmCityBlocker04Vis[1]    DEFAULT=1 DEFAULTOPTION=VAULT
        VAR BOOL    islmCityBlocker05Vis[1]    DEFAULT=1 DEFAULTOPTION=VAULT
        VAR BOOL    islmCityBlocker06Vis[1]    DEFAULT=1 DEFAULTOPTION=VAULT
        VAR BOOL    islmCityBlocker07Vis[1]    DEFAULT=1 DEFAULTOPTION=VAULT
        VAR BOOL    islmCityBlocker08Vis[1]    DEFAULT=1 DEFAULTOPTION=VAULT
        VAR BOOL    islmCityBlocker09Vis[1]    DEFAULT=1 DEFAULTOPTION=VAULT
        VAR BOOL    islmCityBlocker10Vis[1]    DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL    islmCityBlocker11Vis[1]    DEFAULT=1 DEFAULTOPTION=VAULT
        VAR BOOL    islmCityBlocker12Vis[1]    DEFAULT=1 DEFAULTOPTION=VAULT
        VAR BOOL    islmCityBlocker13Vis[1]    DEFAULT=1 DEFAULTOPTION=VAULT
        VAR BOOL    islmCityBlocker14Vis[1]    DEFAULT=1 DEFAULTOPTION=VAULT
        VAR BOOL    islmCityBlocker15Vis[1]    DEFAULT=1 DEFAULTOPTION=VAULT
        
        VAR BOOL    islmJourneyCloth01Vis[1]    DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL    islmJourneyCloth02Vis[1]    DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL    islmJourneyCloth03Vis[1]    DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL    islmJourneyCloth04Vis[1]    DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL    islmJourneyCloth05Vis[1]    DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL    islmBahroShoutLibraryRun[1]    DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL    islmBahroShoutPalaceRun[1]    DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL    islmBahroShoutFerryRun[1]    DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL    islmLakeLightMeterVis[1]    DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL    islmReaderBoardVis[1]    DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL    islmS1FinaleBahro[1]    DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL    islmS1FinaleBahroCity1[1]    DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL    islmS1FinaleBahroCity2[1]    DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL    islmS1FinaleBahroCity3[1]    DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL    islmS1FinaleBahroCity4[1]    DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL    islmS1FinaleBahroCity5[1]    DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL    islmS1FinaleBahroCity6[1]    DEFAULT=0 DEFAULTOPTION=VAULT

    # Kadish gallery stuff
        VAR BOOL    kdshJourneyCloth07Vis[1]    DEFAULT=1 DEFAULTOPTION=VAULT
        VAR BOOL    islmKadishGalleryDoorVis[1]    DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL    islmKadishGalleryDoorsOn[1]    DEFAULT=0
        VAR BOOL    islmKadishGalleryDoor1Closed[1]    DEFAULT=1
        VAR BOOL    islmKadishGalleryDoor2Closed[1]    DEFAULT=1
        
        VAR BOOL    islmTreasureBook01Vis[1]    DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL    islmTreasureBook06Vis[1]    DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL    islmTreasureBook08Vis[1]    DEFAULT=0 DEFAULTOPTION=VAULT # links into Garrison Prison
        VAR BOOL    islmGuildHallConstructionVis[1]    DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL    islmDRCTentVis[1]    DEFAULT=1 DEFAULTOPTION=VAULT
        VAR BOOL    islmPlayerMap01Vis[1]    DEFAULT=1 DEFAULTOPTION=VAULT
        VAR BOOL    islmShroomiePictVis[1]    DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL    islmFerryTerminalCratesVis[1]    DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL    islmStepCratesVis[1]    DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL    islmTeledahnLinkCourtyardVis[1]    DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL    islmGreatZeroVis[1]    DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL    islmTokotahMeetingsVis[1]    DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL    islmExplosionRun[1]    DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL    islmUnderwaterHarborLightsRun[1]    DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL    islmScreamRun[1]    DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL    islmTeledahnLinkLibraryExteriorVis[1]    DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL    islmFerryDoorFunc[1]    DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL    islmCanyonConstructionVis[1]    DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL    islmGalleryThemePlayerVis[1]    DEFAULT=0 DEFAULTOPTION=VAULT

        VAR BOOL	islmTokotahJournal01Vis[1] DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL	islmTokotahJournal02Vis[1] DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL	islmTokotahJournal03Vis[1] DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL	islmTokotahJournal04Vis[1] DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL	islmTokotahJournal05Vis[1] DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL	islmTokotahJournal06Vis[1] DEFAULT=1 DEFAULTOPTION=VAULT
        VAR BOOL	islmTokotahJournal07Vis[1] DEFAULT=1 DEFAULTOPTION=VAULT
        VAR BOOL	islmTokotahJournal08Vis[1] DEFAULT=1 DEFAULTOPTION=VAULT
        VAR BOOL	islmTokotahJournal09Vis[1] DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL	islmTokotahJournal10Vis[1] DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL	islmTokotahJournal11Vis[1] DEFAULT=1 DEFAULTOPTION=VAULT
        VAR BOOL	islmRinerefMTKJournalVis[1] DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL	islmAileshMTKJournalVis[1] DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL	islmShomatMTKJournalVis[1] DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL	islmJakreenMTKJournalVis[1] DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL	islmVeeshaMTKJournalVis[1] DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL	islmMararonMTKJournalVis[1] DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL	islmKoreenMTKJournalVis[1] DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL	islmAhlsendarTKJournalVis[1] DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL	islmSolathMTKJournalVis[1] DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL	islmMeertaMTKJournalVis[1] DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL	islmGanMTKJournalVis[1] DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL	islmBenashirenMTKJournalVis[1] DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL	islmHemelinMTKJournalVis[1] DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL	islmNaygenMTKJournalVis[1] DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL	islmHinashMTKJournalVis[1] DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL	islmNeedrahMTKJournalVis[1] DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL	islmRakeriMTKJournalVis[1] DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL	islmTejaraMTKJournalVis[1] DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL	islmTiamelMTKJournalVis[1] DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL	islmKedriMTKJournalVis[1] DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL	islmLemashalMTKJournalVis[1] DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL	islmIshekMTKJournalVis[1] DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL	islmLoshemaneshMTKJournalVis[1] DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL	islmJiMTKJournalVis[1] DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL	islmDimathMTKJournalVis[1] DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL	islmYableshanMTKJournalVis[1] DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL	islmEmenMTKJournalVis[1] DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL	islmMeemenMTKJournalVis[1] DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL	islmAdeshMTKJournalVis[1] DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL	islmLanarenMTKJournalVis[1] DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL	islmAsemlefMTKJournalVis[1] DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL	islmJaronMTKJournalVis[1] DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL	islmRikoothMTKJournalVis[1] DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL	islmKerathMTKJournalVis[1] DEFAULT=0 DEFAULTOPTION=VAULT


    # Reward Clothing
        VAR BOOL	islmHardHat01Vis[1] DEFAULT=1 DEFAULTOPTION=VAULT
        VAR BOOL	islmHardHat02Vis[1] DEFAULT=1 DEFAULTOPTION=VAULT
        VAR BOOL	islmHardHat03Vis[1] DEFAULT=1 DEFAULTOPTION=VAULT
        VAR BOOL	islmHardHat04Vis[1] DEFAULT=1 DEFAULTOPTION=VAULT
        VAR BOOL	islmHardHat05Vis[1] DEFAULT=1 DEFAULTOPTION=VAULT
        VAR BOOL	islmHardHat06Vis[1] DEFAULT=1 DEFAULTOPTION=VAULT
        VAR BOOL    islmFirstWeekVis[1] DEFAULT=0 DEFAULTOPTION=VAULT

    # Seasonal and Holidays
        VAR BOOL	islmMinorahVis[1] DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL	islmMinorahNight01Vis[1] DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL	islmMinorahNight02Vis[1] DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL	islmMinorahNight03Vis[1] DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL	islmMinorahNight04Vis[1] DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL	islmMinorahNight05Vis[1] DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL	islmMinorahNight06Vis[1] DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL	islmMinorahNight07Vis[1] DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL	islmMinorahNight08Vis[1] DEFAULT=0 DEFAULTOPTION=VAULT

     
    # State variables
        VAR BYTE    islmDRCStageState[1]    DEFAULT=1 DEFAULTOPTION=VAULT
        VAR BYTE    islmCityBlocker16State[1]    DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BYTE    islmScreamChance[1]     DEFAULT=0 DEFAULTOPTION=VAULT

    # Age Mechanics
        VAR BOOL    islmLibraryLowerDoorClosed[1]    DEFAULT=1
        VAR BOOL    islmMuseumDoorClosed[1]    DEFAULT=1
        VAR BOOL    islmMuseumDoorFunc[1]    DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BYTE    islmMuseumDoorOps[1]    DEFAULT=0

    #GZ Marker visibility
        VAR BOOL    islmGZMarkerVis[1]    DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL    islmGZBeamVis[1]    DEFAULT=0 DEFAULTOPTION=VAULT

    # Randomized objects
        VAR BOOL    islmTreasureBook01Enabled[1]    DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BYTE    islmTreasureBook01Chance[1]     DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL    islmTreasureBook01Proximity[1]  DEFAULT=0 DEFAULTOPTION=VAULT

        VAR BOOL    islmTreasureBook06Enabled[1]    DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BYTE    islmTreasureBook06Chance[1]     DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL    islmTreasureBook06Proximity[1]  DEFAULT=0 DEFAULTOPTION=VAULT

        VAR BOOL    islmTreasureBook08Enabled[1]    DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BYTE    islmTreasureBook08Chance[1]     DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL    islmTreasureBook08Proximity[1]  DEFAULT=0 DEFAULTOPTION=VAULT

    # Museum variables
        VAR BOOL    islmNegilahnLinkingBookVis[1]  DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL    islmTodelmerLinkingBookVis[1]  DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL    islmNegilahnJournalVis[1]  DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL    islmTodelmerJournalVis[1]  DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL    islmNegilahnCreatureChartVis[1]  DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL    islmPodMapVis[1]  DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL    islmDerenoLinkingBookVis[1]  DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL    islmPayiferenLinkingBookVis[1]  DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL    islmTetsonotLinkingBookVis[1]  DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL    islmYeeshaPageMoonsVis[1]  DEFAULT=0 DEFAULTOPTION=VAULT

    # Kahlo Pub Event Variables
        VAR BOOL    islmCityBlocker17Vis[1]    DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BYTE	islmKahloPubHallCollapse[1]    DEFAULT=0 DEFAULTOPTION=VAULT


    # Library variables
        VAR BOOL    islmMinkataLinkingBookVis[1]  DEFAULT=0 DEFAULTOPTION=VAULT
        VAR BOOL    islmJalakLinkingBookVis[1]    DEFAULT=0 DEFAULTOPTION=VAULT

    # Memorial Imager
        VAR INT     MemorialImagerStartTime[1]       DEFAULT=0   DISPLAYOPTION=hidden
        VAR BOOL    islmMemorialImagerVis[1]  	 DEFAULT=0 DEFAULTOPTION=VAULT
    }
"""
#

#Cette fonction ne s'utilise pas seule, elle est appelee par Courant()
def RunResp(key, resp, stateidx=None, netForce=1, netPropagate=1, fastforward=0):
    nt = ptNotify(key)
    nt.addReceiver(resp)
    nt.netPropagate(netPropagate)
    nt.netForce(netForce)
    if stateidx != None:
        nt.addResponderState(stateidx)
    if fastforward:
        nt.setType(PtNotificationType.kResponderFF)
        nt.netPropagate(0)
        nt.netForce(0)
    nt.setActivate(1.0)
    nt.send()

# 
#================================================

#

#
def wa(where=None):
    #avCentre = PtGetLocalAvatar()
    #mat = avCentre.getLocalToWorld()
    mat = None
    if where is None or where not in range(1, 5):
        mat = PtGetLocalAvatar().getLocalToWorld()
    else:
        if where == 1:
            tupPos = ((0.98276501894, 0.184859260917, 0.0, 23.3415126801), (-0.184859260917, 0.98276501894, 0.0, 54.0308570862), (0.0, 0.0, 1.0, -0.0328424945474), (0.0, 0.0, 0.0, 1.0))
        elif where == 2:
            tupPos = ((-0.897078573704, -0.44187015295, 0.0, 649.721862793), (0.44187015295, -0.897078573704, 0.0, -877.984619141), (0.0, 0.0, 1.0, 9445.71386719), (0.0, 0.0, 0.0, 1.0))
        elif where == 3:
            tupPos = ((0.00954949762672, -0.999954581261, 0.0, -102.545890808), (0.999954581261, 0.00954949762672, 0.0, 54.9582672119), (0.0, 0.0, 1.0, 10563.0976562), (0.0, 0.0, 0.0, 1.0))
        elif where == 4:
            tupPos = ((-0.748968303204, 0.662607133389, 0.0, 1560.00488281), (-0.662607133389, -0.748968303204, 0.0, -51.4498291016), (0.0, 0.0, 1.0, 10171.9091797), (0.0, 0.0, 0.0, 1.0))
        elif where == 5:
            tupPos = ((-0.937420606613, -0.3482016325, 0.0, 993.751708984), (0.3482016325, -0.937420606613, 0.0, -455.378509521), (0.0, 0.0, 1.0, 9424.86523438), (0.0, 0.0, 0.0, 1.0))
        mat = ptMatrix44()
        mat.setData(tupPos)
    
    #recuperer tous les joueurs
    playerList = PtGetPlayerList()
    playerList.append(PtGetLocalPlayer())
    soAvatarList = map(lambda player: PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject(), playerList)
    for soavatar in soAvatarList:
        #faire flotter tout le monde
        soavatar.netForce(1)
        soavatar.physics.disable()
        soavatar.physics.enable(0)
        soavatar.netForce(1)
    for soavatar in soAvatarList:
        #deplacer les gens
        soavatar.physics.warp(mat)
        soavatar.netForce(1)
    for soavatar in soAvatarList:
        #reactiver la physique pour tous
        soavatar.physics.enable(1)
        soavatar.netForce(1)

# Find scene objects with name like soName in all loaded districts (aka pages or prp files)
# ex.: soName = "Bahro*Stone" will be transformed in regexp "^.*Bahro.*Stone.*$"
def FindSOName(soName):
    import re
    cond = "^.*" + soName.replace("*", ".*") + ".*$"
    try:
        pattern = re.compile(cond, re.IGNORECASE)
    except:
        return list()
    strList = soName.split("*")
    nameList = list()
    for str in strList:
        nameList.extend(map(lambda so: so.getName(), PtFindSceneobjects(str)))
    nameList = list(set(nameList))
    nameList = filter(lambda x: pattern.match(x) != None, nameList)
    return nameList

# Find scene objects with name like soName in all loaded districts (Warning, it includes GUI)
def FindSOLike(soName):
    nameList = FindSOName(soName)
    soList = list()
    for soName in nameList:
        sol = PtFindSceneobjects(soName)
        soList.extend(sol)
    return soList

# Remove the panic regions, I assume that all the panic links contain "Panic" or "panic" in there names.
def DisablePanicLinks():
    sol = FindSOLike("anic")
    for so in sol:
        so.netForce(1)
        so.physics.disable()

#
def panic():
    PtConsoleNet("Avatar.Spawn.DontPanic" , 1)

# !toggle Wreat  1 1
# !toggle Blocker  1 0

# toggles bool sdl (for the city tour 1)
def togglesdl(name="lm"):
    dicNames = {
        "lm":"islmLakeLightMeterVis", 
        "gh":"islmGuildHallConstructionVis", 
        "tent":"islmDRCTentVis", 
        "expl":"islmExplosionRun", 
        "scream":"islmScreamRun", 
        "tldn":"islmTeledahnLinkLibraryExteriorVis", 
        "canyon":"islmCanyonConstructionVis", 
        "kahlob":"islmCityBlocker17Vis", 
        "kahloc":"islmKahloPubHallCollapse", 
        #"mem":"MemorialImagerStartTime", #INT
        "mem":"islmMemorialImagerVis", 
    }
    if (name in dicNames.keys()):
        sdl.ToggleBoolSDL(dicNames[name])
    else:
        print("wrong sdl name")

# long platform(where=1)
def platform(where=None):
    matPos = None
    if where is None or where not in range(1, 5):
        matPos = PtGetLocalAvatar().getLocalToWorld()
    else:
        #Ahnonay
        if where == 1:
            tupPos = ((0.98276501894, 0.184859260917, 0.0, 23.3415126801), (-0.184859260917, 0.98276501894, 0.0, 54.0308570862), (0.0, 0.0, 1.0, -0.0328424945474), (0.0, 0.0, 0.0, 1.0))
        elif where == 2:
            tupPos = ((-0.897078573704, -0.44187015295, 0.0, 649.721862793), (0.44187015295, -0.897078573704, 0.0, -877.984619141), (0.0, 0.0, 1.0, 9445.71386719), (0.0, 0.0, 0.0, 1.0))
        elif where == 3:
            tupPos = ((0.00954949762672, -0.999954581261, 0.0, -102.545890808), (0.999954581261, 0.00954949762672, 0.0, 54.9582672119), (0.0, 0.0, 1.0, 10563.0976562), (0.0, 0.0, 0.0, 1.0))
        elif where == 4:
            tupPos = ((-0.748968303204, 0.662607133389, 0.0, 1560.00488281), (-0.662607133389, -0.748968303204, 0.0, -51.4498291016), (0.0, 0.0, 1.0, 10171.9091797), (0.0, 0.0, 0.0, 1.0))
        elif where == 5:
            tupPos = ((-0.937420606613, -0.3482016325, 0.0, 993.751708984), (0.3482016325, -0.937420606613, 0.0, -455.378509521), (0.0, 0.0, 1.0, 9424.86523438), (0.0, 0.0, 0.0, 1.0))
        matPos = ptMatrix44()
        matPos.setData(tupPos)
        
    Platform.CreatePlatform2(bShow=False, matAv=matPos)

# Plateforme speciale pour Tokotah 2
def platok2():
    Platform.CreatePlatformForTokotah2()

#========================================================
"""
    aliasCitySP = {
        "fg":"LinkInPointBahro-FerryGate",          # = sp  1 # Ferry gate : fg     *
        "fr":"LinkInPointBahro-FerryRoof",          # = sp  2 # Ferry roof : fr     *
        "oh":"LinkInPointBahro-OperaHouse",         # = sp  3 # Opera house : oh    *
        "tr":"LinkInPointBahro-TokotahRoof",        # = sp  4 # Tokotah roof : tr   *
        "gsr":"LinkInPointBahro-GreatStairRoof",    # = sp  5 # Kahlo roof : kr     **
        "kr":"LinkInPointBahro-GreatStairRoof",     # = sp  5 # Kahlo roof : kr     **
        "lr":"LinkInPointBahro-LibraryRoof",        # = sp  6 # Library roof : lr   *
        "pb":"LinkInPointBahro-PalaceBalcony",      # = sp  7 # Palace roof : pr    **
        "pr":"LinkInPointBahro-PalaceBalcony",      # = sp  7 # Palace roof : pr    **
        "ferry":"LinkInPointFerry",                 # = sp  8 # 
        "concert":"LinkInPointConcertHallFoyer",    # = sp  9 # Concert hall : ch   **
        "ch":"LinkInPointConcertHallFoyer",         # = sp  9 # Concert hall : ch   **
        "alley":"LinkInPointDakotahAlley",          # = sp 10 # 
        "greattree":"LinkInPointGreatTree",         # = sp 11 # 
        "islmlib":"LinkInPointIslmLibrary",         # = sp 12 # 
        "library":"LinkInPointLibrary",             # = sp 13 # 
        "palace":"LinkInPointPalace",               # = sp 14 # 
        "gallery":"LinkInPointKadishGallery",       # = sp 15 # Kadish gallery : kg *
        "islm1":"Perf-SpawnPointIslm01",            # = sp 16 # 
        "islm2":"Perf-SpawnPointIslm02",            # = sp 17 # 
        "islm3":"Perf-SpawnPointIslm03",            # = sp 18 # 
        "islm4":"Perf-SpawnPointIslm04",            # = sp 19 # 
        "islm5":"Perf-SpawnPointIslm05",            # = sp 20 # 
        "museum":"MuseumIntStart",                  # = sp 21 # 
        "mu":"jrnlNegilahn",                        # = sp 22 # Museum : mu         xx
        "dakotah":"DakotahRoofPlayerStart",
        "trt":"DakotahRoofPlayerStart",
        "pb1":"PalaceBalcony01PlayerStart",
        "pb2":"PalaceBalcony02PlayerStart",
        "pb3":"PalaceBalcony03PlayerStart",
    }
"""
#========================================================
dicBot = {}
#
def CercleV(coef=2.0, avCentre=None):
    if avCentre is None:
        avCentre = PtGetLocalAvatar()
    #agePlayers = GetAllAgePlayers()
    # ne pas tenir compte des robots
    agePlayers = filter(lambda pl: not(pl.getPlayerID() in dicBot.keys()), PtGetPlayerList())
    i = 0
    n = len(agePlayers)
    print "nb de joueurs: %s" % (n)
    dist = float(coef * n) / (2.0 * math.pi)
    print "distance: %s" % (dist)
    for i in range(n):
        player = agePlayers[i]
        avatar = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
        angle = (float(i) * 2.0 * math.pi) / float(n)
        print "angle(%s): %s" % (i, angle)
        dx = float(dist)*math.cos(angle)
        #dy = float(dist)*math.sin(angle)
        dy = 0
        dz = float(dist)*math.sin(angle)
        matrix = avCentre.getLocalToWorld()
        matrix.translate(ptVector3(dx, dy, dz))
        avatar.netForce(1)
        avatar.physics.warp(matrix)

#
class CircleAlarm:
    def onAlarm(self, en):
        CercleV(coef=2.0, avCentre=None)


# en ville les oiseaux b1 a b6
def ride(soName="b1", t=30.0):
    #recuperer tous les joueurs
    playerList = PtGetPlayerList()
    playerList.append(PtGetLocalPlayer())
    for player in playerList:
        playerName = player.getPlayerName()
        Ride.Suivre(objet=soName, Avatar=playerName, duree=t)
    #CercleV(coef=2.0, avCentre=None)
    PtSetAlarm(2, CircleAlarm(), 0)

"""
    * Au musee :
        - arrivee => !sp 21, //museum ou //mu
        - enlever invisibleBarricadeBlocker01 et invisibleBarricadeBlocker02 
            => !toggle Barricade  0 0
        - derriere les barricades => //find Elevator (ElevatorCamera01)
        - lower floor => platform()
    * Tokotah 1 ( = la place) :
        - arrivee 
            => !sp 11 //greattree
            => !sp 10 //alley
        - enlever tente, caisses, table
            => !toggle Tent  0 0
            => !toggle Crate  0 0
            => !toggle crate  0 0
            => !toggle Table  0 0
          ou
            togglesdl(name="tent")
    * Tokotah roof top :
        - arrivee => //trt, //dakotah
    * Tokotah 2 ( = sur le toit du kahlo pub) :
        - arrivee => !sp 5, //kr
        - plateforme => platok2()
    * Kahlo Pub :
        - arrivee => a pied !
        - montrer le memorial
            togglesdl(name="kahlob")    "islmCityBlocker17Vis", 
            togglesdl(name="kahloc")    "islmKahloPubHallCollapse", 
            togglesdl(name="mem")       "islmMemorialImagerVis", 
        - Acces pice du fond :
            platform()
            !toggle KpWallsCollision  0 0
    * Ferry Terminal :
        - arrivee => //ferry et autres ...
        - light mater
            togglesdl(name="lm")        "islmLakeLightMeterVis", 
        - barricades devant le terminal et autres:
            !toggle Barricade  0 0
            !toggle Rock  0 0
            !toggle Rubble  0 0
            !toggle Rub  0 0
            !toggle Crack  0 0
            !toggle crack  0 0
            !toggle Crate  0 0
            !toggle crate  0 0
            !toggle Blocker  0 0
            !toggle Proxy  0 0
            !toggle Door  1 0
            ?
            !toggle harborLakeSurfaceLight01  1 1
            !toggle harborLakeSurfaceLight02  1 1
            !toggle harborLakeSurfaceLight03  1 1
        - vues depuis le lac
            //onlake
            platform()
    * Water Front :
        - enlever porte : !toggle Door  1 0

            togglesdl(name="gh")        "islmGuildHallConstructionVis", 
            togglesdl(name="expl")      "islmExplosionRun", 
            togglesdl(name="scream")    "islmScreamRun", 
            togglesdl(name="tldn")      "islmTeledahnLinkLibraryExteriorVis", 
            togglesdl(name="canyon")    "islmCanyonConstructionVis", 

    ** ordre d'exploration de zeke :
        ferry termiral, 
        kalo pub, 
        tokadak alley, 
        and musuem
"""

#