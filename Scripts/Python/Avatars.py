# Avatars
# Control the avatars in your Hood.

import math


from Plasma import *
from PlasmaTypes import *

from Basic import *
NetPageIn("MaleVertBlastLevel02")

# Avatars.Animate(string animation, string *players)
# Imposes a sequence of given animations on given players or all players.
def Animate(animation="dance", invert=False, *players):

    maleMoves = {"dance" : ["MaleDance"],
                 "crazy" : ["MaleCrazy"],
                 "link" : ["MaleLinkOut"],
                 "talk1" : ["MaleTalk"],
                 "talk2" : ["MaleTalk", "MaleTalk"], 
                 "ladder" : ["MaleLadderUpOn", "MaleLadderUp", "MaleLadderUp", "MaleLadderUp", "MaleLadderUpOff"],
                 "what" : ["MaleCrazy", "MaleRun", "MaleLaugh", "MaleDoh", "MaleSneeze", "MaleWallSlide"],
                 "swim" : ["MaleSwimFast", "MaleSwimFast", "MaleSwimFast"], 
                 "fall" : ["MaleVertBlastLevel02", "MaleWalkBack"], 
                 "moonwalk" : ["MaleWallSlide", "MaleWallSlide","MaleWallSlide","MaleWallSlide"],
                 "zombie" : ["MaleFall2","MaleFall2","MaleFall2","MaleFall","MaleFall", "MaleFall2", "MaleFall", "MaleFall", "MaleGroundImpact"],
                 "hammer" : ["MaleSideSwimLeft", "MaleSideSwimRight", "MaleSideSwimRight", "MaleSideSwimLeft"],
                 "bahrosit" : ["kgSitDownGround", "kgSitIdleGround", "kgSitStandGround"]}
    femaleMoves = {"dance" : ["FemaleDance"],
                   "crazy" : ["FemaleCrazy"],
                   "link" : ["FemaleLinkOut"],
                   "ladder" : ["FemaleLadderUpOn", "FemaleLadderUp", "FemaleLadderUp", "FemaleLadderUp", "FemaleLadderUpOff"],
                   "what" : ["FemaleCrazy", "FemaleRun", "FemaleLaugh", "FemaleDoh", "FemaleSneeze", "FemaleWallSlide"],
                   "swim" : ["FemaleSwimFast", "FemaleSwimFast", "FemaleSwimFast"],
                   "moonwalk" : ["FemaleWallSlide", "FemaleWallSlide","FemaleWallSlide","FemaleWallSlide"],
                   "zombie" : ["FemaleFall2","FemaleFall2","FemaleFall2","FemaleFall","FemaleFall", "FemaleFall2", "FemaleFall", "FemaleFall", "FemaleGroundImpact"],
                   "hammer" : ["FemaleSideSwimLeft", "FemaleSideSwimRight", "FemaleSideSwimRight", "FemaleSideSwimLeft"],
                   "bahrosit" : ["kgSitDownGround", "kgSitIdleGround", "kgSitStandGround"]}
    agePlayers = []
    if not players:
        agePlayers = GetAllAvatars()
    else:
        agePlayers = list(map(GetOneAvatar, players))
    for player in agePlayers:
        avatar = player.avatar
        objKey = player.getKey()
        gender = avatar.getAvatarClothingGroup()
        if invert:
            gender = not gender
        try:
            if gender == 0:
                animList = maleMoves[animation]
            else:
                animList = femaleMoves[animation]
        except KeyError:
            if gender == 0:
                animList = ["Male" + animation]
            else:
                animList = ["Female" + animation]
        avatar.netForce(1)
        for anim in animList:
            avatar.oneShot(objKey, 1, 1, anim, 0, 0)

# Avatars.ChangeSize(float scaler, string *players)
# Changes the size of avatars.
def ChangeSize(scaler, *players):

    agePlayers = []
    if not players:
        agePlayers = GetAllAvatars()
    else:
        agePlayers = list(map(GetOneAvatar, players))
    for player in agePlayers:
        player.netForce(1)
        if scaler:
            pos = player.getLocalToWorld()
            scale = ptMatrix44()
            scale.makeScaleMat(ptVector3(scaler, scaler, scaler))
            player.physics.disable()
            phys = player.physics
            phys.netForce(True)
            phys.warp(pos * scale)
        else:
            phys = player.physics
            phys.netForce(True)
            player.physics.enable()

# Avatars.ControlNPC(string avatar, string action, string player, string prefix)
# This function allows you to page in, animate and teleport a fully independent
# NPC using one of the custom avatars (Bahro1, Yeesha, Zandi, Blake, 
# Yeeshanoglow, Cate, Sutherland, Engberg, Kodama, Randmiller, Victor).
def ControlNPC(avatar, action="page", player=None, prefix=None):

    avatarList = {"Bahro1" : "kg",
                  "Yeesha" : "Female",
                  "Zandi" : "Male",
                  "Blake" : "Male",
                  "Yeeshanoglow" : "Female",
                  "Cate" : "Female",
                  "Sutherland" : "Female",
                  "Engberg" : "Male",
                  "Kodama" : "Male",
                  "Randmiller" : "Male",
                  "Victor" : "Male"}
    action = action.strip().lower()
    avatar = avatar.strip().capitalize()
    if action == "page":
        NetPageIn(avatar)
    elif action == "move":
        if player is None:
            playerAvatar = GetOneAvatar("me")
        else:
            playerAvatar = GetOneAvatar(player)
        obj = PtFindSceneobject(avatar, "CustomAvatars")
        obj.netForce(1)
        pos = playerAvatar.getLocalToWorld()
        obj.physics.disable()
        obj.physics.warp(pos)
    else:
        obj = PtFindSceneobject(avatar, "CustomAvatars")
        obj.avatar.netForce(1)
        prefix = prefix or avatarList[avatar]
        action = prefix + action.capitalize()
        obj.avatar.oneShot(obj.getKey(), 1, 1, action, 0, 0)

# Avatars.CreateRing(int radius, int height, string *players)
# Creates a ring of specified players around a player.
def CreateRing(radius=5, height=0, *players):

    center = GetOneAvatar("me")
    playerList = GetAllAvatars()
    playerList = []
    if not players:
        playerList = GetAllAvatars()
    else:
        playerList = list(map(GetOneAvatar, players))
    pos = center.position()
    pos = ptVector3(pos.getX(), pos.getY(), pos.getZ() + int(height))
    transMat = ptMatrix44()
    transMat.makeTranslateMat(pos)
    radiusMat = ptMatrix44()
    radiusMat.makeTranslateMat(ptVector3(int(radius), 0, 0))
    reverseMat = ptMatrix44();
    reverseMat.makeRotateMat(2, math.pi / 2)
    ident = ptMatrix44()
    delta = 2 * math.pi / len(playerList)
    angle = 0.0
    for player in playerList:          
        rotateMat = ptMatrix44()
        rotateMat.makeRotateMat(2, angle)
        z = transMat * rotateMat * radiusMat * reverseMat
        player.physics.netForce(True)
        player.physics.warp(z)
        player.physics.enable()
        angle += delta

# Avatars.Ghost(int en, string *players)
# Turns given players or all players visible or invisible.
def Ghost(en=False, *players):

    agePlayers = []
    if not players:
        agePlayers = GetAllAvatars()
    else:
        agePlayers = list(map(GetOneAvatar, players))
    for player in agePlayers:
        player.draw.netForce(True)
        player.draw.enable(en)

# Avatars.Jump(int height, string *players)
# Makes all given players or all players jump a specified height.
def Jump(height=5, *players):

    agePlayers = []
    if not players:
        agePlayers = GetAllAvatars()
    else:
        agePlayers = list(map(GetOneAvatar, players))
    for avatar in agePlayers:
        matrix = avatar.getLocalToWorld()
        matrix.translate(ptVector3(0, 0, float(height)))
        avatar.netForce(True)
        avatar.physics.warp(matrix)

# Avatars.Light(int light, int en)
# Activates and deactivates KI lights or Eder Kemo bug lights for all players.
def Light(light=0, en=True):

    if light == 0:
        for player in GetAllAvatars():
            for resp in player.getResponders():
                if (en == True and resp.getName() == "respKILightOn") or (en == False and resp.getName() == "respKILightOff"):
                    RunResponder(player.getKey(), resp)
                    break
    elif light == 1:
        for player in GetAllAvatars():
            PtSetLightAnimStart(player.getKey(), "RTOmni-BugLightTest", en)

## Avatars.Locate(string player)
# Locates the provided player.
def Locate(player):

    avatar = GetOneAvatar(player)
    coords = avatar.position()
    x = coords.getX()
    y = coords.getY()
    z = coords.getZ()
    return x, y, z

## Avatars.Rotate(player, int degrees)
# Rotates the player a certain number of degrees.
def Rotate(player, axis, degrees):

    if axis == "x":
        axis = 0
    elif axis == "y":
        axis = 1
    else:
        axis = 2
    avatar = GetOneAvatar(player)
    avatar.physics.disable()
    matrix = avatar.getLocalToWorld()
    rot = ptMatrix44()
    rot.makeRotateMat(axis, math.radians(degrees))
    avatar.physics.netForce(True)
    avatar.physics.warp(matrix * rot)

# Avatars.TieToObject(int en, string player, string objName, string age)
# Ties an avatar to the specified object.
def TieToObject(en=1, player="me", objName="BeachBall", age="Neighborhood"):

    obj = PtFindSceneobject(objName, age)
    av = GetOneAvatar(player)
    pos = obj.getLocalToWorld()
    pos.translate(ptVector3(0, 0, 1.5))
    ph = av.physics
    ph.netForce(True)
    ph.enable(not en)
    if en == 1:
        ph.warp(pos)
        PtAttachObject(av, obj)
    elif en == 0:
        PtDetachObject(av, obj)

# Avatars.TieToPlayer(int en, string player)
# Ties a player to another player and makes him invisible.
def TieToPlayer(player1, player2="me", en=True):

    av1 = GetOneAvatar(player1)
    av2 = GetOneAvatar(player2)
    av2pos = av2.getLocalToWorld()
    av1ph = av1.physics
    av1dr = av1.draw
    av1ph.enable(not en)
    av1dr.enable(True)
    av1ph.netForce(True)
    if en == 1:
        av1ph.warp(av2pos)
        PtAttachObject(av1, av2)
    else:
        PtDetachObject(av1, av2)
