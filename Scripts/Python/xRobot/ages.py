from Plasma import *

def ListMyAges():
    ages = ptVault().getAgesIOwnFolder().getChildNodeRefList()
    for age in ages:
        ageInfo = age.getChild().upcastToAgeLinkNode().getAgeInfo()
        myKey = ageInfo.getAgeInstanceName()
        myKey = myKey.lower()
        myKey = myKey.replace(" ", "")
        myKey = myKey.replace("'", "")
        myKey = myKey.replace("eder", "")
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
    return ageDict

#
def PrintMyAgeList():
    ageDict = GetMyAges()
    for k, v in sorted(ageDict.items()):
        print("{0}:{1}, ".format(k, v))

#
MirphakAgeDict = {
}

tmp = dict()
for k, v in MirphakAgeDict.items():
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
    "yellowteam":["Gahreesen", "Garrison", "42f261ba-b74e-45a3-afb8-0bda76f44b34", "Mir-o-Bot's", "LinkInPointCtrlRm01"], 
    "teamyellow":["Gahreesen", "Garrison", "42f261ba-b74e-45a3-afb8-0bda76f44b34", "Mir-o-Bot's", "LinkInPointCtrlRm01"], 
    "yellow"    :["Gahreesen", "Garrison", "42f261ba-b74e-45a3-afb8-0bda76f44b34", "Mir-o-Bot's", "LinkInPointCtrlRm01"], 
    "gctrl2"    :["Gahreesen", "Garrison", "42f261ba-b74e-45a3-afb8-0bda76f44b34", "Mir-o-Bot's", "LinkInPointCtrlRm02"], 
    "purpleteam":["Gahreesen", "Garrison", "42f261ba-b74e-45a3-afb8-0bda76f44b34", "Mir-o-Bot's", "LinkInPointCtrlRm02"], 
    "teampurple":["Gahreesen", "Garrison", "42f261ba-b74e-45a3-afb8-0bda76f44b34", "Mir-o-Bot's", "LinkInPointCtrlRm02"], 
    "purple"    :["Gahreesen", "Garrison", "42f261ba-b74e-45a3-afb8-0bda76f44b34", "Mir-o-Bot's", "LinkInPointCtrlRm02"], 
    "gnexus"    :["Gahreesen", "Garrison", "42f261ba-b74e-45a3-afb8-0bda76f44b34", "Mir-o-Bot's", "LinkInPointDefaultWhite"], 
    "gira":["Eder Gira", "Gira", "5b4678a9-73ab-4b45-9058-e710b45e4dbe", "Mir-o-Bot's", "LinkInPointFromKemo"], 
    "hood":["Hood", "Neighborhood", "e6958ab2-f925-4e36-a884-ee65e5c73896", "Mir-o-Bot's", "LinkInPointBevinBalcony"], 
    "jalak":["Jalak", "Jalak", "1269ee23-baff-4ca2-a3bc-f80df29fe978", "Mir-o-Bot's", ""], 
    "kadish":["Kadish", "Kadish", "31b44de5-0d1e-4c1b-8d8d-d9592df2f214", "Mir-o-Bot's", "LinkInPointFromGallery"], 
    "kemo":["Eder Kemo", "Garden", "3a366b1e-9488-4c77-a278-a6375161ac92", "Mir-o-Bot's", "Perf-SpawnPointKemo02"], 
    "mobKemo":["Eder Kemo", "Garden", "3edc8f3b-fa2c-486e-83f3-795435b2dc88", "mob's", ""],
    "mobgz":["GreatZero", "GreatZero", "66d12fcf-4635-4e7d-b991-38fa5d70108a", "mob's", "BigRoomLinkInPoint"],
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
    "pellet1":["Pellet Cave", "PelletBahroCave", "13c1fdfc-44e2-4230-803a-147d8e6918a0", "Mir-o-Bot's (top)", "LinkInWithPellet"], 
    "pellet2":["Pellet Cave", "PelletBahroCave", "13c1fdfc-44e2-4230-803a-147d8e6918a0", "Mir-o-Bot's (bottom)", "LinkInPointLower"], 
    "Silo":["ErcanaCitySilo", "ErcanaCitySilo", "88177069-fd83-4a07-ba87-5800016e2f28", "Mir-o-Bot's", ""],
    "Office":["Ae'gura", "BaronCityOffice", "2aaf334b-a49e-40f2-963b-5be146d40021", "Mir-o-Bot's Office", ""],
    "spyroom":["spyroom", "spyroom", "df9d49ec-0b9c-4716-9a0f-a1b66f7d9814", "mob's (Sharper's spy room)", ""],
    "fh":["Fun House", "Neighborhood", "33a235b1-9fe0-47f0-a73e-6fbd0044717a", "The", "LinkInPointBevinBalcony"],
    "hi":["Hood of Illusions", "Neighborhood", "3cc44d4b-31e1-4dec-b6e6-4b63c72becc3", "The", ""],
    "GreatTreePub":["GreatTreePub", "GreatTreePub", "08980412-c527-496e-af41-123d40cc06a7", "GreatTreePub", ""],
    "mobgomepub":["GoMePubNew", "GoMePubNew", "da149d57-5671-4302-95d6-8d9ea52167ff", "Mir-o-Bot's", ""],
    "mobchiso":["ChisoPreniv", "ChisoPreniv", "788b836d-2019-48bd-af66-c9f0674dff5a", "Mir-o-Bot's", ""],
    "mobveelay":["VeeTsah", "VeeTsah", "e8c6fbef-4e47-4951-8a9f-ab8c1b800c49", "Mir-o-Bot's", ""],
    "mobSerene":["Serene", "Serene", "f5a44340-3506-4c8f-af97-8bb338193460", "Mir-o-Bot's", ""],
    "mobTrebivdil":["Tre'bivdil", "trebivdil", "ea180c91-e06d-44c4-b18c-c769a7c714cb", "Mir-o-Bot's", ""],
    "mobVothol":["Vothol Gallery", "vothol", "09d93976-b95d-4a31-b2e7-0e63903d77ff", "Mir-o-Bot's", ""],
    "MoB Elonin":["Elonin", "Elonin", "15f9fae2-c9bc-4db4-96ad-f32067840cce", "Mir-o-Bot's", ""],
    "MoB Eder Naybree":["Eder Naybree", "EderNaybree", "ec3f9b55-d6ff-4006-9061-4b8ebc2bd6d2", "Mir-o-Bot's", ""],
    "mobCartographers":["GuildPub-Cartographers", "GuildPub-Cartographers", "23ac83d3-dc52-4572-9b0a-ad13c298276c", "Mir-o-Bot's", ""],
    "mobGreeters":["GuildPub-Greeters", "GuildPub-Greeters", "7a69bacf-2dd0-4b8c-88ae-9878ea1157d3", "Mir-o-Bot's", ""],
    "mobMaintainers":["GuildPub-Maintainers", "GuildPub-Maintainers", "a9e45d08-dfdf-48a7-9539-bdaaa60c13e9", "Mir-o-Bot's", ""],
    "mobMessengers":["GuildPub-Messengers", "GuildPub-Messengers", "950e27bb-77a5-427a-8d7a-c121feb6a74c", "Mir-o-Bot's", ""],
    "mobWriters":["GuildPub-Writers", "GuildPub-Writers", "bf869aee-48b7-406b-a717-8e7c04dc24c0", "Mir-o-Bot's", ""],
    "mobEderBahvahnter":["EderBahvahnter", "EderBahvahnter", "9c5f0961-8299-492f-9f9b-2f3d48f58a55", "Mir-o-Bot's", ""],
    "MobMemorial":["Memorial Island", "MemorialIsland", "bf0c191e-32f5-42a4-a975-5d5656f29796", "Mir-o-Bot's", ""],
    "mobGahreesen":["Gahreesen", "Garrison", "f3e10b6e-069c-4329-903e-3b0377f7e510", "mob's", ""],
    "Tiam":["Tiam", "Tiam", "0c3db58b-0c1a-47a9-8e33-8c061640b9cb", "Mir-o-Bot's", ""],
    "mobTiam":["Tiam", "Tiam", "5e018f72-0ae7-4db8-ba52-101117eb3d15", "mob's", ""],
    "mobElonin2":["Elonin", "Elonin", "b318f385-45ae-4377-9f1c-6e629233f994", "mob's", ""],
    "mobFahetsHighgarden":["FahetsHighgarden", "FahetsHighgarden", "039c7539-ba3d-41d5-a571-0de8da6cb7fd", "mob's", ""],
    "mobFahets":["FahetsHighgarden", "FahetsHighgarden", "039c7539-ba3d-41d5-a571-0de8da6cb7fd", "mob's", ""],
    "mobHighgarden":["FahetsHighgarden", "FahetsHighgarden", "039c7539-ba3d-41d5-a571-0de8da6cb7fd", "mob's", ""],
    "mobKalamee":["Kalamee", "Kalamee", "a035e8c5-a7c1-459b-bfc7-fbbb84014562", "mob's", ""],
    "Kalamee":["Kalamee", "Kalamee", "cb7d9652-4f46-485d-966e-8b144519f413", "Mir-o-Bot's", ""],
}

tmp = dict()
for k, v in MirobotAgeDict.items():
        tmp.update({k.lower().replace(" ", "").replace("'", "").replace("eder", ""): v})
MirobotAgeDict = tmp


#MagicBot ages:
MagicbotAgeDict = {
    "MBErcana":["Ercana", "Ercana", "7c6348d0-ea67-496f-922c-ed940b54f534", "", ""],
    "MBcity":["city", "city", "2cb76f8d-2b26-4732-8275-cdd4172424f0", "", "LinkInPointBahro-PalaceBalcony"],
    "MimiRelto":["Relto", "Personal", "a0f1f587-1819-4e48-9ea5-80c6ed299ba5", "Mimi Bot's", ""],
    "Mimi-Relto":["Relto", "Personal", "138b35b8-2c17-4107-95ed-d65294c9aced", "Mimi-Bot's", ""],
    "MBHood":["Hood", "Neighborhood", "65ef6345-3aa7-4233-a5bb-e86280cc0dd3", "Magic Bot's", ""],
    "MBDereno":["Dereno", "Dereno", "462edc6f-d783-44ae-b254-1bd7b0205082", "MagicBot's", ""],
    "MBTeledahn":["Teledahn", "Teledahn", "955890b9-dad2-4b90-b7e1-7aae59736e3a", "", ""],
    "MBKadish":["Kadish", "Kadish", "fdd4cdbd-51db-4773-8bad-dff0cf14185b", "", ""],
    "MBKveer":["Kveer", "Kveer", "6cd9097b-33bc-4b7a-a78e-392dd4ef2235", "", "LinkInPointPrison"],
    "polo":["Ahnonay", "Ahnonay", "4e1783b5-3620-4139-9798-b51f78cc354b", "", ""],
    "MBDelin":["EderDelin", "EderDelin", "bfd99634-18cd-496e-9b7e-d0868c41e373", "", ""],
    "MBTsogal":["EderTsogal", "EderTsogal", "5cac5a2b-2fd1-4287-b551-9601f7d8989b", "", ""],
    "MBGira":["Gira", "Gira", "627cb1ae-efbb-4e0f-9a95-8c1a7cf622ae", "", ""],
    "MBGarden":["Garden", "Garden", "365e1f3e-c779-4b85-a506-c01a76b7c88a", "", ""],
    "MBKemo":["Garden", "Garden", "365e1f3e-c779-4b85-a506-c01a76b7c88a", "", "Perf-SpawnPointKemo02"],
    "MBJalak":["Jalak", "Jalak", "bf6516a8-c43a-436a-ab95-2318d7a38a7f", "", ""],
    "MBMinkata":["Minkata", "Minkata", "c5a6e34e-b8c4-45d7-8d18-e1224d5cd95f", "Magic Bot's", ""],
    "soccer":["Minkata", "Minkata", "eaca856a-7c6a-48bd-99c2-654263e694b1", "", ""],
    "MBSpy":["spyroom", "spyroom", "78308f2a-e80f-47dd-9fb4-f1334ce72521", "", ""],
    "MBSilo":["ErcanaCitySilo", "ErcanaCitySilo", "28515865-127d-43f6-9c84-c630190807af", "", ""],
    "MBCave":["LiveBahroCaves", "LiveBahroCaves", "0e421cd5-e56a-426d-a7b7-51a98755ada2", "LiveBahroCaves", ""],
    "MagicGreatTreePub":["GreatTreePub", "GreatTreePub", "75bdd14e-a525-4283-a5a0-579878f7305c", "Magic", ""],
    "MBDescent":["Descent", "Descent", "5db9ede0-afa4-47e8-ba15-02cb72b9117b", "Magic", ""],
    "MBGTP":["GreatTreePub", "GreatTreePub", "75bdd14e-a525-4283-a5a0-579878f7305c", "Magic", ""],
    "MBBahvahnter":["EderBahvahnter", "EderBahvahnter", "2c6778c1-ad8c-55aa-ae30-75087164f938", "EderBahvahnter", ""],
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
    "gog":["Hood", "Neighborhood", "ce228892-97ff-42d3-bd3f-2726b4e61f5b", "Guild of Greeters'", ""],
    "gome":["Hood", "Neighborhood", "34ac88e0-14e3-4eb2-87b7-984725875e44", "Guild of Messengers'", ""],
    "international":["Hood", "Neighborhood", "b98bd2b4-3c56-4508-a239-2302e03f01f3", "International's", ""],
    "obd":["Hood", "Neighborhood", "02ab8bcd-2d66-4727-a295-fa6850132aa6", "Obductee's", ""],
    "tjh":["Hood", "Neighborhood", "200be199-f5a0-40a7-b0c9-dad2eb5898e3", "Tereeza's", ""],
    "veelay":["Veelay Tsahvahn", "VeeTsah", "c446d2ed-225f-4492-a9b6-3569d77e462b", "", ""],
    "chiso":["ChisoPreniv", "ChisoPreniv", "0b4f5ad9-d93d-52e3-83e4-9364c2149ae4", "ChisoPreniv", ""],
    "oldmessengerspub":["Messengers' Pub - Ae'gura", "GoMePubNew", "0e1c2ec4-47e0-4231-b258-75d9e138b4b9", "", ""],
    "messengerspub":["Messengers' Pub - Ae'gura", "GoMePubNew", "d002da26-db26-53f1-bdc0-a05a84274d5c", "", ""], #GoMePubNew(9)
    "serene":["Serene", "Serene", "4b70e35f-80c8-463c-b8f5-087e211c112e", "", ""],
    "trebivdil":["Tre'bivdil", "trebivdil", "5b06b39d-27ff-4a80-a00e-40bbdb802e8a", "", ""],
    "vothol":["Vothol Gallery", "Vothol", "303478a8-9e47-4aa7-adc5-985a09033ee8", "", ""],
    "Eder Naybree":["Eder Naybree", "EderNaybree", "1a9f4c27-3603-4252-896a-c460ae3a8dbb", "", ""],
    "Beach":["Eder Naybree", "EderNaybree", "1a9f4c27-3603-4252-896a-c460ae3a8dbb", "", "LinkInPoint-MagicEvent"],
    "Elonin":["Elonin", "Elonin", "81bdc28e-c365-51b3-8c97-59e153db5bf4", "", ""],
    "Fahets Highgarden":["Fahets: Highgarden", "FahetsHighgarden", "744ba6f4-65ce-504f-b623-210ed73d6721", "", ""],
    "Fahets":["Fahets: Highgarden", "FahetsHighgarden", "744ba6f4-65ce-504f-b623-210ed73d6721", "", ""],
    "Highgarden":["Fahets: Highgarden", "FahetsHighgarden", "744ba6f4-65ce-504f-b623-210ed73d6721", "", ""],
    "EderBahvahnter":["EderBahvahnter", "EderBahvahnter", "2c6778c1-ad8c-55aa-ae30-75087164f829", "EderBahvahnter", ""],
    "Memorial":["Memorial Island", "MemorialIsland", "53126f35-8170-401a-8d91-0024886055e9", "", ""],
}
tmp = dict()
for k, v in PublicAgeDict.items():
        tmp.update({k.lower().replace(" ", "").replace("'", "").replace("eder", ""): v})
PublicAgeDict = tmp

# liste des instances disponibles pour moi
# (instance name, file name, guid, user defined name, spawn point)
linkDic = {
    "fh":["Fun House", "Neighborhood", "33a235b1-9fe0-47f0-a73e-6fbd0044717a", "The", "LinkInPointBevinBalcony"],
}
