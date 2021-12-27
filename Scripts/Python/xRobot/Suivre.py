# -*- coding: cp1252 -*-
"""Scripts pour lier un avatar a un objet (exemple ici avec un Bahro de la ville)
Michel Lacoste
-----Avril 2013------"""
from Plasma import *
import math

#1. les scripts et classes nécessaires
def PtpJoueur(nomOuIdJoueur):
    """Retourne le Ptplayer du joueur LOCAL a partir de son nom ou son numero d'ID de KI """
    Liste = PtGetPlayerList()
    Liste.append(PtGetLocalPlayer())
    nomOuIdJoueur = str(nomOuIdJoueur)
    nomOuIdJoueur = nomOuIdJoueur.lower().replace(' ', '')
    for joueur in Liste:
        if ((joueur.getPlayerName().lower().replace(' ', '') == nomOuIdJoueur) or (str(joueur.getPlayerID()) == nomOuIdJoueur)):
            return joueur
            break
    return None

# "B02_BoneSpine3:%s:duree:90:0:90:0"%(nplayer)
def Suivre(parametres="sandscrit:moi:20:0:0:0:0"):
    """Attacher un avatar sur un objet en mouvement et le suivre durant xx secondes
    puis atterrir au point par defaut. Charger la prp contenant l'animal avant !"""    
    params=parametres.split(':')
    objet = params[0]
    nomOuIdAvatar = params[1]
    duree = int(params[2])
    print "'{}', '{}', {}".format(objet, nomOuIdAvatar, duree)
    print "nombre de parametres:%d" %(len(params))
    if (len (params) == 7):
        rotx = int(params[3])
        roty = int(params[4])
        rotz = int(params[5])
        z = int(params[6])
    else:
        rotx = 0
        roty = 0
        rotz = 0
        z = 0
    defobjet = ("%s,,%s,%d,%d,%d,%d" %(PtGetAgeName(),objet,rotx,roty,rotz,z))
    animal = defobjet.split(',')
    Age = animal[0]
    Prp = animal[1]
    Objet = animal[2]
    Anglex = float(animal[3])
    Angley = float(animal[4])
    Anglez = float(animal[5])
    hauteur = float(animal[6])
    if nomOuIdAvatar == 'moi':
        Joueur = PtGetLocalAvatar()
    else:
        try:
            idplayer = PtpJoueur(nomOuIdAvatar).getPlayerID()
            Joueur= PtGetAvatarKeyFromClientID(idplayer).getSceneObject()
        except AttributeError:
            Joueur =  None 
    if Joueur != None:
        Joueur.netForce(1)
        Joueur.physics.netForce(1)
        Joueur.physics.disable()
        PtSetAlarm(1, Lier(Age,Joueur,Objet,duree,Anglex,Angley,Anglez,hauteur), 1)
    
#
class Lier:
    def __init__(self,age,joueur,obj,duree,anglex,angley,anglez,hauteur):
        self._age = age
        self._joueur = joueur
        self._obj = obj
        self._duree = duree
        self._anglex = anglex
        self._angley = angley
        self._anglez = anglez
        self._hauteur = hauteur
    def onAlarm (self, param):
        print "Lier"
        try:
            Aobj = PtFindSceneobject(self._obj, self._age)
        except:
            PtSendKIMessage(26,"ManipAges class Lier :%s introuvable" %(self._obj))
            return
        Aobj.netForce(1)
        Aobj.draw.enable(1)
        centreobj = Aobj.getLocalToWorld()
        rotx = ptMatrix44()
        rotx.makeRotateMat(0, -math.pi * self._anglex/180.0)
        roty = ptMatrix44()
        roty.makeRotateMat(1, -math.pi * self._angley/180.0)
        rotz = ptMatrix44()
        rotz.makeRotateMat(2, -math.pi * self._anglez/180.0)
        hz = ptMatrix44()
        hz.translate(ptVector3(0,0,self._hauteur))
        self._joueur.physics.warp(centreobj * rotx * roty * rotz * hz)
        PtAttachObject(self._joueur, Aobj,1)
        print "duree:{}".format(self._duree)
        if self._duree > 0:
            PtSetAlarm(self._duree, Delier(self._age, self._joueur, Aobj), 1)
        
#
class Delier:
    def __init__(self,age,joueur,obj):
        self._age = age
        self._joueur = joueur
        self._obj = obj
    def onAlarm (self, param):
        print "Delier"
        PtDetachObject(self._joueur,self._obj,1)
        try:
            Robj=PtFindSceneobject('LinkInPointDefault',PtGetAgeName())
            centreobj = Robj.getLocalToWorld()
            self._joueur.physics.warp(centreobj)
            self._joueur.physics.enable(1)
        except NameError:
            return

#
class ChangeSDL: # pour modifier une sdl
    def __init__(self,SDL,val):
        self._SDL = SDL
        self._val = val
    def onAlarm(self,param):
        sdl=PtGetAgeSDL()
        sdl[self._SDL]=(self._val,)

#
class suivreobj:
    def __init__(self,commande):
        self._commande = commande
    def onAlarm(self,param):
        Suivre(self._commande)
        
        
#2. fonction princiopale qui lie un avatar a un objet (ici le bahro 1 de la ville) durant 30 secondes
# si la duree de vol est egale a 0, alors l'avatar restera indéfiniment lie a l'animal. Il faut alors le delier manuellement.
# voir en dessous la liste des autres objets auxquels on peut relier un avatar
# il est a noter que pour les bahros de la ville il faut d'abord changer certaines sdl, pour les autres animaux non
# regarde la liste en bas.
"""
def VolersurBahro1(nplayer ="Annabelle", idplayer = 12345, duree = 30):
    tp = 0
    PtSetAlarm(tp,ChangeSDL("islmS1FinaleBahro",1),1)
    PtSetAlarm(tp,ChangeSDL("islmS1FinaleBahroCity2",1),1)
    tp += 1
    PtSetAlarm(tp,suivreobj("B02_BoneSpine3:%s:duree:90:0:90:0"%(nplayer)),idplayer)
"""
# le parametre idplayer ne sert a rien!

#
def VolersurBahro2(nplayer="moi", duree = 30):
    tp = 0
    PtSetAlarm(tp,ChangeSDL("islmS1FinaleBahro",1),1)
    PtSetAlarm(tp,ChangeSDL("islmS1FinaleBahroCity2",1),1)
    tp += 1
    PtSetAlarm(tp,suivreobj("B02_BoneSpine3:{}:{}:90:0:90:0".format(nplayer, duree)),1)


#
# Urwin de Negilhan: ("Negilahn,Jungle,Urwin_Head,0,-90,180,0")
def urwin(nplayer="moi", duree = 30):
    tp = 0
    PtSetAlarm(tp,suivreobj("B02_BoneSpine3:{}:{}:90:0:90:0".format(nplayer, duree)),1)

# Singe de Negilhan:("Negilahn,Jungle,2Tails_Root,0,0,60,0")
def singe(nplayer="moi", duree = 30):
    tp = 0
    PtSetAlarm(tp,suivreobj("B02_BoneSpine3:{}:{}:90:0:90:0".format(nplayer, duree)),1)

# Raie 1 de Dereno:("Dereno,DrnoExterior,C01_Body,0,0,0,0")
# Raie 2 de Dereno:("Dereno,DrnoExterior,C02_Body,0,0,0,0")
# Poisson de Dereno :("Dereno,DrnoExterior,FishC06,0,0,90,0")
    
######### C'est tout ! lol

### Voici quelques animaux auxqules on peut se lier, avec les angles pour que l'avatar soit bien aligné quand i est dessus
# oiseau 1 du Relto:("Personal,psnlMYSTII,DCSoarBird01,0,0,180,0")

# oiseau 2 du Relto: ("Personal,psnlMYSTII,DCSoarBird03,0,0,180,0")
# Papillon du Relto: ("Personal,psnlMYSTII,ButterflyVertPos11,0,0,0,0")
# Lucioles du Relto: ("Personal,psnlMYSTII,BugFlockingEmitTest,0,0,0,0")
# Lucioles de Negilahn:("Negilahn,Jungle,BugFlockingEmitTest,0,0,0,0")
# Pierres tournates du Relto:("Personal,psnlMYSTII,WedgeRingsMaster05,0,0,0,0")        
# oiseau 1 de Cleft:("Cleft,Desert,DCSoarBird01,0,0,180,0")
# oiseau 2 de Cleft:("Cleft,Desert,DCSoarBird03,0,0,180,0")
# oiseau 1 de Teledahn :("Teledahn,tldnHarvest,BBHead,0,0,-90,0")
# oiseau 2 de Teledahn:("Teledahn,tldnHarvest,BBHead01,0,0,-90,0")
# Shooter 1 de Teledahn :("Teledahn,tldnHarvest,ShooterB-Master,0,0,0,0")
# Shooter 2 de Teledahn : ("Teledahn,tldnHarvest,ShooterC-Master,0,0,90,0")
# Shooter 3 de Teledahn:("Teledahn,tldnHarvest,ShooterD-Master,0,0,0,0")
# Shooter 4 de Teledahn:("Teledahn,tldnHarvest,ShooterF-Master,0,0,0,0")
# Shooter 5 de Teledahn :("Teledahn,tldnHarvest,ShooterH-Master,0,0,0,0")
# Raie 1 de Dereno:("Dereno,DrnoExterior,C01_Body,0,0,0,0")
# Raie 2 de Dereno:("Dereno,DrnoExterior,C02_Body,0,0,0,0")
# Poisson de Dereno :("Dereno,DrnoExterior,FishC06,0,0,90,0")
# Poisson 1 de Kemo :("Garden,kemoGarden,FishA,0,0,90,0")
# Poisson 2 de Kemo :("Garden,kemoGarden,FishB,0,0,90,0")
# Poisson 3 de Kemo :("Garden,kemoGarden,FishC,0,0,90,0")
# Bahro de l'Arche de la Ville:("city,bahroFlyers_arch,B_ArchBody_28,0,0,0,0")
# Bahro1 de la Ville :
    #sdl=PtGetAgeSDL()  
    #defobjet = ("city,bahroFlyers_city1,B01_BoneSpine3,90,0,90,0")        
    #sdl["islmS1FinaleBahro"]=(1,)
    #sdl['islmS1FinaleBahroCity1']=(1,)
# Bahro2 de la Ville :
    #sdl=PtGetAgeSDL()  
    #defobjet = ("city,bahroFlyers_city2,B02_BoneSpine3,90,0,90,0")        
    #sdl["islmS1FinaleBahro"]=(1,)
    #sdl['islmS1FinaleBahroCity2']=(1,)
# Bahro3 de la Ville :
    #sdl=PtGetAgeSDL()  
    #defobjet = ("city,bahroFlyers_city3,B03_BoneSpine3,90,0,90,0")        
    #sdl["islmS1FinaleBahro"]=(1,)
    #sdl['islmS1FinaleBahroCity3']=(1,)
# Bahro4 de la Ville :
    #sdl=PtGetAgeSDL()  
    #defobjet = ("city,bahroFlyers_city4,B04_BoneSpine3,90,0,90,0")        
    #sdl["islmS1FinaleBahro"]=(1,)
    #sdl['islmS1FinaleBahroCity4']=(1,)
# Bahro5 de la Ville: 
    #sdl=PtGetAgeSDL()  
    #defobjet = ("city,bahroFlyers_city5,B05_BoneSpine3,90,0,90,0")        
    #sdl["islmS1FinaleBahro"]=(1,)
    #sdl['islmS1FinaleBahroCity5']=(1,)
# Bahro6 de la Ville: 
    #sdl=PtGetAgeSDL()  
    #defobjet = ("city,bahroFlyers_city6,B06_BoneSpine3,90,0,90,0")        
    #sdl["islmS1FinaleBahro"]=(1,)
    #sdl['islmS1FinaleBahroCity6']=(1,)        
# Urwin de Negilhan: ("Negilahn,Jungle,Urwin_Head,0,-90,180,0")
# Singe de Negilhan:("Negilahn,Jungle,2Tails_Root,0,0,60,0")
# Sandscrit de Payiferen :("Payiferen,Pod,BoneSSHead,0,-90,180,0")        
# Shroomie de Teledahn:("Teledahn,tldnHarvest,Sniff_SB_Spine01,0,0,0,0")
# Oiseau 1 Eder Gira : ("Gira,giraCanyon,Bird01,0,0,180,0")
# Oiseau 2 Eder Gira: ("Gira,giraCanyon,Bird02,0,0,180,0")
# Poisson 1 Eder Gira :("Gira,giraCanyon,Fish01Master,0,0,180,0")
# Poisson 2 Eder Gira :("Gira,giraCanyon,Fish02Master,0,0,180,0")
# Poisson 3 Eder Gira: ("Gira,giraCanyon,Fish03Master,0,0,180,0")
# Poisson 4 Eder Gira :("Gira,giraCanyon,Fish04Master,0,0,180,0")
