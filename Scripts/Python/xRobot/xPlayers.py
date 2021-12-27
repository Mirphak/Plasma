# -*- coding: utf-8 -*-

#Import du module Plasma
from Plasma import *
import math


# Ki des robots (pour les exclure si je lance une commande pour tous les joueurs)
# en fait je ne me sers que des numeros de KI, les noms c'est pour info
dicBot = {
    32319L:"Mir-o-Bot", 
    27527L:"Magic Bot", 
    71459L:"Mimi Bot", 
    3975L:"OHBot",
    24891L:"Magic-Treasure",
    26224L:"Magic Treasure",
    21190L:"Mimi Treasure",
    2332508L:"mob",
    }

#
def Cercle(coef=5.0, h=10.0, avCentre=None):
    if avCentre is None:
        avCentre = PtGetLocalAvatar()
    # ne pas tenir compte des robots
    agePlayers = filter(lambda pl: not(pl.getPlayerID() in dicBot.keys()), PtGetPlayerList())
    i = 0
    n = len(agePlayers)
    print "nb de joueurs: %s" % (n)
    dist = float(coef * n) / (2.0 * math.pi)
    print "distance: %s" % (dist)
    for i in range(n):
        player = agePlayers[i]
        avatar = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
        angle = (float(i) * 2.0 * math.pi) / float(n)
        print "angle(%s): %s" % (i, angle)
        dx = float(dist)*math.cos(angle)
        dy = float(dist)*math.sin(angle)
        matrix = avCentre.getLocalToWorld()
        matrix.translate(ptVector3(dx, dy, float(h)))
        avatar.netForce(1)
        avatar.physics.warp(matrix)

# v2
def AddBud(idplayer):
    vault = ptVault()
    buddies = vault.getBuddyListFolder()
    try:
        localPlayer = PtGetLocalPlayer()
        if idplayer != localPlayer.getPlayerID():
            if not buddies.playerlistHasPlayer(idplayer):
                buddies.playerlistAddPlayer(idplayer)
                return True
    except:
        return False
