# -*- coding: utf-8 -*-

"""
    Version 1 : 19/03/2016
        CAVERN TOUR DU 19/03/2016
        Mail de Larry F du 13 mars (Il y a 6 jours) A zeke365, Rhen, Stone, moi
        The requested effects for this tour are pretty straightforward. 
        We want to go outside the pods in Negilahn, Payiferen, and Dereno as the basics.

        Negilahn: 
            It would be nice if we can call up the urwin and two-tailed monkeys on demand, and show the urwin walking normally. 
            Even better would be if we could hear the sound effects at the same time. 
            Rides on the animals are optional.

        Payiferen: 
            Calling up the sandskrit and showing its normal behavior would be nice, with sound effects would be better. 
            This model has a day / night cycle with a really beautiful sunrise and sunset, 
            so if you can somehow speed that up so our guests can see the whole thing in a short time, I think it would be fabulous.

        Dereno: 
            This is a two-level model, so we'd need to be able to walk around the outside both on the surface and underwater as a goal. 
            The pattern of frost on the windows of the pod are interesting, 
            so if you can come up with a way of highlighting that, so much the better. 
            Rides on the fish are optional.

        Tetsonot: 
            No outside to see, so just arranging better light inside the pod is enough.

    Version 2 : 25/03/2017
        Larry F 18 mars 2017
        À zeke365, Guild, Stone, moi

        Next week will be the pod Ages? 
        Here are some suggestions and reminders.

        Last week, Mirphak somehow managed to disable at least some of the bot commands that allowed explorers to do things like import firemarbles or other objects, turn on KI lights, and so forth. 
        Is there a way to do that which doesn't block their ability to use warp or link commands to recover and rejoin the tour? 
        If so, then preventing them from doing things that disrupt the tour and add to lag is highly desirable. 
        Give them the ability, and some of them will abuse it no matter how often we ask them not to.

        If you all don't mind, how about we start in Tetsonot? 
            I think it would be a good idea to get that out of the way first, since there's nothing to see outside it. 
            We'll want Stone and Mirphak to do whatever they can to light it up better, but that's the only special effect needed. 
            Plus, since it's a dark, enclosed space, it might be a good place to get some of the general talk about the Pod Age done with.

        Negilahn: 
            The usual stuff. 
            We want to go outside, and to summon the monkeys and urwin on demand. 
            If we can get the urwin moving and get the sound effects working, that would be much better.

        Payiferen: 
            Same as Negilahn. 
            Outside, urwin moving with sound effects if possible. 
            Additionally, we want to be able to switch back and forth between day and night, and/or speed up the day-night cycle to see the sunrise and sunset.

        Dereno: 
            Outside, transparent ice to see the fish below. 
            Perhaps a lower walking surface to run around with the fish?

        Whatever you can do with these suggestions will be good. 
        Plus, don't hesitate to do anything else you can think of.

        I don't have any particular preference in the Age order other than wanting to knock Tetsonot out of the way first. 
        Anyone else have an order they'd like to go with?
        
        Larry F 18 mars 2017
        À zeke365, Guilde, Pierre, moi

        La semaine prochaine sera le pod Ages?
        Voici quelques suggestions et rappels.

        La semaine dernière, Mirphak a réussi à désactiver au moins quelques-unes des commandes de bot qui permettaient aux explorateurs de faire des choses comme importer des firemarbles ou d'autres objets, allumer des lumières KI, et ainsi de suite.
        Y at-il un moyen de faire ce qui ne bloque pas leur capacité à utiliser la chaîne ou des commandes de lien pour récupérer et rejoindre la tournée?
        Si c'est le cas, alors il est très souhaitable de les empêcher de faire des choses qui dérangent la tournée et d'ajouter au décalage.
        Donnez-leur la capacité, et certains d'entre eux vont abuser, peu importe combien de fois nous leur demandons de ne pas.

        Si vous ne vous en faites pas, que diriez-vous de commencer à Tetsonot?
            Je pense que ce serait une bonne idée de sortir cela du premier plan, puisqu'il n'y a rien à voir en dehors.
            Nous allons demander à Stone et Mirphak de faire tout leur possible pour l'éclairer mieux, mais c'est le seul effet spécial nécessaire.
            De plus, puisque c'est un espace sombre, clos, il pourrait être un bon endroit pour obtenir certains des général parler de l'âge de Pod fait avec.

        Negilahn:
            Le truc habituel.
            Nous voulons aller à l'extérieur, et de convoquer les singes et urwin sur demande.
            Si nous pouvons obtenir l'urwin en mouvement et obtenir les effets sonores de travail, ce serait beaucoup mieux.

        Payiferen:
            Identique à Negilahn.
            En dehors, urwin se déplaçant avec des effets sonores si possible.
            De plus, nous voulons pouvoir alterner entre le jour et la nuit, et / ou accélérer le cycle jour / nuit pour voir le lever et le coucher du soleil.

        Dereno:
            Dehors, la glace transparente pour voir les poissons ci-dessous.
            Peut-être une surface de marche inférieure pour courir avec le poisson?

        Quoi que vous puissiez faire avec ces suggestions sera bon.
        De plus, n'hésitez pas à faire autre chose que vous pouvez penser.

        Je n'ai pas de préférence particulière dans l'ordre de l'âge autre que de vouloir frapper Tetsonot hors de la voie d'abord.
        Quelqu'un d'autre a une commande avec laquelle il aimerait y aller?
"""

from Plasma import *
import Ride
import math

#
def LinkPlayerTo(age, playerID=None, spawnPointNumber=None):
    if not playerID or playerID == "":
        playerID = PtGetLocalPlayer().getPlayerID()
    else:
        try:
            playerID = long(playerID)
        except:
            return "incorrect playerID"
            #pass
    if len(age) < 3:
        #pass
        return "incorrect age"
    ageInstanceName = age[0]
    ageFileName = age[1]
    ageGuid = age[2]
    ageUserDefinedName = ""
    if len(age) > 3:
        ageUserDefinedName = age[3]
    
    ageLink = ptAgeLinkStruct()
    ageInfo = ptAgeInfoStruct()
    ageInfo.setAgeFilename(ageFileName)
    ageInfo.setAgeInstanceGuid(ageGuid)
    ageInfo.setAgeInstanceName(ageInstanceName)
    
    ageLink.setAgeInfo(ageInfo)
    """
    spawnPt = "LinkInPointDefault"
    if spawnPointNumber:
        spawnPt = GetSpawnPoint(spawnPointNumber)
    else:
        ageSpawPoint = ""
        if len(age) > 4:
            ageSpawPoint = age[4]
        if ageSpawPoint != "":
            spawnPt = ageSpawPoint
    #self.chatMgr.AddChatLine(None, "sp=\""+spawnPt+"\"", 3)
    spawnPoint = ptSpawnPointInfo()
    spawnPoint.setName(spawnPt)
    ageLink.setSpawnPoint(spawnPoint)
    """
    ptNetLinkingMgr().linkPlayerToAge(ageLink, playerID)
    return ageUserDefinedName + " " + ageInstanceName

# negilahn, dereno, payiferen, tetsonot
def LinkAll(ageName="dereno"):
    ages = {
        "hi":["Hood of Illusions", "Neighborhood", "3cc44d4b-31e1-4dec-b6e6-4b63c72becc3", "The", ""],
        #"tsogal":["EderTsogal", "EderTsogal", "03c05256-c149-4fa5-9210-b848b9b9b5c0", "Mir-o-Bot's", ""],
        #"delin":["EderDelin", "EderDelin", "6ed7f98c-a3f6-4000-bb79-91843f78441a", "Mir-o-Bot's", ""],
        #"gz":["Ae'gura", "GreatZero", "76aa23d2-07a0-45f6-b355-5de39302f455", "Mir-o-Bot's GZ", ""],
        "negilahn":["Negilahn", "Negilahn", "41d48e5b-d037-4054-8c63-42a1273c3830", "Mir-o-Bot's", ""], 
        "dereno":["Dereno", "Dereno", "330f59b9-9b21-4130-81e4-9852d3493fa9", "Mir-o-Bot's", ""], 
        "payiferen":["Payiferen", "Payiferen", "ae90edff-73ed-413c-a3b1-f2b4f1ae217d", "Mir-o-Bot's", ""], 
        "tetsonot":["Tetsonot", "Tetsonot", "c0f86889-e38a-412f-9eb9-9ac2091b3fa7", "Mir-o-Bot's", ""], 
    }
    
    ageName = ageName.lower()
    if (ageName in ages.keys()):
        age = ages[ageName]
    else:
        return
    
    #les autre joueurs dans mon age
    for player in PtGetPlayerList():
        LinkPlayerTo(age, playerID = player.getPlayerID(), spawnPointNumber = None)
    # link myself
    #LinkPlayerTo(age, playerID = None, spawnPointNumber = None)

#
def wa(where=None):
    #avCentre = PtGetLocalAvatar()
    #mat = avCentre.getLocalToWorld()
    mat = None
    if where is None: #or where not in range(1, 5):
        mat = PtGetLocalAvatar().getLocalToWorld()
    else:
        """
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
        mat = ptMatrix44()
        mat.setData(tupPos)
        """
        objName = "ZandiMobileRegion"
        ageName = "Cleft"
        so = PtFindSceneobject(objName, ageName)
        mat = so.getLocalToWorld()

        #return 0
    
    #recuperer tous les joueurs
    playerList = PtGetPlayerList()
    playerList.append(PtGetLocalPlayer())
    soAvatarList = map(lambda player: PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject(), playerList)
    for soavatar in soAvatarList:
        #faire flotter tout le monde
        soavatar.netForce(1)
        soavatar.physics.disable()
        soavatar.physics.enable(0)
        soavatar.netForce(1)
    for soavatar in soAvatarList:
        #deplacer les gens
        soavatar.physics.warp(mat)
        soavatar.netForce(1)
    for soavatar in soAvatarList:
        #reactiver la physique pour tous
        soavatar.physics.enable(1)
        soavatar.netForce(1)

#

#========================================================
dicBot = {}

#
def Cercle(coef=5.0, h=10.0, avCentre=None):
    if avCentre is None:
        avCentre = PtGetLocalAvatar()
    #agePlayers = GetAllAgePlayers()
    # ne pas tenir compte des robots
    agePlayers = filter(lambda pl: not(pl.getPlayerID() in dicBot.keys()), PtGetPlayerList())
    i = 0
    n = len(agePlayers)
    print "nb de joueurs: %s" % (n)
    dist = float(coef * n) / (2.0 * math.pi)
    print "distance: %s" % (dist)
    for i in range(n):
        player = agePlayers[i]
        avatar = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
        angle = (float(i) * 2.0 * math.pi) / float(n)
        print "angle(%s): %s" % (i, angle)
        dx = float(dist)*math.cos(angle)
        dy = float(dist)*math.sin(angle)
        matrix = avCentre.getLocalToWorld()
        matrix.translate(ptVector3(dx, dy, float(h)))
        avatar.netForce(1)
        avatar.physics.warp(matrix)

#
def CercleV(coef=2.0, avCentre=None):
    if avCentre is None:
        avCentre = PtGetLocalAvatar()
    #agePlayers = GetAllAgePlayers()
    # ne pas tenir compte des robots
    agePlayers = filter(lambda pl: not(pl.getPlayerID() in dicBot.keys()), PtGetPlayerList())
    i = 0
    n = len(agePlayers)
    print "nb de joueurs: %s" % (n)
    dist = float(coef * n) / (2.0 * math.pi)
    print "distance: %s" % (dist)
    for i in range(n):
        player = agePlayers[i]
        avatar = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
        angle = (float(i) * 2.0 * math.pi) / float(n)
        print "angle(%s): %s" % (i, angle)
        dx = float(dist)*math.cos(angle)
        #dy = float(dist)*math.sin(angle)
        dy = 0
        dz = float(dist)*math.sin(angle)
        matrix = avCentre.getLocalToWorld()
        matrix.translate(ptVector3(dx, dy, dz))
        avatar.netForce(1)
        avatar.physics.warp(matrix)

#
class CircleAlarm:
    def onAlarm(self, param):
        if param == 0:
            CercleV(coef=2.0, avCentre=None)
        elif param == 1:
            Cercle(coef=2.0, h=0, avCentre=None)

"""
Negilhan : 'singe', 'urwin'
Dereno : 'poissond', 'raie1', 'raie2'
Payiferen : 'sandscrit'
"""
# 
def ride(soName="sandscrit", t=30.0, c=None):
    #recuperer tous les joueurs
    playerList = PtGetPlayerList()
    playerList.append(PtGetLocalPlayer())
    for player in playerList:
        playerName = player.getPlayerName()
        Ride.Suivre(objet=soName, Avatar=playerName, duree=t)
    if c is not None:
        PtSetAlarm(2, CircleAlarm(), c)

"""
Negilhan : 
	'singe' : 'alarme', 'grimpe', 'mange', 'attend', 'crie', 'saute', 'arbre1', 'arbre2', 'arbre3', 'sur moi'
	'urwin' : 'start', 'stop', 'sur moi'
Payiferen : 
	'sandscrit' : 'start', 'stop', 'sur moi'
"""
# 'alarme', 'grimpe', 'mange', 'attend', 'crie', 'saute', 'arbre1', 'arbre2', 'arbre3', 'sur moi'
def monkey(what='sur moi'):
    Ride.Action(animal='singe', action=what)

# 'start', 'stop', 'sur moi'
def urwin(what='sur moi'):
    Ride.Action(animal='urwin', action=what)

# 'start', 'stop', 'sur moi'
def sandscrit(what='sur moi'):
    Ride.Action(animal='sandscrit', action=what)

#