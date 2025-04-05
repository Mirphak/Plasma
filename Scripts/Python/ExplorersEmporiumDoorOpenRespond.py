# -*- coding: utf-8 -*-
""" *==LICENSE==*

CyanWorlds.com Engine - MMOG client, server and tools
Copyright (C) 2011  Cyan Worlds, Inc.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

Additional permissions under GNU GPL version 3 section 7

If you modify this Program, or any covered work, by linking or
combining it with any of RAD Game Tools Bink SDK, Autodesk 3ds Max SDK,
NVIDIA PhysX SDK, Microsoft DirectX SDK, OpenSSL library, Independent
JPEG Group JPEG library, Microsoft Windows Media SDK, or Apple QuickTime SDK
(or a modified version of those libraries),
containing parts covered by the terms of the Bink SDK EULA, 3ds Max EULA,
PhysX SDK EULA, DirectX SDK EULA, OpenSSL and SSLeay licenses, IJG
JPEG Library README, Windows Media SDK EULA, or QuickTime SDK EULA, the
licensors of this Program grant you additional
permission to convey the resulting work. Corresponding Source for a
non-source form of such a combination shall include the source code for
the parts of OpenSSL and IJG JPEG Library used as well as that of the covered
work.

You can contact Cyan Worlds, Inc. by email legal@cyan.com
 or by snail mail at:
      Cyan Worlds, Inc.
      14617 N Newport Hwy
      Mead, WA   99021

 *==LICENSE==* """
 
"""
Module: ExplorersEmporiumDoorOpenRespond
Age: ExplorersEmporium
Date: May 2024
Author: Seejay
"""

from Plasma import *
from PlasmaTypes import *

doorOpenVarName = ptAttribString(1, "Door Open Age SDL Var Name")
doorPreviouslyOpenVarName = ptAttribString(2, "Door Previously Open Age SDL Var Name")
openDoorResponder = ptAttribResponder(3, "Responder to open the door")
unlockAndOpenDoorResponder = ptAttribResponder(4, "Responder to unlock and open the door")
closeDoorResponder = ptAttribResponder(5, "Responder to close the door:")
vmFastFwd = ptAttribBoolean(6, "F-Forward on VM notify", default=True)
initFastFwd = ptAttribBoolean(7, "F-Forward on Init", default=True)
evalOnFirstUpdate = ptAttribBoolean(8, "Init SDL On First Update?", default=False)

class ExplorersEmporiumDoorOpenRespond(ptResponder):
    """Runs a given responder based on the values of two SDL booleans"""

    def __init__(self):
        ptResponder.__init__(self)
        self.id = 22021003
        self.version = 1

    def OnFirstUpdate(self):
        if evalOnFirstUpdate.value:
            self._Setup()

    def OnServerInitComplete(self):
        if not evalOnFirstUpdate.value:
            self._Setup()

    def _Setup(self):
        ageSDL = PtGetAgeSDL()
        ageSDL.setFlags(doorOpenVarName.value, 1, 1)
        ageSDL.sendToClients(doorOpenVarName.value)
        ageSDL.setNotify(self.key, doorOpenVarName.value, 0.0)
        
        ageSDL.setFlags(doorPreviouslyOpenVarName.value, 1, 1)
        ageSDL.sendToClients(doorPreviouslyOpenVarName.value)
        
        try:
            self._Execute(ageSDL[doorOpenVarName.value][0], ageSDL[doorPreviouslyOpenVarName.value][0], initFastFwd.value)
        except LookupError:
            PtDebugPrint(f"xAgeSDLBoolRespond._Setup():\tVariable '{doorOpenVarName.value}' is invalid on object '{self.sceneobject.getName()}'")

    def OnSDLNotify(self, VARname, SDLname, playerID, tag):
        if VARname != doorOpenVarName.value:
            return

        ageSDL = PtGetAgeSDL()
        doorOpen = ageSDL[doorOpenVarName.value][0]
        doorPreviouslyOpen = ageSDL[doorPreviouslyOpenVarName.value][0]
        PtDebugPrint(f"ExplorersEmporiumDoorOpenRespond.OnSDLNotify():\tVARname:{VARname}, SDLname:{SDLname}, value:{doorOpen}, playerID:{playerID}")

        # A playerID of zero indicates a vault mangler change
        if playerID:
            try:
                avatar = PtGetAvatarKeyFromClientID(playerID).getSceneObject()
            except:
                avatar = None
            ff = tag.lower() == "fastforward"
        else:
            avatar = None
            ff = vmFastFwd.value
        self._Execute(doorOpen, doorPreviouslyOpen, ff, avatar)

    def _Execute(self, doorOpen, doorPreviouslyOpen, ff, avatar=None):
        ageSDL = PtGetAgeSDL()

        if doorOpen:
            if doorPreviouslyOpen:
                PtDebugPrint(f"ExplorersEmporiumDoorOpenRespond._Execute():\tRunning openDoorResponder on {self.sceneobject.getName()} ff={ff}")
                openDoorResponder.run(self.key, avatar=avatar, fastforward=ff)
            else:
                PtDebugPrint(f"ExplorersEmporiumDoorOpenRespond._Execute():\tRunning unlockAndOpenDoorResponder on {self.sceneobject.getName()} ff={ff}")
                unlockAndOpenDoorResponder.run(self.key, avatar=avatar, fastforward=ff)
                doorPreviouslyOpen = True
                PtDebugPrint(f"DEBUG: ExplorersEmporiumDoorOpenRespond._Execute():\tsetting SDL var {doorPreviouslyOpenVarName.value} to {doorPreviouslyOpen}")
                ageSDL[doorPreviouslyOpenVarName.value] = (doorPreviouslyOpen,)
        else:
            PtDebugPrint(f"ExplorersEmporiumDoorOpenRespond._Execute():\tRunning closeDoorResponder on {self.sceneobject.getName()} ff={ff}")
            closeDoorResponder.run(self.key, avatar=avatar, fastforward=ff)
