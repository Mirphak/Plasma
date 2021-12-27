# Fait varier la couleur du fond de ciel.
# (1 + math.sin(radAngle) + math.sin(3*radAngle)/3 + math.sin(5*radAngle)/5)/2
# (1 + math.sin(radAngle + (2*math.pi/3)) + math.sin(3*(radAngle + (2*math.pi/3)))/3 + math.sin(5*(radAngle + (2*math.pi/3)))/5)/2
# (1 + math.sin(radAngle + (4*math.pi/3)) + math.sin(3*(radAngle + (4*math.pi/3)))/3 + math.sin(5*(radAngle + (4*math.pi/3)))/5)/2
from Plasma import *
import math

# 
class ChangeSky:
    running = False
    start   = 1000
    end     = 10000
    density = 0.0
    delay   = 1.0
    step    = 0
    stepR   = 0
    stepG   = 10
    stepB   = 20
    ageGuid = None

    def __init__(self):
        pass

    def onAlarm(self, context=1):
        if self.ageGuid != PtGetAgeInfo().getAgeInstanceGuid():
            self.running = False
        if not self.running:
            return
        # un peu de math pour faire varier la couleur :)
        radAngle = self.stepR * math.pi / 180.
        #vr = (1 + math.sin(radAngle) + math.sin(3*radAngle)/3 + math.sin(5*radAngle)/5)*(math.sin(radAngle))**2/2
        #vr = 0.25 + (1 + math.sin(radAngle) + math.sin(3*radAngle)/3 + math.sin(5*radAngle)/5)/4
        #vr = 0.5 + ((0 + math.sin(radAngle) + math.sin(3*radAngle)/3 + math.sin(5*radAngle)/5)/4)
        vr = 0.5 + ((0 + math.sin(radAngle) + math.sin(3*radAngle)/3 + math.sin(5*radAngle)/5)/2.5)
        if vr < 0:
            vr = 0
        self.stepR = (self.stepR + 3) % 360
        
        radAngle = self.stepG * math.pi / 180.
        #vg = (1 + math.sin(radAngle + (2*math.pi/3)) + math.sin(3*(radAngle + (2*math.pi/3)))/3 + math.sin(5*(radAngle + (2*math.pi/3)))/5)*(math.sin(radAngle + (2*math.pi/3)))**2/2
        #vg = 0.25 + (1 + math.sin(radAngle + (2*math.pi/3)) + math.sin(3*(radAngle + (2*math.pi/3)))/3 + math.sin(5*(radAngle + (2*math.pi/3)))/5)/4
        #vg = 0.45 + ((0 + math.sin(radAngle + (1*math.pi/36)) + math.sin(3*(radAngle + (1*math.pi/36)))/3 + math.sin(5*(radAngle + (1*math.pi/36)))/5)/4)
        vg = 0.45 + ((0 + math.sin(radAngle) + math.sin(3*radAngle)/3 + math.sin(5*radAngle)/5)/2.6)
        if vg < 0:
            vg = 0
        self.stepG = (self.stepG + 3) % 360
        #vg = 0
        
        radAngle = self.stepB * math.pi / 180.
        #vb = (1 + math.sin(radAngle + (4*math.pi/3)) + math.sin(3*(radAngle + (4*math.pi/3)))/3 + math.sin(5*(radAngle + (4*math.pi/3)))/5)*(math.sin(radAngle + (4*math.pi/3)))**2/2
        #vb = 0.25 + (1 + math.sin(radAngle + (4*math.pi/3)) + math.sin(3*(radAngle + (4*math.pi/3)))/3 + math.sin(5*(radAngle + (4*math.pi/3)))/5)/4
        #vb = 0.4 + ((0 + math.sin(radAngle + (2*math.pi/36)) + math.sin(3*(radAngle + (2*math.pi/36)))/3 + math.sin(5*(radAngle + (2*math.pi/36)))/5)/4)
        vb = 0.4 + ((0 + math.sin(radAngle) + math.sin(3*radAngle)/3 + math.sin(5*radAngle)/5)/2.7)
        if vb < 0:
            vb = 0
        self.stepB = (self.stepB + 3) % 360

        if self.step == 0:
            # pas la peine de changer le reste a chaque fois
            fy = "Graphics.Renderer.Setyon 100000"
            fd = "Graphics.Renderer.Fog.SetDefLinear {} {} {}".format(self.start, self.end, self.density)
            #cc = "Graphics.Renderer.SetClearColor {} {} {}".format(.5, .45, .4)
            fc = "Graphics.Renderer.Fog.SetDefColor {} {} {}".format(0.0, 0.0, 0.0)
            PtConsoleNet(fy, True)
            PtConsoleNet(fd, True)
            #PtConsoleNet(cc, True)
            PtConsoleNet(fc, True)
        self.step = (self.step + 3) % 180
        # et la couleur fut!
        #fc = "Graphics.Renderer.Fog.SetDefColor {} {} {}".format(vr, vg, vb)
        #fc = "Graphics.Renderer.Fog.SetDefColor {} {} {}".format(vr * 0.4, vg, vb * 0.4)
        #print "[{}, {}, {}]".format(vr * 0.1, vg, vb * 0.1)
        #PtConsoleNet(fc, True)
        cc = "Graphics.Renderer.SetClearColor {} {} {}".format(vr, vg, vb)
        #print "[{}, {}, {}]".format(vr, vg, vb)
        PtConsoleNet(cc, True)
        
        # on rappelle set alarm
        PtSetAlarm(self.delay, self, 1)

# init class
sky = ChangeSky()

# Start ChangeSky.
def Start(delay=None, start=None, end=None, density=None):
    if isinstance(start, int):
        sky.start = start
    if isinstance(end, int):
        sky.end = end
    if isinstance(density, float):
        sky.density = density
    if isinstance(delay, float):
        sky.delay = delay
    sky.ageGuid = PtGetAgeInfo().getAgeInstanceGuid()
    if not sky.running:
        sky.running = True
        sky.onAlarm()

# Stop ChangeSky.
def Stop():
    sky.running = False
