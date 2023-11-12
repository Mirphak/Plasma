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
    
    Pubs Version 3 : Cavern Tour du 22/08/2020 
        That means the next tour on the schedule is the Guild Pubs. 
        Since the Watcher’s Pub is the one with the most to do, we should save it for the last.
        
        a.     Guild of Cartographers’ Pub
        b.     Guild of Greeters’ Pub
        c.     Guild of Maintainers’ Pub
        d.     Guild of Messengers’ Pub
        e.     Guild of Writers’ Pub
        
        These pubs do not require effects other than to warp the guests to them, each in turn. 
        I’ll talk about the D’ni and explorer versions of the guilds in each.
        
        As a prelude, I’ll discuss D’ni guilds in general. 
        Since that’s an introduction, 
        I’ll be giving that lecture before we leave the tour neighborhood to warp to 
        the Cartographers’ Pub.
        
        f.     The Watchers’ Pub
        
        This is the one where Mirphak gets to do some real work instead of just being a virtual tour 
        bus driver. No need to thank me, Mirphak. 
        I know you appreciate me making your dreary life interesting.   ^_-
        
        So… on arrival, we want the curtains removed from the alcoves, of course, 
        so we can show the pub’s full interior. Later on, we’ll want to make the walls of the pub 
        invisible so that the guests can see what is outside it when I talk about it being in the 
        J’Taeri district.
        
        We want the animation of the day / night cycle in the Tree chamber turned on.
        
        We’ll want to show the dead Bahro on demand.
        
        We want the door into the clock room upstairs open or removed when we move on to that part of 
        the tour, and if possible, we want to show the animation of the bridge across to the stairs 
        down to the Tree bridge.
        
        We’ll probably want to warp up to the platform before the bridge instead of climbing up there, 
        since the spiral path is a little tricky and becomes a choke point for movement.
        
        Other than that, I can’t remember or think of anything else that’s important.
        
        --Larry
        
        Susa'n :
        
        I assume Mirphak will add onlake to The Watchers’ Pub so we don’t fall through the age when 
        the curtains are down.
        
        Do we want to float up to the windows around the periphery of the age?
        
        Larry F :
        
        Most of the alcoves are solid. 
        The only one that isn’t is the one where there was apparently going to be some kind of 
        linking arrangement that wasn’t completed. 
        I have no idea where an onlake effect would be in that model. 
        The pub itself is much higher up than the lake is supposed to be if were part of the 
        Ae’gura set.
        
        As for the outside windows, 
        it was to  see them that I asked to make the building walls invisible. 
        That way we’ll see them without risking someone falling and panic linking, 
        and it would save Mirphak having to build a Jalak pillar platform above the pub.
        
        The pubs don’t have an exterior skin, 
        so going outside wouldn’t show anything interesting other than the surrounding area, 
        and we can show that without leaving the interior. 
        Unless Mirphak wants to do that. 
        But after I talk about the outside, we’ll be heading up to the clock room. 
        I don’t know which would be simpler: 
        building a Jalak pillar platform above the pub and warping to it and back again, 
        or making the walls invisible and then opaque again.

    2023-09-23:
    "mobCartographers":["GuildPub-Cartographers", "GuildPub-Cartographers", "23ac83d3-dc52-4572-9b0a-ad13c298276c", "Mir-o-Bot's", ""],
    "mobGreeters":["GuildPub-Greeters", "GuildPub-Greeters", "7a69bacf-2dd0-4b8c-88ae-9878ea1157d3", "Mir-o-Bot's", ""],
    "mobMaintainers":["GuildPub-Maintainers", "GuildPub-Maintainers", "a9e45d08-dfdf-48a7-9539-bdaaa60c13e9", "Mir-o-Bot's", ""],
    "mobMessengers":["GuildPub-Messengers", "GuildPub-Messengers", "950e27bb-77a5-427a-8d7a-c121feb6a74c", "Mir-o-Bot's", ""],
    "mobWriters":["GuildPub-Writers", "GuildPub-Writers", "bf869aee-48b7-406b-a717-8e7c04dc24c0", "Mir-o-Bot's", ""],

    "mobgomepub":["GoMePubNew", "GoMePubNew", "da149d57-5671-4302-95d6-8d9ea52167ff", "Mir-o-Bot's", ""],

"""

from Plasma import *
from . import sdl

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
            print("Guil SDL name={}, value={}".format(name, value))
        except:
            print("Guil SDL \"{}\" not found".format(name))

#
#def ToggleBoolSDL(name="ba"):

# toggles guild bool sdl
def guild(name):
    dicNames = {
        "er":"grtpErcanaLinkingBookVis", 
        "ah":"grtpAhnonayLinkingBookVis", 
        "dj":"grtpDRCWatchersJournalVis", 
        "jo":"grtpWatchersJournalsVis", 
        "be":"islmGZBeamVis", 
        "ba":"grtpBallHallDoorVis", 
        "db":"grtpDeadBahroVis",
        "ch":"grtpChisoBookVis",   
        "ro":"grtpBookRoom02CrtnVis",
        "bb":"grtpBookRoomBarrierVis",
        
    }
    if (name in list(dicNames.keys())):
        sdl.ToggleBoolSDL(dicNames[name])
    else:
        print("wrong sdl name")


# Basic.RunResponder(ptKey key, string resp, ...)
# Run the responder attached to an object. Usually the first two parameters are
# sufficient.
def RunResponder(key, resp, stateidx=None, netForce=True, netPropagate=True, fastforward=False):

    nt = ptNotify(key)
    nt.addReceiver(resp)
    nt.netPropagate(netPropagate)
    nt.netForce(netForce)
    if stateidx is not None:
        nt.addResponderState(stateidx)
    if fastforward:
        nt.setType(PlasmaConstants.PtNotificationType.kResponderFF)
        nt.netPropagate(0)
        nt.netForce(0)
    nt.setActivate(1.0)
    nt.send()


#Cette fonction ne s'utilise pas seule, elle est appelée par Action()
def RunResp(key, resp, stateidx = None, netForce = 1, netPropagate = 1, fastforward = 0):
    nt = ptNotify(key)
    nt.addReceiver(resp)
    nt.netPropagate(netPropagate)
    nt.netForce(netForce)
    if stateidx != None:
        nt.addResponderState(stateidx)
    if fastforward:
        nt.setType(PtNotificationType.kResponderFF)
        nt.netPropagate(0)
        nt.netForce(0)
    nt.setActivate(1.0)
    nt.send()

#
def sky(bOffOn=0):
    PtSetAlarm(0, RunResp("SphereEnvironDARK", "GeatTreePub", bOffOn, 0), 1)
    #PtSetAlarm(0, RunResp('', 1, 0), 1)
    #PtSetAlarm(0, RunResponder("SphereEnvironDARK", "GeatTreePub", bOffOn, 0), 1)

#
def TreeSphere(en=True, clouds=True):
    for item in ('SphereEnviron', 'SphereEnvironDARK', 'SphereClouds')[:2+clouds]:
        d = PtFindSceneobject(item, 'GreatTreePub').draw
        d.netForce(1)
        d.enable(en)
        en = not en;