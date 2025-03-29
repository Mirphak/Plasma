# -*- coding: utf-8 -*-

from Plasma import *
from . import jalak_michel as jalak
import glob

path = "jeux\\Jcubes\\"
cubeFiles = glob.glob(path + "*.txt")
#print("cubeFiles = {}".format(cubeFiles))

f = list(map(lambda file: file.replace(path, '').split('.')[0].split('_'), cubeFiles))
#print("cubeFiles = {}".format(f))

f = list(filter(lambda file: file[1] != 'Minasunda', f))

#
class WaitAndLoadCubes:
    _nomFichier = ""
    _nomAvatar = ""
    #_delais = 20
    # il faut environ 20s pour que les colonne aillent de la position basse a la position haute
    
    def __init__(self, nomFichier, nomAvatar):
        self._nomFichier = nomFichier
        self._nomAvatar = nomAvatar
    def onAlarm(self, param):
        jalak.LoadCubes(self._nomFichier, self._nomAvatar)

#
def LoadStruct(nomFichier, nomAvatar):
    print("> LoadStruct")
    ageName = PtGetAgeName()
    if ageName != 'Jalak':
        return 0
    print(">> LoadStruct")
    maxDeltaHauteur = jalak.LoadColumns(nomFichier, nomAvatar)
    if maxDeltaHauteur < 0:
        #Le fichier des colonnes n'a pas ete charge
        maxDeltaHauteur = 0
    delai = maxDeltaHauteur
    PtSetAlarm(delai, WaitAndLoadCubes(nomFichier, nomAvatar), 1)
    return 1


### Display a message to the player (or players).
def SendChatMessage(msg):
    agePlayers = PtGetPlayerList()
    myself = PtGetLocalPlayer()
    #agePlayers.append(myself)

    if msg is None:
        msg = "Oops, I forgot what I had to tell you!"
    
    if len(agePlayers) > 0:
        # Don't take care of flags nor bots, always send message as buddies inter-age
        #PtSendRTChat(fromPlayer=myself, toPlayerList=agePlayers, message=msg, flags=24)
        PtSendRTChat(myself, agePlayers, msg, 24)

#
i = 0
imax = len(f)

#
def next():
    global i
    #SendChatMessage(msg="Loading structure '{}' from {} ...".format(f[i][0], f[i][1]))
    try:
        SendChatMessage(msg="Loading structure '{}' ...".format(f[i][0], ))
        LoadStruct(nomFichier=f[i][0], nomAvatar=f[i][1])
    i += 1
    if i >= imax :
        i = 0

#