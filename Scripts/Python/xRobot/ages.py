from Plasma import *

def ListMyAges():
    #ageDict = dict()
    ages = ptVault().getAgesIOwnFolder().getChildNodeRefList()
    for age in ages:
        ageInfo = age.getChild().upcastToAgeLinkNode().getAgeInfo()
        myKey = ageInfo.getAgeInstanceName()
        myKey = myKey.lower()
        myKey = myKey.replace(" ", "")
        myKey = myKey.replace("'", "")
        myKey = myKey.replace("eder", "")
        #ageDict.update({myKey:ageInfoList})
        print("{5} : {3} ({4}) {0}|{1}|{2}".format(ageInfo.getAgeInstanceName(), ageInfo.getAgeFilename(), ageInfo.getAgeInstanceGuid(), ageInfo.getAgeUserDefinedName(), ageInfo.getAgeSequenceNumber(), myKey))

def GetMyAges():
    ageDict = dict()
    ageInfoList = list()
    ages = ptVault().getAgesIOwnFolder().getChildNodeRefList()
    for age in ages:
        ageInfo = age.getChild().upcastToAgeLinkNode().getAgeInfo()
        ageInfoList = (ageInfo.getAgeInstanceName(), ageInfo.getAgeFilename(), ageInfo.getAgeInstanceGuid(), ageInfo.getAgeUserDefinedName(), "")
        #print ageInfoList
        #ageDict.update({ageInfo.getAgeInstanceName():ageInfoList})
        myKey = ageInfo.getAgeInstanceName()
        myKey = myKey.lower()
        myKey = myKey.replace(" ", "")
        myKey = myKey.replace("'", "")
        myKey = myKey.replace("eder", "")
        ageDict.update({myKey:ageInfoList})
        """
        tmp.update({k.lower().replace(" ", "").replace("'", "").replace("eder", ""): v})
        if myKey == "city":
            myKey = "mycity"
            myKey = "mydakotah"
            myKey = "myferry"
            myKey = "myconcert"
            myKey = "mylibrary"
            myKey = "mypalace"
            myKey = "mygallery"
            
            sp = "LinkInPointDakotahAlley"
            sp = "DakotahRoofPlayerStart"
            sp = "LinkInPointFerry"
            sp = "LinkInPointConcertHallFoyer"
            sp = "LinkInPointLibrary"
            sp = "LinkInPointPalace"
            sp = "LinkInPointKadishGallery"
        """
        #elif myKey == "":
            #myKey = "My" + ""
        #ageDict.update({myKey:ageInfoList})
    return ageDict

#
def PrintMyAgeList():
    ageDict = GetMyAges()
    for k, v in sorted(ageDict.items()):
        print("{0}:{1}, ".format(k, v))

#
MirphakAgeDict = {
    #"Ae'gura":["Ae'gura", "city", "7e0facea-dae1-4aec-a4ca-e76c05fdcfcf", "city"],
    #"Relto":["Relto", "Personal", "3d390df9-0ae1-41ea-8f79-0a8934473139", "Mirphak's"],
    #"AvatarCustomization":["AvatarCustomization", "AvatarCustomization", "2462cd01-99ba-4795-9ca9-143e8a39dda2", "Mirphak's"],
    #"Pellet Cave":["Pellet Cave", "PelletBahroCave", "8a4564d7-ce81-4dc0-9414-243007830c06", "Mirphak's"],
    #"Cleft":["Cleft", "Cleft", "1bdba0c1-7966-4bd4-8f5d-bda32a0774be", "Mirphak's"],
    #"Nexus":["Nexus", "Nexus", "aff2ffca-7024-4d12-9537-6c1abcd60a72", "Mirphak's"],
    #"Kadish":["Kadish", "Kadish", "75fe56b3-480e-42d9-9a5e-ae36d49916f4", "Mirphak's"],
    #"Gahreesen":["Gahreesen", "Garrison", "029637d0-e9a0-4252-b5df-c42691210696", "Mirphak's"],
    #"Teledahn":["Teledahn", "Teledahn", "ab3276a8-9c90-47fe-8f1f-a180d1ab5e35", "Mirphak's"],
    #"Eder Gira":["Eder Gira", "Gira", "102b406b-e838-4954-b160-5eeed1721c22", "Mirphak's"],
    #"Eder Kemo":["Eder Kemo", "Garden", "79fc3c50-8fc2-4b88-aceb-433f3c5f5e23", "Mirphak's"],
    #"Negilahn":["Negilahn", "Negilahn", "71fca7cb-2bf2-4aa2-b134-7f6e500cee50", "Mirphak's"],
    #"Payiferen":["Payiferen", "Payiferen", "73140dc1-a829-4127-aaee-95aa17f94bfd", "Mirphak's"],
    #"Tetsonot":["Tetsonot", "Tetsonot", "7a536e2e-7cf5-4881-8ad5-566ba40d8062", "Mirphak's"],
    #"Dereno":["Dereno", "Dereno", "a29d7261-0e0a-4cae-8113-5a2a6b0ea85a", "Mirphak's"],
    #"Ahnonay Cathedral":["Ahnonay Cathedral", "AhnonayCathedral", "042800ae-2430-443b-84eb-6b901d310e33", "Mirphak's"],
    #"Jalak":["Jalak", "Jalak", "610ccdaa-b044-4e97-8dae-4faa31f9f45e", "Mirphak's"],
    #"Minkata":["Minkata", "Minkata", "45ca3f68-e6a0-4f28-9b2e-34733d18e8c9", "Mirphak's"],
    #"Er'cana":["Er'cana", "Ercana", "8a74625b-1170-4961-b4c9-d3333491f678", "Mirphak's"],
    #"Myst":["Myst", "Myst", "8c69c3aa-83b1-4b82-8c5d-77a699de6bad", "Mirphak's"],
    #"Hood":["Hood", "Neighborhood", "f965a407-bf96-4a4c-a66a-a5ad25d4b5a2", "Mystpedia's"],
    #"BaronCityOffice":["BaronCityOffice", "BaronCityOffice", "8981d32c-ebb6-404b-813d-a43a19138318", "Mirphak's"],
}

tmp = dict()
for k, v in MirphakAgeDict.items():
        tmp.update({k.lower().replace(" ", "").replace("'", "").replace("eder", ""): v})
MirphakAgeDict = tmp

PrivateAgeDict = {
    "pedia":["Hood", "Neighborhood", "fb91f9e5-544f-4175-a0a5-7d83e0592dfa", "Mystpedia's", ""],
    "nexus":["Nexus", "Nexus", "5d1b8e80-3737-4494-ac33-446668bc06dd", "Mir-o-Bot's", ""], 
    "JanRelto":["Relto", "Personal", "844d30c1-3ebf-4323-83cd-684c345b1be9", "Janeerah's", ""],
    "fh":["Fun House", "Neighborhood", "33a235b1-9fe0-47f0-a73e-6fbd0044717a", "The", "LinkInPointBevinBalcony"],
    "hi":["Hood", "Neighborhood", "3cc44d4b-31e1-4dec-b6e6-4b63c72becc3", "The Hood of Illusions", ""],
    "Stone5's Teledahn":["Teledahn", "Teledahn", "f5f8774b-bf24-4c24-96a1-ebf8053b5574", "Stone5's", ""],
    "Stone5's Pellet Cave":["Pellet Cave", "PelletBahroCave", "e8903d76-2b49-e411-98fe-a7f1d92a82c8", "Stone5's", ""],
    "Stone5's GreatZero":["GreatZero", "GreatZero", "3630823d-9199-4462-9c29-e099fcd25795", "", ""],
    "Stone's city":["city", "city", "0221dd71-4b26-45c9-919e-d9bacd09f2e3", "", ""],
    "Minasunda's Jalak":["Jalak", "Jalak", "3bf1f16e-896a-4bb0-a2dd-fd3d1f472233", "Minasunda's", ""],
    "Stone5's Jalak":["Jalak", "Jalak", "7e7ee705-b804-413d-8e69-784bc627c68c", "Stone5's", ""],
    "Stone5's Ahnonay":["Ahnonay", "Ahnonay", "b5aa8c3d-0e08-4d78-9061-fc99018494ac", "", ""],
    "Ehren's GreatTreePub":["GreatTreePub", "GreatTreePub", "6876d56b-fddb-43d1-890a-dafbfc4bdb43", "Ehren's", ""],
    "MTH":["Hood", "Neighborhood", "e871c6d5-8e2d-4279-964c-71ebd8a954d5", "MystiTech's", ""],
    "MTA":["Ae'gura", "city", "48106ed9-c82a-43ae-8b3d-d5b8e741516d", "MystiTech's", "LinkInPointBahro-PalaceBalcony"],
    "MTGZ":["GreatZero", "GreatZero", "2557fccd-effa-4153-aff6-e26d3901ac52", "MystiTech's", "BigRoomLinkInPoint"],
    
    "YodaBot's Relto":["Relto", "Personal", "12ea442a-32d4-490f-85be-48b8e3feccba", "YodaBot's", ""],
    "YodaBot's Hood":["Hood", "Neighborhood", "d4eec6e9-efcd-49db-856e-20a527ed3496", "YodaBot's", ""],
    "YodaBot's EderDelin":["EderDelin", "EderDelin", "93520394-9704-4e36-bff2-e2302c43c2b4", "YodaBot's", ""],
    "MagicYoda's Eder Gira":["Eder Gira", "Gira", "029a5735-54eb-458f-8ecf-c7e8f7020794", "MagicYoda's", ""],
    "YBGTP":["GreatTreePub", "GreatTreePub", "5d1efb6d-b794-48f3-a2c6-c8951c152673", "", ""],
    "Tereeza's Hood":["Hood", "Neighborhood", "200be199-f5a0-40a7-b0c9-dad2eb5898e3", "Tereeza's", ""],
}

MirobotAgeDict = {
    "ahnonay":["Ahnonay", "Ahnonay", "55ce4207-aba9-4f2e-80de-7980a75ac3f2", "Mir-o-Bot's", ""],
    "aegura":["city", "city", "9511bed4-d2cb-40a6-9983-6025cdb68d8b", "Mir-o-Bot's", "LinkInPointBahro-PalaceBalcony"],
    #"avatarcustomization":('AvatarCustomization", "AvatarCustomization", "e6e64c5b-4dae-4b48-b662-ff3210720263", "Mir-o-Bot's", ""], 
    "cathedral":["Ahnonay Cathedral", "AhnonayCathedral", "bf4528a7-cb82-46ea-964d-1615a6babb0e", "Mir-o-Bot's", ""], 
    "cleft":["Cleft", "Cleft", "fef1ef9f-09dd-422c-a3d6-1229d615af85", "Mir-o-Bot's", "LinkInPointFissureDrop"], 
    "cleft1":["Cleft", "Cleft", "fef1ef9f-09dd-422c-a3d6-1229d615af85", "Mir-o-Bot's", "Perf-SpawnPointDesert01"], 
    "cleft2":["Cleft", "Cleft", "fef1ef9f-09dd-422c-a3d6-1229d615af85", "Mir-o-Bot's", "Perf-SpawnPointChasm02"], 
    "dereno":["Dereno", "Dereno", "330f59b9-9b21-4130-81e4-9852d3493fa9", "Mir-o-Bot's", ""], 
    "ercana":["Er'cana", "Ercana", "eb048e3d-c0ec-4a60-bc93-a64b67c58a66", "Mir-o-Bot's", ""], 
    "oven":["Er'cana", "Ercana", "eb048e3d-c0ec-4a60-bc93-a64b67c58a66", "Mir-o-Bot's", "LinkInPointPelletRoom"], 
    "gahreesen" :["Gahreesen", "Garrison", "42f261ba-b74e-45a3-afb8-0bda76f44b34", "Mir-o-Bot's", ""], 
    #"gahreesen1":["Gahreesen", "Garrison", "42f261ba-b74e-45a3-afb8-0bda76f44b34", "Mir-o-Bot's", "Dummy01"], 
    "gear"      :["Gahreesen", "Garrison", "42f261ba-b74e-45a3-afb8-0bda76f44b34", "Mir-o-Bot's", "LinkInPointGearRm"], 
    "pinnacle"  :["Gahreesen", "Garrison", "42f261ba-b74e-45a3-afb8-0bda76f44b34", "Mir-o-Bot's", "LinkInPointPinnacle"], 
    "training"  :["Gahreesen", "Garrison", "42f261ba-b74e-45a3-afb8-0bda76f44b34", "Mir-o-Bot's", "StartPointEntry01"], 
    "team"      :["Gahreesen", "Garrison", "42f261ba-b74e-45a3-afb8-0bda76f44b34", "Mir-o-Bot's", "StartinBoxYellow"], 
    "team2"     :["Gahreesen", "Garrison", "42f261ba-b74e-45a3-afb8-0bda76f44b34", "Mir-o-Bot's", "StartinBoxPurple"], 
    #"wall"      :["Gahreesen", "Garrison", "42f261ba-b74e-45a3-afb8-0bda76f44b34", "Mir-o-Bot's", "StartPoint"], 
    "prison"    :["Gahreesen", "Garrison", "42f261ba-b74e-45a3-afb8-0bda76f44b34", "Mir-o-Bot's", "LinkInPointPrison"], 
    "veranda"   :["Gahreesen", "Garrison", "42f261ba-b74e-45a3-afb8-0bda76f44b34", "Mir-o-Bot's", "PlayerStart"], 
    "gctrl"     :["Gahreesen", "Garrison", "42f261ba-b74e-45a3-afb8-0bda76f44b34", "Mir-o-Bot's", "LinkInPointCtrlRm01"], 
    "gctrl2"    :["Gahreesen", "Garrison", "42f261ba-b74e-45a3-afb8-0bda76f44b34", "Mir-o-Bot's", "LinkInPointCtrlRm02"], 
    "gnexus"    :["Gahreesen", "Garrison", "42f261ba-b74e-45a3-afb8-0bda76f44b34", "Mir-o-Bot's", "LinkInPointDefaultWhite"], 
    "gira":["Eder Gira", "Gira", "5b4678a9-73ab-4b45-9058-e710b45e4dbe", "Mir-o-Bot's", "LinkInPointFromKemo"], 
    "hood":["Hood", "Neighborhood", "e6958ab2-f925-4e36-a884-ee65e5c73896", "Mir-o-Bot's", "LinkInPointBevinBalcony"], 
    "jalak":["Jalak", "Jalak", "1269ee23-baff-4ca2-a3bc-f80df29fe978", "Mir-o-Bot's", ""], 
    "kadish":["Kadish", "Kadish", "31b44de5-0d1e-4c1b-8d8d-d9592df2f214", "Mir-o-Bot's", "LinkInPointFromGallery"], 
    "kemo":["Eder Kemo", "Garden", "3a366b1e-9488-4c77-a278-a6375161ac92", "Mir-o-Bot's", "Perf-SpawnPointKemo02"], 
    "mobKemo":["Eder Kemo", "Garden", "3edc8f3b-fa2c-486e-83f3-795435b2dc88", "mob's", ""],
    "mobgz":["GreatZero", "GreatZero", "66d12fcf-4635-4e7d-b991-38fa5d70108a", "mob's", "BigRoomLinkInPoint"],
    #"mobkveer":["Ae'gura", "Kveer", "dc721118-1ea2-44ad-9ff0-df58676ed73c", "", ""],
    "mobkveer":["K'veer", "Kveer", "dc721118-1ea2-44ad-9ff0-df58676ed73c", "Mir-o-Bot's", ""],
    "mobrelto":["Relto", "Personal", "d21c19f9-c664-4650-a027-512688fc75d4", "mob's", "LinkInPointCloset"],
    "minkata":["Minkata", "Minkata", "125c7c98-9c18-49df-acce-ddc3f8108bd6", "Mir-o-Bot's", ""], 
    "myst1":["Myst", "Myst", "63aad82f-5d85-416e-bd35-50b63b09b5e2", "Mir-o-Bot's", ""], 
    "myst":["Myst", "Myst", "67b9503e-3eaf-4d5a-a0dc-3ff7dccddcde", "Mir-o-Bot's", ""],
    "negilahn":["Negilahn", "Negilahn", "41d48e5b-d037-4054-8c63-42a1273c3830", "Mir-o-Bot's", ""], 
    "payiferen":["Payiferen", "Payiferen", "ae90edff-73ed-413c-a3b1-f2b4f1ae217d", "Mir-o-Bot's", ""], 
    "relto":["Relto", "Personal", "6e7a66cc-e0c1-4efc-977a-cd7a354a736a", "Mir-o-Bot's", "LinkInPointBahroPoles"], 
    "teledahn":["Teledahn", "Teledahn", "cf9f1261-7412-4470-9c31-3965738656d3", "Mir-o-Bot's", "Perf-SpawnPointExterior02"], 
    "teledahn2":["Teledahn", "Teledahn", "cf9f1261-7412-4470-9c31-3965738656d3", "Mir-o-Bot's", ""], 
    "tetsonot":["Tetsonot", "Tetsonot", "c0f86889-e38a-412f-9eb9-9ac2091b3fa7", "Mir-o-Bot's", ""], 

    "tsogal":["EderTsogal", "EderTsogal", "03c05256-c149-4fa5-9210-b848b9b9b5c0", "Mir-o-Bot's", ""],
    "delin":["EderDelin", "EderDelin", "6ed7f98c-a3f6-4000-bb79-91843f78441a", "Mir-o-Bot's", ""],
    "GZ":["GreatZero", "GreatZero", "76aa23d2-07a0-45f6-b355-5de39302f455", "Mir-o-Bot's GZ", ""],
    "GreatZero":["GreatZero", "GreatZero", "76aa23d2-07a0-45f6-b355-5de39302f455", "Mir-o-Bot's GZ", "BigRoomLinkInPoint"],
    "Descent":["Descent", "Descent", "4543f4e3-aa4b-4c4b-b6f4-eaa1aee4c440", "Mir-o-Bot's", "LinkInPointShaftFall"],
    "Tiwah":["Descent", "Descent", "4543f4e3-aa4b-4c4b-b6f4-eaa1aee4c440", "Mir-o-Bot's", "LinkInPointShaftFall"],
    "GreatShaft":["Descent", "Descent", "4543f4e3-aa4b-4c4b-b6f4-eaa1aee4c440", "Mir-o-Bot's", ""],
    
    "PrimeCave":["LiveBahroCaves", "LiveBahroCaves", "74b81313-c5f4-4eec-8e21-94d55e59ea8a", "Mir-o-Bot's Prime", ""],
    "PodsCave":["LiveBahroCaves", "LiveBahroCaves", "9b764f14-2d0e-493e-aa4a-e7ed218e3168", "Mir-o-Bot's Pods", ""],
    "EderCave":["LiveBahroCaves", "LiveBahroCaves", "1c9388c2-e4da-4e2e-a442-a0f58ad216b9", "Mir-o-Bot's Eder", ""],
    "Rudenna":["BahroCave", "BahroCave", "a8f6a5a6-4e5e-4d3f-9160-a9b75f0768c5", "Mir-o-Bot's Rudenna", ""],
    "pelletcave":["Pellet Cave", "PelletBahroCave", "13c1fdfc-44e2-4230-803a-147d8e6918a0", "Mir-o-Bot's (top)", ""], 
    #"pellet0":["Pellet Cave", "PelletBahroCave", "13c1fdfc-44e2-4230-803a-147d8e6918a0", "Mir-o-Bot's", "LinkInPointDefault"], 
    "pellet1":["Pellet Cave", "PelletBahroCave", "13c1fdfc-44e2-4230-803a-147d8e6918a0", "Mir-o-Bot's (top)", "LinkInWithPellet"], 
    "pellet2":["Pellet Cave", "PelletBahroCave", "13c1fdfc-44e2-4230-803a-147d8e6918a0", "Mir-o-Bot's (bottom)", "LinkInPointLower"], 
    #"LinkInPointDefault" "LinkInPointLower" "LinkInWithPellet"
    "Silo":["ErcanaCitySilo", "ErcanaCitySilo", "88177069-fd83-4a07-ba87-5800016e2f28", "Mir-o-Bot's", ""],
    "Office":["Ae'gura", "BaronCityOffice", "2aaf334b-a49e-40f2-963b-5be146d40021", "Mir-o-Bot's Office", ""],
    
    "spyroom":["spyroom", "spyroom", "df9d49ec-0b9c-4716-9a0f-a1b66f7d9814", "mob's (Sharper's spy room)", ""],

    #"Ahnonay": ["Ahnonay", "Ahnonay", "dd51c064-002c-4627-9cbc-2b3598cac3df", "Mir-o-Bot's", "StartPoint"], 
    ##"s1": ["Ahnonay", "Ahnonay", "dd51c064-002c-4627-9cbc-2b3598cac3df", "Mir-o-Bot's", "LinkInPointSphere01"], 
    ##"s2": ["Ahnonay", "Ahnonay", "dd51c064-002c-4627-9cbc-2b3598cac3df", "Mir-o-Bot's", "LinkInPointSphere02"], 
    ##"s3": ["Ahnonay", "Ahnonay", "dd51c064-002c-4627-9cbc-2b3598cac3df", "Mir-o-Bot's", "LinkInPointSphere02"], 
    ##"s4": ["Ahnonay", "Ahnonay", "dd51c064-002c-4627-9cbc-2b3598cac3df", "Mir-o-Bot's", "LinkInPointSphere04"],
    
    "pedia":["Hood", "Neighborhood", "fb91f9e5-544f-4175-a0a5-7d83e0592dfa", "Mystpedia's", ""],
    
    "fh":["Fun House", "Neighborhood", "33a235b1-9fe0-47f0-a73e-6fbd0044717a", "The", "LinkInPointBevinBalcony"],
    ##"hi":["Hood", "Neighborhood", "3cc44d4b-31e1-4dec-b6e6-4b63c72becc3", "The Hood of Illusions", ""],
    "hi":["Hood of Illusions", "Neighborhood", "3cc44d4b-31e1-4dec-b6e6-4b63c72becc3", "The", ""],
    #"Stone5PelletCave":["Pellet Cave", "PelletBahroCave", "e8903d76-2b49-e411-98fe-a7f1d92a82c8", "Stone5's", ""],
    "Stone5's GreatZero":["GreatZero", "GreatZero", "3630823d-9199-4462-9c29-e099fcd25795", "", ""],
    "Stone5's Teledahn":["Teledahn", "Teledahn", "f5f8774b-bf24-4c24-96a1-ebf8053b5574", "Stone5's", ""],
    "stone's city":["city", "city", "0221dd71-4b26-45c9-919e-d9bacd09f2e3", "", ""],
    #"lysanna's Relto":["Relto", "Personal", "acb71896-e4f7-4b23-9b06-d2d845394fd9", "lysanna's", ""],
    #"MagicAhnonay":["Ahnonay", "Ahnonay", "8b2af51f-b3bd-46e9-bee3-1236f29b5cd6", "", ""],
    "MinaJalak":["Jalak", "Jalak", "3bf1f16e-896a-4bb0-a2dd-fd3d1f472233", "Minasunda's", ""],
    "Stone5's Jalak":["Jalak", "Jalak", "7e7ee705-b804-413d-8e69-784bc627c68c", "Stone5's", ""],
    #"Stone5's Ahnonay":["Ahnonay", "Ahnonay", "b5aa8c3d-0e08-4d78-9061-fc99018494ac", "", ""],
    "Stone5's Gahreesen":["Gahreesen", "Garrison", "092190a7-10d1-4864-b43c-0ac95d8f3966", "Stone5's", ""],
    "MTH":["Hood", "Neighborhood", "e871c6d5-8e2d-4279-964c-71ebd8a954d5", "MystiTech's", ""],
    "MTA":["Ae'gura", "city", "48106ed9-c82a-43ae-8b3d-d5b8e741516d", "MystiTech's", "LinkInPointBahro-PalaceBalcony"],
    "MTGZ":["GreatZero", "GreatZero", "2557fccd-effa-4153-aff6-e26d3901ac52", "MystiTech's", "BigRoomLinkInPoint"],
    "NMM":["Minkata", "Minkata", "174a1bae-135e-4235-a194-630e8e06424d", "NikiMay's", ""],
    "NMMC":["LiveBahroCaves", "LiveBahroCaves", "d315c235-9650-4fc3-8581-38db7387277e", "LiveBahroCaves", ""],
    "AlexJoErcana":["Er'cana", "Ercana", "f3073c55-d14b-426d-adba-03793190fdb0", "AlexJo's", ""],
    "NME":["Er'cana", "Ercana", "a57340b0-b0d6-4d3e-a2dd-51249335fcd3", "NikiMay's", "LinkInPointPelletRoom"],
    "MTKErcana":["Ercana", "Ercana", "d9647a7d-aa48-4cbd-aa79-ef98cd9f04a7", "", ""],
    "GabeJoErcana":["Er'cana", "Ercana", "099ec522-50b0-4dd2-9cda-ec58d8ab8a60", "GabeJo's", ""],
    "NMErcana1":["Ercana", "Ercana", "af5ed9ac-2607-47be-8105-88382cbce0f5", "Ercana", ""],
    "MTSPY":["spyroom", "spyroom", "92210c72-555f-4ef3-a9a7-366109c712d5", "", ""],
    "MTTsogal":["EderTsogal", "EderTsogal", "36a4a1a3-addc-4683-b1e0-3f51f3807ec9", "EderTsogal", ""],
    "mtkirel":["Neighborhood02", "Neighborhood02", "18a95119-b466-472e-8d31-39488145f9b1", "Neighborhood02", ""],
    "kirel106":["Neighborhood02", "Neighborhood02", "7116bda8-9686-482a-82f4-ff16ace30da9", "Neighborhood02", ""],
    "NMCleft":["Cleft", "Cleft", "4d83d68f-9d84-4b7b-b7b7-7867de93a6a5", "NikiMay's", ""],
    "BLCleft":["Cleft", "Cleft", "56c2e0d3-28a2-4c06-bc60-4e95064f7425", "BeatriceLang's", ""],
    "YBGTP":["GreatTreePub", "GreatTreePub", "5d1efb6d-b794-48f3-a2c6-c8951c152673", "", ""],
    "LTDereno":["Dereno", "Dereno", "ac5301d3-cce0-435c-8804-daa05dec15ba", "LteynTahn's", ""],
    "nmEderGira":["Eder Gira", "Gira", "bc12aca7-5b2f-4be4-bf36-cb0f8beabeac", "NikiMay's", ""],
    "nmGahreesen":["Gahreesen", "Garrison", "cc496686-4873-491d-8036-1c14fbf0dc22", "NikiMay's", ""],
    "nmRelto":["Relto", "Personal", "9c3a4608-d312-41f6-95cd-a0148061cf2d", "NikiMay's", ""],
    "nmTeledahn":["Teledahn", "Teledahn", "7fb5e110-4149-4ddd-b92e-df1c8f08ff9d", "NikiMay's", ""],
    "nmKadish":["Kadish", "Kadish", "e728267d-06a4-42e9-a698-3419a6a4a6b4", "NikiMay's", ""],
    "nmKadish":["Kadish", "Kadish", "e728267d-06a4-42e9-a698-3419a6a4a6b4", "NikiMay's", ""],
    "nmDereno":["Dereno", "Dereno", "8e3798e9-6df6-46af-888a-4f3f38395c00", "NikiMay's", ""],
    "nmPayiferen":["Payiferen", "Payiferen", "4b4d01ac-12cb-4104-b498-267224f0f6e1", "NikiMay's", ""],
    "nmTetsonot":["Tetsonot", "Tetsonot", "91a23dd2-ce50-4922-b631-67594d4873ca", "NikiMay's", ""],
    "nmErcana":["Er'cana", "Ercana", "a57340b0-b0d6-4d3e-a2dd-51249335fcd3", "NikiMay's", ""],
    "nmCathedral":["Ahnonay Cathedral", "AhnonayCathedral", "7326a881-c90f-41ad-b9d0-bc4064467197", "NikiMay's", ""],
    "nmAhnonay":["Ahnonay", "Ahnonay", "d07b6219-04c9-4017-84a7-ac53ad5f80de", "", ""],
    "nmEderKemo":["Eder Kemo", "Garden", "34311293-566e-4f07-8bc9-d95c6b495c2d", "NikiMay's", ""],
    "nmJalak":["Jalak", "Jalak", "1f3f5a16-b2df-4ac1-bc7f-28c9ecd22ede", "NikiMay's", ""],
    "nmCleft":["Cleft", "Cleft", "4d83d68f-9d84-4b7b-b7b7-7867de93a6a5", "NikiMay's", ""],
    "nmOffice":["Ae'gura", "BaronCityOffice", "ee2b5b3d-3ed4-4dbf-a08d-7b7e6911ad47", "", ""],
    "nmSilo":["ErcanaCitySilo", "ErcanaCitySilo", "2d9a6f9f-91ad-4dfd-8e70-3d8f6f461588", "", ""],
    "nmpellet":["Pellet Cave", "PelletBahroCave", "f7b30e38-1b4f-4cd1-abaa-8700a0300fac", "NikiMay's", ""],
    "mtGira":["Eder Gira", "Gira", "94bb6851-294d-4377-bc82-27e188d7bda1", "MT Korovyev 1's", ""],
    "nmPelletB":["Pellet Cave", "PelletBahroCave", "f7b30e38-1b4f-4cd1-abaa-8700a0300fac", "NikiMay's (bottom)", "LinkInPointLower"],
    "gmkGira":["Eder Gira", "Gira", "f75eacb1-4250-496c-8ff5-2e8a5c0ae930", "GoMeKorov'ev's", ""],
    "mtKveer":["Kveer", "Kveer", "b7731c38-4016-4f77-a904-f1c318aa3c9e", "", ""],
    "GreatTreePub":["GreatTreePub", "GreatTreePub", "08980412-c527-496e-af41-123d40cc06a7", "GreatTreePub", ""],
    "minakveer":["Ae'gura", "Kveer", "3945d0f1-5832-4cc2-b81f-22d2048019b1", "", ""],
    #"mtgome":["GoMePubNew", "GoMePubNew ffe1f0bf-e24f-4e49-955f-d95f5c2292cf", "", "", ""],
    "mtgome":["GoMePubNew", "GoMePubNew", "28a73c56-949c-4327-ad56-7df8753933e6", "Kahnop's", ""],
    "mobgomepub":["GoMePubNew", "GoMePubNew", "da149d57-5671-4302-95d6-8d9ea52167ff", "Mir-o-Bot's", ""],
    "KorGoMe":["GoMePubNew", "GoMePubNew", "19a3b778-fac7-4f2a-8795-316dffd292df", "MT Korovyev 1's", ""],
    "mobchiso":["ChisoPreniv", "ChisoPreniv", "788b836d-2019-48bd-af66-c9f0674dff5a", "Mir-o-Bot's", ""],
    "mobveelay":["VeeTsah", "VeeTsah", "e8c6fbef-4e47-4951-8a9f-ab8c1b800c49", "Mir-o-Bot's", ""],
    #" Veelay Tsahvahn":["Veelay Tsahvahn", "VeeTsah", "914d2ad2-6a69-478e-9087-265e10d85c48", "mob's", ""],
    "mobSerene":["Serene", "Serene", "f5a44340-3506-4c8f-af97-8bb338193460", "Mir-o-Bot's", ""],
    "mobTrebivdil":["Tre'bivdil", "trebivdil", "ea180c91-e06d-44c4-b18c-c769a7c714cb", "Mir-o-Bot's", ""],
    "mobVothol":["Vothol Gallery", "vothol", "09d93976-b95d-4a31-b2e7-0e63903d77ff", "Mir-o-Bot's", ""],
    "korVothol":["Vothol", "Vothol", "f3693cc1-c795-4895-94e6-aa40b232e34a", "MT Korovyev 1's", ""],
    "MinaTeledahn":["Teledahn", "Teledahn", "40c29da9-c01d-445e-a99f-421176ecb6d8", "Minasunda's", ""],
    "KorChiso":["ChisoPreniv", "ChisoPreniv", "28e65caa-f0c5-46c7-ac95-3b2a1dc08b7a", "MT Korovyev 1's", ""],
    "mobGahreesen":["Gahreesen", "Garrison", "f3e10b6e-069c-4329-903e-3b0377f7e510", "mob's", ""],
    "Tiam":["Tiam", "Tiam", "0c3db58b-0c1a-47a9-8e33-8c061640b9cb", "Mir-o-Bot's", ""],
    "mobTiam":["Tiam", "Tiam", "5e018f72-0ae7-4db8-ba52-101117eb3d15", "mob's", ""],
    "MinaGoMePub":["GoMePubNew", "GoMePubNew", "d0591f42-9a2b-4247-9f1b-523709ba9b04", "GoMePubNew", ""],
    "MinaGoMePubNew":["GoMePubNew", "GoMePubNew", "bc429917-4db5-49bd-af2a-4c2e53284346", "", ""],
    "MinaErcana":["Er'cana", "Ercana", "5435d8b4-c3ad-4bf5-817d-26ce73490828", "Minasunda's", ""],
    #"DulcamaraElonin":["Elonin", "Elonin", "1be11cee-3bf7-4a14-a886-e06e9603b72c", "Dulcamara's", ""],
    #"Elonin":["Elonin", "Elonin", "", "Mir-o-Bot's", ""],
    "mobElonin":["Elonin", "Elonin", "b318f385-45ae-4377-9f1c-6e629233f994", "mob's", ""],
    "TLATestChamber":["TLATestChamber", "TLATestChamber", "a1bc1e55-1453-43be-9d5a-9be4d0f31dd5", "", ""],
}

#    "Daredevil Jan's Relto":["Relto", "Personal", "1fc289df-a11c-4754-b2c1-7043073eebdb", "Daredevil Jan's", ""],
#["D'ni Rezeero", "", "", "", "BigRoomLinkInPoint"] #GZIntStart
#["Kveer", "", "", "", "LinkInPointPrison"] #MystBookPOS #LinkOutPOSKveer
#["Myst", "", "", "", "FireplaceStartPoint"] #FireplaceClimbInPOS #FireplaceClimbOutPOS
#Kadish => LinkInPointYeeshaVault, LinkInPointFromGallery, LinkInPointGlowRmBalcony
# Gira => LinkInPointFromKemo
#Kemo => Perf-SpawnPointKemo02
#Er'cana => StartPoint, LinkInPointPelletRoom
#Watcher => RedHerringDoorSafePoint
#Ahnanay : LinkInPointShere01
#Cleft : LinkInPointFissureDrop
#Sharper's Office : Perf-SpawnPointBCO
#Kirel: kirelPerf-SpawnPointBevin01
#Nexus : c'est pas Perf-SpawnPointNexus
tmp = dict()
for k, v in MirobotAgeDict.items():
        tmp.update({k.lower().replace(" ", "").replace("'", "").replace("eder", ""): v})
MirobotAgeDict = tmp


#MagicBot ages:
MagicbotAgeDict = {
    #"MBErcana":["Er'cana", "Ercana", "eccb9705-60b5-4746-b77c-02a3cf73f6a8", "MagicBot's", "StartPoint"],
    "MBErcana":["Ercana", "Ercana", "7c6348d0-ea67-496f-922c-ed940b54f534", "", ""],
    #"MBCleft":["Magic Cleft", "Cleft", "53C424e2-5922-44e8-be1f-1215ec8d9820", "MagicBot's", "LinkInPointFissureDrop"],
    #"MBCity":["city", "City", "411e452b-7077-4328-ad5b-4dadc1467a9a", "", "LinkInPointBahro-PalaceBalcony"],
    "MBcity":["city", "city", "2cb76f8d-2b26-4732-8275-cdd4172424f0", "", "LinkInPointBahro-PalaceBalcony"],
    #"soccercity":["Ae'gura", "city", "e07e214f-5a7c-4165-8377-26ae4be8f42e", "", ""],
    #"MBRelto1":["Relto", "Personal", "798cc281-e224-4c60-aba4-5cc43027d069", "MagicBot's", "LinkInPointBahroPoles"],
    #"MagicRelto":["Relto", "Personal", "134672a5-2e67-43bc-90e9-aad4e0a7e2b5", "Magic Bot's", "LinkInPointBahroPoles"],
    #"MBRelto":["Relto", "Personal", "e661c216-cb66-4e59-80ab-7cf272dbecdc", "Mimi Bot's", ""],
    "MimiRelto":["Relto", "Personal", "a0f1f587-1819-4e48-9ea5-80c6ed299ba5", "Mimi Bot's", ""],
    "Mimi-Relto":["Relto", "Personal", "138b35b8-2c17-4107-95ed-d65294c9aced", "Mimi-Bot's", ""],
    ##'MBHood":["Magic Hood", "Neighborhood", "0e28e00d-6a4e-4131-8ed8-95bfcee2631b", "MagicBot's", "LinkInPointBevinBalcony"], #GUID faux!
    #"MBHood":["Hood", "Neighborhood", "0e28e00d-6a4e-4131-8ed8-95bfcec2631b", "MagicBot's", "LinkInPointBevinBalcony"],
    "MBHood":["Hood", "Neighborhood", "65ef6345-3aa7-4233-a5bb-e86280cc0dd3", "Magic Bot's", ""],
    #"MBDereno":["Dereno", "Dereno", "39a09bd2-49b0-4fe1-a7ae-c1cf2e3356bc", "MagicBot's", ""],
    "MBDereno":["Dereno", "Dereno", "462edc6f-d783-44ae-b254-1bd7b0205082", "MagicBot's", ""],
    #"MBTeledahn":["Teledahn", "Teledahn", "edb74f4d-e0c5-4867-b8a6-f7f823bbd449", "MagicBot's", "Perf-SpawnPointExterior01"],
    "MBTeledahn":["Teledahn", "Teledahn", "955890b9-dad2-4b90-b7e1-7aae59736e3a", "", ""],
    #"MBOffice":["Ae'gura", "BaronCityOffice", "aabecec0-b747-4437-a7de-7675be13e348", "MagicBot's", "Perf-SpawnPointBCO"],
    #"MBRudenna":["Magic RudennaCave", "BahroCave", "035ab538-e407-4d15-b666-68095f487243", "MagicBot's", ""],
    #"MBKadish":["Kadish", "Kadish", "a99728d2-9d2f-481f-bb9f-02b36709cbcd", "MagicBot's", "LinkInPointFromGallery"],
    "MBKadish":["Kadish", "Kadish", "fdd4cdbd-51db-4773-8bad-dff0cf14185b", "", ""],
    #"MBKveer":["Kveer", "Kveer", "e5738673-08ee-4e8f-8567-4acb982edfff", "MagicBot's", "LinkInPointPrison"],
    "MBKveer":["Kveer", "Kveer", "6cd9097b-33bc-4b7a-a78e-392dd4ef2235", "", "LinkInPointPrison"],
    #"MBGahreesen":["Gahreesen", "Garrison", "604cec77-e528-4f7c-b76c-68d0cb878ce1", "MagicBot's", ""],
    #"MBAhnonay":["Ahnonay", "Ahnonay", "dc0f2355-ebdd-4c47-9707-fc0fd6d33469", "", "LinkInPointSphere01"],
    #"MBAhnonay":["Ahnonay", "Ahnonay", "d56f0f22-6ab1-4e33-a245-9afdbacbf12e", "", ""],
    #"Polo":["Ahnonay", "Ahnonay", "702a17fd-9573-4da5-88b1-4e727a586bd0", "Water Polo", ""],
    #"polo1":["Ahnonay", "Ahnonay", "8f735605-9174-45f1-989b-688401827b06", "", ""],
    "polo":["Ahnonay", "Ahnonay", "4e1783b5-3620-4139-9798-b51f78cc354b", "", ""],
    #"MBDelin":["Eder Delin", "EderDelin", "fcc3692e-4723-433f-919e-fdc22bf6f4d1", "MagicBot's", ""],
    "MBDelin":["EderDelin", "EderDelin", "bfd99634-18cd-496e-9b7e-d0868c41e373", "", ""],
    #"MBTsogal":["Eder Tsogal", "EderTsogal", "33d1a429-6dc3-48d8-8bae-3901b8d72df6", "MagicBot's", ""],
    "MBTsogal":["EderTsogal", "EderTsogal", "5cac5a2b-2fd1-4287-b551-9601f7d8989b", "", ""],
    #"MBGira": ["Eder Gira", "Gira", "f1cd68aa-2710-4b1d-b95c-18d910c90e1f", "MagicBot's", "LinkInPointFromKemo"], 
    "MBGira":["Gira", "Gira", "627cb1ae-efbb-4e0f-9a95-8c1a7cf622ae", "", ""],
    #"MBKemo":["Garden", "Garden", "bd713fe9-23e7-4cd0-b875-6cdd1c7fb6f5", "MagicBot's", ""],
    "MBGarden":["Garden", "Garden", "365e1f3e-c779-4b85-a506-c01a76b7c88a", "", ""],
    "MBKemo":["Garden", "Garden", "365e1f3e-c779-4b85-a506-c01a76b7c88a", "", "Perf-SpawnPointKemo02"],
    #"MBJalak":["Jalak", "Jalak", "495499f1-4c56-42d7-b02b-d79bc328fc70", "Magic Bot's", ""],
    "MBJalak":["Jalak", "Jalak", "bf6516a8-c43a-436a-ab95-2318d7a38a7f", "", ""],
    #"MBMinkata":["Minkata", "Minkata", "41376d9b-173f-45d2-b379-2d406c2053f1", "", ""],
    "MBMinkata":["Minkata", "Minkata", "c5a6e34e-b8c4-45d7-8d18-e1224d5cd95f", "Magic Bot's", ""],
    #"soccer":["Minkata", "Minkata", "e2c7d61f-0b7e-4f11-9181-c98e401dcaa6", "", ""],
    "soccer":["Minkata", "Minkata", "eaca856a-7c6a-48bd-99c2-654263e694b1", "", ""],
    #"MBNegilahn":["Negilahn", "Negilahn", "e51a4ee9-a428-492b-b9aa-d199bf49e274", "", ""],
    #"MBGZ":["Ae'gura", "GreatZero", "e522677c-e2ba-4fea-9322-bb8799032de3", "", ""],
    #"MBSpy":["Ae'gura", "spyroom", "25d9b234-0a19-4b12-83b7-d4828169c80d", "", ""],
    "MBSpy":["spyroom", "spyroom", "78308f2a-e80f-47dd-9fb4-f1334ce72521", "", ""],
    "MBSilo":["ErcanaCitySilo", "ErcanaCitySilo", "28515865-127d-43f6-9c84-c630190807af", "", ""],
    "MBCave":["LiveBahroCaves", "LiveBahroCaves", "0e421cd5-e56a-426d-a7b7-51a98755ada2", "LiveBahroCaves", ""],
    #MagicGreatTreePub = "GreatTreePub":["GreatTreePub", "GreatTreePub", "75bdd14e-a525-4283-a5a0-579878f7305c", "GreatTreePub", ""],
    "MagicGreatTreePub":["GreatTreePub", "GreatTreePub", "75bdd14e-a525-4283-a5a0-579878f7305c", "Magic", ""],
    "MBDescent":["Descent", "Descent", "5db9ede0-afa4-47e8-ba15-02cb72b9117b", "Magic", ""],
    "MBGTP":["GreatTreePub", "GreatTreePub", "75bdd14e-a525-4283-a5a0-579878f7305c", "Magic", ""],
    #"TGTP":["GreatTreePub", "GreatTreePub", "75bdd14e-a525-4283-a5a0-579878f7305b", "Treasure", ""],
    #
    ##'Kirel":["Neighborhood02", "Kirel", "4cfbe95a-1bb2-4cbc-a6c4-87eb28a2aac1'],
    ##"Ae'gura":["City", "Ae'gura", "7e0facea-dae1-4aec-a4ca-e76c05fdcfcf'],
    ##"GreatTreePub":["GreatTreePub", "The Watchers Pub", "75bdd14e-a525-4283-a5a0-579878f7305a'],
    ##"PhilRelto":["philRelto", "Phil's Relto", "e8a2aaed-5cab-40b6-97f3-6d19dd92a71f'],
    ##"FunHouse":["Neighborhood", "FunHouse", "90938281-2c92-4e16-b959-85fce306f00c'],
    ##"CFunHouse":["City", "FunHouse City", "abee8828-869d-4756-89d3-5b374b518595'],
    ##"TVoltigeur":["Les Voltigeurs", "Neighborhood", "bd519469-f289-4c64-b77d-45C079e18d6c", "Les Voltigeurs'", ""],
    ##"CTVoltigeur":["Ville des Voltigeurs", "City", "e07e214f-5a7c-4165-8377-26ae4be8f42e", "Les Voltigeurs'", ""],
    #
    ##"STA1":["Hood", "Neighborhood02", "ebadcbee-df96-4db6-aaab-96797e49a53b", "STA1's", ""],
    ##"Sophie's Hood":["Hood", "Neighborhood", "17bec19d-6d33-4dd0-bbb6-8c9dca8c02f8", "Sophie's", ""],
    #
    ##" city":["city", "city", "c7001fdf-f7e2-4cff-82e9-15357a3b1379", "", ""],

}
tmp = dict()
for k, v in MagicbotAgeDict.items():
        tmp.update({k.lower(): v})
MagicbotAgeDict = tmp

#Instances publiques:
PublicAgeDict = {
    "city":["Ae'gura", "city", "f4dcfd9d-d897-4e5b-9ac9-f39961500bbb", "", "LinkInPointDakotahAlley"],
    "alley":["Ae'gura", "city", "f4dcfd9d-d897-4e5b-9ac9-f39961500bbb", "D'ni-", "LinkInPointDakotahAlley"],
    "tokotah":["Ae'gura", "city", "f4dcfd9d-d897-4e5b-9ac9-f39961500bbb", "D'ni-", "LinkInPointDakotahAlley"],
    "dakotah":["Ae'gura", "city", "f4dcfd9d-d897-4e5b-9ac9-f39961500bbb", "D'ni-", "DakotahRoofPlayerStart"],
    "ferry":["Ae'gura", "city", "f4dcfd9d-d897-4e5b-9ac9-f39961500bbb", "D'ni-", "LinkInPointFerry"],
    "concert":["Ae'gura", "city", "f4dcfd9d-d897-4e5b-9ac9-f39961500bbb", "D'ni-", "LinkInPointConcertHallFoyer"],
    "library":["Ae'gura", "city", "f4dcfd9d-d897-4e5b-9ac9-f39961500bbb", "D'ni-", "LinkInPointLibrary"],
    "palace":["Ae'gura", "city", "f4dcfd9d-d897-4e5b-9ac9-f39961500bbb", "D'ni-", "LinkInPointPalace"],
    #"gallery":["Ae'gura", "city", "f4dcfd9d-d897-4e5b-9ac9-f39961500bbb", "D'ni-", "LinkInPointKadishGallery"],

    #"city":["Ae'gura", "city", "7e0facea-dae1-4aec-a4ca-e76c05fdcfcf", "D'ni-", "LinkInPointDakotahAlley"],
    #"tokotah":["Ae'gura", "city", "7e0facea-dae1-4aec-a4ca-e76c05fdcfcf", "D'ni-", "LinkInPointDakotahAlley"],
    #"dakotah":["Ae'gura", "city", "7e0facea-dae1-4aec-a4ca-e76c05fdcfcf", "D'ni-", "DakotahRoofPlayerStart"],
    #"ferry":["Ae'gura", "city", "7e0facea-dae1-4aec-a4ca-e76c05fdcfcf", "D'ni-", "LinkInPointFerry"],
    #"concert":["Ae'gura", "city", "7e0facea-dae1-4aec-a4ca-e76c05fdcfcf", "D'ni-", "LinkInPointConcertHallFoyer"],
    #"library":["Ae'gura", "city", "7e0facea-dae1-4aec-a4ca-e76c05fdcfcf", "D'ni-", "LinkInPointLibrary"],
    #"palace":["Ae'gura", "city", "7e0facea-dae1-4aec-a4ca-e76c05fdcfcf", "D'ni-", "LinkInPointPalace"],
    #"gallery":["Ae'gura", "city", "7e0facea-dae1-4aec-a4ca-e76c05fdcfcf", "D'ni-", "LinkInPointKadishGallery"],
    #
    #"phil":["philRelto", "philRelto", "e8a2aaed-5cab-40b6-97f3-6d19dd92a71f", "philRelto", ""],
    "phil":["philRelto", "philRelto", "e8a2aaed-5cab-40b6-97f3-6d19dd92a71f", "philRelto", ""],
    #
    "kirel":["Kirel", "Neighborhood02", "4cfbe95a-1bb2-4cbc-a6c4-87eb28a2aac1", "D'ni-", ""],
    "kveer":["Kveer", "Kveer", "68e219e0-ee25-4df0-b855-0435584e29e2", "D'ni-", "LinkInPointPrison"],
    #"cartographers":["GuildPub-Cartographers", "GuildPub-Cartographers", "35624301-841e-4a07-8db6-b735cf8f1f53", "", ""],
    "cartographers":["GuildPub-Cartographers", "GuildPub-Cartographers", "35624301-841e-4a07-8db6-b735cf8f1f53", "GuildPub-Cartographers", ""],
    "greeters":["GuildPub-Greeters", "GuildPub-Greeters", "381fb1ba-20a0-45fd-9bcb-fd5922439d05", "", ""],
    "maintainers":["GuildPub-Maintainers", "GuildPub-Maintainers", "e8306311-56d3-4954-a32d-3da01712e9b5", "", ""],
    "messengers":["GuildPub-Messengers", "GuildPub-Messengers", "9420324e-11f8-41f9-b30b-c896171a8712", "", ""],
    "watcher":["The Watcher's Pub", "GreatTreePub", "75bdd14e-a525-4283-a5a0-579878f7305a", "D'ni-", ""],
    "watchers":["The Watcher's Pub", "GreatTreePub", "75bdd14e-a525-4283-a5a0-579878f7305a", "D'ni-", ""],
    "pub":["The Watcher's Pub", "GreatTreePub", "75bdd14e-a525-4283-a5a0-579878f7305a", "D'ni-", ""],
    "writers":["GuildPub-Writers", "GuildPub-Writers", "5cf4f457-d546-47dc-80eb-a07cdfefa95d", "", ""],
    #"fhwatcher":["The Watcher's Pub", "GreatTreePub", "71f6ceab-a883-4fe7-9b9a-1fe12e79c731", "The Fun House's", ""],
    #"gog":["Hood", "Neighborhood", "4a2b83f1-2095-4d95-9f2a-e011d5c2a821", "Guild of Greeters'", ""],
    "gog":["Hood", "Neighborhood", "ce228892-97ff-42d3-bd3f-2726b4e61f5b", "Guild of Greeters'", ""],
    "gome":["Hood", "Neighborhood", "34ac88e0-14e3-4eb2-87b7-984725875e44", "Guild of Messengers'", ""],
    #"international":["Hood", "Neighborhood", "6f14a9e0-a439-44dd-9eaa-95375bb5766a", "International's", ""],
    "international":["Hood", "Neighborhood", "b98bd2b4-3c56-4508-a239-2302e03f01f3", "International's", ""],
    #"obd":["Hood", "Neighborhood", "0e2fc3d4-eca3-40ee-ab10-7ae6b37a8b82", "Obductee's", ""],
    "obd":["Hood", "Neighborhood", "02ab8bcd-2d66-4727-a295-fa6850132aa6", "Obductee's", ""],
    "tjh":["Hood", "Neighborhood", "200be199-f5a0-40a7-b0c9-dad2eb5898e3", "Tereeza's", ""],
    "veelay":["Veelay Tsahvahn", "VeeTsah", "c446d2ed-225f-4492-a9b6-3569d77e462b", "", ""],
    "chiso":["ChisoPreniv", "ChisoPreniv", "0b4f5ad9-d93d-52e3-83e4-9364c2149ae4", "ChisoPreniv", ""],
    "oldmessengerspub":["Messengers' Pub - Ae'gura", "GoMePubNew", "0e1c2ec4-47e0-4231-b258-75d9e138b4b9", "", ""],
    "messengerspub":["Messengers' Pub - Ae'gura", "GoMePubNew", "d002da26-db26-53f1-bdc0-a05a84274d5c", "", ""], #GoMePubNew(9)
    "serene":["Serene", "Serene", "4b70e35f-80c8-463c-b8f5-087e211c112e", "", ""],
    "trebivdil":["Tre'bivdil", "trebivdil", "5b06b39d-27ff-4a80-a00e-40bbdb802e8a", "", ""],
    "vothol":["Vothol Gallery", "Vothol", "303478a8-9e47-4aa7-adc5-985a09033ee8", "", ""],
}
"""
Ae'gura	D'ni-Ae'gura	13	f4dcfd9d-d897-4e5b-9ac9-f39961500bbb
Guild Pub	The Greeters' Guild Pub	0	381fb1ba-20a0-45fd-9bcb-fd5922439d05
Guild Pub	The Maintainers' Guild Pub	0	e8306311-56d3-4954-a32d-3da01712e9b5
Guild Pub	The Messengers' Guild Pub	0	9420324e-11f8-41f9-b30b-c896171a8712
Guild Pub	The Writers' Guild Pub	0	5cf4f457-d546-47dc-80eb-a07cdfefa95d
Kirel	The DRC's Guild Age	0	4cfbe95a-1bb2-4cbc-a6c4-87eb28a2aac1
K'veer	Atrus's Childhood Prison	0	68e219e0-ee25-4df0-b855-0435584e29e2
The Watcher's Pub	The Watcher's Sanctuary	1	75bdd14e-a525-4283-a5a0-579878f7305a
Neighborhood	Guild of Greeters' Hood	0	ce228892-97ff-42d3-bd3f-2726b4e61f5b
Neighborhood	Obductees' Hood	0	02ab8bcd-2d66-4727-a295-fa6850132aa6

"""

# liste des instances disponibles pour moi
# (instance name, file name, guid, user defined name, spawn point)
linkDic = {
    #"fh":["Fun House", "Neighborhood", "90938281-2c92-4e16-b959-85fce306f00c", "The", "LinkInPointBevinBalcony"],
    "fh":["Fun House", "Neighborhood", "33a235b1-9fe0-47f0-a73e-6fbd0044717a", "The", "LinkInPointBevinBalcony"],
    ##"fhci":["The Fun House - City", "city", "abee8828-869d-4756-89d3-5b374b518595", "", "LinkInPointBahro-PalaceBalcony"],
    ##"fhde":["Fun House\'s (1) Eder Delin", "EderDelin", "b0512722-ef62-4fc2-a414-7c7d883a0456", "", ""],
    ##"fhga":["Fun House\'s Gahreesen", "Garrison", "268fc252-6b65-4e06-bb55-ae87869ebd25", "", "LinkInPointGearRm"],
    ##"fhte":["Fun House\'s Teledahn", "Teledahn", "66174cf2-ecf0-4001-969e-ec72092937b0", "", "Perf-SpawnPointExterior02"],
    ##"fhka":["The Fun House - Kadish Tolesa", "Kadish", "8d17ee0f-a127-4267-90fe-587f5998d520", "", "LinkInPointFromGallery"],
    ##"fhgi":["The Fun House - Eder Gira", "Gira", "2f21a44c-5a05-45f7-9587-4ca519f55f71", "", "LinkInPointFromKemo"],
    ##"fhke":["The Fun House - Eder Kemo", "Garden", "b75e5acb-75c1-40e4-bee1-47b0a67d7340", "", ""],
    ##"fhcl":["Fun House\'s Cleft", "Cleft", "da475fa8-b810-4310-9193-9bbd73ca3c64", "", "LinkInPointFissureDrop"],
    ##"fhmy":["Fun House\'s Myst", "Myst", "d92fc69a-badc-49a8-b586-3de8754e598e", "", "FireplaceStartPoint"],
    ##"fhph":["The Fun House - Phil\'s Relto", "philRelto", "e8a2aaed-5cab-40b6-97f3-6d19dd92a71f", "", "LinkInPointCloset"],

    ##"fh":["Hood", "Neighborhood", "90938281-2c92-4e16-b959-85fce306f00c", "Fun House's", "LinkInPointBevinBalcony"],
    #"fhci":["city", "city", "abee8828-869d-4756-89d3-5b374b518595", "Fun House's", "LinkInPointBahro-PalaceBalcony"],
    ##"fhde":["Eder Delin", "EderDelin", "b0512722-ef62-4fc2-a414-7c7d883a0456", "Fun House's", "", "1"],
    #"fhde":["Eder Delin", "EderDelin", "b0512722-ef62-4fc2-a414-7c7d883a0456", "Fun House's", ""],
    #"fhga":["Gahreesen", "Garrison", "268fc252-6b65-4e06-bb55-ae87869ebd25", "Fun House's", "LinkInPointGearRm"],
    #"fhte":["Teledahn", "Teledahn", "66174cf2-ecf0-4001-969e-ec72092937b0", "Fun House's", "Perf-SpawnPointExterior02"],
    #"fhka":["Kadish", "Kadish", "8d17ee0f-a127-4267-90fe-587f5998d520", "Fun House's", "LinkInPointFromGallery"],
    #"fhgi":["Eder Gira", "Gira", "2f21a44c-5a05-45f7-9587-4ca519f55f71", "Fun House's", "LinkInPointFromKemo"],
    #"fhke":["Eder Kemo", "Garden", "b75e5acb-75c1-40e4-bee1-47b0a67d7340", "Fun House's", ""],
    #"fhcl":["Cleft", "Cleft", "da475fa8-b810-4310-9193-9bbd73ca3c64", "Fun House's", "LinkInPointFissureDrop"],
    #"fhmy":["Myst", "Myst", "d92fc69a-badc-49a8-b586-3de8754e598e", "Fun House's", "FireplaceStartPoint"],
    #"fhph":["Phil\'s Relto", "philRelto", "e8a2aaed-5cab-40b6-97f3-6d19dd92a71f", "Fun House's", "LinkInPointCloset"],
    #
    #"gz":["Great Zero", "GreatZero", "1e309bb5-3548-49f5-afdb-91fe38eb3438", "Test's", "BigRoomLinkInPoint"],
    #"ki":["Kirel", "Neighborhood02", "4cfbe95a-1bb2-4cbc-a6c4-87eb28a2aac1", "D'ni-", "kirelPerf-SpawnPointBevin01"],
    #"ki2":["V@Michel\'s D\'ni Kirel", "Neighborhood02", "c85db77e-3908-4f37-b115-e62fc0ce6968", "Not exactly", "kirelPerf-SpawnPointBevin02"],
    #"tvh":["TVoltigeur\'s Hood", "Neighborhood", "bd519469-f289-4c64-b77d-45c079e18d6c", "TVoltigeur's", "LinkInPointBevinBalcony"],
    #"wp":["The Watcher\'s Pub", "GreatTreePub", "71f6ceab-a883-4fe7-9b9a-1fe12e79c731", "Not exactly", "RedHerringDoorSafePoint"],
    ##"wp":["The Watcher's Pub", "GreatTreePub", "71f6ceab-a883-4fe7-9b9a-1fe12e79c731", "Not Exactly", ""],
    #"dmr":["Hood", "Neighborhood", "8b5769a4-1d4f-4c03-b0c5-949b73e93f29", "D\'ni Musicological research\'s", "LinkInPointBevinBalcony"],
    #
    #"mbe":["Ercana", "Ercana", "eccb9705-60b5-4746-b77c-02a3cf73f6a8", "MagicBot's", "StartPoint"],
    #"mcl":["Cleft", "Cleft", "53c424e2-5922-44e8-be1f-1215ec8d9820", "MagicBot's", "LinkInPointFissureDrop"],
    #"mre":["Relto", "Personal", "798cc281-e224-4c60-aba4-5cc43027d069", "MagicBot's", "LinkInPointBahroPoles"],
    #"mte":["Teledahn", "Teledahn", "edb74f4d-e0c5-4867-b8a6-f7f823bbd449", "MagicBot's", "Perf-SpawnPointExterior02"],
    #"mso":["Sharper Office", "BaronCityOffice", "798cc281-e224-4c60-aba4-5cc43027d069", "MagicBot's", "Perf-SpawnPointBCO"],
    #"mkv":["Kveer","Kveer","e5738673-08ee-4e8f-8567-4acb982edfff", "MagicBot's", "LinkInPointPrison"],
    #"mka":["Magic Tolesa", "Kadish","a99728d2-9d2f-481f-bb9f-02b36709cbcd", "MagicBot's", "LinkInPointFromGallery"],
    ##"nmci":["Not Magic City", "city", "91d5c0f8-69c7-4c28-8218-1fab5cf284f0", "Not MagicBot's", "LinkInPointBahro-PalaceBalcony"],
    #"mci":["city", "city", "411e452b-7077-4328-ad5b-4dadc1467a9a", "MagicBot's", "LinkInPointBahro-PalaceBalcony"],
    #
    ##"scl":["Cleft", "Cleft", "13fb8323-350c-4f98-90be-50c870450fa6", "Stone5's", "LinkInPointFissureDrop"],
    "stldn":["Teledahn", "Teledahn", "f5f8774b-bf24-4c24-96a1-ebf8053b5574", "Stone5's", ""],
    #
    ##"glh":["Hood", "Neighborhood", "e15f2919-9d76-4af4-8ba7-f63f674451e2", "GoLeaners'", "LinkInPointBevinBalcony"],
    #"hi":["Hood of Illusions", "Neighborhood", "827d535d-af75-4b1a-b78f-696ecd8770f7", "The", ""],
}


# ahnySphere01:
#   LinkInPointSphere01
#   SaveClothPoint31
#   SaveClothPoint_old
# ahnySphere02:
#   LinkInPointSphere02
#   SaveClothPoint12
#   SaveClothPoint22
#   SaveClothPoint32
# ahnySphere03:
#   LinkInPointSphere03
#   SaveClothPoint13
#   SaveClothPoint23
#   SaveClothPoint33
# ahnySphereCtrl:
#   LinkInPointDefault
# EngeneerHut:
#   SaveClothPoint74
# Hub:
#   Dummy01
# MaintRoom01:
#   SaveClothPoint41
#   SaveClothPoint51
#   SaveClothPoint61
#   StartPoint
# MaintRoom02:
#   SaveClothPoint42
#   SaveClothPoint52
#   SaveClothPoint62
#   StartPoint
# MaintRoom03:
#   SaveClothPoint43
#   SaveClothPoint53
#   SaveClothPoint63
#   StartPoint
# MaintRoom04:
#   SaveClothPoint44
#   SaveClothPoint54
#   SaveClothPoint64
#   StartPoint
