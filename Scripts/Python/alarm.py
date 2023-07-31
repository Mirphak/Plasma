
#==========================#
# AutoLink
#==========================#
class AutoLink:
    _running = False
    
    def __init__(self):
        print("AutoLink: __init__")
    
    def onAlarm(self, param=1):
        if not self._running:
            return
        #
        playerID = PtGetLocalPlayer().getPlayerID()
        LinkPlayerTo(self, link, playerID, spawnPointNumber=None)
        
        PtSetAlarm(15, self, 1)
    
    def Start(self):
        if not self._running:
            self._running = True
            self.onAlarm()
    
    def Stop(self):
        self._running = False

autoLink = AutoLink()
autoLink.Start(self)