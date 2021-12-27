# -*- coding: cp1252 -*-

from Plasma import *
import math
import xClonage

# Objet auquel on va attacher les clones de bille
# (tu peux en choisir un autre)
#so = PtFindSceneobject("MarblePhy01", "Neighborhood")
so = None

# J'ai fait du 5x3, donc 15 clones a creer

# Dictionnaire des chiffres:
dicChiffres = {
    "0": [
        [1, 1, 1], 
        [1, 0, 1], 
        [1, 0, 1], 
        [1, 0, 1], 
        [1, 1, 1], 
    ],
    "1": [
        [0, 0, 1], 
        [0, 0, 1], 
        [0, 0, 1], 
        [0, 0, 1], 
        [0, 0, 1], 
    ],
    "2": [
        [1, 1, 1], 
        [0, 0, 1], 
        [1, 1, 1], 
        [1, 0, 0], 
        [1, 1, 1], 
    ],
    "3": [
        [1, 1, 1], 
        [0, 0, 1], 
        [1, 1, 1], 
        [0, 0, 1], 
        [1, 1, 1], 
    ],
    "4": [
        [1, 0, 1], 
        [1, 0, 1], 
        [1, 1, 1], 
        [0, 0, 1], 
        [0, 0, 1], 
    ],
    "5": [
        [1, 1, 1], 
        [1, 0, 0], 
        [1, 1, 1], 
        [0, 0, 1], 
        [1, 1, 1], 
    ],
    "6": [
        [1, 1, 1], 
        [1, 0, 0], 
        [1, 1, 1], 
        [1, 0, 1], 
        [1, 1, 1], 
    ],
    "7": [
        [1, 1, 1], 
        [0, 0, 1], 
        [0, 1, 0], 
        [1, 0, 0], 
        [1, 0, 0], 
    ],
    "8": [
        [1, 1, 1], 
        [1, 0, 1], 
        [1, 1, 1], 
        [1, 0, 1], 
        [1, 1, 1], 
    ],
    "9": [
        [1, 1, 1], 
        [1, 0, 1], 
        [1, 1, 1], 
        [0, 0, 1], 
        [1, 1, 1], 
    ],
    ":": [
        [0, 1, 0], 
        [0, 1, 0], 
        [0, 0, 0], 
        [0, 1, 0], 
        [0, 1, 0], 
    ],
    "X": [
        [1, 0, 1], 
        [1, 0, 1], 
        [0, 1, 0], 
        [1, 0, 1], 
        [1, 0, 1], 
    ]
}


# Dictionnaire des chiffres:
dicLettres5x7 = {
    "A": [
        [0, 1, 1, 1, 0], 
        [1, 0, 0, 0, 1], 
        [1, 0, 0, 0, 1], 
        [1, 1, 1, 1, 1], 
        [1, 0, 0, 0, 1], 
        [1, 0, 0, 0, 1], 
        [1, 0, 0, 0, 1], 
    ],          
    "B": [      
        [1, 1, 1, 1, 0], 
        [1, 0, 0, 0, 1], 
        [1, 0, 0, 0, 1], 
        [1, 1, 1, 1, 0], 
        [1, 0, 0, 0, 1], 
        [1, 0, 0, 0, 1], 
        [1, 1, 1, 1, 0], 
    ],          
    "C": [      
        [0, 1, 1, 1, 0], 
        [1, 0, 0, 0, 1], 
        [1, 0, 0, 0, 0], 
        [1, 0, 0, 0, 0], 
        [1, 0, 0, 0, 0], 
        [1, 0, 0, 0, 1], 
        [0, 1, 1, 1, 0], 
    ],          
    "D": [      
        [1, 1, 1, 1, 0], 
        [1, 0, 0, 0, 1], 
        [1, 0, 0, 0, 1], 
        [1, 0, 0, 0, 1], 
        [1, 0, 0, 0, 1], 
        [1, 0, 0, 0, 1], 
        [1, 1, 1, 1, 0], 
    ],          
    "E": [      
        [1, 1, 1, 1, 1], 
        [1, 0, 0, 0, 0], 
        [1, 0, 0, 0, 0], 
        [1, 1, 1, 1, 0], 
        [1, 0, 0, 0, 0], 
        [1, 0, 0, 0, 0], 
        [1, 1, 1, 1, 1], 
    ],          
    "F": [      
        [1, 1, 1, 1], 
        [1, 0, 0, 0], 
        [1, 0, 0, 0], 
        [1, 1, 1, 0], 
        [1, 0, 0, 0], 
        [1, 0, 0, 0], 
        [1, 0, 0, 0], 
    ],          
    "G": [      
        [0, 1, 1, 0], 
        [1, 0, 0, 1], 
        [1, 0, 0, 0], 
        [1, 0, 1, 1], 
        [1, 0, 0, 1], 
        [1, 0, 0, 1], 
        [0, 1, 1, 0], 
    ],          
    "": [      
        [0, 1, 1, 0], 
        [1, 0, 0, 1], 
        [1, 0, 0, 0], 
        [1, 0, 0, 0], 
        [1, 0, 0, 0], 
        [1, 0, 0, 1], 
        [0, 1, 1, 0], 
    ],          
    "": [      
        [0, 1, 1, 0], 
        [1, 0, 0, 1], 
        [1, 0, 0, 0], 
        [1, 0, 0, 0], 
        [1, 0, 0, 0], 
        [1, 0, 0, 1], 
        [0, 1, 1, 0], 
    ],          
    "": [      
        [0, 1, 1, 0], 
        [1, 0, 0, 1], 
        [1, 0, 0, 0], 
        [1, 0, 0, 0], 
        [1, 0, 0, 0], 
        [1, 0, 0, 1], 
        [0, 1, 1, 0], 
    ],          
    "": [      
        [0, 1, 1, 0], 
        [1, 0, 0, 1], 
        [1, 0, 0, 0], 
        [1, 0, 0, 0], 
        [1, 0, 0, 0], 
        [1, 0, 0, 1], 
        [0, 1, 1, 0], 
    ],          
    "": [      
        [0, 1, 1, 0], 
        [1, 0, 0, 1], 
        [1, 0, 0, 0], 
        [1, 0, 0, 0], 
        [1, 0, 0, 0], 
        [1, 0, 0, 1], 
        [0, 1, 1, 0], 
    ],          
    "": [      
        [0, 1, 1, 0], 
        [1, 0, 0, 1], 
        [1, 0, 0, 0], 
        [1, 0, 0, 0], 
        [1, 0, 0, 0], 
        [1, 0, 0, 1], 
        [0, 1, 1, 0], 
    ],          
    "": [      
        [0, 1, 1, 0], 
        [1, 0, 0, 1], 
        [1, 0, 0, 0], 
        [1, 0, 0, 0], 
        [1, 0, 0, 0], 
        [1, 0, 0, 1], 
        [0, 1, 1, 0], 
    ],          
    "": [      
        [0, 1, 1, 0], 
        [1, 0, 0, 1], 
        [1, 0, 0, 0], 
        [1, 0, 0, 0], 
        [1, 0, 0, 0], 
        [1, 0, 0, 1], 
        [0, 1, 1, 0], 
    ],          
    "": [      
        [0, 1, 1, 0], 
        [1, 0, 0, 1], 
        [1, 0, 0, 0], 
        [1, 0, 0, 0], 
        [1, 0, 0, 0], 
        [1, 0, 0, 1], 
        [0, 1, 1, 0], 
    ],          
    "": [      
        [0, 1, 1, 0], 
        [1, 0, 0, 1], 
        [1, 0, 0, 0], 
        [1, 0, 0, 0], 
        [1, 0, 0, 0], 
        [1, 0, 0, 1], 
        [0, 1, 1, 0], 
    ],          
    "": [      
        [0, 1, 1, 0], 
        [1, 0, 0, 1], 
        [1, 0, 0, 0], 
        [1, 0, 0, 0], 
        [1, 0, 0, 0], 
        [1, 0, 0, 1], 
        [0, 1, 1, 0], 
    ],          
    "": [      
        [0, 1, 1, 0], 
        [1, 0, 0, 1], 
        [1, 0, 0, 0], 
        [1, 0, 0, 0], 
        [1, 0, 0, 0], 
        [1, 0, 0, 1], 
        [0, 1, 1, 0], 
    ],          
    "": [      
        [0, 1, 1, 0], 
        [1, 0, 0, 1], 
        [1, 0, 0, 0], 
        [1, 0, 0, 0], 
        [1, 0, 0, 0], 
        [1, 0, 0, 1], 
        [0, 1, 1, 0], 
    ],          
    "": [      
        [0, 1, 1, 0], 
        [1, 0, 0, 1], 
        [1, 0, 0, 0], 
        [1, 0, 0, 0], 
        [1, 0, 0, 0], 
        [1, 0, 0, 1], 
        [0, 1, 1, 0], 
    ],          
    "": [      
        [0, 1, 1, 0], 
        [1, 0, 0, 1], 
        [1, 0, 0, 0], 
        [1, 0, 0, 0], 
        [1, 0, 0, 0], 
        [1, 0, 0, 1], 
        [0, 1, 1, 0], 
    ],          
    "": [      
        [0, 1, 1, 0], 
        [1, 0, 0, 1], 
        [1, 0, 0, 0], 
        [1, 0, 0, 0], 
        [1, 0, 0, 0], 
        [1, 0, 0, 1], 
        [0, 1, 1, 0], 
    ],          
    "X": [      
        [1, 1, 1, 1], 
        [1, 0, 1, 1], 
        [1, 0, 1, 1], 
        [1, 1, 1, 1], 
        [1, 0, 1, 1], 
        [1, 0, 1, 1], 
        [1, 1, 1, 1], 
    ],          
    "Y": [      
        [1, 1, 1, 1], 
        [1, 0, 1, 1], 
        [1, 0, 1, 1], 
        [1, 1, 1, 1], 
        [1, 0, 1, 1], 
        [1, 0, 1, 1], 
        [1, 1, 1, 1], 
    ],          
    "Z": [      
        [1, 1, 0, 1, 1], 
        [1, 0, 0, 0, 1], 
        [0, 0, 0, 1, 0], 
        [0, 0, 1, 0, 0], 
        [0, 1, 0, 0, 0], 
        [1, 0, 0, 0, 0], 
        [1, 1, 0, 1, 1], 
    ],
}
# Une "matrice" de positionement ressemble a ca:
#element = [
    #[[0, 0, 0], [1, 0, 0], [2, 0, 0]],
    #[[0, 0, 1], [1, 0, 1], [2, 0, 1]],
    #[[0, 0, 2], [1, 0, 2], [2, 0, 2]],
    #[[0, 0, 3], [1, 0, 3], [2, 0, 3]],
    #[[0, 0, 4], [1, 0, 4], [2, 0, 4]]
#]

# matrice de positions des billes pour former les chiffres (orientation en x, z)
# avec choix de l'ecartement des clones de billes
def CreerElement(espacement = 10):
    element = [[[0 for coord in range(3)] for col in range(3)] for row in range(5)]
    y = 0
    z = 0
    for row in range(5):
        x = 0
        for col in range(3):
            print str(row) + ", " +str(col)
            element[row][col][0] = x
            element[row][col][1] = y
            element[row][col][2] = z
            x += espacement
        z += espacement
    return element

# Dessine-moi un mouton...
class Dessiner():
    xClonage.dicClonesPhy
    xClonage.dicClonesDra
    
    _so = None
    _nbClones = 0
    _couleur = "yellow"
    _dist = 3
    _hauteur = 4
    _nbFois = 0
    
    def __init__(self, so, nbClones, couleur, dist, hauteur):
        print "> Dessiner : INIT"
        self._so = so
        self._nbClones = nbClones
        self._couleur = couleur
        self._dist = dist
        self._hauteur = hauteur
        print "> Dessiner : INIT ok"
    
    def onAlarm(self, param):
        print "> Dessiner : onAlarm"
        if param == 1:
            nbClonesFound = len(xClonage.dicClonesPhy[self._couleur])
            print "> Dessiner : nb de clones %s %i" % (self._couleur, nbClonesFound)
            # Attendre que tous les clones soient crees, mais pas indefiniment au cas ou
            if (nbClonesFound < self._nbClones and self._nbFois < 20):
                self._nbFois += 1
                print ">>> Attente nb: %i" % self._nbFois
                PtSetAlarm(1, self, 1)
            else:
                PtSetAlarm(1, self, 2)
        elif param == 2:
            print "> Dessiner : nb de clones %s %i" % (self._couleur, self._nbClones)
            # J'ai fixe l'espacement a 2, peut etre mis en parametre
            element = CreerElement(2)
            
            for row in range(5):
                for col in range(3):
                    i = (row * 3) + col
                    print "> Dessiner : r = %i, c = %i ==> i = %i" % (row, col, i)
                    sop = xClonage.dicClonesPhy[self._couleur][i].getSceneObject()
                    sod = xClonage.dicClonesDra[self._couleur][i].getSceneObject()
                    dx = element[row][col][0] + self._dist
                    dy = element[row][col][1]
                    dz = self._hauteur + 8 - element[row][col][2]
                    sop.physics.netForce(1)
                    sod.draw.netForce(1)
                    xClonage.Attacher(sop, self._so, dx, dy, dz, False)
        else:
            pass
        print "> Dessiner : FIN"

#Permet de creer un element de clones de FireMarbles
def AfficherElement(dist, hauteur, couleur = None, nb = None, av = None):
    #start = time.time()
    xClonage.dicClonesPhy
    #av peut etre n'importe quel scene object ayant des coordonnees
    if av == None:
        av = PtGetLocalAvatar()
    if couleur == None:
        couleur = "yellow"
    if nb == None:
        # Fixe a 15 par defaut pour chiffre en 3x5
        nb = 15

    nbClones = len(xClonage.dicClonesPhy[couleur])
    print "nb de clones %s %i" % (couleur, nbClones)

    #Ajouter des clones si besoin
    if nbClones < nb:
        xClonage.Cloner(nb - nbClones)
    print "> AfficherElement : appel a Dessiner..."
    PtSetAlarm(1, Dessiner(av, nb, couleur, dist, hauteur), 1)
    print "> AfficherElement : FIN"

#
class AlarmAffichage():
    def __init__(self, dist, hauteur, couleur, nb, so):
        self._dist = dist
        self._hauteur = hauteur
        self._couleur = couleur
        self._nbClones = nb
        self._so = so
        self._nbFois = 0

    def onAlarm(self, param):
        if param == 1:
            print "AlarmAffichage onAlarm 1"
            nbClonesFound = len(xClonage.dicClonesPhy[self._couleur])
            # Attendre que tous les clones soient crees, mais pas indefiniment au cas ou
            if (nbClonesFound < self._nbClones and self._nbFois < 20):
                self._nbFois += 1
                print ">>> Attente nb: %i" % self._nbFois
                PtSetAlarm(1, self, 1)
            else:
                PtSetAlarm(1, self, 2)
        elif param == 2:
            print "AlarmAffichage onAlarm 2"
            AfficherElement(self._dist, self._hauteur, self._couleur, self._nbClones, self._so)
        else:
            print "AlarmAffichage onAlarm mauvais param"

# Initialise le panneau de score
def InitScore():
    global so
    ##Charger nb01:
    #PtConsoleNet("Nav.PageInNode %s" % ("nb01") , 1)
    ##il faudrait patienter un peu...
    #so = PtFindSceneobject("MarblePhy01", "Neighborhood")
    ##initialiser les dictionnaires de clonage
    #xClonage.InitDicts()
    ##
    #if so != None:
    #    so.netForce(1)
    #    so.physics.enable(0)
    #    AfficherElement(-8, 7, "yellow", 15, so)
    #    PtSetAlarm (1, AlarmAffichage(0, 7, "white", 15, so), 1)
    #    PtSetAlarm (1, AlarmAffichage(8, 7, "blue", 15, so), 1)
    #else:
    #    pass
    PtSetAlarm(4, AlarmInit(), 1)

#
class AlarmInit():
    def __init__(self):
        self._nbFois = 0
        self._so = None
        #Charger nb01:
        PtConsoleNet("Nav.PageInNode %s" % ("nb01") , 1)
        
    def onAlarm(self, param):
        if param == 1:
            print "AlarmInit onAlarm 1"
            #self._so = PtFindSceneobject("MarblePhy01", "Neighborhood")
            self._so = PtFindSceneobject("GPSGreatZero", "Neighborhood")
            # Attendre que 
            if (self._so == None and self._nbFois < 20):
                self._nbFois += 1
                print ">>> Attente nb: %i" % self._nbFois
                PtSetAlarm(1, self, 1)
            else:
                PtSetAlarm(1, self, 2)
        elif param == 2:
            print "AlarmInit onAlarm 2"
            #initialiser les dictionnaires de clonage
            xClonage.InitDicts()
            #
            if self._so != None:
                global so
                so = self._so
                self._so.netForce(1)
                self._so.physics.enable(0)
                AfficherElement(-8, 7, "yellow", 15, self._so)
                PtSetAlarm (1, AlarmAffichage(0, 7, "white", 15, self._so), 1)
                PtSetAlarm (1, AlarmAffichage(8, 7, "blue", 15, self._so), 1)
            else:
                pass
        else:
            print "AlarmInit onAlarm mauvais param"


# Pour positionner l'afficheur de score
# par defaut SetPosScore(58, -999, 991, 0) : au bord du terrain
# Note : L'orientation a l'initialisation peut changer!
#appelee dans le chat via xKiBot, exemples:
#"move " : toutes les valeurs par defaut (comme j'ai code, l'espace a la fin est obligatoire)
#"move 90" : les valeurs x y et z par defaut, rz = 90 degres
#"move 1 2 3" : rz = 0 par defaut, x=1, y=2, z=3
def SetPosScore(x, y, z, rz):
    global so
    sX = str(x).strip()
    sY = str(y).strip()
    sZ = str(z).strip()
    sRZ = str(rz).strip()
    try:
        float(sX)
    except:
        sX = "58"
    try:
        float(sY)
    except:
        sY = "-999"
    try:
        float(sZ)
    except:
        sZ = "991"
    try:
        float(sRZ)
    except:
        sRZ = "0"
    matRZ = ptMatrix44()
    matRZ.rotate(2, (math.pi * float(sRZ)) / 180)
    matPos = ptMatrix44()
    tupleMatPos = ( (1, 0, 0, float(sX)), 
                    (0, 1, 0, float(sY)), 
                    (0, 0, 1, float(sZ)), 
                    (0, 0, 0, 1)
                    )
    matPos.setData(tupleMatPos)
    so.netForce(1)
    so.physics.warp(matPos * matRZ)
    so.physics.enable(0)
    so.draw.enable(0)

#Met a jour le score
#appelee dans le chat via xKiBot, ex: score 2 4
def SetScore(score1 = 0, score2 = 0):
    sScore1 = str(score1).strip()
    separateur = ":"
    sScore2 = str(score2).strip()
    
    try:
        iScore1 = int(sScore1)
        if iScore1 < 0 or iScore1 > 9:
            sScore1 = "X"
    except:
        sScore1 = "X"
    
    try:
        iScore2 = int(score2)
        if iScore2 < 0 or iScore2 > 9:
            sScore2 = "X"
    except:
        sScore2 = "X"
    
    for row in range(5):
        for col in range(3):
            i = (row * 3) + col
            couleur = "yellow"
            so = xClonage.dicClonesDra[couleur][i].getSceneObject()
            estVisible = dicChiffres[str(sScore1)][row][col]
            so.draw.netForce(1)
            so.draw.enable(estVisible)
            print "> Score: row=%i, col=%i, i=%i, cou=%s, vis=%i" % (row, col, i, couleur, estVisible)
            couleur = "white"
            so = xClonage.dicClonesDra[couleur][i].getSceneObject()
            estVisible = dicChiffres[str(separateur)][row][col]
            so.draw.netForce(1)
            so.draw.enable(estVisible)
            print "> Score: row=%i, col=%i, i=%i, cou=%s, vis=%i" % (row, col, i, couleur, estVisible)
            couleur = "blue"
            so = xClonage.dicClonesDra[couleur][i].getSceneObject()
            estVisible = dicChiffres[str(sScore2)][row][col]
            so.draw.netForce(1)
            so.draw.enable(estVisible)
            print "> Score: row=%i, col=%i, i=%i, cou=%s, vis=%i" % (row, col, i, couleur, estVisible)

#Reprise du script de Michel MBAhnonay.py

class Board:
    def __init__(self, n1, n2):
        self._n1 = n1
        self._n2 = n2
    def onAlarm(self, param = 1):
        print ">> Board onAlarm"
        SetScore(self._n1, self._n2)
        
class AffichageTournant():
    def __init__(self):
        self._running = False
        self._tour = 0
        self._positions = [[-59, -1030, 991, -90], [-59, -1000, 991, -90], [-59, -970, 991, -90],
                           [-30, -946, 991, 0],[30, -946, 991, 0],
                           [59, -970, 991, 90],  [59, -1000, 991, 90], [59, -1030, 991, 90],
                           [30, -1056, 991, 180], [-30, -1056, 991, 180]]
        self._vitesse = 1.0

    def onAlarm(self, param = 1):
        if self._running == True:
            print ">> AffichageTournant onAlarm running (tour=%i) [%i, %i, %i, %i]" % (self._tour, self._positions[self._tour][0], self._positions[self._tour][1], self._positions[self._tour][2], self._positions[self._tour][3])
            SetPosScore(self._positions[self._tour][0], self._positions[self._tour][1], self._positions[self._tour][2], self._positions[self._tour][3])
            self._tour = (self._tour + 1) % len(self._positions)
            PtSetAlarm(self._vitesse,self,1)
        else:
            return
    
    def start(self, vitesse):
        print ">> AffichageTournant start"
        self._running = True
        self._vitesse = vitesse
        self._tour = 3
        PtSetAlarm(7, self, 1)
    
    def stop(self):
        print ">> AffichageTournant stop"
        self._running = False
        PtSetAlarm(0, self, 1)

panneauTournant = AffichageTournant()
scoreActuel = ["0","0"]
poloAdminliste = ["Mister Magic","[x]"]


#FIN!
