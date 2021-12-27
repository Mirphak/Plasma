# Colors
# Functions to change colors.

from Plasma import *
#import random
import math
import xBotAge

## Set fog color.
#def SetFog(r,g,b):
#	PtConsoleNet("Graphics.Renderer.Fog.SetDefColor " + str(r) + " " + str(g) + " " + str(b),1)

# Adapted from (Hoikas) Disco code.
class DiscoFog:
    running = False
    start   = 1000
    end     = 10000
    density = 1.0
    delay   = 1.0
    step    = 0
    #stepR   = 30
    #stepG   = 90
    #stepB   = 150
    stepR   = 0
    stepG   = 0
    stepB   = 90

    def __init__(self):
        #random.seed()
        pass

    def onAlarm(self, context=1):
        if not self.running:
            return

        #try:
        #    #start = random.randrange(self.start[0], self.start[1])
        #except TypeError:
        #    start = int(self.start)
        #try:
        #    #end = random.randrange(self.end[0], self.end[1])
        #except TypeError:
        #    end = int(self.end)
        #try:
        #    #density = random.randrange(self.density[0], self.density[1])
        #except TypeError:
        #    #density = int(self.density)
        #    density = float(self.density)

        #r = float(random.randint(0, 255)) / 255.0
        #g = float(random.randint(0, 255)) / 255.0
        #b = float(random.randint(0, 255)) / 255.0
        
        #vr = math.sin(self.stepR * math.pi / 180.) * .15
        #self.stepR = (self.stepR + 3) % 180
        #vg = math.sin(self.stepG * math.pi / 180.) * .15
        #self.stepG = (self.stepG + 3) % 180
        #vb = math.sin(self.stepB * math.pi / 180.) * .15
        #self.stepB = (self.stepB + 3) % 180
        
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

        #print "self.step = {}".format(self.step)
        if self.step == 0:
            print ">> update style"
            #xBotAge.SetRendererStyle(vstyle = "100000")
            #xBotAge.SetRendererFogLinear(self.start, self.end, self.density)
            #xBotAge.SetRendererClearColor(.6, .6, .6)
            fy = "Graphics.Renderer.Setyon 100000"
            fd = "Graphics.Renderer.Fog.SetDefLinear {} {} {}".format(self.start, self.end, self.density)
            cc = "Graphics.Renderer.SetClearColor {} {} {}".format(.6, .6, .6)
            PtConsoleNet(fy, True)
            PtConsoleNet(fd, True)
            PtConsoleNet(cc, True)
        self.step = (self.step + 3) % 180

        #fd = "Graphics.Renderer.Fog.SetDefLinear %i %i %f" % (start, end, density)
        #fc = "Graphics.Renderer.Fog.SetDefColor %f %f %f" % (r, g, b)
        #PtConsoleNet(fd, True)
        #PtConsoleNet(fc, True)
        
        #xBotAge.SetRenderer(style = "100000", start = self.start, end = self.end, density = self.density, r = vr, g = vg, b = vb, cr = .8, cg = .8, cb = .8)
        #xBotAge.SetRendererFogColor(vr, vg, vb)
        fc = "Graphics.Renderer.Fog.SetDefColor {} {} {}".format(vr, vg, vb)
        PtConsoleNet(fc, True)

        PtSetAlarm(self.delay, self, 1)

# init class
disco = DiscoFog()
#disco = None

# Start Disco.
def DiscoStart(delay=None, start=None, end=None, density=None):
    if isinstance(start, int):
        disco.start = start
    if isinstance(end, int):
        disco.end = end
    if isinstance(density, float):
        disco.density = density
    if isinstance(delay, float):
        disco.delay = delay
    #if disco is None:
    #    disco = DiscoFog()
    if not disco.running:
        disco.running = True
        disco.onAlarm()

# Stop Disco.
def DiscoStop():
    disco.running = False
    #reload(Colors)
    #SetFog(0, 0, 0)
    # rendu normal de l'age
    #xBotAge.SetRenderer(style = "default")
    #disco = None
