# Fait varier la couleur du fog.

from Plasma import *
import math

# Adapted from Hoikas Disco code.
class ChangeFog:
    running = False
    start   = 1000
    end     = 10000
    density = 1.0
    delay   = 1.0
    step    = 0
    stepR   = 0
    stepG   = 0
    stepB   = 90
    ageGuid = None

    def __init__(self):
        pass

    def onAlarm(self, context=1):
        if self.ageGuid != PtGetAgeInfo().getAgeInstanceGuid():
            self.running = False
        if not self.running:
            return
        # un peu de math pour faire varier la couleur :)
        vr = (math.sin(self.stepR * math.pi / 180.) * .15) + .15
        if vr < 0:
            vr = 0
        self.stepR = (self.stepR + 3) % 360
        
        #vg = (math.sin(self.stepG * math.pi / 180.) * .15) - .125
        #if vg < 0:
        #    vg = 0
        #self.stepG = (self.stepG + 4) % 360
        vg = 0
        
        vb = (math.sin(self.stepB * math.pi / 180.) * .15) + .05
        if vb < 0:
            vb = 0
        self.stepB = (self.stepB + 3) % 360

        if self.step == 0:
            # pas la peine de changer le reste a chaque fois
            fy = "Graphics.Renderer.Setyon 100000"
            fd = "Graphics.Renderer.Fog.SetDefLinear {} {} {}".format(self.start, self.end, self.density)
            #cc = "Graphics.Renderer.SetClearColor {} {} {}".format(.6, .6, .6)
            cc = "Graphics.Renderer.SetClearColor {} {} {}".format(.5, .45, .4)
            PtConsoleNet(fy, True)
            PtConsoleNet(fd, True)
            PtConsoleNet(cc, True)
        self.step = (self.step + 3) % 180
        # et la couleur fut!
        #fc = "Graphics.Renderer.Fog.SetDefColor {} {} {}".format(vr, vg, vb)
        fc = "Graphics.Renderer.Fog.SetDefColor {} {} {}".format(vr * 0.4, vg, vb * 0.4)
        #print "[{}, {}, {}]".format(vr * 0.1, vg, vb * 0.1)
        PtConsoleNet(fc, True)
        
        # on rappelle set alarm
        PtSetAlarm(self.delay, self, 1)

# init class
fog = ChangeFog()

# Start ChangeFog.
def Start(delay=None, start=None, end=None, density=None):
    if isinstance(start, int):
        fog.start = start
    if isinstance(end, int):
        fog.end = end
    if isinstance(density, float):
        fog.density = density
    if isinstance(delay, float):
        fog.delay = delay
    fog.ageGuid = PtGetAgeInfo().getAgeInstanceGuid()
    if not fog.running:
        fog.running = True
        fog.onAlarm()

# Stop ChangeFog.
def Stop():
    fog.running = False
