# -*- coding: utf-8 -*-
""" 
*******************
* Yodawave Eureka *
*******************
Que la lumière soit - Fiat lux

PtGetPlayerList()               # Retourne une liste d'objets ptPlayer dans l'age

class ptPlayer:
    def getPlayerID(self):
    def getPlayerName(self):                                                               

ptPlayer.getPlayerName(self):   # A partir de Name
    player = PtGetLocalPlayer()
    Name =player.getPlayerName()

ptKey   AvatarKey

AvatarKey = PtGetAvatarKeyFromClientID(AvatarID)    # A partire de ID
 
AvatarSceneObject = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()

AvatarSceneObject = AvatarKey.getSceneObject()

PtGetClientIDFromAvatarKey(AvatarKey)
PtGetClientName(AvatarKey=None)

CdPerso.IDavatarOk(NoID = 0)

type
"""

from Plasma import *
#import CdPerso
#import GestionClones
from FeuDeCampMir import CdPerso, GestionClones

def Get_Nom_ID_SceneObject_Avatar(NomOrID=None):
    PtDebugPrint(f"Eureka.Get_Nom_ID_SceneObject_Avatar(NomOrID={NomOrID})")
    if isinstance(NomOrID, str):
        AvatarName = NomOrID
        AvatarID = 0
    elif isinstance(NomOrID, int):
        AvatarID = NomOrID
        AvatarName = ""
    else:
        print ("erreur Nom_Or_ID")
    
    PtDebugPrint(f"Eureka.Get_Nom_ID_SceneObject_Avatar: AvatarName = {AvatarName}")
    PtDebugPrint(f"Eureka.Get_Nom_ID_SceneObject_Avatar: AvatarID = {AvatarID}")
    
    PlayerListAvatar = PtGetPlayerList()
    PlayerListAvatar.append(PtGetLocalPlayer())
    for Player in PlayerListAvatar:
        if AvatarName != "" and AvatarID == 0:
            AvatarName = AvatarName.lower().replace(' ', '')
            if Player.getPlayerName().lower() == AvatarName:
                AvatarKey = PtGetAvatarKeyFromClientID(Player.getPlayerID())
                break
        elif AvatarName == "" and AvatarID != 0:
            if Player.getPlayerID() == AvatarID:
                AvatarKey = PtGetAvatarKeyFromClientID(Player.getPlayerID())
                break
        else:
            return []
    ListRetour = []
    ListRetour.append(PtGetClientName(AvatarKey))
    ListRetour.append(PtGetClientIDFromAvatarKey(AvatarKey))
    ListRetour.append(AvatarKey.getSceneObject())
    PtDebugPrint(f"Eureka.Get_Nom_ID_SceneObject_Avatar: ListRetour = {ListRetour}")
    return ListRetour
    
def SpotSurAvatar(Avatar=None, NoSpot=1, On=0):  # NoSpot = 0 = Off, Avatar = Name or ID
    PtDebugPrint(f"Eureka.SpotSurAvatar(Avatar={Avatar}, NoSpot={NoSpot}, On={On})")
    InfoAvatar = Get_Nom_ID_SceneObject_Avatar(Avatar)
    AvatarName = InfoAvatar[0]
    AvatarName = Spot_SurAvatar(InfoAvatar, NoSpot)
    AvatarName.SpotSurAvatar(On)

class Spot_SurAvatar(): 
    def __init__(self, InfoAvatar=[], NoSpot=0):
        self.masterKeySpot1 = PtFindSceneobject("RTGlowLight", "CustomAvatars").getKey()  # spot Mir = Yeesha Glow Light
        self.ListCloneKeysSpot1 = []
        self.ListSceneObjectSpot1 = []
        self.NbrClone = 2
        
        self.Demandeur = InfoAvatar[0]  # AvatarName
        self.SceneObjectJoueurDest = None
        self._InfoAvatar = InfoAvatar
        self._NoSpot = NoSpot
        self._On = 0
        self.NvCentreObj = ptMatrix44()
        PtDebugPrint(f"Eureka.Spot_SurAvatar().__init__: self.masterKeySpot1 = {self.masterKeySpot1}")
        PtDebugPrint(f"Eureka.Spot_SurAvatar().__init__: self.ListCloneKeysSpot1 = {self.ListCloneKeysSpot1}")
        PtDebugPrint(f"Eureka.Spot_SurAvatar().__init__: self.ListSceneObjectSpot1 = {self.ListSceneObjectSpot1}")
        PtDebugPrint(f"Eureka.Spot_SurAvatar().__init__: self.NbrClone = {self.NbrClone}")
        PtDebugPrint(f"Eureka.Spot_SurAvatar().__init__: self.Demandeur = {self.Demandeur}")
        PtDebugPrint(f"Eureka.Spot_SurAvatar().__init__: self.SceneObjectJoueurDest = {self.SceneObjectJoueurDest}")
        PtDebugPrint(f"Eureka.Spot_SurAvatar().__init__: self._InfoAvatar = {self._InfoAvatar}")
        PtDebugPrint(f"Eureka.Spot_SurAvatar().__init__: self._NoSpot = {self._NoSpot}")
        PtDebugPrint(f"Eureka.Spot_SurAvatar().__init__: self._On = {self._On}")
        PtDebugPrint(f"Eureka.Spot_SurAvatar().__init__: self.NvCentreObj = {self.NvCentreObj}")

    def SpotSurAvatar(self, On=0):
        self._On = On
        self.SceneObjectJoueurDest = self._InfoAvatar[2]
        PtDebugPrint(f"Eureka.Spot_SurAvatar().SpotSurAvatar: self._On = {self._On}")
        PtDebugPrint(f"Eureka.Spot_SurAvatar().SpotSurAvatar: self.SceneObjectJoueurDest = {self.SceneObjectJoueurDest}")
        PtSetAlarm(0.5, self, 1)
            
    def onAlarm(self, param):
        PtDebugPrint(f"Eureka.Spot_SurAvatar().onAlarm: param = {param}")
        if param == 2:
            PtDebugPrint(f"Eureka.Spot_SurAvatar().onAlarm: param => 2")
            self.ListCloneKeysSpot1 = GestionClones.GetClones(self.Demandeur,self.masterKeySpot1, self.NbrClone)
            if len(self.ListCloneKeysSpot1) == self.NbrClone:
                PtSetAlarm(1, self, 3)
            else:
                PtSetAlarm(1, self, 2)
                
        if param == 1:
            PtDebugPrint(f"Eureka.Spot_SurAvatar().onAlarm: param => 1")
            self.ListCloneKeysSpot1 = GestionClones.GetClones(self.Demandeur,self.masterKeySpot1, self.NbrClone)
            if len(self.ListCloneKeysSpot1) != self.NbrClone:
                try:
                    GestionClones.DemandeClone(self.Demandeur, self.masterKeySpot1, self.NbrClone)
                except:
                    PtSendKIMessage(26, "SpotSurAvatar erreur chargement clone.")
                PtSetAlarm(1, self, 2)
            else:
                PtSetAlarm(1, self, 3)

        if param == 3: # ***********************************************************************************     
            PtDebugPrint(f"Eureka.Spot_SurAvatar().onAlarm: param => 3")
            try:
                self.ListSceneObjectSpot1 = []
                for cloneKey in self.ListCloneKeysSpot1:
                   self.ListSceneObjectSpot1.append(cloneKey.getSceneObject())
            except:
                PtSendKIMessage(26, "Erreur SpotSurAvatar param == 3.")
                
            if self._On:
                phy = 1
                self.NvCentreObj = self.SceneObjectJoueurDest.getLocalToWorld()
                self.NvCentreObj.translate(ptVector3(0.0, 0.0, 7.0))
                CdPerso.PlaceSceneobjectNvCRS(self.ListSceneObjectSpot1[0], self.NvCentreObj, phy=1, )
#                CdPerso.PlaceSceneobjectNvCRS(self.ListSceneObjectSpot1[1], self.NvCentreObj, phy=1, )
            else :
                self.NvCentreObj.translate(ptVector3(0.0, 0.0, 5000.0))
                CdPerso.PlaceSceneobjectNvCRS(self.ListSceneObjectSpot1[0], self.NvCentreObj, phy=1, )
#                CdPerso.PlaceSceneobjectNvCRS(self.ListSceneObjectSpot1[1], self.NvCentreObj, phy=1, )
                
            PtSendKIMessage(26, "SpotSurAvatar OK.")

# Juste pour info lorsque l'on charge le module
PtSendKIMessage(26, "Reload Eureka OK")















      
