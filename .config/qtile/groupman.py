from typing import Any, Callable, List, Tuple
from re import compile

from libqtile.config import Group, Match
from libqtile.lazy import lazy
from libqtile import hook, qtile
from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration

from conformity import wallpapers

"""
Here I manage all group related things.

Top and Home row are all generic groups with no specific purpose.
Bottom row are for special groups where more specific apps will be spawned.

No numbers as I like to keep numbers bound to screens.
"""

"""
Autogenerate special groups based on how many List(s) of Match(es) there are
in `matches_special`.

"""
matches_browsers = [
    Match(wm_class='Navigator'),
    # Match()
]
matches_editors = [
    Match(wm_class="vscodium"),
    Match(wm_class="kdenlive"),
    Match(wm_class="Blender"),
    Match(wm_class="Godot_Editor"),
    Match(wm_class="libreoffice"),
]
matches_games = [
    Match(wm_class = "Godot_Engine"),
    Match(wm_class = compile(r"steam_app_\d+")), # pretty much all Proton apps
    Match(wm_class = "Mindustry"),
    Match(wm_class = "hl2_linux"), # tf2
]
alphabet_special = "zxcvbnm"

specials : List[Tuple] = [
    # A tuple must contain a string to use as a label and a List[Match]
    ("",matches_browsers),
    ("",matches_games),
    ("",matches_editors),
]

def getSpecialsAmount():
    return len(specials)

def specialGroups() -> List[Group]: # these are visible on every screen
    a = []
    for i in range(len(specials)):
        a.append(
            Group(
                # the first character of `name` will be what is used for keybinds
                name    = alphabet_special[i],

                # letter after glyph will be uppercase
                label   = str(specials[i][0]+" "+alphabet_special[i].upper()),

                matches = specials[i][1],
            )
        )
    return a

"""
Autogenerate 3 generic groups per screen
"""
alphabet = "qwe"+"rty"+"uio"+"pas"+"dfg"+"hjk" # 6 screens, 3 groups per screen

def genericGroups(screen_number) -> List[Group]: # these are visible only on the screen they are made for
    a = []
    for i in range(screen_number):
        for j in alphabet[i*3:(i+1)*3]: #slice string in groups of 3
            a.append(Group(j))
    return a

# Actually set the groups variable to be imported by config
# groups: List[Group] = genericGroups() + specialGroups()
def getGroups(screen_num):
    return genericGroups(screen_num) + specialGroups()
# def pause() -> None:
#     lazy.spawn(f"kill -STOP {proc_id(lazy.window)}")
#     return

@hook.subscribe.setgroup
def onGroupChange() -> None: 
    return

@hook.subscribe.group_window_add
def onWindowAddToGroup(group, window):
    if group.name == specials[2][1]:
    # ensure shit like tf2 doesn't just randomly float
      window.cmd_disable_floating()
    return
