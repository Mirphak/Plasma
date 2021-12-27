# -*- coding: utf-8 -*-
"""
    Save and move avatar to a position.
    Read and write avatar positions.
    2018-05-21
"""


from Plasma import *
import os

## Set the file name
def SetFileName(self):
    ageFileName = PtGetAgeInfo().getAgeFilename()
    if not os.path.exists("Save"):
        os.mkdir("Save")
    fileName = "Save/{}.pos".format(ageFileName)
    return fileName

## Reads the file and returns a list of strings representing the saved positions
def ReadFile(fileName):
    positions = list()
    try:
        file = open(fileName, "r")
        content = file.read()
        file.close()
        for strPos in content.split("\n"):
            positions.append(strPos)
    except:
        # The file does not exist yet, the list of positions is empty
        positions = [""]
    return positions

## Write the file
def WriteFile(fileName, content):
    try:
        file = open(fileName, "w")
        file.write(content)
        file.close()
        return 1
    except:
        return 0

## Returns the tuple of the n-th position from a list of strings representing the saved positions
def GetPosition(positions, n=None):
    if type(positions) != list:
        return None
    if positions == list():
        return None
    if n == None:
        n = 0
    try:
        n = int(n)
    except:
        return None
    if n >= 0 and n < len(positions):
        lstPos = list()
        lstStr = positions[n].split("|")
        for s in lstStr:
            lst = s.split(";")
            lstVal = list()
            for elm in lst:
                lstVal.append(float(elm))
            lstPos.append(tuple(lstVal))
        tuplePos = tuple(lstPos)
        return tuplePos
    else:
        return None

## Write the position
def WriteMatrix44(self, n=None):
    if n is None:
        n = 0
    try:
        n = int(n)
    except:
        self.chatMgr.AddChatLine(None, "==> n must be a positive integer.", 3)
        return 1
    # Get the already known positions inthis age (if none, it'll return an empty list)
    fileName = SetFileName(self)
    positions = ReadFile(fileName)
    if n < 0:
        self.chatMgr.AddChatLine(None, "==> n must be a positive integer.", 3)
        return 1
    elif n >= len(positions):
        # I need to increase the number of positions in the list
        newPositions = [""] * (n - len(positions) + 1)
        positions.extend(newPositions)
    
    # Get new position
    soAvatar = PtGetLocalAvatar()
    matPos = soAvatar.getLocalToWorld()
    tuplePos = matPos.getData()
    strPos = ""
    for t in tuplePos:
        for e in t:
            strPos += str(e) + ";"
        strPos = strPos[:len(strPos) - 1]
        strPos += "|"
    strPos = strPos[:len(strPos) - 1]
    # Replace the n-th position by the new one
    positions[n] = strPos
    # Stringify the list of positions
    content = ""
    for strPos in positions:
        content += strPos + "\n"
    content = content[:len(content) - 1]
    # Edit the file
    if WriteFile(fileName, content) == 0:
        self.chatMgr.AddChatLine(None, "Error while saving your position!", 3)

def WarpToSaved(self, n=None):
    soAvatar = PtGetLocalAvatar()
    try:
        # Get the already known positions for thisage (if none, it'll return an empty list)
        fileName = SetFileName(self)
        positions = ReadFile(fileName)
        tuplePos = GetPosition(positions, n)
        matPos = ptMatrix44()
        matPos.setData(tuplePos)
        soAvatar.netForce(1)
        soAvatar.physics.warp(matPos)
        #self.chatMgr.AddChatLine(None, "You are going to your saved position.", 0)
        return 1
    except:
        #self.chatMgr.AddChatLine(None, "You have no saved position!", 3)
        return 0
