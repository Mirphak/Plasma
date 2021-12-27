# -*- coding: utf-8 -*-
from Plasma import *
from PlasmaVaultConstants import *

#
def GetMyAges():
    ageDict = dict()
    ageInfoList = list()
    ages = ptVault().getAgesIOwnFolder().getChildNodeRefList()
    for age in ages:
        ageInfo = age.getChild().upcastToAgeLinkNode().getAgeInfo()
        ageInfoList = (ageInfo.getAgeInstanceName(), ageInfo.getAgeFilename(), ageInfo.getAgeInstanceGuid(), ageInfo.getAgeUserDefinedName(), "")
        #print ageInfoList
        #ageDict.update({ageInfo.getAgeInstanceName():ageInfoList})
        myKey = ageInfo.getAgeInstanceName()
        myKey = myKey.lower()
        myKey = myKey.replace(" ", "")
        myKey = myKey.replace("'", "")
        myKey = myKey.replace("eder", "")
        ageDict.update({myKey:ageInfoList})
        """
        tmp.update({k.lower().replace(" ", "").replace("'", "").replace("eder", ""): v})
        if myKey == "city":
            myKey = "mycity"
            myKey = "mydakotah"
            myKey = "myferry"
            myKey = "myconcert"
            myKey = "mylibrary"
            myKey = "mypalace"
            myKey = "mygallery"
            
            sp = "LinkInPointDakotahAlley"
            sp = "DakotahRoofPlayerStart"
            sp = "LinkInPointFerry"
            sp = "LinkInPointConcertHallFoyer"
            sp = "LinkInPointLibrary"
            sp = "LinkInPointPalace"
            sp = "LinkInPointKadishGallery"
        """
        #elif myKey == "":
            #myKey = "My" + ""
        #ageDict.update({myKey:ageInfoList})
    return ageDict

#

def ListMyAges():
    ages = ptVault().getAgesIOwnFolder().getChildNodeRefList()
    i = 0
    for age in ages:
        ageInfo = age.getChild().upcastToAgeLinkNode().getAgeInfo()
        i += 1
        print "{0}\t: {1}".format(i, ageInfo.getAgeFilename())

"""
===========================================
Trouve dans nxusBookMachine.py : Pour le GZ
===========================================
"""
#
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

#
def IGetHoodInfoNode():
    vault = ptVault()
    folder = vault.getAgesIOwnFolder()
    return IFindAgeInfoInFolder(folder, 'Neighborhood')

#
def IGetGZLinkNode():
    childAgeFolder = IGetHoodInfoNode().getChildAgesFolder()
    contents = childAgeFolder.getChildNodeRefList()
    for content in contents:
        link = content.getChild()
        link = link.upcastToAgeLinkNode()
        name = link.getAgeInfo().getAgeFilename()
        if name.lower() == "greatzero":
            return link
    return None # not found

"""==========================================================="""

# Ne permet de trouver que les sous ages du quartier
def GetChildAges():
    vault = ptVault()
    folder = vault.getAgesIOwnFolder()
    contentsA = folder.getChildNodeRefList()
    for contentA in contentsA:
        link = contentA.getChild()
        link = link.upcastToAgeLinkNode()
        if link is not None:
            info = link.getAgeInfo()
        else:
            link = contentA.getChild()
            info = link.upcastToAgeInfoNode()
        
        print "Age : {0}".format(info.getAgeFilename())
        
        childAgeFolder = info.getChildAgesFolder()
        contentsC = childAgeFolder.getChildNodeRefList()
        for contentC in contentsC:
            link = contentC.getChild()
            link = link.upcastToAgeLinkNode()
            name = link.getAgeInfo().getAgeFilename()
            print ">> Child : {0}".format(name)

# Pour Ahnonay (voir xLinkingBookGUIPopup.py) ==> RIEN !!
def GetAhnonaySP():
    ageVault = ptAgeVault()
    ageInfoNode = ageVault.getAgeInfo()
    ageInfoChildren = ageInfoNode.getChildNodeRefList()
    for ageInfoChildRef in ageInfoChildren:
        ageInfoChild = ageInfoChildRef.getChild()
        folder = ageInfoChild.upcastToFolderNode()
        if folder and folder.folderGetName() == "AgeData":
            ageDataChildren = folder.getChildNodeRefList()
            for ageDataChildRef in ageDataChildren:
                ageDataChild = ageDataChildRef.getChild()
                chron = ageDataChild.upcastToChronicleNode()
                if chron and chron.getName() == "AhnonaySpawnPoints":
                    spawns = chron.getValue().split(";")
                    spawnPoints = []
                    for spawn in spawns:
                        #spawnInfo = spawn.split(",")
                        #spawnPointInfo = ptSpawnPointInfo(spawnInfo[0], spawnInfo[1])
                        #spawnPoints.append(spawnPointInfo)
                        print spawn
                    break

# Et ca? ==> Pas mieux!!
def PelletCaveFromAhnonay():
    ageStruct = ptAgeInfoStruct()
    ageStruct.setAgeFilename("AhnonayCathedral")
    vault = ptAgeVault()
    ageLinkNode = vault.getSubAgeLink(ageStruct)
    if ageLinkNode:
        ageInfoNode = ageLinkNode.getAgeInfo()
        ageInfoChildren = ageInfoNode.getChildNodeRefList()
        for ageInfoChildRef in ageInfoChildren:
            ageInfoChild = ageInfoChildRef.getChild()
            folder = ageInfoChild.upcastToFolderNode()
            if folder and folder.folderGetName() == "AgeData":
                ageDataChildren = folder.getChildNodeRefList()
                for ageDataChildRef in ageDataChildren:
                    ageDataChild = ageDataChildRef.getChild()
                    chron = ageDataChild.upcastToChronicleNode()
                    if chron and chron.getName() == "PelletCaveGUID":
                        print "Found pellet cave guid - ", chron.getValue()
                        return chron.getValue()
                return ""


#