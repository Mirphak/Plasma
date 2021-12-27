# -*- coding: utf-8 -*-

"""
    Animations simples possibles:
        "Walk"
        "WalkBack"
        "LadderDown"
        "LadderDownOn"
        "LadderDownOff"
        "LadderUp"
        "LadderUpOn"
        "LadderUpOff"
        "SwimSlow"
        "SwimBackward"
        "BallPushWalk"
        "SwimFast"
        "TurnLeft"
        "TurnRight"
        "StepLeft"
        "StepRight"
        "SideSwimLeft"
        "SideSwimRight"
        "TreadWaterTurnLeft"
        "TreadWaterTurnRight"
        "GroundImpact"
        "RunningImpact"
        "Run"
        "Idle"

    ****
        plAGAnim *idle = fAvMod->FindCustomAnim("Idle");
        plAGAnim *walk = fAvMod->FindCustomAnim("Walk");
        plAGAnim *run = fAvMod->FindCustomAnim("Run");
        plAGAnim *walkBack = fAvMod->FindCustomAnim("WalkBack");
        plAGAnim *stepLeft = fAvMod->FindCustomAnim("StepLeft");
        plAGAnim *stepRight = fAvMod->FindCustomAnim("StepRight");
        plAGAnim *standingLeft = fAvMod->FindCustomAnim("TurnLeft");
        plAGAnim *standingRight = fAvMod->FindCustomAnim("TurnRight");
        plAGAnim *fall = fAvMod->FindCustomAnim("Fall");
        plAGAnim *standJump = fAvMod->FindCustomAnim("StandingJump");
        plAGAnim *walkJump = fAvMod->FindCustomAnim("WalkingJump");
        plAGAnim *runJump = fAvMod->FindCustomAnim("RunningJump");
        plAGAnim *groundImpact = fAvMod->FindCustomAnim("GroundImpact");
        plAGAnim *runningImpact = fAvMod->FindCustomAnim("RunningImpact");
        plAGAnim *movingLeft = nil; // fAvMod->FindCustomAnim("LeanLeft");
        plAGAnim *movingRight = nil; // fAvMod->FindCustomAnim("LeanRight");
        plAGAnim *pushWalk = fAvMod->FindCustomAnim("BallPushWalk");
    ****
        'anim':(Animer, ["[animation name] [n]:", 
            " where [animation name] is in:", 
            "    {ladderup/ladderdown/climbup/climbdown/stairs", 
            "    /walk/run/back/moonwalk/swim", 
            "    /dance/crazy/what/zomby/hammer/wait/laugh/thank/talk}.", 
            " and [n] is the number of times you want to do."]),

"""
"""
animDict = {'danse'      : ['Dance'],
            'fou'        : ['Crazy'],
            'echelle'    : ['LadderUpOn', 'LadderUp', 'LadderUp', 'LadderUp', 'LadderUpOff'],
            'ladderup'   : ['LadderUpOn', 'LadderUp', 'LadderUpOff'],
            'descendre'  : ['LadderDownOn', 'LadderDown', 'LadderDown', 'LadderDown', 'LadderDownOff'],
            'ladderdown' : ['LadderDownOn', 'LadderDown', 'LadderDownOff'],
            'escalier'   : ['LadderUpOn', 'LadderUp', 'LadderUp', 'LadderUp', 'LadderUpOff','Walk'],
            'quoi'       : ['Crazy', 'Run', 'Laugh', 'Doh', 'Sneeze', 'WallSlide'],
            'nage'       : ['SwimFast', 'SwimFast', 'SwimFast'],
            'brasse'     : ['SwimSlow'],
            'moonwalk'   : ['WallSlide', 'WallSlide', 'WallSlide', 'WallSlide'],
            'zombie'     : ['Fall2', 'Fall2','Fall2', 'Fall', 'Fall', 'Fall2', 'Fall', 'Fall', 'GroundImpact'],
            'marteau'    : ['SideSwimLeft', 'SideSwimRight', 'SideSwimRight', 'SideSwimLeft'],
            'attente'    : ['TapFoot', 'StepLeft', 'LeanLeft', 'CrossArms', 'LookAround', 'StepRight', 'LeanRight','Peer'],
            'rire'       : ['Point', 'Laugh', 'Shakefist', 'Thank'],
            'merci'      : ['Kneel', 'KiGlance', 'Thank'],
            'marche'     : ['Walk'],
            'cours'      : ['Run'],
            'recule'     : ['WalkBack'],
            'parler'     : ['Talk'],
            'pasdroite'  : ['StepRight'],
            'pasgauche'  : ['StepLeft'],
            }
"""

from Plasma import *
import xSave

#
animDict = {
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
        "crazy"               : ["Crazy"], 
        "cringe"              : ["Cringe"], 
        "crossarms"           : ["CrossArms"], 
        "cry"                 : ["Cry"], 
        "dance"               : ["Dance"], 
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
        "laugh"               : ["Laugh"], 
        "leanleft"            : ["LeanLeft"], 
        "leanright"           : ["LeanRight"], 
        "lookaround"          : ["LookAround"], 
        "okay"                : ["Okay"], 
        "overhere"            : ["OverHere"], 
        "peer"                : ["Peer"], 
        "point"               : ["Point"], 
        "run"                 : ["Run"], 
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
        "stepleft"            : ["StepLeft"], 
        "stepright"           : ["StepRight"], 
        "stop"                : ["Stop"], 
        "swimbackward"        : ["SwimBackward"], 
        "swimfast"            : ["SwimFast"], 
        "swimslow"            : ["SwimSlow"], 
        "talkhand"            : ["TalkHand"], 
        "tapfoot"             : ["TapFoot"], 
        "taunt"               : ["Taunt"], 
        "thank"               : ["Thank"], 
        "thumbsdown"          : ["ThumbsDown"], 
        "thumbsdown2"         : ["ThumbsDown2"], 
        "thumbsup"            : ["ThumbsUp"], 
        "thumbsup2"           : ["ThumbsUp2"], 
        "treadwaterturnleft"  : ["TreadWaterTurnLeft"], 
        "treadwaterturnright" : ["TreadWaterTurnRight"], 
        "turnleft"            : ["TurnLeft"], 
        "turnright"           : ["TurnRight"], 
        "walk"                : ["Walk"], 
        "walkback"            : ["WalkBack"], 
        "wave"                : ["Wave"], 
        "wavelow"             : ["WaveLow"], 
        "winded"              : ["Winded"], 
        "yawn"                : ["Yawn"], 
        #"ballpushwalk"        : ["BallPushWalk"], 
        #"idle"                : ["Idle"], 
}

# Noms alternatifs des animations
altAnim = {
    "climbdown" :["climbdown" , "descendre" ,                ],
    "climbup"   :["climbup"   , "echelle"   , "climb"        ],
    "crazy"     :["crazy"     , "fou"       ,                ],
    "dance"     :["dance"     , "danse"     ,                ],
    "hammer"    :["hammer"    , "marteau"   ,                ],
    "laugh"     :["laugh"     , "rire"      ,                ],
    "ladderdown":["ladderdown",                              ],
    "ladderup"  :["ladderup"  ,                              ],
    "moonwalk"  :["moonwalk"  ,                              ],
    "run"       :["run"       , "cours"     ,                ],
    "stairs"    :["stairs"    , "escalier"  ,                ],
    "stepleft"  :["stepleft"  , "pasgauche" ,                ],
    "stepright" :["stepright" , "pasdroite" ,                ],
    "swim"      :["swim"      , "nage"      ,                ],
    "swimslow"  :["swimslow"  , "brasse"    ,                ],
    "talk"      :["talk"      , "parler"    ,                ],
    "thank"     :["thank"     , "merci"     , "thanks"       ],
    "wait"      :["wait"      , "attente"   ,                ],
    "walk"      :["walk"      , "marche"    ,                ],
    "walkback"  :["walkback"  , "recule"    , "back"      ,  ],
    "what"      :["what"      , "quoi"      ,                ],
    "zomby"     :["zomby"     , "zombie"    , "ombie", "omby"],
    
    "agree"               : ["agree", "yes", "oui"], 
    "amazed"              : ["amazed", "etonne"], 
    "askquestion"         : ["askquestion"], 
    "ballpushwalk"        : ["ballpushwalk"], 
    "beckonbig"           : ["beckonbig"], 
    "beckonsmall"         : ["beckonsmall"], 
    "blowkiss"            : ["blowkiss"], 
    "bow"                 : ["bow"], 
    "callme"              : ["callme"], 
    "cheer"               : ["cheer"], 
    "clap"                : ["clap"], 
    "cough"               : ["cough"], 
    "cower"               : ["cower"], 
    "cringe"              : ["cringe"], 
    "crossarms"           : ["crossarms"], 
    "cry"                 : ["cry", "cries"], 
    "doh"                 : ["doh"], 
    "fall"                : ["fall"], 
    "fall2"               : ["fall2"], 
    "flinch"              : ["flinch"], 
    "groan"               : ["groan"], 
    "groundimpact"        : ["groundimpact"], 
    "kiglance"            : ["kiglance"], 
    "kneel"               : ["kneel"], 
    "ladderdown"          : ["ladderdown"], 
    "ladderdownoff"       : ["ladderdownoff"], 
    "ladderdownon"        : ["ladderdownon"], 
    "ladderup"            : ["ladderup"], 
    "ladderupoff"         : ["ladderupoff"], 
    "ladderupon"          : ["ladderupon"], 
    "laugh"               : ["laugh", "lol", "rotfl"], 
    "leanleft"            : ["leanleft"], 
    "leanright"           : ["leanright"], 
    "lookaround"          : ["lookaround"], 
    "okay"                : ["okay"], 
    "overhere"            : ["overhere"], 
    "peer"                : ["peer"], 
    "point"               : ["point"], 
    "runningimpact"       : ["runningimpact"], 
    "runningjump"         : ["runningjump"], 
    "salute"              : ["salute"], 
    "scratchhead"         : ["scratchhead"], 
    "shakefist"           : ["shakefist"], 
    "shakehead"           : ["shakehead", "no", "non"], 
    "shoo"                : ["shoo"], 
    "shrug"               : ["shrug", "dontknow", "dunno"], 
    "sideswimleft"        : ["sideswimleft"], 
    "sideswimright"       : ["sideswimright"], 
    "sit"                 : ["sit"], 
    "slouchsad"           : ["slouchsad"], 
    "sneeze"              : ["sneeze"], 
    "standingjump"        : ["standingjump"], 
    "stop"                : ["stop"], 
    "swimbackward"        : ["swimbackward"], 
    "swimfast"            : ["swimfast"], 
    "talkhand"            : ["talkhand"], 
    "tapfoot"             : ["tapfoot"], 
    "taunt"               : ["taunt"], 
    "thx"                 : ["thank"], 
    "thumbsdown"          : ["thumbsdown"], 
    "thumbsdown2"         : ["thumbsdown2"], 
    "thumbsup"            : ["thumbsup"], 
    "thumbsup2"           : ["thumbsup2"], 
    "treadwaterturnleft"  : ["treadwaterturnleft"], 
    "treadwaterturnright" : ["treadwaterturnright"], 
    "turnleft"            : ["turnleft"], 
    "turnright"           : ["turnright"], 
    "walkingjump"         : ["walkingjump"], 
    "wallslide"           : ["wallslide"], 
    "wave"                : ["wave", "wavebye"], 
    "wavelow"             : ["wavelow"], 
    "winded"              : ["winded"], 
    "yawn"                : ["yawn"], 

}

#
travelAnimList = ("climbdown", "climbup", "ladderdown", "ladderup", "run", "stairs", "stepleft", "stepright", "swimslow", "swim", "walk", "walkback")

#
def RetreaveAnimCmdName(altCmdName):
    for k, v in altAnim.items():
        if altCmdName.lower() in v:
            return str(k)
    return None

#
def Play(player, animName, nbTimes=1, duration=1):
    animName = animName.lower()
    try :
        repet = int(nbTimes)
    except ValueError:
        repet = 0
    try :
        time = float(duration)
    except ValueError:
        time = 1.0
    objKey = PtGetAvatarKeyFromClientID(player.getPlayerID())
    avatar = objKey.getSceneObject().avatar

    if avatar.getAvatarClothingGroup() == 0:
        gender = "Male"
    else:
        gender = "Female"
    gAnimSeq = []
    try:
        animSeq = animDict[animName]
        gAnimSeq = map(lambda x: gender+x, animSeq)
    except KeyError:
        gAnimSeq = [gender+animName]
    except:
        return 0
    
    avatar.netForce(1)
    """
    if animName in ("ladderup", "ladderdown"):
        avatar.oneShot(objKey, 1, 1, gAnimSeq[0], 0, 0)
        for r in range(repet):
            avatar.oneShot(objKey, 1, 1, gAnimSeq[1], 0, 0)
        avatar.oneShot(objKey, 1, 1, gAnimSeq[2], 0, 0)
    else:
        for r in range(repet):
            for anim in gAnimSeq:
                avatar.oneShot(objKey, 1, 1, anim, 0, 0)
    """
    for r in range(repet):
        for anim in gAnimSeq:
            avatar.oneShot(objKey, time, 1, anim, 0, 0)
    return 1

#
def AutoSaveMat(self, player):
    xSave.WriteMatrix44(self, player, None, "auto")

#
def AutoWarp(self, player):
    xSave.WarpToSaved(self, player, None, "auto")

# Faire faire une animation a l'avatar demandeur
def Animer(self, cFlags, args = []):
    #self.chatMgr.AddChatLine(None, "> Animer", 3)
    if len(args) < 2:
        return 0
    myself = PtGetLocalPlayer()
    player = args[0]
    #PtSendRTChat(myself, [player], str(args) , 1)
    params = args[1].split()
    if len(params) < 2:
        return 0
    if not isPlayerInAge(player):
        SendChatMessage(self, myself, [player], "You must be in my age, use link to join me.", cFlags.flags)
        return 1
    animName = params[0]
    nbTimes = params[1]
    ret = xAnim.Play(player, animName, nbTimes)
    if ret and animName in travelAnimList:
        AutoSaveMat(self, player)
        AutoWarp(self, player)
    return ret

#
"""
    a) avec pickle:
    import pickle
    l = [1,2,3,4]
    with open("test.txt", "wb") as fp:   #Pickling
      pickle.dump(l, fp)
    
    with open("test.txt", "rb") as fp:   # Unpickling
      b = pickle.load(fp)
    
    # b <- [1, 2, 3, 4]

    b) basiquement, sous forme de texte
    score = [1,2,3,4,5]

    with open("file.txt", "w") as f:
        for s in score:
            f.write(str(s) +"\n")

    with open("file.txt", "r") as f:
      for line in f:
        score.append(int(line.strip()))
"""