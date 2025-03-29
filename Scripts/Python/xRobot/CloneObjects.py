# -*- coding: utf-8 -*-

from Plasma import *
import math
from . import YodaClones

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
        print("WaitAndChangeScale: init")
        self._scale = scale
        self._so = so
    
    def onAlarm(self, param):
        print("WaitAndChangeScale: onAlarm")
        if isinstance(self._so, ptSceneobject):
            pos = self._so.getLocalToWorld()
            mscale = ptMatrix44()
            mscale.makeScaleMat(self._scale)
            self._so.physics.disable()
            self._so.physics.netForce(True)
            self._so.physics.warp(pos * mscale)
            print("WaitAndChangeScale: done")
        else:
            print("WaitAndChangeScale: not a ptSceneobject")

#=========================================
#
def DoStuff(params=[]):
    print("DoStuff begin")
    
    #Verifions les parametres
    # au moins 5 parametres
    if len(params) > 4:
        print("DoStuff params 4")
        try:
            bAttach = bool(params[4])
        except:
            bAttach = True
    else:
        bAttach = True
    # au moins 4 parametres
    if len(params) > 3:
        print("DoStuff params 3")
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
        print("DoStuff params 2")
        if isinstance(params[2], ptVector3):
            scale = params[2]
        else:
            print("DoStuff scale is not a ptVector3!")
            scale = ptVector3(1, 1, 1)
    else:
        scale = ptVector3(1, 1, 1)
    # au moins 2 parametres
    if len(params) > 1:
        print("DoStuff params 1")
        try:
            bShow = bool(params[1])
        except:
            bShow = True
    else:
        bShow = True
    # au moins 1 parametre
    if len(params) > 0:
        print("DoStuff params 0")
        masterKey = params[0]
        if not isinstance(masterKey, ptKey):
            print("DoStuff: first paremeter must be a ptKey")
            return 1
    # pas de parametre
    if len(params) == 0:
        print("DoStuff: needs 1, 2, 3 or 4 paremeters")
        return 1
    
    print("DoStuff params ok")
    soMaster = masterKey.getSceneObject()
    print("DoStuff({}, {}, {}, matPos)".format(soMaster.getName(), bShow, scale))
    
    # Manipulons les clones
    cloneKeys = PtFindClones(masterKey)
    if len(cloneKeys) < 1:
        print("DoStuff no clone found!")
    else:
        print("DoStuff : the stuff") 
        ck = cloneKeys[len(cloneKeys) - 1]
        #for ck in cloneKeys:
        soTop = ck.getSceneObject()

        #mscale = ptMatrix44()
        #mscale.makeScaleMat(scale)

        soTop.netForce(1)
        soTop.physics.disable()
        soTop.physics.warp(pos)
        #soTop.physics.warp(pos * mscale)
        print("DoStuff : call WaitAndChangeScale") 
        PtSetAlarm(1, WaitAndChangeScale(soTop, scale), 1)
        if bShow:
            soTop.draw.enable(1)
        else:
            soTop.draw.enable(0)
        if bAttach:
            Attacher(soTop, PtGetLocalAvatar(), bPhys=False)
        else:
            Detacher(soTop, PtGetLocalAvatar())

    print("DoStuff done")
    return 0

#=========================================
# Cree un clone a la position desiree
def Clone1Bille(objName, age, bShow=True, bLoad=True, color="red", scale=ptVector3(1, 1, 1), matPos=None, bAttach=False, fct=DoStuff):
    print("          ** clone1 ** 1 begin")
    msg = "CloneObject.clone1(): "
    nb = 1
    masterkey = None

    try:
        masterkey = PtFindSceneobject(objName, age).getKey()
    except:
        print("{} not found in {}".format(objName, age))
        msg += "{} not found in {}\n".format(objName, age)
    print("          ** clone1 ** 2")
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
            print("          ** clone1 ** 3 loading")
            
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
            
            print("{} clone(s) of {} loaded".format(nbClonesLoaded, objName))
            msg += "{} clone(s) of {} loaded\n".format(nbClonesLoaded, objName)
            
            DoStuff([marblePhysKey, bShow, scale, matPos, bAttach])
        else:
            # Retour a la normale
            """ == IL FAUT QUE JE CHANGE CETTE PARTIE POUR UTILISER LES METHODES DE YODA
            CloneFactory.DechargerClones(masterkey)
            """

            print("Clone of {} unloaded".format(objName))
            msg += "Clone of {} unloaded\n".format(objName)
    else:
        print("not a ptKey!")
        msg += "not a ptKey\n"
    return msg

#=========================================
# Test jouons avec une bille (firemarble)
def UneBille(bOnOff=True, x=0, y=0, z=0, bAttacher=False):
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
    print("DoStuff2 begin")
    
    #Verifions les parametres
    # au moins 6 parametres
    if len(params) > 5:
        print("DoStuff2 params 4")
        try:
            bAttach = bool(params[5])
        except:
            bAttach = True
    else:
        bAttach = True
    # au moins 5 parametres
    if len(params) > 4:
        print("DoStuff2 params 3")
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
        print("DoStuff2 params 2")
        if isinstance(params[3], ptVector3):
            scale = params[3]
        else:
            print("DoStuff2 scale is not a ptVector3!")
            scale = ptVector3(1, 1, 1)
    else:
        scale = ptVector3(1, 1, 1)
    # au moins 3 parametres
    if len(params) > 2:
        print("DoStuff2 params 2")
        if isinstance(params[2], int):
            nb = params[2]
        else:
            print("DoStuff2 nb is not an integer!")
            nb = 0
    else:
        scale = ptVector3(1, 1, 1)
    # au moins 2 parametres
    if len(params) > 1:
        print("DoStuff2 params 1")
        try:
            bShow = bool(params[1])
        except:
            bShow = True
    else:
        bShow = True
    # au moins 1 parametre
    if len(params) > 0:
        print("DoStuff2 params 0")
        masterKey = params[0]
        if not isinstance(masterKey, ptKey):
            print("DoStuff2: first paremeter must be a ptKey")
            return 1
    # pas de parametre
    if len(params) == 0:
        print("DoStuff2: needs 1, 2, 3 or 4 paremeters")
        return 1
    
    print("DoStuff2 params ok")
    soMaster = masterKey.getSceneObject()
    print("DoStuff2({}, {}, {}, matPos)".format(soMaster.getName(), bShow, scale))
    
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
        print("DoStuff2 no enough clones found!")
    else:
        print("DoStuff2 : the stuff") 
        ck = cloneKeys[nb-1]
        soTop = ck.getSceneObject()
        soTop.netForce(1)
        soTop.physics.disable()
        soTop.physics.warp(pos)

        print("DoStuff2 : call WaitAndChangeScale") 
        PtSetAlarm(1, WaitAndChangeScale(soTop, scale), 1)
        if bShow:
            soTop.draw.enable(1)
        else:
            soTop.draw.enable(0)
        if bAttach:
            Attacher(soTop, PtGetLocalAvatar(), bPhys=False)
        else:
            Detacher(soTop, PtGetLocalAvatar())

    print("DoStuff2 done")
    return 0

#=========================================
#
def DoStuff3(params=[]):
    print("DoStuff3 begin")
    
    #Verifions les parametres
    # au moins 7 parametres
    if len(params) > 6:
        print("DoStuff3 params 6")
        try:
            bAttach = bool(params[6])
        except:
            bAttach = True
    else:
        bAttach = True
    # au moins 6 parametres
    if len(params) > 5:
        print("DoStuff3 params 5")
        if isinstance(params[5], ptMatrix44):
            pos = params[5]
        else:
            #position par defaut: sur moi
            pos = PtGetLocalAvatar().getLocalToWorld()
    else:
        #position par defaut: sur moi
        pos = PtGetLocalAvatar().getLocalToWorld()
    # au moins 5 parametres
    if len(params) > 4:
        print("DoStuff3 params 4")
        if isinstance(params[4], ptVector3):
            scale = params[4]
        else:
            print("DoStuff3 scale is not a ptVector3!")
            scale = ptVector3(1, 1, 1)
    else:
        scale = ptVector3(1, 1, 1)
    # au moins 4 parametres
    if len(params) > 3:
        print("DoStuff3 params 3")
        if isinstance(params[3], int):
            num = params[3]
        else:
            print("DoStuff3 num is not an integer!")
            num = 0
    else:
        scale = ptVector3(1, 1, 1)
    # au moins 3 parametres
    if len(params) > 2:
        print("DoStuff3 params 2")
        if isinstance(params[2], int):
            nb = params[2]
        else:
            print("DoStuff3 nb is not an integer!")
            nb = 0
    else:
        scale = ptVector3(1, 1, 1)
    # au moins 2 parametres
    if len(params) > 1:
        print("DoStuff3 params 1")
        try:
            bShow = bool(params[1])
        except:
            bShow = True
    else:
        bShow = True
    # au moins 1 parametre
    if len(params) > 0:
        print("DoStuff3 params 0")
        masterKey = params[0]
        if not isinstance(masterKey, ptKey):
            print("DoStuff3: first paremeter must be a ptKey")
            return 1
    # pas de parametre
    if len(params) == 0:
        print("DoStuff3: needs 1, 2, 3 or 4 paremeters")
        return 1
    
    print("DoStuff3 params ok")
    soMaster = masterKey.getSceneObject()
    print("DoStuff3({}, {}, {}, matPos)".format(soMaster.getName(), bShow, scale))
    
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
    if len(cloneKeys) < nb or len(cloneKeys) < num:
        print("DoStuff3 no enough clones found!")
    else:
        print("DoStuff3 : the stuff") 
        #ck = cloneKeys[nb-1]
        ck = cloneKeys[num]
        soTop = ck.getSceneObject()
        soTop.netForce(1)
        soTop.physics.disable()
        soTop.physics.warp(pos)
        
        p=soTop.position()
        #print("DoStuff3 : pos=ptVector3(", p.getX(), ",", p.getY(), ",", p.getZ(), ")")
        PtSendKIMessage(26, "DoStuff3 : pos=ptVector3({:.2f}, {:.2f}, {:.2f})".format(p.getX(), p.getY(), p.getZ()))
        #print("DoStuff3 : call WaitAndChangeScale") 
        PtSetAlarm(1, WaitAndChangeScale(soTop, scale), 1)
        if bShow:
            soTop.draw.enable(1)
        else:
            soTop.draw.enable(0)
        if bAttach:
            Attacher(soTop, PtGetLocalAvatar(), bPhys=False)
        else:
            Detacher(soTop, PtGetLocalAvatar())

    print("DoStuff3 done")
    return 0

#=========================================
#
class WaitAndDoStuff2:
    _nbFois = 0

    def __init__(self, masterkey, bShow, nb, scale, matPos, bAttach):
        print("WaitAndDoStuff2: init")
        self._masterKey = masterkey
        self._bShow = bShow
        self._nb = nb
        self._scale = scale
        self._matPos = matPos
        self._bAttach = bAttach
    
    def onAlarm(self, param):
        print("WaitAndDoStuff2: onAlarm")
        if param == 1:
            print("WaitAndDoStuff2: onAlarm 1")
            if nomAction in YodaClones.dicDemandeurs:
                print("WaitAndDoStuff2: onAlarm 1 a")
                if self._masterKey.getName() in YodaClones.dicDemandeurs[nomAction]:
                    print("WaitAndDoStuff2: onAlarm 1 b")
                    nbClonesLoaded = len(YodaClones.dicDemandeurs[nomAction][self._masterKey.getName()])
                    if (nbClonesLoaded < self._nb and self._nbFois < 20):
                        print("WaitAndDoStuff2: onAlarm 1 c")
                        self._nbFois += 1
                        print(">>> Attente 3 nb: %i" % self._nbFois)
                        PtSetAlarm(1, self, 1)
                    else:
                        print("WaitAndDoStuff2: onAlarm 1 c trouve")
                        PtSetAlarm(1, self, 2)
                else:
                    print("WaitAndDoStuff2: onAlarm 1 b non trouve")
                    self._nbFois += 1
                    print(">>> Attente 2 nb: %i" % self._nbFois)
                    PtSetAlarm(1, self, 1)
            else:
                print("WaitAndDoStuff2: onAlarm 1 a non trouve")
                self._nbFois += 1
                print(">>> Attente 1 nb: %i" % self._nbFois)
                PtSetAlarm(1, self, 1)
        elif param == 2:
            print("WaitAndDoStuff2: onAlarm 2")
            if nomAction in YodaClones.dicDemandeurs:
                print("WaitAndDoStuff2: onAlarm 2 a")
                if self._masterKey.getName() in YodaClones.dicDemandeurs[nomAction]:
                    print("WaitAndDoStuff2: onAlarm 2 b")
                    cloneKeys = YodaClones.dicDemandeurs[nomAction][self._masterKey.getName()]
                    cloneNb = 0
                    for cloneKey in cloneKeys:
                        mtrans = ptMatrix44()
                        mtrans.translate(ptVector3(0, 0, ((cloneNb + 1) * 1.2) - 0.5 ))
                        pos = self._matPos * mtrans
                        DoStuff2([self._masterKey, self._bShow, cloneNb, self._scale, pos, self._bAttach])
                        cloneNb += 1

#=========================================
#
class WaitAndDoStuff3:
    _nbFois = 0

    def __init__(self, masterkey, bShow, nb, num, scale, matPos, bAttach):
        print("WaitAndDoStuff3: init")
        self._masterKey = masterkey
        self._bShow = bShow
        self._nb = nb
        self._num = num
        self._scale = scale
        self._matPos = matPos
        self._bAttach = bAttach
    
    def onAlarm(self, param):
        print("WaitAndDoStuff3: onAlarm")
        if param == 1:
            print("WaitAndDoStuff3: onAlarm 1")
            if nomAction in YodaClones.dicDemandeurs:
                print("WaitAndDoStuff3: onAlarm 1 a")
                if self._masterKey.getName() in YodaClones.dicDemandeurs[nomAction]:
                    print("WaitAndDoStuff3: onAlarm 1 b")
                    nbClonesLoaded = len(YodaClones.dicDemandeurs[nomAction][self._masterKey.getName()])
                    if (nbClonesLoaded < self._nb and self._nbFois < 20):
                        print("WaitAndDoStuff3: onAlarm 1 c")
                        self._nbFois += 1
                        print(">>> Attente 3 nb: %i" % self._nbFois)
                        PtSetAlarm(1, self, 1)
                    else:
                        print("WaitAndDoStuff3: onAlarm 1 c trouve")
                        PtSetAlarm(1, self, 2)
                else:
                    print("WaitAndDoStuff3: onAlarm 1 b non trouve")
                    self._nbFois += 1
                    print(">>> Attente 2 nb: %i" % self._nbFois)
                    PtSetAlarm(1, self, 1)
            else:
                print("WaitAndDoStuff3: onAlarm 1 a non trouve")
                self._nbFois += 1
                print(">>> Attente 1 nb: %i" % self._nbFois)
                PtSetAlarm(1, self, 1)
        elif param == 2:
            print("WaitAndDoStuff3: onAlarm 2")
            if nomAction in YodaClones.dicDemandeurs:
                print("WaitAndDoStuff3: onAlarm 2 a")
                if self._masterKey.getName() in YodaClones.dicDemandeurs[nomAction]:
                    print("WaitAndDoStuff3: onAlarm 2 b")
                    cloneKeys = YodaClones.dicDemandeurs[nomAction][self._masterKey.getName()]
                    """
                    cloneNb = 0
                    for cloneKey in cloneKeys:
                        #mtrans = ptMatrix44()
                        #mtrans.translate(ptVector3(0, 0, ((cloneNb + 1) * 1.2) - 0.5 ))
                        #pos = self._matPos * mtrans
                        pos = self._matPos
                        #DoStuff2([self._masterKey, self._bShow, cloneNb, self._scale, pos, self._bAttach])
                        #if self._num >= 0 and self._num < cloneNb:
                        DoStuff3([self._masterKey, self._bShow, cloneNb, self._num, self._scale, pos, self._bAttach])
                        cloneNb += 1
                    """
                    if len(cloneKeys) < self._nb or len(cloneKeys) < self._num:
                        print("WaitAndDoStuff3 no enough clones found!")
                    else:
                        pos = self._matPos
                        DoStuff3([self._masterKey, self._bShow, self._nb, self._num, self._scale, pos, self._bAttach])

#=========================================
# Cree un clone a la position desiree
def ClonePumpkin(objName, age, bShow=True, bLoad=True, number=1, scale=ptVector3(1, 1, 1), matPos=None, bAttach=False, fct=DoStuff2):
    print("          ** ClonePumpkin ** 1 begin")
    msg = "CloneObject.ClonePumpkin(): "
    nb = number
    masterkey = None

    try:
        masterkey = PtFindSceneobject(objName, age).getKey()
    except:
        print("{} not found in {}".format(objName, age))
        msg += "{} not found in {}\n".format(objName, age)
    print("          ** ClonePumpkin ** 2")
    if isinstance(masterkey, ptKey):

        if bLoad:
            print("          ** ClonePumpkin ** 3 loading")
            
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

            print("Clone of {} unloaded".format(objName))
            msg += "Clone of {} unloaded\n".format(objName)
    else:
        print("not a ptKey!")
        msg += "not a ptKey\n"
    return msg

#=========================================
# Cree n clones et en mettre un a la position desiree
def CloneThat(objName, age, bShow=True, bLoad=True, number=1, thisone=0, scale=ptVector3(1, 1, 1), matPos=None, bAttach=False, fct=DoStuff2):
    print("          ** CloneThat ** 1 begin")
    msg = "CloneObject.CloneThat(): "
    nb = number
    num = thisone
    masterkey = None

    try:
        masterkey = PtFindSceneobject(objName, age).getKey()
    except:
        print("{} not found in {}".format(objName, age))
        msg += "{} not found in {}\n".format(objName, age)
    print("          ** CloneThat ** 2")
    if isinstance(masterkey, ptKey):

        if bLoad:
            print("          ** CloneThat ** 3 loading")
            
            #nomAction = "Marble" # A MODIFIER
            YodaClones.DemandeClone(nomDemandeur=nomAction, masterKey=masterkey, nbClones=nb)
            #nbClonesLoaded = len(YodaClones.dicDemandeurs[nomAction][masterkey.getName()])
            
            #print "{} clone(s) of {} loaded".format(nbClonesLoaded, objName)
            #msg += "{} clone(s) of {} loaded\n".format(nbClonesLoaded, objName)
            
            #DoStuff2([masterkey, bShow, nb, scale, matPos, bAttach])
            PtSetAlarm(1, WaitAndDoStuff3(masterkey, bShow, nb, num, scale, matPos, bAttach), 1)

        else:
            # Retour a la normale
            """ == IL FAUT QUE JE CHANGE CETTE PARTIE POUR UTILISER LES METHODES DE YODA
            CloneFactory.DechargerClones(masterkey)
            """

            print("Clone of {} unloaded".format(objName))
            msg += "Clone of {} unloaded\n".format(objName)
    else:
        print("not a ptKey!")
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


#=========================================
# Test DeadBahro ==> NON DEPLACABLE!
def DeadBahro(obj="DeadBahroMeshBody", bOnOff=True, x=0, y=0, z=0, bAttacher=False):
    pos = PtGetLocalAvatar().getLocalToWorld()
    mtrans = ptMatrix44()
    mtrans.translate(ptVector3(x, y, z))
    pos = pos * mtrans
    vScale = ptVector3(1, 1, 1)
    nb = 1
    ClonePumpkin(objName=obj, age="GreatTreePub", bShow=bOnOff, bLoad=bOnOff, number=nb, scale=vScale, matPos=pos, bAttach=bAttacher, fct=DoStuff2)

#=========================================
# Clonage de Bahro1
def Bahro(bOnOff=True, nb=1, num=0, x=0, y=0, z=0, scale=1, bAttacher=False):
    obj="Bahro1"
    pos = PtGetLocalAvatar().getLocalToWorld()
    mtrans = ptMatrix44()
    mtrans.translate(ptVector3(x, y, z))
    pos = pos * mtrans
    vScale = ptVector3(scale, scale, scale)
    #nb = 1
    CloneThat(objName=obj, age="CustomAvatars", bShow=bOnOff, bLoad=bOnOff, number=nb, thisone=num, scale=vScale, matPos=pos, bAttach=bAttacher, fct=DoStuff2)

def PutBahroHere(show=True, load=True, nb=1, num=0, scale=1, pos=None, attach=False):
    if nb > 0 and num >= 0 and num < nb:
        if not isinstance(pos, ptMatrix44):
            pos = ptMatrix44().translate(ptVector3(-10000, -10000, -10000))
        vScale = ptVector3(scale, scale, scale)
        CloneThat(objName="Bahro1", age="CustomAvatars", bShow=show, bLoad=load, number=nb, thisone=num, scale=vScale, matPos=pos, bAttach=attach, fct=DoStuff2)
    else:
        pass

def PutYeeshaGlowHere(show=True, load=True, nb=1, num=0, scale=1, pos=None, attach=False, dx=0, dy=0, dz=0, rx=0, ry=0, rz=0, cr=1, cg=1, cb=1, ca=1):
    if nb > 0 and num >= 0 and num < nb:
        if not isinstance(pos, ptMatrix44):
            pos = ptMatrix44().translate(ptVector3(-10000, -10000, -10000))
        #pos1 = pos
        #pos1.translate(ptVector3(dx, dy, dz))
        pos.translate(ptVector3(dx, dy, dz))
        mRot = ptMatrix44()
        mRot.rotate(0, (math.pi * rx) / 180)
        mRot.rotate(1, (math.pi * ry) / 180)
        mRot.rotate(2, (math.pi * rz) / 180)
        #pos1 = pos1 * mRot
        pos = pos * mRot
        vScale = ptVector3(scale, scale, scale)
        #CloneThat(objName="RTGlowLight", age="CustomAvatars", bShow=show, bLoad=load, number=nb, thisone=num, scale=vScale, matPos=pos1, bAttach=attach, fct=DoStuff2)
        CloneThat(objName="RTGlowLight", age="CustomAvatars", bShow=show, bLoad=load, number=nb, thisone=num, scale=vScale, matPos=pos, bAttach=attach, fct=DoStuff2)
        mso = PtFindSceneobject("RTGlowLight", "CustomAvatars")
        cloneKeys = PtFindClones(mso.getKey())
        if len(cloneKeys) > num:
            ck = cloneKeys[num]
        #for ck in cloneKeys:
            so = ck.getSceneObject()
            so.netForce(True)
            
            #PtSetLightValue(key=ck, name="RTGlowLight", r=cr, g=cg, b=cb, a=ca)
            PtSetLightValue(ck, "RTGlowLight", cr, cg, cb, ca)
    else:
        pass

#=========================================
# Clonage de Billes
def Bille(color="red", bOnOff=True, nb=1, num=0, x=0, y=0, z=0, bAttacher=False):
    ageName = "Neighborhood"
    masterName = "MarblePhy"
    if color.startswith("y"):
        masterName = masterName + "01"
    elif color.startswith("w"):
        masterName = masterName + "02"
    elif color.startswith("b"):
        masterName = masterName + "03"
    else:
        masterName = masterName + "04"
    """
    pos = PtGetLocalAvatar().getLocalToWorld()
    mtrans = ptMatrix44()
    mtrans.translate(ptVector3(x, y, z))
    pos = pos * mtrans
    """
    pos = ptVector3(x, y, z)
    vScale = ptVector3(1, 1, 1)
    #nb = 1
    PtSendKIMessage(26, "Bille : {}, {}, {}".format(color, nb, num))
    CloneThat(objName=masterName, age=ageName, bShow=bOnOff, bLoad=bOnOff, number=nb, thisone=num, scale=vScale, matPos=pos, bAttach=bAttacher, fct=DoStuff2)

# pas bon, trop de clones sont crees et tous vont sur moi!
def xmas():
    #Bille(color="red", bOnOff=True, nb=1, num=0, x=0, y=0, z=0, bAttacher=False)
    Bille("r", True, 8, 0, 530.33, -792.95, 79.02, False)
    Bille("w", True, 8, 0, 529.51, -796.40, 79.01, False)
    Bille("b", True, 8, 0, 528.66, -799.03, 79.01, False)
    Bille("y", True, 8, 0, 526.37, -798.35, 79.28, False)
    Bille("r", True, 8, 1, 522.83, -797.50, 79.28, False)
    Bille("w", True, 8, 1, 519.29, -796.44, 79.28, False)
    Bille("b", True, 8, 1, 513.83, -796.43, 80.40, False)
    Bille("y", True, 8, 1, 510.78, -807.36, 79.67, False)
    Bille("r", True, 8, 2, 514.08, -809.75, 79.21, False)
    Bille("w", True, 8, 2, 517.66, -810.76, 79.21, False)
    Bille("b", True, 8, 2, 515.83, -817.37, 79.22, False)
    Bille("y", True, 8, 2, 513.87, -823.95, 79.22, False)
    Bille("r", True, 8, 3, 511.88, -830.81, 79.22, False)
    Bille("w", True, 8, 3, 510.16, -836.75, 79.22, False)
    Bille("b", True, 8, 3, 508.93, -840.98, 79.22, False)
    Bille("y", True, 8, 3, 505.46, -839.97, 79.22, False)
    Bille("r", True, 8, 4, 535.08, -841.74, 81.36, False)
    Bille("w", True, 8, 4, 531.97, -851.96, 81.36, False)
    Bille("b", True, 8, 4, 532.85, -849.08, 82.36, False)
    Bille("y", True, 8, 4, 534.30, -844.30, 82.36, False)
    Bille("r", True, 8, 5, 533.53, -846.85, 83.36, False)
    Bille("w", True, 8, 5, 537.51, -833.77, 84.37, False)
    Bille("b", True, 8, 5, 539.16, -828.35, 84.37, False)
    Bille("y", True, 8, 5, 537.21, -826.71, 79.36, False)
    Bille("r", True, 8, 6, 536.05, -830.54, 79.36, False)
    Bille("w", True, 8, 6, 534.98, -834.06, 79.36, False)
    Bille("b", True, 8, 6, 541.87, -819.42, 81.36, False)
    Bille("y", True, 8, 6, 544.88, -809.54, 81.36, False)
    Bille("r", True, 8, 7, 544.14, -811.96, 82.37, False)
    Bille("w", True, 8, 7, 542.59, -817.07, 82.37, False)
    Bille("b", True, 8, 7, 543.36, -814.52, 83.03, False)

#
def tldn(nom="shroomie", bOnOff=True, nb=1, num=0, x=0, y=0, z=0, bAttacher=False, scale=1):
    ageName = "Teledahn"
    #masterName = "MarblePhy"
    if nom.startswith("shr"):
        masterName = "LakeShoomieHandle" # marche pas
    elif nom.startswith("b"):
        masterName = "BBRootNode01" # marche pas
    elif nom.startswith("f"):
        # Flapper / Shooter
        #masterName = "ShooterB-Master" # marche pas
        masterName = "Dummy01"
    else:
        masterName = nom
    pos = PtGetLocalAvatar().getLocalToWorld()
    mtrans = ptMatrix44()
    mtrans.translate(ptVector3(x, y, z))
    pos = pos * mtrans
    vScale = ptVector3(scale, scale, scale)
    #nb = 1
    PtSendKIMessage(26, "tldn : {}, {}, {}".format(nom, nb, num))
    CloneThat(objName=masterName, age=ageName, bShow=bOnOff, bLoad=bOnOff, number=nb, thisone=num, scale=vScale, matPos=pos, bAttach=bAttacher, fct=DoStuff2)

#=========================================
# Clonage d'objets
def Clone(ageName="CustomAvatars", obj="Bahro1", bOnOff=True, nb=1, num=0, x=0, y=0, z=0, scale=1, bAttacher=False):
    """
    Clonage d'objets
    Clone(obj="Bahro1", ageName="CustomAvatars", bOnOff=True, nb=1, num=0, x=0, y=0, z=0, scale=1, bAttacher=False):
    A tester:
    age     objet
    Ahnonay Dummy01 (doit cloner quasiment toute la sphere 2) => non, rien n'apparait
    Ahnonay FogInnerBottomLayer => apparait mais a une position fixe
                                ce doit etre pareil pour les autres couches de brume
    AhnonayCathedral    ALRGear03 => pas deplacable mais fait apparaitre une partie de la cathedrale
    BahroCave   CityWater01
    BahroCave   Duster, Duster01 a Duster09 => petites etincelles tombantes
    BahroCave   Flamer, Flamer01 a Flamer05 => petites flames montantes
    BahroCave   Pole_Garden, Pole_GardenBlue, Pole_GardenReturn
                idem Garrison, Kadish, Teledahn
                RTOmniLighFlame, + 01 a 04
                RTomniRed01 a 06
                SmokerUp + 01 a 04
    
    Personal    Yeesha13butterflies
                StLog23
                WedgeMinkata
                KickBoulder +01,02
                
    Teledahn    StarsParticles
                Buggaro 1 : 
                    BBRootNode01, 
                    BBThorax, 
                    BBHead, 
                    BBFrontLegRight, 
                    BBFrontLegLeft, 
                    BBLegsLeft, 
                    BBLegsRight, 
                    BBLWing01, 
                    BBRWing01, 
                    BBTail, 
                    BBClawLeft, 
                    BBClawRight, 
                    BBLWing02, 
                    BBLWing03, 
                    BBRWing02, 
                    BBRWing03, 
                    BBRudder, 
                    
                Buggaro 2 : 
                    BBRootNode02, 
                    BBThorax01, 
                    BBHead01, 
                    BBFrontLegLeft01, 
                    BBFrontLegRight01, 
                    BBLegsLeft01
                    BBLegsRight01, 
                    BBTail01, 
                    BBClawLeft01, 
                    BBClawRight01, 
                    BBLWing04, 
                    BBLWing05, 
                    BBLWing06, 
                    BBRWing04, 
                    BBRWing05, 
                    BBRWing06, 
                    BBRudder01, 
                
    VeeTsah SkyDome => defaut ca ramene quasiment tout l'age...
    
    """
    pos = PtGetLocalAvatar().getLocalToWorld()
    mtrans = ptMatrix44()
    mtrans.translate(ptVector3(x, y, z))
    pos = pos * mtrans
    vScale = ptVector3(scale, scale, scale)
    #nb = 1
    CloneThat(objName=obj, age=ageName, bShow=bOnOff, bLoad=bOnOff, number=nb, thisone=num, scale=vScale, matPos=pos, bAttach=bAttacher, fct=DoStuff2)

#
def CercleH(objname="Duster", age="BahroCave", n=10, scale=1.0, coef=2.0, avCentre=None):
    """
        BahroCave   Duster, Duster01 a Duster09 => petites etincelles tombantes
        BahroCave   Flamer, Flamer01 a Flamer05 => petites flames montantes
        BahroCave   Pole_Garden, Pole_GardenBlue, Pole_GardenReturn
                    idem Garrison, Kadish, Teledahn
                    RTOmniLighFlame, + 01 a 04
                    RTomniRed01 a 06
    """
    if avCentre is None:
        avCentre = PtGetLocalAvatar()
    #agePlayers = GetAllAgePlayers()
    # ne pas tenir compte des robots
    #agePlayers = [pl for pl in PtGetPlayerList() if not(pl.getPlayerID() in list(dicBot.keys()))]
    #n = len(agePlayers)
    i = 0
    print("nb de joueurs: %s" % (n))
    dist = float(coef * n) / (2.0 * math.pi)
    print("distance: %s" % (dist))
    for i in range(n):
        #player = agePlayers[i]
        #avatar = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
        angle = (float(i) * 2.0 * math.pi) / float(n)
        print("angle(%s): %s" % (i, angle))
        dx = float(dist) * math.cos(angle)
        #dx = 0
        dy = float(dist) * math.sin(angle)
        #dy = 0
        #dz = float(dist) * math.sin(angle)
        dz = 0
        #matrix = avCentre.getLocalToWorld()
        #matrix.translate(ptVector3(dx, dy, dz))
        #avatar.netForce(1)
        #avatar.physics.warp(matrix)
        print("x={}, y={}, z={}".format(dx, dy, dz))
        Clone(ageName=age, obj=objname, bOnOff=True, nb=n, num=i, x=dx, y=dy, z=dz, scale=1, bAttacher=False)
