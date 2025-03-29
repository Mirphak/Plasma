from Plasma import *

def AhnNoBook(bVis=False) :
    objs = PtFindSceneobjects("DniLinkingBook")
    objs += PtFindSceneobjects("YeeshaDecalAhny")
    for obj in objs :
        obj.netForce(bVis)
        obj.draw.enable(bVis)

def AhnBook(bVis=True) :
    objs = PtFindSceneobjects("DniLinkingBook")
    for obj in objs :
        obj.netForce(bVis)
        obj.draw.enable(bVis)

