# -*- coding: cp1252 -*-

"""Scripts pour animation d'objets animables Uru Live
Michel Lacoste
-----Aout 2012------"""

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
    elif (objet.lower()) == 'bird1' :
    # Oiseau 1 Eder Gira
        defobjet = ("Gira,giraCanyon,Bird01,0,0,180")
    elif (objet.lower()) == 'bird2' :
    # Oiseau 2 Eder Gira
        defobjet = ("Gira,giraCanyon,Bird02,0,0,180")
    elif (objet.lower()) == 'fish1' :
    # Poisson 1 Eder Gira
        defobjet = ("Gira,giraCanyon,Fish01Master,0,0,180")
    elif (objet.lower()) == 'fish2' :
    # Poisson 2 Eder Gira
        defobjet = ("Gira,giraCanyon,Fish02Master,0,0,180")
    elif (objet.lower()) == 'fish3' :
    # Poisson 3 Eder Gira
        defobjet = ("Gira,giraCanyon,Fish03Master,0,0,180")
    elif (objet.lower()) == 'fish4' :
    # Poisson 4 Eder Gira
        defobjet = ("Gira,giraCanyon,Fish04Master,0,0,180")
    elif (objet.lower()) == 'bahro' :
    # Bahro de l'Arche de la Ville    
        #defobjet = ("city,bahroFlyers_arch,B_ArchBody_01,0,0,0")
        defobjet = ("city,bahroFlyers_arch,B_ArchBody_28,0,0,0")
    elif (objet.lower()) == 'b1' :
    # Bahro1 de la Ville :
        sdl=PtGetAgeSDL()
        defobjet = ("city,bahroFlyers_city1,B01_BoneSpine3,90,0,90")
        sdl["islmS1FinaleBahro"]=(1,)
        sdl['islmS1FinaleBahroCity1']=(1,)
    elif (objet.lower()) == 'b2' :
    # Bahro2 de la Ville :
        sdl=PtGetAgeSDL()
        defobjet = ("city,bahroFlyers_city2,B02_BoneSpine3,90,0,90")
        sdl["islmS1FinaleBahro"]=(1,)
        sdl['islmS1FinaleBahroCity2']=(1,)
    elif (objet.lower()) == 'b3' :
    # Bahro3 de la Ville :
        sdl=PtGetAgeSDL()
        defobjet = ("city,bahroFlyers_city3,B03_BoneSpine3,90,0,90")
        sdl["islmS1FinaleBahro"]=(1,)
        sdl['islmS1FinaleBahroCity3']=(1,)
    elif (objet.lower()) == 'b4' :
    # Bahro4 de la Ville :
        sdl=PtGetAgeSDL()
        defobjet = ("city,bahroFlyers_city4,B04_BoneSpine3,90,0,90")
        sdl["islmS1FinaleBahro"]=(1,)
        sdl['islmS1FinaleBahroCity4']=(1,)
    elif (objet.lower()) == 'b5' :
    # Bahro5 de la Ville :
        sdl=PtGetAgeSDL()
        defobjet = ("city,bahroFlyers_city5,B05_BoneSpine3,90,0,90")
        sdl["islmS1FinaleBahro"]=(1,)
        sdl['islmS1FinaleBahroCity5']=(1,)
    elif (objet.lower()) == 'b6' :
    # Bahro6 de la Ville :
        sdl=PtGetAgeSDL()
        defobjet = ("city,bahroFlyers_city6,B06_BoneSpine3,90,0,90")
        sdl["islmS1FinaleBahro"]=(1,)
        sdl['islmS1FinaleBahroCity6']=(1,)        
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
    
#
class Lier:
    # init
    def __init__(self, age, joueur, obj, duree, anglex, angley, anglez):
        self._age = age
        self._joueur = joueur
        self._obj = obj
        self._duree = duree
        self._anglex = anglex
        self._angley = angley
        self._anglez = anglez
    # on alarm
    def onAlarm (self, param):
        Aobj = PtFindSceneobject(self._obj, self._age)
        Aobj.netForce(1)
        Aobj.draw.enable(1)
        centreobj = Aobj.getLocalToWorld()
        rotx = ptMatrix44()
        rotx.makeRotateMat(0, -math.pi * self._anglex / 180)
        roty = ptMatrix44()
        roty.makeRotateMat(1, -math.pi * self._angley / 180)
        rotz = ptMatrix44()
        rotz.makeRotateMat(2, -math.pi * self._anglez / 180)
        self._joueur.physics.warp(centreobj * rotx * roty * rotz)
        PtAttachObject(self._joueur, Aobj,1)
        PtSetAlarm(self._duree, Delier(self._age, self._joueur, Aobj), 1)
        
class Delier:
    def __init__(self, age, joueur, obj):
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

#

"""
"key":     # comment 
    [["alias", ...], ["age", "page", "objet", rx, ry, rz]], 
"""

animals = {
    "oiseaur1":     # oiseau 1 du Relto				
        [["oiseaur1"  , "birdr1", ], ["Personal", "psnlMYSTII", "DCSoarBird01", 0, 0, 180]], 
    "oiseaur2":     # oiseau 2 du Relto				
        [["oiseaur2"  , "birdr2", ], ["Personal", "psnlMYSTII", "DCSoarBird03", 0, 0, 180]], 
    "papillonr":    # Papillon du Relto				
        [["papillonr" , "butterfly", ], ["Personal", "psnlMYSTII", "ButterflyVertPos11", 0, 0, 0]], 
    "luciolesr":    # Lucioles du Relto				
        [["luciolesr" , "firefly", ], ["Personal", "psnlMYSTII", "BugFlockingEmitTest", 0, 0, 0]], 
    "oiseauc1":     # oiseau 1 de Cleft				
        [["oiseauc1"  , "birdc1", ], ["Cleft", "Desert", "DCSoarBird01", 0, 0, 180]], 
    "oiseauc2":     # oiseau 2 de Cleft				
        [["oiseauc2"  , "birdc2", ], ["Cleft", "Desert", "DCSoarBird03", 0, 0, 180]], 
    "oiseaut1":     # oiseau 1 de Teledahn			
        [["oiseaut1"  , "birdt1", ], ["Teledahn", "tldnHarvest", "BBHead", 0, 0, -90]], 
    "oiseaut2":     # oiseau 2 de Teledahn			
        [["oiseaut2"  , "birdt2", ], ["Teledahn", "tldnHarvest", "BBHead01", 0, 0, -90]], 
    "shooter1":     # Shooter 1 de Teledahn			
        [["shooter1"  , "s1", ], ["Teledahn", "tldnHarvest", "ShooterB-Master", 0, 0, 0]], 
    "shooter2":     # Shooter 2 de Teledahn			
        [["shooter2"  , "s2", ], ["Teledahn", "tldnHarvest", "ShooterC-Master", 0, 0, 90]], 
    "shooter3":     # Shooter 3 de Teledahn			
        [["shooter3"  , "s3", ], ["Teledahn", "tldnHarvest", "ShooterD-Master", 0, 0, 0]], 
    "shooter4":     # Shooter 4 de Teledahn			
        [["shooter4"  , "s4", ], ["Teledahn", "tldnHarvest", "ShooterF-Master", 0, 0, 0]], 
    "shooter5":     # Shooter 5 de Teledahn			
        [["shooter5"  , "s5", ], ["Teledahn", "tldnHarvest", "ShooterH-Master", 0, 0, 0]], 
    "raie1":        # Raie 1 de Dereno				
        [["raie1"     , "ray1", ], ["Dereno", "DrnoExterior", "C01_Body", 0, 0, 0]], 
    "raie2":        # Raie 2 de Dereno				
        [["raie2"     , "ray2", ], ["Dereno", "DrnoExterior", "C02_Body", 0, 0, 0]], 
    "poissond":     # Poisson de Dereno				
        [["poissond"  , "fishd", ], ["Dereno", "DrnoExterior", "FishC06", 0, 0, 90]], 
    "poissong1":    # Poisson 1 de Kemo				
        [["poissong1" , "fishk1", ], ["Garden", "kemoGarden", "FishA", 0, 0, 90]], 
    "poissong2":    # Poisson 2 de Kemo				
        [["poissong2" , "fishk2", ], ["Garden", "kemoGarden", "FishB", 0, 0, 90]], 
    "poissong3":    # Poisson 3 de Kemo				
        [["poissong3" , "fishk3", ], ["Garden", "kemoGarden", "FishC", 0, 0, 90]], 
    "urwin":        # Urwin de Negilhan				
        [["urwin"     , ], ["Negilahn", "Jungle", "Urwin_Head", 0, -90, 180]], 
    "singe":        # Singe de Negilhan				
        [["singe"     , "monkey", ], ["Negilahn", "Jungle", "2Tails_Root", 0, 0, 60]], 
    "sandscrit":    # Sandscrit de Payiferen		
        [["sandscrit" , ], ["Payiferen", "Pod", "BoneSSHead", 0, -90, 180]], 
    "shroomie":     # Shroomie de Teledahn			
        [["shroomie"  , ], ["Teledahn", "tldnHarvest", "Sniff_SB_Spine01", 0, 0, 0]], 
    "bird1":        # Oiseau 1 Eder Gira			
        [["birdg1"    , "bg1", ], ["Gira", "giraCanyon", "Bird01", 0, 0, 180]], 
    "bird2":        # Oiseau 2 Eder Gira			
        [["birdg2"    , "bg2", ], ["Gira", "giraCanyon", "Bird02", 0, 0, 180]], 
    "fish1":        # Poisson 1 Eder Gira			
        [["fishg1"    , "fg1", ], ["Gira", "giraCanyon", "Fish01Master", 0, 0, 180]], 
    "fish2":        # Poisson 2 Eder Gira			
        [["fishg2"    , "fg2", ], ["Gira", "giraCanyon", "Fish02Master", 0, 0, 180]], 
    "fish3":        # Poisson 3 Eder Gira			
        [["fishg3"    , "fg3", ], ["Gira", "giraCanyon", "Fish03Master", 0, 0, 180]], 
    "fish4":        # Poisson 4 Eder Gira			
        [["fishg4"    , "fg4", ], ["Gira", "giraCanyon", "Fish04Master", 0, 0, 180]], 
    "bahro":        # Bahro de l'Arche de la Ville	
        [["bahro"     , "bahro0", "b0"], ["city", "bahroFlyers_arch", "B_ArchBody_28", 0, 0, 0]], 
    "b1":           # Bahro1 de la Ville			
        [["b1"        , "bahro1", ], ["city", "bahroFlyers_city1", "B01_BoneSpine3", 90, 0, 90]], 
    "b2":           # Bahro2 de la Ville			
        [["b2"        , "bahro2", ], ["city", "bahroFlyers_city2", "B02_BoneSpine3", 90, 0, 90]], 
    "b3":           # Bahro3 de la Ville			
        [["b3"        , "bahro3", ], ["city", "bahroFlyers_city3", "B03_BoneSpine3", 90, 0, 90]], 
    "b4":           # Bahro4 de la Ville			
        [["b4"        , "bahro4", ], ["city", "bahroFlyers_city4", "B04_BoneSpine3", 90, 0, 90]], 
    "b5":           # Bahro5 de la Ville			
        [["b5"        , "bahro5", ], ["city", "bahroFlyers_city5", "B05_BoneSpine3", 90, 0, 90]], 
    "b6":           # Bahro6 de la Ville			
        [["b6"        , "bahro6", ], ["city", "bahroFlyers_city6", "B06_BoneSpine3", 90, 0, 90]]
}

## Recherche de l'animal
def GetAnimal(name):
    for k, v in animals.items():
        if name.lower() in v[0]:
            return [k, v[1]]
    return None

# Activer les SDL de la ville pour les bahros
def ActivateBahros():
    sdl=PtGetAgeSDL()
    sdl["islmS1FinaleBahro"] = (1,)
    sdl['islmS1FinaleBahroCity1'] = (1,)
    sdl['islmS1FinaleBahroCity2'] = (1,)
    sdl['islmS1FinaleBahroCity3'] = (1,)
    sdl['islmS1FinaleBahroCity4'] = (1,)
    sdl['islmS1FinaleBahroCity5'] = (1,)
    sdl['islmS1FinaleBahroCity6'] = (1,)        

#*****************************#
#                             #
#Suivre objets en mouvements  #
#                             #
#*****************************#
def Suivre2(objet='sandscrit',Avatar='moi',duree=300): #la duree est en secondes
    """Attacher un avatar sur un objet en mouvement dont la taille est xxx %
    et le suivre durant xx secondes puis atterrir au point par defaut"""
    # Formatage de la duree
    if isinstance(duree, int):
        duree = duree * 1.0
    elif isinstance(duree, float):
        pass
    else:
        try:
            duree = float(duree)
        except:
            duree = 60.0
    
    # Recherche de l'animal
    animal = GetAnimal(object)
    if animal is None:
        # l'animal n'a pas ete trouve, on arrete la.
        print "L'animal '{0}' n'a pas ete trouve".format(objet)
        return
    
    # Pour les Bahros de la Ville :
    if animal[1][0] == "city":
        ActivateBahros()
    
    animal = animal[1]
    Age = animal[0]
    Prp = animal[1]
    Objet = animal[2]
    Anglex = float(animal[3])
    Angley = float(animal[4])
    Anglez = float(animal[5])
    PtConsoleNet('Nav.PageInNode '+ Prp, 1)
    if Avatar == 'moi':
        Joueur = PtGetLocalAvatar()
    else:
        Joueur = SCOAvatar(Avatar)
    Joueur.netForce(1)
    Joueur.physics.netForce(1)
    Joueur.physics.disable()
    PtSetAlarm(1, Lier(Age, Joueur, Objet, duree, Anglex, Angley, Anglez), 1)
