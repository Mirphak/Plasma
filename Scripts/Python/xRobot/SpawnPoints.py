# Dictionnaire(s) ou Liste(s) de SpawnPoints
smDict = {
"Personal":("StartPoint01", "PolesStartPoint02", "cPerf-SpawnPointRelto01", "cPerf-SpawnPointRelto02", "cPerf-SpawnPointRelto03", "StartPoint-Closet"),
"city":(
"StartPoint01_0", 
"StartPoint01_4", 
"StartPoint01_0", 
"cPerf-SpawnPointIslm01", 
"cPerf-SpawnPointIslm05", 
"StartPoint01_6", 
"StartPoint01_7", 
"StartPoint01_0", 
"StartPoint01_3", 
"cPerf-SpawnPointIslm04", 
"StartPoint01_4", 
"StartPoint01_5", 
"StartPoint_0", 
"StartPoint_1", 
"StartPoint01", 
"StartPointActors", 
"cStartPoint_5", 
"StartPoint01", 
"cPerf-SpawnPointIslm03", 
"cStartPoint_6", 
"LibPlayerStart", 
"StartPoint01", 
"StartPoint_5", 
"StartPoint_4", 
"StartPoint_0", 
"StartPoint_6", 
"StartPoint_7", 
"StartPoint_8", 
"cPerf-SpawnPointIslm02", 
"StartPoint_9", 
"StartPoint_10", 
"StartPoint01")
}
# ! il y 4 "LinkInPointDefault" dans city (differents prp)
spDict = {
    "Ahnonay":[
        # ahnySphereCtrl:"
        "LinkInPointDefault"
        # Sphere 1 (sp 1 a 5)
        # ahnySphere01:"
        , "LinkInPointSphere01", "SaveClothPoint31"
        #, "SaveClothPoint_old"
        # MaintRoom01:
        ,"SaveClothPoint41", "SaveClothPoint51", "SaveClothPoint61"
        #,"StartPoint"
        # Sphere 2 (sp 6 a 12)
        # ahnySphere02:"
        , "LinkInPointSphere02", "SaveClothPoint12", "SaveClothPoint22", "SaveClothPoint32"
        # MaintRoom02:
        ,"SaveClothPoint42", "SaveClothPoint52", "SaveClothPoint62"
        #,"StartPoint"
        # Sphere 3 (sp 13 a 19)
        # ahnySphere03:"
        , "LinkInPointSphere03", "SaveClothPoint13", "SaveClothPoint23", "SaveClothPoint33"
        # MaintRoom03:
        ,"SaveClothPoint43", "SaveClothPoint53", "SaveClothPoint63"
        #,"StartPoint"
        # Sphere 4 (sp 20 a 23)
        # MaintRoom04:
        ,"SaveClothPoint44", "SaveClothPoint54", "SaveClothPoint64"
        #,"StartPoint"
        # EngeneerHut:
        ,"SaveClothPoint74"
        # Hub:
        ,"Dummy01"
    ], 
    "Cleft":["LinkInPointDefault"
        # Desert
        , "LinkInPointFissureDrop", "Perf-SpawnPointDesert01", "Perf-SpawnPointDesert02", "zDesertLinkInCloser"
        # Cleft
        , "SpawnPointTomahna01", "Perf-SpawnPointChasm01", "Perf-SpawnPointChasm02"
    ],
    "city":["LinkInPointDefault"
        , "LinkInPointBahro-FerryGate", "LinkInPointBahro-FerryRoof", "LinkInPointBahro-OperaHouse", "LinkInPointBahro-TokotahRoof", "LinkInPointBahro-GreatStairRoof"
        , "LinkInPointBahro-LibraryRoof", "LinkInPointBahro-PalaceBalcony"
        , "LinkInPointFerry", "LinkInPointConcertHallFoyer", "LinkInPointDakotahAlley"
        , "LinkInPointGreatTree", "LinkInPointIslmLibrary", "LinkInPointLibrary", "LinkInPointPalace", "LinkInPointKadishGallery"
        , "Perf-SpawnPointIslm01", "Perf-SpawnPointIslm02", "Perf-SpawnPointIslm03", "Perf-SpawnPointIslm04", "Perf-SpawnPointIslm05"
        , "MuseumIntStart"
    ],
    "BaronCityOffice":["LinkInPointDefault", "Perf-SpawnPointBCO"],
    "Dereno":["LinkInPointDefault", "Dummy01"],
    "Descent":["LinkInPointShaftFall"],
    "Ercana":["LinkInPointDefault"
        , "HrvstrSpawnPt", "SaveCloth1POS", "SaveCloth2POS", "SaveCloth3POS"
        , "SaveCloth4POS", "StartPoint"
        , "SaveCloth5POS", "SiloAStartDummy"
        , "SaveCloth6POS" #, "Dummy01" #=> point non solide!
        , "SpawnBakery", "ercaContrlRmStart", "Tnnl001StartDummy"
        , "SaveCloth7POS", "LinkInPointPelletRoom"
    ],
    "Garrison":["LinkInPointDefault"
        # ** Gahreesen I **
        #- grsnWellInner (1) : 
        , "LinkInPointDefault"
        #- grsnWellFirstFloorRooms (2-4) : 
        , "Dummy01", "grsnJourneyCloth01POS", "grsnJourneyCloth02POS"
        #- grsnWellSecondFloorGearRoom (5-6) : 
        , "LinkInPointGearRm", "grsnJourneyCloth06POS"
        # ** Gahreesen III **
        #- grsnExterior (main world)(7 + 8-13 + 14) : 
        , "grsnJourneyCloth07POS"
        , "LinkInPointPinnacle", "LinkInPointPinnacle01", "LinkInPointPinnacle02", "LinkInPointPinnacle03", "LinkInPointPinnacle04", "LinkInPointPinnacle05"
        , "CaveEntry"
        #- grsnTrainingCenterMudRooms (15) : 
        , "StartPointEntry01"
        # ** Gahreesen II **
        #- grsnTeamRoom01 (16) : 
        , "StartinBoxYellow"
        #- grsnTeamRoom02 (17) : 
        , "StartinBoxPurple"
        #- grsnWallRoomClimbingPhys (18) : 
        #, "LinkInPointWall"
        # ** Gahreesen Prison **
        #- grsnTrainingCtrlLinkRm (18) : 
        , "grsnJourneyCloth05POS"
        #- grsnPrison (19-20) : 
        , "LinkInPointPrison"
        , "LinkInPointLwrVerandaRm"
        #- grsnVeranda (21-22) : 
        , "grsnJourneyCloth04POS", "PlayerStart"
        # ** Gahreesen Wall **
        #- WallRoom (24) : 
        #, "StartPoint"
        #- trainingCenterObservationRooms (23-25) : 
        , "grsnJourneyCloth03POS", "pstObservationRoom", "pstObservationRoom01"
        #- TrnCtrControlRoom01 (26) : 
        , "LinkInPointCtrlRm01"
        #- TrnCtrControlRoom02 (27-28) : 
        , "LinkInPointCtrlRm02", "tempStartPointDummy"
        # ** Gahreesen Nexus **
        #- grsnNexusBlackRoom (29) (l'ascenseur un un sous-monde, faire //Walk 1) : 
        , "Black_LinkInPointDefaultBlack"
        #- grsnNexusWhiteRoom (30) (l'ascenseur est un sous-monde, faire //Walk 1) : 
        , "LinkInPointDefaultWhite"
        # ** Gahreesen III **
        #- grsnExterior (subworld)(31-34) : 
        , "enterWellSubworldRegion", "exitWellSubRgn01", "exitWellSubRgn02", "SubworldEnterRegionTemp"
    ],
    "GreatZero":["LinkInPointDefault"
        , "BigRoomLinkInPoint", "GZIntStart"
    ],
    "Kadish":["LinkInPointDefault", 
        #- kdshCourtyard : 
        "kdshJourneyCloth06POS", "LinkInPointFromGallery", 
        #- kdshForest : 
        "Perf-SpawnPointKdsh03", "kdshJourneyCloth01POS", "kdshJourneyCloth02POS", "LinkInPointDefault", 
        #- kdshShadowPath : 
        "StartPoint", 
        #- kdshGlowInTheDark : 
        "LinkInPointDummy", 
        #- kdshPillars : 
        "kdshJourneyCloth04POS", "kdshJourneyCloth07POS", "Perf-SpawnPointKdsh04", "pillarRoomStartingPoint", 
        #- kdshVaultExtr : 
        "Perf-SpawnPointKdsh01", "KadishVaultPST02", 
        #- kdshVaultIntr : 
        "kdshJourneyCloth05POS", "Perf-SpawnPointKdsh05", "StartDummy02", 
        #- kdshVaultIntrYeesha : 
        "StartDummy02", "LinkInPointYeeshaVault"
    ],
    "Neighborhood":["LinkInPointDefault"
        , "Perf-SpawnPointClassroom", "Perf-SpawnPointCommonroom"
        , "LinkInPointBevinBalcony02", "Perf-SpawnPointBevin01"
        , "Perf-SpawnPointBevin02"
        , "LinkInPointBevinBalcony" #, "StartPoint01-4" non trouve
        , "Perf-SpawnPointPrivateRooms"
    ],
    "Minkata":["LinkInPointDefault"
        , "LinkInPointCave01", "LinkInPointCave04", "LinkInPointCave05", "LinkInPointCave02", "LinkInPointCave03"
    ],
    "PelletBahroCave":["LinkInPointDefault"
        , "LinkInWithPellet", "LinkInPointLower"
    ],
    "Personal":["LinkInPointDefault", "LinkInPointBahroPoles"
        , "Perf-SpawnPointRelto01", "Perf-SpawnPointRelto02"
        , "Perf-SpawnPointRelto03", "LinkInPointCloset"
    ],
    "Teledahn":["LinkInPointDefault"
        # tldnHarvest : 
        , "tldnJourneyCloth03POS", "Perf-SpawnPointExterior01", "Perf-SpawnPointExterior02", "DockStartPoint", "StumpStartPoint"
        # tldnLowerShroom : 
        , "tldnJourneyCloth06POS", "Perf-SpawnPointInShroom", "LinkInPointDefault", "LinkInPointUnderCabin"
        # tldnNoxiousCave : 
        , "tldnJourneyCloth02POS", "NoxiousStart"
        # tldnSlaveCave : 
        , "tldnJourneyCloth01POS", "Perf-SpawnPointSlaveCave"
        # tldnSlaveShroom : 
        , "tldnJourneyCloth04POS", "LinkInWarshroomUpstairs"
        # tldnUpperShroom : 
        , "tldnJourneyCloth05POS", "LinkInPointUpperRoom"
        # tldnWorkroom : 
        , "tldnJourneyCloth07POS", "Perf-SpawnPointWorkroom"
    ],
}

"""
To go to specific places of the city :
Opera house : oh    *
Tokotah roof : tr   *
Ferry gate : fg     *
Dakotah roof : dr   ?? DakotahRoofPlayerStart ?? (si oui = Tokotah Roof Top)
Kahlo roof : kr     ** = "gsr":"LinkInPointBahro-GreatStairRoof"
Library roof : lr   *
Kadish gallery : kg *
Museum : mu         xx = jrnlNegilahn = sur le livre du DRC sur la table a droite en haut des escaliers
Ferry roof : fr     *
Concert hall : ch   ** = LinkInPointConcertHallFoyer
Palace roof : pr    ** = LinkInPointBahro-PalaceBalcony
"""

aliasCitySP = {
    "fg":"LinkInPointBahro-FerryGate",          # = sp  1 # Ferry gate : fg     *
    "fr":"LinkInPointBahro-FerryRoof",          # = sp  2 # Ferry roof : fr     *
    "oh":"LinkInPointBahro-OperaHouse",         # = sp  3 # Opera house : oh    *
    "tr":"LinkInPointBahro-TokotahRoof",        # = sp  4 # Tokotah roof : tr   *
    "gsr":"LinkInPointBahro-GreatStairRoof",    # = sp  5 # Kahlo roof : kr     **
    "kr":"LinkInPointBahro-GreatStairRoof",     # = sp  5 # Kahlo roof : kr     **
    "lr":"LinkInPointBahro-LibraryRoof",        # = sp  6 # Library roof : lr   *
    "pb":"LinkInPointBahro-PalaceBalcony",      # = sp  7 # Palace roof : pr    **
    "pr":"LinkInPointBahro-PalaceBalcony",      # = sp  7 # Palace roof : pr    **
    "ferry":"LinkInPointFerry",                 # = sp  8 # 
    "concert":"LinkInPointConcertHallFoyer",    # = sp  9 # Concert hall : ch   **
    "ch":"LinkInPointConcertHallFoyer",         # = sp  9 # Concert hall : ch   **
    "alley":"LinkInPointDakotahAlley",          # = sp 10 # 
    "greattree":"LinkInPointGreatTree",         # = sp 11 # 
    "islmlib":"LinkInPointIslmLibrary",         # = sp 12 # 
    "library":"LinkInPointLibrary",             # = sp 13 # 
    "palace":"LinkInPointPalace",               # = sp 14 # 
    "gallery":"LinkInPointKadishGallery",       # = sp 15 # Kadish gallery : kg *
    "islm1":"Perf-SpawnPointIslm01",            # = sp 16 # 
    "islm2":"Perf-SpawnPointIslm02",            # = sp 17 # 
    "islm3":"Perf-SpawnPointIslm03",            # = sp 18 # 
    "islm4":"Perf-SpawnPointIslm04",            # = sp 19 # 
    "islm5":"Perf-SpawnPointIslm05",            # = sp 20 # 
    "museum":"MuseumIntStart",                  # = sp 21 # 
    "mu":"jrnlNegilahn",                        # = sp 22 # Museum : mu         xx
    "dakotah":"DakotahRoofPlayerStart",
    "trt":"DakotahRoofPlayerStart",
    "pb1":"PalaceBalcony01PlayerStart",
    "pb2":"PalaceBalcony02PlayerStart",
    "pb3":"PalaceBalcony03PlayerStart",
}

"""
    "Ercana":["LinkInPointDefault"
        , "HrvstrSpawnPt", "SaveCloth1POS", "SaveCloth2POS", "SaveCloth3POS"
        , "SaveCloth4POS", "StartPoint"
        , "SaveCloth5POS", "SiloAStartDummy"
        , "SaveCloth6POS"
        , "SpawnBakery", "ercaContrlRmStart", "Tnnl001StartDummy"
        , "SaveCloth7POS", "LinkInPointPelletRoom" #, "Dummy01"
    ],
"""
aliasErcanaSP = {
    "e0":"LinkInPointDefault",   # = sp  0 
    "e1":"HrvstrSpawnPt",        # = sp  1 
    "e2":"SaveCloth1POS",        # = sp  2 
    "e3":"SaveCloth2POS",        # = sp  3 
    "e4":"SaveCloth3POS",        # = sp  4 
    "e5":"SaveCloth4POS",        # = sp  5 
    "e6":"StartPoint",           # = sp  6 
    "e7":"SaveCloth5POS",        # = sp  7 
    "e8":"SiloAStartDummy",      # = sp  8 
    "e9":"SaveCloth6POS",        # = sp  9 
    "e10":"SpawnBakery",          # = sp 10 
    "e11":"ercaContrlRmStart",    # = sp 11 
    "e12":"Tnnl001StartDummy",    # = sp 12 
    "e13":"SaveCloth7POS",        # = sp 13 
    "e14":"LinkInPointPelletRoom",# = sp 14 
    #"e15":"Dummy01",              # = sp 15 #=> point non solide!
}

aliasKadishSP = {
    "k0":"LinkInPointDefault",       # = sp 0  
		#- kdshCourtyard : 
    "k1":"kdshJourneyCloth06POS",    # = sp 1
    "k2":"LinkInPointFromGallery",   # = sp 2 
		#- kdshForest :                     
    "k3":"Perf-SpawnPointKdsh03",    # = sp 3
    "k4":"kdshJourneyCloth01POS",    # = sp 4
    "k5":"kdshJourneyCloth02POS",    # = sp 5
    "k6":"LinkInPointDefault",       # = sp 6  
		#- kdshShadowPath :                 
    "k7":"StartPoint",               # = sp 7 
		#- kdshGlowInTheDark :              
    "k8":"LinkInPointDummy",         # = sp 8 
		#- kdshPillars :                    
    "k9":"kdshJourneyCloth04POS",    # = sp 9
    "k10":"kdshJourneyCloth07POS",   # = sp 10
    "k11":"Perf-SpawnPointKdsh04",   # = sp 11
    "k12":"pillarRoomStartingPoint", # = sp 12 
		#- kdshVaultExtr :                  
    "k13":"Perf-SpawnPointKdsh01",   # = sp 13
    "k14":"KadishVaultPST02",        # = sp 14 
		#- kdshVaultIntr :                  
    "k15":"kdshJourneyCloth05POS",   # = sp 15
    "k16":"Perf-SpawnPointKdsh05",   # = sp 16
    "k17":"StartDummy02",            # = sp 17 
		#- kdshVaultIntrYeesha :            
    "k18":"StartDummy02",            # = sp 18
    "k19":"LinkInPointYeeshaVault"   # = sp 19
}
"""
    "Minkata":["LinkInPointDefault"
        , "LinkInPointCave01", "LinkInPointCave04", "LinkInPointCave05", "LinkInPointCave02", "LinkInPointCave03"
"""
aliasMinkataSP = {
    "m0":"LinkInPointDefault",         # = sp  0 # Default/Center : m0     *
    "m1":"LinkInPointCave01",          # = sp  1 # Cave 1 : m1     *
    "m2":"LinkInPointCave04",          # = sp  2 # Cave 2 : m2     *
    "m3":"LinkInPointCave05",          # = sp  3 # Cave 3 : m3     *
    "m4":"LinkInPointCave02",          # = sp  4 # Cave 4 : m4     *
    "m5":"LinkInPointCave03",          # = sp  5 # Cave 5 : m5     *
    "cave1":"LinkInPointCave01",          # = sp  1 # Cave 1 : m1     *
    "cave2":"LinkInPointCave04",          # = sp  2 # Cave 2 : m2     *
    "cave3":"LinkInPointCave05",          # = sp  3 # Cave 3 : m3     *
    "cave4":"LinkInPointCave02",          # = sp  4 # Cave 4 : m4     *
    "cave5":"LinkInPointCave03",          # = sp  5 # Cave 5 : m5     *
    "k0":"LinkInPointDefault",         # = sp  0 # Default/Center : m0     *
    "k1":"LinkInPointCave01",          # = sp  1 # Cave 1 : m1     *
    "k2":"LinkInPointCave04",          # = sp  2 # Cave 2 : m2     *
    "k3":"LinkInPointCave05",          # = sp  3 # Cave 3 : m3     *
    "k4":"LinkInPointCave02",          # = sp  4 # Cave 4 : m4     *
    "k5":"LinkInPointCave03",          # = sp  5 # Cave 5 : m5     *
    "kiva0":"LinkInPointDefault",         # = sp  0 # Default/Center : m0     *
    "kiva1":"LinkInPointCave01",          # = sp  1 # Cave 1 : m1     *
    "kiva2":"LinkInPointCave04",          # = sp  2 # Cave 2 : m2     *
    "kiva3":"LinkInPointCave05",          # = sp  3 # Cave 3 : m3     *
    "kiva4":"LinkInPointCave02",          # = sp  4 # Cave 4 : m4     *
    "kiva5":"LinkInPointCave03",          # = sp  5 # Cave 5 : m5     *
}
aliasTeledahnSP = {
    "t0":"LinkInPointDefault",        # = sp 0
        # tldnHarvest :                       
    "t1":"tldnJourneyCloth03POS",     # = sp 1
    "t2":"Perf-SpawnPointExterior01", # = sp 2
    "t3":"Perf-SpawnPointExterior02", # = sp 3
    "t4":"DockStartPoint",            # = sp 4
    "t5":"StumpStartPoint",           # = sp 5
        # tldnLowerShroom :                   
    "t6":"tldnJourneyCloth06POS",     # = sp 6
    "t7":"Perf-SpawnPointInShroom",   # = sp 7
    "t8":"LinkInPointDefault",        # = sp 8
    "t9":"LinkInPointUnderCabin",     # = sp 9
        # tldnNoxiousCave :                    
    "t10":"tldnJourneyCloth02POS",    # = sp 10
    "t11":"NoxiousStart",             # = sp 11
        # tldnSlaveCave :                      
    "t12":"tldnJourneyCloth01POS",    # = sp 12
    "t13":"Perf-SpawnPointSlaveCave", # = sp 13
        # tldnSlaveShroom :                    
    "t14":"tldnJourneyCloth04POS",    # = sp 14
    "t15":"LinkInWarshroomUpstairs",  # = sp 15
        # tldnUpperShroom :                    
    "t16":"tldnJourneyCloth05POS",    # = sp 16
    "t17":"LinkInPointUpperRoom",     # = sp 17
        # tldnWorkroom :                       
    "t18":"tldnJourneyCloth07POS",    # = sp 18
    "t19":"Perf-SpawnPointWorkroom",  # = sp 19
}
aliasGarrisonSP = {
    "g0":"LinkInPointDefault",              # = sp 0
        # ** Gahreesen I **
        #- grsnWellInner (1) : 
    "g1":"LinkInPointDefault",              # = sp 1
        #- grsnWellFirstFloorRooms (2-4) : 
    "g2":"Dummy01",                         # = sp 2
    "g3":"grsnJourneyCloth01POS",           # = sp 3
    "g4":"grsnJourneyCloth02POS",           # = sp 4
        #- grsnWellSecondFloorGearRoom (5-6) : 
    "g5":"LinkInPointGearRm",               # = sp 5
    "g6":"grsnJourneyCloth06POS",           # = sp 6
        # ** Gahreesen III **
        #- grsnExterior (main world)(7 + 8-13 + 14) : 
    "g7":"grsnJourneyCloth07POS",           # = sp 7
    "g8":"LinkInPointPinnacle",             # = sp 8
    "g9":"LinkInPointPinnacle01",           # = sp 9
    "g10":"LinkInPointPinnacle02",          # = sp 10
    "g11":"LinkInPointPinnacle03",          # = sp 11
    "g12":"LinkInPointPinnacle04",          # = sp 12
    "g13":"LinkInPointPinnacle05",          # = sp 13
    "g14":"CaveEntry",                      # = sp 14
        #- grsnTrainingCenterMudRooms (15) : 
    "g15":"StartPointEntry01",              # = sp 15
        # ** Gahreesen II **
        #- grsnTeamRoom01 (16) : 
    "g16":"StartinBoxYellow",               # = sp 16
        #- grsnTeamRoom02 (17) : 
    "g17":"StartinBoxPurple",               # = sp 17
        #- grsnWallRoomClimbingPhys (18) : 
    #"g18":"LinkInPointWall",                # = sp 18
        # ** Gahreesen Prison **
        #- grsnTrainingCtrlLinkRm (18) : 
    "g18":"grsnJourneyCloth05POS",          # = sp 18
        #- grsnPrison (19-20) : 
    "g19":"LinkInPointPrison",              # = sp 19
    "g20":"LinkInPointLwrVerandaRm",        # = sp 20
        #- grsnVeranda (21-22) : 
    "g21":"grsnJourneyCloth04POS",          # = sp 21
    "g22":"PlayerStart",                    # = sp 22
        # ** Gahreesen Wall **
        #- WallRoom (24) : 
    #"g24":"StartPoint",                     # = sp 24
        #- trainingCenterObservationRooms (25-27) : 
    "g23":"grsnJourneyCloth03POS",          # = sp 23
    "g24":"pstObservationRoom",             # = sp 24
    "g25":"pstObservationRoom01",           # = sp 25
        #- TrnCtrControlRoom01 (26) : 
    "g26":"LinkInPointCtrlRm01",            # = sp 26
        #- TrnCtrControlRoom02 (27-28) : 
    "g27":"LinkInPointCtrlRm02",            # = sp 27
    "g28":"tempStartPointDummy",            # = sp 28
        # ** Gahreesen Nexus **
        #- grsnNexusBlackRoom (29) (l'ascenseur un un sous-monde, faire //Walk 1) : 
    "g29":"Black_LinkInPointDefaultBlack",  # = sp 29
        #- grsnNexusWhiteRoom (30) (l'ascenseur est un sous-monde, faire //Walk 1) : 
    "g30":"LinkInPointDefaultWhite",        # = sp 30
        # ** Gahreesen III **
        #- grsnExterior (subworld)(31-34) : 
    "g31":"enterWellSubworldRegion",        # = sp 31
    "g32":"exitWellSubRgn01",               # = sp 32
    "g33":"exitWellSubRgn02",               # = sp 33
    "g34":"SubworldEnterRegionTemp",        # = sp 34
}
