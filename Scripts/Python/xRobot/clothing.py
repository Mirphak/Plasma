# -*- coding: utf-8 -*-

"""
Saveme : To save your current appearance. 
Restoreme : To recover your usual look. (the last saved by the bot!) 
"""

from Plasma import *
from PlasmaTypes import *
import string
import os

# Constants
kNumberOfMorphs = 9
kNumberOfTexMorphs = 4

#
def SetFileName(clothingName):
    subdir = "Clothing"
    if not os.path.exists(subdir):
        os.mkdir(subdir)
    fileName = "{0}/{1}.txt".format(subdir, clothingName)
    return fileName

#Pour savoir si le joueur est dans l'age du robot
def IsPlayerInAge(player):
    if player.getPlayerID() == PtGetLocalPlayer().getPlayerID():
        return True
    agePlayers = PtGetPlayerList()
    ids = [player.getPlayerID() for player in agePlayers]
    try:
        if player.getPlayerID() in ids:
            return True
        else:
            return False
    except:
        return False

#av = PtGetAvatarKeyFromClientID(player[0].getPlayerID()).getSceneObject()
def SaveAvatarClothingTo(player, clothingName):
    print("xRobot.clothing.SaveAvatarClothingTo(): INIT")
    clothingFileName = SetFileName(clothingName)
    if IsPlayerInAge(player):
        # grab current settings
        #avatar = PtGetLocalAvatar()
        avatar = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
        worn = avatar.avatar.getAvatarClothingList()
        clothingList = []
        color1 = []
        color2 = []
        print("xRobot.clothing.SaveAvatarClothingTo(): 1")
        for item in worn:
            clothingList.append(item[0])
            color1.append(avatar.avatar.getTintClothingItem(item[0],1))
            color2.append(avatar.avatar.getTintClothingItem(item[0],2))
        skinColor = avatar.avatar.getTintSkin()
        gender = avatar.avatar.getAvatarClothingGroup()
        geomMorphs = []
        print("xRobot.clothing.SaveAvatarClothingTo(): 2")
        # I don't know why but there is an error for females here
        """
        for morphID in range(kNumberOfMorphs):
            morphVal = 0
            try:
                if gender == kFemaleClothingGroup:
                    morphVal = avatar.avatar.getMorph("FFace",morphID)
                else:
                    morphVal = avatar.avatar.getMorph("MFace",morphID)
            except:
                #pass
                print u"xRobot.clothing.SaveAvatarClothingTo(): morphID:{}, morphVal:{}".format(morphID, morphVal)
            geomMorphs.append(morphVal)
        texMorphs = []
        """
        # Le'ts try something else : male by default, try to test if gender is female on error force as female
        face = "MFace"
        try:
            if gender == kFemaleClothingGroup:
                face = "FFace"
        except:
            print("Gender face morph error for female! Force as female...")
            face = "FFace"
        print("xRobot.clothing.SaveAvatarClothingTo(): Gender face = {}".format(face))
        try:
            for morphID in range(kNumberOfMorphs):
                morphVal = 0
                try:
                    morphVal = avatar.avatar.getMorph(face,morphID)
                except:
                    #pass
                    print("xRobot.clothing.SaveAvatarClothingTo(): morphID:{}, morphVal:{}".format(morphID, morphVal))
                geomMorphs.append(morphVal)
        except KeyError as err:
            print(("Key error: {0}".format(err)))
        except:
            print(("Unexpected error:", sys.exc_info()[0]))

        print("xRobot.clothing.SaveAvatarClothingTo(): 3")
        texMorphs = []
        for texMorphID in range(kNumberOfTexMorphs):
            morphVal = 0
            try:
                morphVal = avatar.avatar.getSkinBlend(texMorphID)
            except:
                #pass
                "xRobot.clothing.SaveAvatarClothingTo(): texMorphID:{}, morphVal:{}".format(texMorphID, morphVal)
            texMorphs.append(morphVal)
        ageMorph = 0
        try:
            ageMorph = avatar.avatar.getSkinBlend(4)
        except:
            #pass
            print("xRobot.clothing.SaveAvatarClothingTo(): ageMorph:{}".format(ageMorph))
        
        #name = PtGetLocalPlayer().getPlayerName()
        print("xRobot.clothing.SaveAvatarClothingTo(): 4")
        
        try:
            # write them to a file on disk
            #saveFile = open(name+".avatar.ava",'w')
            saveFile = open(clothingFileName,'w')
            #
            saveFile.write(str(len(clothingList))+'\n')
            for i in range(len(clothingList)):
                item = clothingList[i]
                item += ' '+str(color1[i].getRed())+' '+str(color1[i].getGreen())+' '+str(color1[i].getBlue())
                item += ' '+str(color2[i].getRed())+' '+str(color2[i].getGreen())+' '+str(color2[i].getBlue())
                saveFile.write(item+'\n')
            saveFile.write(str(skinColor.getRed())+' '+str(skinColor.getGreen())+' '+str(skinColor.getBlue())+'\n')
            saveFile.write(str(len(geomMorphs))+'\n')
            for i in range(len(geomMorphs)):
                saveFile.write(str(geomMorphs[i])+'\n')
            saveFile.write(str(len(texMorphs))+'\n')
            for i in range(len(texMorphs)):
                saveFile.write(str(texMorphs[i])+'\n')
            saveFile.write(str(ageMorph)+'\n')
            # write the gender at the end
            saveFile.write(str(gender)+'\n')
            saveFile.close()
            return True
        except IOError:
            print("xRobot.clothing.SaveAvatarClothingTo(): ERROR WHILE WRITTING FILE (\"{}\").".format(saveFile))
            return False
    else:
        return False

#
def LoadAvatarClothingFrom(player, clothingName):
    print("xRobot.clothing.LoadAvatarClothingFrom(): INIT")
    clothingFileName = SetFileName(clothingName)
    if IsPlayerInAge(player):
        # open the file and read in the settings
        #name = PtGetLocalPlayer().getPlayerName()
        try:
            #saveFile = open(name+".avatar.ava",'r')
            saveFile = open(clothingFileName,'r')
            #
            numClothingItems = int(saveFile.readline())
            clothingList = []
            color1 = []
            color2 = []
            for i in range(numClothingItems):
                line = saveFile.readline()
                items = line.split()
                clothingList.append(items[0])
                color1.append(ptColor(float(items[1]),float(items[2]),float(items[3])))
                color2.append(ptColor(float(items[4]),float(items[5]),float(items[6])))
            line = saveFile.readline()
            items = line.split()
            skinColor = ptColor(float(items[0]),float(items[1]),float(items[2]))
            numMorphs = int(saveFile.readline())
            geomMorphs = []
            for i in range(numMorphs):
                morphVal = float(saveFile.readline())
                geomMorphs.append(morphVal)
            numMorphs = int(saveFile.readline())
            texMorphs = []
            for i in range(numMorphs):
                morphVal = float(saveFile.readline())
                texMorphs.append(morphVal)
            ageMorph = float(saveFile.readline())
            # finally the gender (if exists)
            try:
                fileGender = int(saveFile.readline())
            except:
                fileGender = 0
            saveFile.close()
            
            print("xRobot.clothing.LoadAvatarClothingFrom(): 0")
            #avatar = PtGetLocalAvatar()
            avatar = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
            gender = avatar.avatar.getAvatarClothingGroup()
            if fileGender != gender:
                print("xRobot.clothing.LoadAvatarClothingFrom(): Bad gender!")
                return True, "Incorrect gender"
            
            print("xRobot.clothing.LoadAvatarClothingFrom(): 1")
            # Et si on virait tout, tout simplement...
            avatar.avatar.netForce(1)
            worn = avatar.avatar.getAvatarClothingList()
            for item in worn:
                avatar.avatar.removeClothingItem(item[0])
            
            print("xRobot.clothing.LoadAvatarClothingFrom(): 2")
            # add all the clothing items back
            for i in range(len(clothingList)):
                item = clothingList[i]
                clr1 = color1[i]
                clr2 = color2[i]
                avatar.avatar.wearClothingItem(item,0)
                avatar.avatar.tintClothingItem(item,clr1,0)
                avatar.avatar.tintClothingItemLayer(item,clr2,2)
                # add the matching item, if it exists
                matchingItem = avatar.avatar.getMatchingClothingItem(item)
                if type(matchingItem) == type([]):
                    avatar.avatar.wearClothingItem(matchingItem[0],0)
                    avatar.avatar.tintClothingItem(matchingItem[0],clr1,0)
                    avatar.avatar.tintClothingItemLayer(matchingItem[0],clr2,2,0)
            print("xRobot.clothing.LoadAvatarClothingFrom(): 3")
            # reset skin color
            avatar.avatar.tintSkin(skinColor)
            print("xRobot.clothing.LoadAvatarClothingFrom(): 4")
            # reset geometry morphs
            """
            for morphID in range(len(geomMorphs)):
                gender = avatar.avatar.getAvatarClothingGroup()
                print u"xRobot.clothing.LoadAvatarClothingFrom(): 5 - morphID : {}, gender : {}".format(morphID, gender)
                if gender == kFemaleClothingGroup:
                    avatar.avatar.setMorph("FFace",morphID,geomMorphs[morphID])
                else:
                    avatar.avatar.setMorph("MFace",morphID,geomMorphs[morphID])
            """
            # Le'ts try something else : male by default, try to test if gender is female on error force as female
            face = "MFace"
            try:
                if gender == kFemaleClothingGroup:
                    face = "FFace"
            except:
                print("Gender face morph error for female! Force as female...")
                face = "FFace"
            print("xRobot.clothing.LoadAvatarClothingFrom(): Gender face = {}".format(face))
            try:
                for morphID in range(len(geomMorphs)):
                    print("xRobot.clothing.LoadAvatarClothingFrom(): 5 - morphID : {}, gender : {}".format(morphID, gender))
                    try:
                        avatar.avatar.setMorph(face,morphID,geomMorphs[morphID])
                    except:
                        #pass
                        print("xRobot.clothing.LoadAvatarClothingFrom(): morphID:{}, geomMorph:{}".format(morphID, geomMorphs[morphID]))
            except KeyError as err:
                print(("Key error: {0}".format(err)))
            except:
                print(("Unexpected error:", sys.exc_info()[0]))
            
            print("xRobot.clothing.LoadAvatarClothingFrom(): 6")
            # reset texture morphs
            for morphID in range(len(texMorphs)):
                avatar.avatar.setSkinBlend(morphID,texMorphs[morphID])
            print("xRobot.clothing.LoadAvatarClothingFrom(): 7")
            avatar.avatar.setSkinBlend(4,ageMorph)
            return True
        except IOError:
            return False
    else:
        return False

"""
#
def SaveMe(self, cFlags, args = []):
    if len(args) < 2:
        return 0
    params = args[1].split()
    if len(params) < 1:
        return 0
    myself = PtGetLocalPlayer()
    player = args[0]
    if not isPlayerInAge(player):
        SendChatMessage(self, myself, [player], "You must be in my age, use link to join me." , cFlags.flags)
        return 1
    # set action
"""

# **********************************
# ** From xAvatarCustomization.py **
# **********************************
"""
kNumberOfMorphs = 9
#E:\MystOnLineUruLiveAgain\PlClient_Mirphak\Python\plasma\PlasmaTypes.py (1 hit) Line 127
#kFemaleClothingGroup=1
kNumberOfTexMorphs = 4
"""

"""
#----ClothingListboxes
kHairOptionsLB=70
kHeadOptionsLB=71
kUpperBodyOptionsLB=72
kHandsOptionsLB=73
kLwrBodyOptionsLB=74
kFeetOptionsLB=75
#kAccessOptionsLB=76

#=== color types
kColorTypeNone=0
kColorTypeNormal=1
kColorTypeSkin=2
kColorTypeHair=3
#-----Clothing list cross reference (to clothing lists, clothing types and listboxes
#   [0] = clothing_type; [1] = listbox ID; [2] = colorType; [3] = saturation;
#   [4] = number of items per; [5] = Closet'd clothing;
#   [6] = Closet color layer 1; [7] = Closet color layer 2
CLxref = [ [kHairClothingItem,kHairOptionsLB,kColorTypeHair,0.25,1,1,1,1],\
           [kFaceClothingItem,kHeadOptionsLB,kColorTypeSkin,0.25,1,0,1,0],\
           [kShirtClothingItem,kUpperBodyOptionsLB,kColorTypeNormal,0.40,1,1,1,1],\
           [kRightHandClothingItem,kHandsOptionsLB,kColorTypeNone,0.0,2,1,1,1],\
           [kPantsClothingItem,kLwrBodyOptionsLB,kColorTypeNormal,0.25,1,1,1,1],\
           [kRightFootClothingItem,kFeetOptionsLB,kColorTypeNormal,0.25,2,1,1,1] ]
#====
def FindSaturationAndCloset(itemname,itemtype):
    "returns the color type and saturation for a particular clothing item"
    # this returns the default for clothing type, ClothingItem.__init__ will determine local
    for xref in CLxref:
        if xref[0] == itemtype:
            return (xref[2],xref[3],xref[5],xref[6],xref[7])
    return (0,0,1,1,1)
"""

"""
#
def SaveAvatarToDisk():
    # grab current settings
    avatar = PtGetLocalAvatar()
    worn = avatar.avatar.getAvatarClothingList()
    clothingList = []
    color1 = []
    color2 = []
    for item in worn:
        clothingList.append(item[0])
        color1.append(avatar.avatar.getTintClothingItem(item[0],1))
        color2.append(avatar.avatar.getTintClothingItem(item[0],2))
    skinColor = avatar.avatar.getTintSkin()
    gender = avatar.avatar.getAvatarClothingGroup()
    geomMorphs = []
    for morphID in range(kNumberOfMorphs):
        morphVal = 0
        try:
            if gender == kFemaleClothingGroup:
                morphVal = avatar.avatar.getMorph("FFace",morphID)
            else:
                morphVal = avatar.avatar.getMorph("MFace",morphID)
        except:
            pass
        geomMorphs.append(morphVal)
    texMorphs = []
    for texMorphID in range(kNumberOfTexMorphs):
        morphVal = 0
        try:
            morphVal = avatar.avatar.getSkinBlend(texMorphID)
        except:
            pass
        texMorphs.append(morphVal)
    ageMorph = 0
    try:
        ageMorph = avatar.avatar.getSkinBlend(4)
    except:
        pass
    name = PtGetLocalPlayer().getPlayerName()
    
    # write them to a file on disk
    saveFile = open(name+".avatar.ava",'w')
    saveFile.write(str(len(clothingList))+'\n')
    for i in range(len(clothingList)):
        item = clothingList[i]
        item += ' '+str(color1[i].getRed())+' '+str(color1[i].getGreen())+' '+str(color1[i].getBlue())
        item += ' '+str(color2[i].getRed())+' '+str(color2[i].getGreen())+' '+str(color2[i].getBlue())
        saveFile.write(item+'\n')
    saveFile.write(str(skinColor.getRed())+' '+str(skinColor.getGreen())+' '+str(skinColor.getBlue())+'\n')
    saveFile.write(str(len(geomMorphs))+'\n')
    for i in range(len(geomMorphs)):
        saveFile.write(str(geomMorphs[i])+'\n')
    saveFile.write(str(len(texMorphs))+'\n')
    for i in range(len(texMorphs)):
        saveFile.write(str(texMorphs[i])+'\n')
    saveFile.write(str(ageMorph)+'\n')
    saveFile.close()
"""

"""
# Version modifiee
def GetClothingWorn():
    "Avatars clothing has changed"
    #global WornList
    avatar = PtGetLocalAvatar()
    # update what is being worn (it may have changed)
    worn = avatar.avatar.getAvatarClothingList()
    WornList = []
    for item in worn:
        colortype,saturation,inCloset,inClosClr1,inClosClr2 = FindSaturationAndCloset(item[0],item[1])
        WornList.append(ClothingItem(item,colortype,saturation,inCloset,inClosClr1,inClosClr2))
    return WornList
"""

"""
#def IRestoreAvatarFromDisk(self):
def RestoreAvatarFromDisk():
    # open the file and read in the settings
    name = PtGetLocalPlayer().getPlayerName()
    try:
        saveFile = open(name+".avatar.ava",'r')
        numClothingItems = int(saveFile.readline())
        clothingList = []
        color1 = []
        color2 = []
        for i in range(numClothingItems):
            line = saveFile.readline()
            items = line.split()
            clothingList.append(items[0])
            color1.append(ptColor(float(items[1]),float(items[2]),float(items[3])))
            color2.append(ptColor(float(items[4]),float(items[5]),float(items[6])))
        line = saveFile.readline()
        items = line.split()
        skinColor = ptColor(float(items[0]),float(items[1]),float(items[2]))
        numMorphs = int(saveFile.readline())
        geomMorphs = []
        for i in range(numMorphs):
            morphVal = float(saveFile.readline())
            geomMorphs.append(morphVal)
        numMorphs = int(saveFile.readline())
        texMorphs = []
        for i in range(numMorphs):
            morphVal = float(saveFile.readline())
            texMorphs.append(morphVal)
        ageMorph = float(saveFile.readline())
        saveFile.close()
        
        '''
        # une modif a moi
        WornList = GetClothingWorn()
        
        # now set up the avatar properly
        # reset our clothing
        avatar = PtGetLocalAvatar()
        # remove all accessories that aren't in our accessory list
        for item in WornList:
            if item.accessoryType >= 0:
                found = 0
                for acc in DefaultClothing:
                    if acc.name == item.name:
                        found = 1
                        break
                if not found:
                    avatar.avatar.removeClothingItem(item.name)
        # Et si on virait tout, tout simplement...
        for item in WornList:
            avatar.avatar.removeClothingItem(item.name)
        '''
        # Et si on virait tout, tout simplement...
        avatar = PtGetLocalAvatar()
        worn = avatar.avatar.getAvatarClothingList()
        for item in worn:
            avatar.avatar.removeClothingItem(item[0])
        
        # add all the clothing items back
        for i in range(len(clothingList)):
            item = clothingList[i]
            clr1 = color1[i]
            clr2 = color2[i]
            avatar.avatar.wearClothingItem(item,0)
            avatar.avatar.tintClothingItem(item,clr1,0)
            avatar.avatar.tintClothingItemLayer(item,clr2,2)
            # add the matching item, if it exists
            matchingItem = avatar.avatar.getMatchingClothingItem(item)
            if type(matchingItem) == type([]):
                avatar.avatar.wearClothingItem(matchingItem[0],0)
                avatar.avatar.tintClothingItem(matchingItem[0],clr1,0)
                avatar.avatar.tintClothingItemLayer(matchingItem[0],clr2,2,0)
        # reset skin color
        avatar.avatar.tintSkin(skinColor)
        # reset geometry morphs
        for morphID in range(len(geomMorphs)):
            gender = avatar.avatar.getAvatarClothingGroup()
            if gender == kFemaleClothingGroup:
                avatar.avatar.setMorph("FFace",morphID,geomMorphs[morphID])
            else:
                avatar.avatar.setMorph("MFace",morphID,geomMorphs[morphID])
        # reset texture morphs
        for morphID in range(len(texMorphs)):
            avatar.avatar.setSkinBlend(morphID,texMorphs[morphID])
        avatar.avatar.setSkinBlend(4,ageMorph)
        ## give the avatar a bit of time to update before trying to update the controls
        #PtAtTimeCallback(self.key, 1, kTimerUpdateControls)
    except IOError:
        pass
"""

#
