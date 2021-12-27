# -*- coding: utf-8 -*-
from Plasma import *

def IFindAgeInfoInFolder(folder, ageName):
    ageName = ageName.lower()
    contents = folder.getChildNodeRefList()
    for content in contents:
        link = content.getChild()
        link = link.upcastToAgeLinkNode()
        if link is not None:
            info = link.getAgeInfo()
        else:
            link = content.getChild()
            info = link.upcastToAgeInfoNode()

        if info.getAgeFilename().lower() == ageName:
            return info
    return None

def IGetHoodInfoNode():
    vault = ptVault()
    folder = vault.getAgesIOwnFolder()
    return IFindAgeInfoInFolder(folder, 'Neighborhood')

def IIsMyHoodPublic():
    hoodInfo = IGetHoodInfoNode()
    if hoodInfo is not None:
        return hoodInfo.isPublic()

def IMakeHoodPublic():
    hoodInfo = IGetHoodInfoNode()
    if hoodInfo is not None:
        infoStruct = hoodInfo.asAgeInfoStruct()
        PtCreatePublicAge(infoStruct, None)


def IMakeHoodPrivate():
    hoodInfo = IGetHoodInfoNode()
    if hoodInfo is not None:
        guid = hoodInfo.getAgeInstanceGuid()
        PtRemovePublicAge(guid, None)

def IPublicAgeCreated(ageName):
    PtDebugPrint("IPublicAgeCreated: " + ageName)
    PtGetPublicAgeList(ageName, None)

def IPublicAgeRemoved(ageName):
    PtDebugPrint("IPublicAgeRemoved: " + ageName)
    PtGetPublicAgeList(ageName, None)
