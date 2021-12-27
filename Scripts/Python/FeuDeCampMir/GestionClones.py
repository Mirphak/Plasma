# -*- coding: utf-8 -*-
""" Yodawave"""

from Plasma import *
from FeuDeCampMir import   CdPerso , VarPerso
"""   Gestion des clones  permet de generer mes clones sans influencer  les autres,  gere un dictionnaire des demandeurs et des clones leur appartenant    
        !!!!!!!! si reload perte du Dictionnaire (DicDesDemandeurs) donc clones orphelins  il y a un  SceneObject   par objet ou par clone  donc un cloneKey  par clone
VarPerso.DicDemandeursClones     =   {}              vide le Dictionnaire
VarPerso.AccessVarPerso.DicDemandeursClones = {        [self._NomDemandeur] :      {        [self._masterKey.getName()] = [  liste de   CloneKey ]      }      }

**********************************************************      Exemple de demande  avec attente du resultat        *************************
    def Start(self,):
        self.On = True
        PtSetAlarm( 0.5  ,  self,  -1 )
        return

    def onAlarm(self,param):#--------------------------------------------------------------------------------------------------------       onAlarm
        if param == -2 :
            self.cloneKeysBugs = GestionClones.GetClones(self.Demandeur,self.masterKeyBugs, self.NbrClone )
            if       len (self.cloneKeysBugs ) == self.NbrClone   :
                PtSetAlarm( 0.5 ,  self,  0 )
            else :
                PtSetAlarm( 0.5 ,  self,  -2 )

        if param == -1 :
            self.cloneKeysBugs = GestionClones.GetClones(self.Demandeur,self.masterKeyBugs, self.NbrClone )
            if len (  self.cloneKeysBugs  ) != self.NbrClone :
                try :
                    GestionClones.DemandeClone(self.Demandeur,self.masterKeyBugs , self.NbrClone )
                except :
                    PtSendKIMessage(26,"Bugs      erreur chargement clone")
                PtSetAlarm( 0.5 ,  self,  -2  )
            else :
                PtSetAlarm( 0.5 ,  self,  0 )
        
        if param== 0 :#**********************************************************            clone OK  on peut les utiliser        *************************
"""
 #                 deplace tout les clones d'un objet ,                        (  si il sont encore en cours de validité  l'instance proprietaire les reprends automatiquement  )         ???????????
def CacheCloneInutile(NomDemandeur ="" ,  masterKey = None ,  OffsetZ =0 ) :
    print("CacheCloneInutile(NomDemandeur='{}', masterKeyName='{}', OffsetZ={})".format(NomDemandeur, masterKey.getName(), OffsetZ))
    try :
        if NomDemandeur not in VarPerso.AccessVarPerso.DicDemandeursClones :
            print("On cache les clones du demandeur inconnu {}".format(NomDemandeur))
            cloneKeys = PtFindClones(masterKey)
            if len( cloneKeys ) > 0 :
                for cloneKey in scloneKeys :#                                                          suprime  draw  et physics    des     cloneKey.getSceneObject
                    CdPerso.RetireSceneobject( cloneKey.getSceneObject() , 0 )
            else :
                #PtSendKIMessage(26,"pas de CloneInutile    :" )
                print("Pas de CloneInutile (n'appartenant pas a {})".format(NomDemandeur))
        else:
            print("On ne cache pas les clones des demandeurs connu.")
    except :
        PtSendKIMessage(26,"Erreur  CacheCloneInutile    :" )
    return

def GetClones(NomDemandeur ="",masterKey=None , NbrClones=0 ):
    """      regarde si NomDemandeur, masterKey.getName      existe dans VarPerso.AccessVarPerso.DicDemandeursClones et renvoie la liste de CloneKey de NbrClones demandée
            sinon retourne une liste vide """
    if NomDemandeur in VarPerso.AccessVarPerso.DicDemandeursClones :
        if  masterKey.getName()   in  VarPerso.AccessVarPerso.DicDemandeursClones[NomDemandeur] :
            try :
                if len(VarPerso.AccessVarPerso.DicDemandeursClones[NomDemandeur][masterKey.getName()]) >=  NbrClones :
                    ListRetour =[]
                    CloneKeys  =  PtFindClones(masterKey)
                    for CloneKey in VarPerso.AccessVarPerso.DicDemandeursClones[NomDemandeur][masterKey.getName()] :
                        if CloneKey   in CloneKeys :#    !!!!!!!!!!!!!!!           sont ils encore actifs     ?
                            ListRetour.append (CloneKey)
                            if len (ListRetour)  == NbrClones :#              ne retourne que le Nbr voulu
                                return ListRetour#                                      OK  ils sont bon
                        else :
#                            PtSendKIMessage(26,"GetClones  CloneKey  " + str(masterKey.getName())+"  n est plus valide")
                            return []
                else:
#                    PtSendKIMessage(26,"NbrClones  insufisant")#                 ils sont inferieur à   NbrClones
                    return []
            except   :
                PtSendKIMessage(26,"Erreur  GetClones    :" + str(masterKey.getName()) + "             " + str( NomDemandeur )                  )
                return []
        else:
#            PtSendKIMessage(26,"GetClones  masterKey.getName()   invalide ")
            return []
    else :
#        PtSendKIMessage(26,"GetClones  NomDemandeur   absent ")
        return []

def DemandeClone ( NomDemandeur ="",masterKey=None , NbrClones=0):#           !!!!!!!!!!!!!!!!!!!!!!!!!!!            Rien  en retour                       faire  GetClones
    Clonage.DemandeClone(NomDemandeur,masterKey , NbrClones )

def RegenereClone ( NomDemandeur ="",masterKey = None):
    Clonage.DemandeClone(NomDemandeur,masterKey ,    len (VarPerso.AccessVarPerso.DicDemandeursClones[NomDemandeur][masterKey.getName()])   ) #     a revoire

def RenouvelerClone ( NomDemandeur ="",masterKey=None , NbrClones=0):#                                              voir le faire avec supression dans dictionnaire
    Clonage.RenouvelerClone(NomDemandeur,masterKey , NbrClones )

class InitClonage():
    """          gestion des clones permet d avoir plusieurs types de clones par demandeur et  plusieurs demandeurs ayant le meme type de clones  
                   memorise les  demandeurs, les  types de clone (CloneKey )  dans un dictionnaire 
                   !!!!!!!!!!!!!!!!!!!!!!!           reloader le module provoque des orphelins            perte du Dic        voir fichier
                  delete est impossible reste desactivation activation  """
    def __init__(self, ):
        self._NomDemandeur  = None
        self._masterKey = None
        self._NbrClones = None
        self._cloneKeys  = []
        self._cloneKeysNonPerso = []
        self._ListCloneKeyDemandeur =[]
        self.ClonageEnCours = False
        self.ListeClonage =[]

    def DemandeClone ( self,  NomDemandeur ="",masterKey=None , NbrClones=0):
        NvDemande = (  NomDemandeur  , masterKey  ,  NbrClones ,  )#---------------------------------------------------------------------------------------------------------------------------------- empile les demandes
        self.ListeClonage.append ( NvDemande   )
        PtSetAlarm(0.5,self, 1)

    def RenouvelerClone ( self,  NomDemandeur ="",masterKey=None , NbrClones=0):
        """  si probleme avec les clones en attribue de Nv  """
        self._NomDemandeur  = NomDemandeur
        self._masterKey = masterKey
        self._NbrClones = NbrClones
        PtSetAlarm(0.5,self, 9)

#        *******************************************************************************************************************************************************         onAlarm
    def onAlarm(self, param): # param = (3 ou 8) libre
#        PtSendKIMessage(26,"InitClonage  onAlarm   ="+ str(param))
        if param == 1 :#------------------------------------------------------------------------------------------------------------------              traitement   Liste d'attente   DemandeClone
            if  len (self.ListeClonage)  ==  0 :
#                PtSendKIMessage(26,"ListeClonage vide")
                return
            else:
#                PtSendKIMessage(26,"ListeClonage =  " + str(len (self.ListeClonage)))
                PtSetAlarm(1.0 ,self, 1)
                if self.ClonageEnCours == False :
                    self.ClonageEnCours = True
                    Demande =  self.ListeClonage[0]#--------------------------------------------------------------------------------------------------------------------------------------------------------             depile les demandes
                    self._NomDemandeur  = Demande[0]
                    self._masterKey = Demande[1]
                    self._NbrClones = Demande[2]
                    del self.ListeClonage [0]
                    PtSendKIMessage(26,"_NomDemandeur  :" +str(self._NomDemandeur) + "        _masterKey :" +str(self._masterKey.getName())  + "            _NbrClones :" +str(self._NbrClones)      )
                    CacheCloneInutile(self._NomDemandeur  ,  self._masterKey  ,  0 )
                    PtSetAlarm(1,self, 2)
            return
            
        if param == 2 :#-------------------------------------------------------------------------------------------------------------------------  DemandeClone              si ils existe     on se contente   de   les recharge et retour
            self._ListCloneKeyDemandeur =[]
            if not isinstance(self._masterKey, ptKey):
                PtSendKIMessage(26,"masterKey n'est pas valide")
                return
            if self._NomDemandeur == "":
                PtSendKIMessage(26,"NomDemandeur  absent")
                return
            try :
                if self._NomDemandeur in VarPerso.AccessVarPerso.DicDemandeursClones :#         -----------------------------------------------------  est ce que le demandeur est deja dans VarPerso.AccessVarPerso.DicDemandeursClones
                    if self._masterKey.getName()  in VarPerso.AccessVarPerso.DicDemandeursClones[self._NomDemandeur] :#  -------------- est ce que masterKey.getName est deja dans VarPerso.AccessVarPerso.DicDemandeursClones
#                        PtSendKIMessage(26," recherche bug DemandeClone  :" +  str (  VarPerso.AccessVarPerso.DicDemandeursClones[self._NomDemandeur] )  ) 
                        self._ListCloneKeyDemandeur = VarPerso.AccessVarPerso.DicDemandeursClones[self._NomDemandeur][self._masterKey.getName()]
                        if len(self._ListCloneKeyDemandeur) == self._NbrClones : #-------------------------------------------------------------------------------   Nbr = a la demande   :   renvoyer et recharger le Nbr demandé
#                            PtSendKIMessage(26,"recherche bug DemandeClone   Nbr = a la demande")
                            PtSetAlarm(0.5, self, 5)
                        else :
                            if len(self._ListCloneKeyDemandeur) > self._NbrClones : #-------------------------------------------------------------------------------  Nbr > a la demande :  renvoyer et recharger le Nbr demandé        ( fait par GetClones)
#                                PtSendKIMessage(26,"recherche bug DemandeClone  Nbr > a la demande")
                                PtSetAlarm(0.5, self, 5)
                            if len(self._ListCloneKeyDemandeur) < self._NbrClones : #------------------------------------------------------------------------------  Nbr <  a la demande : cloner le Nbr manquant    renvoyer et recharger le Nbr demandé   OK
#                                PtSendKIMessage(26,"recherche bug DemandeClone Nbr <  a la demande")
                                self._cloneKeysNonPerso = PtFindClones(self._masterKey)
                                PtSetAlarm(0.5, self, 4)
                    else :  #------------------------------------------------------------------------------------------------------------------------------------------------------------  demandeur est deja dans VarPerso.AccessVarPerso.DicDemandeursClones          mais pas    masterKey.getName
#                        PtSendKIMessage(26,"recherche bug DemandeClone  demandeur est deja dans VarPerso.AccessVarPerso.DicDemandeursClones          mais pas    masterKey.getName")
                        VarPerso.AccessVarPerso.DicDemandeursClones[self._NomDemandeur] [ self._masterKey.getName() ] = []
                        self._cloneKeysNonPerso = PtFindClones(self._masterKey)#****************************************************************************erreur ????????????????????????
                        PtSetAlarm(0.5, self, 4)
                else : #    ---------------------------------------------------------------------------------------------------------------------------------------------------------------  inventaire inutile  ils ne m"appartiennent  pas                    prendre en compte la Cd 
#                    PtSendKIMessage(26,"recherche bug DemandeClone  inventaire inutile")
                    VarPerso.AccessVarPerso.DicDemandeursClones[self._NomDemandeur] = {}
                    VarPerso.AccessVarPerso.DicDemandeursClones[self._NomDemandeur] [self._masterKey.getName()] = []
                    self._cloneKeysNonPerso = PtFindClones(self._masterKey)
                    PtSetAlarm(0.5, self, 4)
            except  :
                PtSendKIMessage(26,"erreur DemandeClone   :  "+str(self._NomDemandeur)+"          : "+str( self._masterKey.getName() )         )
            return
            
        if param == 4 :#-------------------------------------------------------------------------------------------------------------------------------------  creation des clones
            try :
                CloneObtenue = len(self._ListCloneKeyDemandeur)
                for i in range(self._NbrClones - CloneObtenue):
                    PtCloneKey(self._masterKey)
                    PtDebugPrint("PtCloneKey   " + str(i))#              pour ralentire la boucle depuit python3
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
            except :
                 PtSendKIMessage(26,"erreur creation des clones   :  param == 4 "  )
                 
            if compteur < self._NbrClones  :
                PtSetAlarm(1, self, 4)
            else :
                PtSetAlarm(0.5, self, 5)
            return
                
        if param == 5 :#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  inventaire  des Clones  et recharge
            ListCloneKeyActif = PtFindClones(self._masterKey)
            CloneActif =0
            try :
                for CloneKey in self._ListCloneKeyDemandeur :#  --------------------------  on verifie qu"il sont toujours Actif
                    if CloneKey in ListCloneKeyActif :
                        CloneActif +=1
            except :
                PtSendKIMessage(26,"erreur Clonage  param == 5     CloneActif :  "  +str( CloneActif) +  "      ListCloneKeyActif :   " + str(len (ListCloneKeyActif)) + "         Name_masterKey   :" + str  (self._masterKey.getName())         )
            
            if CloneActif  ==  self._NbrClones : #                                                      ok  on  les recharge et retour
                PtSetAlarm(0.5, self, 6)
            else :
                PtSetAlarm(0.0, self, 9)#                     le Nbr n"est pas OK
            return
            
        if param == 6 :#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  on recharge les clones et memorise la liste
            if  len(self._ListCloneKeyDemandeur) == 1 :#   -----------------------------  si il y en a 1 seul
                PtCloneKey (self._ListCloneKeyDemandeur[0], 1) 
            else :#  ----------------------------------------------------------------------------------- si > a 1
                try :
                    for CloneKey in self._ListCloneKeyDemandeur :#              ---------------------------------------------------------------  verifie si fonctionne avec 1 seul element dans la liste
                        PtCloneKey (CloneKey, 1) 
                except :
                    PtSendKIMessage(26,"erreur  on recharge les clones et memorise la liste :  param == 6   " + str( len(self._ListCloneKeyDemandeur) ) )#--------------------------EVITER L'ERRREUR   ???????????????????
            VarPerso.AccessVarPerso.DicDemandeursClones[self._NomDemandeur][self._masterKey.getName()] = self._ListCloneKeyDemandeur
            self.ClonageEnCours = False
            return


        if param == 7 :#----------------------------------------------------------------------  revalider  les clones d un demandeur          (Regenere)             inutile 6 le fait                      faire TRY
            try :
                if self._NomDemandeur in VarPerso.AccessVarPerso.DicDemandeursClones :
                    self._cloneKeys = VarPerso.AccessVarPerso.DicDemandeursClones[self._NomDemandeur][self._masterKey.getName()]
                    for  CloneKey  in self._cloneKeys :
                        PtCloneKey(CloneKey, 1)
                return
            except :
                PtSendKIMessage(26,"erreur revalider  les clones d'un demandeur :  param == 7 "  )
            return
            
        if param == 9 :#------------------------------------   renouvelle  les clones d'un demandeur                 ( le Nbr n"est pas OK,        ou un autre Magic les utilise )
            """   les  suprime du Dic et les fait passer dans      _cloneKeysNonPerso         et renouvelle la demande    repasse par   DemandeClone   """
            try :
                if self._NomDemandeur in VarPerso.AccessVarPerso.DicDemandeursClones :
                    if self._masterKey.getName()  in VarPerso.AccessVarPerso.DicDemandeursClones[self._NomDemandeur] :
                        NbrClones = len (VarPerso.AccessVarPerso.DicDemandeursClones[self._NomDemandeur][self._masterKey.getName()])
                        VarPerso.AccessVarPerso.DicDemandeursClones[self._NomDemandeur][self._masterKey.getName()] = []
                        self._cloneKeysNonPerso = PtFindClones(self._masterKey)
                        DemandeClone (   self._NomDemandeur  , self._masterKey , NbrClones  )
                return
            except :
                PtSendKIMessage(26,"erreur  renouvelle  les clones d'un demandeur :  param == 4 "  )
            return

Clonage = InitClonage()

PtSendKIMessage(26,"Reload GestionClones OK")



"""
ce Module sert à créer de nouveaux clones
/Save-WD-Elements/Element EXT3-5/Uru Totalite/Source/Plasma-master/17-05-31/Plasma-master/Sources/Plasma/PubUtilLib/plMessage/plLoadCloneMsg.cpp

PtCloneKey()             exige   ptKey  and bool

PtFindClones()

PtCloneKey(self._masterKey, 1)                                      pour créer un clone de l"objet  _masterKey
PtCloneKey(self._masterKey)

cloneKeys = PtFindClones(masterKey)                                fourni la liste des clones d"un objet si il en a

PtCloneKey(cloneKey, 0)                                                      devalide affichage   ---------------------------------------------------------------------#-----   a eviter provoque des plantages
PtCloneKey(cloneKey, 1)                                                      valide affichage    ! si associé à un respondeur  le declencher

REMARQUE :=============================================================================================================================================

CONSTAT :  par experience personnelle   **************************************

CERTAINS  CLONES NE POSENT AUCUN PROBLEME            à l'arrive comme au depart dans l'age
("GreatZeroBeam-RTProj", "city")  ShowLaser
("PodSymbolRoot", "Payiferen")     Spirale           et bien d'autres

CERTAINS CLONES   posent des problemes lorsque l'on quitte l'age ou que l'on devalide les clones 
                                ces clones sont souvent liés à d'autres objets ou gerés par d'autres animations
                                
("BugFlockingEmitTest", "Personal")
("FireworkRotater1", "Personal")
("FireworkRotater102", "Personal")
("FireworkRotater103", "Personal")

DE PLUS si plusieurs Magic veulent jouer ensemble il peut y avoir des problèmes d'attribution des clones
MA SOLUTION :

j'ai plusieurs scripts pouvant utiliser des clones du meme objet (risque de conflic)

je crée un Dictionnaire (VarPerso.AccessVarPerso.DicDemandeursClones) avec une entrée par script (demandeur) je memorise CloneKey et NbrClones demandés
donc je connais à tout moment mes clones

MAIS il y a un autre problème ! si je quitte (plante) quand je reviens le serveur me reattribue les memes clones  ou pas
ce qui peut poser problème !   (reloader le module provoque des orphelins   (perte du Dictionnaire)    )       il faudrait memoriser sur disque pour l'éviter

autre probleme principalement pour les FireworkRotater   (Spark)   si les joueurs arrivent après la creation des clones ******************************************************
ils ne voient que l'explosion et rien d'autre donc comme le serveur me réattribue les memes clones ils ne peuvent pas les voir meme si je redémarre
donc il faut les oublier d'où l'utilisation de  RenouvelerClone  pour que les Nv arrivants puissent les voir

    def RenouvelerClone(self):
        self.On = False
        GestionClones.RenouvelerClone("Spark",self.masterKeySpark1 ,5)
        GestionClones.RenouvelerClone("Spark",self.masterKeySpark2 ,5)
        GestionClones.RenouvelerClone("Spark",self.masterKeySpark3 ,5)


Autre REMARQUE :===========================================================================================================================================
Du, pour une grande par à l'environnement graphique il peut y avoir du lag voire plantage si dans la region d'affichage 
il y a beaucoup d'elements   (et bien sur beaucoup de clones)  en mouvement (ou pas) à afficher,     la carte graphique peut se trouver depassée .

Donc en general             je ne les devalide plus (plantage)                mais je les deplace le plus loin possible,  

ils ne sont plus affichés voire ils n'occupent qu'une partie infime de l'affichage
"""




