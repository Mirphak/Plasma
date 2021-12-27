# -*- coding: cp1252 -*-

"""Scripts pour animation d'objets animables Uru Live
Michel Lacoste
-----Aout 2012------"""

from Plasma import *
import math


def SCOJoueur(nom):
    """Retourne un SCO joueur a partir de son nom ou son numero d'ID de KI """
    Liste = PtGetPlayerList()
    nom = nom.lower().replace(' ', '')
    if nom == 'moi':
        return PtGetLocalPlayer()
    result = None
    for joueur in Liste:
        if ((joueur.getPlayerName().lower().replace(' ', '') == nom) or (str(joueur.getPlayerID()) == nom)):
            return joueur
            break

def SCOListAvatars ():    
    """Retourne la liste des avatars presents dans l'age courant sous forme de SceneObjects"""
    Listejoueurs = PtGetPlayerList()
    Liste = map(lambda player: PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject(), Listejoueurs)
    Liste.append(PtGetLocalAvatar())
    return Liste
    
def SCOAvatar(nom):
    """Retourne le SceneObject d'un avatar d'apres son nom ou son ID"""
    nom = nom.lower()
    if (nom == 'moi'):
        return PtGetLocalAvatar()
    else:
        return PtGetAvatarKeyFromClientID(SCOJoueur(nom).getPlayerID()).getSceneObject()

#*****************************#
#                             #
#Suivre objets en mouvements  #
#                             #
#*****************************#
def Suivre(objet='sandscrit',Avatar='moi',duree=300): #la duree est en secondes
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
    if (objet.lower()) == 'oiseaur1' :
    # oiseau 1 du Relto    
        defobjet = ("Personal,psnlMYSTII,DCSoarBird01,0,0,180")
    elif (objet.lower()) == 'oiseaur2' :
    # oiseau 2 du Relto    
        defobjet = ("Personal,psnlMYSTII,DCSoarBird03,0,0,180")
    elif (objet.lower()) == 'papillonr' :
    # Papillon du Relto  
        defobjet = ("Personal,psnlMYSTII,ButterflyVertPos11,0,0,0")
    elif (objet.lower()) == 'luciolesr' :
    # Lucioles du Relto  
        defobjet = ("Personal,psnlMYSTII,BugFlockingEmitTest,0,0,0")        
    elif (objet.lower()) == 'oiseauc1' :
    # oiseau 1 de Cleft    
        defobjet = ("Cleft,Desert,DCSoarBird01,0,0,180")
    elif (objet.lower()) == 'oiseauc2' :
    # oiseau 2 de Cleft    
        defobjet = ("Cleft,Desert,DCSoarBird03,0,0,180")
    elif (objet.lower()) == 'oiseaut1' :
    # oiseau 1 de Teledahn    
        defobjet = ("Teledahn,tldnHarvest,BBHead,0,0,-90")
    elif (objet.lower()) == 'oiseaut2' :
    # oiseau 2 de Teledahn    
        defobjet = ("Teledahn,tldnHarvest,BBHead01,0,0,-90")
    elif (objet.lower()) == 'shooter1' :
    # Shooter 1 de Teledahn    
        defobjet = ("Teledahn,tldnHarvest,ShooterB-Master,0,0,0")
    elif (objet.lower()) == 'shooter2' :
    # Shooter 2 de Teledahn    
        defobjet = ("Teledahn,tldnHarvest,ShooterC-Master,0,0,90")
    elif (objet.lower()) == 'shooter3' :
    # Shooter 3 de Teledahn     
        defobjet = ("Teledahn,tldnHarvest,ShooterD-Master,0,0,0")
    elif (objet.lower()) == 'shooter4' :
    # Shooter 4 de Teledahn    
        defobjet = ("Teledahn,tldnHarvest,ShooterF-Master,0,0,0")
    elif (objet.lower()) == 'shooter5' :
    # Shooter 5 de Teledahn    
        defobjet = ("Teledahn,tldnHarvest,ShooterH-Master,0,0,0")
    elif (objet.lower()) == 'raie1' :
    # Raie 1 de Dereno
        defobjet = ("Dereno,DrnoExterior,C01_Body,0,0,0")
    elif (objet.lower()) == 'raie2' :
    # Raie 2 de Dereno
        defobjet = ("Dereno,DrnoExterior,C02_Body,0,0,0")
    elif (objet.lower()) == 'poissond' :
    # Poisson de Dereno  
        defobjet = ("Dereno,DrnoExterior,FishC06,0,0,90")
    elif (objet.lower()) == 'poissong1' :
    # Poisson 1 de Kemo  
        defobjet = ("Garden,kemoGarden,FishA,0,0,90")
    elif (objet.lower()) == 'poissong2' :
    # Poisson 2 de Kemo  
        defobjet = ("Garden,kemoGarden,FishB,0,0,90")
    elif (objet.lower()) == 'poissong3' :
    # Poisson 3 de Kemo  
        defobjet = ("Garden,kemoGarden,FishC,0,0,90")
    elif (objet.lower()) == 'bahro' :
    # Bahro de l'Arche de la Ville    
        defobjet = ("city,bahroFlyers_arch,B_ArchBody_01,0,0,0")
    elif (objet.lower()) == 'urwin' :
    # Urwin de Negilhan    
        defobjet = ("Negilahn,Jungle,Urwin_Head,0,-90,180")
    elif (objet.lower()) == 'singe' :
    # Singe de Negilhan    
        defobjet = ("Negilahn,Jungle,2Tails_Root,0,0,60")
    elif (objet.lower()) == 'sandscrit' :
    # Sandscrit de Payiferen    
        defobjet = ("Payiferen,Pod,BoneSSHead,0,-90,180")        
    elif (objet.lower()) == 'shroomie' :
    # Shroomie de Teledahn    
        defobjet = ("Teledahn,tldnHarvest,Sniff_SB_Spine01,0,0,0")
    else:
            print "{} inconnu".format(objet)
            return
    animal = defobjet.split(',')
    Age = animal[0]
    Prp = animal[1]
    Objet = animal[2]
    Anglex = float(animal[3])
    Angley = float(animal[4])
    Anglez = float(animal[5])
    PtConsoleNet('Nav.PageInNode '+ Prp ,1)
    if Avatar == 'moi':
        Joueur = PtGetLocalAvatar()
    else:
        Joueur = SCOAvatar(Avatar)
    Joueur.netForce(1)
    Joueur.physics.netForce(1)
    Joueur.physics.disable()
    PtSetAlarm(1, Lier(Age,Joueur,Objet,duree,Anglex,Angley,Anglez), 1)
    
class Lier:
    def __init__(self,age,joueur,obj,duree,anglex,angley,anglez):
        self._age = age
        self._joueur = joueur
        self._obj = obj
        self._duree = duree
        self._anglex = anglex
        self._angley = angley
        self._anglez = anglez
    def onAlarm (self, param):
        Aobj = PtFindSceneobject(self._obj, self._age)
        Aobj.netForce(1)
        Aobj.draw.enable(1)
        centreobj = Aobj.getLocalToWorld()
        rotx = ptMatrix44()
        rotx.makeRotateMat(0, -math.pi * self._anglex/180)
        roty = ptMatrix44()
        roty.makeRotateMat(1, -math.pi * self._angley/180)
        rotz = ptMatrix44()
        rotz.makeRotateMat(2, -math.pi * self._anglez/180)
        self._joueur.physics.warp(centreobj * rotx * roty * rotz)
        PtAttachObject(self._joueur, Aobj,1)
        PtSetAlarm(self._duree, Delier(self._age, self._joueur, Aobj), 1)
        
class Delier:
    def __init__(self,age,joueur,obj):
        self._age = age
        self._joueur = joueur
        self._obj = obj
    def onAlarm (self, param):
        PtDetachObject(self._joueur,self._obj,1)
        Robj=PtFindSceneobject('LinkInPointDefault',PtGetAgeName())
        centreobj = Robj.getLocalToWorld()
        self._joueur.physics.warp(centreobj)
        self._joueur.physics.enable(1)
#*****************************#
#   Animer un objet animable  #
#                             #
#*****************************# 
import sys
    
        
#Cette fonction ne s'utilise pas seule, elle est appelée par Action()
def runResp(key, resp, stateidx = None, netForce = 1, netPropagate = 1, fastforward = 0):
    nt = ptNotify(key)
    nt.addReceiver(resp)
    nt.netPropagate(netPropagate)
    nt.netForce(netForce)
    if stateidx != None:
        nt.addResponderState(stateidx)
    if fastforward:
        nt.setType(PtNotificationType.kResponderFF)
        nt.netPropagate(0)
        nt.netForce(0)
    nt.setActivate(1.0)
    nt.send()

def Action (animal='singe',action='grimper'):
    #Cette fonction permet d'animer les objets animables
	#Utiliser d'abord la fonction Suivre() ci dessus
    surmoi = PtGetLocalAvatar().getLocalToWorld()
    if (animal.lower()) == 'singe':
        obj = PtFindSceneobject('TempMonkeyHandle','Negilahn')
        responders = obj.getResponders()
        if (action.lower()) == 'alarme':
            runResp(obj.getKey(), responders[3], 0)
        elif (action.lower()) == 'grimpe':
            runResp(obj.getKey(), responders[3], 1)        
        elif (action.lower()) == 'mange':
            runResp(obj.getKey(), responders[3], 2)
        elif (action.lower()) == 'attend':
            runResp(obj.getKey(), responders[3], 3)
        elif (action.lower()) == 'crie':
            runResp(obj.getKey(), responders[1], 5)
            runResp(obj.getKey(), responders[3], 4)
        elif (action.lower()) == 'saute':
            runResp(obj.getKey(), responders[1], 0)
            runResp(obj.getKey(), responders[0], 0)    
        elif (action.lower()) == 'arbre1':
            runResp(obj.getKey(), responders[1], 0)
            runResp(obj.getKey(), responders[2], 0)     
        elif (action.lower()) == 'arbre2':
            runResp(obj.getKey(), responders[1], 0)
            runResp(obj.getKey(), responders[2], 1)
        elif (action.lower()) == 'arbre3':
            runResp(obj.getKey(), responders[1], 0)
            runResp(obj.getKey(), responders[2], 2)
        elif (action.lower()) == 'sur moi':
            obj.physics.warp(surmoi)            
        else :
            PtSendKIMessage(45,"L'action %s n'existe pas !" % action)
    elif (animal.lower()) == 'urwin':
        obj = PtFindSceneobject('Dummy04','Negilahn')
        responders = obj.getResponders()
        if (action.lower()) == 'start':
            runResp(obj.getKey(), responders[1], 5) #cri
            runResp(obj.getKey(), responders[6], 0) #mouvement de tete
            runResp(obj.getKey(), responders[5], 0) #marche
            anim = sys.modules['Dummy04cPythUrwinBird'].UrwinMasterAnim.animation
            anim.resume()
        elif (action.lower()) == 'stop':
            runResp(obj.getKey(), responders[1], 5) #cri
            runResp(obj.getKey(), responders[6], 0) #mouvement de tete
            anim = sys.modules['Dummy04cPythUrwinBird'].UrwinMasterAnim.animation
            anim.stop()
        elif (action.lower()) == 'sur moi':
            obj.physics.warp(surmoi)            
        else :
            PtSendKIMessage(45,"L'action %s n'existe pas !" % action)        
    elif (animal.lower()) == 'sandscrit':
        obj = PtFindSceneobject('Sandscrit_Mover','Payiferen')
        responders = obj.getResponders()
        if (action.lower()) == 'start':
            runResp(obj.getKey(), responders[6], 0) #mouvement de tete
            runResp(obj.getKey(), responders[5], 0) #marche
            anim = sys.modules['SandscritMovercPyUrwin'].UrwinMasterAnim.animation
            anim.resume()
        elif (action.lower()) == 'stop':
            runResp(obj.getKey(), responders[6], 0) #mouvement de tete
            anim = sys.modules['SandscritMovercPyUrwin'].UrwinMasterAnim.animation
            anim.stop()
        elif (action.lower()) == 'sur moi':
            obj.physics.warp(surmoi)    
        else :
            PtSendKIMessage(45,"L'action %s n'existe pas !" % action)              
    elif (animal.lower()) == 'shroomie':
        shro1 = PtFindSceneobject('MasterShroomie','Teledahn')
        shro2 = PtFindSceneobject('LakeShoomieHandle','Teledahn')
        spwn1 = PtFindSceneobject('SpawnPtNear01','Teledahn').getLocalToWorld()
        spwn2 = PtFindSceneobject('SpawnPtNear02','Teledahn').getLocalToWorld()
        spwn3 = PtFindSceneobject('SpawnPtNear03','Teledahn').getLocalToWorld()
        spwn4 = PtFindSceneobject('SpawnPtNear04','Teledahn').getLocalToWorld()
        spwn5 = PtFindSceneobject('SpawnPtNear05','Teledahn').getLocalToWorld()
        if (action.lower()) == 'visible':
            responders = shro1.getResponders()
            runResp(shro1.getKey(), responders[1], 0)
        elif (action.lower()) == 'cache':
            responders = shro1.getResponders()
            runResp(shro1.getKey(), responders[0], 0)        
        elif (action.lower()) == 'plonge':
            responders = shro2.getResponders()
            runResp(shro2.getKey(), responders[0], 0)
        elif (action.lower()) == 'surface':
            responders = shro2.getResponders()
            runResp(shro2.getKey(), responders[1], 0)
        elif (action.lower()) == 'avance':
            responders = shro2.getResponders()
            runResp(shro2.getKey(), responders[2], 0)
        elif (action.lower()) == 'tourne':
            responders = shro2.getResponders()
            runResp(shro2.getKey(), responders[3], 0)
        elif (action.lower()) == 'gauche':
            shro2.physics.warp(spwn1)
        elif (action.lower()) == 'centre':
            shro2.physics.warp(spwn2)
        elif (action.lower()) == 'droite':
            shro2.physics.warp(spwn3)
        elif (action.lower()) == 'sortie':
            shro2.physics.warp(spwn4)
        elif (action.lower()) == 'entree':
            shro2.physics.warp(spwn5)
        elif (action.lower()) == 'sur moi':
            shro2.physics.warp(surmoi)    
        else :
            PtSendKIMessage(45,"L'action %s n'existe pas !" % action)
    else :
        PtSendKIMessage(45,"%s n'existe pas !" % animal)
