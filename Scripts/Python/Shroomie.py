# Shroomie
# Allows for management of the entity known as Shroomie.
# Shromie can:
# - Grow/shrink Shroomie.
# - Reload herself when someone links in.
# - Run some animations.
# - Warp to another player.

from Plasma import *

from Basic import *


class Shroomie:

    # Page in Teledahn the first time.
    def __init__(self):

        self.shroomie = None
        self.shroomieHandle = None
        NetPageIn("tldnHarvest")
        PtSetAlarm(3, self, 1)

    # React to alarms.
    def onAlarm(self, context):

        # Initial manipulations of Shroomie.
        if context == 1:
            self.shroomie = PtFindSceneobject("MasterShroomie", "Teledahn")
            self.shroomieHandle = PtFindSceneobject("LakeShoomieHandle", "Teledahn")
            self.shroomie.netForce(True)
            self.shroomieHandle.netForce(True)
        # Reload Shroomie for newly paged-in players.
        elif context == 2:
            self.ReloadPos()

    # Change Shroomie's size.
    def ChangeSize(self, scale):

        ScaleObj("LakeShoomieHandle", scale, age="Teledahn")

    # Make Shroomie visible.
    def MakeVisible(self):

        respName = "cRespShroomieVisible"
        responders = self.shroomie.getResponders()
        for responder in responders:
            if responder.getName() == respName:
                RunResponder(self.shroomie.getKey(), responder)
                break

    # Reload Shroomie's position for new players.
    def ReloadPos(self):

        position = self.shroomieHandle.position()
        self.shroomieHandle.physics.warp(position)

    # Run a behavior on Shroomie.
    def RunBehavior(self, behavior):

        responders = self.shroomieHandle.getResponders()
        responder = responders[behavior]
        RunResponder(self.shroomie.getKey(), responder)

    # Warp Shroomie to the specified player.
    def WarpToPlayer(self, player):

        avatar = GetOneAvatar(player)
        self.shroomieHandle.physics.warp(avatar.getLocalToWorld())
