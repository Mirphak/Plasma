# -*- coding: utf-8 -*-

from Plasma import *
import math

def SCOJoueur(nom):
    """Retourne un SCO joueur a partir de son nom ou son numero d'ID de KI """
    Liste = PtGetPlayerList()
    Liste.append(PtGetLocalPlayer())
    nom = nom.lower().replace(' ', '')
    if nom == 'moi':
        return PtGetLocalPlayer()
    result = None
    for joueur in Liste:
        if ((joueur.getPlayerName().lower().replace(' ', '') == nom) or (str(joueur.getPlayerID()) == nom)):
            return joueur
            break

def SCOListAvatars():    
    """Retourne la liste des avatars presents dans l'age courant sous forme de SceneObjects"""
    Listejoueurs = PtGetPlayerList()
    Liste = [PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject() for player in Listejoueurs]
    Liste.append(PtGetLocalAvatar())
    return Liste
    
def SCOAvatar(nom):
    """Retourne le SceneObject d'un avatar d'apres son nom ou son ID"""
    nom = nom.lower()
    if (nom == 'moi'):
        return PtGetLocalAvatar()
    else:
        return PtGetAvatarKeyFromClientID(SCOJoueur(nom).getPlayerID()).getSceneObject()

def Suivre(objet='b3', avatar='moi', duree=60): #la duree est en secondes
    """Attacher un avatar sur un objet en mouvement dont la taille est xxx %
    et le suivre durant xx secondes puis atterrir au point par defaut"""
    if isinstance(duree, int):
        duree = duree * 1.0
    elif isinstance(duree, float):
        pass
    else:
        try:
            duree = float(duree)
        except:
            duree = 60.0
    if (objet.lower()) == 'b3' :
    # Bahro3 de la Ville :
        sdl=PtGetAgeSDL()
        defobjet = ("city,bahroFlyers_city3,B03_BoneSpine3,90,0,90,0.0,1.2,-6.0")
        sdl["islmS1FinaleBahro"] = (1,)
        sdl['islmS1FinaleBahroCity3'] = (1,)
    else:
            print("{} inconnu".format(objet))
            return
    animal = defobjet.split(',')
    Age = animal[0]
    Prp = animal[1]
    Objet = animal[2]
    rx = float(animal[3])
    ry = float(animal[4])
    rz = float(animal[5])
    dx = float(animal[6])
    dy = float(animal[7])
    dz = float(animal[8])
    PtConsoleNet('Nav.PageInNode ' + Prp, 1)
    if avatar == 'moi':
        Joueur = PtGetLocalAvatar()
    else:
        Joueur = SCOAvatar(avatar)
    Joueur.netForce(True)
    Joueur.physics.netForce(True)
    Joueur.physics.disable()
    PtSetAlarm(1, Lier(Age, Joueur, Objet, duree, rx, ry, rz, dx, dy, dz), 1)
    
class Lier:
    def __init__(self, age, joueur, obj, duree, rx, ry, rz, dx, dy, dz):
        self._age = age
        self._joueur = joueur
        self._obj = obj
        self._duree = duree
        self._rx = rx
        self._ry = ry
        self._rz = rz
        self._dx = dx
        self._dy = dy
        self._dz = dz
        
    def onAlarm (self, param):
        if param == 1:
            self._Aobj = PtFindSceneobject(self._obj, self._age)
            self._Aobj.netForce(True)
            self._Aobj.draw.enable(True)
            centreobj = self._Aobj.getLocalToWorld()
            rotx = ptMatrix44()
            rotx.makeRotateMat(0, -math.pi * self._rx / 180)
            roty = ptMatrix44()
            roty.makeRotateMat(1, -math.pi * self._ry / 180)
            rotz = ptMatrix44()
            rotz.makeRotateMat(2, -math.pi * self._rz / 180)
            trans = ptMatrix44()
            trans.translate(ptVector3(self._dx, self._dy, self._dz))
            print("self._rx={}, self._ry={}, self._rz={}, self._dx={}, self._dy={}, self._dz={}".format(self._rx, self._ry, self._rz, self._dx, self._dy, self._dz))
            self._joueur.physics.warp(centreobj * rotx * roty * rotz * trans)

            PtAttachObject(self._joueur, self._Aobj, 1)
            print("Lier auto call onalarm 2")
            PtSetAlarm(3, self, 2)
        else:
            print("Lier onalarm 2, age = ", self._age)
            PtSetAlarm(self._duree, Delier(self._age, self._joueur, self._Aobj), 1)
        
class Delier:
    def __init__(self, age, joueur, obj):
        self._age = age
        self._joueur = joueur
        self._obj = obj
    def onAlarm (self, param):
        PtDetachObject(self._joueur, self._obj, 1)
        
        # Attention 'LinkInPointDefault' n'existe pas toujours
        rObj = None
        try:
            rObj = PtFindSceneobject('LinkInPointDefault', PtGetAgeName())
        except:
            # Recherche d'un autre point de liaison
            objectList = FindSOInAge(soName='LinkInPoint', ageFileName=PtGetAgeName())
            if len(objectList) > 0:
                rObj = objectList[0]
        if rObj is not None:
            centreObj = rObj.getLocalToWorld()
            self._joueur.physics.warp(centreObj)
        self._joueur.physics.enable(1)
        
        """
        # Je vais plutot ramener le joueur sur le robot
        rObj = PtGetLocalAvatar()
        centreObj = rObj.getLocalToWorld()
        # Faut-il s'assurer que le joueur est encore dans l'age ?
        try:
            self._joueur.physics.warp(centreObj)
            self._joueur.physics.enable(1)
        except:
            pass
        """


def Action (animal='b3', action='sur moi'):
    #Cette fonction permet d'animer les objets animables
	#Utiliser d'abord la fonction Suivre() ci dessus
    surmoi = PtGetLocalAvatar().getLocalToWorld()
    if (animal.lower()) == 'b3':
        obj = PtFindSceneobject('B03_BoneMover', 'city')
        #obj = PtFindSceneobject('B03_BoneSpine3', 'city')
        responders = obj.getResponders()
        if (action.lower()) == 'sur moi':
            obj.physics.warp(surmoi)            
        else :
            PtSendKIMessage(45,"L'action %s n'existe pas !" % action)
    else :
        PtSendKIMessage(45,"%s n'existe pas !" % animal)

