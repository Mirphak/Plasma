# -*- coding: cp1252 -*-
"""
import pickle

test = {
    "1":["a", "b", "c"], 
    "2":["d", "e", "f"], 
    "3":["g", "h", "i"], 
    }

def Save(obj, name):
    #with open('/' + name + '.pkl', 'wb') as f:
    #    pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)
    f = open('./' + name + '.pkl', 'wb')
    try:
        pickle.dump(obj, f)
    #except:
    #    print "Error wile reading file"
    finally:
        f.close()

def Load(name):
    #with open('/' + name + '.pkl', 'rb') as f:
    #    pickle.load(f)
    dic = {}
    f = open('./' + name + '.pkl', 'rb')
    try:
        dic = pickle.load(f)
    #except:
    #    print "Error wile reading file"
    finally:
        f.close()
        return dic
"""
#==============
"""
import yaml

data = dict(
    A = 'a',
    B = dict(
        C = 'c',
        D = 'd',
        E = 'e',
    )
)

with open('data.yml', 'w') as outfile:
    outfile.write( yaml.dump(data, default_flow_style=True) )

d = {'A':'a', 'B':{'C':'c', 'D':'d', 'E':'e'}}
with open('result.yml', 'w') as yaml_file:
    yaml_file.write( yaml.dump(d, default_flow_style=False))

with open('result.yaml', 'w') as f:
  yaml.dump(d, f, default_flow_style=False)
"""
#==============
"""
>>> import sys
>>> sys.path.append('J:\\MOULa_CWE\\Python\\xRobot')
sys.path.append('J:\\MOULa_CWE\\Python\\system')
"""
"""
import os
import yaml
"""
"""
from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper
"""
"""
data = load(stream, Loader=Loader)
output = dump(data, Dumper=Dumper)
"""
"""
test = {
    "1":["a", "b", "c"], 
    "2":["l'aube?", "h", "i"],
    "3":["à l'aube?", "h", "i"],
    "2189761": ["Art's Teledahn Inn", "01/12/15", "df8de6a9-3b43-4ddc-94c9-9d4ed248e3f0"], 
    "2195841": ["Hide and Marker? ", "01/13/15", "c4d08ed0-1d53-461d-be65-084e79650810"], 
    }
"""
"""
def Save(obj, fileName):
    if not os.path.exists("Games"):
        os.makedirs("Games")
    with open('Games/' + fileName + '.yaml', 'w') as f:
        #yaml.dump(obj, f, default_flow_style=False)
        #yaml.dump(obj, f, default_flow_style=None)
        #yaml.dump(obj, f, default_flow_style=False, default_style='"', indent=4, allow_unicode=True, encoding="cp1252")
        #yaml.dump(obj, f, default_flow_style=None, default_style='"', indent=4, allow_unicode=True, encoding="utf-8")
        yaml.dump(obj, f, default_flow_style=None, default_style='"')
        #yaml.dump(obj, f, default_flow_style=None, Dumper=yaml.BaseDumper)
        #dump(obj, f, Dumper=Dumper)
        #yaml.dump(obj, f, canonical=True)

def Load(fileName):
    obj = None
    with open('Games/' + fileName + '.yaml', 'r') as f:
        obj = yaml.load(f)
        #obj = load(f, Loader=Loader)
    return obj
"""
# ============ V 3 =============
import os
import sys
import datetime

# pour les tests en dehors du jeu:
#os.chdir('J:\\MOULa_CWE\\Python\\xRobot')
#sys.path.append('J:\\MOULa_CWE\\Python\\xRobot')
sys.path.append('J:\\MOULa_CWE\\Python\\system')
sys.path.append('J:\\MOULa_CWE\\Python\\plasma')
#import xRobot.ReadWrite as rw
#import system.yaml as yaml
import yaml

from Plasma import *
from PlasmaVaultConstants import *


fileName = "games"
gamesDic = None

def SaveGamesDic(obj=gamesDic, fileName="games"):
    if not os.path.exists("Games"):
        os.makedirs("Games")
    with open('Games/' + fileName + '.yaml', 'w') as f:
        yaml.dump(obj, f, default_flow_style=None, default_style='"')

def LoadGamesDic(fileName="games"):
    obj = None
    with open('Games/' + fileName + '.yaml', 'r') as f:
        obj = yaml.load(f)
    return obj

#gamesDic = LoadGamesDic()

# Recherche un jeu de marqueur par son Guid
def GetGameByGuid(gameGuid):
    tempNode = ptVaultMarkerGameNode()
    tempNode.setGameGuid(gameGuid)

    try:
        node = ptVault().findNode(tempNode)
        if node.getType() == PtVaultNodeTypes.kMarkerGameNode:
            game = node.upcastToMarkerGameNode()
            print "game found"
            return game
        else:
            print "game not found"
            return None
    except:
        print "error in GetGameByGuid"
        return None

"""
Il faut que je transforme ta liste en un dictionnaire, genre:

listeJeux ={"#ID":["NomJeux", "Guid du jeux"], ...}

Le joueur va faire sa demande comme chez toi via son #ID,
puis gameGuid = listeJeux["#ID"][1]

game = GetGameByGuid(gameGuid)

Et je fais comme toi pour l'envoyer:

    if game is not None:
        game.sendTo(idAvatar)
        return 1
    else :
        return 0

Voila, en principe ça devrait marcher.
"""
#
def GetGameFromGamesDic(gameId=0):
    gamesDic = LoadGamesDic()
    strGameId = ""
    if isinstance(gameId, int):
        strGameId = str(gameId)
    if isinstance(gameId, str):
        strGameId = gameId
    else:
        print "Error in GetGameFromGamesDic: gameId must be an integer or a string"
        return None
    strGameId.lstrip("0")
    if strGameId in gamesDic.Keys:
        gameGuid = gamesDic[strGameId][1]
        game = GetGameByGuid(gameGuid)
        if game is not None:
            print "GetGameFromGamesDic: Game found => #{}".format(game.getID())
            print "> Name:{}".format(game.getGameName())
            print "> Date:{}".format(game.getCreateTime())
            print "> Guid:{}".format(game.getGameGuid())
            print "> CreatorID:{}".format(game.getCreatorNodeID())
            print "> Age:{}".format(game.getCreateAgeName())
        else:
            print "GetGameFromGamesDic: Game #{} not found in the vault!".format(strGameId)
        return game
    else:
        print "Error in GetGameFromGamesDic: gameId {} not found".format(strGameId)
        return None

#
def SendGame(gameId, playerId=None):
    if playerId is None:
        playerId = PtGetLocalPlayer().getPlayerID()
    elif not isinstance(playerId, int):
        print "Error in SendGame : playerId must be an integer"
        return 0
    game = GetGameFromGamesDic(gameId=0)
    if game is not None:
        # Envoyer la quete
        try:
            game.sendTo(playerId)
            print "SendGame : game #{} sent to #{}".format(game.getID, playerId)
            return 1
        except:
            print "SendGame : Error while sending game"
            return 0

#
"""
today = datetime.date.today()
print str(today)
print today.strftime('We are the %d, %b %Y')

            gametime = img.getModifyTime()
            st = datetime.datetime.fromtimestamp(gametime).strftime('%m/%d/%y')
"""
# Get new games in my inbox folder
def GetNewInboxGames():
    gamesDic = LoadGamesDic()
    nbNewGames = 0
    inbox = ptVault().getInbox()
    if inbox is not None:
        if inbox.getType() == PtVaultNodeTypes.kFolderNode:
            subs = inbox.getChildNodeRefList()
            for sub in subs:
                sub = sub.getChild()
                if sub.getType() == PtVaultNodeTypes.kMarkerGameNode:
                    game = sub.upcastToMarkerGameNode()
                    if game is not None:
                        strGameId = str(game.getID)
                        if strGameId not in gamesDic.Keys:
                            gamesDic.update({strGameId: [game.getGameName(), game.getModifyTime(), game.getGameGuid()]})
                            nbNewGames = nbNewGames + 1
                            print "New game added : #{}, {}, {}, {}".format(strGameId, game.getGameName(), game.getModifyTime(), game.getGameGuid())
            print "=> {} new games added".format(nbNewGames)
            if nbNewGames > 0:
                SaveGamesDic(gamesDic)
        else:
            print "inbox is not a folder node!"
    else:
        print "your vault indox was not found!"
