
from Plasma import *
import datetime
import os
import errno

from PlasmaVaultConstants import *


"""
List of markers games (2025-12-05)
--------------------------------
sendme 114361: Lauritz's Tent Marker Game (09/27/14)
sendme 146301: Minkata Cave 1 (09/27/14)
sendme 153232: Minkata Kiva 2 (09/27/14)
sendme 158311: Minkata Kiva 3 (09/27/14)
sendme 159767: Minkata Kiva 4 (09/27/14)
sendme 161115: Minkata Cave 5 (09/27/14)
sendme 171345: Magicgame4 (09/27/14)
sendme 202990: Meet the Rocks (09/28/14)
sendme 228496: Xeniphers Quest 1 (09/28/14)
sendme 228543: Xeniphers Quest 2: Mystery of the Stolen Amulet (starts in Relt (09/28/14)
sendme 228561: Xeniphers Quest 3: The Old City Clock (09/28/14)
sendme 228629: BRIDGE TO BALCONY by Zesty of Xeniphers (09/28/14)
sendme 253459: Pegasus (09/28/14)
sendme 253532: Jack O' Lantern (09/28/14)
sendme 253552: Be Mine, Valentine (09/28/14)
sendme 253691: Dove of Peace (09/28/14)
sendme 253708: Mermaid, Merman (09/28/14)
sendme 369406: MINKATA: The Ultimate Route (09/30/14)
sendme 430904: INTERNATIONAL/WIZARD HOOD Cloth Numbers (10/02/14)
sendme 477912: Horse With No Name (10/03/14)
sendme 505294: Tent to Musium  (10/03/14)
sendme 512278: TCB The Scar's Minkata Marker Game (10/04/14)
sendme 542422: The Gambit (10/04/14)
sendme 727513: Soccer Ball (10/10/14)
sendme 905066: enders' Holo Minkata (10/17/14)
sendme 906835: Lauritz's Railing Marker Game (10/17/14)
sendme 945583: Watashi's Tent  (10/19/14)
sendme 948910: ZANDI STUCK IN MUD - Start City Sign (10/19/14)
sendme 949347: Treasure Hunt - City Map/ Kadish/ Eder Gira (10/19/14)
sendme 1024184: How to become a Monument - dedicated to Isobel (10/23/14)
sendme 1106151: Minkata Cheats - Kivas 1-5 & Goodies (10/27/14)
sendme 1117606: Tokotah Stalagmite (10/27/14)
sendme 1170561: Library Lower Level (10/31/14)
sendme 1285889: Art's Ancient Museum game (11/07/14)
sendme 1310099: Kadish Underfloors Guide    (11/09/14)
sendme 1561787: D'ni Elites (11/27/14)
sendme 1598458: Kirel's High Points (11/29/14)
sendme 1607622: Ahnonay's 3 minute return to Relto (11/30/14)
sendme 1612776: Christmas Countdown Game (11/30/14)
sendme 1669656: Bahro Stone Marker Quest - 14 Total (12/05/14)
sendme 1672176: Art's Foyer lamp To Ferry (12/05/14)
sendme 1742920: Art & Billie's  Er'cana Mixer & View (12/10/14)
sendme 1749761: Er'cana Marker past the Gorge (12/11/14)
sendme 1770073: D'ni Xmas Tehrpahrah (12/13/14)
sendme 1860673: Art's Jacksn Bevin Throne (12/21/14)
sendme 1890902: Aegura 2015 quest (12/23/14)
sendme 1892150: URU LIVE (city) (12/23/14)
sendme 1920074: Scrambled Must play in Cavern Events hood  (12/26/14)
sendme 1925811: Art's From Bridge to Shore Caves (library route) (12/26/14)
sendme 1954337: Art's Kemo-Scenic, Bugs and Door (12/28/14)
sendme 1981522: Xeniphers Quest 4: Hidden Jewels (12/29/14)
sendme 1985696: Art & Billie's Bridge With a Twist (12/29/14)
sendme 2076578: D'ni Subjects (01/04/15)
sendme 2121338: K'VEER LAGGER (01/07/15)
sendme 2123834: ART'S K'VEER WINDOW & MORE (01/08/15)
sendme 2132239: _Hadamard's Marker Hood (01/08/15)
sendme 2132323: _Hadamard's Marker Game Part 2 Teledahn (01/08/15)
sendme 2133386: _Hadamard's Marker Game Part 3 Gahreesen (01/08/15)
sendme 2133481: _Hadamard's Marker Game Part 4 Kadish Tolesa (01/08/15)
sendme 2134207: _Hadamard's Marker Game Part 5 Eder... (Beta) (01/08/15)
sendme 2137110: D'ni Ports (01/09/15)
sendme 2141914: _Hadamard's Marker Riltagamin (01/09/15)
sendme 2143180: _Hadamard's Marker bevin,kirel,aegura,the watcher's pub,rezeero (01/09/15)
sendme 2145860: Do Not Download This (01/09/15)
sendme 2173961: Relto Sparkies  Riding (01/11/15)
sendme 2181246: Kadish Purple Sea (01/11/15)
sendme 2189761: Art's Teledahn Inn (01/12/15)
sendme 2195841: Hide and Marker?  (01/13/15)
sendme 2216878: Tokotah - Kahlo Express (01/14/15)
sendme 2341834: Art's Teledahn 2nd floor to Barricade (01/25/15)
sendme 2378818: teledahn drawbridge to sea vista (01/28/15)
sendme 2394899: 5 years of URU (city) (01/29/15)
sendme 2401978: enders' Minkata flag to 3125 flag (01/30/15)
sendme 2402322: Watcher's Pub Secret Rooms (01/30/15)
sendme 2548110: Teledahn Stump (02/10/15)
sendme 2560094: Eder Delin's & Tsogal's Hood Cloth Numbers (02/11/15)
sendme 2630615: CITY TENT by Zesty of Xeniphers (02/16/15)
sendme 2668028: kadish pagoda torture (02/19/15)
sendme 2683476: Teledahn Hut (02/21/15)
sendme 2691952: Hall of Kings (Ae'gura Heights 1) (02/21/15)
sendme 2691986: The Greater Library (City's Belt) (02/21/15)
sendme 2691988: The Tokotah Side (City's Belt) (02/21/15)
sendme 2691989: The New Spine (Ae'gura Lakefront) (02/21/15)
sendme 2691990: The Heights (City's Belt) (02/21/15)
sendme 2691991: The Floating Sculpture (Delin) (02/21/15)
sendme 2691992: Delin Fountain Area (02/21/15)
sendme 2691994: The Neverending Path (Delin) (02/21/15)
sendme 2691996: Terminal Front (Er'cana Canyon) (02/21/15)
sendme 2691997: The Silos (Er'cana Factory) (02/21/15)
sendme 2691998: Stones & Wheel (Er'cana Factory) (02/21/15)
sendme 2691999: Spiral & Ovens (Er'cana Factory) (02/21/15)
sendme 2692004: Spiralling Around the Seed (Neighborhood) (02/21/15)
sendme 2692005: The Clock Square (Neighborhood) (02/21/15)
sendme 2692006: Back in The Watcher's (The Watcher's Pub) (02/21/15)
sendme 2692007: The Watcher's Pub (02/21/15)
sendme 2692010: The Bahroglyphs (Kemo) (02/21/15)
sendme 2692011: The Far Reaches (Kemo) (02/21/15)
sendme 2692013: Puffers, Water Lilies, & Kemos (Kemo) (02/21/15)
sendme 2692014: The Brain Trees (Kemo) (02/21/15)
sendme 2692015: The Wooden Area (Kemo) (02/21/15)
sendme 2692016: The Fountain Plaza (Kemo) (02/21/15)
sendme 2692039: The Sutherland Point (Ae'gura Heights 4) (02/21/15)
sendme 2692040: Courtyard Heights (Ae'gura Heights 7) (02/21/15)
sendme 2692041: T-Junction Cave (Ae'gura Heights 3) (02/21/15)
sendme 2692042: Ferry Terminal (Ae'gura Lakefront) (02/21/15)
sendme 2692043: La jolie's Hall of Kings (Ae'gura Heights 5) (02/21/15)
sendme 2692044: The Forgotten Cave (Ae'gura Lakefront) (02/21/15)
sendme 2692045: Mist Lake Splendor (Kadish) (02/21/15)
sendme 2692046: Clearing Heights (Kadish) (02/21/15)
sendme 2692047: The Shore of Mist (Kadish) (02/21/15)
sendme 2692048: The Broken Arches (Kadish) (02/21/15)
sendme 2692049: The Connections (Kadish) (02/21/15)
sendme 2692050: Poetic Skydiving (Kadish) (02/21/15)
sendme 2692051: The Swirls (Kadish) (02/21/15)
sendme 2692052: The Riches (Kadish) (02/21/15)
sendme 2692054: Cracking the Vault (Kadish) (02/21/15)
sendme 2692081: Kadish Pillars (02/21/15)
sendme 2692083: Great Zero Once More (02/21/15)
sendme 2692095: Great Zero Again (02/21/15)
sendme 2692097: Archview Descent (Ae'gura Lakefront) (02/21/15)
sendme 2692103: Spelunking in City (Ae'gura Heights 2) (02/21/15)
sendme 2692104: The Sunken Ships (Ae'gura Lakefront) (02/21/15)
sendme 2692106: Docks Xpressway (Ae'gura Lakefront) (02/21/15)
sendme 2692107: The Bahro Stone Cave (Ae'gura Lakefront) (02/21/15)
sendme 2692151: Kadish Great Elevator (02/21/15)
sendme 2692152: Under the Clouds (Kadish) (02/21/15)
sendme 2692153: Underneath Kadish Forest (02/21/15)
sendme 2692166: Forest Extraordinaire (Kadish) (02/21/15)
sendme 2692167: Around the Chasm (Kadish) (02/21/15)
sendme 2692169: The Great Fall (Kadish) (02/21/15)
sendme 2692170: The Canopy (Kadish) (02/21/15)
sendme 2692171: The Deathly Marshes (Kadish) (02/21/15)
sendme 2692172: The Sky Route (Kadish) (02/21/15)
sendme 2692173: The Dais (Kadish) (02/21/15)
sendme 2692174: The Suspended Moons (Kadish) (02/21/15)
sendme 2692175: The Pellets (Er'cana Factory) (02/21/15)
sendme 2692179: Exploring Ahnonay (02/21/15)
sendme 2692180: The Gloomy Maintenance (Ahnonay) (02/21/15)
sendme 2692181: Ahnonay Space Landing (CQ) (02/21/15)
sendme 2692182: A Ghost in Space (Ahnonay) (CQ) (02/21/15)
sendme 2692183: The Terrose Trees (Ahnonay) (02/21/15)
sendme 2692184: Underwater Ahnonay (02/21/15)
sendme 2692185: 1st Sphere Xit (Ahnonay) (02/21/15)
sendme 2692203: Under Island (Ahnonay) (02/21/15)
sendme 2692208: Some Levitation (Ahnonay) (02/21/15)
sendme 2692209: The Cathedral (Ahnonay Cathedral) (02/21/15)
sendme 2692210: Under Tsogal's Sun (02/21/15)
sendme 2692211: The Surrounding Valley (Tsogal) (02/21/15)
sendme 2692222: Third Time's a Charm (Relto) (02/21/15)
sendme 2692223: Relto Revisited (02/21/15)
sendme 2692224: Annabelle's Relto (02/21/15)
sendme 2692225: A Touch of Yellow (Gahreesen) (02/21/15)
sendme 2692226: Gahreesen Prison Area (02/21/15)
sendme 2692227: The Definitive Kahlo (02/21/15)
sendme 2692228: Museum Hardcore (02/21/15)
sendme 2692229: Gear & Dark Attic (Gahreesen) (02/21/15)
sendme 2692230: Kirel Auditorium (02/21/15)
sendme 2692232: Kirel Light Garden (02/21/15)
sendme 2692233: Reaching the Seed (Kirel) (02/21/15)
sendme 2692234: Kirel Heights (02/21/15)
sendme 2692236: The Kirel Neighborhood (02/21/15)
sendme 2692240: Splendid K'veer (02/21/15)
sendme 2692241: K'veer Attic (02/21/15)
sendme 2692243: The Rings (Gahreesen Subworld) (02/21/15)
sendme 2692244: New Rings (Gahreesen Subworld) (02/21/15)
sendme 2692246: More Rings (Gahreesen Subworld) (02/21/15)
sendme 2692247: Platform Launching (Gahreesen Subworld) (02/21/15)
sendme 2692248: Into Fortress' Darkness (Gahreesen) (02/21/15)
sendme 2692249: The Generators (Gahreesen) (02/21/15)
sendme 2692250: KI Gahreesen (02/21/15)
sendme 2692251: 15 Gems (Gahreesen) (02/21/15)
sendme 2692253: The Outdoors (Gahreesen) (02/21/15)
sendme 2692270: Delin Garden (02/21/15)
sendme 2692271: Delin Journey Door (02/21/15)
sendme 2692273: Swampy Heights (Teledahn) (02/21/15)
sendme 2692274: Railings Over Swamp (Teledahn) (02/21/15)
sendme 2692275: The Perils of Teledahn (02/21/15)
sendme 2692276: The Storage Room (teledahn) (02/21/15)
sendme 2692277: Seaside Teledahn (02/21/15)
sendme 2692278: The Docking Area (Teledahn) (02/21/15)
sendme 2692279: Canyon Exploration (Er'cana Canyon) (02/21/15)
sendme 2692280: The Mill (Er'cana Factory) (02/21/15)
sendme 2692281: Factory Railings (Er'cana Factory) (02/21/15)
sendme 2692282: The Water Ends (Er'cana Factory) (02/21/15)
sendme 2692283: The Canyon Forks (Ae'gura Lakefront) (02/21/15)
sendme 2692284: The Lakefront (City's Belt) (02/21/15)
sendme 2692285: Tokotah Tent (02/21/15)
sendme 2692286: Tokotah Courtyard (02/21/15)
sendme 2692287: Baskets, Bones, & Caves (Gira) (02/21/15)
sendme 2692288: Journey in Gira (02/21/15)
sendme 2692289: The Lava Flow (Gira) (02/21/15)
sendme 2692290: The Water Pool (Gira) (02/21/15)
sendme 2692291: Desertic Flora (Gira) (02/21/15)
sendme 2692292: The Accesses (Gira) (02/21/15)
sendme 2692293: Lower Gira Exploration (02/21/15)
sendme 2692294: Waterfalls Views (Gira) (02/21/15)
sendme 2692300: Railways & Terminal (Er'cana Canyon) (02/21/15)
sendme 2692301: Grandiose Path (2 of 4) (Er'cana) (02/21/15)
sendme 2692302: Grandiose Path (3 of 4) (Er'cana) (02/21/15)
sendme 2692303: Grandiose Path (4 of 4) (Er'cana) (02/21/15)
sendme 2692304: Upper Vistas (Er'cana Factory) (02/21/15)
sendme 2692305: The Broken Link (Er'cana Factory) (02/21/15)
sendme 2692306: Grandiose Path (1 of 4) (Er'cana) (02/21/15)
sendme 2692307: Palace Surroundings (Ae'gura Heights 6) (02/21/15)
sendme 2692308: The Strip Mall (Ae'gura Heights 9) (02/21/15)
sendme 2692310: Arch Vistas (Ae'gura Heights 8) (02/21/15)
sendme 2692311: Ae'gura By-the-Lake (Ae'gura Lakefront) (02/21/15)
sendme 2692312: Docks Connection (Ae'gura Lakefront) (02/21/15)
sendme 2692313: The Paths to Docks (Ae'gura Lakefront) (02/21/15)
sendme 2692314: The Gallery (Ae'gura Lakefront) (02/21/15)
sendme 2692315: Around the Hut (Teledahn) (02/21/15)
sendme 2692316: The Lagoon (Teledahn) (02/21/15)
sendme 2692317: The Stump Descent (Teledahn) (02/21/15)
sendme 2692319: The Spores (Teledahn) (02/21/15)
sendme 2692320: Reaching the Sky (Teledahn) (CQ) (02/21/15)
sendme 2692321: The Vaults (Kadish) (02/21/15)
sendme 2692322: The Everlasting Rain (Phil's) (02/21/15)
sendme 2692323: Stories Have Been Told (Cleft) (02/21/15)
sendme 2692324: Cleft Sunny-Side Up (02/21/15)
sendme 2692326: A Fissure and Some Teeth (Cleft) (02/21/15)
sendme 2692332: Maintainers' Wall (Gahreesen) (02/21/15)
sendme 2692333: The Great Zero (02/21/15)
sendme 2692335: Tanks & Pipes (Er'cana Factory) (02/21/15)
sendme 2692336: The Gems (Ae'gura Lakefront) (02/21/15)
sendme 2692339: Docks Magnificent (Ae'gura Lakefront) (02/21/15)
sendme 2692340: Library Hallway (02/21/15)
sendme 2692341: Library Basement (02/21/15)
sendme 2692342: Ae'gura Lakeshore (02/21/15)
sendme 2692343: Library Courtyard (02/21/15)
sendme 2692344: Library Cliff (02/21/15)
sendme 2692346: The Light Garden (Neighborhood) (02/21/15)
sendme 2692347: The Main Plaza (Neighborhood) (02/21/15)
sendme 2692348: Neighborhood Heights (02/21/15)
sendme 2692350: Gahreesen Entrance Area (02/21/15)
sendme 2692351: Purple in Darkness (Gahreesen) (02/21/15)
sendme 2692353: Paths of Darkness (Gahreesen) (02/21/15)
sendme 2692354: The Dark Corners (Gahreesen) (02/21/15)
sendme 2692355: The Cartographers' Pub (02/21/15)
sendme 2692356: The Messengers' Pub (02/21/15)
sendme 2692357: The Greeters' Pub (02/21/15)
sendme 2692358: The Writers' Pub (02/21/15)
sendme 2692359: The Maintainers' Pub (02/21/15)
sendme 2692361: The Amazing Maze (Neighborhood) (02/21/15)
sendme 2692362: The Community Room (Neighborhood) (02/21/15)
sendme 2693154: Annabelle's Reaching Dusty (Minkata) (02/22/15)
sendme 2694451: The Unachieved Project (Kadish) (02/22/15)
sendme 2706501: Climbing Er'cana (02/22/15)
sendme 2733375: Kadish Spider eggs. (02/25/15)
sendme 2904883: Terokh Jeruth's Competition Marker Game (03/12/15)
sendme 3071421: WATCHER'S: Secret Rooms by Zesty of Xeniphers (03/29/15)
sendme 3080013: Easter Marker Hunt (03/30/15)
sendme 3127780: Super Sleuth 1 - Relto - (04/05/15)
sendme 3188218: Super Sleuth 2 - Relto -- (04/12/15)
sendme 3205258: Super Sleuth 4 Graduation Day - (Relto) ---- (04/14/15)
sendme 3327082: Super Sleuth 3 - Relto --- (04/29/15)
sendme 3383155: KIREL: Route 1 by Zesty of Xeniphers (05/06/15)
sendme 3396694: Hood Quest Part 3  (05/08/15)
sendme 3505101: enders' Minkata Marker Game (05/20/15)
sendme 3553602: enders' Minkata kiva 2 &  kiva 5 (05/25/15)
sendme 3557071: KIQuest! (05/25/15)
sendme 4054469: Relto Rock Jump (07/25/15)
sendme 4199687: scylax's Easier Ae'gura Plaza Tent Climb (08/11/15)
sendme 4298108: Bridge to strip mall direct (08/22/15)
sendme 4483982: MEMORY LANE - start Ae'gura (09/13/15)
sendme 4561496: Ahnonay 4th Maintenance (09/22/15)
sendme 4698983: Happy Thanksgiving (10/10/15)
sendme 4741859: TENT TO MUSEUM by Zesty of Xeniphers (10/16/15)
sendme 4909579: Minkata Kiva 1 Quest (11/04/15)
sendme 4909785: Minkata Kiva 2 Quest (11/04/15)
sendme 4910057: Minkata Kiva 3 Quest (11/04/15)
sendme 4910161: Minkata Kiva 4 Quest (11/04/15)
sendme 4910300: Minkata Kiva 5 Quest (11/04/15)
sendme 4915990: WRITER'S: Secret Rooms by Zesty of Xeniphers (11/05/15)
sendme 5007676: ER'CANA: Top to Turbine (11/16/15)
sendme 5008534: GOG Hood's Eder Tsogal Cloth Numbers (11/16/15)
"""
# Dictionnaire des quetes de MB:
dicQuests = {
    "114361":["Lauritz's Tent Marker Game", "(09/27/14)"], 
    "146301":["Minkata Cave 1", "(09/27/14)"], 
    "153232":["Minkata Kiva 2", "(09/27/14)"], 
    "158311":["Minkata Kiva 3", "(09/27/14)"], 
    "159767":["Minkata Kiva 4", "(09/27/14)"], 
    "161115":["Minkata Cave 5", "(09/27/14)"], 
    "171345":["Magicgame4", "(09/27/14)"], 
    "202990":["Meet the Rocks", "(09/28/14)"], 
    "228496":["Xeniphers Quest 1", "(09/28/14)"], 
    "228543":["Xeniphers Quest 2:Mystery of the Stolen Amulet (starts in Relt", "(09/28/14)"], 
    "228561":["Xeniphers Quest 3:The Old City Clock", "(09/28/14)"], 
    "228629":["BRIDGE TO BALCONY by Zesty of Xeniphers", "(09/28/14)"], 
    "253459":["Pegasus", "(09/28/14)"], 
    "253532":["Jack O' Lantern", "(09/28/14)"], 
    "253552":["Be Mine, Valentine", "(09/28/14)"], 
    "253691":["Dove of Peace", "(09/28/14)"], 
    "253708":["Mermaid, Merman", "(09/28/14)"], 
    "369406":["MINKATA:The Ultimate Route", "(09/30/14)"], 
    "430904":["INTERNATIONAL/WIZARD HOOD Cloth Numbers", "(10/02/14)"], 
    "477912":["Horse With No Name", "(10/03/14)"], 
    "505294":["Tent to Musium ", "(10/03/14)"], 
    "512278":["TCB The Scar's Minkata Marker Game", "(10/04/14)"], 
    "542422":["The Gambit", "(10/04/14)"], 
    "727513":["Soccer Ball", "(10/10/14)"], 
    "905066":["enders' Holo Minkata", "(10/17/14)"], 
    "906835":["Lauritz's Railing Marker Game", "(10/17/14)"], 
    "945583":["Watashi's Tent ", "(10/19/14)"], 
    "948910":["ZANDI STUCK IN MUD - Start City Sign", "(10/19/14)"], 
    "949347":["Treasure Hunt - City Map/ Kadish/ Eder Gira", "(10/19/14)"], 
    "1024184":["How to become a Monument - dedicated to Isobel", "(10/23/14)"], 
    "1106151":["Minkata Cheats - Kivas 1-5 & Goodies", "(10/27/14)"], 
    "1117606":["Tokotah Stalagmite", "(10/27/14)"], 
    "1170561":["Library Lower Level", "(10/31/14)"], 
    "1285889":["Art's Ancient Museum game", "(11/07/14)"], 
    "1310099":["Kadish Underfloors Guide   ", "(11/09/14)"], 
    "1561787":["D'ni Elites", "(11/27/14)"], 
    "1598458":["Kirel's High Points", "(11/29/14)"], 
    "1607622":["Ahnonay's 3 minute return to Relto", "(11/30/14)"], 
    "1612776":["Christmas Countdown Game", "(11/30/14)"], 
    "1669656":["Bahro Stone Marker Quest - 14 Total", "(12/05/14)"], 
    "1672176":["Art's Foyer lamp To Ferry", "(12/05/14)"], 
    "1742920":["Art & Billie's  Er'cana Mixer & View", "(12/10/14)"], 
    "1749761":["Er'cana Marker past the Gorge", "(12/11/14)"], 
    "1770073":["D'ni Xmas Tehrpahrah", "(12/13/14)"], 
    "1860673":["Art's Jacksn Bevin Throne", "(12/21/14)"], 
    "1890902":["Aegura 2015 quest", "(12/23/14)"], 
    "1892150":["URU LIVE (city)", "(12/23/14)"], 
    "1920074":["Scrambled Must play in Cavern Events hood ", "(12/26/14)"], 
    "1925811":["Art's From Bridge to Shore Caves (library route)", "(12/26/14)"], 
    "1954337":["Art's Kemo-Scenic, Bugs and Door", "(12/28/14)"], 
    "1981522":["Xeniphers Quest 4:Hidden Jewels", "(12/29/14)"], 
    "1985696":["Art & Billie's Bridge With a Twist", "(12/29/14)"], 
    "2076578":["D'ni Subjects", "(01/04/15)"], 
    "2121338":["K'VEER LAGGER", "(01/07/15)"], 
    "2123834":["ART'S K'VEER WINDOW & MORE", "(01/08/15)"], 
    "2132239":["_Hadamard's Marker Hood", "(01/08/15)"], 
    "2132323":["_Hadamard's Marker Game Part 2 Teledahn", "(01/08/15)"], 
    "2133386":["_Hadamard's Marker Game Part 3 Gahreesen", "(01/08/15)"], 
    "2133481":["_Hadamard's Marker Game Part 4 Kadish Tolesa", "(01/08/15)"], 
    "2134207":["_Hadamard's Marker Game Part 5 Eder... (Beta)", "(01/08/15)"], 
    "2137110":["D'ni Ports", "(01/09/15)"], 
    "2141914":["_Hadamard's Marker Riltagamin", "(01/09/15)"], 
    "2143180":["_Hadamard's Marker bevin,kirel,aegura,the watcher's pub,rezeero", "(01/09/15)"], 
    "2145860":["Do Not Download This", "(01/09/15)"], 
    "2173961":["Relto Sparkies  Riding", "(01/11/15)"], 
    "2181246":["Kadish Purple Sea", "(01/11/15)"], 
    "2189761":["Art's Teledahn Inn", "(01/12/15)"], 
    "2195841":["Hide and Marker? ", "(01/13/15)"], 
    "2216878":["Tokotah - Kahlo Express", "(01/14/15)"], 
    "2341834":["Art's Teledahn 2nd floor to Barricade", "(01/25/15)"], 
    "2378818":["teledahn drawbridge to sea vista", "(01/28/15)"], 
    "2394899":["5 years of URU (city)", "(01/29/15)"], 
    "2401978":["enders' Minkata flag to 3125 flag", "(01/30/15)"], 
    "2402322":["Watcher's Pub Secret Rooms", "(01/30/15)"], 
    "2548110":["Teledahn Stump", "(02/10/15)"], 
    "2560094":["Eder Delin's & Tsogal's Hood Cloth Numbers", "(02/11/15)"], 
    "2630615":["CITY TENT by Zesty of Xeniphers", "(02/16/15)"], 
    "2668028":["kadish pagoda torture", "(02/19/15)"], 
    "2683476":["Teledahn Hut", "(02/21/15)"], 
    "2691952":["Hall of Kings (Ae'gura Heights 1)", "(02/21/15)"], 
    "2691986":["The Greater Library (City's Belt)", "(02/21/15)"], 
    "2691988":["The Tokotah Side (City's Belt)", "(02/21/15)"], 
    "2691989":["The New Spine (Ae'gura Lakefront)", "(02/21/15)"], 
    "2691990":["The Heights (City's Belt)", "(02/21/15)"], 
    "2691991":["The Floating Sculpture (Delin)", "(02/21/15)"], 
    "2691992":["Delin Fountain Area", "(02/21/15)"], 
    "2691994":["The Neverending Path (Delin)", "(02/21/15)"], 
    "2691996":["Terminal Front (Er'cana Canyon)", "(02/21/15)"], 
    "2691997":["The Silos (Er'cana Factory)", "(02/21/15)"], 
    "2691998":["Stones & Wheel (Er'cana Factory)", "(02/21/15)"], 
    "2691999":["Spiral & Ovens (Er'cana Factory)", "(02/21/15)"], 
    "2692004":["Spiralling Around the Seed (Neighborhood)", "(02/21/15)"], 
    "2692005":["The Clock Square (Neighborhood)", "(02/21/15)"], 
    "2692006":["Back in The Watcher's (The Watcher's Pub)", "(02/21/15)"], 
    "2692007":["The Watcher's Pub", "(02/21/15)"], 
    "2692010":["The Bahroglyphs (Kemo)", "(02/21/15)"], 
    "2692011":["The Far Reaches (Kemo)", "(02/21/15)"], 
    "2692013":["Puffers, Water Lilies, & Kemos (Kemo)", "(02/21/15)"], 
    "2692014":["The Brain Trees (Kemo)", "(02/21/15)"], 
    "2692015":["The Wooden Area (Kemo)", "(02/21/15)"], 
    "2692016":["The Fountain Plaza (Kemo)", "(02/21/15)"], 
    "2692039":["The Sutherland Point (Ae'gura Heights 4)", "(02/21/15)"], 
    "2692040":["Courtyard Heights (Ae'gura Heights 7)", "(02/21/15)"], 
    "2692041":["T-Junction Cave (Ae'gura Heights 3)", "(02/21/15)"], 
    "2692042":["Ferry Terminal (Ae'gura Lakefront)", "(02/21/15)"], 
    "2692043":["La jolie's Hall of Kings (Ae'gura Heights 5)", "(02/21/15)"], 
    "2692044":["The Forgotten Cave (Ae'gura Lakefront)", "(02/21/15)"], 
    "2692045":["Mist Lake Splendor (Kadish)", "(02/21/15)"], 
    "2692046":["Clearing Heights (Kadish)", "(02/21/15)"], 
    "2692047":["The Shore of Mist (Kadish)", "(02/21/15)"], 
    "2692048":["The Broken Arches (Kadish)", "(02/21/15)"], 
    "2692049":["The Connections (Kadish)", "(02/21/15)"], 
    "2692050":["Poetic Skydiving (Kadish)", "(02/21/15)"], 
    "2692051":["The Swirls (Kadish)", "(02/21/15)"], 
    "2692052":["The Riches (Kadish)", "(02/21/15)"], 
    "2692054":["Cracking the Vault (Kadish)", "(02/21/15)"], 
    "2692081":["Kadish Pillars", "(02/21/15)"], 
    "2692083":["Great Zero Once More", "(02/21/15)"], 
    "2692095":["Great Zero Again", "(02/21/15)"], 
    "2692097":["Archview Descent (Ae'gura Lakefront)", "(02/21/15)"], 
    "2692103":["Spelunking in City (Ae'gura Heights 2)", "(02/21/15)"], 
    "2692104":["The Sunken Ships (Ae'gura Lakefront)", "(02/21/15)"], 
    "2692106":["Docks Xpressway (Ae'gura Lakefront)", "(02/21/15)"], 
    "2692107":["The Bahro Stone Cave (Ae'gura Lakefront)", "(02/21/15)"], 
    "2692151":["Kadish Great Elevator", "(02/21/15)"], 
    "2692152":["Under the Clouds (Kadish)", "(02/21/15)"], 
    "2692153":["Underneath Kadish Forest", "(02/21/15)"], 
    "2692166":["Forest Extraordinaire (Kadish)", "(02/21/15)"], 
    "2692167":["Around the Chasm (Kadish)", "(02/21/15)"], 
    "2692169":["The Great Fall (Kadish)", "(02/21/15)"], 
    "2692170":["The Canopy (Kadish)", "(02/21/15)"], 
    "2692171":["The Deathly Marshes (Kadish)", "(02/21/15)"], 
    "2692172":["The Sky Route (Kadish)", "(02/21/15)"], 
    "2692173":["The Dais (Kadish)", "(02/21/15)"], 
    "2692174":["The Suspended Moons (Kadish)", "(02/21/15)"], 
    "2692175":["The Pellets (Er'cana Factory)", "(02/21/15)"], 
    "2692179":["Exploring Ahnonay", "(02/21/15)"], 
    "2692180":["The Gloomy Maintenance (Ahnonay)", "(02/21/15)"], 
    "2692181":["Ahnonay Space Landing (CQ)", "(02/21/15)"], 
    "2692182":["A Ghost in Space (Ahnonay) (CQ)", "(02/21/15)"], 
    "2692183":["The Terrose Trees (Ahnonay)", "(02/21/15)"], 
    "2692184":["Underwater Ahnonay", "(02/21/15)"], 
    "2692185":["1st Sphere Xit (Ahnonay)", "(02/21/15)"], 
    "2692203":["Under Island (Ahnonay)", "(02/21/15)"], 
    "2692208":["Some Levitation (Ahnonay)", "(02/21/15)"], 
    "2692209":["The Cathedral (Ahnonay Cathedral)", "(02/21/15)"], 
    "2692210":["Under Tsogal's Sun", "(02/21/15)"], 
    "2692211":["The Surrounding Valley (Tsogal)", "(02/21/15)"], 
    "2692222":["Third Time's a Charm (Relto)", "(02/21/15)"], 
    "2692223":["Relto Revisited", "(02/21/15)"], 
    "2692224":["Annabelle's Relto", "(02/21/15)"], 
    "2692225":["A Touch of Yellow (Gahreesen)", "(02/21/15)"], 
    "2692226":["Gahreesen Prison Area", "(02/21/15)"], 
    "2692227":["The Definitive Kahlo", "(02/21/15)"], 
    "2692228":["Museum Hardcore", "(02/21/15)"], 
    "2692229":["Gear & Dark Attic (Gahreesen)", "(02/21/15)"], 
    "2692230":["Kirel Auditorium", "(02/21/15)"], 
    "2692232":["Kirel Light Garden", "(02/21/15)"], 
    "2692233":["Reaching the Seed (Kirel)", "(02/21/15)"], 
    "2692234":["Kirel Heights", "(02/21/15)"], 
    "2692236":["The Kirel Neighborhood", "(02/21/15)"], 
    "2692240":["Splendid K'veer", "(02/21/15)"], 
    "2692241":["K'veer Attic", "(02/21/15)"], 
    "2692243":["The Rings (Gahreesen Subworld)", "(02/21/15)"], 
    "2692244":["New Rings (Gahreesen Subworld)", "(02/21/15)"], 
    "2692246":["More Rings (Gahreesen Subworld)", "(02/21/15)"], 
    "2692247":["Platform Launching (Gahreesen Subworld)", "(02/21/15)"], 
    "2692248":["Into Fortress' Darkness (Gahreesen)", "(02/21/15)"], 
    "2692249":["The Generators (Gahreesen)", "(02/21/15)"], 
    "2692250":["KI Gahreesen", "(02/21/15)"], 
    "2692251":["15 Gems (Gahreesen)", "(02/21/15)"], 
    "2692253":["The Outdoors (Gahreesen)", "(02/21/15)"], 
    "2692270":["Delin Garden", "(02/21/15)"], 
    "2692271":["Delin Journey Door", "(02/21/15)"], 
    "2692273":["Swampy Heights (Teledahn)", "(02/21/15)"], 
    "2692274":["Railings Over Swamp (Teledahn)", "(02/21/15)"], 
    "2692275":["The Perils of Teledahn", "(02/21/15)"], 
    "2692276":["The Storage Room (teledahn)", "(02/21/15)"], 
    "2692277":["Seaside Teledahn", "(02/21/15)"], 
    "2692278":["The Docking Area (Teledahn)", "(02/21/15)"], 
    "2692279":["Canyon Exploration (Er'cana Canyon)", "(02/21/15)"], 
    "2692280":["The Mill (Er'cana Factory)", "(02/21/15)"], 
    "2692281":["Factory Railings (Er'cana Factory)", "(02/21/15)"], 
    "2692282":["The Water Ends (Er'cana Factory)", "(02/21/15)"], 
    "2692283":["The Canyon Forks (Ae'gura Lakefront)", "(02/21/15)"], 
    "2692284":["The Lakefront (City's Belt)", "(02/21/15)"], 
    "2692285":["Tokotah Tent", "(02/21/15)"], 
    "2692286":["Tokotah Courtyard", "(02/21/15)"], 
    "2692287":["Baskets, Bones, & Caves (Gira)", "(02/21/15)"], 
    "2692288":["Journey in Gira", "(02/21/15)"], 
    "2692289":["The Lava Flow (Gira)", "(02/21/15)"], 
    "2692290":["The Water Pool (Gira)", "(02/21/15)"], 
    "2692291":["Desertic Flora (Gira)", "(02/21/15)"], 
    "2692292":["The Accesses (Gira)", "(02/21/15)"], 
    "2692293":["Lower Gira Exploration", "(02/21/15)"], 
    "2692294":["Waterfalls Views (Gira)", "(02/21/15)"], 
    "2692300":["Railways & Terminal (Er'cana Canyon)", "(02/21/15)"], 
    "2692301":["Grandiose Path (2 of 4) (Er'cana)", "(02/21/15)"], 
    "2692302":["Grandiose Path (3 of 4) (Er'cana)", "(02/21/15)"], 
    "2692303":["Grandiose Path (4 of 4) (Er'cana)", "(02/21/15)"], 
    "2692304":["Upper Vistas (Er'cana Factory)", "(02/21/15)"], 
    "2692305":["The Broken Link (Er'cana Factory)", "(02/21/15)"], 
    "2692306":["Grandiose Path (1 of 4) (Er'cana)", "(02/21/15)"], 
    "2692307":["Palace Surroundings (Ae'gura Heights 6)", "(02/21/15)"], 
    "2692308":["The Strip Mall (Ae'gura Heights 9)", "(02/21/15)"], 
    "2692310":["Arch Vistas (Ae'gura Heights 8)", "(02/21/15)"], 
    "2692311":["Ae'gura By-the-Lake (Ae'gura Lakefront)", "(02/21/15)"], 
    "2692312":["Docks Connection (Ae'gura Lakefront)", "(02/21/15)"], 
    "2692313":["The Paths to Docks (Ae'gura Lakefront)", "(02/21/15)"], 
    "2692314":["The Gallery (Ae'gura Lakefront)", "(02/21/15)"], 
    "2692315":["Around the Hut (Teledahn)", "(02/21/15)"], 
    "2692316":["The Lagoon (Teledahn)", "(02/21/15)"], 
    "2692317":["The Stump Descent (Teledahn)", "(02/21/15)"], 
    "2692319":["The Spores (Teledahn)", "(02/21/15)"], 
    "2692320":["Reaching the Sky (Teledahn) (CQ)", "(02/21/15)"], 
    "2692321":["The Vaults (Kadish)", "(02/21/15)"], 
    "2692322":["The Everlasting Rain (Phil's)", "(02/21/15)"], 
    "2692323":["Stories Have Been Told (Cleft)", "(02/21/15)"], 
    "2692324":["Cleft Sunny-Side Up", "(02/21/15)"], 
    "2692326":["A Fissure and Some Teeth (Cleft)", "(02/21/15)"], 
    "2692332":["Maintainers' Wall (Gahreesen)", "(02/21/15)"], 
    "2692333":["The Great Zero", "(02/21/15)"], 
    "2692335":["Tanks & Pipes (Er'cana Factory)", "(02/21/15)"], 
    "2692336":["The Gems (Ae'gura Lakefront)", "(02/21/15)"], 
    "2692339":["Docks Magnificent (Ae'gura Lakefront)", "(02/21/15)"], 
    "2692340":["Library Hallway", "(02/21/15)"], 
    "2692341":["Library Basement", "(02/21/15)"], 
    "2692342":["Ae'gura Lakeshore", "(02/21/15)"], 
    "2692343":["Library Courtyard", "(02/21/15)"], 
    "2692344":["Library Cliff", "(02/21/15)"], 
    "2692346":["The Light Garden (Neighborhood)", "(02/21/15)"], 
    "2692347":["The Main Plaza (Neighborhood)", "(02/21/15)"], 
    "2692348":["Neighborhood Heights", "(02/21/15)"], 
    "2692350":["Gahreesen Entrance Area", "(02/21/15)"], 
    "2692351":["Purple in Darkness (Gahreesen)", "(02/21/15)"], 
    "2692353":["Paths of Darkness (Gahreesen)", "(02/21/15)"], 
    "2692354":["The Dark Corners (Gahreesen)", "(02/21/15)"], 
    "2692355":["The Cartographers' Pub", "(02/21/15)"], 
    "2692356":["The Messengers' Pub", "(02/21/15)"], 
    "2692357":["The Greeters' Pub", "(02/21/15)"], 
    "2692358":["The Writers' Pub", "(02/21/15)"], 
    "2692359":["The Maintainers' Pub", "(02/21/15)"], 
    "2692361":["The Amazing Maze (Neighborhood)", "(02/21/15)"], 
    "2692362":["The Community Room (Neighborhood)", "(02/21/15)"], 
    "2693154":["Annabelle's Reaching Dusty (Minkata)", "(02/22/15)"], 
    "2694451":["The Unachieved Project (Kadish)", "(02/22/15)"], 
    "2706501":["Climbing Er'cana", "(02/22/15)"], 
    "2733375":["Kadish Spider eggs.", "(02/25/15)"], 
    "2904883":["Terokh Jeruth's Competition Marker Game", "(03/12/15)"], 
    "3071421":["WATCHER'S:Secret Rooms by Zesty of Xeniphers", "(03/29/15)"], 
    "3080013":["Easter Marker Hunt", "(03/30/15)"], 
    "3127780":["Super Sleuth 1 - Relto -", "(04/05/15)"], 
    "3188218":["Super Sleuth 2 - Relto --", "(04/12/15)"], 
    "3205258":["Super Sleuth 4 Graduation Day - (Relto) ----", "(04/14/15)"], 
    "3327082":["Super Sleuth 3 - Relto ---", "(04/29/15)"], 
    "3383155":["KIREL:Route 1 by Zesty of Xeniphers", "(05/06/15)"], 
    "3396694":["Hood Quest Part 3 ", "(05/08/15)"], 
    "3505101":["enders' Minkata Marker Game", "(05/20/15)"], 
    "3553602":["enders' Minkata kiva 2 &  kiva 5", "(05/25/15)"], 
    "3557071":["KIQuest!", "(05/25/15)"], 
    "4054469":["Relto Rock Jump", "(07/25/15)"], 
    "4199687":["scylax's Easier Ae'gura Plaza Tent Climb", "(08/11/15)"], 
    "4298108":["Bridge to strip mall direct", "(08/22/15)"], 
    "4483982":["MEMORY LANE - start Ae'gura", "(09/13/15)"], 
    "4561496":["Ahnonay 4th Maintenance", "(09/22/15)"], 
    "4698983":["Happy Thanksgiving", "(10/10/15)"], 
    "4741859":["TENT TO MUSEUM by Zesty of Xeniphers", "(10/16/15)"], 
    "4909579":["Minkata Kiva 1 Quest", "(11/04/15)"], 
    "4909785":["Minkata Kiva 2 Quest", "(11/04/15)"], 
    "4910057":["Minkata Kiva 3 Quest", "(11/04/15)"], 
    "4910161":["Minkata Kiva 4 Quest", "(11/04/15)"], 
    "4910300":["Minkata Kiva 5 Quest", "(11/04/15)"], 
    "4915990":["WRITER'S:Secret Rooms by Zesty of Xeniphers", "(11/05/15)"], 
    "5007676":["ER'CANA:Top to Turbine", "(11/16/15)"], 
    "5008534":["GOG Hood's Eder Tsogal Cloth Numbers", "(11/16/15)"], 
}


### Ca ne marche pas, setID ne fonctionne pas
### par contre setGameGuid et setGameName oui
##def GetGameByID(gameID):
##    tempNode = ptVaultMarkerGameNode()
##    tempNode.setID(gameID)
##
##    try:
##        node = ptVault().findNode(tempNode)
##        if node.getType() == PtVaultNodeTypes.kMarkerGameNode:
##            game = node.upcastToMarkerGameNode()
##            return game
##        else:
##            return None
##    except:
##        return None

# Recherche un jeu de marqueur par son Guid
def GetGameByGuid(gameGuid):
    tempNode = ptVaultMarkerGameNode()
    tempNode.setGameGuid(gameGuid)

    try:
        node = ptVault().findNode(tempNode)
        if node.getType() == PtVaultNodeTypes.kMarkerGameNode:
            game = node.upcastToMarkerGameNode()
            print "game found"
            return game
        else:
            print "game not found"
            return None
    except:
        print "error in GetGameByGuid"
        return None

# Recherche un jeu de marqueur par son nom
def GetGameByName(gameName):
    tempNode = ptVaultMarkerGameNode()
    tempNode.setGameName(gameName)

    try:
        node = ptVault().findNode(tempNode)
        if node.getType() == PtVaultNodeTypes.kMarkerGameNode:
            game = node.upcastToMarkerGameNode()
            print "game found"
            return game
        else:
            print "game not found"
            return None
    except:
        print "error in GetGameByGuid"
        return None

# Recherche un jeu de marqueur par son ID dans dicQuests
def GetGameInDic(gameId):
    global dicQuests
    if isinstance(gameId, int):
        key = str(gameId)
    elif isinstance(gameId, str):
        key = gameId
    else:
        return "gameID incorrect"
    
    if key not in dicQuests.keys():
        return "key incorrect"
    
    gameName = dicQuests[key][0]
    gameDate = dicQuests[key][1]
    print "Game : {0} {1} {2}".format(key, gameName, gameDate)
    
    tempNode = ptVaultMarkerGameNode()
    tempNode.setGameName(gameName)

    try:
        node = ptVault().findNode(tempNode)
        if node.getType() == PtVaultNodeTypes.kMarkerGameNode:
            game = node.upcastToMarkerGameNode()
            print "game found"
            print "=> GUID = {0}".format(game.getGameGuid())
            return game
        else:
            print "game not found"
            return None
    except:
        print "error in GetGameByGuid"
        return None

#
#def SendMeAllGamesFromDic():
def AllGamesFromDic():
    player = PtGetLocalPlayer()
    playerId = player.getPlayerID()
    for k, v in dicQuests.iteritems():
        print "Game #{0}: name=\"{1}\", date={2}".format(k, v[0], v[1])
        tempNode = ptVaultMarkerGameNode()
        tempNode.setGameName(v[0])
        node = None
        try:
            node = ptVault().findNode(tempNode)
        except:
            print "Error in ptVault().findNode(tempNode)"
        if node is not None:
            try:
                if node.getType() == PtVaultNodeTypes.kMarkerGameNode:
                    game = node.upcastToMarkerGameNode()
                    print "Game found => GUID = {0}".format(game.getGameGuid())
                    # Envoyer la quete
                    #try:
                    #    game.sendTo(playerId)
                    #except:
                    #    print "Error while sending game"
                    #return game
                else:
                    print "Game not found"
                    #return None
            except:
                print "Error in node.getType(), PtVaultNodeTypes.kMarkerGameNode, node.upcastToMarkerGameNode() or game.getGameGuid()"
        else:
            print "node is None => game not found."
            #return None
    print "END"
    return

#
n = -1
#
#def SendMeGame(n=0):
def NextGame():
    #player = PtGetLocalPlayer()
    #playerId = player.getPlayerID()
    global n
    n = n + 1
    nbGamesInDic = len(dicQuests.keys())
    if n < 0 or n > nbGamesInDic - 1:
        print "END : index out of bounds."
        n = -1
        return
    k = dicQuests.keys()[n]
    v = dicQuests[k]
    print "Game {0} => #{1}: name=\"{2}\", date={3}".format(n, k, v[0], v[1])
    tempNode = ptVaultMarkerGameNode()
    tempNode.setGameName(v[0])
    try:
        node = ptVault().findNode(tempNode)
        if node is None:
            print "Game not found (node is None)"
            return
        if node.getType() == PtVaultNodeTypes.kMarkerGameNode:
            game = node.upcastToMarkerGameNode()
            print "Game found => GUID = {0}".format(game.getGameGuid())
            # Envoyer la quete
            #try:
            #    game.sendTo(playerId)
            #except:
            #    print "Error while sending game"
            #return game
        else:
            print "Game not found (not a marker game)"
            #return None
    except:
        print "Error in SendMeGame"
        #return None
    print "END"
    return


