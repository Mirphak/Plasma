# -*- coding: utf-8 -*-

"""
    -- V1 : 24/10/2015 => Door
    -- V2 : Cavern Tour du 16/01/2016
    -- V3 : Cavern Tour du 28/01/2017
       
"""

from Plasma import *

"""
    stringSDLVarClosed = ptAttribString(13,"SDL Bool Closed")
    xrgnDoorBlocker = ptAttribExcludeRegion(14,"Exclude Region")

    actInterior  = ptAttribActivator(15,"Clickable: interior")
    respOpenInt = ptAttribResponder(16,"Rspndr: open from inside",netForce=0)

    actExterior  = ptAttribActivator(17,"Clickable: exterior")
    respOpenExt = ptAttribResponder(18,"Rspndr: open from outside",netForce=0)

    boolCanManualClose = ptAttribBoolean(19,"Player can close me",default=1)
    respCloseInt  = ptAttribResponder(20,"Rspndr: close from inside",netForce=0)
    respCloseExt  = ptAttribResponder(21,"Rspndr: close from outside",netForce=0)

    boolCanAutoClose = ptAttribBoolean(22,"Door can autoclose")
    respAutoClose = ptAttribResponder(23,"Rspndr: Auto Close",netForce=0)

    # doors that auto-close or auto-open can be left in bogus state if players lose connection etc.
    # if I enter an age by myself and a door that should've auto-opened is closed...just open it and correct the state
    boolForceOpen = ptAttribBoolean(24,"Force Open if Age Empty")
    # if I enter an age by myself and a door that should've auto-closed is open...just close it and correct the state
    boolForceClose = ptAttribBoolean(25,"Force Close if Age Empty")

    boolOwnedDoor = ptAttribBoolean(26,"Only Owners Can Use",default=false)

    stringSDLVarEnabled = ptAttribString(27,"SDL Bool Enabled (Optional)") # for lockable or powerable doors etc.
"""

"""
    Kadish spawn points:
            "k0":"LinkInPointDefault",       # = sp 0  
        #- kdshCourtyard : 
            "k1":"kdshJourneyCloth06POS",    # = sp 1
            "k2":"LinkInPointFromGallery",   # = sp 2 
        #- kdshForest :                     
            "k3":"Perf-SpawnPointKdsh03",    # = sp 3
            "k4":"kdshJourneyCloth01POS",    # = sp 4
            "k5":"kdshJourneyCloth02POS",    # = sp 5
            "k6":"LinkInPointDefault",       # = sp 6  
        #- kdshShadowPath :                 
            "k7":"StartPoint",               # = sp 7 
        #- kdshGlowInTheDark :              
            "k8":"LinkInPointDummy",         # = sp 8 
        #- kdshPillars :                    
            "k9":"kdshJourneyCloth04POS",    # = sp 9
            "k10":"kdshJourneyCloth07POS",   # = sp 10
            "k11":"Perf-SpawnPointKdsh04",   # = sp 11
            "k12":"pillarRoomStartingPoint", # = sp 12 
        #- kdshVaultExtr :                  
            "k13":"Perf-SpawnPointKdsh01",   # = sp 13
            "k14":"KadishVaultPST02",        # = sp 14 
        #- kdshVaultIntr :                  
            "k15":"kdshJourneyCloth05POS",   # = sp 15
            "k16":"Perf-SpawnPointKdsh05",   # = sp 16
            "k17":"StartDummy02",            # = sp 17 
        #- kdshVaultIntrYeesha :            
            "k18":"StartDummy02",            # = sp 18
            "k19":"LinkInPointYeeshaVault"   # = sp 19

"""
#Cette fonction ne s'utilise pas seule, elle est appelée par Action()
def RunResp(key, resp, stateidx = None, netForce = 1, netPropagate = 1, fastforward = 0):
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
def Door(action = 0):
    objName = "TreeGateWood"
    ageName = "Kadish"
    so = PtFindSceneobject(objName, ageName)
    responders = so.getResponders()
    if action == 0:
        #Open the tree door
        RunResp(key = so.getKey(), resp = responders[1], stateidx = None, netForce = 1, netPropagate = 1, fastforward = 0)
    else:
        #Close the tree door
        RunResp(key = so.getKey(), resp = responders[0], stateidx = None, netForce = 1, netPropagate = 1, fastforward = 0)

#

# Find scene objects with name like soName in all loaded districts (aka pages or prp files)
# ex.: soName = "Bahro*Stone" will be transformed in regexp "^.*Bahro.*Stone.*$"
# copie de celle de xBotAge
def FindSOName(soName):
    import re
    cond = "^.*" + soName.replace("*", ".*") + ".*$"
    pattern = re.compile(cond, re.IGNORECASE)
    strList = soName.split("*")
    nameList = list()
    for str in strList:
        nameList.extend(map(lambda so: so.getName(), PtFindSceneobjects(str)))
    nameList = list(set(nameList))
    nameList = filter(lambda x: pattern.match(x) != None, nameList)
    return nameList

# Retourne la liste des clones trouve des objets dont le nom ressemble a <name>
def GetCloneList(name):
    nameList = FindSOName(name)
    soCloneDic = {}
    for soName in nameList:
        print "nom: {}".format(soName)
        try:
            sol = PtFindSceneobjects(soName)
            for mso in sol:
                print "mso: {}".format(mso.getName())
                cloneKeys = PtFindClones(mso.getKey())
                print "cloneKeys: {}".format(len(cloneKeys))
                soCloneList = map(lambda ck: ck.getSceneObject(), cloneKeys)
                soCloneDic.update({mso.getName(): soCloneList})
        except:
            continue
    return soCloneDic

# toggle minkata floor
def tmf(bOn=0):
    name = "GroundFloorProxy"
    somfDic = GetCloneList(name)
    if len(somfDic) > 0:
        cloneList = somfDic[name]
        for clone in cloneList:
            clone.netForce(1)
            clone.physics.enable(bOn)
            #clone.physics.netForce(1)
            #clone.physics.disable()
    else:
        print "No clone found"

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

#

# ** FIN **