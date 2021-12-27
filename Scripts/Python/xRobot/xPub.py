# -*- coding: utf-8 -*-

"""
    Pubs Version 1 : Cavern Tour du 12/12/2015

    Pubs Version 2 : Cavern Tour du 29/04/2017 
        From Larry (19/04/2017) :
            The pubs are another pretty easy one for the techs up until the end. 
            We just need to warp to the individual guild pubs in turn, and that's that. 
            The order that we visit the pubs in doesn't matter, except that we want to 
            go to the Watcher's pub last.

            It's when we get to the Watcher's pub that it becomes more challenging. 
            Here's the wish list:

            Remove the curtains from the side chambers so we can see inside them.

            Enable the projections for day and night in the spherical Tree chamber.

            Take us outside the pub so we can see the J'taeri neighborhood and the 
            rest of the cavern around it. 
            (Alternatively, making the walls of the pub invisible would accomplish 
            the same purpose.)

            Open up the second floor puzzle room and extend the bridge across the gap, 
            so we can walk to the Great Tree sculpture. 
            (We could warp across, but that's less desirable.)

            We may want to warp to the landing at the top of the puzzle room, 
            just before the bridge, since getting up the ladder and walking along 
            the spiral path is a choke point.

            That's pretty much it. If there's anything else, I don't remember it off 
            the top of my head.
    
        Traduction :
            Les pubs sont un autre assez facile pour les techniciens jusqu'à la fin.
            Il suffit de faire preuve de déformation pour les pubs de guilde 
            individuels, et c'est tout.
            L'ordre dans lequel nous visitons les pubs n'a pas d'importance, 
            sauf que nous voulons aller au pub Watcher dernier.

            C'est quand on arrive au pub Watcher qu'il devient plus difficile.
            Voici la liste de souhaits:

            Retirez les rideaux des chambres latérales afin que nous puissions voir 
            à l'intérieur d'eux.

            Activer les projections pour le jour et la nuit dans la chambre arborescente 
            sphérique.

            Prenez-nous à l'extérieur du pub afin que nous puissions voir le quartier 
            de J'taeri et le reste de la caverne autour de lui.
            (Alternativement, rendre les murs du pub invisibles accomplirait le même 
            but.)

            Ouvrez la salle de puzzle du deuxième étage et étendez le pont à travers 
            l'espace, afin que nous puissions aller à la sculpture Great Tree.
            (Nous pourrions traverser, mais c'est moins souhaitable.)

            Nous voudrions peut-être nous déformer vers l'atterrissage au sommet de la 
            salle de puzzle, juste avant le pont, depuis la montée de l'échelle et le 
            long du chemin en spirale est un point d'étouffement.

            C'est à peu près ça. S'il y a autre chose, je ne me souviens pas du haut de 
            ma tête.
    
"""

from Plasma import *
import sdl

bJalakAdded = False

#
def AddPrp():
    global bJalakAdded
    pages = ["GreatTree", "Pub"]
    for page in pages:
        PtConsoleNet("Nav.PageInNode %s" % (page) , 1)
    bJalakAdded = True

#
def DelPrp():
    global bJalakAdded
    pages = ["GreatTree", "Pub"]
    for page in pages:
        PtConsoleNet("Nav.PageOutNode %s" % (page) , 1)
    bJalakAdded = False

#
def DelPrpLocal():
    global bJalakAdded
    if bJalakAdded:
        pages = ["GreatTree", "Pub"]
        for page in pages:
            PtPageOutNode(page)
        bJalakAdded = False

#

#=====================================
# GreatTreePub.sdl
#=====================================
"""
STATEDESC GreatTreePub
{
	VERSION 3

## Age Mechanics ##
    	VAR BOOL grtpErcanaLinkingBookVis[1] 		DEFAULT=0 DEFAULTOPTION=VAULT
    	VAR BOOL grtpAhnonayLinkingBookVis[1] 		DEFAULT=0 DEFAULTOPTION=VAULT
    	VAR BOOL grtpDRCWatchersJournalVis[1] 		DEFAULT=0 DEFAULTOPTION=VAULT
	VAR BOOL grtpWatchersJournalsVis[1] 		DEFAULT=0 DEFAULTOPTION=VAULT
	VAR BOOL islmGZBeamVis[1] 			DEFAULT=0 DEFAULTOPTION=VAULT
	VAR BOOL grtpBallHallDoorVis[1] 		DEFAULT=0 DEFAULTOPTION=VAULT
	VAR BOOL grtpDeadBahroVis[1] 			DEFAULT=0 DEFAULTOPTION=VAULT

}
"""

#
def GuildSdl():
    names = [
        "grtpErcanaLinkingBookVis",  # BOOL      0
        "grtpAhnonayLinkingBookVis", # BOOL      0
        "grtpDRCWatchersJournalVis", # BOOL      0
        "grtpWatchersJournalsVis",   # BOOL      0
        "islmGZBeamVis",             # BOOL      0
        "grtpBallHallDoorVis"        # BOOL      0
        "grtpDeadBahroVis"           # BOOL      0
    ]
    for name in names:
        try:
            value = GetSDL(name)
            print "Guil SDL name={}, value={}".format(name, value)
        except:
            print "Guil SDL \"{}\" not found".format(name)

# toggles guild bool sdl
def guild(name):
    dicNames = {
        "book":"grtpErcanaLinkingBookVis", 
        "first":"grtpAhnonayLinkingBookVis", 
        "switch":"grtpDRCWatchersJournalVis", 
        "bridge":"grtpWatchersJournalsVis", 
        "door":"islmGZBeamVis", 
        "ladder":"grtpBallHallDoorVis", 
        "ball":"grtpDeadBahroVis"
    }
    if (name in dicNames.keys()):
        ToggleBoolSDL(dicNames[name])
    else:
        print("wrong sdl name")


#
def sky(bOffOn=0):
    PtSetAlarm(0, RunResp("SphereEnvironDARK", "GeatTreePub", bOffOn, 0), 1)
    #PtSetAlarm(0, RunResp('', 1, 0), 1)

#
def TreeSphere(en=True, clouds=True):
    for item in ('SphereEnviron', 'SphereEnvironDARK', 'SphereClouds')[:2+clouds]:
        d = PtFindSceneobject(item, 'GreatTreePub').draw
        d.netForce(1)
        d.enable(en)
        en = not en;