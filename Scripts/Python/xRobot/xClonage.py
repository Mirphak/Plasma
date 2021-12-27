# -*- coding: cp1252 -*-

from Plasma import *

nomAge = "Neighborhood"
master = "nb01FireMarbles2VisMaster"

# Partie physics des billes
dicMarblesPhy = {}
# Partie draw des billes
dicMarblesDra = {}

# Init dict
def InitDicts():
    marblesPhys = PtFindSceneobjects('MarblePhy')
    dicMarblesPhy.update({'yellow':marblesPhys[0].getKey()})
    dicMarblesPhy.update({'white':marblesPhys[1].getKey()})
    dicMarblesPhy.update({'blue':marblesPhys[2].getKey()})
    dicMarblesPhy.update({'red':marblesPhys[3].getKey()})

    dicMarblesDra.update({'yellow':PtFindSceneobject("YellowMarble", nomAge).getKey()})
    dicMarblesDra.update({'white':PtFindSceneobject("WhiteMarble04", nomAge).getKey()})
    dicMarblesDra.update({'blue':PtFindSceneobject("BlueMarble", nomAge).getKey()})
    dicMarblesDra.update({'red':PtFindSceneobject("RedMarble", nomAge).getKey()})

# Dictionnaire des clones (physics)
dicClonesPhy = {}
dicClonesPhy.update({'yellow':[]})
dicClonesPhy.update({'white':[]})
dicClonesPhy.update({'blue':[]})
dicClonesPhy.update({'red':[]})

# Dictionnaire des clones (draw)
dicClonesDra = {}
dicClonesDra.update({'yellow':[]})
dicClonesDra.update({'white':[]})
dicClonesDra.update({'blue':[]})
dicClonesDra.update({'red':[]})


# Classe de clonage
class ClonageBilles:
    _masterKey2 = PtFindSceneobject(master, nomAge).getKey()
    _nombre = 1
    _delais = 1

    # Initialisation
    def __init__(self, nombre):
        self._nombre = nombre
        self._delais = 1
        print "init ClonageBilles(%i)" % self._nombre

    # Clonage general (n billes de chaque couleur)
    def ClonerBilles(self, nombre):
        for i in range(nombre):
            PtCloneKey(self._masterKey2, 1)

    # Prenons notre temps...
    def onAlarm (self, param):
        if param == 1:
            # partie 1 : clonage
            print "clonage en cours..."
            self.ClonerBilles(self._nombre)
            PtSetAlarm(self._delais, self, 2)
        elif param == 2:
            # partie 2 : sauvegarde des clones
            n = len(PtFindClones(self._masterKey2))
            # attendre que tous les clones soient crees
            if n < self._nombre:
                print "%i clones trouves sur les %i demandes!" % (n, self._nombre)
                PtSetAlarm(self._delais, self, 2)
            else:
                print "sauvegarde des %i clones..." % n
                self.sauver()
        else:
            print "ClonageBilles.onAlarm : param incorrect"

    # Sauvons les clones!
    def sauver(self):
        global dicMarblesPhy
        global dicMarblesDra
        global dicClonesPhy
        global dicClonesDra
        for couleur in dicMarblesPhy.keys():
            keyPhy = dicMarblesPhy[couleur]
            keyDra = dicMarblesDra[couleur]
            print couleur + " clones " + str(len(PtFindClones(keyPhy)))
            dicClonesPhy[couleur] = PtFindClones(keyPhy)
            dicClonesDra[couleur] = PtFindClones(keyDra)
            print couleur + " phy " + str(len(dicClonesPhy[couleur]))
            print couleur + " dra " + str(len(dicClonesDra[couleur]))

# Appelee dans xScore pour creer les clones dont on a besoin
def Cloner(nombre):
    print "Cloner(" + str(nombre) + ")"
    PtSetAlarm(1, ClonageBilles(nombre), 1)


# methodes complementaires utiles (ou pas)

## Methode de deplacement basique 
#def Deplacer(so1, so2, dx = 0, dy = 0, dz = 0, bPhys = True):
#    """Deplacer le Sceneobject so1 vers so2 + options: decalage et physique"""
#    pos2 = so2.getLocalToWorld()
#    vect = ptVector3(dx, dy, dz)
#    pos2.translate(vect)
#    so1.netForce(True)
#    so1.physics.warp(pos2)
#    if bPhys:
#        so1.physics.enable()
#    else:
#        so1.physics.disable()

# Methode de deplacement V2 
def Deplacer(so1, so2, dx = 0, dy = 0, dz = 0, bPhys = True):
    """Deplacer le Sceneobject so1 vers so2 + options: decalage et physique"""
    pos2 = so2.getLocalToWorld()
    #vect = ptVector3(dx, dy, dz)
    #pos2.translate(vect)
    tpos2 = pos2.getData()
    x = tpos2[0][3] + dx
    y = tpos2[1][3] + dy
    z = tpos2[2][3] + dz
    tpos2 = ((tpos2[0][0], tpos2[0][1], tpos2[0][2], x), 
            (tpos2[1][0], tpos2[1][1], tpos2[1][2], y), 
            (tpos2[2][0], tpos2[2][1], tpos2[2][2], z), 
            (tpos2[3][0], tpos2[3][1], tpos2[3][2], tpos2[3][3]))
    pos2.setData(tpos2)
    so1.netForce(True)
    so1.physics.warp(pos2)
    if bPhys:
        so1.physics.enable()
    else:
        so1.physics.disable()

#attacher so1 a so2 : attacher(obj, av) ou l'inverse    
def Attacher(so1, so2, dx = 0, dy = 0, dz = 0, bPhys = False):
    """attacher so1 à so2 : attacher(obj, av) ou l'inverse"""
    so1.physics.netForce(1)
    so1.draw.netForce(1)
    Deplacer(so1, so2, dx, dy, dz, bPhys)
    PtAttachObject(so1, so2, 1)

# detacher so1 de so2 : detach(obj, av) ou l'inverse    
def Detacher(so1, so2):
    #so1.physics.netForce(1)
    #so1.draw.netForce(1)
    PtDetachObject(so1, so2, 1)
    #so1.physics.warp(PositionDefaut())
    #so1.physics.enable()
    #so1.physics.netForce(1)
    #so1.draw.netForce(1)

#
def nbClones():
    print str(len(PtFindClones(dicMarblesPhy["red"])))
    print str(len(dicClonesPhy["red"]))
    print str(len(dicClonesDra["red"]))
