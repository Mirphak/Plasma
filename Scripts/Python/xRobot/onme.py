# -*- coding: cp1252 -*-

from Plasma import *

def onme():
    surmoi = PtGetLocalAvatar().getLocalToWorld()
    obj = PtFindSceneobject('FogRegion - Caves','Minkata')
    obj.physics.warp(surmoi)            
    obj.physics.netForce(1)
    obj = PtFindSceneobject('FogRegion - Exterior','Minkata')
    obj.physics.warp(surmoi)            
    obj.physics.netForce(1)
