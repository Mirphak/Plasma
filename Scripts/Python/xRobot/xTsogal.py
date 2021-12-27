# -*- coding: utf-8 -*-
from Plasma import *

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
    objName = "tsglBlueSpiralDoorPOS"
    ageName = "EderTsogal"
    so = PtFindSceneobject(objName, ageName)
    responders = so.getResponders()
    RunResp(key = so.getKey(), resp = responders[8], stateidx = action, netForce = 1, netPropagate = 1, fastforward = 0)

# ** FIN **