# -*- coding: utf-8 -*-
""" Yodawave"""


from Plasma import *
"""
PtCloneKey()             exige   ptKey  and bool

PtFindClones()

PtCloneKey(self._masterKey, 1)                                      pour créer un clone de l"objet  _masterKey
PtCloneKey(self._masterKey)

cloneKeys = PtFindClones(masterKey)                                fourni la liste des clones d"un objet si il en a

PtCloneKey(cloneKey, 0)                                                      devalide affichage
PtCloneKey(cloneKey, 1)                                                      valide affichage    ! si associé à un respondeur


REMARQUE :=================================================================================

CONSTAT :  par experience personnelle   **************************************

CERTAINS  CLONES NE POSENT AUCUN PROBLEME            à l'arriv'e comme au depart dans l'age
("GreatZeroBeam-RTProj", "city")  Laser
("PodSymbolRoot", "Payiferen")     Spiral           et bien d'autres

CERTAINS CLONES   posent des problemes lorsque l'on quitte l'age ou que l'on devalide les clones 
                                ces clones sont souvent liés à d'autres objets ou gerés par d'autres animations
                                
("BugFlockingEmitTest", "Personal")
("FireworkRotater1", "Personal")
("FireworkRotater102", "Personal")
("FireworkRotater103", "Personal")

DE PLUS si plusieurs Magic veulent jouer ensemble il peut y avoir des problèmes d'attribution des clones
MA SOLUTION :

j'ai plusieurs scripts pouvant utiliser des clones du meme objet (risque de conflic)

je crée un Dictionnaire (DicDesDemandeurs) avec une entrée par script (demandeur) je memorise CloneKey et NbrClones demandés
donc je connais à tout moment mes clones

MAIS il y a un autre problème ! si je quitte (plante) quand je reviens le serveur me reattribue les memes clones
ce qui peut poser problème !   (reloader le module provoque des orphelins   (perte du Dictionnaire)    )       il faudrait memoriser sur disque pour l'éviter

autre probleme principalement pour les FireworkRotater   (Spark)   si les joueurs arrivent après la creation des clones ******************************************************
ils ne voient que l'explosion et rien d'autre donc comme le serveur me réattribue les memes clones ils ne peuvent pas les voir meme si je redémarre
donc il faut les oublier d'où l'utilisation de  RenouvelerClone  pour que les Nv arrivants puissent les voir

    def RenouvelerClone(self):
        self.On = False
        GestionClones.RenouvelerClone("Spark",self.masterKeySpark1 ,5)
        GestionClones.RenouvelerClone("Spark",self.masterKeySpark2 ,5)
        GestionClones.RenouvelerClone("Spark",self.masterKeySpark3 ,5)


Autre REMARQUE :=================================================================================
Du, pour une grande par à l'environnement graphique il peut y avoir du lag voire plantage si dans la region d'affichage 
il y a beaucoup d'elements   (et bien sur beaucoup de clones)  en mouvement (ou pas) à afficher,     la carte graphique peut se trouver depassée .
Donc en general je ne les devalide plus (plantage) mais je les deplace le plus loin possible, soit ils ne sont plus affichés voire ils n'occupent qu'une partie infime de l'affichage


"""

#=========================================================================================================================================================
"""
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!                            je n'utilise plus   les lignes  24 à 113     ,      ( peut poser des problemes si on est plusieurs Magic )                 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
"""
#=========================================
def DechargerClones(masterKey):#     devalide  tout les clones de l objet   masterKey
    """
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!     si un autre Magic a aussi crée des clones de meme type il peut  planter  à l'execution de DechargerClones
    
    et tout autre joueur dans certains cas
    
    """
    print ">> DechargerClones() <<"
    cloneKeys = PtFindClones(masterKey)
    for ck in cloneKeys:
        PtCloneKey(ck, 0)


def RechargerClones(masterKey):#   revalide  tous les clones de l objet   masterKey
    print ">> RechargerClones() <<"
    cloneKeys = PtFindClones(masterKey)
    for ck in cloneKeys:
        PtCloneKey(ck, 1)#   ?????????

# Clonage d"un object (nom de l"objet, nom fichier age et nombre de clones en parametre)
def CloneObject(objectName, ageFileName, nombre):
    PtSendKIMessage(26,"CloneObject ")
    print "CloneObject({}, {}, {})".format(objectName, ageFileName, nombre)
    PtSetAlarm(0.0, AlarmCloneObject(objectName, ageFileName, nombre), 0)#----------------------APPEL 1er  PASSAGE

class AlarmCloneObject:
    _objectName = ""
    _ageFileName = ""
    _masterKey = None
    _nombre = 1
    _delais = 1
    _maxAttempts = 5
    _attempts = 1

    # Initialisation
    def __init__(self, objectName, ageFileName, nombre):
        self._objectName = objectName
        self._ageFileName = ageFileName
        self._masterKey = PtFindSceneobject(objectName, ageFileName).getKey()
        self._nombre = nombre
        self._delais = 1
        self._attempts = 1
        print "init AlarmCloneObject(%i)" % self._nombre

    # Prenons notre temps...
    def onAlarm(self, param):
        PtSendKIMessage(26,"AlarmCloneObject  ="+ str(param))
        # Verifions d"abord si l"objet maitre a ete trouve (que c"est un ptKey)
        if isinstance(self._masterKey, ptKey):
            if param == 0:
                #                                                                                                                                        partie 0 : dechargeons d"abord les clones s"il y en a
                cloneKeys = PtFindClones(self._masterKey)
                for ck in cloneKeys:
                    PtCloneKey(ck, 0)
                PtSetAlarm(self._delais, self, 1)#----------------------APPEL 2em  PASSAGE
            elif param == 1:
                #                                                                                                                                        partie 1 : clonage
                print "clonage en cours..."
                # Existe-t-il deja des clones?
                n = len(PtFindClones(self._masterKey))
                if n < self._nombre:
                    # Il nous en faut (self._nombre - n) en plus
                    for i in range(self._nombre - n):
                        PtCloneKey(self._masterKey)
                PtSetAlarm(self._delais, self, 2)#----------------------APPEL 3em  PASSAGE
            elif param == 2:
                #                                                                                                                                       partie 2 : attendre que tous les clones soient crees    on regarde Nbr avec  len(PtFindClones(self._masterKey))
                n = len(PtFindClones(self._masterKey))
                if n < self._nombre:
                    print "%i clones trouves sur les %i demandes! (attempt #%i)" % (n, self._nombre, self._attempts)
                    if self._attempts < self._maxAttempts:
                        self._attempts = self._attempts + 1
                        PtSetAlarm(self._delais, self, 2)#----------------------APPEL 4em  PASSAGE                       si  n < self._nombre   on recommence     dans 1s
                    else:
                        print "Le clonage met trop de temps!!"
                else:
                    #                                                                                                                                   attendre avant de recharger les clones
                    PtSetAlarm(self._delais, self, 3)#----------------------APPEL 5em  PASSAGE
            elif param == 3:
                # partie 3 : rechargeons les clones crees
                cloneKeys = PtFindClones(self._masterKey)
                print "rechargement des {} clones...".format(len(cloneKeys))
                for ck in cloneKeys:
                    PtCloneKey(ck, 1)
            else:
                print "AlarmCloneObject.onAlarm : param incorrect"
        else:
            print "self._masterKey is not a ptKey (object not found)"





#
#=========================================================================================================================================================
#                                                                                                         Version actuel je n'agis que sur les clones que je crée
#=========================================
# Clonage d"un object

"""   Gestion des clones  permet de generer mes clones sans influencer  les autres,  gere un dictionnaire des demandeurs et des clones leur appartenant    
        !!!!!!!! si reload perte du Dictionnaire (DicDesDemandeurs) donc clones orphelins
---le nom de demandeur doit etre valide

                il y a un  SceneObject   par objet ou par clone
                donc un cloneKey  par clone


"""

DicDesDemandeurs = {}

def GetClones(NomDemandeur ="",masterKey=None , NbrClones=0 ):
    """      regarde si NomDemandeur, masterKey.getName      existe dans DicDesDemandeurs et renvoie la liste de CloneKey de NbrClones demandée
            sinon retourne une liste vide """
    global DicDesDemandeurs
    if NomDemandeur in DicDesDemandeurs :
        try :
            if len(DicDesDemandeurs[NomDemandeur][masterKey.getName()]) >=  NbrClones :
                ListRetour =[]
                CloneKeys  =  PtFindClones(masterKey)
                for CloneKey in DicDesDemandeurs[NomDemandeur][masterKey.getName()] :
                    if CloneKey   in CloneKeys :#    !!!!!!!!!!!!!!!           sont ils encore actifs     ?
                        ListRetour.append (CloneKey)
                        if len (ListRetour)  == NbrClones :#              ne retourne que le Nbr voulu
                            return ListRetour
                    else :
                        PtSendKIMessage(26,"GetClones  CloneKey  " + str(masterKey.getName())+"  n est plus valide")
                        return []
            return  DicDesDemandeurs[NomDemandeur][masterKey.getName()]
        except  KeyError :
            PtSendKIMessage(26,"GetClones  KeyError  " + str(masterKey.getName()))
            return []
    else :
        return []

def DemandeClone ( NomDemandeur ="",masterKey=None , NbrClones=0):
    PtSetAlarm(0.0,InitClonage(NomDemandeur,masterKey , NbrClones ), 2)

def RegenereClone ( NomDemandeur ="",masterKey = None):
    PtSetAlarm(0.0,InitClonage(NomDemandeur,masterKey , NbrClones=0 ), 7)

def DevalideClone ( NomDemandeur ="",masterKey = None):
    """ A EVITER """
    PtSetAlarm(0.0,InitClonage(NomDemandeur,masterKey , NbrClones=0 ), 8)

def RenouvelerClone ( NomDemandeur ="",masterKey=None , NbrClones=0):
     PtSetAlarm(0.0,InitClonage(NomDemandeur,masterKey , NbrClones ), 9 )

class InitClonage():
    """          gestion des clones permet d avoir plusieurs types de clones par demandeur et  plusieurs demandeurs ayant le meme type de clones  
                   memorise les  demandeurs, les  types de clone (CloneKey )  dans un dictionnaire 
                   !!!!!!!!!!!!!!!!!!!!!!!           reloader le module provoque des orphelins            perte du Dic
                  delete est impossible reste desactivation activation  """
    def __init__(self, NomDemandeur ="",masterKey=None , NbrClones=0):
        global DicDesDemandeurs
        self._DicDesDemandeurs = DicDesDemandeurs
        self._NomDemandeur  = NomDemandeur
        self._masterKey = masterKey
        self._NbrClones = NbrClones
        self._cloneKeys  = []
        self._cloneKeysNonPerso = []
        self._ListCloneKeyDemandeur =[]
        
    def onAlarm(self, param):
#        PtSendKIMessage(26,"InitClonage  onAlarm   ="+ str(param))
        
        if param == 2 :#-------------------------------------------------------------------------------------------------------------------------------------  DemandeClone
            self._ListCloneKeyDemandeur =[]
            if not isinstance(self._masterKey, ptKey):
                PtSendKIMessage(26,"masterKey n'est pas valide")
                return
            if self._NomDemandeur == "":
                PtSendKIMessage(26,"NomDemandeur  absent")
                return
            if not self._NomDemandeur in ("Marble" , "Spiral" , "Laser", "Gasper", "AttObjetSurAvatar", "PosClone", "CdMixologie" ,"Spark","AnimationArche"  ):#   liste des demandeurs valide
                PtSendKIMessage(26,"NomDemandeur  Non Valide")
                return
                
            if self._NomDemandeur in self._DicDesDemandeurs :#         ----------------------------------------------------------------------------------------------------------- est ce que le demandeur est deja dans DicDesDemandeurs
                if self._masterKey.getName()  in self._DicDesDemandeurs[self._NomDemandeur] :#  ----------------------------------------------------------------- est ce que masterKey.getName est deja dans DicDesDemandeurs
                    self._ListCloneKeyDemandeur = self._DicDesDemandeurs[self._NomDemandeur][self._masterKey.getName()]
                    if len(self._ListCloneKeyDemandeur) == self._NbrClones : #  ------------------------------------------------------------------------------------------------------- il existe et le Nbr est suffisant  :         inventaire des clones  et les recharger 
                        PtSetAlarm(0.0, self, 5)
                    else :
                        if len(self._ListCloneKeyDemandeur) > self._NbrClones : #   Nbr > a la demande :  renvoyer et recharger le Nbr demandé        ( fait par GetClones)
                            PtSetAlarm(0.0, self, 5)
                        if len(self._ListCloneKeyDemandeur) < self._NbrClones : #   Nbr <  a la demande : cloner le Nbr manquant    renvoyer et recharger le Nbr demandé   OK
                            PtSetAlarm(0.0, self, 4)
                else : #   -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  demandeur est deja dans DicDesDemandeurs          mais pas    masterKey.getName
                    self._DicDesDemandeurs[self._NomDemandeur] [self._masterKey.getName()] = []
                    self._cloneKeysNonPerso = PtFindClones(self._masterKey)
                    PtSetAlarm(0.0, self, 4)
            else :#                                                                                                                                     inventaire inutile  ils ne m"appartiennent  pas                    prendre en compte la Cd 
                self._DicDesDemandeurs[self._NomDemandeur] = {}
                self._DicDesDemandeurs[self._NomDemandeur] [self._masterKey.getName()] = []
                self._cloneKeysNonPerso = PtFindClones(self._masterKey)
                PtSetAlarm(0.0, self, 4)
            return
            
            
        if param == 3 :#------------------------------------------------------------------------------------------------------------------------ effacer les clones               !!!!!!  ils ne sont plus actifs mais peuvent toujours etre presents dans   PtFindClones(self._masterKey)
            for CloneKey in self._ListCloneKeyDemandeur:#                            a utilser que si probleme avec ceux existant eviter de les suprimer du dic
                PtCloneKey(CloneKey, 0)
            self._ListCloneKeyDemandeur = []#                                                        !!!!!!!!!  le dic n est pas a jour            les clones deviennent orphelins
            self._cloneKeysNonPerso = PtFindClones(self._masterKey)
            PtSetAlarm(0.5, self, 4)
            return
            
            
        if param == 4 :#-------------------------------------------------------------------------------------------------------------------------------------  creation des clones 
            CloneObtenue = len(self._ListCloneKeyDemandeur)
            for i in range(self._NbrClones - CloneObtenue):
                PtCloneKey(self._masterKey)
            ListCloneKeyActif = PtFindClones(self._masterKey)
            compteur =0
            if len( self._cloneKeysNonPerso) > 0 :#                                         il faut trier  les miens
                for CloneKey in ListCloneKeyActif :
                    if CloneKey in self._cloneKeysNonPerso :#                            pas a moi
                        pass
                    else :#                                                                                                celui ci est a moi
                        if not CloneKey  in self._ListCloneKeyDemandeur :
                            self._ListCloneKeyDemandeur.append(CloneKey) 
                        compteur +=1
            else :#                                                                                                        ils sont tous a moi
                for CloneKey in ListCloneKeyActif :
                    self._ListCloneKeyDemandeur.append(CloneKey)
                    compteur +=1
            if compteur < self._NbrClones  :
                PtSetAlarm(0.5, self, 4)
            else :
                PtSetAlarm(0.0, self, 5)
            return
                
        if param == 5 :#-------------------------------------------------------------------------------------------------------------------------------------  inventaire  des Clones
            ListCloneKeyActif = PtFindClones(self._masterKey)
            CloneActif =0
            for CloneKey in self._ListCloneKeyDemandeur :#                         on verifie qu"il sont toujours Actif
                if CloneKey in ListCloneKeyActif :
                    CloneActif +=1
            if CloneActif  ==  self._NbrClones : #                                                ok  on  les recharge et retour
              PtSetAlarm(0.0, self, 6)
            else :
              PtSetAlarm(0.0, self, 3)#                                                                     le Nbr n"est pas OK         on efface et on recommence                                a eviter      voir  timeout
            return
            
        if param == 6 :#-------------------------------------------------------------------------------------------------------------------------------------  on recharge les clones et memorise la liste
            for CloneKey in self._ListCloneKeyDemandeur :
                PtCloneKey(CloneKey, 1)
            self._DicDesDemandeurs[self._NomDemandeur][self._masterKey.getName()] = self._ListCloneKeyDemandeur
            return


        if param == 7 :#-------------------------------------------------------------------------------------------------------------------------------------  revalider  les clones d un demandeur          (Regenere)
            if self._NomDemandeur in self._DicDesDemandeurs :
                self._cloneKeys = self._DicDesDemandeurs[self._NomDemandeur][self._masterKey.getName()]
                for  CloneKey  in self._cloneKeys :
                    PtCloneKey(CloneKey, 1)
            return


        if param == 8 :#-------------------------------------------------------------------------------------------------------------------------------------   devalider  les clones d un demandeur ne les suprime pas du    DicDesDemandeurs
            if self._NomDemandeur in self._DicDesDemandeurs :
                if self._masterKey.getName()  in self._DicDesDemandeurs[self._NomDemandeur] :
                    self._cloneKeys = self._DicDesDemandeurs[self._NomDemandeur][self._masterKey.getName()]
                    for  CloneKey  in self._cloneKeys :
                        PtCloneKey(CloneKey, 0)
            return

        if param == 9 :#-------------------------------------------------------------------------------------------------------------------------------------   renouvelle  les clones d un demandeur un autre Magic les utilise
            if self._NomDemandeur in self._DicDesDemandeurs :
                if self._masterKey.getName()  in self._DicDesDemandeurs[self._NomDemandeur] :
                    self._DicDesDemandeurs[self._NomDemandeur][self._masterKey.getName()] = []
                    self._cloneKeysNonPerso = PtFindClones(self._masterKey)
                    PtSetAlarm(0.0, self, 4)
            return

PtSendKIMessage(26,"Reload GestionClones OK")


























