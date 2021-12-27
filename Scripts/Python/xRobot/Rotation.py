# Fait varier la couleur du autoRotation.

from Plasma import *
import math

# Classe pour la rotation automatique
class AutoRotation:
    running = False
    delay   = 1.0
    so      = None
    stepZ   = 0.1
    #thetaZ  = 0.0
    ageGuid = None

    def __init__(self, delay=None, so=None, stepZ=None):
        if isinstance(so, ptSceneobject):
            self.so = so
        if isinstance(stepZ, float):
            self.stepZ = stepZ
        elif isinstance(stepZ, int):
            self.stepZ = float(stepZ)
        else:
            self.stepZ = 0.1
        if isinstance(delay, float):
            self.delay = delay
        elif isinstance(delay, int):
            self.delay = float(delay)

    def onAlarm(self, context=1):
        if self.ageGuid != PtGetAgeInfo().getAgeInstanceGuid():
            self.running = False
        if not self.running:
            return
        if not isinstance(self.so, ptSceneobject):
            self.running = False
            print "AutoRotation stoped: self.so is not a ptSceneobject!"
            return

        # tournez manege!
        pos = self.so.getLocalToWorld()
        m = ptMatrix44()
        #self.thetaZ = self.thetaZ + self.stepZ
        #print "--> AutoRotation: self.thetaZ = {}".format(self.thetaZ)
        # rotation automatique en z uniquement
        m.rotate(2, (math.pi * (self.stepZ)) / 180.0)
        self.so.netForce(1)
        self.so.physics.warp(pos * m)
        
        # on rappelle set alarm
        PtSetAlarm(self.delay, self, 1)

    # Start AutoRotation.
    def Start(self):
        self.ageGuid = PtGetAgeInfo().getAgeInstanceGuid()
        if not self.running:
            self.running = True
            self.onAlarm()

    # Stop AutoRotation.
    def Stop(self):
        self.running = False

"""
# init class
autoRotation = AutoRotation()

# Start AutoRotation.
def Start(delay=None, so=None, stepZ=None):
    if isinstance(so, ptSceneobject):
        autoRotation.so = so
    if isinstance(stepZ, float):
        autoRotation.stepZ = stepZ
    elif isinstance(stepZ, int):
        autoRotation.stepZ = float(stepZ)
    if isinstance(delay, float):
        autoRotation.delay = delay
    elif isinstance(delay, int):
        autoRotation.delay = float(delay)
    if not autoRotation.running:
        autoRotation.running = True
        autoRotation.onAlarm()

# Stop AutoRotation.
def Stop():
    autoRotation.running = False
"""
