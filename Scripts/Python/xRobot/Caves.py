"""
    Cavern Tour in Caves 2017-06-09 :
        Last Zeke order : 
        I would like to do the Silo, first, then the hourglass cave, then the cleft cave and wrap up with the Rudenna cave.
        - Silo
        - Pellet2
        - Cleft
        - Rudenna

        Larry F (29 mai (Il y a 11 jours)) a Guild, Stone, moi, zeke365
        Week 11 : Er'cana Silo / Bahro caves wish list.

        The Er'cana Silo: 
        I have things I can say there, and I know that r'Tay can say a fair amount about the history 
        of the Ashem'en district.

        When there, the only things we really want to do that the techs would be concerned with is 
        a) showing all the pellet drop effects on cue, and 
        b) arranging to either take the guests outside or above the enclosure so they can see the 
        scenery that's past the wall that surrounds the catwalks.

        The Bahro Caves: 
        There are several caves to cover.

        The Cleft cave: 
        After arriving in the Cleft, we want to warp to the bottom of the ladder in the cave. 
        If the ladder into the cave can be removed so that the guests can't climb on it and get stuck, 
        so much the better. 
        No other special effects needed.

        The Hourglass cave: 
        After warping there, we want to make the Bahroglyphs appear. 
        Dropping pellets on a timer is okay, but if you can find a way to bypass that and just 
        turn them on continuously, so much the better. 
        On request, we want the lighting to be changed so that the details are in contrast and we can see 
        them more clearly. 
        While I doubt it can be done, it would be great if a mechanism could be found to only show 
        one glyph at a time, making it easier for the guests and guides to tell which one is being 
        talked about. 
        But since they are a set, no grief from me if there's no way to do it 
        -- we'll muddle through the way we have in previous years.

        The Rudenna cave: 
        If you can change the set dressings so that we see the various versions of that cave for each 
        of the wedge sets, so much the better. 
        If not, then just cycling between the two color schemes for the pillar quest will do.

        At the end of the tour, I'll close with a talk about Rudenna, the cavern below the cave. 
        We want to disable the panic link zones and get an on-lake effect at water level in the cave, s
        o the guests can run around on the surface of the water for a little while before you start playing 
        around with the model. 
        That's been very difficult to do in the past, but hope springs eternal. ^_^
"""

"""
    "PrimeCave":["LiveBahroCaves", "LiveBahroCaves", "74b81313-c5f4-4eec-8e21-94d55e59ea8a", "Mir-o-Bot's Prime", ""],
    "PodsCave":["LiveBahroCaves", "LiveBahroCaves", "9b764f14-2d0e-493e-aa4a-e7ed218e3168", "Mir-o-Bot's Pods", ""],
    "EderCave":["LiveBahroCaves", "LiveBahroCaves", "1c9388c2-e4da-4e2e-a442-a0f58ad216b9", "Mir-o-Bot's Eder", ""],
    "Rudenna":["BahroCave", "BahroCave", "a8f6a5a6-4e5e-4d3f-9160-a9b75f0768c5", "Mir-o-Bot's Rudenna", ""],
    "pelletcave":["Pellet Cave", "PelletBahroCave", "13c1fdfc-44e2-4230-803a-147d8e6918a0", "Mir-o-Bot's (top)", ""], 
    "pellet1":["Pellet Cave", "PelletBahroCave", "13c1fdfc-44e2-4230-803a-147d8e6918a0", "Mir-o-Bot's (top)", "LinkInWithPellet"], 
    "pellet2":["Pellet Cave", "PelletBahroCave", "13c1fdfc-44e2-4230-803a-147d8e6918a0", "Mir-o-Bot's (bottom)", "LinkInPointLower"], 
"""
"""
    Sky.py
        <ChangeSky>
            Start(delay=None, start=None, end=None, density=None)
            Stop()
    Pellet.py
        pellet(respnum=0)
        symbol(quad="N", n=1, bOn=True)
        machine(n=0)
        drop()
        <AutoPellet>
            Start(delay=None)
            Stop()
        Show(n=-1)
    BahroCaveFloor.py
        Floor(en=True)
"""
from Plasma import *
import Sky
import Pellet
import BahroCaveFloor
import xBotAge

#
def ChangeSky(bOn=True):
    if bOn:
        Sky.Start(delay=0.5, start=0, end=0, density=0)
    else:
        Sky.Stop()

#
def AutoPellet(bOn=True):
    if bOn:
        Pellet.Start(delay=19)
    else:
        Pellet.Stop()

#
def Show(nb=-1):
    Pellet.Show(n=nb)


"""
pages :
    BahroCave :
        pages = ["YeeshaCave"]

    LiveBahroCaves :
        pages = ["BlueSpiralCave", "PODcave", "MINKcave", "POTScave"]

    PelletBahroCave :
        pages = ["Cave"]
PtPageInNode(pages)
PtConsoleNet("Nav.PageInNode {0}".format(pages[i]) ,1)
"""
#
def PageInAllCaves():
    pages = ["YeeshaCave", "BlueSpiralCave", "PODcave", "MINKcave", "POTScave", "Cave"]
    #PtPageInNode(pages)
    for page in pages:
        PtConsoleNet("Nav.PageInNode {0}".format(page), 1)

#
def PageOutAllCaves():
    pages = ["YeeshaCave", "BlueSpiralCave", "PODcave", "MINKcave", "POTScave", "Cave"]
    #PtPageOutNode(page, 1)
    for page in pages:
        PtConsoleNet("Nav.PageOutNode {0}".format(page), 0)

"""
Spawn Points :
    BahroCave :
        sp = ["LinkInPointGarden", "LinkInPointGarrison", "LinkInPointKadish", "LinkInPointTeledahn"]

    LiveBahroCaves :
        "BlueSpiralCave" 
            sp = ["LinkInPointDelin", "LinkInPointTsogal"]
        "PODcave" 
            sp = ["LinkInPointDereno", "LinkInPointNegilahn", "LinkInPointPayiferen", "LinkInPointTetsonot"]
        "MINKcave" 
            sp = ["LinkInPointMinkata"]
        "POTScave"
            sp = ["LinkInPointAhnonay", "LinkInPointErcana"]

    PelletBahroCave :
        sp = ["LinkInPointDefault", "LinkInWithPellet", "LinkInPointLower"]
"""
# BahroCave                     : 0 a 3
# LiveBahroCaves BlueSpiralCave : 4 et 5
# LiveBahroCaves PODcave        : 6 a 9
# LiveBahroCaves MINKcave       : 10
# LiveBahroCaves POTScave       : 11 et 12
# PelletBahroCave               ! (13), 14 et 15
def Spawn(spawnPointNumber=0):
    # BahroCave :
    sp = ["LinkInPointGarden", "LinkInPointGarrison", "LinkInPointKadish", "LinkInPointTeledahn"]
    # LiveBahroCaves :
    #    "BlueSpiralCave" 
    sp += ["LinkInPointDelin", "LinkInPointTsogal"]
    #    "PODcave" 
    sp += ["LinkInPointDereno", "LinkInPointNegilahn", "LinkInPointPayiferen", "LinkInPointTetsonot"]
    #    "MINKcave" 
    sp += ["LinkInPointMinkata"]
    #    "POTScave"
    sp += ["LinkInPointAhnonay", "LinkInPointErcana"]
    # PelletBahroCave :
    sp += ["LinkInPointDefault", "LinkInWithPellet", "LinkInPointLower"]
    
    print "Spawn ({0})".format(spawnPointNumber)
    
    pos = None
    if isinstance(spawnPointNumber, int):
        print "Spawn ({0}) => sp : {1}".format(spawnPointNumber, sp[spawnPointNumber])
        #pos = xBotAge.GetSPCoord(spawnPointNumber)
        """
        try:
            so = PtFindSceneobject(spName, PtGetAgeName())
        except NameError:
            so = None
        if isinstance(so, ptSceneobject):
            pos = so.getLocalToWorld()
        else:
            pos = None
        """
        sol = PtFindSceneobjects(sp[spawnPointNumber])
        print "Spawn ({0}) => sol : {1}".format(spawnPointNumber, sol)
        
        so = None
        if len(sol) > 0:
            so = sol[0]
            print "Spawn ({0}) => so : {1}".format(spawnPointNumber, so)
        if isinstance(so, ptSceneobject):
            pos = so.getLocalToWorld()
            print "Spawn ({0}) => pos : {1}".format(spawnPointNumber, pos)
        
    if isinstance(pos, ptMatrix44):
        print "Spawn ({0}) => pos : ptMatrix44".format(spawnPointNumber)
        soAvatar = PtGetLocalAvatar()
        print "Spawn ({0}) => soAvatar : {0}".format(soAvatar)
        soAvatar.netForce(1)
        soAvatar.physics.warp(pos)


#
def WarpToSpawnPoint(self, cFlags, args = []):
    #self.chatMgr.AddChatLine(None, "> WarpToSpawnPoint", 3)
    if len(args) < 2:
        return 0
    myself = PtGetLocalPlayer()
    player = args[0]
    try:
        spawnPointNumber = int(args[1])
        spawnPointAlias = None
    except:
        spawnPointNumber = None
        spawnPointAlias = args[1]
    
    if not isPlayerInAge(player):
        SendChatMessage(self, myself, [player], "You must be in my age, use link to join me." , cFlags.flags)
        return 1
    if spawnPointNumber is not None:
        pos = xBotAge.GetSPCoord(spawnPointNumber)
        if isinstance(pos, ptMatrix44):
            spName = xBotAge.GetSPName(spawnPointNumber)
            SendChatMessage(self, myself, [player], spName , cFlags.flags)
            #self.chatMgr.AddChatLine(None, "> " + spName, 3)
        else:
            SendChatMessage(self, myself, [player], "Unknown spawn point!" , cFlags.flags)
    elif spawnPointAlias is not None:
        pos = xBotAge.GetSPByAlias(spawnPointAlias)[0]
        spName = xBotAge.GetSPByAlias(spawnPointAlias)[1]
        SendChatMessage(self, myself, [player], spName , cFlags.flags)
        #self.chatMgr.AddChatLine(None, "> " + spName, 3)
    else:
        return 0
    if isinstance(pos, ptMatrix44):
        soAvatar = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
        soAvatar.netForce(1)
        soAvatar.physics.warp(pos)
    return 1
