# -*- coding: utf-8 -*-
from Plasma import *

yeeshaPages = [
    "YeeshaPage1",  # sun and moon
    "YeeshaPage2",  # waterfall
    "YeeshaPage3",  # hut decal / interior rug
    "YeeshaPage4",  # hut roof (swap)
    "YeeshaPage5",  # jumping pinnacles
    "YeeshaPage6",  # dock
    "YeeshaPage7",  # kickable physicals
    "YeeshaPage8",  # Rain
    "YeeshaPage9",  # music player
    "YeeshaPage10", # the tree
    "YeeshaPage11", # second bookcase
    "YeeshaPage12", # imager addition
    "YeeshaPage13", # butterflies
    "YeeshaPage14", # fireplace
    "YeeshaPage15", # bench
    "YeeshaPage16", # firemarbles
    "YeeshaPage17", # lush
    "YeeshaPage18", # clock
    "YeeshaPage19", # birds
    "YeeshaPage20", # calendar/bridge
    "YeeshaPage21", # maple trees
    "YeeshaPage22", # grass
    "YeeshaPage23", # ercana plants
    "YeeshaPage24", # thunderstorm
    "YeeshaPage25", # Bahro poles
    "YeeshaPage26", # VeeTsah Sky
    "YeeshaPage27", # Oceans
    "YeeshaPage28", # Blue Flowers
    "YeeshaPage29", # 
    "YeeshaPage30", # 
    "YeeshaPage31", # 
    "YeeshaPage32", # 
    "YeeshaPage33", # 
    "YeeshaPage34", # 
    "YeeshaPage35", # 
    "YeeshaPage36", # 
    "YeeshaPage37", # 
    "YeeshaPage38", # 
    "YeeshaPage39", # 
    "YeeshaPage40", # 
    "YeeshaPage41", # 
    "YeeshaPage42", # 
    "YeeshaPage43", # 
    "YeeshaPage44", # 
    "YeeshaPage45", # 
    "YeeshaPage46", # 
    "YeeshaPage47", # 
    "YeeshaPage48", # 
    "YeeshaPage49", # 
    "YeeshaPage50"  # 
]

def bugs():
    sdl = PtGetAgeSDL()
    sdl["psnlBugsVis"] = (1,)

def maples(bOn=0):
    sdl = PtGetAgeSDL()
    sdl["YeeshaPage21"] = (bOn,)

# Tree
# Butter
