# -*- coding: utf-8 -*-

#Import du module Plasma
from Plasma import *
import math


# Ki des robots (pour les exclure si je lance une commande pour tous les joueurs)
# en fait je ne me sers que des numeros de KI, les noms c'est pour info
"""
dicBot = {
            19542524L:"Mir-o-Bot", 
            19040117L:"MagicBot", 
            19316060L:"MimiBot", 
            21418998L:"Magic Bot", 
            21420380L:"Mimi Bot", 
            18327624L:"Lyrobot", 
            17511267L:"Stone5", 
            #15112736L:"STA1",
            20916217L:"Annabot",
            20969016L:"SkydiverBot",
            1516847L:"OHBot",
            16974699L:"sad",
            #13013841L:"Sautaillet",
            23656022L:"Magic-Treasure",
            23433946L:"Magic Treasure",
            26010113L:"Mimi Treasure",
            }
"""
dicBot = {
    32319:"Mir-o-Bot", 
    27527:"Magic Bot", 
    71459:"Mimi Bot", 
    #L:"Stone5", 
    64145:"Annabot",
    #L:"SkydiverBot",
    3975:"OHBot",
    24891:"Magic-Treasure",
    26224:"Magic Treasure",
    21190:"Mimi Treasure",
    2332508:"mob",
    8848659:"Magic Skydiver",
    }

#
def Cercle(coef=5.0, h=10.0, avCentre=None):
    if avCentre is None:
        avCentre = PtGetLocalAvatar()
    #agePlayers = GetAllAgePlayers()
    # ne pas tenir compte des robots
    agePlayers = [pl for pl in PtGetPlayerList() if not(pl.getPlayerID() in list(dicBot.keys()))]
    i = 0
    n = len(agePlayers)
    print("nb de joueurs: %s" % (n))
    dist = float(coef * n) / (2.0 * math.pi)
    print("distance: %s" % (dist))
    for i in range(n):
        player = agePlayers[i]
        avatar = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
        angle = (float(i) * 2.0 * math.pi) / float(n)
        print("angle(%s): %s" % (i, angle))
        dx = float(dist)*math.cos(angle)
        dy = float(dist)*math.sin(angle)
        matrix = avCentre.getLocalToWorld()
        matrix.translate(ptVector3(dx, dy, float(h)))
        avatar.netForce(1)
        avatar.physics.warp(matrix)
        #i += 1

# Add a player in my buddies list if not yet a friend
def AddBud(playerId):
    vault = ptVault()
    buddies = vault.getBuddyListFolder()
    try:
        localPlayer = PtGetLocalPlayer()
        if playerId != localPlayer.getPlayerID():
            if not buddies.hasPlayer(playerId):
                buddies.addPlayer(playerId)
                return True
    except:
        return False

# Add a player in my ignore list if not yet ignored
def AddIgnore(playerId):
    vault = ptVault()
    ignores = vault.getIgnoreListFolder()
    try:
        localPlayer = PtGetLocalPlayer()
        if playerId != localPlayer.getPlayerID():
            if not ignores.hasPlayer(playerId):
                ignores.addPlayer(playerId)
                return True
    except:
        return False

# Remove a player from my buddy list
def RemoveBuddy(playerId):
    vault = ptVault()
    buddies = vault.getBuddyListFolder()
    try:
        localPlayer = PtGetLocalPlayer()
        if playerId != localPlayer.getPlayerID():
            if buddies.hasPlayer(playerId):
                buddies.removePlayer(playerId)
                return True
    except:
        return False

# Remove a player from my ignore list
def RemoveIgnore(playerId):
    vault = ptVault()
    ignores = vault.getIgnoreListFolder()
    try:
        localPlayer = PtGetLocalPlayer()
        if playerId != localPlayer.getPlayerID():
            if ignores.hasPlayer(playerId):
                ignores.removePlayer(playerId)
                return True
    except:
        return False

# Is the player a friend?
def IsBud(playerId):
    vault = ptVault()
    buddies = vault.getBuddyListFolder()
    try:
        localPlayer = PtGetLocalPlayer()
        if not isinstance(playerId, int):
            return False
        if playerId == 0:
            return False
        if playerId == localPlayer.getPlayerID():
            return False
        if buddies.hasPlayer(playerId):
            return True
    except:
        return False

# Is the player ignored?
def IsIgnore(playerId):
    vault = ptVault()
    ignores = vault.getIgnoreListFolder()
    try:
        localPlayer = PtGetLocalPlayer()
        if not isinstance(playerId, int):
            return False
        if playerId == 0:
            return False
        if playerId == localPlayer.getPlayerID():
            return False
        if ignores.hasPlayer(playerId):
            return True
    except:
        return False

#

def UploadImage(imagefile,imagetitle,playerId=0,width=0,height=0): 
    #envoie image depuis le pc vers un playerId (l'playerId doit etre different de celui qui l'envoie)
    #il faudrait chercher pour voir comment le sauver dans le ki de celui qui l'envoie (voir dans plasma.class ptVaultImageNode(ptVaultNode))
    #width, height laisser a 0 pour ne pas modifier l'image originale
    #les tests ont ete effectues avec des fichiers dont la taille est voisine des images sauvegardees depuis le ki (+/- 90 KB)
    #imagefile est le nom sur le disque dans le repertoire d'install avec extension .jpg
    #exemple : UploadImage('Test.jpg','Mon test',1255010) : fichier Test.jpg, envoye a 1255010, avec le nom Mon Test
    try:
        img = PtLoadJPEGFromDisk(imagefile,width,height)
        node = ptVaultImageNode(0)
        node.setImage(img)
        node.setTitle(imagetitle)
        playerid = PtGetLocalPlayer().getPlayerID()
        if playerId != playerid and playerId != 0:
            node.sendTo(playerId)
        return True
    except:
        return False


#