# -*- coding: utf-8 -*-
# == Script pour generer un clone d'objet au choix ==
# Mirphak 2013-12-15 version 3

from Plasma import *
import CloneFactory

#Liste d'objets interessants

#=========================================
#
def PutAndShow(params=[]):
    print "PutAndShow begin"
    
    #Verifions les parametres
    # au moins 3 parametres
    if len(params) > 3:
        print "PutAndShow params 3"
        if isinstance(params[3], int):
            h = params[3]
        else:
            #hauteur par defaut
            h = 10
    else:
        #heurteur par defaut
        h = 10
    # au moins 2 parametres
    if len(params) > 2:
        print "PutAndShow params 2"
        if isinstance(params[2], ptMatrix44):
            pos = params[2]
        else:
            #position par defaut: sur moi
            pos = PtGetLocalAvatar().getLocalToWorld()
    else:
        #position par defaut: sur moi
        pos = PtGetLocalAvatar().getLocalToWorld()
    if len(params) > 1:
        try:
            bShow = bool(params[1])
        except:
            bShow = True
    else:
        bShow = True
    if len(params) > 0:
        masterKey = params[0]
        if not isinstance(masterKey, ptKey):
            print "PutAndShow: first paremeter must be a ptKey"
            return 0
    if len(params) == 0:
        print "PutAndShow: needs 1 or 2 paremeters"
        return 0
    
    print "PutAndShow params ok"
    soMaster = masterKey.getSceneObject()
    print "PutAndShow({}, {})".format(soMaster.getName(), bShow)
    
    # Manipulons les clones
    cloneKeys = PtFindClones(masterKey)
    if len(cloneKeys) < 1:
        print "PutAndShow no clone found!"
    #h = 100
    for ck in cloneKeys:
        so = ck.getSceneObject()
        #pos = PtGetLocalAvatar().getLocalToWorld()
        mtransUp = ptMatrix44()
        mtransUp.translate(ptVector3(.0, .0, h))
        so.netForce(1)
        so.physics.warp(pos * mtransUp)
        if bShow:
            so.draw.enable(1)
        else:
            so.draw.enable(0)
        so.physics.enable(1)
        h = h + 5

    print "PutAndShow done"
    return 1


#=========================================
# Cree des clones V1
def CloneObjectList(lstObj, age, nb, bShow=True, bLoad=True, matPos=None):
    
    h = 10
    msg = "DropObjects.CloneObjectList(): "
    masterkey = None
    for obj in lstObj:
        try:
            masterkey = PtFindSceneobject(obj, age).getKey()
        except:
            print "{} not found in {}".format(obj, age)
            msg += "{} not found in {}\n".format(obj, age)
        if isinstance(masterkey, ptKey):
            if bLoad:
                # Combien de clones a-t-on deja?
                nbClones = len(PtFindClones(masterkey))
                print "Test : nb de clones de {} ==> {}".format(obj, nbClones)
                # Ajouter des clones si besoin
                if nbClones < nb:
                    CloneFactory.CloneObject(obj, age, nb - nbClones)
                # Attendre que les clones soient prets et les manipuler
                PtSetAlarm(1, CloneFactory.AlarmWaittingForClones(obj, age, nb, PutAndShow, [masterkey, bShow, matPos, h]), 1)
                h = h + (nb * 5)
                print "Clone of {} loaded".format(obj)
                msg += "Clone of {} loaded\n".format(obj)
            else:
                # Retour a la normale
                CloneFactory.DechargerClones(masterkey)
                #DayTime()
                print "Clone of {} unloaded".format(obj)
                msg += "Clone of {} unloaded\n".format(obj)
        else:
            print "not a ptKey!"
            msg += "not a ptKey\n"

    return msg


# =========
#
def Drop(position=None):
    # verifying parameters:
    bOn = True
    
    # position
    if isinstance(position, ptPoint3):
        px = position.getX()
        py = position.getY()
        pz = position.getZ()
    elif isinstance(position, ptMatrix44):
        tuplePos=position.getData()
        px=tuplePos[0][3]
        py=tuplePos[1][3]
        pz=tuplePos[2][3]
    elif position is None:
        pos = PtGetLocalAvatar().position()
        px=pos.getX()
        py=pos.getY()
        pz=pos.getZ()
    else:
        print "Drop Error: position must be an int or a ptPoint3 or a ptMatrix44"
        return

    # parameters are set, we can continue
    tuplePos = ((1,0,0,px),(0,1,0,py),(0,0,1,pz),(0,0,0,1))
    mPos = ptMatrix44()
    mPos.setData(tuplePos)
    
    #objects = ["OrangeCone01"
        #, "OrangeCone04"
        #, "OrangeCone05"
        #, "OrangeCone11"
        #, "OrangeCone12"
        #, "OrangeCone15"
        #, "OrangeCone16"
        #, "OrangeCone17"]

    #CloneObjectList(lstObj=objects, age="Neighborhood", nb=3, bShow=bOn, bLoad=bOn, matPos=mPos)
    
    #objects = ["KickBoulder", "KickBoulder01", "KickBoulder02"]
    objects = ["StLog23"]
    CloneObjectList(lstObj=objects, age="Personal", nb=5, bShow=bOn, bLoad=bOn, matPos=mPos)
    
    #"Skull01", "Skull02"
    #"RollingRock01", "RollingRock02", "RollingRock03", "RollingRock04", "RollingRock05", "RollingRock06", "RollingRock07", "RollingRock08", "RollingRock09", "RollingRock10"
    #"Bone-C-17", "Bone-C-18", "Bone-Q-12"
    #"Basket01", "Basket02"
    #objects = ["Skull02", "RollingRock02", "Bone-Q-12", "Basket02"]
    #CloneObjectList(lstObj=objects, age="Teledahn", nb=2, bShow=bOn, bLoad=bOn, matPos=mPos)

    #objects = ["Pebble301", "Stick01"]
    #CloneObjectList(lstObj=objects, age="philRelto", nb=4, bShow=bOn, bLoad=bOn, matPos=mPos)

    #objects = ["RedLeaf00"]
    #CloneObjectList(lstObj=objects, age="Kadish", nb=4, bShow=bOn, bLoad=bOn, matPos=mPos)

    #objects = ["SoccerBall"]
    #CloneObjectList(lstObj=objects, age="Minkata", nb=4, bShow=bOn, bLoad=bOn, matPos=mPos)

    #objects = ["Basket01", "Basket02", "Basket03"]
    #CloneObjectList(lstObj=objects, age="Gira", nb=2, bShow=bOn, bLoad=bOn, matPos=mPos)

# == FIN ==