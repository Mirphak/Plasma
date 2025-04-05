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
Module: ExplorersEmporiumLockableDoor
Age: ExplorersEmporium
Date: May 2024
Author: Seejay
"""

from Plasma import *
from PlasmaTypes import *

# ---------
# max wiring
# ---------

actTrigger = ptAttribActivator(1, "Activator")
holdingKeyVarName = ptAttribString(2, "Holding Key Age SDL Var Name")
doorUnlockedVarName = ptAttribString(3, "Door Unlocked Age SDL Var Name")
doorOpenVarName = ptAttribString(4, "Door Open Age SDL Var Name")
doorPreviouslyOpenVarName = ptAttribString(5, "Door Previously Open Age SDL Var Name")
doorLockedResponder = ptAttribResponder(6, "Responder to run if door is locked")

class ExplorersEmporiumLockableDoor(ptResponder):

    def __init__(self):
        ptResponder.__init__(self)
        self.id = 22021002
        self.version = 1

    def OnFirstUpdate(self):
        if not holdingKeyVarName.value:
            PtDebugPrint("ERROR: ExplorersEmporiumLockableDoor.OnFirstUpdate():\tERROR: missing SDL var holding key name in max file")
        if not doorUnlockedVarName.value:
            PtDebugPrint("ERROR: ExplorersEmporiumLockableDoor.OnFirstUpdate():\tERROR: missing SDL var door unlocked name in max file")
        if not doorOpenVarName.value:
            PtDebugPrint("ERROR: ExplorersEmporiumLockableDoor.OnFirstUpdate():\tERROR: missing SDL var door open name in max file")
        if not doorPreviouslyOpenVarName.value:
            PtDebugPrint("ERROR: ExplorersEmporiumLockableDoor.OnFirstUpdate():\tERROR: missing SDL var door previously open name in max file")

    def OnServerInitComplete(self):
        ageSDL = PtGetAgeSDL()
        ageSDL.setFlags(holdingKeyVarName.value, 1, 1)
        ageSDL.sendToClients(holdingKeyVarName.value)
        ageSDL.setFlags(doorUnlockedVarName.value, 1, 1)
        ageSDL.sendToClients(doorUnlockedVarName.value)
        ageSDL.setFlags(doorOpenVarName.value, 1, 1)
        ageSDL.sendToClients(doorOpenVarName.value)
        ageSDL.setFlags(doorPreviouslyOpenVarName.value, 1, 1)
        ageSDL.sendToClients(doorPreviouslyOpenVarName.value)

    def OnNotify(self, state, id, events):
        # Is this notify something I should act on?
        if not state or id != actTrigger.id:
            return
        if not PtWasLocallyNotified(self.key):
            return
        else:
            if actTrigger.value:
                PtDebugPrint(f"DEBUG: ExplorersEmporiumLockableDoor.OnNotify():\tLocal player requesting change via {actTrigger.value[0].getName()}")
                pass
        # Error check
        if not holdingKeyVarName.value:
            PtDebugPrint("ERROR: ExplorersEmporiumLockableDoor.OnNotify():\tERROR: missing SDL var holding key name")
            return
        if not doorUnlockedVarName.value:
            PtDebugPrint("ERROR: ExplorersEmporiumLockableDoor.OnNotify():\tERROR: missing SDL var door unlocked name")
            return
        if not doorOpenVarName.value:
            PtDebugPrint("ERROR: ExplorersEmporiumLockableDoor.OnNotify():\tERROR: missing SDL var door open name")
            return
        if not doorPreviouslyOpenVarName.value:
            PtDebugPrint("ERROR: ExplorersEmporiumLockableDoor.OnNotify():\tERROR: missing SDL var door previously open name")
            return
        ageSDL = PtGetAgeSDL()
        holdingKey = ageSDL[holdingKeyVarName.value][0]
        doorUnlocked = ageSDL[doorUnlockedVarName.value][0]
        doorOpen = ageSDL[doorOpenVarName.value][0]
        doorPreviouslyOpen = ageSDL[doorPreviouslyOpenVarName.value][0]
        PtDebugPrint(f"DEBUG: ExplorersEmporiumLockableDoor.OnNotify():\tSDL var {holdingKeyVarName.value} is currently {holdingKey}")
        PtDebugPrint(f"DEBUG: ExplorersEmporiumLockableDoor.OnNotify():\tSDL var {doorUnlockedVarName.value} is currently {doorUnlocked}")
        PtDebugPrint(f"DEBUG: ExplorersEmporiumLockableDoor.OnNotify():\tSDL var {doorOpenVarName.value} is currently {doorOpen}")
        PtDebugPrint(f"DEBUG: ExplorersEmporiumLockableDoor.OnNotify():\tSDL var {doorPreviouslyOpenVarName.value} is currently {doorPreviouslyOpen}")
        if doorOpen:
            doorOpen = False
        else:
            if doorUnlocked:
                doorOpen = True
            else:
                if holdingKey:
                    doorUnlocked = True
                    doorOpen = True
                else:
                    self.TriggerDoorLockedResponder(events)
        if doorUnlocked != ageSDL[doorUnlockedVarName.value][0]:
            PtDebugPrint(f"DEBUG: ExplorersEmporiumLockableDoor.OnNotify():\tsetting SDL var {doorUnlockedVarName.value} to {doorUnlocked}")
            ageSDL[doorUnlockedVarName.value] = (doorUnlocked,)
        if doorOpen != ageSDL[doorOpenVarName.value][0]:
            PtDebugPrint(f"DEBUG: ExplorersEmporiumLockableDoor.OnNotify():\tsetting SDL var {doorOpenVarName.value} to {doorOpen}")
            ageSDL[doorOpenVarName.value] = (doorOpen,)

    def TriggerDoorLockedResponder(self, events):
        PtDebugPrint("DEBUG: ExplorersEmporiumLockableDoor.TriggerDoorLockedResponder():\tTriggering door locked responder")
        doorLockedResponder.run(self.key, avatar=PtFindAvatar(events))
