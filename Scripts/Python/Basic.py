# Basic
# Essential commands mostly used by the other modules.


from Plasma import *

# Basic.GetAllAvatars(bool me)
# Gets a list of all avatars in the current Age (which either includes or
# excludes me).
def GetAllAvatars(me=True):

    playerList = PtGetPlayerList()
    result = [PtGetAvatarKeyFromClientID(player.getPlayerID()).getSceneObject() for player in playerList]
    if me:
        result.append(PtGetLocalAvatar())
    return result
    
# Basic.GetOneAvatar(string name)
# Gets an avatar in the current Age from his KI number (or his name).
def GetOneAvatar(name):

    name = name.lower()
    if name == "me":
        return PtGetLocalAvatar()
    else:
        return PtGetAvatarKeyFromClientID(GetPlayer(name).getPlayerID()).getSceneObject()

# Basic.GetPlayer(string name)
# Gets a player from his KI number (or his name). This does not return an 
# avatar.
def GetPlayer(name):

    playerList = PtGetPlayerList()
    name = name.lower().replace(' ', '')
    if name == "me":
        return PtGetLocalPlayer()
    result = None
    for player in playerList:
        if player.getPlayerName().lower().replace(" ", "") == name or str(player.getPlayerID()) == name:
            return player
            break

# Basic.GetSDL(string name)
# Gets the current value for an SDL setting.
def GetSDL(name):

    sdl = PtGetAgeSDL()
    value = sdl[name][0]
    return value

# Basic.ListResponders(string objName, string age)
# Find a list of responders for the associated object.
def ListResponders(objName, age=None):

    if age is None:
        age = PtGetAgeName()
    obj = PtFindSceneobject(objName, age)
    print("Listing scene objects for: {}".format(objName))
    for responder in obj.getResponders():
        print(responder.getName())

# Basic.MoveObj(string obj, float x, float y, float z, string age)
# Move an object to the specified coordinates.
def MoveObj(objName, x, y, z, age=None):

    if not age:
        age = PtGetAgeInfo().getAgeFilename()
    obj = PtFindSceneobject(objName, age)
    obj.netForce(True)
    pos = ptPoint3(x, y, z)
    obj.physics.warp(pos)

# Basic.NetPageIn(string page)
# Pages in a scene or object.
def NetPageIn(page):

    PtConsoleNet("Nav.PageInNode {}".format(page), True)

def NetPageOut(page):

    PtConsoleNet("Nav.PageOutNode {}".format(page), True)

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

# Basic.SetSDL(string name, string value)
# Sets the value for an SDL setting.
def SetSDL(name, value):

    sdl = PtGetAgeSDL()
    sdl[name] = (value, )
    return GetSDL(name)

## Basic.ScaleObj(string objName, float x, float y, float z, string age)
# Scale an object by the specified coordinates.
# TODO: Fix this.
def ScaleObj(objName, x, y=None, z=None, age=None):

    if not age:
        age = PtGetAgeInfo().getAgeFilename()
    if not y: y = x
    if not z: z = x
    obj = PtFindSceneobject(objName, age)
    obj.netForce(True)
    if x == 0:
        obj.physics.enable()
        return
    pos = obj.getLocalToWorld()
    scale = ptMatrix44()
    scale.makeScaleMat(ptVector3(x, y, z))
    obj.physics.disable()
    obj.physics.netForce(True)
    obj.physics.warp(pos * scale)

# Basic.ToggleDraw(string/ptSceneobject obj, int en, string age)
# Toggles the visibility setting on an object.
def ToggleDraw(obj, en=False, age=None):

    if age is None:
        age = PtGetAgeName()
    if not isinstance(obj, ptSceneobject):
        obj = PtFindSceneobject(obj, age)
    obj.draw.netForce(True)
    obj.draw.enable(en)

# Basic.TogglePhysics(string/ptSceneobject obj, int en, string age)
# Toggles the physics setting on an object.
def TogglePhysics(object, en=False, age=None):

    if age is None:
        age = PtGetAgeName()
    if not isinstance(object, ptSceneobject):
        object = PtFindSceneobject(object, age)
    object.physics.netForce(True)
    object.physics.enable(en)
