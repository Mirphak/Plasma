# -*- coding: cp1252 -*-

"""Scripts pour teleport avatars Uru Live
Michel Lacoste
-----Septembre 212------"""

from Plasma import *
import ast
import string
import os
import errno

#*****************************#
# Sauvegarde et restauration  #
#     colonnes de Jalak       #
#*****************************#
sdlColumns = [  "jlakColumn00","jlakColumn01","jlakColumn02","jlakColumn03","jlakColumn04",\
                "jlakColumn05","jlakColumn06","jlakColumn07","jlakColumn08","jlakColumn09",\
                "jlakColumn10","jlakColumn11","jlakColumn12","jlakColumn13","jlakColumn14",\
                "jlakColumn15","jlakColumn16","jlakColumn17","jlakColumn18","jlakColumn19",\
                "jlakColumn20","jlakColumn21","jlakColumn22","jlakColumn23","jlakColumn24"]


def SaveColumns(nomfichier,nomavatar):
    if PtGetAgeName() == 'Jalak':
        byteColumns = []
        ageSDL = PtGetAgeSDL()
        for sdl in sdlColumns:
            val = ageSDL[sdl][0]
            byteColumns.append(val)
        
        #nomfichier = nomfichier + Avatars.Nomsimplifie(nomavatar) + ".txt"
        nomfichier = nomfichier + "_" + nomavatar + ".txt"
        repertoire = "jeux/Jcolonnes/"
        chemin = repertoire+nomfichier
        try:
            os.makedirs(repertoire)
        except OSError as e:
            if not(e.errno==errno.EEXIST and os.path.isdir(repertoire)):
                raise
        fWrite = file(chemin,'w')
        i = 0
        for pos in byteColumns:
            fWrite.write(str(pos)+"\n")
            i += 1
        fWrite.close()
        PtSendKIMessage(26,"Position des colonnes sauvegardee en %s"% (chemin))
        return 1
    else:
        PtSendKIMessage(26,"You are not in Jalak !")
        return 0

def LoadColumns(nomfichier,nomavatar): 
    #nomfichier = nomfichier + Avatars.Nomsimplifie(nomavatar) + ".txt"
    nomfichier = nomfichier + "_" + nomavatar + ".txt"
    repertoire = "jeux/Jcolonnes/"
    chemin = repertoire + nomfichier
    try:
        os.makedirs(repertoire)
    except OSError as e:
        if not(e.errno==errno.EEXIST and os.path.isdir(repertoire)):
            raise
    try:
        fRead = file(chemin,'r')
    except:
        print "ERROR!  File '%s' not found, load canceled." % (chemin)
        return 0
    preset = []
    i = 0
    for line in fRead:
        pos = string.atoi(line)
        if pos < 0 or pos > 19:
            print "ERROR!  Column %d has an invalid position of %d, must be an integer between 0 and 19.  Load canceled." % (i,pos)
            fRead.close()
            return -1
        else:
            preset.append(pos)
        i += 1
    if len(preset) != 25:
        print "ERROR!  File contains %d positions, must contain positions for 25 columns, only.  Load canceled." % (len(preset))
        return -2
    else:
        PtSendKIMessage(26,"Reading file '%s', preset Jalak's columns"% (chemin))    	
    fRead.close()
    maxDeltaHauteur = 0
    ageSDL = PtGetAgeSDL()
    i = 0
    for col in sdlColumns:
        oldVal = ageSDL[col][0]
        newVal = preset[i]
        delta = abs(oldVal - newVal)
        maxDeltaHauteur = max(maxDeltaHauteur, delta)
        ageSDL[col] = (preset[i],)
        i += 1
    return maxDeltaHauteur

#*****************************#
# Sauvegarde et restauration  #
#     cubes de Jalak          #
#*****************************#
cubes = ['BigBox0','BigBox1','BigBox2','BigBox3','BigBox4',
             'Ramp0','Ramp1','Ramp2','Ramp3','Ramp4',
             'LilBox0','LilBox1','LilBox2','LilBox3','LilBox4',
             'Rect0','Rect1','Rect2','Rect3','Rect4',
             'Sphere0','Sphere1','Sphere2','Sphere3','Sphere4']
warpcubes = ['BigBox0Warp','BigBox1Warp','BigBox2Warp','BigBox3Warp','BigBox4Warp',
             'Ramp0Warp','Ramp1Warp','Ramp2Warp','Ramp3Warp','Ramp4Warp',
             'LilBox0Warp','LilBox1Warp','LilBox2Warp','LilBox3Warp','LilBox4Warp',
             'Rect0Warp','Rect1Warp','Rect2Warp','Rect3Warp','Rect4Warp',
             'Sphere0Warp','Sphere1Warp','Sphere2Warp','Sphere3Warp','Sphere4Warp']

def SaveCubes(nomfichier,nomavatar):
    #nomfichier = nomfichier + Avatars.Nomsimplifie(nomavatar) + ".txt"
    nomfichier = nomfichier + "_" + nomavatar + ".txt"
    repertoire = "jeux/Jcubes/"
    chemin = repertoire + nomfichier
    try:
        os.makedirs(repertoire)
    except OSError as e:
        if not(e.errno==errno.EEXIST and os.path.isdir(repertoire)):
            raise
    fWrite = file(chemin,'w')
    fWrite.write(nomfichier+'\n')
    for cc in cubes:
        SObjet = PtFindSceneobject(cc, 'Jalak')
        matrix = SObjet.getLocalToWorld()
        data = matrix.getData()
        if cc == 'Sphere4':
            finale = ''
        else:
            finale = '\n'
        fWrite.write("%s%s"%(data,finale))
    fWrite.close()
    PtSendKIMessage(26,"Position des Cubes sauvegardee en %s"% (chemin))

def FichierDisque(repertoire, nomfichier):
    #nomfichier = nomfichier + "_" + nomavatar + ".txt"
    #repertoire = "jeux/Jcubes/"
    chemin = repertoire + nomfichier
    #try:
    #    os.makedirs(repertoire)
    #except OSError as e:
    #    if not(e.errno==errno.EEXIST and os.path.isdir(repertoire)):
    #        raise
    try:
        fRead = open(chemin,'r')
    except:
        print "ERROR!  File '%s' not found, load canceled." % (chemin)
        return None
    positions = []
    #i = 0
    for line in fRead:
        """
        pos = string.atoi(line)
        if pos < 0 or pos > 19:
            print "ERROR!  Column %d has an invalid position of %d, must be an integer between 0 and 19.  Load canceled." % (i,pos)
            fRead.close()
            return 1
        else:
            positions.append(pos)
        """
        positions.append(str(line))
        #i += 1
    # warning, the first line contains the file name! (pour as-tu fais ca Michel??)
    # je l'enleve de la liste
    positions.pop(0)
    if len(positions) != 25:
        print "ERROR!  File contains %d positions, must contain positions for 25 'cubes', only.  Load canceled." % (len(positions))
        #return 2
        return None
    else:
        PtSendKIMessage(26,"Reading file '%s', positions of Jalak's 'cubes'"% (chemin))
    fRead.close()
    return positions

def LoadCubes(nomfichier,nomavatar):
    #nomfichier = nomfichier + Avatars.Nomsimplifie(nomavatar) + ".txt"
    nomfichier = nomfichier + "_" + nomavatar + ".txt"
    repertoire = "jeux/Jcubes/"
    #nfichier = FichierDisque(repertoire, nomfichier)
    #texteobjets = nfichier.lire()
    #if texteobjets == "ERROR":
    #    #le fichier n'existe pas
    #    print "ERROR!  File '%s' not found, load canceled." % (repertoire+nomfichier)
    #    return 0
    #Matrices = texteobjets.split('\n')
    lstStrTuples = FichierDisque(repertoire, nomfichier)
    if lstStrTuples is None:
        # Une erreur s'est produite, fichier inexistant ou nb de tuples incorrect
        print "ERROR!  File '%s' not found or incorrect number of tuples, load canceled." % (repertoire+nomfichier)
        return 0
    #enlever les cubes du terrain
    ResetCubes()
    #i=0
    ##for smatrice in Matrices:       
    #for smatrice in lstTuples:       
    #    matrice = ast.literal_eval(smatrice)
    #    matrix = ptMatrix44()
    #    matrix.setData(matrice)
    #    objet = PtFindSceneobject(cubes[i],'Jalak')
    #    objet.physics.netForce(1)
    #    objet.physics.warp(matrix)
    #    objet.physics.enable(1)
    #    objet.draw.netForce(1)
    #    objet.draw.enable(1)
    #    i += 1
    PtSetAlarm(2, PlaceCubes(lstStrTuples), 1)
    return 1

class PlaceCubes():
    def __init__(self, lstStrTuples):
        self._lstStrTuples = lstStrTuples

    def onAlarm(self, param=1):
        if param == 1:
            i = 0
            for strTuple in self._lstStrTuples:       
                tplMatrix = ast.literal_eval(strTuple)
                matrix = ptMatrix44()
                matrix.setData(tplMatrix)
                objet = PtFindSceneobject(cubes[i],'Jalak')
                objet.physics.netForce(1)
                objet.physics.disable()
                objet.physics.warp(matrix)
                #objet.physics.enable(1)
                objet.draw.netForce(1)
                objet.draw.enable(1)
                i += 1
            PtSetAlarm(2, self, 2)
        if param == 2 :
            for cube in cubes:
                objet = PtFindSceneobject(cube,'Jalak')
                objet.netForce(1)
                objet.physics.enable(1)


def ResetCubes():
    i=0
    for cc in cubes:
        SOcube = PtFindSceneobject(cc, 'Jalak')
        SOwarp = PtFindSceneobject(warpcubes[i], 'Jalak')
        warpPT = SOwarp.getKey()
        SOcube.physics.netForce(1)
        SOcube.draw.netForce(1)
        SOcube.draw.enable(1)
        SOcube.physics.warpObj(warpPT)
        i += 1
    ageSDL = PtGetAgeSDL()
    ageSDL["jlakCurrentSphere"] = (5,)
    ageSDL["jlakCurrentLilBox"] = (5,)
    ageSDL["jlakCurrentBigBox"] = (5,)
    ageSDL["jlakCurrentRamp"] = (5,)
    ageSDL["jlakCurrentRectangle"] = (5,)

def ResetColumns(hauteur=0):
    ageSDL = PtGetAgeDSDL()
    for col in sdlColumns:
        ageSDL[col] = (hauteur,)

