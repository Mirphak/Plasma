from Plasma import *
import jalak_michel as jalak
import math

# 
def GetPtPlayerAlphaNumName(player):
    name = player.getPlayerName()
    alphaNumName = ""
    for c in name:
        if c.isalnum():
            alphaNumName += c
    if alphaNumName == "":
        alphaNumName = str(player.getPlayerID())
    return alphaNumName

    
"""
To go to 5 differents spot points : J1 to J5
J4 is under the field. All the ground there is stable !
To go on the field : J0
"""

"""
To light on : light on
To light off : light off
To take off the landscape : undecorated
To place again the landscape : decorated
"""

"""
To drop objects on me : drop
"""

"""
To save a structure (Columns and widgets) : savestruct [savename]
To load  a structure: loadstruct [savename]
To load only columns : loadcolumns [savename]
To load only widgets : loadcubes [savename]
To start a 3D slide show : slideshow on
To stop the slide show : slideshow off
"""

#
def SaveStruct(self, cFlags, args):
    self.chatMgr.AddChatLine(None, "> SaveStruct", 3)
    if len(args) < 2:
        return 0
    myself = PtGetLocalPlayer()
    player = args[0]
    ageName = PtGetAgeName()
    if ageName != 'Jalak':
        #return [0, "The bot must be in Jalak to use this command."]
        return 0
    nomAvatar = GetPtPlayerAlphaNumName(player)
    nomFichier = args[1]
    self.chatMgr.AddChatLine(None, ">> SaveStruct", 3)
    jalak.SaveColumns(nomFichier, nomAvatar)
    jalak.SaveCubes(nomFichier, nomAvatar)
    return 1

#
class WaitAndLoadCubes:
    _nomFichier = ""
    _nomAvatar = ""
    _delais = 20
    # il faut environ 20s pour que les colonne aillent de la position basse a la positio haute
    
    def __init__(self, nomFichier, nomAvatar):
        self._nomFichier = nomFichier
        self._nomAvatar = nomAvatar
    def onAlarm(self, param):
        jalak.LoadCubes(self._nomFichier, self._nomAvatar)

#
def LoadStruct(self, cFlags, args):
    self.chatMgr.AddChatLine(None, "> LoadStruct", 3)
    if len(args) < 2:
        return 0
    myself = PtGetLocalPlayer()
    player = args[0]
    ageName = PtGetAgeName()
    if ageName != 'Jalak':
        #return [0, "The bot must be in Jalak to use this command."]
        return 0
    nomAvatar = GetPtPlayerAlphaNumName(player)
    nomFichier = args[1]
    self.chatMgr.AddChatLine(None, ">> LoadStruct", 3)
    maxDeltaHauteur = jalak.LoadColumns(nomFichier, nomAvatar)
    if maxDeltaHauteur < 0:
        #Le fichier des colonnes n'a pas ete charge
        maxDeltaHauteur = 0
    #delai = 10
    delai = maxDeltaHauteur
    PtSetAlarm(delai, WaitAndLoadCubes(nomFichier, nomAvatar), 1)
    return 1

#
def SaveColumns(self, cFlags, args):
    self.chatMgr.AddChatLine(None, "> SaveColumns", 3)
    if len(args) < 2:
        return 0
    myself = PtGetLocalPlayer()
    player = args[0]
    ageName = PtGetAgeName()
    if ageName != 'Jalak':
        #return [0, "The bot must be in Jalak to use this command."]
        return 0
    nomAvatar = GetPtPlayerAlphaNumName(player)
    nomFichier = args[1]
    self.chatMgr.AddChatLine(None, ">> SaveColumns", 3)
    jalak.SaveColumns(nomFichier, nomAvatar)
    return 1

#
def LoadColumns(self, cFlags, args):
    self.chatMgr.AddChatLine(None, "> LoadColumns", 3)
    if len(args) < 2:
        return 0
    myself = PtGetLocalPlayer()
    player = args[0]
    ageName = PtGetAgeName()
    if ageName != 'Jalak':
        #return [0, "The bot must be in Jalak to use this command."]
        return 0
    nomAvatar = GetPtPlayerAlphaNumName(player)
    nomFichier = args[1]
    self.chatMgr.AddChatLine(None, ">> LoadColumns", 3)
    jalak.LoadColumns(nomFichier, nomAvatar)
    return 1

#
def SaveCubes(self, cFlags, args):
    self.chatMgr.AddChatLine(None, "> SaveCubes", 3)
    if len(args) < 2:
        return 0
    myself = PtGetLocalPlayer()
    player = args[0]
    ageName = PtGetAgeName()
    if ageName != 'Jalak':
        #return [0, "The bot must be in Jalak to use this command."]
        return 0
    nomAvatar = GetPtPlayerAlphaNumName(player)
    nomFichier = args[1]
    self.chatMgr.AddChatLine(None, ">> SaveCubes", 3)
    jalak.SaveCubes(nomFichier, nomAvatar)
    return 1

#
def LoadCubes(self, cFlags, args):
    self.chatMgr.AddChatLine(None, "> LoadCubes", 3)
    if len(args) < 2:
        return 0
    myself = PtGetLocalPlayer()
    player = args[0]
    ageName = PtGetAgeName()
    if ageName != 'Jalak':
        #return [0, "The bot must be in Jalak to use this command."]
        return 0
    nomAvatar = GetPtPlayerAlphaNumName(player)
    nomFichier = args[1]
    self.chatMgr.AddChatLine(None, ">> LoadCubes", 3)
    jalak.LoadCubes(nomFichier, nomAvatar)
    return 1

"""
To take off widgets : ResetCubes
To move down the columns : ResetColumns
To take off widgets and down columns : ResetStruct
"""

#
def ResetCubes(self, cFlags, args):
    self.chatMgr.AddChatLine(None, "> ResetCubes", 3)
    ageName = PtGetAgeName()
    if ageName != 'Jalak':
        #return [0, "The bot must be in Jalak to use this command."]
        return 0
    jalak.ResetCubes()
    return 1

#
def ResetColumns(self, cFlags, args):
    self.chatMgr.AddChatLine(None, "> ResetColumns", 3)
    ageName = PtGetAgeName()
    if ageName != 'Jalak':
        #return [0, "The bot must be in Jalak to use this command."]
        return 0
    jalak.ResetColumns()
    return 1

#==================================================
# 
#==================================================
import math

age = "Jalak"
pages = ["jlakArena"]

bPagesAdded = False

#lstColumnPhys = [   "columnPhys_00","columnPhys_01","columnPhys_02","columnPhys_03","columnPhys_04",\
#                    "columnPhys_05","columnPhys_06","columnPhys_07","columnPhys_08","columnPhys_09",\
#                    "columnPhys_10","columnPhys_11","columnPhys_12","columnPhys_13","columnPhys_14",\
#                    "columnPhys_15","columnPhys_16","columnPhys_17","columnPhys_18","columnPhys_19",\
#                    "columnPhys_20","columnPhys_21","columnPhys_22","columnPhys_23","columnPhys_24"]

# Les variables
lstColumnPhys = list()
dicColumnPhys = dict()
dicClones = dict()

def InitColumns():
    global lstColumnPhys
    global dicColumnPhys
    global dicClones
    # Recuperons la liste des colonnes (sceneobject)
    #lstColumnPhys = PtFindSceneobjects("columnPhys_")
    lstColumnPhys = PtFindSceneobjects("column_")
    # Dictionnaire des ptKey des colonnes
    for i in range(len(lstColumnPhys)):
        dicColumnPhys.update({"columnphys{}".format(i):lstColumnPhys[i].getKey()})
    # Dictionnaire des clones
    for i in range(len(lstColumnPhys)):
        dicClones.update({"columnphys{}".format(i):[]})

#

#
class AlarmCloneColumnPhys:
    _masterKey = PtFindSceneobject("columnPhys_00", age).getKey()
    _nombre = 1
    _numero = 0
    _delais = 1
    _maxAttempts = 5
    _attempts = 1
    def onAlarm(self, context = 0):
        CloneColumnPhys(self._masterKey)

    # Initialisation
    def __init__(self, nombre, numero=0):
        self._nombre = nombre
        self._numero = numero
        self._masterKey = dicColumnPhys["columnphys{}".format(self._numero)]
        self._delais = 1
        self._attempts = 1
        print "init AlarmCloneColumnPhys {}".format(self._nombre)

    # Clonage general (n clones)
    def Cloner(self, nombre):
        for i in range(nombre):
            PtCloneKey(self._masterKey, 1)

    # Prenons notre temps...
    def onAlarm(self, param):
        if param == 1:
            # partie 1 : clonage
            print "clonage en cours..."
            # Existe-t-il deja des clones?
            n = len(PtFindClones(self._masterKey))
            if n < self._nombre:
                # Il nous en faut (self._nombre - n) en plus
                self.Cloner(self._nombre - n)
            PtSetAlarm(self._delais, self, 2)
        elif param == 2:
            # partie 2 : sauvegarde des clones
            n = len(PtFindClones(self._masterKey))
            # attendre que tous les clones soient crees
            if n < self._nombre:
                print "{} clones trouves sur les {} demandes! (attempt #{})".format(n, self._nombre, self._attempts)
                if self._attempts < self._maxAttempts:
                    self._attempts = self._attempts + 1
                    PtSetAlarm(self._delais, self, 2)
                else:
                    print "Le clonage met trop de temps!!"
            else:
                print "sauvegarde des {} clones...".format(n)
                self.saveClones()
        else:
            print "AlarmCloneColumnPhys.onAlarm : param incorrect"

    # Sauvons les clones!
    def saveClones(self):
        global dicClones
        #dicClones["columnphys"] = PtFindClones(self._masterKey)
        for i in range(len(lstColumnPhys)):
            dicClones["columnphys{}".format(i)] = PtFindClones(dicColumnPhys["columnphys{}".format(i)])
            print "nb clones de {}: {}".format(lstColumnPhys[i].getName(), len(dicClones["columnphys{}".format(i)]))

#
def CloneColumnPhys(nombre, numero=0):
    print "CloneColumnPhys()"
    PtSetAlarm(1, AlarmCloneColumnPhys(nombre, numero), 1)

#
def Figure():
    posZero = ptMatrix44()
    for i in range(len(lstColumnPhys)):
        lstCloneKeys = dicClones["columnphys{}".format(i)]
        for j in range(len(lstCloneKeys)):
            so = lstCloneKeys[j].getSceneObject()
            #if i == 0 and j == 0:
                #posZero = so.getLocalToWorld()
            posZero = lstColumnPhys[i].getLocalToWorld()
            mRot = ptMatrix44()
            mRot.rotate(0, math.pi / 2)
            mTrans = ptMatrix44()
            mTrans.translate(ptVector3(i, j, 0))
            newPos = posZero * mTrans * mRot
            so.netForce(1)
            so.physics.disable()
            so.physics.warp(newPos)
        
##
#class AlarmWaittingForClones:
#    _nbFois = 0
#    _nbClones = 0
#    _scale = 1
#    #_masterName = "columnphys"
#    
#    def __init__(self, nombre, scale):
#        self._nbClones = nombre
#        self._scale = scale
#    
#    def onAlarm(self, param):
#        print "> AlarmWaitting.onAlarm"
#        if param == 1:
#            nbClonesFound = len(dicClones["columnphys"])
#            print ">> nb de clones de %s %i" % ("columnphys", nbClonesFound)
#            # Attendre que tous les clones soient crees, mais pas indefiniment au cas ou
#            if (nbClonesFound < self._nbClones and self._nbFois < 20):
#                self._nbFois += 1
#                print ">>> Attente nb: %i" % self._nbFois
#                PtSetAlarm(1, self, 1)
#            else:
#                PtSetAlarm(1, self, 2)
#        elif param == 2:
#            nbClonesFound = len(dicClones["columnphys"])
#            print ">> nb de clones de %s %i" % ("columnphys", nbClonesFound)
#            if (self._nbFois < 20):
#                print ">> Les clones sont prets."
#                soMaster = PtFindSceneobject("columnphys", age)
#                # Masquons les clones surnumeraires s'il y en a
#                for i in range(0,nbClonesFound - 2):
#                    so = dicClones["columnphys"][i].getSceneObject()
#                    so.draw.netForce(1)
#                    so.draw.enable(0)
#                # Manipulons les clones
#                soTop = dicClones["columnphys"][nbClonesFound - 2].getSceneObject()
#                soBottom = dicClones["columnphys"][nbClonesFound - 1].getSceneObject()
#                pos = soMaster.getLocalToWorld()
#                mrot = ptMatrix44()
#                mrot.rotate(0, math.pi)
#                mscale = ptMatrix44()
#                mscale.makeScaleMat(ptVector3(self._scale, self._scale, self._scale))
#                mtransUp = ptMatrix44()
#                mtransUp.translate(ptVector3(.0, .0, 30))
#                mtransDown = ptMatrix44()
#                mtransDown.translate(ptVector3(.0, .0, -30))
#                soTop.draw.netForce(1)
#                soTop.physics.netForce(1)
#                soBottom.draw.netForce(1)
#                soBottom.physics.netForce(1)
#                soTop.physics.warp(pos * mtransUp * mscale * mrot)
#                soBottom.physics.warp(pos * mtransDown * mscale)
#                soTop.draw.enable(1)
#                soBottom.draw.enable(1)
#                SetFog(style = "10000", start = 0, end = 0, density = 0, r = 0.2, g = 0.2, b = 0.4, cr = 0.4, cg = 0.4, cb = 0.5)
#                ToggleObjects("Fog", False)
#                ToggleObjects("Surface", False)
#                ToggleObjects("Sky", False)
#                ToggleObjects("CameraClouds", False)
#                print ">> Fin."
#            else:
#                print ">> Le clonage prend trop de temps!!"
#            self._nbFois = 0

## Cree une sphere etoilee complete a partir de 2 clones tete-beche de "columnphys" agrandis
#def CreateNightSky(scale=7.5, bOn=True):
#    #global dicClones
#    nb = 2
#    if bOn:
#        # Combien de clones a-t-on deja?
#        nbClones = len(dicClones["columnphys"])
#        print "CreateNightSky : nb de clones de %s ==> %i" % ("columnphys", nbClones)
#        # Ajouter des clones si besoin
#        if nbClones < nb:
#            CloneColumnPhys(nb - nbClones)
#        # Attendre que les clones soient pret et les manipuler
#        PtSetAlarm(1, AlarmWaittingForClones(nb, scale), 1)
#        return "nuit"
#    else:
#        # Retour a la normale
#        for i in range(len(dicClones["columnphys"])):
#            so = dicClones["columnphys"][i].getSceneObject()
#            so.draw.netForce(1)
#            so.draw.enable(0)
#        SetFog(style = "defaulf")
#        #ToggleObjects("Fog", True)
#        #ToggleObject("FogLayerBill", True)
#        ToggleObject("FogLayer", True)
#        ToggleObjects("Surface", True)
#        ToggleObjects("Sky", True)
#        ToggleObjects("CameraClouds", True)
#        return "jour"

#