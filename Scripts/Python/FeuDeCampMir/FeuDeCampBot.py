# -*- coding: utf-8 -*-
""" Yodawave                                                                                                                                          FeuDeCampBot
placé  à   la Position  de NoID 
si NoID = 0    ( FeuDeCamp  est placé à Position)    ou    ( si age = cleft(   503 ,  -95.5  ,  -0.5   ))

"""
from Plasma import*
from FeuDeCampMir import   CdPerso , GestionClones

            #**********************************************************************************************************************     cleft 
def FeuDeCampCleft(NoID = 0 , Position = [ 0.0 , 0.0 , 0.0 ] ):
    PlaceFeuDeCampCleft.Place_FeuDeCampCleft( NoID , Position )
            
#import xPsnlVaultSDL
class InitFeuDeCampCleft():
    def __init__(self, Demandeur =  ""  ):
        self.Demandeur = Demandeur
        self.masterKeyClockPart08   = PtFindSceneobject("ClockPart08", "Ahnonay").getKey()
        self.ListcloneKeyClockPart08 = []
        self.ListSceneObjClockPart08 = []
        self.NbrObjClockPart08  = 1
        self.masterKeyClockPart05   = PtFindSceneobject("ClockPart05", "Ahnonay").getKey()
        self.ListcloneKeyClockPart05 = []
        self.ListSceneObjClockPart05 = []
        self.NbrObjClockPart05  = 1
        
        self.masterKeyFlamerRed01   = PtFindSceneobject("FlamerRed01", "BahroCave").getKey()#    flame                                ROUGE
        self.ListcloneKeyFlamerRed01 = []
        self.ListSceneObjFlamerRed01 = []
        self.NbrObjFlamerRed01  = 5
        self.masterKeySmokerUpRed   = PtFindSceneobject("SmokerUpRed", "BahroCave").getKey()#   poudre
        self.ListcloneKeySmokerUpRed = []
        self.ListSceneObjSmokerUpRed = []
        self.NbrObjSmokerUpRed  = 5
        self.masterKeyDusterRed   = PtFindSceneobject("DusterRed", "BahroCave").getKey()#   chute d'étincelle 
        self.ListcloneKeyDusterRed = []
        self.ListSceneObjDusterRed = []
        self.NbrObjDusterRed  = 5
        self.masterKeyRTomniRed01   = PtFindSceneobject("RTomniRed01", "BahroCave").getKey()#        eclaire  le sol et les avatar
        self.ListcloneKeyRTomniRed01 = []
        self.ListSceneObjRTomniRed01 = []
        self.NbrObjRTomniRed01  = 2
        self.masterKeyRTomniRed06   = PtFindSceneobject("RTomniRed06", "BahroCave").getKey()#        eclaire  le sol et les avatar
        self.ListcloneKeyRTomniRed06 = []
        self.ListSceneObjRTomniRed06 = []
        self.NbrObjRTomniRed06  = 2        
        
        self.masterKeyFlamer   = PtFindSceneobject("Flamer", "BahroCave").getKey()#    flame                                                        BLEU
        self.ListcloneKeyFlamer = []
        self.ListSceneObjFlamer = []
        self.NbrObjFlamer  = 5
        self.masterKeySmokerUp   = PtFindSceneobject("SmokerUp", "BahroCave").getKey()#   poudre
        self.ListcloneKeySmokerUp = []
        self.ListSceneObjSmokerUp = []
        self.NbrObjSmokerUp  = 5
        self.masterKeyDuster   = PtFindSceneobject("Duster", "BahroCave").getKey()#   chute d'étincelle 
        self.ListcloneKeyDuster = []
        self.ListSceneObjDuster = []
        self.NbrObjDuster  = 5
        self.masterKeyRTOmniLighFlame   = PtFindSceneobject("RTOmniLighFlame", "BahroCave").getKey()#        eclaire  le sol et les avatar
        self.ListcloneKeyRTOmniLighFlame = []
        self.ListSceneObjRTOmniLighFlame = []
        self.NbrObjRTOmniLighFlame  = 2
        self.masterKeyRTOmniLighFlame01   = PtFindSceneobject("RTOmniLighFlame01", "BahroCave").getKey()#        eclaire  le sol et les avatar
        self.ListcloneKeyRTOmniLighFlame01 = []
        self.ListSceneObjRTOmniLighFlame01 = []
        self.NbrObjRTOmniLighFlame01  = 2
        
        self.phys = 0
        self.Foyer = 1
        self.scale = ptMatrix44()
        self.NvCentreObj  = ptMatrix44()
        
    def Place_FeuDeCampCleft(self , NoID = 0 ,  Position = [ 0.0 , 0.0 , 0.0 ] ):
#        psnlSDL = xPsnlVaultSDL.xPsnlVaultSDL()
#        sdllist = psnlSDL.BatchGet( ["TeledahnPoleState", "GardenPoleState", "GarrisonPoleState", "KadishPoleState"] )
#        for var in ["Teledahn", "Garrison", "Garden", "Kadish"]:
#            PtSendKIMessage(26,   str (  sdllist[var + "PoleState"] ))
#            if sdllist[var + "PoleState"] <= 5 :
#                PtSendKIMessage(26,   var + "PoleState <= 5"   )
#                return
        self.NvCentreObj.reset()
        if NoID :
            self.NvCentreObj = PtGetAvatarKeyFromClientID( CdPerso.IDavatarOk(NoID) ).getSceneObject().getLocalToWorld()
            self.Foyer = 1
        else :
            if PtGetAgeName() == "Cleft" : 
                self.NvCentreObj.reset()
                self.NvCentreObj.translate (ptVector3(   503 ,  -95.5  ,  -0.5   )) 
                self.Foyer = 0
            else :
                self.Foyer = 1
                self.NvCentreObj.translate (ptVector3(   *Position  )) 
                
        PtSetAlarm(0.5,self , -1  )
        
        
    def onAlarm(self,param  ):#**********************************************************************************************************************      onAlarm      
        if param == -2 :
            self.ListcloneKeyClockPart08 =  GestionClones.GetClones(self.Demandeur,self.masterKeyClockPart08, self.NbrObjClockPart08 )
            self.ListcloneKeyClockPart05 =  GestionClones.GetClones(self.Demandeur,self.masterKeyClockPart05, self.NbrObjClockPart05 )
            
            self.ListcloneKeyFlamerRed01 =  GestionClones.GetClones(self.Demandeur,self.masterKeyFlamerRed01, self.NbrObjFlamerRed01 )# ROUGE
            self.ListcloneKeySmokerUpRed =  GestionClones.GetClones(self.Demandeur,self.masterKeySmokerUpRed, self.NbrObjSmokerUpRed )
            self.ListcloneKeyDusterRed =  GestionClones.GetClones(self.Demandeur,self.masterKeyDusterRed, self.NbrObjDusterRed )
            self.ListcloneKeyRTomniRed01 =  GestionClones.GetClones(self.Demandeur,self.masterKeyRTomniRed01, self.NbrObjRTomniRed01 )
            self.ListcloneKeyRTomniRed06 =  GestionClones.GetClones(self.Demandeur,self.masterKeyRTomniRed06, self.NbrObjRTomniRed06 )
            
            self.ListcloneKeyFlamer =  GestionClones.GetClones(self.Demandeur,self.masterKeyFlamer, self.NbrObjFlamer )# BLEU
            self.ListcloneKeySmokerUp =  GestionClones.GetClones(self.Demandeur,self.masterKeySmokerUp, self.NbrObjSmokerUp )
            self.ListcloneKeyDuster =  GestionClones.GetClones(self.Demandeur,self.masterKeyDuster, self.NbrObjDuster )
            self.ListcloneKeyRTOmniLighFlame =  GestionClones.GetClones(self.Demandeur,self.masterKeyRTOmniLighFlame, self.NbrObjRTOmniLighFlame )
            self.ListcloneKeyRTOmniLighFlame01 =  GestionClones.GetClones(self.Demandeur,self.masterKeyRTOmniLighFlame01, self.NbrObjRTOmniLighFlame01 )
            
            if   len ( self.ListcloneKeyClockPart08 ) == self.NbrObjClockPart08 and   len ( self.ListcloneKeyClockPart05 ) == self.NbrObjClockPart05   \
                    and len ( self.ListcloneKeyFlamerRed01 ) == self.NbrObjFlamerRed01   and   len ( self.ListcloneKeySmokerUpRed ) == self.NbrObjSmokerUpRed   and   len ( self.ListcloneKeyDusterRed ) == self.NbrObjDusterRed   \
                    and   len ( self.ListcloneKeyRTomniRed01 ) == self.NbrObjRTomniRed01  and   len ( self.ListcloneKeyRTomniRed06 ) == self.NbrObjRTomniRed06   \
                    and len ( self.ListcloneKeyFlamer ) == self.NbrObjFlamer   and   len ( self.ListcloneKeySmokerUp ) == self.NbrObjSmokerUp   and   len ( self.ListcloneKeyDuster ) == self.NbrObjDuster   \
                    and   len ( self.ListcloneKeyRTOmniLighFlame ) == self.NbrObjRTOmniLighFlame  and   len ( self.ListcloneKeyRTOmniLighFlame01 ) == self.NbrObjRTOmniLighFlame01  :
                PtSetAlarm( 0.5 ,  self,  0 )
            else :
                PtSetAlarm( 0.5 ,  self,  -2 )
        if param == -1 :
            self.ListcloneKeyClockPart08 =  GestionClones.GetClones(self.Demandeur,self.masterKeyClockPart08, self.NbrObjClockPart08 )
            self.ListcloneKeyClockPart05 =  GestionClones.GetClones(self.Demandeur,self.masterKeyClockPart05, self.NbrObjClockPart05 )
            
            self.ListcloneKeyFlamerRed01 =  GestionClones.GetClones(self.Demandeur,self.masterKeyFlamerRed01, self.NbrObjFlamerRed01 )# ROUGE
            self.ListcloneKeySmokerUpRed =  GestionClones.GetClones(self.Demandeur,self.masterKeySmokerUpRed, self.NbrObjSmokerUpRed )
            self.ListcloneKeyDusterRed =  GestionClones.GetClones(self.Demandeur,self.masterKeyDusterRed, self.NbrObjDusterRed )
            self.ListcloneKeyRTomniRed01 =  GestionClones.GetClones(self.Demandeur,self.masterKeyRTomniRed01, self.NbrObjRTomniRed01 )
            self.ListcloneKeyRTomniRed06 =  GestionClones.GetClones(self.Demandeur,self.masterKeyRTomniRed06, self.NbrObjRTomniRed06 )
            
            self.ListcloneKeyFlamer =  GestionClones.GetClones(self.Demandeur,self.masterKeyFlamer, self.NbrObjFlamer )# BLEU
            self.ListcloneKeySmokerUp =  GestionClones.GetClones(self.Demandeur,self.masterKeySmokerUp, self.NbrObjSmokerUp )
            self.ListcloneKeyDuster =  GestionClones.GetClones(self.Demandeur,self.masterKeyDuster, self.NbrObjDuster )
            self.ListcloneKeyRTOmniLighFlame =  GestionClones.GetClones(self.Demandeur,self.masterKeyRTOmniLighFlame, self.NbrObjRTOmniLighFlame )
            self.ListcloneKeyRTOmniLighFlame01 =  GestionClones.GetClones(self.Demandeur,self.masterKeyRTOmniLighFlame01, self.NbrObjRTOmniLighFlame01 )
            
            if   len ( self.ListcloneKeyClockPart08 ) != self.NbrObjClockPart08 or   len ( self.ListcloneKeyClockPart05 ) != self.NbrObjClockPart05   \
                    or len ( self.ListcloneKeyFlamerRed01 ) != self.NbrObjFlamerRed01   or   len ( self.ListcloneKeySmokerUpRed ) != self.NbrObjSmokerUpRed   or   len ( self.ListcloneKeyDusterRed ) != self.NbrObjDusterRed   \
                    or   len ( self.ListcloneKeyRTomniRed01 ) != self.NbrObjRTomniRed01  or   len ( self.ListcloneKeyRTomniRed06 ) != self.NbrObjRTomniRed06   \
                    or len ( self.ListcloneKeyFlamer ) != self.NbrObjFlamer   or   len ( self.ListcloneKeySmokerUp ) != self.NbrObjSmokerUp   or   len ( self.ListcloneKeyDuster ) != self.NbrObjDuster   \
                    or   len ( self.ListcloneKeyRTOmniLighFlame ) != self.NbrObjRTOmniLighFlame  or   len ( self.ListcloneKeyRTOmniLighFlame01 ) != self.NbrObjRTOmniLighFlame01  :
                try :
                    GestionClones.DemandeClone(self.Demandeur , self.masterKeyClockPart08 , self.NbrObjClockPart08 )
                    GestionClones.DemandeClone(self.Demandeur , self.masterKeyClockPart05 , self.NbrObjClockPart05 )
                    
                    GestionClones.DemandeClone(self.Demandeur,self.masterKeyFlamerRed01, self.NbrObjFlamerRed01 )# ROUGE
                    GestionClones.DemandeClone(self.Demandeur,self.masterKeySmokerUpRed, self.NbrObjSmokerUpRed )
                    GestionClones.DemandeClone(self.Demandeur,self.masterKeyDusterRed, self.NbrObjDusterRed )
                    GestionClones.DemandeClone(self.Demandeur,self.masterKeyRTomniRed01, self.NbrObjRTomniRed01 )
                    GestionClones.DemandeClone(self.Demandeur,self.masterKeyRTomniRed06, self.NbrObjRTomniRed06 )
                    
                    GestionClones.DemandeClone(self.Demandeur,self.masterKeyFlamer, self.NbrObjFlamer )# BLEU
                    GestionClones.DemandeClone(self.Demandeur,self.masterKeySmokerUp, self.NbrObjSmokerUp )
                    GestionClones.DemandeClone(self.Demandeur,self.masterKeyDuster, self.NbrObjDuster )
                    GestionClones.DemandeClone(self.Demandeur,self.masterKeyRTOmniLighFlame, self.NbrObjRTOmniLighFlame )
                    GestionClones.DemandeClone(self.Demandeur,self.masterKeyRTOmniLighFlame01, self.NbrObjRTOmniLighFlame01 )
                except :
                    PtSendKIMessage(26,"FeuDeCampBot     erreur chargement clone")
                PtSetAlarm( 0.5 ,  self,  -2  )
            else :
                PtSetAlarm( 0.5 ,  self,  0  )
            
        if param== 0 :
            self.ListSceneObjClockPart08 = []
            for cloneKey in self.ListcloneKeyClockPart08 :
                self.ListSceneObjClockPart08.append(cloneKey.getSceneObject())
            self.ListSceneObjClockPart05 = []
            for cloneKey in self.ListcloneKeyClockPart05 :
                self.ListSceneObjClockPart05.append(cloneKey.getSceneObject())
                
            self.ListSceneObjFlamerRed01 = []
            for cloneKey in self.ListcloneKeyFlamerRed01 :
                self.ListSceneObjFlamerRed01.append(cloneKey.getSceneObject())#         ROUGE
            self.ListSceneObjSmokerUpRed = []
            for cloneKey in self.ListcloneKeySmokerUpRed :
                self.ListSceneObjSmokerUpRed.append(cloneKey.getSceneObject())
            self.ListSceneObjDusterRed = []
            for cloneKey in self.ListcloneKeyDusterRed :
                self.ListSceneObjDusterRed.append(cloneKey.getSceneObject())
            self.ListSceneObjRTomniRed01 = []
            for cloneKey in self.ListcloneKeyRTomniRed01 :
                self.ListSceneObjRTomniRed01.append(cloneKey.getSceneObject())
            self.ListSceneObjRTomniRed06 = []
            for cloneKey in self.ListcloneKeyRTomniRed06 :
                self.ListSceneObjRTomniRed06.append(cloneKey.getSceneObject())
                
            self.ListSceneObjFlamer = []
            for cloneKey in self.ListcloneKeyFlamer :
                self.ListSceneObjFlamer.append(cloneKey.getSceneObject())#                   BLEU
            self.ListSceneObjSmokerUp = []
            for cloneKey in self.ListcloneKeySmokerUp :
                self.ListSceneObjSmokerUp.append(cloneKey.getSceneObject())
            self.ListSceneObjDuster = []
            for cloneKey in self.ListcloneKeyDuster :
                self.ListSceneObjDuster.append(cloneKey.getSceneObject())
            self.ListSceneObjRTOmniLighFlame = []
            for cloneKey in self.ListcloneKeyRTOmniLighFlame :
                self.ListSceneObjRTOmniLighFlame.append(cloneKey.getSceneObject())
            self.ListSceneObjRTOmniLighFlame01 = []
            for cloneKey in self.ListcloneKeyRTOmniLighFlame01 :
                self.ListSceneObjRTOmniLighFlame01.append(cloneKey.getSceneObject())

            if  self.Foyer  :
                rotObj = CdPerso.CalculVecRot(   180 , 0 , 0  )#                                                            place la couronne
                self.scale.makeScaleMat(ptVector3 ( 0.5 ,  0.5  ,  0.2  )    )
                CentreObj1 = self.NvCentreObj.copy()
                CentreObj1.translate (ptVector3(   0.0 , 0.0  ,1.0   ))
                CdPerso.PlaceSceneobjectNvCRS(  self.ListSceneObjClockPart08[0]   , CentreObj1 * self.scale*rotObj ,  self.phys  )
                
                rotObj = CdPerso.CalculVecRot(   0 , 0 , 0  )#                                                                   place le fond
                self.scale.makeScaleMat(ptVector3 ( 0.5 ,  0.5  ,  1  )    )
                CentreObj2 = self.NvCentreObj.copy()
                CentreObj2.translate (ptVector3(   0.3 , 0.0  ,  3.7  ))
                CdPerso.PlaceSceneobjectNvCRS(  self.ListSceneObjClockPart05[0]   , CentreObj2 * self.scale*rotObj ,  self.phys  )
            
            position = [ (0.0 , 0.0  , 0.0 ) ,  (1.0 , 0.0  , 0.0 ) ,  (0.0 , 1.0  , 0.0 ) ,  (1.0 , 1.0  , 0.0 ) ,  (-1.0 , -1.0  , 0.0 ) ,       ]
            compteur = 0#                                   place les Flame                                                                                                        # ROUGE
            self.scale.makeScaleMat(ptVector3 ( 4.5 ,  4.5  ,  1  )    )
            for Sceneobject  in self.ListSceneObjFlamerRed01 :
                CentreObj = self.NvCentreObj.copy()
                CentreObj.translate (ptVector3( *position[ compteur ] ) )
                CentreObj.translate (ptVector3(   0.0 , 0.0  ,1.0   ))
                CdPerso.PlaceSceneobjectNvCRS(  Sceneobject   , CentreObj * self.scale ,  self.phys  )
                compteur +=1
                
            compteur = 0#                                   place les poudres
            self.scale.makeScaleMat(ptVector3 ( 4.5 ,  4.5  ,  1  )    )
            for Sceneobject  in self.ListSceneObjSmokerUpRed :
                CentreObj = self.NvCentreObj.copy()
                CentreObj.translate (ptVector3( *position[ compteur ] ) )
                CentreObj.translate (ptVector3(   0.0 , 0.0  ,1.0   ))
                CdPerso.PlaceSceneobjectNvCRS(  Sceneobject   , CentreObj  ,  self.phys  )
                compteur +=1
                
            compteur = 0#                                   place les chutes d'étincelles
            rotObj = CdPerso.CalculVecRot(   180 , 0 , 0  )
            for Sceneobject  in self.ListSceneObjDusterRed :
                CentreObj = self.NvCentreObj.copy()
                CentreObj.translate (ptVector3( *position[ compteur ] ) )
                CentreObj.translate (ptVector3(   0.0 , 0.0  ,3.0   ))
                CdPerso.PlaceSceneobjectNvCRS(  Sceneobject   , CentreObj *rotObj ,  self.phys  )
                compteur +=1
                
            compteur = 0#                                    eclaire  le sol et les avatars
            position = [   (1.0 , 1.0  , 0.0 ) ,  (-1.0 , -1.0  , 0.0 ) ,       ]
            for Sceneobject  in self.ListSceneObjRTomniRed01 :
                CentreObj = self.NvCentreObj.copy()
                CentreObj.translate (ptVector3( *position[ compteur ] ) )
                CentreObj.translate (ptVector3(   0.0 , 0.0  ,2.0   ))
                CdPerso.PlaceSceneobjectNvCRS(  Sceneobject   , CentreObj  ,  self.phys  )
                compteur +=1
                
            compteur = 0#                                    eclaire  le sol et les avatars
            position = [ (0.0 , 0.0  , 0.0 ) ,  (1.0 , 0.0  , 0.0 ) ,         ]
            for Sceneobject  in self.ListSceneObjRTomniRed06 :
                CentreObj = self.NvCentreObj.copy()
                CentreObj.translate (ptVector3( *position[ compteur ] ) )
                CentreObj.translate (ptVector3(   0.0 , 0.0  ,2.0   ))
                CdPerso.PlaceSceneobjectNvCRS(  Sceneobject   , CentreObj  ,  self.phys  )
                compteur +=1
                
                
            position = [ (0.0 , 0.0  , 0.0 ) ,  (1.0 , 0.0  , 0.0 ) ,  (0.0 , 1.0  , 0.0 ) ,  (1.0 , 1.0  , 0.0 ) ,  (-1.0 , -1.0  , 0.0 ) ,       ]
            compteur = 0#                                   place les Flame                                                                                                       # BLEU
            self.scale.makeScaleMat(ptVector3 ( 4.5 ,  4.5  ,  1  )    )
            for Sceneobject  in self.ListSceneObjFlamer :
                CentreObj = self.NvCentreObj.copy()
                CentreObj.translate (ptVector3( *position[ compteur ] ) )
                CentreObj.translate (ptVector3(   0.0 , 0.0  ,1.0   ))
                CdPerso.PlaceSceneobjectNvCRS(  Sceneobject   , CentreObj * self.scale ,  self.phys  )
                compteur +=1
                
            compteur = 0#                                   place les poudres
            self.scale.makeScaleMat(ptVector3 ( 4.5 ,  4.5  ,  1  )    )
            for Sceneobject  in self.ListSceneObjSmokerUp :
                CentreObj = self.NvCentreObj.copy()
                CentreObj.translate (ptVector3( *position[ compteur ] ) )
                CentreObj.translate (ptVector3(   0.0 , 0.0  ,1.0   ))
                CdPerso.PlaceSceneobjectNvCRS(  Sceneobject   , CentreObj  ,  self.phys  )
                compteur +=1
                
            rotObj = CdPerso.CalculVecRot(   180 , 0 , 0  )
            for Sceneobject  in self.ListSceneObjDuster :
                CentreObj = self.NvCentreObj.copy()
                CentreObj.translate (ptVector3( *position[ compteur ] ) )
                CentreObj.translate (ptVector3(   0.0 , 0.0  ,3.0   ))
                CdPerso.PlaceSceneobjectNvCRS(  Sceneobject   , CentreObj *rotObj ,  self.phys  )
                compteur +=1
                
            compteur = 0#                                    eclaire  le sol et les avatars
            position = [   (1.0 , 1.0  , 0.0 ) ,  (-1.0 , -1.0  , 0.0 ) ,       ]
            for Sceneobject  in self.ListSceneObjRTOmniLighFlame :
                CentreObj = self.NvCentreObj.copy()
                CentreObj.translate (ptVector3( *position[ compteur ] ) )
                CentreObj.translate (ptVector3(   0.0 , 0.0  ,2.0   ))
                CdPerso.PlaceSceneobjectNvCRS(  Sceneobject   , CentreObj  ,  self.phys  )
                compteur +=1
                
            compteur = 0#                                    eclaire  le sol et les avatars
            position = [ (0.0 , 0.0  , 0.0 ) ,  (1.0 , 0.0  , 0.0 ) ,         ]
            for Sceneobject  in self.ListSceneObjRTOmniLighFlame01 :
                CentreObj = self.NvCentreObj.copy()
                CentreObj.translate (ptVector3( *position[ compteur ] ) )
                CentreObj.translate (ptVector3(   0.0 , 0.0  ,2.0   ))
                CdPerso.PlaceSceneobjectNvCRS(  Sceneobject   , CentreObj  ,  self.phys  )
                compteur +=1
            
            PtSendKIMessage(26,"  FeuDeCamp OK")
            
            
PlaceFeuDeCampCleft = InitFeuDeCampCleft("FeuDeCamp")



