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
        print "{5} : {3} ({4}) {0}|{1}|{2}".format(ageInfo.getAgeInstanceName(), ageInfo.getAgeFilename(), ageInfo.getAgeInstanceGuid(), ageInfo.getAgeUserDefinedName(), ageInfo.getAgeSequenceNumber(), myKey)

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
    for k, v in sorted(ageDict.iteritems()):
        print "{0}:{1}, ".format(k, v)

#
MirphakAgeDict = {
}

tmp = dict()
for k, v in MirphakAgeDict.iteritems():
        tmp.update({k.lower().replace(" ", "").replace("'", "").replace("eder", ""): v})
MirphakAgeDict = tmp

PrivateAgeDict = {
}

MirobotAgeDict = {
    "ahnonay":["Ahnonay", "Ahnonay", "55ce4207-aba9-4f2e-80de-7980a75ac3f2", "Mir-o-Bot's", ""],
    "aegura":["city", "city", "9511bed4-d2cb-40a6-9983-6025cdb68d8b", "Mir-o-Bot's", "LinkInPointBahro-PalaceBalcony"],
    "cathedral":["Ahnonay Cathedral", "AhnonayCathedral", "bf4528a7-cb82-46ea-964d-1615a6babb0e", "Mir-o-Bot's", ""], 
    "cleft":["Cleft", "Cleft", "fef1ef9f-09dd-422c-a3d6-1229d615af85", "Mir-o-Bot's", "LinkInPointFissureDrop"], 
    "cleft1":["Cleft", "Cleft", "fef1ef9f-09dd-422c-a3d6-1229d615af85", "Mir-o-Bot's", "Perf-SpawnPointDesert01"], 
    "cleft2":["Cleft", "Cleft", "fef1ef9f-09dd-422c-a3d6-1229d615af85", "Mir-o-Bot's", "Perf-SpawnPointChasm02"], 
    "dereno":["Dereno", "Dereno", "330f59b9-9b21-4130-81e4-9852d3493fa9", "Mir-o-Bot's", ""], 
    "ercana":["Er'cana", "Ercana", "eb048e3d-c0ec-4a60-bc93-a64b67c58a66", "Mir-o-Bot's", ""], 
    "oven":["Er'cana", "Ercana", "eb048e3d-c0ec-4a60-bc93-a64b67c58a66", "Mir-o-Bot's", "LinkInPointPelletRoom"], 
    "gahreesen" :["Gahreesen", "Garrison", "42f261ba-b74e-45a3-afb8-0bda76f44b34", "Mir-o-Bot's", ""], 
    "gear"      :["Gahreesen", "Garrison", "42f261ba-b74e-45a3-afb8-0bda76f44b34", "Mir-o-Bot's", "LinkInPointGearRm"], 
    "pinnacle"  :["Gahreesen", "Garrison", "42f261ba-b74e-45a3-afb8-0bda76f44b34", "Mir-o-Bot's", "LinkInPointPinnacle"], 
    "training"  :["Gahreesen", "Garrison", "42f261ba-b74e-45a3-afb8-0bda76f44b34", "Mir-o-Bot's", "StartPointEntry01"], 
    "team"      :["Gahreesen", "Garrison", "42f261ba-b74e-45a3-afb8-0bda76f44b34", "Mir-o-Bot's", "StartinBoxYellow"], 
    "team2"     :["Gahreesen", "Garrison", "42f261ba-b74e-45a3-afb8-0bda76f44b34", "Mir-o-Bot's", "StartinBoxPurple"], 
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
    "mobkveer":["K'veer", "Kveer", "dc721118-1ea2-44ad-9ff0-df58676ed73c", "Mir-o-Bot's", ""],
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
    "GZ":["Ae'gura", "GreatZero", "76aa23d2-07a0-45f6-b355-5de39302f455", "Mir-o-Bot's GZ", ""],
    "GreatZero":["Ae'gura", "GreatZero", "76aa23d2-07a0-45f6-b355-5de39302f455", "Mir-o-Bot's GZ", ""],
    "Descent":["Descent", "Descent", "4543f4e3-aa4b-4c4b-b6f4-eaa1aee4c440", "Mir-o-Bot's", "LinkInPointShaftFall"],
    "Tiwah":["Descent", "Descent", "4543f4e3-aa4b-4c4b-b6f4-eaa1aee4c440", "Mir-o-Bot's", "LinkInPointShaftFall"],
    "GreatShaft":["Descent", "Descent", "4543f4e3-aa4b-4c4b-b6f4-eaa1aee4c440", "Mir-o-Bot's", ""],
    
    "PrimeCave":["LiveBahroCaves", "LiveBahroCaves", "74b81313-c5f4-4eec-8e21-94d55e59ea8a", "Mir-o-Bot's Prime", ""],
    "PodsCave":["LiveBahroCaves", "LiveBahroCaves", "9b764f14-2d0e-493e-aa4a-e7ed218e3168", "Mir-o-Bot's Pods", ""],
    "EderCave":["LiveBahroCaves", "LiveBahroCaves", "1c9388c2-e4da-4e2e-a442-a0f58ad216b9", "Mir-o-Bot's Eder", ""],
    "Rudenna":["BahroCave", "BahroCave", "a8f6a5a6-4e5e-4d3f-9160-a9b75f0768c5", "Mir-o-Bot's Rudenna", ""],
    "pelletcave":["Pellet Cave", "PelletBahroCave", "13c1fdfc-44e2-4230-803a-147d8e6918a0", "Mir-o-Bot's (top)", ""], 
    "pellet1":["Pellet Cave", "PelletBahroCave", "13c1fdfc-44e2-4230-803a-147d8e6918a0", "Mir-o-Bot's (top)", "LinkInWithPellet"], 
    "pellet2":["Pellet Cave", "PelletBahroCave", "13c1fdfc-44e2-4230-803a-147d8e6918a0", "Mir-o-Bot's (bottom)", "LinkInPointLower"], 
    "Silo":["ErcanaCitySilo", "ErcanaCitySilo", "88177069-fd83-4a07-ba87-5800016e2f28", "Mir-o-Bot's", ""],
    "Office":["Ae'gura", "BaronCityOffice", "2aaf334b-a49e-40f2-963b-5be146d40021", "Mir-o-Bot's Office", ""],
    
    "spyroom":["spyroom", "spyroom", "df9d49ec-0b9c-4716-9a0f-a1b66f7d9814", "mob's (Sharper's spy room)", ""],
}

tmp = dict()
for k, v in MirobotAgeDict.iteritems():
        tmp.update({k.lower().replace(" ", "").replace("'", "").replace("eder", ""): v})
MirobotAgeDict = tmp


#MagicBot ages:
MagicbotAgeDict = {
}
tmp = dict()
for k, v in MagicbotAgeDict.iteritems():
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
    "phil":["philRelto", "philRelto", "e8a2aaed-5cab-40b6-97f3-6d19dd92a71f", "philRelto", ""],
    "kirel":["Kirel", "Neighborhood02", "4cfbe95a-1bb2-4cbc-a6c4-87eb28a2aac1", "D'ni-", ""],
    "kveer":["Kveer", "Kveer", "68e219e0-ee25-4df0-b855-0435584e29e2", "D'ni-", "LinkInPointPrison"],
    "cartographers":["GuildPub-Cartographers", "GuildPub-Cartographers", "35624301-841e-4a07-8db6-b735cf8f1f53", "GuildPub-Cartographers", ""],
    "greeters":["GuildPub-Greeters", "GuildPub-Greeters", "381fb1ba-20a0-45fd-9bcb-fd5922439d05", "", ""],
    "maintainers":["GuildPub-Maintainers", "GuildPub-Maintainers", "e8306311-56d3-4954-a32d-3da01712e9b5", "", ""],
    "messengers":["GuildPub-Messengers", "GuildPub-Messengers", "9420324e-11f8-41f9-b30b-c896171a8712", "", ""],
    "watcher":["The Watcher's Pub", "GreatTreePub", "75bdd14e-a525-4283-a5a0-579878f7305a", "D'ni-", ""],
    "watchers":["The Watcher's Pub", "GreatTreePub", "75bdd14e-a525-4283-a5a0-579878f7305a", "D'ni-", ""],
    "pub":["The Watcher's Pub", "GreatTreePub", "75bdd14e-a525-4283-a5a0-579878f7305a", "D'ni-", ""],
    "writers":["GuildPub-Writers", "GuildPub-Writers", "5cf4f457-d546-47dc-80eb-a07cdfefa95d", "", ""],
}

# liste des instances disponibles pour moi
# (instance name, file name, guid, user defined name, spawn point)
linkDic = {
}

