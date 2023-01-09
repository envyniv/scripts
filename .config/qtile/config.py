# std python imports
from os.path import expanduser
from subprocess import Popen

# qtile imports
from libqtile.config import Group, Match
from libqtile.lazy import lazy
from libqtile import hook, qtile, layout

# custom imports
from conformity import theme, widget_defaults, extension_defaults
from keybinds import getKeys, getMouse
from groupman import getGroups, getSpecialsAmount
from screenman import getScreens

screenMinimum = 2

groups = getGroups(screenMinimum)
screens = getScreens(groups, screenMinimum, getSpecialsAmount()) #getScreens(List[Group], NumberOfScreens:int)
keys = getKeys(groups)
mouse = getMouse()

layouts = [
    layout.Columns(
        border_focus_stack = theme["accent"],
        border_focus = theme["accent"],
        border_normal_stack = theme["unfocused"],
        border_normal = theme["unfocused"],
        margin = 5,
        margin_on_single = 10,
    ),
]

@hook.subscribe.startup_once
def autostart() -> None:
    Popen([expanduser('~/scripts/autostart.sh')])
    return

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = False
focus_on_window_activation = "smart"
reconfigure_screens = True

# Some applications will wanna minimize after losing focus.
# This prevents them from doing that.
auto_minimize = False

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; it is suggested setting this string if your
# java app doesn't work correctly. We may as well just lie and say that we're
# a working one by default.
wmname = "LG3D"
