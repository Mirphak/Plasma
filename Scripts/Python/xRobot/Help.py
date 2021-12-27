# -*- coding: utf-8 -*-

# ** Mir-o-Bot Help files **

update = "2014-05-27"

# -- General Help --
    title = "Mir-o-Bot General Help"
    msg = "Shorah explorer!\n"
    msg += "List of commands available (Remember I'm not MagicBot nor MimiBot):\n"
    msg += "------------------------------------\n\n"
    msg += "help : sends you this text note.\n"
    msg += "help [command name]: PM you a specific help on a command.\n\n"
    msg += "link or meet : links your avatar to Mir-o-Bot's current Age.\n\n"
    msg += "onbot or warp or w : warps your avatar to Mir-o-Bot's current position.\n\n"
    msg += "warp or warp [avatar name] or warp [x] [y] [z] : see onbot, find and rgoto.\n (the avatar name can be incomplete).\n\n"
    msg += "wd : warps your avatar to the default linkin point.\n\n"
    msg += "nopanic : Disables most of the panic zones.\n\n"
    
    msg += " You can save and return to 10 positions in each age with:\n"
    msg += "  save [n] : Save your current position. Where n = 0 to 9\n"
    msg += "  ws [n] : Warps you to your n-th saved position. Where n = 0 to 9\n"
    msg += "  I save them on my disk. You will be able to return to a saved position when you want!\n\n"

    msg += "door [open/close] : opens or closes the bahro door (only in Delin or Tsogal).\n\n"
    
    msg += "drop : Drops some objects.\n\n"
    msg += "clean : Cleans the previously droped objects.\n\n"
    msg += "ring [yellow/blue/red/white] [on/off] : Activates and deactivates a ring of Firemarbles.\n"
    msg += "    Optionally: ring [color] [on] [height] [radius].\n\n"

    # Specifique a city/aegura
    msg += "sp [number]: warps you to a spawn point (number between 0 and 20). Only works in city.\n"
    msg += "    City specific spots:\n"
    msg += "        Ferry Gate       = FG               (= sp 1)\n"
    msg += "        Ferry Roof       = FR               (= sp 2)\n"
    msg += "        Opera House      = OH               (= sp 3)\n"
    msg += "        Tokotah Roof     = TR               (= sp 4)\n"
    msg += "        Kahlo Roof       = KR               (= sp 5)\n"
    msg += "        Library Roof     = LR               (= sp 6)\n"
    msg += "        Palace Roof      = PR               (= sp 7)\n"
    msg += "        Concert Hall     = CH               (= sp 9)\n"
    msg += "        Museum           = MU               \n"
    msg += "        Tokotah Roof Top = DAKOTAH or TRT   \n"
    msg += "        Palace Balconies = PB1, PB2 and PB3.\n\n"
    #msg += "        Great Stairs Roof = GSR (= kahlo pub roof)\n"
    #msg += "        Palace Balcony = PB (= palace roof)\n"
    
    #Linking commands
    msg += "to {city/library/ferry/dakotah/tokotah/concert/palace/kirel/kveer/watcher/greeters/writers.../gog/international} : links YOU to a public age\n"
    msg += "or a Mir-o-Bot age {Ae'gura/Ahnonay Cathedral/Cleft/Relto/Eder Gira/Eder Kemo/Er'cana/Gahreesen/Hood/Kadish/Pellet Cave/Teledahn}.\n"
    msg += "or a Magic age: to {MBCity/MBRelto/MBErcana/MBTeledahn/MBOffice/MBKadish/MBKveer/MBHood/MBDereno/MBRudenna}.\n\n"
    #msg += "linkbotto {fh/fhci/fhde/fhga/fhte/fhka/fhgi/fhcl/mbe/mcl/mre/mkv/mka/scl}: links Mir-o-Bot to the specified Age.\n"
    msg += "linkbotto [age name]: links Mir-o-Bot to the specified Age.\n"
    msg += "   linkbotto fh   = The Fun House\n"
    msg += "   linkbotto fhci = The Fun House - City\n"
    msg += "   linkbotto fhde = Fun House\'s (1) Eder Delin\n"
    msg += "   linkbotto fhga = The Fun House - Gahreesen\n"
    msg += "   linkbotto fhte = The Fun House - Teledahn\n"
    #msg += "   linkbotto fhcl = Fun House\'s Cleft\n"
    msg += "   linkbotto fhka = The Fun House - Kadish Tolesa\n"
    msg += "   linkbotto fhgi = The Fun House - Eder Gira\n"
    msg += "   linkbotto mbe = MagicBot Ercana\n"
    #msg += "   linkbotto mcl = Magic Cleft\n"
    msg += "   linkbotto mre = Magic Relto\n"
    msg += "   linkbotto mkv = Magic Kveer\n"
    msg += "   linkbotto mka = Magic Tolesa\n"
    #msg += "   linkbotto scl = Stone5's Cleft\n\n"
    msg += "   Mir-o-Bot's ages are available too :Ae'gura, Ahnonay, Ahnonay Cathedral, Cleft, Eder Gira, Eder Kemo, Eder Tsogal, Eder Delin, Er'cana, Gahreesen, Hood, Jalak, Kadish, Minkata, Pellet Cave, Relto, Teledahn\n"

    msg += "coord : returns your current position.\n\n"
    msg += "agoto [x] [y] [z] or teleport [x] [y] [z] : disable physics and warps your avatar to an absolute position.\n\n"
    msg += "rgoto [x] [y] [z] or xwarp [x] [y] [z] or warp [x] [y] [z] : disable physics and warps your avatar relative to your current position.\n\n"
    msg += "rot [axis] [angle] : disables physics and rotates your avatar along the specified x, y or z axis, and following the specified angle in degrees.\n\n"
    msg += "turn [angle] : disables physics and rotates your avatar on Z axis relative to your current position.\n\n"
    msg += "float [height]: disables physics and warps your avatar up or down relative to your current position.\n\n"
    msg += "jump [height] or jump [forward] [height]: jump in the air.\n\n"
    msg += "land or normal: enables physics.\n\n"
    msg += "find [object or avatar name]: warps you to the first object or avatar found (use * as any unknown caracters but not only a *), this command is case sensitive.\n\n"
    msg += "list [object name]: shows you the list of object names found (use * as any unknown caracters but not only a *), this command is case sensitive.\n\n"

    #msg += "addcleft : Add a partially invisible Cleft and disable panic links, enjoy!\n\n"

#=============================================================================	
#Animation commands
HelpAnim = ["Mir-o-Bot Animation Commands", 
"""Some animations: [animation name] [n]:
    where [animation name] can be:
    ladderup/ladderdown/climbup/climbdown/stairs
    /walk/run/back/moonwalk/swim/swimslow
    /dance/crazy/what/zomby/hammer/wait/laugh/thank/talk
    and [n] is the number of times you want to do."""]
    
#=============================================================================	
#Style, fog and sky commands
HelpStyle = ["Mir-o-Bot Style Commands", 
"""Global age style (sky background and fog layer):
    style [value] : Changes the \"style\". Where value can be default or an age file name (i.e. city for Ae'gura)

To modify the fog layer:
    fog [on/off]: Adds or removes the fog layer.
    nofog : Disables the fog.
    fogshape [start] [end] [density]: Changes the \"shape\" of the fog. Where start, end and density are integers.
    fogcolor [r] [g] [b] : Changes the fog color. Where r, g and b (red, green and blue) are numbers between 0 and 100.
    fogcolor [color name] : Changes the fog color. Where [color name] can be white, red, pink, orange, brown, yellow, green, blue, violet, purple, black or gold.

To modify the sky background:
    sky [on/off]: Adds or removes the sky layers.
    skycolor [r] [g] [b] : Changes the sky color. Where r, g and b (red, green and blue) are numbers between 0 and 100.
    skycolor [color name] : Changes the sky color. Where [color name] can be white, red, pink, orange, brown, yellow, green, blue, violet, purple, black or gold.

Starry night effets:
    night [on/off/scale]: on = enables night, off = disable night, scale = enables night with a specified enlargement of star field.
    day : disables night. (equivalent to "night off")
    cms [on/off]: on = enables Colored Moving Sky during 5 minutes, off = disables Colored Moving Sky."""]

#=============================================================================	
#Jalak commands
HelpJalak = ["Mir-o-Bot Jalak Commands", 
"""-- Jalak creations (thanks to Michel) --
In Jalak, you can save and load your creations with the following commands:
    savestruct [savename] : Saves a structure (columns and widgets).
    loadstruct [savename] : Loads a structure (columns and widgets).
    savecolumns [savename]: Saves only columns.
    loadcolumns [savename]: Loads only columns.
    savecubes [savename]  : Saves only widgets.
    loadcubes [savename]  : Loads only widgets.
    resetcubes            : Takes off widgets."""]
    
    msg += "\nThats all for the moment."
