
"""
V1 : 20/12/2014
V2 : 03/01/2016
** Larry's wish list **
    -1. Voir l'effet des pellets sur l'eclairage du Hood (ou de la ville).
    0. The only real need for the Silo is arranging it so that the different pellet drop effects can be played on demand.
    
    1. First off, there isn't an awful lot to be done with the Ahnonay cathedral, since nothing exists outside the interior model. 
       All that's needed is to get us there, and then to Ahnonay afterward. 
       A group warp is preferred for that step to avoid wasting time while everyone links through the book individually, but that's up to you, Stone and Mirphak.

    2. Ahnonay spheres 1 and 2 need to be set to their default starting states, so we see all of the conditions that exist when an explorer first arrives in them. 
       That's to allow us to talk about the quabs, ning trees, and other characteristics.

    3. We will need to visit each sphere in turn, 1 through 4, and warping the group is the most efficient way I know to keep control of it. 
       Again, if you have a better idea, go with it. 
       In sphere 4, if you can get us down to the base of the statue to see the mechanism down there, so much the better.

    4. We do not need to visit every one of the maintenance rooms, since there's little difference between them other than the numbers. 
       All that's really needed is to warp to control room 4 after the spheres have been toured. 
       When we get there, the hatch to the hub room should be closed by preference, but if you need to have it open, we'll roll with it.

    5. When we open the hatch, we will want to cycle the spheres so that the audience can see the gears work and the image on the screen change.

    6. We will skip riding the vogondola, since it's a major choke point. 
       Unless you can think of a way to move the whole group along the track simultaneously, it's just not worth it. 
       Instead, a warp to Kadish's offices will do just as well.

    7. Once we are in the offices, it would be great if we can warp the group over to the area outside the sphere machine, 
       as close as possible and with as wide an area of movement as possible. 
       When we are there, we'll want to rotate the spheres so that the audience can see the entire mechanism in motion from whatever angle they want. 
       Barring that, a small platform they can't fall off would do. 
       That should be placed on the opposite side of the machine from the offices, because that's where most of the moving parts are.
    
"""
from Plasma import *
from PlasmaTypes import *
from xPsnlVaultSDL import *
import time

import math
import sdl
import Platform


#------------
#max wiring
#------------

ActRotateSwitch   = ptAttribActivator(1,"clk: rotate spheres")
RespRotateSwitch   = ptAttribResponder(2,"resp: rotate spheres switch")
SDLWaterCurrent   = ptAttribString(3,"SDL: water current")
ActWaterCurrent   = ptAttribActivator(4,"clk: water current")
RespCurrentValve   = ptAttribResponder(5,"resp: water current valve",['on','off'])
WaterCurrent1   = ptAttribSwimCurrent(6,"water current 1")
WaterCurrent2   = ptAttribSwimCurrent(7,"water current 2")
WaterCurrent3   = ptAttribSwimCurrent(8,"water current 3")
WaterCurrent4   = ptAttribSwimCurrent(9,"water current 4")
RespCurrentChange   = ptAttribResponder(10,"resp: change the water current",['on','off'])
RespRotateSpheres   = ptAttribResponder(11,"resp: rotate the spheres")
SDLHutDoor   = ptAttribString(12,"SDL: hut door")
ActHutDoor   = ptAttribActivator(13,"clk: hut door switch")
RespHutDoorBeh   = ptAttribResponder(14,"resp: hut door switch",['open','close'])
RespHutDoor   = ptAttribResponder(15,"resp: hut door",['open','close'])


#---------
# globals
#---------

boolCurrent = 0
boolHutDoor = 0
actingAvatar = None
actingAvatarDoor = None

class ahnyIslandHut(ptResponder):

    def __init__(self):
        ptResponder.__init__(self)
        self.id = 5580
        self.version = 1

    def Courant(self, boolCurrent=0):
        if boolCurrent:
            RespCurrentChange.run(self.key,state='on',fastforward=1)
            print "OnInit, will now enable current"
            WaterCurrent1.current.enable()
            WaterCurrent2.current.enable()
            WaterCurrent3.current.enable()
            WaterCurrent4.current.enable()
        else:
            RespCurrentChange.run(self.key,state='off',fastforward=1)
            print "OnInit, will now disable current"
            WaterCurrent1.current.disable()
            WaterCurrent2.current.disable()
            WaterCurrent3.current.disable()
            WaterCurrent4.current.disable()

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

# open or close the bahro door ('open' = 0, 'close' = 1)
def Courant(action=0):
    objName = "hutValveWheel"
    ageName = "Ahnonay"
    so = PtFindSceneobject(objName, ageName)
    responders = so.getResponders()
    RunResp(key = so.getKey(), resp = responders[0], stateidx = action, netForce = 1, netPropagate = 1, fastforward = 0)
    RunResp(key = so.getKey(), resp = responders[1], stateidx = action, netForce = 1, netPropagate = 1, fastforward = 0)

#================================================
#
#================================================
"""
        if newSphere == 1:
            PtPageInNode("Sphere01BuildingInterior")
            PtPageInNode("MaintRoom01")
            PtPageInNode("ahnySphere01")
        elif newSphere == 2:
            PtPageInNode("MaintRoom02")
            PtPageInNode("ahnySphere02")
        elif newSphere == 3:
            PtPageInNode("MaintRoom03")
            PtPageInNode("ahnySphere03")
        elif newSphere == 4:
            PtPageInNode("Vortex")
            PtPageInNode("Hub")
            PtPageInNode("MaintRoom04")
            PtPageInNode("EngineerHut")
            PtPageInNode("ahnySphere04")
"""
# pour savoir dans quelle sphere on se trouve
def QSphere():
    ageName = PtGetAgeName ()
    if ageName != 'Ahnonay' :
        print "Vous n'etes pas a Ahnonay"
        return 0
    else:
        ageSDL = PtGetAgeSDL ()
        sphere = ageSDL ["ahnyCurrentSphere"] [0]
        print "Vous etes dans la sphere {}".format(sphere)
        return sphere

# faire tourner a la sphere suivante
def RSphere():
    # sphere = 1 a 4
    sphere = QSphere()
    #val = (((sphere - 1) + 1) % 4) + 1
    val = (sphere % 4) + 1
    ageSDL = PtGetAgeSDL()
    ageSDL ["ahnyCurrentSphere"] = (val,)

#
def LinkPlayerTo(age, playerID=None, spawnPointNumber=None):
    if not playerID or playerID == "":
        playerID = PtGetLocalPlayer().getPlayerID()
    else:
        try:
            playerID = long(playerID)
        except:
            return "incorrect playerID"
            #pass
    if len(age) < 3:
        #pass
        return "incorrect age"
    ageInstanceName = age[0]
    ageFileName = age[1]
    ageGuid = age[2]
    ageUserDefinedName = ""
    if len(age) > 3:
        ageUserDefinedName = age[3]
    
    ageLink = ptAgeLinkStruct()
    ageInfo = ptAgeInfoStruct()
    ageInfo.setAgeFilename(ageFileName)
    ageInfo.setAgeInstanceGuid(ageGuid)
    ageInfo.setAgeInstanceName(ageInstanceName)
    
    ageLink.setAgeInfo(ageInfo)
    """
    spawnPt = "LinkInPointDefault"
    if spawnPointNumber:
        spawnPt = GetSpawnPoint(spawnPointNumber)
    else:
        ageSpawPoint = ""
        if len(age) > 4:
            ageSpawPoint = age[4]
        if ageSpawPoint != "":
            spawnPt = ageSpawPoint
    #self.chatMgr.AddChatLine(None, "sp=\""+spawnPt+"\"", 3)
    spawnPoint = ptSpawnPointInfo()
    spawnPoint.setName(spawnPt)
    ageLink.setSpawnPoint(spawnPoint)
    """
    ptNetLinkingMgr().linkPlayerToAge(ageLink, playerID)
    return ageUserDefinedName + " " + ageInstanceName

#
def LinkAll(ageName="ahnonay"):
    #age = ["Ahnonay", "Ahnonay", "55ce4207-aba9-4f2e-80de-7980a75ac3f2", "Mir-o-Bot", ""]
    ages = {
        "ahnonay":["Ahnonay", "Ahnonay", "55ce4207-aba9-4f2e-80de-7980a75ac3f2", "Mir-o-Bot's", ""],
        "cathedral":["Ahnonay Cathedral", "AhnonayCathedral", "bf4528a7-cb82-46ea-964d-1615a6babb0e", "Mir-o-Bot's", ""], 
        #"hi":["Hood", "Neighborhood", "3cc44d4b-31e1-4dec-b6e6-4b63c72becc3", "The Hood of Illusions", ""],
        "hi":["Hood of Illusions", "Neighborhood", "3cc44d4b-31e1-4dec-b6e6-4b63c72becc3", "The", ""],
        "aegura":["city", "city", "9511bed4-d2cb-40a6-9983-6025cdb68d8b", "Mir-o-Bot's", "LinkInPointFerry"],
        "hood":["Hood", "Neighborhood", "e6958ab2-f925-4e36-a884-ee65e5c73896", "Mir-o-Bot's", ""], 
        "silo":["ErcanaCitySilo", "ErcanaCitySilo", "88177069-fd83-4a07-ba87-5800016e2f28", "Mir-o-Bot's", ""],
    }
    
    ageName = ageName.lower()
    if (ageName in ages.keys()):
        age = ages[ageName]
    else:
        return
    
    #les autre joueurs dans mon age
    for player in PtGetPlayerList():
        LinkPlayerTo(age, playerID = player.getPlayerID(), spawnPointNumber = None)
    # link myself
    LinkPlayerTo(age, playerID = None, spawnPointNumber = None)

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
    sol = FindSOLike("Panic")
    sol = sol.append(FindSOLike("panic"))
    for so in sol:
        so.netForce(1)
        so.physics.disable()

#
def panic():
    PtConsoleNet("Avatar.Spawn.DontPanic" , 1)

# toggles guild bool sdl
def togglesdl(name):
    dicNames = {
        "wings":"ercaHrvstrWingsOk", 
        "wd":"ercaHrvstrWingLeverDown", 
    }
    if (name in dicNames.keys()):
        sdl.ToggleBoolSDL(dicNames[name])
    else:
        print("wrong sdl name")

# platform(name="spy")
def platform(where=None):
    matPos = None
    if where is None or where not in range(1, 5):
        matPos = PtGetLocalAvatar().getLocalToWorld()
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
        matPos = ptMatrix44()
        matPos.setData(tupPos)
        
    Platform.CreatePlatform2(bShow=False, matAv=matPos)

#========================================================
# Ercana City Silo : Pellets
#========================================================
# RunResp(key, resp, stateidx=None, netForce=1, netPropagate=1, fastforward=0)

# entree en haut avec un pellet
liwp={"LinkInWithPellet":["cRespFadeInPellet", "cRespDropPellet"]}

#ageName = "PelletBahroCave"
ageName = "ErcanaCitySilo"
#def RunResponder(key, resp, stateidx = None, netForce = 1, netPropagate = 1, fastforward = 0):
def pellet(respnum=0):
    so = PtFindSceneobject("LinkInWithPellet", ageName)
    sok = so.getKey()
    rn = liwp["LinkInWithPellet"][respnum]
    for resp in so.getResponders():
        if resp.getName() == rn:
            RunResponder(sok, resp)
            break

#
def testresp():
    print "testresp - Ercana City Silo : Pellets - (MachineCamRespDummy)"
    soName = "MachineCamRespDummy"
    so = PtFindSceneobject(soName, ageName)
    print "so {} found".format(soName)
    sok = so.getKey()
    for resp in so.getResponders():
        print "testresp => resp name = '{}'".format(resp.getName())

#
liwp = {"MachineCamRespDummy":[
        "cRespExplosion", 
        "cRespBubbles", 
        "cRespSteam", 
        "cRespGlowOrange", 
        "cRespDud", 
        "cRespDropPellet", 
        "cRespGlowWhite", 
        "cRespFadeInPellet", 
        "cRespMachineCamExit", 
        "cRespMachineCamEnter"
    ]
}

#
def machine(n=0):
    if n not in range(0, 10):
        n = 0
    soName = "MachineCamRespDummy"
    so = PtFindSceneobject(soName, ageName)
    print "so {} found".format(soName)
    sok = so.getKey()
    RunResp(sok, so.getResponders()[n])

#
def launch(n=0):
    if n not in range(0, 10):
        n = 0
    soName = "MachineCamRespDummy"
    so = PtFindSceneobject(soName, ageName)
    print "so {} found".format(soName)
    sok = so.getKey()
    # ajouter des tempos entre les animations...
    RunResp(sok, so.getResponders()[9])
    RunResp(sok, so.getResponders()[5])
    RunResp(sok, so.getResponders()[4])
    RunResp(sok, so.getResponders()[7])
    RunResp(sok, so.getResponders()[n])
    RunResp(sok, so.getResponders()[8])


#