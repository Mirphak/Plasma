# -*- coding: cp1252 -*-

from Plasma import *
import math

#nb01ConesVisMaster
#   OrangeCone01
#   OrangeCone04
#   OrangeCone05
#   OrangeCone11
#   OrangeCone12
#   OrangeCone15
#   OrangeCone16
#   OrangeCone17

#nb01FireMarbles1VisMaster
#   WhiteFiremarble02
#       MarblePhys06
#   WhiteFiremarble03
#       MarblePhys07
#   WhiteFiremarble04
#       MarblePhys08

#nb01FireMarbles2VisMaster
#   BlueFiremarble
#       MarblePhys03
#   RedFiremarble
#       MarblePhys04
#   YellowFiremarble
#       MarblePhys01
#   WhiteFiremarble
#       MarblePhys02

#nb01GardenBugsVisMaster
#   nb01GardenBugsVis-Group

masterKeys = {
"cones":PtFindSceneobject("nb01ConesVisMaster", "Neighborhood").getKey(),
"fm1":PtFindSceneobject("nb01FireMarbles1VisMaster", "Neighborhood").getKey(),
"fm2":PtFindSceneobject("nb01FireMarbles2VisMaster", "Neighborhood").getKey(),
}

#### pour la methode Entourer ####
d = float(0.0)
h = float(0.0)
#av = PtGetLocalAvatar()
nomAgeCourrant = PtGetAgeName()
nomAge = "Neighborhood"
prp = "nb01"


marbles = PtFindSceneobjects('MarblePhy')

dicMarbles = {}
#nb01FireMarbles2VisMaster
dicMarbles.update({'yellow':marbles[0].getKey()})
dicMarbles.update({'white':marbles[1].getKey()})
dicMarbles.update({'blue':marbles[2].getKey()})
dicMarbles.update({'red':marbles[3].getKey()})
#nb01FireMarbles1VisMaster
#dicMarbles.update({'white2':marbles[4].getKey()})
#dicMarbles.update({'white3':marbles[5].getKey()})
#dicMarbles.update({'white4':marbles[6].getKey()})

#
dicClones = {}
dicClones.update({'yellow':[]})
dicClones.update({'white':[]})
dicClones.update({'blue':[]})
dicClones.update({'red':[]})
#dicClones.update({'white2':[]})
#dicClones.update({'white3':[]})
#dicClones.update({'white4':[]})

#lstClones = []

#
dicBadClones = {}
dicBadClones.update({'yellow':[]})
dicBadClones.update({'white':[]})
dicBadClones.update({'blue':[]})
dicBadClones.update({'red':[]})

# reset dicClone
def ResetDicClones():
    global dicClones
    dicClones = {}
    dicClones.update({'yellow':[]})
    dicClones.update({'white':[]})
    dicClones.update({'blue':[]})
    dicClones.update({'red':[]})

# reset the clones
def ResetClones():
    global dicBadClones
    for couleur in dicMarbles.keys():
        key = dicMarbles[couleur]
        dicBadClones[couleur] = PtFindClones(key)
    ResetDicClones()

#class Attendre:
#    def onAlarm(self, etape = 1):
#        print "Attendre ..."


# Unload all the clones
def DechargerClonesBilles():
    masterKey2 = PtFindSceneobject('nb01FireMarbles2VisMaster', 'Neighborhood').getKey()
    cloneKeys = PtFindClones(masterKey2)
    for ck in cloneKeys:
        PtCloneKey(ck, 0)

# Reload all the clones
def RechargerClonesBilles():
    masterKey2 = PtFindSceneobject('nb01FireMarbles2VisMaster', 'Neighborhood').getKey()
    cloneKeys = PtFindClones(masterKey2)
    for ck in cloneKeys:
        PtCloneKey(ck, 1)

# Count the clones
def CompterClonesBilles():
    masterKey2 = PtFindSceneobject('nb01FireMarbles2VisMaster', 'Neighborhood').getKey()
    return len(PtFindClones(masterKey2))


# classe de clonage
class ClonageBilles:
    #_masterKey1 = PtFindSceneobject('nb01FireMarbles1VisMaster', 'Neighborhood').getKey()
    _masterKey2 = PtFindSceneobject('nb01FireMarbles2VisMaster', 'Neighborhood').getKey()
    _nombre = 1
    _delais = 1
    
    def __init__(self, nombre):
        self._nombre = nombre
        self._delais = int(nombre/5) + 1
        print "init ClonageBilles(%i)" % self._nombre

    def ClonerBilles(self, nombre):
        #self._masterKey
        #clonage general (n billes de chaque couleur)
        for i in range(nombre):
            #PtCloneKey(self._masterKey1, 1)
            PtCloneKey(self._masterKey2, 1)

    def onAlarm (self, param):
        if param == 1:
            #print "clonage en cours..."
            self.ClonerBilles(self._nombre)
            PtSetAlarm(self._delais, self, 2)
        elif param == 2:
            #n = len(PtFindClones(self._masterKey2))
            #print "sauvegarde des %i clones..." % n
            self.sauver()
        else:
            #print "param incorrect"
            pass
        
    def sauver(self):
        global dicMarbles
        global dicClones
        for couleur in dicMarbles.keys():
            key = dicMarbles[couleur]
            print couleur + " " + str(len(PtFindClones(key)))
            #dicClones[couleur] = PtFindClones(key)
            dicClones[couleur] = filter(lambda k: k not in dicBadClones[couleur], PtFindClones(key))
            print couleur + " " + str(len(dicClones[couleur])) + " " + str(len(dicBadClones[couleur]))

#
def Cloner(nombre):
    PtSetAlarm(0, ClonageBilles(nombre), 1)

#def cloner(key, n):
#    global lstClones
#    for i in range(n):
#        PtCloneKey(key, 1)
#    lstClones = PtFindClones(key)

#position du point d'arrivee par defaut
def PositionDefaut():
    o = PtFindSceneobject('LinkInPointDefault', PtGetAgeName())
    p = o.getLocalToWorld()
    return p

#deplacer 
def Deplacer(so1, so2, dx = 0, dy = 0, dz = 0, bPhys = True):
    """Deplacer le Sceneobject so1 vers so2 + options: decalage et physique"""
    pos2 = so2.getLocalToWorld()
    vect = ptVector3(dx, dy, dz)
    pos2.translate(vect)
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
def DetacherEtWD(so1, so2):
    so1.physics.netForce(1)
    so1.draw.netForce(1)
    PtDetachObject(so1, so2, 1)
    so1.physics.warp(PositionDefaut())
    #PtSetAlarm(1, Attendre(), 1)
    so1.physics.enable()
    so1.physics.netForce(1)
    so1.draw.netForce(1)

# detacher so1 de so2 : detach(obj, av) ou l'inverse    
def Detacher(so1, so2):
    so1.physics.netForce(1)
    so1.draw.netForce(1)
    PtDetachObject(so1, so2, 1)

# detacher so1 de so2 : detach(obj, av) ou l'inverse    
def Detacher2(so1, so2, dz):
    so1.physics.netForce(1)
    so1.draw.netForce(1)
    so1.draw.enable(1)
    PtDetachObject(so1, so2, 1)
    Deplacer(so1, so2, 0, 0, dz, True)
    #so1.physics.enable()
    #so1.physics.netForce(1)
    #so1.draw.netForce(1)

#return map(lambda k:k.getsceneobjcet(), PtFindClones(PtFindSceneobjects(oname, age).getKey()))

#Permet de faire un cercle de clones de FireMarbles qui suit un avatar
def Entourer(dist, hauteur, couleur = None, nb = None, av = None, bOn = True):
    global dicMarbles
    #global lstClones
    global dicClones
    if av == None:
        av = PtGetLocalAvatar()
    if couleur == None:
        couleur = 'yellow'
    if nb == None:
        nb = len(dicClones[couleur])
    d = dist
    h = hauteur
    nbClones = len(dicClones[couleur])
    nbBadClones = len(dicBadClones[couleur])
    
    #Les clones n'existent peut-etre plus
    nbClonesFound = CompterClonesBilles() - nbBadClones
    if nbClonesFound < nbClones:
        nbClones = nbClonesFound
    
    #print "nb de clones %s %i" % (couleur, nbClones)
    if bOn:
        #Ajouter des clones si besoin
        if nbClones < nb:
            #Cloner(dicMarbles[couleur], nb - len(lstClones))
            Cloner(nb - nbClones)
            #lstClones = dicClones[couleur]
        #    nbClones = len(dicClones[couleur])
        #if nbClones < nb:
        #    nb = nbClones
        ##print "nb de clones %s %i" % (couleur, nbClones)
        #for i in range(nb):
        #    #so = PtFindSceneobject(self.lst[i], self.nomAge)
        #    so = dicClones[couleur][i].getSceneObject()
        #    angle = (float(i)*2.0*math.pi)/float(nb)
        #    dx = dist*math.cos(angle)
        #    dy = dist*math.sin(angle)
        #    so.physics.netForce(1)
        #    so.draw.netForce(1)
        #    Attacher(so, av, dx, dy, hauteur, False)
        print "> Entourer : I will draw..."
        PtSetAlarm(int(nb/5) + 2, Draw(av, nb, couleur, dist, hauteur), 1)
        print "> Entourer : FIN"
    else:
        #self.running = False
        #for i in range(nb):
        #    #so = PtFindSceneobject(self.lst[i], self.nomAge)
        #    so = dicClones[couleur][i].getSceneObject()
        #    #DetacherEtWD(so, av)
        #    Detacher2(so, av, 5)
        for k in dicClones[couleur]:
            so = k.getSceneObject()
            Detacher2(so, av, 5)

#
class Draw():
    global dicClones
    global lstPositions
    _avatar = None
    _nbClones = 0
    _couleur = 'jaune'
    _dist = 3
    _hauteur = 4
    
    def __init__(self, avatar, nbClones, couleur, dist, hauteur):
        print "> Draw : INIT"
        self._avatar = avatar
        self._nbClones = nbClones
        self._couleur = couleur
        self._dist = dist
        self._hauteur = hauteur
    
    def onAlarm(self, param):
        #for i in range(self._nbClones):
        #    key = dicClones[self._couleur][i]
        #    so = key.getSceneObject()
        #    so.physics.netForce(1)
        #    so.draw.netForce(1)
        #    so.physics.disable()
        #    so.physics.warp(lstPositions[i])
        #print "la figure est creee"
        #
        #print "> Draw : onAlarm"
        nbClonesFound = len(dicClones[self._couleur])
        print "> Draw : nb de clones %s %i" % (self._couleur, nbClonesFound)
        if nbClonesFound < self._nbClones:
            self._nbClones = nbClonesFound
        print "> Draw : nb de clones %s %i" % (self._couleur, self._nbClones)
        for i in range(self._nbClones):
            print "> Draw : i = %i" % (i)
            try:
                so = dicClones[self._couleur][i].getSceneObject()
                angle = (float(i)*2.0*math.pi)/float(self._nbClones)
                dx = self._dist*math.cos(angle)
                dy = self._dist*math.sin(angle)
                so.physics.netForce(1)
                so.draw.netForce(1)
                so.draw.enable(1)
                Attacher(so, self._avatar, dx, dy, self._hauteur, False)
            except AttributeError:
                print "> Draw : AttributeError : {}, {}".format(dicClones[self._couleur][i], type(dicClones[self._couleur][i]))
        print "> Draw : FIN"
        # recharger les clones dans certains cas ils ne sont plus visibles
        RechargerClonesBilles()

#
def AddPrp():
    #global bCleftAdded
    pages = ["nb01"]
    for page in pages:
        PtConsoleNet("Nav.PageInNode %s" % (page) , 1)
    #bCleftAdded = True

#
class AlarmAddPrp:
    def onAlarm(self, context):
        AddPrp()
#
#class AlarmEnableAll:
#    def onAlarm(self, context = 0):
#        EnableAll(context)

#
def AddHood(self, args = []):
    self.chatMgr.AddChatLine(None, "Adding Hood...", 3)
    try:
        PtSetAlarm (1, AlarmAddPrp(), 0)
        #PtSetAlarm(5, AlarmEnableAll(), 0)
        self.chatMgr.AddChatLine(None, "Hood added!", 3)
        return 1
    except:
        self.chatMgr.AddChatLine(None, "Error while adding Hood.", 3)
        return 0
