from libqtile.lazy import lazy
from libqtile.config import Key, Click, Drag, EzKey, KeyChord

from screenman import screenshot, backlight #, screens

"""
This is where the magic happens.

I set most keybinds depending on what makes sense to me, but some keybinds,
Like those for screens and groups, are automatically bound.

Bindings for groups are made by picking the first character in the group name.
It is assumed no two groups start with the same letter, merely because I don't-
wanna extend the generating function.

Bindings for screens are much simpler, going from 1 through out 9, and then 0.
"""

# https://raw.githubusercontent.com/qtile/qtile/master/libqtile/backend/x11/xkeysyms.py
# https://docs.qtile.org/en/latest/manual/config/lazy.html

keybinds_system = [
    EzKey("M-C-S-r",      lazy.reload_config(),                       desc="Reload the config"),
    EzKey("M-C-S-<Tab>",  lazy.next_layout(),                         desc="Use the next layout"),
    EzKey("M-C-S-A-r",    lazy.restart(),                             desc="Restart Qtile"),

    EzKey("A-<Space>",    lazy.spawn("dunstctl close"),               desc="Close notification"),
]

keybinds_wm = [
    EzKey("M-<space>",    lazy.spawn("rofi -show drun -show-icons -theme drun-nord"),  desc="Bring up rofi"),
    EzKey("M-C-x",        lazy.window.kill(),                         desc="Kill focused window"),

    EzKey("M-<Tab>",    lazy.layout.next(),                         desc="Switch window focus to other pane(s) of stack"),

    EzKey("M-C-r",        lazy.layout.normalize(),                    desc="Reset all window sizes"),
    EzKey("M-A-<Tab>",      lazy.spawn("rofi -show window"),            desc="Window Switcher"),
    EzKey("M-S-f",        lazy.window.toggle_floating(),              desc="Put the focused window to/from floating mode"),
    # EzKey("M-C-f",        lazy.window.toggle_fullscreen(),            desc="Put the focused window to/from fullscreen mode"),
    
    KeyChord(["mod4", "control"], "Tab", [
            EzKey("b", lazy.layout.grow_left(), desc="Move window to the left"),
            EzKey("m", lazy.layout.grow_right(), desc="Move window to the right"),
            EzKey("n", lazy.layout.grow_down(), desc="Move window down"),
            EzKey("h", lazy.layout.grow_up(), desc="Move window up"),

            EzKey("S-b", lazy.layout.shuffle_left(), desc="Grow window to the left"),
            EzKey("S-m", lazy.layout.shuffle_right(), desc="Grow window to the right"),
            EzKey("S-n", lazy.layout.shuffle_down(), desc="Grow window down"),
            EzKey("S-h", lazy.layout.shuffle_up(), desc="Grow window up"),

            EzKey("b", lazy.layout.grow(), desc="Grow window"),
            EzKey("b", lazy.layout.shrink(), desc="Shrink window"),
        ],
        name = "缾 襁 ",
        mode = True,
        # desc = "Activate window manipulation mode.",
    ),

    EzKey("M-C-S-<Left>",   lazy.layout.shuffle_left(),                 desc="Move window to the left"),
    EzKey("M-C-S-<Right>",  lazy.layout.shuffle_right(),                desc="Move window to the right"),
    EzKey("M-C-S-<Down>",   lazy.layout.shuffle_down(),                 desc="Move window down"),
    EzKey("M-C-S-<Up>",     lazy.layout.shuffle_up(),                   desc="Move window up"),

    EzKey("M-C-<Left>",   lazy.layout.grow_left(),                    desc="Grow window to the left"),
    EzKey("M-C-<Right>",  lazy.layout.grow_right(),                   desc="Grow window to the right"),
    EzKey("M-C-<Down>",   lazy.layout.grow_down(),                    desc="Grow window down"),
    EzKey("M-C-<Up>",     lazy.layout.grow_up(),                      desc="Grow window up"),
]

keybinds_input = [ # inputting snippets, characters, and using media keys

    #Input things
    EzKey("M-c",                      lazy.spawn('rofimoji'), desc="Character selector"),
    EzKey("M-S-x",                    lazy.spawn("rofi -modi emoji -show emoji"), desc="Snippet Manager"),

    EzKey("<XF86AudioLowerVolume>",   lazy.spawn("pw-volume change -5%"),   desc="Lower Volume"),
    EzKey("<XF86AudioRaiseVolume>",   lazy.spawn("pw-volume change +5%"),   desc="Raise Volume"),
    EzKey("<XF86AudioMute>",          lazy.spawn("pw-volume mute toggle"),  desc="Toggle Sound"),

    EzKey("M-<XF86AudioLowerVolume>", lazy.spawn(""), desc="Lower Application Volume"),
    EzKey("M-<XF86AudioRaiseVolume>", lazy.spawn(""), desc="Raise Application Volume"),
    EzKey("M-<XF86AudioMute>",        lazy.spawn(""), desc="Toggle Application Sound Output"),
    
    EzKey("A-<XF86AudioPrev>",        lazy.spawn(""), desc="Go to previous song"),
    EzKey("A-<XF86AudioNext>",        lazy.spawn(""), desc="Go to next song"),
    EzKey("A-<XF86AudioPlay>",        lazy.spawn(""), desc="Pause / Resume playback"),
    EzKey("A-<XF86AudioStop>",        lazy.spawn(""), desc="Stop playback"),

    EzKey("<XF86MonBrightnessDown>",  lazy.function(backlight("dec")), desc="Lower Monitor Brightness"),
    EzKey("<XF86MonBrightnessUp>",  lazy.function(backlight("inc")), desc="Raise Monitor Brightness"),

    EzKey("<XF86TouchpadToggle>",  lazy.spawn(""), desc="Toggle Touchpad"),

    EzKey("<Print>",                  lazy.function(screenshot()),     desc="Take a screenshot"),
    EzKey("S-<Print>",                lazy.function(screenshot(select=True)),     desc="Take a screenshot, select an area"),
    # EzKey("M-<Print>",                lazy.function(screenshot(select=True)),     desc="Screenshot current window"),
    EzKey("<XF86Calculator>",         lazy.spawn("rofi -show calc -no-show-match -no-sort"), desc="Calculator"),

    EzKey("C-<Insert>", lazy.widget["keyboardlayout"].next_keyboard(), desc="Next keyboard layout."),
]

def groupKeybind(groups):
    keybinds_groups = []
    for i in groups:
        keybinds_groups.extend([
            EzKey(f"M-{i.name[0]}", lazy.group[i.name].toscreen(), desc=f"Switch to group '{i.name}'"),
            EzKey(f"M-S-{i.name[0]}", lazy.window.togroup(i.name), desc=f"Move focused window to group '{i.name}'"),
        ])
    return keybinds_groups

# def screenKeybind(screens):
#     keybinds_screens = []
#     for i in screens:
#         keybinds_screens.extend([
#             EzKey("", lazy.toscreen())
#         ])
#     return keybinds_screens

def getKeys(g):
    return keybinds_system + keybinds_wm + keybinds_input + groupKeybind(g)

mouse_actions = [
    Drag(["mod4"], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag(["mod4"], "Button3", lazy.window.kill()),
]

def getMouse():
    return mouse_actions

# kb_layouts = ["it"]