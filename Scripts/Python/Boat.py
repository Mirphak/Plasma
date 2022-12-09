from Plasma import *

from Basic import *

def Boat():
    NetPageIn("Boat")
    obj=PtFindSceneobject("Schiff","cityofdimensions")
    obj.netForce(True)
    obj.draw.disable()
    obj=PtFindSceneobject("SchiffSteg","cityofdimensions")
    obj.netForce(True)
    obj.draw.disable()
    obj=PtFindSceneobject("Bild","cityofdimensions")
    obj.netForce(True)
    obj.draw.disable()
    obj=PtFindSceneobject("BildRand","cityofdimensions")
    obj.netForce(True)
    obj.draw.disable()
    obj=PtFindSceneobject("KaminPlane","cityofdimensions")
    obj.netForce(True)
    obj.draw.disable()