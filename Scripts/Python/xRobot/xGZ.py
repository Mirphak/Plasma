# -*- coding: utf-8 -*-

"""
    xGZ.py
    
    Version 1 : 20/02/2016 12:37
        Start and stop GZ (made by Stone for mystitech)

        # Python/fun/mystitech/gzSDL.py

        from xCheat import SetSDL
        from Plasma import PtSetAlarm

        def EnableGZ( en ):
            ''' Set SDLs for the Great Zero. '''
            PtSetAlarm( 6.7 * en, gz_callback(), en )
            SetSDL( 'grtzGZActive_%s' % en )
        class gz_callback:
            def onAlarm( self, en ):
                SetSDL( 'grtzGreatZeroState_%s' % en )

    Version 2 : 25/02/2017

        De zeke365 18/02/2017 23:43
        À Guild, Larry, Stone, moi

        So what you guys like to do for this tour coming up which is Great Zero?

        One suggestion is if it possible to make a platform on the outside of the great chamber so so 
        that when we get that part we you r'aty and larry can explain it with us being closer to the 
        beam area.
        This way your not explaining everything inside that and if you like to change up to go on ahead 
        do it. 

        De Larry F 19/02/2017 01:49
        À zeke365, Guild, Stone, moi

        That sounds like a good idea to me.

        The usual effects schedule for the tour are to start out in the observation chamber, and then 
        warp to the courtyard.

        Once we get there, it would be a good idea to have the machine turned off so that we can turn 
        it on for the tour group, so they can see the neutrino beam arrive and activate it.
        Then we’d want to turn it off again so we can do it later, when we are in the calibration center.

        From the calibration center, yes, it would be nice to go outside when we talk about the 
        neutrino collection towers instead of me just describing them from a distance.
        If that is possible, we’d want to warp over to them as a group instead of just having people 
        run there.
        If a platform of invisible Jalak pillars with some set as a fence, we can keep the group from 
        running off before the lectures is over.

        My other long-running ambition is to show the guests the hidden wall patterns in the pool below 
        the neutrino dispenser machine, in the neutrino tunnel, and in the central pool in the 
        calibration center.

        Another nice touch would be if we could switch the imager back to the Tokotah Alley picture on 
        demand.
        However, I have no idea if that picture is still in the game files.

        The patterns and images I’m talking about can be found on my GZ page, 
        http://www.florestica.com/hpotd/great_zero/

        -----------------
        De zeke365 18/02/2017 23:43
        À Guilde, Larry, Stone, moi

        Alors, ce que vous les gars aiment faire pour cette tournée à venir qui est Grand Zéro?

        Une suggestion est si il est possible de faire une plate-forme à l'extérieur de la grande 
        chambre afin de sorte que lorsque nous obtenons cette partie nous r'aty et larry peut 
        l'expliquer avec nous étant plus proche de la zone de la poutre.
        De cette façon votre ne pas expliquer tout à l'intérieur que et si vous aimez changer pour 
        aller de l'avant le faire.

        De Larry F 19/02/2017 01:49
        À zeke365, Guilde, Pierre, moi

        Ça me semble une bonne idée.

        Le calendrier habituel des effets de la tournée est de commencer dans la chambre d'observation, 
        puis se déformer vers la cour.

        Une fois que nous y serons, ce serait une bonne idée d'avoir la machine éteinte afin que nous 
        puissions l'activer pour le groupe de tour, afin qu'ils puissent voir le faisceau de neutrino 
        arriver et l'activer.
        Alors nous voudrions l'éteindre de nouveau afin que nous puissions le faire plus tard, quand 
        nous sommes dans le centre d'étalonnage.

        Du centre d'étalonnage, oui, ce serait bien de sortir quand on parle des tours de collecte de 
        neutrinos au lieu de me les décrire à distance.
        Si cela est possible, nous voudrions les faire passer pour un groupe au lieu de simplement 
        faire courir les gens.
        Si une plate-forme de piliers Jalak invisible avec certains mis comme une clôture, nous pouvons 
        empêcher le groupe de courir avant les conférences est terminée.

        Mon autre ambition de longue date est de montrer aux invités les motifs de mur cachés dans la 
        piscine sous la machine de distributeur de neutrinos, dans le tunnel de neutrino et dans la 
        piscine centrale dans le centre de calibration.

        Une autre touche agréable serait si nous pouvions changer l'imageur à l'image de Tokotah Alley 
        sur demande.
        Cependant, je n'ai aucune idée si cette image est toujours dans les fichiers de jeu.

        Les motifs et les images dont je parle peuvent être trouvés sur ma page GZ, 
        http://www.florestica.com/hpotd/great_zero/


        ============================

        # GUI Marker Scope SDL record
        STATEDESC grtzMarkerScopes
        {
            VERSION 1
            VAR INT		boolOperated[1]
            VAR INT		OperatorID[1]
        }



        # Access Door SDL record
        STATEDESC grtzAccessDoors
        {
            VERSION 1
            VAR INT		DoorOpen[1]
        }

        ...

        STATEDESC GreatZero
        {
            VERSION 5

        # Boolean variables
            VAR BOOL    grtzGZActive[1]    DEFAULT=0 DEFAULTOPTION=VAULT
            VAR BOOL    grtzGZMarkerVis[1]    DEFAULT=0 DEFAULTOPTION=VAULT
            VAR BOOL    grtzYeeshaPage12Vis[1]    DEFAULT=0 DEFAULTOPTION=VAULT
            VAR STRING32 grtzGZImagerInbox[1]
            VAR BYTE    grtzGreatZeroState[1]    DEFAULT=0 DEFAULTOPTION=VAULT
            VAR BOOL    grtzCalendarSpark11[1]    DEFAULT=0 DEFAULTOPTION=VAULT

        }

        * Commandes pour le tour
            import xRobot.xGZ as g
            g.EnableGZ(0)
            g.EnableGZ(1)
            g.Cercle(coef=3.0, h=10.0, avCentre=None, bPhys=True)
            g.platform2()
            
            F10
            //ws 1 : sur la linking room
            g.platform2()
            !warpall
            F10
            
            F10
            //ws 2 : sous le protractor
            g.platform2()
            !warpall
            F10
            
            F10
            //ws 3 : sous l'imageur
            g.platform2()
            !warpall
            F10
            
            F10
            //ws 4 : un peu plus loin
            g.platform2()
            !warpall
            F10
            
            F10
            //ws 5 : au bout V1
            g.platform2()
            !warpall
            F10
            
            F10
            //ws 6 : au bout V2
            g.platform2()
            !warpall
            F10
            
            F10
            //ws 7 : colonnes oranges
            g.platform2()
            !warpall
            g.Cercle(coef=3.0, h=10.0, avCentre=None, bPhys=True)
            F10
            !toggle Pillar  0 1
            g.EnableGZ(0)
            g.EnableGZ(1)
            
            //onlake
            
            !toggle column Jalak 0 1
            
            !toggle ProtractorPart  0 0
            !toggle Water  0 0
            !toggle Wall  0 1
            !toggle Pillar  0 1
            
            * District_CathedralVIEW.prp
            CityBackDrop
            CloudLayer
            
            import CloneObject
            CloneObject.co3("grsnTerrain", "Garrison", bShow=bOn, bLoad=bOn, scale=1, matPos=mat)

            
"""

# Python/fun/mystitech/gzSDL.py

from xCheat import SetSDL
from Plasma import PtSetAlarm

def EnableGZ( en ):
    ''' Set SDLs for the Great Zero. '''
    PtSetAlarm( 6.7 * en, gz_callback(), en )
    SetSDL( 'grtzGZActive_%s' % en )
class gz_callback:
    def onAlarm( self, en ):
        SetSDL( 'grtzGreatZeroState_%s' % en )

#=====================================================================

from Plasma import *
import math
import sdl
import Ride
import Platform
import CloneObject

#
def clone(obj="grsnTerrain", age="Garrison", bOn=True):
    mat = None
    CloneObject.co3(obj, age, bShow=bOn, bLoad=bOn, scale=1, matPos=mat)

# toggles guild bool sdl
def togglesdl(name):
    dicNames = {
        "active":"grtzGZActive", 
        "state":"grtzGreatZeroState", 
    }
    if (name in dicNames.keys()):
        sdl.ToggleBoolSDL(dicNames[name])
    else:
        print("wrong sdl name")


#
dicBot = {
    32319L:"Mir-o-Bot", 
    27527L:"Magic Bot", 
    71459L:"Mimi Bot", 
    #L:"Stone5", 
    64145L:"Annabot",
    #L:"SkydiverBot",
    3975L:"OHBot",
    24891L:"Magic-Treasure",
    26224L:"Magic Treasure",
    21190L:"Mimi Treasure",
    2332508L:"mob",
    }

# Larry LeDeay [KI: 11308]
plSpeakerID = 11308


#
def Cercle(coef=3.0, h=10.0, avCentre=None, bPhys=True):
    maxdist = 5
    matrix  = ptMatrix44()
    if isinstance(avCentre, ptMatrix44):
        matrix = avCentre
    elif avCentre is None:
        avCentre = PtGetLocalAvatar()
        matrix = avCentre.getLocalToWorld()
    
    #agePlayers = GetAllAgePlayers()
    # ne pas tenir compte des robots
    agePlayers = filter(lambda pl: not(pl.getPlayerID() in dicBot.keys()), PtGetPlayerList())
    agePlayers.append(PtGetLocalPlayer())
    soAvatarList = map(lambda player: PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject(), agePlayers)
    for soavatar in soAvatarList:
        #faire flotter tout le monde
        soavatar.netForce(1)
        soavatar.physics.disable()
        soavatar.physics.enable(0)
        soavatar.netForce(1)

    i = 0
    n = len(agePlayers)
    print "nb de joueurs: %s" % (n)
    dist = float(coef * n) / (2.0 * math.pi)
    print "distance: %s" % (dist)
    nbCercles = dist // maxdist
    if nbCercles > 0:
        dist = dist / nbCercles
    for i in range(n):
        avatar = soAvatarList[i]
        angle = (float(i%maxdist) * float(nbCercles) * 2.0 * math.pi) / float(n)
        dist = dist + (n // maxdist)
        print "angle(%s): %s" % (i, angle)
        dx = float(dist)*math.cos(angle)
        dy = float(dist)*math.sin(angle)
        #matrix = avCentre.getLocalToWorld()
        matrix.translate(ptVector3(dx, dy, float(h)))
        mRot = ptMatrix44()
        mRot.rotate(2, angle - math.pi)
        avatar.netForce(1)
        avatar.physics.warp(matrix * mRot)
    for soavatar in soAvatarList:
        soavatar.netForce(1)
        soavatar.physics.enable(bPhys)


#
def panic(bAll=True):
    PtConsoleNet("Avatar.Spawn.DontPanic" , True)


#
def AddPrp(pages=["kemoStorm"]):
    #global bCleftAdded
    for page in pages:
        PtConsoleNet("Nav.PageInNode {0}".format(pages) , 1)
    bCleftAdded = True

#
def DelPrp(pages=["kemoStorm"]):
    #global bCleftAdded
    for page in pages:
        PtConsoleNet("Nav.PageOutNode {0}".format(pages) , 1)
    bCleftAdded = False

#
def hide(bOn=False):
    #Platform.HideJalak()
    # Hide some objects
    names = ["Bamboo", "Dome", "Garden", "Pillar", "TreeTrunk", "Rain", "Water"]
    Platform.ShowObjectList("garden", names, bOn)
    # Disable physics for some objects
    names = ["TreeTrunk"]
    Platform.PhysObjectList("garden", names, bOn)

# long platform(where=1)
def platform2(where=None):
    matPos = None
    if where is None or where not in range(1, 5):
        matPos = PtGetLocalAvatar().getLocalToWorld()
    else:
        #Ahnonay
        if where == 1:
            tupPos = ((0.98276501894, 0.184859260917, 0.0, 23.3415126801), (-0.184859260917, 0.98276501894, 0.0, 54.0308570862), (0.0, 0.0, 1.0, -0.0328424945474), (0.0, 0.0, 0.0, 1.0))
        elif where == 2:
            tupPos = ((-0.897078573704, -0.44187015295, 0.0, 649.721862793), (0.44187015295, -0.897078573704, 0.0, -877.984619141), (0.0, 0.0, 1.0, 9445.71386719), (0.0, 0.0, 0.0, 1.0))
        elif where == 3:
            tupPos = ((0.00954949762672, -0.999954581261, 0.0, -102.545890808), (0.999954581261, 0.00954949762672, 0.0, 54.9582672119), (0.0, 0.0, 1.0, 10563.0976562), (0.0, 0.0, 0.0, 1.0))
        elif where == 4:
            tupPos = ((-0.748968303204, 0.662607133389, 0.0, 1560.00488281), (-0.662607133389, -0.748968303204, 0.0, -51.4498291016), (0.0, 0.0, 1.0, 10171.9091797), (0.0, 0.0, 0.0, 1.0))
        elif where == 5:
            tupPos = ((-0.937420606613, -0.3482016325, 0.0, 993.751708984), (0.3482016325, -0.937420606613, 0.0, -455.378509521), (0.0, 0.0, 1.0, 9424.86523438), (0.0, 0.0, 0.0, 1.0))
        matPos = ptMatrix44()
        matPos.setData(tupPos)
        
    Platform.CreatePlatform2(bShow=False, matAv=matPos)

#