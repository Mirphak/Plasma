# Avatar
# Functions to manipulate avatars.

from Plasma import *
#from Players import *

#def RemoveAllBooks():
#	agePlayers = GetAll()
#	for player in agePlayers:
#		player.netForce(1)
#		player.avatar.removeClothingItem("FAccPlayerBook")
#		player.avatar.removeClothingItem("MAccPlayerBook") - Old don't use 

# Thanks Stone 
def ToggleAccPlayerBooks(en=0):

    ''' Remove/Wear the M/F AccPlayerBook from everyone in this age. '''

    for player in PtGetPlayerList() + [PtGetLocalPlayer(),]:
        avatar = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject().avatar
        name = ('M', 'F')[avatar.getAvatarClothingGroup()] + 'AccPlayerBook'
        avatar.netForce(1)
        (avatar.removeClothingItem, avatar.wearClothingItem)[en](name)


"""
from Plasma import *
from Basic import *
GoMePubNew_Default
NetPageIn("GoMePubNew_Default")

PtConsoleNet("Nav.PageInNode GoMePubNew_Default", True)

PtGetLocalAvatar().avatar.removeClothingItem("FAccPlayerBook")

"""