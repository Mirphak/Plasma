# -*- coding: utf-8 -*-
from Plasma import *

def listsp():
    vault = ptVault()
    myAges = vault.getAgesIOwnFolder()
    myAges = myAges.getChildNodeRefList()
    print("AgeFilename;SP Num;Name;Title")
    for ageInfo in myAges:
        link = ageInfo.getChild()
        link = link.upcastToAgeLinkNode()
        info = link.getAgeInfo()
        if not info:
            continue
        ageName = info.getAgeFilename()
        spawnPoints = link.getSpawnPoints()
        i = 0
        for spawnPoint in spawnPoints:
            name = spawnPoint.getName()
            title = spawnPoint.getTitle()
            print(f"{ageName};{i};{name};{title}")
            i += 1
