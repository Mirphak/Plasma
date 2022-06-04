# -*- coding: utf-8 -*-

from Plasma import *
from PlasmaKITypes import *

#
class AlarmAddPrp:
    _nbTimes = 0
    _bPrpLoaded = False
    
    def __init__(self, objectName="SchiffSteg", ageFileName="cityofdimensions"):
        print("AlarmAddPrp: init")
        self._objectName = objectName
        self._ageFileName = ageFileName
        self._bPrpLoaded = False
        self._so = PtFindSceneobject(self._objectName, self._ageFileName)
    def onAlarm(self, context):
        if context == 0:
            print("AlarmAddPrp: 0 - AddPrp")
            PtConsoleNet("Nav.PageInNode cityofdimensions_Boat", True)
            PtSetAlarm(.25, self, 1)
        elif context == 1:
            print("AlarmAddPrp: 1 - Waitting loop")
            try:
                pos = self._so.position()
            except:
                print("err so pos")
                return
            print("pos: {}, {}, {}".format(pos.getX(), pos.getY(), pos.getZ()))
            if (pos.getX() == 0 and pos.getY() == 0 and pos.getZ() == 0 and self._nbTimes < 20):
                self._nbTimes += 1
                print(">>> Attente nb: {}".format(self._nbTimes))
                PtSetAlarm(.25, self, 1)
            else:
                if (self._nbTimes < 20):
                    self._bPrpLoaded = True
                    PtSetAlarm(0, self, 2)
                else:
                    print("loading prp was too long...")
                self._nbTimes = 0
        elif context == 2:
            print("AlarmAddPrp: 2 - The prp is ready")
            # Hide some objects
            objNames = ["Schiff", "SchiffSteg", "Bild", "BildRand", "KaminPlane"]
            for objName in objNames:
                obj = PtFindSceneobject(objName, self._ageFileName)
                if isinstance(obj, ptSceneobject):
                    obj.draw.netForce(True)
                    obj.draw.enable(False)
                else:
                    print(f"Error : object {objName} not found in {self._ageFileName}!")

#
def AddCoDBoat():
    print("Adding CoD Boat...")
    try:
        PtSetAlarm (0, AlarmAddPrp(), 0)
        print("CoD Boat added!")
        return 1
    except:
        PtSendKIMessage(kKILocalChatErrorMsg, "Error while adding CoD Boat.")
        return 0

#
