# -*- coding: utf-8 -*-

from Plasma import *



#**********************************************************************
# Other backend functions. Undocumented.
def RunResponder(key, resp, stateidx = None, netForce = 1, netPropagate = 1, fastforward = 0):
    nt = ptNotify(key)
    nt.addReceiver(resp)
    nt.netPropagate(netPropagate)
    nt.netForce(netForce)
    if stateidx != None:
        nt.addResponderState(stateidx)
    if fastforward:
        nt.setType(PlasmaConstants.PtNotificationType.kResponderFF)
        nt.netPropagate(0)
        nt.netForce(0)
    nt.setActivate(1.0)
    nt.send()
    
def Responder(soName, respName, pfm = None, ageName = None, state = None, ff = False):
    if ageName == None:
        ageName = PtGetAgeName()
    
    so = PtFindSceneobject(soName, ageName)
    respKey = None
    for i in so.getResponders():
        if i.getName() == respName:
            respKey = i
            break
    
    if respKey == None:
        print "Responder():\tResponder not found..."
        return
    
    if pfm == None:
        pms = so.getPythonMods()
        if len(pms) == 0:
            key = respKey
        else:
            key = pms[0]
    else:
        key = PtFindSceneobject(pfm, ageName).getPythonMods()[0]
    
    RunResponder(PtGetLocalAvatar().getKey(), key, stateidx = state, fastforward = ff)

#=========================
"""
* "Sandscrit_Mover", "Payiferen"
cRespUrwin-SFX
cRespUrwin-WalkSniff_2Walk
cRespUrwin-WalkSniff_2Eat
cRespUrwin-WalkSniff
cRespUrwin-Walk_2WalkSniff
cRespUrwin-Walk_2Idle
cRespUrwin-Walk_02
cRespUrwin-Walk_01
cRespUrwin-Idle_Vocalize
cRespUrwin-Idle_2Walk
cRespUrwin-Idle_2Eat
cRespUrwin-Idle_02
cRespUrwin-Idle_01
cRespUrwin-Eat_Swallow
cRespUrwin-Eat_ShakeSwallow
cRespUrwin-Eat_Scoop
cRespUrwin-Eat_2WalkSniff
cRespUrwin-Eat_2Idle

'cPyUrwin'
"""

# Activates and deactivates KI light for a player.
def KiLight(self, cFlags, args = []):
    if len(args) < 2:
        return 0
    player = args[0]
    myself = PtGetLocalPlayer()
    if not isPlayerInAge(player):
        PtSendRTChat(myself, [player], "You must be in my age, use link to join me." , cFlags.flags)
        return 1
    soAvatar = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()

    if args[1] == "on":
        en = 1
    elif args[1] == "off":
        en = 0
    else:
        return 0
    for resp in soAvatar.getResponders():
        if (en == 1 and resp.getName() == 'respKILightOn') or (en == 0 and resp.getName() == 'respKILightOff'):
            RunResponder(soAvatar.getKey(), resp)
            break
    return 1

#def RunResponder(key, resp, stateidx = None, netForce = 1, netPropagate = 1, fastforward = 0):
def test(rn = "cRespUrwin-Walk_01"):
    so = PtFindSceneobject("Sandscrit_Mover", "Payiferen")
    sok = so.getKey()
    for resp in so.getResponders():
        if resp.getName() == rn:
            RunResponder(sok, resp)
            break

#
def test2(rn = "cRespUrwin-Walk_01"):
    so = PtFindSceneobject("Sandscrit_Mover", "Payiferen")
    sok = so.getKey()
    cklst = PtFindClones(sok)
    if len(cklst) > 0:
        sok = cklst[0]
        so = sok.getSceneObject()
        print "clone[0] selected"
    else:
        print "no clone found, original selected"
    rf = False
    for resp in so.getResponders():
        if resp.getName() == rn:
            rf = True
            RunResponder(sok, resp)
            break
    if rf:
        print "responder found"
    else:
        print "responder not found"

#
def clone(bOn=True):
    import CloneObject
    myself = PtGetLocalPlayer()
    # mettre le sandscrit dans le Pod:
    print "==> Sandscrit"
    tupMat = ((-0.275523930788,-0.961294174194,0.0,15.0463008881),(0.961294174194,-0.275523930788,0.0,3.88983178139),(0.0,0.0,1.0,2.06506371498),(0.0,0.0,0.0,1.0))
    mat = ptMatrix44()
    mat.setData(tupMat)
    #SandscritRoot
    #SandscritFlipper
    CloneObject.co3("SandscritFlipper", "Payiferen", bShow=bOn, bLoad=bOn, scale=1) #, matPos=mat)
    CloneObject.co3("Sandscrit_Mover", "Payiferen", bShow=bOn, bLoad=bOn, scale=1) #, matPos=mat)
    CloneObject.co3("SandscritRoot", "Payiferen", bShow=bOn, bLoad=bOn, scale=1) #, matPos=mat)
