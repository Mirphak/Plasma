from Plasma import *

pageBugs = "ItinerantBugCloud"

def AddPrp(page=pageBugs):
    PtConsoleNet("Nav.PageInNode %s" % (page) , 1)

def DelPrp(page=pageBugs):
    PtConsoleNet("Nav.PageOutNode %s" % (page) , 1)

def DelPrpLocal(page=pageBugs):
    PtPageOutNode(page)

#
def Bugs(av, bOnOff):
    #global bugs
    #self.chatMgr.AddChatLine(None, "> Bugs", 3)
    #if len(args) < 2:
    #    return 0
    #myself = PtGetLocalPlayer()
    #player = args[0]
    #onOff = args[1].strip().lower()
    #av = PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject()
    #avPos = av.getLocalToWorld()
    AddPrp(pageBugs)
    bugs = PtFindSceneobject("BugFlockingEmitTest", "Garden")
    #bugsPos = bugs.getLocalToWorld()
    bugs.draw.netForce(1)
    #msg = player.getPlayerName()
    if bOnOff == True:
        PtTransferParticlesToObject(bugs.getKey(),av.getKey(),100)
        bugs.draw.enable(1)
        #msg += " calls bugs."
    else:
        PtKillParticles(0,1,av.getKey())
        #msg += " has killed bugs."
        bugs.draw.enable(0)
        #msg += " releases bugs."
    #PtSendRTChat(myself, [player], msg, 24)
