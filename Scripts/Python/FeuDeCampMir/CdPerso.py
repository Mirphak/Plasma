# -*- coding: utf-8 -*-
""" Yodawave                                                                                                                                          CdPerso

"""

from Plasma import*
import Plasma
from math import*

def CdResponder( Object ="",age="", No=100, stateidx = None):#                  ajouter age si obj pas Ds age courant marche pas
    try :
        obj=PtFindSceneobject(Object,age)
        responders =obj.getResponders()
        resp=responders[No]
        key=obj.getKey()

        nt = ptNotify(key)
        nt.clearReceivers()
        nt.addReceiver(resp)
        nt.netPropagate(1)
        nt.netForce(1)
        if stateidx != None:
            nt.addResponderState(stateidx)#                                  initialise le sous Resp                                     nt.setType(PtNotificationType.kResponderFF)            A voir
        nt.setActivate(1.0)
        nt.send()
    except :
        PtSendKIMessage(26, "CdResponder   Error:   "   )

def CdResponderScObject(Sceneobject, No=100, stateidx = None):
    """      !!!!!!!!!             si Cd trop rapide apres   positionement de Sceneobject   il peut y avoir des erreurs
    resp=responders[No] :IndexError: list index out of range
    nt.addReceiver(resp)  :  UnboundLocalError: local variable 'resp' referenced before assignment    """
    responders = Sceneobject.getResponders()
#    PtSendKIMessage(26,"CdResponderScObject     "+ str (responders) )
    try:
        resp=responders[No]        
        key=Sceneobject.getKey()
        nt = ptNotify(key)
        nt.clearReceivers()
        nt.addReceiver(resp)
        nt.netPropagate(1)
        nt.netForce(1)
        if stateidx != None:
            nt.addResponderState(stateidx)#                                  initialise le sous Resp
        nt.setActivate(1.0)
        nt.send()
    except:
        PtSendKIMessage(26, "CdResponderScObject   Error:   " +  str( Sceneobject.getName() )  )
        pass
#***********************************************************************************************************************************************************************************************

def IDPlayerDsAge(AvecMoi = 0 ):
    """renvoi la list int() des IDPlayer  present dans l age        me valider  si   AvecMoi = 1 """
    try:
        ListIDPlayer = []
        if AvecMoi :
            ListIDPlayer.append ( int ( PtGetLocalClientID()  ) ) #                 pour  me valider PtGetLocalClientID       si   AvecMoi = 1
        for Player in PtGetPlayerList() :
            ListIDPlayer.append ( int ( Player.getPlayerID() ) )    
        return ListIDPlayer
    except :
        PtSendKIMessage(26, "IDPlayerDsAge   Error:   "   )

def IDavatarOk(NoID = 0):
    """verifie que le NoID  est bien present dans l'age si non renvoie 0
    MODEL
    if not IDavatarOk(IDAvatar) :
        return """
    try:
        if int(NoID) in  IDPlayerDsAge(1) :
           return NoID
        else :
            PtSendKIMessage(26, "IDavatar Absent de l age  :  "  + str ( NoID )  )
            return 0
    except :
        PtSendKIMessage(26, "IDavatarOk   Error:   "   )

def PositionAvatar(NoID=0, ):
    try:
        VectPosAvatar = PtGetAvatarKeyFromClientID( IDavatarOk(NoID) ).getSceneObject().getLocalToWorld().getTranslate(ptVector3())
        return  [VectPosAvatar.getX() , VectPosAvatar.getY() , VectPosAvatar.getZ() ]
    except :
        PtSendKIMessage(26, "PositionAvatar   Error:   "   )

def TuplePositionAvatar(NoID=0, ):
    try:
        VectPosAvatar = PtGetAvatarKeyFromClientID( IDavatarOk(NoID) ).getSceneObject().getLocalToWorld().getTranslate(ptVector3())
        return  (VectPosAvatar.getX() , VectPosAvatar.getY() , VectPosAvatar.getZ() )
    except :
        PtSendKIMessage(26, "TuplePositionAvatar   Error:   "   )
#***********************************************************************************************************************************************************************************************
#    Sceneobject = PtFindSceneobject("SkyDome","Minkata")
#    Sceneobject.netForce(1)
#    Sceneobject.draw.netForce(1)
#    Sceneobject.draw.enable(0)
#    Sceneobject.physics.netForce(1)
#    Sceneobject.physics.enable(1)


def FindSOName(soName):
    try:
        import re
        cond = "^.*" + soName.replace("*", ".*") + ".*$"
        try:
            pattern = re.compile(cond, re.IGNORECASE)
        except:
            return list()
        strList = soName.split("*")
        nameList = list()
        for str in strList:
            nameList.extend([so.getName() for so in PtFindSceneobjects(str)])
        nameList = list(set(nameList))
        nameList = [x for x in nameList if pattern.match(x) is not None]
        return nameList
    except :
        PtSendKIMessage(26, "FindSOName   Error:   "   )

def FindSOLike(soName):
    try:
        nameList = FindSOName(soName)
        soList = list()
        for soName in nameList:
            sol = PtFindSceneobjects(soName)
            soList.extend(sol)
        return soList
    except :
        PtSendKIMessage(26, "FindSOLike   Error:   "   )

"""   !!!!!!!!       attention au   espaces                      GroundPlaneVis , 1             !=                 (    GroundPlaneVis,1    ) OK                           !!! un groupe d objet                                /ro   """
def RetireObjs(  Object="" , physics=1 ):
    try:
        ListSceneobjects = PtFindSceneobjects(Object)
#        ListSceneobjects = FindSOLike(Object)
        for Sceneobject in ListSceneobjects:
#            PtSendKIMessage(26, str ( Sceneobject.getName()  )  )
            RetireSceneobject(Sceneobject , physics    )
    except :
        PtSendKIMessage(26, "RetireObjs   Error  :   "  + str ( Sceneobject.getName() ) )

def RetireSceneobject(Sceneobject = None, physics=1):
    try:
        if Sceneobject  is not None:
            Sceneobject.netForce(1)
            Sceneobject.draw.netForce(1)
            Sceneobject.draw.enable(0)
            Sceneobject.physics.netForce(1)
            if physics :
                Sceneobject.physics.enable(physics)
#                PtSendKIMessage(26, "1111111111111111"   )
            else :
                Sceneobject.physics.suppress(1) #OK
#                Sceneobject.physics.disable()  # OK        ******************************************************************************************************************
#                Sceneobject.physics.enable(0) # OK
#                Sceneobject.physics.disableCollision()
#                PtSendKIMessage(26, "000000000000000000"   )
                
#                Sceneobject.physics.suppress(0)

#            PtSendKIMessage(26,"Retire  Sceneobject:  NameSceneobject  :"+str ( Sceneobject.getName()  ))
        else :
            PtSendKIMessage(26,"Retire  Sceneobject = None  NameSceneobject  :"+str ( Sceneobject.getName()  ))
    except :
        PtSendKIMessage(26,"   Error    RetireSceneobject  : " + str (  Sceneobject.getName()  )) 


"""  PtFindSceneobject    au singulier   ne fontionne pas sans l'age                                    voir  Ptdraw   """
def RetireObj(Object="", age="", physics=1):
    """                                                                          Object  doit etre un Nom d"objet Valide ,               1 seul objet               age obligatoire pour certain objet    """
    try:
        Sceneobject = PtFindSceneobject(Object,age)#     valable pour  1 seul objet
        if Sceneobject  is not None:
            Sceneobject.netForce(1)
            Sceneobject.draw.netForce(1)
            Sceneobject.draw.enable(0)
            Sceneobject.physics.netForce(1)
            Sceneobject.physics.enable(physics)
        else :
            PtSendKIMessage(26,"RetireObj =None  NameSceneobject  :"+str ( Sceneobject.getName()  ))
    except :
        PtSendKIMessage(26,"   Error    RetireObj  : "+str (Object)) 

def RetirePhysicsObj(Object="", age="",):
    """ Object  doit etre un Nom d"objet Valide ,     age est facutatif si absent enleve tout les objets ayant un Nom d"objet Valide                1 seul objet"""
    try:
        Sceneobject = PtFindSceneobject(Object,age)
        Sceneobject.netForce(1)
        Sceneobject.physics.netForce(1)
        Sceneobject.physics.suppress(1) #OK
#        Sceneobject.physics.disable()  # OK        ******************************************************************************************************************
#        Sceneobject.physics.enable(0) # OK
#        Sceneobject.physics.disableCollision()
    except :
        PtSendKIMessage(26,"   Error     RetirePhysicsObj  :"+str (Object))

#**********************************************************************************************

def AjouteObjs(Object="",  physics=1):
    try :
        ListSceneobjects = PtFindSceneobjects(Object)
        for Sceneobject in ListSceneobjects:
#            PtSendKIMessage(26, str ( Sceneobject.getName()  )  )
            AjouteSceneobject( Sceneobject ,   physics)
    except :
        PtSendKIMessage(26,"Erreur AjouteObjs:")

def AjouteSceneobject(Sceneobject = None, physics=1):
#    PtSendKIMessage(26,"AjouteObj   NameSceneobject  :" + str ( Sceneobject.getName()  ))
    try:
        if Sceneobject  is not None:
            Sceneobject.netForce(1)
            Sceneobject.draw.netForce(1)
            Sceneobject.draw.enable(1)
            Sceneobject.physics.netForce(1)
            Sceneobject.physics.enable(physics)
        else :
            PtSendKIMessage(26,"AjouteSceneobject   Sceneobject  is  None  :"  )
    except :
        PtSendKIMessage(26,"   Error    AjouteSceneobject  : "+str (  Sceneobject.getName()  )) 

def AjouteObj(Object="", age="", physics=1):
    """ si age est precise Ajoute  que  les Objets de l"age precise """
    """ Object  doit etre un Nom d"objet Valide ,     age est facutatif si absent Ajoute tout les objets ayant un Nom d"objet Valide """
    try:
        Sceneobject = PtFindSceneobject(Object,age)
        Sceneobject.netForce(1)
        Sceneobject.draw.netForce(1)
        Sceneobject.draw.enable(1)
        Sceneobject.physics.netForce(1)
        Sceneobject.physics.enable(physics)
    except :
        PtSendKIMessage(26,"Erreur AjouteObj           NameSceneobject  :"+str (Object))

#***********************************************************************************************************************************************************************************************
"""                                         A revoir         CdPerso.ChargeImage ( "KIimage0011" )
from ki import *
def ChargeImage( Img = "" ):#           charge une image du disque dur dans le KI    elle sera dans le dossier de l age courant
    try :
        CdKI =  xKI ()
        Image = PtLoadJPEGFromDisk( Img  + ".png",900, 600)#  Returns a pyImage of the specified file
        CdKI.BigKICreateJournalImage(Image)
    except :
        PtSendKIMessage(26,"Erreur ChargeImage:")
"""
#***********************************************************************************************************************************************************************************************

#    CdPerso.SetSDLPerso ( "YeeshaPage24" ,  1 )
def LSDL():
    try:
        listobjSDL=GetSDLPerso("all")
        file = open("listobj-SDL.txt", "w")
        file.write(listobjSDL)
        file.close()
        PtSendKIMessage(26, "LSLDL OK")
    except :
        PtSendKIMessage(26, "LSDL   Error:   "   )

def SetSDLPerso(name="",valeur=100):
    try:
        sdl=PtGetAgeSDL()
        sdl[name] = (valeur,)
        PtSendKIMessage(26,"name ="+str(name)+"             valeur ="+str(valeur))
    except :
        PtSendKIMessage(26, "SetSDLPerso   Error:   "   )

def SetSDLreltoPerso(name="",valeur=100 ):
    try:
        vault = ptVault()
        psnlSDL = vault.getPsnlAgeSDL()
        FoundValue = psnlSDL.findVar(name)#                 nom
        FoundValue.setInt(valeur)#                                        valeur
        vault.updatePsnlAgeSDL(psnlSDL)#                             met a jour la voute
        PtSendKIMessage(26,"name ="+str(name)+"             valeur ="+str(valeur))
    except :
        PtSendKIMessage(26, "SetSDLreltoPerso   Error:   "   )


def GetSDLPerso(varName):
    """----------------------------------------------------Adapté  pour présentation dans fichier       voir  xCheat
    GetSDL is used to get the value of an Age SDL variable by name.
    Expects one argument:
     (string) VariableName
    """
    try:
        if not varName:
    #        print("xCheat.GetSDL(): GetSDL takes one argument: SDL variable name is required.\n Use 'all' to list all variables for the current Age.")
            return "ok 82"
    
        ageName = Plasma.PtGetAgeName()
        try:
            ageSDL = Plasma.PtGetAgeSDL()
        except:
    #        print("xCheat.GetSDL(): Unable to retrieve SDL for '{}'.".format(ageName))
            return "ok 89"
    
        varList = []
        if varName == "all":
            ListSDL =" depart"
            ListSDL= ListSDL  + " essai \n "
            if ageName == "Personal":
                varRecord = Plasma.ptVault().getPsnlAgeSDL()
                if varRecord:
                    varList = varRecord.getVarList()
            else:
                vault = Plasma.ptAgeVault()
                if vault:
                    varRecord = vault.getAgeSDL()
                    if varRecord:
                        varList = varRecord.getVarList()
            if not varList:
    #            print("xCheat.GetSDL(): Couldn't retrieve SDL list.")
                return "ok 106"
            maxlen = len(max(varList, key=len))
            for var in varList:
                try:
                    if len(ageSDL[var]) == 0:
                        val = ""
                    else:
                        val = ageSDL[var][0]
    #                print("xCheat.GetSDL(): {:>{width}}  =  {}".format(var, val, width=maxlen))
                    ListSDL= ListSDL  +  "{:>{width}}  =  {}  \n".format(var, val, width=maxlen)
                except:
    #                print("xCheat.GetSDL(): Error retrieving value for '{}'.".format(var))
                    pass
            return "ok 118 \n" +  ageName + "\n" + ListSDL + "\n Fin"
        else:
            try:
                if len(ageSDL[varName]) == 0:
    #                print("xCheat.GetSDL():  SDL variable '{}' is not set.".format(varName))
                    pass
                else:
    #                print("xCheat.GetSDL(): {}  =  {}".format(varName, ageSDL[varName][0]))
                    pass
            except:
    #            print("xCheat.GetSDL(): SDL variable '{}' not found.".format(varName))
                return "ok 126"
            return "ok 128"
    except :
        PtSendKIMessage(26, "GetSDLPerso   Error:   "   )
        
#***********************************************************************************************************************************************************************************************

def AddPrp(page=""):
    try :
        PtConsoleNet("Nav.PageInNode   "+page , 1)
    except :
        PtSendKIMessage(26,"Erreur AddPrp:")
def DelPrp(page=""):
    try :
        PtConsoleNet("Nav.PageOutNode "+page , 1)
    except :
        PtSendKIMessage(26,"Erreur DelPrp:")

#***********************************************************************************************************************************************************************************************

def CalculMatRot( x, y, z ):
    try :
        RotX = ptMatrix44()
        RotY = ptMatrix44()
        RotZ = ptMatrix44()
        RotX.makeRotateMat(0,radians(x))
        RotY.makeRotateMat(1,radians(y))
        RotZ.makeRotateMat(2,radians(z))
        return  (RotX * RotY * RotZ)
    except :
        PtSendKIMessage(26,"Erreur CalculMatRot:")

def CalculVecRot( x, y, z ):
    try :
        RotObj = ptMatrix44()
        RotObj.rotate (0, radians (x))
        RotObj.rotate (1, radians (y))
        RotObj.rotate (2, radians (z))
        return RotObj
    except :
        PtSendKIMessage(26,"Erreur CalculVecRot:")
#***********************************************************************************************************************************************************************************************

def var_name(var):
    try :
        for name,value in list(globals().items()) :
            if value is var :
                return name
        return "?????"
    except :
        PtSendKIMessage(26,"Erreur var_name:")
#***********************************************************************************************************************************************************************************************

def PlaceObj ( NomObj="", Age=""  ,  NvCentre= (0, 0, 0), rot= (0, 0, 0), scale = (1, 1, 1), phy=1)  :
    try :
        NvCentreObj = ptMatrix44()
        NvCentreObj.translate ( ptVector3  (   NvCentre [0]   ,  NvCentre[1]    , NvCentre[2] )       ) 
        rotObj =CalculMatRot( *rot  )
        Scale = ptMatrix44()
        Scale.makeScaleMat(ptVector3 (   scale [0]   ,  scale[1]    , scale[2]    )    )
        NvCRS = NvCentreObj * rotObj * Scale
        PlaceSceneobjectNvCRS(PtFindSceneobject ( NomObj, Age  ),NvCRS, phy)
    except :
        PtSendKIMessage(26,"Erreur PlaceObj:" + str ( NomObj ) + "         " +  str ( Age ))

def PlaceObjet ( NomObj="", Age="",NvCentreObj= ptMatrix44(), rot= ptMatrix44(), scale = ptMatrix44(), phy=1):
    try :
        PlaceSceneobject( PtFindSceneobject (NomObj, Age) ,NvCentreObj, rot, scale, phy)
    except :
        PtSendKIMessage(26,"Erreur PlaceObjet:")

def PlaceObjets ( NomObj="", Age="",NvCentreObj= ptMatrix44(), rot= ptMatrix44(), scale = ptMatrix44(), phy=1):
    try :
        ListSceneobjects = PtFindSceneobjects(NomObj)
        for Sceneobject in ListSceneobjects:
            PlaceSceneobject(Sceneobject,NvCentreObj, rot, scale, phy)
    except :
        PtSendKIMessage(26,"Erreur PlaceObjets:")


def  PlaceSceneobject(Sceneobject,NvCentreObj= ptMatrix44(), rot= ptMatrix44(), scale = ptMatrix44(), phy=1):
    try :
        NvCRS = ptMatrix44()
        NvCRS = NvCentreObj * rot * scale
        PlaceSceneobjectNvCRS(Sceneobject,NvCRS,phy)
    except:
        PtSendKIMessage(26,"Erreur PlaceSceneobject   :  "  + str( Sceneobject.getName() )   )

def  PlaceSceneobjectNvCRS(Sceneobject,NvCRS= ptMatrix44(), phy=1):
    """         NvCRS    =    CentreObj * Rot * Scale              ou un seul des trois     voir 2  """
    try:
        Sceneobject.netForce(1)
        Sceneobject.draw.netForce(1)
        Sceneobject.draw.enable(1)
        Sceneobject.physics.netForce(1)
        Sceneobject.physics.enable(phy)
    #    Sceneobject.physics.disableCollision()
        Sceneobject.physics.warp (NvCRS)
    except:
        PtSendKIMessage(26,"Erreur PlaceSceneobjectNvCRS:")




def PlaceDicObj(DicObj={}, Offset = (0.0, 0.0, 0.0), rot= ptMatrix44(), SurAvatar = False , IDAvatar=20193822):
    """ positione les objets d'un DicObj={"AgePlusRotObj": "NomAge","NomObj":((Ox,Oy,Oz)(Rx,Ry,Rz)),  }       Nom :  ((offset)(rotation))                   Ajouter Scale
                                                                "Age" : "NomAge"  ,   "NomObj":(Ox,Oy,Oz)     """
    try:
        if "AgePlusRotObj" in DicObj  : 
            #   DicObj   avec une rotation  par objet
            Age = DicObj["AgePlusRotObj"]
            for NomObj, Valeur in DicObj.items():
                if NomObj != "AgePlusRotObj" :
                    rotObj = CalculMatRot(Valeur[1][0], Valeur[1][1], Valeur[1][2])
                    Vect = ptVector3 (Valeur[0][0]+Offset[0], Valeur[0][1]+Offset[1], Valeur[0][2]+Offset[2])#       Valeur = offset du dic  +  Offset des param
                    if SurAvatar==True:
                        if IDAvatar== PtGetLocalClientID():#                    recupere le SceneObj  de l avatar
                            RecoitObj = PtGetLocalAvatar()
                        else:
                            RecoitObj = PtGetAvatarKeyFromClientID(IDAvatar).getSceneObject()
                        NvPos = RecoitObj.getLocalToWorld()
                        NvPos.translate (Vect)
                        NvPos = NvPos * rotObj
                    else:
                        NvPos = ptMatrix44()
                        NvPos.translate(Vect)
                        NvPos = NvPos * rotObj
                    PlaceObjet (NomObj,Age,NvPos,  rot)
        else:
            Age = DicObj["Age"]
            for NomObj, Valeur in DicObj.items():
                if NomObj  != "Age"  : 
                    Vect = ptVector3 (Valeur[0]+Offset[0], Valeur[1]+Offset[1], Valeur[2]+Offset[2])#       Valeur = offset du dic  +  Offset des param
                    if SurAvatar==True:
                        if IDAvatar== PtGetLocalClientID():#                    recupere le SceneObj  de l avatar
                            RecoitObj = PtGetLocalAvatar()
                        else:
                            RecoitObj = PtGetAvatarKeyFromClientID(IDAvatar).getSceneObject()
                        NvPos = RecoitObj.getLocalToWorld()
                        NvPos.translate (Vect)
                    else:
                        NvPos = ptMatrix44()
                        NvPos.translate(Vect)
                    PlaceObjet (NomObj,Age, NvPos, rot)
    except:
        PtSendKIMessage(26,"Erreur PlaceDicObj:")











PtSendKIMessage(26,"Reload CdPerso OK")























