# -*- coding: utf-8 -*-

from Plasma import *
from . import Light

# Larry LeDeay [KI: 11308]
plSpeakerID = 11308

def light(bOn=True):
    soPlayer = PtGetAvatarKeyFromClientID(plSpeakerID).getSceneObject()
    Light.PayLight3b(soPlayer, bOn, bOn, 0, 0, 100, 30, 0, 0)
