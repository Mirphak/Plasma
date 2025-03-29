# -*- coding: utf-8 -*-
from Plasma import *

# The conference room podium is in GoMePubNew District_Mysterium.prp
def Hide():
    ageName = 'GoMePubNew'
    # Visible parts
    podiumPartsNames = [
        'Cylinder02_001',
        'Mic01',
        'MicBase01',
        'MicBaseHilt01',
        'MicClip01',
        'Podium01',
        'PodiumSign01',
    ]
    for objectName in podiumPartsNames:
        so = PtFindSceneobject(objectName, ageName)
        so.netForce(True)
        so.draw.enable(False)
    # Physical pat
    objectName = 'PodiumCol'
    so = PtFindSceneobject(objectName, ageName)
    so.netForce(True)
    so.physics.enable(False)
