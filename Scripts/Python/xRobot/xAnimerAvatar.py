def AnimeAv(parametres):
    """danse:1:moi Lance une animation dans la liste ci-dessous ou standard:nombre de fois:avatar ou tout le monde si vide"""
    params = parametres.split(':')
    animation = params[0]
    try :
        repet = int(params[1])
    except ValueError:
        repet = 0
    players = params[2]
    ExcludeList = []
    ExcludeList = ["Lyrobot","MagicBot"]    #,"MimiBot"
      
       
    maleMoves = {'danse' : ['MaleDance'],
                 'fou' : ['MaleCrazy'],
                 'echelle' : ['MaleLadderUpOn', 'MaleLadderUp', 'MaleLadderUp', 'MaleLadderUp', 'MaleLadderUpOff'],
                 'descendre' : ['MaleLadderDownOn','MaleLadderDown', 'MaleLadderDown', 'MaleLadderDown', 'MaleLadderDownOff'],
                 'escalier' : ['MaleLadderUpOn', 'MaleLadderUp', 'MaleLadderUp', 'MaleLadderUp', 'MaleLadderUpOff','MaleWalk'],
                 'quoi' : ['MaleCrazy', 'MaleRun', 'MaleLaugh', 'MaleDoh', 'MaleSneeze', 'MaleWallSlide'],
                 'nage' : ['MaleSwimFast', 'MaleSwimFast', 'MaleSwimFast'],
                 'moonwalk' : ['MaleWallSlide', 'MaleWallSlide','MaleWallSlide','MaleWallSlide'],
                 'zombie' : ['MaleFall2','MaleFall2','MaleFall2','MaleFall','MaleFall', 'MaleFall2', 'MaleFall', 'MaleFall', 'MaleGroundImpact'],
                 'marteau' : ['MaleSideSwimLeft', 'MaleSideSwimRight', 'MaleSideSwimRight', 'MaleSideSwimLeft'],
                 'attente': ['MaleTapFoot', 'MaleStepLeft', 'MaleLeanLeft', 'MaleCrossArms', 'MaleLookAround', 'MaleStepRight', 'MaleLeanRight','MalePeer'],
                 'rire': ['MalePoint', 'MaleLaugh', 'MaleShakefist', 'MaleThank'],
                 'merci': ['MaleKneel', 'MaleKiGlance', 'MaleThank'],
                 'marche':['MaleWalk'],
                 'cours' :['MaleRun'],
                 'recule' :['MaleWalkBack'],
                 'parler':['MaleTalk']}
                
    femaleMoves = {'danse' : ['FemaleDance'],
                   'fou' : ['FemaleCrazy'],
                   'echelle' : ['FemaleLadderUpOn', 'FemaleLadderUp', 'FemaleLadderUp', 'FemaleLadderUp', 'FemaleLadderUpOff'],
                   'descendre' : ['FemaleLadderDownOn','FemaleLadderDown', 'FemaleLadderDown', 'FemaleLadderDown', 'FemaleLadderDownOff'],
                   'escalier' : ['FemaleLadderUpOn', 'FemaleLadderUp', 'FemaleLadderUp', 'FemaleLadderUp', 'FemaleLadderUpOff','FemaleLadderUpOff'],
                   'quoi' : ['FemaleCrazy', 'FemaleRun', 'FemaleLaugh', 'FemaleDoh', 'FemaleSneeze', 'FemaleWallSlide'],
                   'nage' : ['FemaleSwimFast', 'FemaleSwimFast', 'FemaleSwimFast'],
                   'moonwalk' : ['FemaleWallSlide', 'FemaleWallSlide','FemaleWallSlide','FemaleWallSlide'],
                   'zombie' : ['FemaleFall2','FemaleFall2','FemaleFall2','FemaleFall','FemaleFall', 'FemaleFall2', 'FemaleFall', 'FemaleFall', 'FemaleGroundImpact'],
                   'marteau' : ['FemaleSideSwimLeft', 'FemaleSideSwimRight', 'FemaleSideSwimRight', 'FemaleSideSwimLeft'],
                   'attente': ['FemaleTapFoot', 'FemaleStepLeft', 'FemaleLeanLeft', 'FemaleCrossArms', 'FemaleLookAround', 'FemaleStepRight', 'FemaleLeanRight','FemalePeer'],
                   'rire': ['FemalePoint', 'FemaleLaugh', 'FemaleShakefist', 'FemaleThank'],
                   'merci': ['FemaleKneel', 'FemaleKiGlance', 'FemaleThank'],
                   'marche':['FemaleWalk'],
                   'cours' :['FemaleRun'],
                   'recule' :['FemaleWalkBack'],
                   'parler':['FemaleTalk']}
                  
    if (players ==''):
        agePlayers = []
        agePlayers = SCOListAvatars()
        for player in agePlayers:
            avatar = player.avatar
            objKey = player.getKey()
            nom = PtGetClientName(objKey)
            if (nom not in ExcludeList):
                gender = avatar.getAvatarClothingGroup()
                try:
                    if (gender == 0):
                        animList = maleMoves[animation]
                    else:
                        animList = femaleMoves[animation]
                except KeyError:
                    if (gender == 0):
                        animList = ["Male"+animation]
                    else:
                        animList = ["Female"+animation]
                player.netForce(1)
                for r in range(repet) :
                    for anim in animList:
                        avatar.oneShot(objKey, 1, 1, anim, 0, 0)
    else:
        player = SCOAvatar(players)
        if player != None:
            avatar = player.avatar
            objKey = player.getKey()
            nom = PtGetClientName(objKey)
            if players == 'moi' or (nom not in ExcludeList):
                gender = avatar.getAvatarClothingGroup()
                try:
                    if (gender == 0):
                        animList = maleMoves[animation]
                    else:
                        animList = femaleMoves[animation]
                except KeyError:
                    if (gender == 0):
                        animList = ["Male"+animation]
                    else:
                        animList = ["Female"+animation]
                player.netForce(1)
                for r in range(repet) :
                    for anim in animList:
                        avatar.oneShot(objKey, 1, 1, anim, 0, 0)
