# -*- coding: utf-8 -*-

from Plasma import *
import YodaClones

"""
    * Yoda's clone commands:

        def DemandeClone(nomDemandeur="", masterKey=None, nbClones=0):
            PtSetAlarm(0.0, InitClonage(nomDemandeur, masterKey, nbClones), 2)

        def RegenereClone(nomDemandeur="", masterKey=None):
            PtSetAlarm(0.0, InitClonage(nomDemandeur, masterKey, nbClones=0), 7)

        def DevalideClone(nomDemandeur="", masterKey=None):
            # *** A EVITER ***
            PtSetAlarm(0.0, InitClonage(nomDemandeur, masterKey, nbClones=0), 8)

        def RenouvelerClone(nomDemandeur ="", masterKey=None, nbClones=0):
             PtSetAlarm(0.0, InitClonage(nomDemandeur, masterKey, nbClones), 9)


    * Quelques objets utilises
        CERTAINS  CLONES NE POSENT AUCUN PROBLEME            à l'arrive comme au depart dans l'age
        ("GreatZeroBeam-RTProj", "city")  Laser
        ("PodSymbolRoot", "Payiferen")     Spiral           et bien d'autres
        CERTAINS CLONES   posent des problemes lorsque l'on quitte l'age ou que l'on devalide les clones 
                                        ces clones sont souvent liés à d'autres objets ou gerés par d'autres animations
        ("BugFlockingEmitTest", "Personal")
        ("FireworkRotater1", "Personal")
        ("FireworkRotater102", "Personal")
        ("FireworkRotater103", "Personal")

    * Liste des demandeurs valides de Yoda : ("Marble", "Spiral", "Laser", "Gasper", "AttObjetSurAvatar", "PosClone", "CdMixologie", "Spark", "AnimationArche")
        => Il faut que j'en utilise d'autres

    # Exemple:
    def RenouvelerClone(self):
        self.On = False
        GestionClones.RenouvelerClone("Spark", self.masterKeySpark1, 5)
        GestionClones.RenouvelerClone("Spark", self.masterKeySpark2, 5)
        GestionClones.RenouvelerClone("Spark", self.masterKeySpark3, 5)

"""


#=========================================
#attacher so1 a so2 : attacher(obj, av) ou l'inverse    
def Attacher(so1, so2, bPhys=False):
    """attacher so1 à so2 : attacher(obj, av) ou l'inverse"""
    so1.physics.netForce(1)
    so1.draw.netForce(1)
    PtAttachObject(so1, so2, 1)

#=========================================
# detacher so1 de so2 : detach(obj, av) ou l'inverse    
def Detacher(so1, so2):
    so1.physics.netForce(1)
    so1.draw.netForce(1)
    PtDetachObject(so1, so2, 1)

#=========================================
#
class WaitAndChangeScale:
    def __init__(self, so=None, scale=ptVector3(1, 1, 1)):
        print "WaitAndChangeScale: init"
        self._scale = scale
        self._so = so
    
    def onAlarm(self, param):
        print "WaitAndChangeScale: onAlarm"
        if isinstance(self._so, ptSceneobject):
            pos = self._so.getLocalToWorld()
            mscale = ptMatrix44()
            mscale.makeScaleMat(self._scale)
            self._so.physics.warp(pos * mscale)
            print "WaitAndChangeScale: done"
        else:
            print "WaitAndChangeScale: not a ptSceneobject"

#=========================================
#
def DoStuff(params=[]):
    print "DoStuff begin"
    
    #Verifions les parametres
    # au moins 5 parametres
    if len(params) > 4:
        print "DoStuff params 4"
        try:
            bAttach = bool(params[4])
        except:
            bAttach = True
    else:
        bAttach = True
    # au moins 4 parametres
    if len(params) > 3:
        print "DoStuff params 3"
        if isinstance(params[3], ptMatrix44):
            pos = params[3]
        else:
            #position par defaut: sur moi
            pos = PtGetLocalAvatar().getLocalToWorld()
    else:
        #position par defaut: sur moi
        pos = PtGetLocalAvatar().getLocalToWorld()
    # au moins 3 parametres
    if len(params) > 2:
        print "DoStuff params 2"
        if isinstance(params[2], ptVector3):
            scale = params[2]
        else:
            print "DoStuff scale is not a ptVector3!"
            scale = ptVector3(1, 1, 1)
    else:
        scale = ptVector3(1, 1, 1)
    # au moins 2 parametres
    if len(params) > 1:
        print "DoStuff params 1"
        try:
            bShow = bool(params[1])
        except:
            bShow = True
    else:
        bShow = True
    # au moins 1 parametre
    if len(params) > 0:
        print "DoStuff params 0"
        masterKey = params[0]
        if not isinstance(masterKey, ptKey):
            print "DoStuff: first paremeter must be a ptKey"
            return 1
    # pas de parametre
    if len(params) == 0:
        print "DoStuff: needs 1, 2, 3 or 4 paremeters"
        return 1
    
    print "DoStuff params ok"
    soMaster = masterKey.getSceneObject()
    print "DoStuff({}, {}, {}, matPos)".format(soMaster.getName(), bShow, scale)
    
    # Manipulons les clones
    cloneKeys = PtFindClones(masterKey)
    if len(cloneKeys) < 1:
        print "DoStuff no clone found!"
    else:
        print "DoStuff : the stuff" 
        ck = cloneKeys[len(cloneKeys) - 1]
        #for ck in cloneKeys:
        soTop = ck.getSceneObject()

        #mscale = ptMatrix44()
        #mscale.makeScaleMat(scale)

        soTop.netForce(1)
        soTop.physics.disable()
        soTop.physics.warp(pos)
        #soTop.physics.warp(pos * mscale)
        print "DoStuff : call WaitAndChangeScale" 
        PtSetAlarm(1, WaitAndChangeScale(soTop, scale), 1)
        if bShow:
            soTop.draw.enable(1)
        else:
            soTop.draw.enable(0)
        if bAttach:
            Attacher(soTop, PtGetLocalAvatar(), bPhys=False)
        else:
            Detacher(soTop, PtGetLocalAvatar())

    print "DoStuff done"
    return 0

#=========================================
# Cree un clone a la position desiree
def Clone1Bille(objName, age, bShow=True, bLoad=True, color="red", scale=ptVector3(1, 1, 1), matPos=None, bAttach=False, fct=DoStuff):
    print "          ** clone1 ** 1 begin"
    msg = "CloneObject.clone1(): "
    nb = 1
    masterkey = None

    try:
        masterkey = PtFindSceneobject(objName, age).getKey()
    except:
        print "{} not found in {}".format(objName, age)
        msg += "{} not found in {}\n".format(objName, age)
    print "          ** clone1 ** 2"
    if isinstance(masterkey, ptKey):
        marbles = PtFindSceneobjects('MarblePhy')
        marblePhysKey = None
        if color == "yellow":
            marblePhysKey = marbles[0].getKey()
        elif color == "white":
            marblePhysKey = marbles[1].getKey()
        elif color == "blue":
            marblePhysKey = marbles[2].getKey()
        else:
            marblePhysKey = marbles[3].getKey()

        if bLoad:
            print "          ** clone1 ** 3 loading"
            
            """ == IL FAUT QUE JE CHANGE CETTE PARTIE POUR UTILISER LES METHODES DE YODA
            # Combien de clones a-t-on deja?
            nbClones = len(PtFindClones(masterkey))
            print "Test : nb de clones de {} ==> {}".format(objName, nbClones)
            # Ajouter des clones si besoin
            if nbClones < nb:
                CloneFactory.CloneObject(objName, age, nb - nbClones)
            # Attendre que les clones soient prets et les manipuler
            PtSetAlarm(1, CloneFactory.AlarmWaittingForClones(objName, age, nb, fct, [marblePhysKey, bShow, scale, matPos, bAttach]), 1)
            """ 
            
            nomAction = "Marble"
            YodaClones.DemandeClone(nomDemandeur=nomAction, masterKey=masterkey, nbClones=nb)
            nbClonesLoaded = len(YodaClones.dicDemandeurs[nomAction][masterkey.getName()])
            
            print "{} clone(s) of {} loaded".format(nbClonesLoaded, objName)
            msg += "{} clone(s) of {} loaded\n".format(nbClonesLoaded, objName)
            
            DoStuff([marblePhysKey, bShow, scale, matPos, bAttach])
        else:
            # Retour a la normale
            """ == IL FAUT QUE JE CHANGE CETTE PARTIE POUR UTILISER LES METHODES DE YODA
            CloneFactory.DechargerClones(masterkey)
            """

            print "Clone of {} unloaded".format(objName)
            msg += "Clone of {} unloaded\n".format(objName)
    else:
        print "not a ptKey!"
        msg += "not a ptKey\n"
    return msg

#=========================================
# Test jouons avec une bille (firemarble)
def Bille(bOnOff=True, x=0, y=0, z=0, bAttacher=False):
    pos = PtGetLocalAvatar().getLocalToWorld()
    mtrans = ptMatrix44()
    mtrans.translate(ptVector3(x, y, z))
    pos = pos * mtrans
    #vScale = ptVector3(10, 10, 200)
    vScale = ptVector3(1, 1, 1)
    vColor = "red"
    Clone1Bille("nb01FireMarbles2VisMaster", "Neighborhood", bShow=bOnOff, bLoad=bOnOff, color=vColor, scale=vScale, matPos=pos, bAttach=bAttacher, fct=DoStuff)

#=========================================

nomAction = "Pumpkin"

#=========================================
#
def DoStuff2(params=[]):
    print "DoStuff2 begin"
    
    #Verifions les parametres
    # au moins 6 parametres
    if len(params) > 5:
        print "DoStuff2 params 4"
        try:
            bAttach = bool(params[5])
        except:
            bAttach = True
    else:
        bAttach = True
    # au moins 5 parametres
    if len(params) > 4:
        print "DoStuff2 params 3"
        if isinstance(params[4], ptMatrix44):
            pos = params[4]
        else:
            #position par defaut: sur moi
            pos = PtGetLocalAvatar().getLocalToWorld()
    else:
        #position par defaut: sur moi
        pos = PtGetLocalAvatar().getLocalToWorld()
    # au moins 4 parametres
    if len(params) > 3:
        print "DoStuff2 params 2"
        if isinstance(params[3], ptVector3):
            scale = params[3]
        else:
            print "DoStuff2 scale is not a ptVector3!"
            scale = ptVector3(1, 1, 1)
    else:
        scale = ptVector3(1, 1, 1)
    # au moins 3 parametres
    if len(params) > 2:
        print "DoStuff2 params 2"
        if isinstance(params[2], int):
            nb = params[2]
        else:
            print "DoStuff2 nb is not an integer!"
            nb = 0
    else:
        scale = ptVector3(1, 1, 1)
    # au moins 2 parametres
    if len(params) > 1:
        print "DoStuff2 params 1"
        try:
            bShow = bool(params[1])
        except:
            bShow = True
    else:
        bShow = True
    # au moins 1 parametre
    if len(params) > 0:
        print "DoStuff2 params 0"
        masterKey = params[0]
        if not isinstance(masterKey, ptKey):
            print "DoStuff2: first paremeter must be a ptKey"
            return 1
    # pas de parametre
    if len(params) == 0:
        print "DoStuff2: needs 1, 2, 3 or 4 paremeters"
        return 1
    
    print "DoStuff2 params ok"
    soMaster = masterKey.getSceneObject()
    print "DoStuff2({}, {}, {}, matPos)".format(soMaster.getName(), bShow, scale)
    
    """ A MODIFIER :
        Il faut recuperer les clones du dictionnaire
    # Manipulons les clones
    cloneKeys = PtFindClones(masterKey)
    if len(cloneKeys) < 1:
        print "DoStuff2 no clone found!"
    else:
        print "DoStuff2 : the stuff" 
        ck = cloneKeys[len(cloneKeys) - 1]
        #for ck in cloneKeys:
        soTop = ck.getSceneObject()

        #mscale = ptMatrix44()
        #mscale.makeScaleMat(scale)

        soTop.netForce(1)
        soTop.physics.disable()
        soTop.physics.warp(pos)
        #soTop.physics.warp(pos * mscale)
        print "DoStuff2 : call WaitAndChangeScale" 
        PtSetAlarm(1, WaitAndChangeScale(soTop, scale), 1)
        if bShow:
            soTop.draw.enable(1)
        else:
            soTop.draw.enable(0)
        if bAttach:
            Attacher(soTop, PtGetLocalAvatar(), bPhys=False)
        else:
            Detacher(soTop, PtGetLocalAvatar())
    """
    #nomAction = "Marble" # A MODIFIER
    cloneKeys = YodaClones.dicDemandeurs[nomAction][masterKey.getName()]
    if len(cloneKeys) < nb:
        print "DoStuff2 no enough clones found!"
    else:
        print "DoStuff2 : the stuff" 
        ck = cloneKeys[nb-1]
        soTop = ck.getSceneObject()
        soTop.netForce(1)
        soTop.physics.disable()
        soTop.physics.warp(pos)

        print "DoStuff2 : call WaitAndChangeScale" 
        PtSetAlarm(1, WaitAndChangeScale(soTop, scale), 1)
        if bShow:
            soTop.draw.enable(1)
        else:
            soTop.draw.enable(0)
        if bAttach:
            Attacher(soTop, PtGetLocalAvatar(), bPhys=False)
        else:
            Detacher(soTop, PtGetLocalAvatar())

    print "DoStuff2 done"
    return 0

#=========================================
#
class WaitAndDoStuff2:
    _nbFois = 0

    def __init__(self, masterkey, bShow, nb, scale, matPos, bAttach):
        print "WaitAndDoStuff2: init"
        self._masterKey = masterkey
        self._bShow = bShow
        self._nb = nb
        self._scale = scale
        self._matPos = matPos
        self._bAttach = bAttach
    
    def onAlarm(self, param):
        print "WaitAndDoStuff2: onAlarm"
        if param == 1:
            print "WaitAndDoStuff2: onAlarm 1"
            if nomAction in YodaClones.dicDemandeurs:
                print "WaitAndDoStuff2: onAlarm 1 a"
                if self._masterKey.getName() in YodaClones.dicDemandeurs[nomAction]:
                    print "WaitAndDoStuff2: onAlarm 1 b"
                    nbClonesLoaded = len(YodaClones.dicDemandeurs[nomAction][self._masterKey.getName()])
                    if (nbClonesLoaded < self._nb and self._nbFois < 20):
                        print "WaitAndDoStuff2: onAlarm 1 c"
                        self._nbFois += 1
                        print ">>> Attente 3 nb: %i" % self._nbFois
                        PtSetAlarm(1, self, 1)
                    else:
                        print "WaitAndDoStuff2: onAlarm 1 c trouve"
                        PtSetAlarm(1, self, 2)
                else:
                    print "WaitAndDoStuff2: onAlarm 1 b non trouve"
                    self._nbFois += 1
                    print ">>> Attente 2 nb: %i" % self._nbFois
                    PtSetAlarm(1, self, 1)
            else:
                print "WaitAndDoStuff2: onAlarm 1 a non trouve"
                self._nbFois += 1
                print ">>> Attente 1 nb: %i" % self._nbFois
                PtSetAlarm(1, self, 1)
        elif param == 2:
            print "WaitAndDoStuff2: onAlarm 2"
            if nomAction in YodaClones.dicDemandeurs:
                print "WaitAndDoStuff2: onAlarm 2 a"
                if self._masterKey.getName() in YodaClones.dicDemandeurs[nomAction]:
                    print "WaitAndDoStuff2: onAlarm 2 b"
                    cloneKeys = YodaClones.dicDemandeurs[nomAction][self._masterKey.getName()]
                    cloneNb = 0
                    for cloneKey in cloneKeys:
                        mtrans = ptMatrix44()
                        mtrans.translate(ptVector3(0, 0, ((cloneNb + 1) * 1.2) - 0.5 ))
                        pos = self._matPos * mtrans
                        DoStuff2([self._masterKey, self._bShow, cloneNb, self._scale, pos, self._bAttach])
                        cloneNb += 1

#=========================================
# Cree un clone a la position desiree
def ClonePumpkin(objName, age, bShow=True, bLoad=True, number=1, scale=ptVector3(1, 1, 1), matPos=None, bAttach=False, fct=DoStuff2):
    print "          ** ClonePumpkin ** 1 begin"
    msg = "CloneObject.ClonePumpkin(): "
    nb = number
    masterkey = None

    try:
        masterkey = PtFindSceneobject(objName, age).getKey()
    except:
        print "{} not found in {}".format(objName, age)
        msg += "{} not found in {}\n".format(objName, age)
    print "          ** ClonePumpkin ** 2"
    if isinstance(masterkey, ptKey):

        if bLoad:
            print "          ** ClonePumpkin ** 3 loading"
            
            #nomAction = "Marble" # A MODIFIER
            YodaClones.DemandeClone(nomDemandeur=nomAction, masterKey=masterkey, nbClones=nb)
            #nbClonesLoaded = len(YodaClones.dicDemandeurs[nomAction][masterkey.getName()])
            
            #print "{} clone(s) of {} loaded".format(nbClonesLoaded, objName)
            #msg += "{} clone(s) of {} loaded\n".format(nbClonesLoaded, objName)
            
            #DoStuff2([masterkey, bShow, nb, scale, matPos, bAttach])
            PtSetAlarm(1, WaitAndDoStuff2(masterkey, bShow, nb, scale, matPos, bAttach), 1)

        else:
            # Retour a la normale
            """ == IL FAUT QUE JE CHANGE CETTE PARTIE POUR UTILISER LES METHODES DE YODA
            CloneFactory.DechargerClones(masterkey)
            """

            print "Clone of {} unloaded".format(objName)
            msg += "Clone of {} unloaded\n".format(objName)
    else:
        print "not a ptKey!"
        msg += "not a ptKey\n"
    return msg

#=========================================
# Test jouons avec une citrouille (Pumpkin01 ou Pumpkin02)
#def Pumpkins(bOnOff=True, nb=1, x=0, y=0, z=0, bAttacher=True):
def Pumpkins():
    bOnOff = True
    nb = 4
    bAttacher=True
    pos = PtGetLocalAvatar().getLocalToWorld()
    """
    mtrans = ptMatrix44()
    mtrans.translate(ptVector3(x, y, z))
    pos = pos * mtrans
    """
    #vScale = ptVector3(10, 10, 200)
    vScale = ptVector3(1, 1, 1)
    ClonePumpkin("Pumpkin01", "Neighborhood", bShow=bOnOff, bLoad=bOnOff, number=nb, scale=vScale, matPos=pos, bAttach=bAttacher, fct=DoStuff2)
    

"""
    # Modifs a faire :
        - demander 3 clones de citrouilles
        - attendre
        - deplacer et attacher les clones crees
    
"""