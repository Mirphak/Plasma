# -*- coding: utf-8 -*-
from Plasma import *

animDict = {'danse'      : ['Dance'],
            'fou'        : ['Crazy'],
            'echelle'    : ['LadderUpOn', 'LadderUp', 'LadderUp', 'LadderUp', 'LadderUpOff'],
            'ladderup2'  : ['LadderUpOn', 'LadderUp', 'LadderUpOff'],
            'descendre'  : ['LadderDownOn', 'LadderDown', 'LadderDown', 'LadderDown', 'LadderDownOff'],
            'ladderdown2': ['LadderDownOn', 'LadderDown', 'LadderDownOff'],
            'escalier'   : ['LadderUpOn', 'LadderUp', 'LadderUp', 'LadderUp', 'LadderUpOff','Walk'],
            'quoi'       : ['Crazy', 'Run', 'Laugh', 'Doh', 'Sneeze', 'WallSlide'],
            'nage'       : ['SwimFast', 'SwimFast', 'SwimFast'],
            'brasse'     : ['SwimSlow'],
            'moonwalk'   : ['WallSlide', 'WallSlide', 'WallSlide', 'WallSlide'],
            'zombie'     : ['Fall2', 'Fall2','Fall2', 'Fall', 'Fall', 'Fall2', 'Fall', 'Fall', 'GroundImpact'],
            'marteau'    : ['SideSwimLeft', 'SideSwimRight', 'SideSwimRight', 'SideSwimLeft'],
            'attente'    : ['TapFoot', 'StepLeft', 'LeanLeft', 'CrossArms', 'LookAround', 'StepRight', 'LeanRight','Peer'],
            'rire2'      : ['Point', 'Laugh', 'Shakefist', 'Thank'],
            'merci'      : ['Kneel', 'KiGlance', 'Thank'],
            'marche'     : ['Walk'],
            'cours'      : ['Run'],
            'recule'     : ['WalkBack'],
            'parler'     : ['Talk'],
            'pasdroite'  : ['StepRight'],
            'pasgauche'  : ['StepLeft'],
            # Other known simple animations
            "agree"               : ["Agree"],
            "amazed"              : ["Amazed"],
            "askquestion"         : ["AskQuestion"],
            "beckonbig"           : ["BeckonBig"],
            "beckonsmall"         : ["BeckonSmall"],
            "blowkiss"            : ["BlowKiss"],
            "bow"                 : ["Bow"],
            "callme"              : ["CallMe"],
            "cheer"               : ["Cheer"],
            "clap"                : ["Clap"],
            "cough"               : ["Cough"],
            "cower"               : ["Cower"],
            "cringe"              : ["Cringe"],
            "crossarms"           : ["CrossArms"],
            "cry"                 : ["Cry"],
            "doh"                 : ["Doh"],
            "flinch"              : ["Flinch"],
            "groan"               : ["Groan"],
            "groundimpact"        : ["GroundImpact"],
            "kneel"               : ["Kneel"],
            "ladderdown"          : ["LadderDown"],
            "ladderdownoff"       : ["LadderDownOff"],
            "ladderdownon"        : ["LadderDownOn"],
            "ladderup"            : ["LadderUp"],
            "ladderupoff"         : ["LadderUpOff"],
            "ladderupon"          : ["LadderUpOn"],
            "leanleft"            : ["LeanLeft"],
            "leanright"           : ["LeanRight"],
            "lookaround"          : ["LookAround"],
            "okay"                : ["Okay"],
            "overhere"            : ["OverHere"],
            "peer"                : ["Peer"],
            "point"               : ["Point"],
            "runningimpact"       : ["RunningImpact"],
            "salute"              : ["Salute"],
            "scratchhead"         : ["ScratchHead"],
            "shakefist"           : ["ShakeFist"],
            "shakehead"           : ["ShakeHead"],
            "shoo"                : ["Shoo"],
            "shrug"               : ["Shrug"],
            "sideswimleft"        : ["SideSwimLeft"],
            "sideswimright"       : ["SideSwimRight"],
            "slouchsad"           : ["SlouchSad"],
            "sneeze"              : ["Sneeze"],
            "stop"                : ["Stop"],
            "swimbackward"        : ["SwimBackward"],
            "swimfast"            : ["SwimFast"],
            "talkhand"            : ["TalkHand"],
            "tapfoot"             : ["TapFoot"],
            "taunt"               : ["Taunt"],
            "thx"                 : ["Thank"],
            "thumbsdown"          : ["ThumbsDown"],
            "thumbsdown2"         : ["ThumbsDown2"],
            "thumbsup"            : ["ThumbsUp"],
            "thumbsup2"           : ["ThumbsUp2"],
            "treadwaterturnleft"  : ["TreadWaterTurnLeft"],
            "treadwaterturnright" : ["TreadWaterTurnRight"],
            "turnleft"            : ["TurnLeft"],
            "turnright"           : ["TurnRight"],
            "wave"                : ["Wave"],
            "wavelow"             : ["WaveLow"],
            "winded"              : ["Winded"],
            "yawn"                : ["Yawn"],
            # and other ones ...
            "talk"          : ["Talk"],
            "fall"          : ["Fall"],
            "fall2"         : ["Fall2"],
            "standingjump"  : ["StandingJump"],
            "walkingjump"   : ["WalkingJump"],
            "runningjump"   : ["RunningJump"],
            "ballpushwalk"  : ["BallPushWalk"],
            # it continues :)
            "wallslide"     : ["WallSlide"],
            "kiglance"      : ["KiGlance"],
            # these might exist too
            "afk"           : ["Afk"],
            "cries"         : ["Cry"],
            "dontknow"      : ["Shrug"],
            "dunno"         : ["Shrug"],
            "laugh"         : ["Laugh"],
            "lol"           : ["Laugh"],
            "rotfl"         : ["Laugh"],
            "no"            : ["ShakeHead"],
            "sit"           : ["Sit"],
            "wavebye"       : ["Wave"],
            "yes"           : ["Agree"],
            # to be tried
            "buttontouch"         : ["ButtonTouch"],
            "doorbuttontouch"     : ["DoorButtonTouch"],
            #"fallinglinkout"      : ["FallingLinkOut"], # /!\bloquant
            #"fishbooklinkout"     : ["FishBookLinkOut"], # /!\bloquant
            "floorlevera"         : ["FloorLeverA"],
            "floorleveraup"       : ["FloorLeverAUp"],
            "globalscopegrab"     : ["GlobalScopeGrab"],
            "globalscopehold"     : ["GlobalScopeHold"],
            "globalscoperelease"  : ["GlobalScopeRelease"],
            "kihand"              : ["KiHand"],
            "kihandlonger"        : ["KiHandLonger"],
            "kibegin"             : ["KiBegin"],
            "kiend"               : ["KiEnd"],
            "kiglance"            : ["KiGlance"],
            "kitap"               : ["KITap"],
            "kiuse"               : ["KiUse"],
            #"linkout"             : ["LinkOut"], # /!\bloquant
            "pelletbookleft"      : ["PelletBookLeft"],
            "pelletbookright"     : ["PelletBookRight"],
            "pelletbookwait"      : ["PelletBookWait"],
            "personnallink"       : ["PersonnalLink"],
            "shootertrapactivate" : ["ShooterTrapActivate"],
            "shortidle"           : ["ShortIdle"],
            "shortleap"           : ["ShortLeap"],
            "sitfront"            : ["SitFront"],
            "sitidle"             : ["SitIdle"],
            "sitidleground"       : ["SitIdleGround"],
            "steponfloorplate"    : ["StepOnFloorPlate"],
            # ** Thoses should also work everywhere **
            "afkidle"                 : ["AFKIdle"],
            "blindsleverdown"         : ["BlindsLeverDown"],
            "blindsleverup"           : ["BlindsLeverUp"],
            "blndfrntleverdown"       : ["BlndFrntLeverDown"],
            "blndfrntleverup"         : ["BlndFrntLeverUp"],
            "bookaccept"              : ["BookAccept"],
            "bookacceptidle"          : ["BookAcceptIdle"],
            "bookoffer"               : ["BookOffer"],
            "bookofferfinish"         : ["BookOfferFinish"],
            "bookofferidle"           : ["BookOfferIdle"],
            "insertkihand"            : ["InsertKiHand"],
            "insertkihandlonger"      : ["InsertKiHandLonger"],
            "softlanding"             : ["SoftLanding"],
            "touchpellet"             : ["TouchPellet"],
            # ** Thoses only work in Ahnonay **
            "swimdockexit"            : ["SwimDockExit"],
            "swimsurfacedive"         : ["SwimSurfaceDive"],
            "swimunderwater"          : ["SwimUnderwater"],
            "valvewheelcw"            : ["ValveWheelCW"],
            "valvewheelccw"           : ["ValveWheelCCW"],
            # ** Thoses only work in Er'cana **
            "floorleverapullhard"     : ["FloorLeverAPullHard"],
            "floorleverapushhard"     : ["FloorLeverAPushHard"],
            "floorleverastuck"        : ["FloorLeverAStuck"],
            "floorleveraup"           : ["FloorLeverAUp"],
            "hatchlockedbelow"        : ["HatchLockedBelow"],
            "hrvstrleverbackward"     : ["HrvstrLeverBackward"],
            "hrvstrleverforward"      : ["HrvstrLeverForward"],
            "pushdebris"              : ["PushDebris"],
            # ** Thoses only work in Cleft **
            "cleftdropin"             : ["CleftDropIn"],
            "windmilllockedccw"       : ["WindmillLockedCCW"],
            "windmilllockedcw"        : ["WindmillLockedCW"],
            # ** Thoses only work in Gahreesen **
            "elevatorarrivingbottom"  : ["ElevatorArrivingBottom"],
            "elevatorarrivingtop"     : ["ElevatorArrivingTop"],
            "elevatorleavingbottom"   : ["ElevatorLeavingBottom"],
            "elevatorleavingtop"      : ["ElevatorLeavingTop"],
            "wallclimbdismountdown"   : ["WallClimbDismountDown"],
            "wallclimbdismountleft"   : ["WallClimbDismountLeft"],
            "wallclimbdismountright"  : ["WallClimbDismountRight"],
            "wallclimbdismountup"     : ["WallClimbDismountUp"],
            "wallclimbdown"           : ["WallClimbDown"],
            "wallclimbidle"           : ["WallClimbIdle"],
            "wallclimbleft"           : ["WallClimbleft"], # (pas WallClimbLeft !)
            "wallclimbright"          : ["WallClimbright"], # (pas WallClimbRight !)
            "wallclimbmountdown"      : ["WallClimbMountDown"],
            "wallclimbmountleft"      : ["WallClimbMountLeft"],
            "wallclimbmountright"     : ["WallClimbMountRight"],
            "wallclimbmountup"        : ["WallClimbMountUp"],
            # ** Thoses only work in Eder Gira **
            "fumerolclothjump"        : ["FumerolClothJump"],
            "fumerolledgeblast"       : ["FumerolLedgeBlast"],
            "fumerolrockblast"        : ["FumerolRockBlast"],
            "vertblastlevel01"        : ["VertBlastLevel01"],
            "vertblastlevel02"        : ["VertBlastLevel02"],
            "vertblastlevel03"        : ["VertBlastLevel03"],
            "vertblastlevel04"        : ["VertBlastLevel04"],
            "vertblastlevel05"        : ["VertBlastLevel05"],
            "vertblastlevel06"        : ["VertBlastLevel06"],
            # ** Thoses only work in Teledahn **
            "aquariumbuttonhold"      : ["AquariumButtonHold"],
            "aquariumbuttonpress"     : ["AquariumButtonPress"],
            "aquariumbuttonrelease"   : ["AquariumButtonRelease"],
            "clutchlevergeargrind"    : ["ClutchLeverGearGrind"],
            "dropoutofbucket"         : ["DropOutOfBucket"],
            "getinbucket"             : ["GetInBucket"],
            "getoutofbucket"          : ["GetOutOfBucket"],
            "hatchclose"              : ["HatchClose"],
            "hatchlockedabove"        : ["HatchLockedAbove"],
            "hatchlockedbelow"        : ["HatchLockedBelow"],
            "hatchopenabove"          : ["HatchOpenAbove"],
            "hatchopenbelow"          : ["HatchOpenBelow"],
            "noxiouscavedoorpullopen" : ["NoxiousCaveDoorPullOpen"],
            "noxiouscavedoorpushopen" : ["NoxiousCaveDoorPushOpen"],
            "noxiousdoorclose"        : ["NoxiousDoorClose"],
            "powertowerprimerbutton"  : ["PowerTowerPrimerButton"],
            "powertowerprimerlevers"  : ["PowerTowerPrimerLevers"],
            "secretwallbutton"        : ["SecretWallButton"],
           }

#
def Play(player, animName, nbTimes, gender=""):
    try :
        repet = int(nbTimes)
    except ValueError:
        repet = 0
    objKey = PtGetAvatarKeyFromClientID(player.getPlayerID())
    avatar = objKey.getSceneObject().avatar
    
    if gender == "b":
        gender = "kg"
    elif gender == "f":
        gender = "Female"
    elif gender == "m":
        gender = "Male"
    elif avatar.getAvatarClothingGroup() == 0:
        gender = "Male"
    else:
        gender = "Female"
    gAnimSeq = []
    try:
        animSeq = animDict[animName]
        gAnimSeq = [gender+x for x in animSeq]
    except KeyError:
        gAnimSeq = [gender+animName]
    except:
        return 0
    
    avatar.netForce(1)
    if animName in ("ladderup2", "ladderdown2"):
        avatar.oneShot(objKey, 1, 1, gAnimSeq[0], 0, 0)
        if len(gAnimSeq) > 2:
            for r in range(repet):
                avatar.oneShot(objKey, 1, 1, gAnimSeq[1], 0, 0)
            avatar.oneShot(objKey, 1, 1, gAnimSeq[2], 0, 0)
    else:
        for r in range(repet):
            for anim in gAnimSeq:
                avatar.oneShot(objKey, 1, 1, anim, 0, 0)
    return 1
