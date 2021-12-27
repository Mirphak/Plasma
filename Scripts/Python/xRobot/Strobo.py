# -*- coding: utf-8 -*-
# Fait varier la couleur du fog.

from Plasma import *
import math
from . import CloneObject
from . import Light

# Adapted from Hoikas Disco code.
class ChangeFog:
    running = False
    ageGuid = None
    delay = 0.5
    objName = "RTProjDirLight03"
    age = "Payiferen"
    bOn = True

    def __init__(self):
        pass

    #
    def Light1(self,objectName="RTGlowLight", ageName="CustomAvatars", av=None, bLoadShowOn=True, bAttachOn=False, dx=0, dy=0, dz=4, rx=0, ry=0, rz=0):
        bOn = bLoadShowOn
        if av is None:
            av = PtGetLocalAvatar()
        pos = av.getLocalToWorld()
        pos1 = pos
        pos1.translate(ptVector3(dx, dy, dz))
        mRotX = ptMatrix44()
        mRotY = ptMatrix44()
        mRotZ = ptMatrix44()
        mRotX.rotate(0, (math.pi * rx) / 180)
        mRotY.rotate(1, (math.pi * ry) / 180)
        mRotZ.rotate(2, (math.pi * rz) / 180)
        pos1 = pos1 * mRotZ * mRotY * mRotX
        CloneObject.Clone2(objName=objectName, age=ageName, bShow=bOn, bLoad=bOn, matPos=pos1, bAttach=bAttachOn, soAvatar=av)
        return PtFindSceneobject(objectName, ageName)

    def onAlarm(self, context=1):
        if self.ageGuid != PtGetAgeInfo().getAgeInstanceGuid():
            self.running = False
        if not self.running:
            return
        
        #fogStart = (math.sin(self.stepStart * math.pi / 180.) * self.start * 1.2) + self.start
        
        #self.stepStart = (self.stepStart + 5) % 360
        #self.stepEnd   = (self.stepEnd + 10) % 360
        #self.stepDensity = (self.stepDensity + 30) % 360
        
        #if self.step == 0:
            # pas la peine de changer le reste a chaque fois
            #fy = "Graphics.Renderer.Setyon 100000"
            #fy = "Graphics.Renderer.Setyon 10000"
            #PtConsoleNet(fy, True)
        #fd = "Graphics.Renderer.Fog.SetDefLinear {} {} {}".format(fogStart, fogEnd, fogDensity)
        #cc = "Graphics.Renderer.SetClearColor {} {} {}".format(vb * 3., vg * 9., vr * 3.)
        #PtConsoleNet(fd, True)
        #PtConsoleNet(cc, True)
        #self.step = (self.step + 3) % 180
        # et la couleur fut!
        #fc = "Graphics.Renderer.Fog.SetDefColor {} {} {}".format(vr * 0.4, vg, vb * 0.4)
        #fc = "Graphics.Renderer.Fog.SetDefColor {} {} {}".format(vr, vg, vb)
        #PtConsoleNet(fc, True)
        #self.Light1(objectName="RTProjDirLight03", ageName="Payiferen", av=None, bLoadShowOn=self.bOn, bAttachOn=False, dx=0, dy=-10, dz=50, rx=60, ry=0, rz=0)
        Light.PayLight3b(av=None, bLoadShowOn=self.bOn, bAttachOn=False, dx=0, dy=0, dz=50, rx=60, ry=0, rz=0)
        self.bOn = not self.bOn

        # on rappelle set alarm
        PtSetAlarm(self.delay, self, 1)

# init class
fog = ChangeFog()

# Start ChangeFog.
def Start(delay=None):
    if isinstance(delay, float):
        fog.delay = delay
    fog.ageGuid = PtGetAgeInfo().getAgeInstanceGuid()
    if not fog.running:
        fog.running = True
        fog.onAlarm()

# Stop ChangeFog.
def Stop():
    fog.running = False
    #fog.Light1(bLoadShowOn=False, bAttachOn=False)
    Light.PayLight3b(av=None, bLoadShowOn=False, bAttachOn=False, dx=0, dy=0, dz=10, rx=0, ry=0, rz=0)