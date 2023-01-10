import os
from pathlib import Path
from time import time

from libqtile.config import Screen
from libqtile.bar import Bar
from libqtile import qtile, hook
from libqtile.lazy import lazy

from qtile_extras.widget import GroupBox
from widgets import widget_panel_left, widget_panel_right
from conformity import theme, wp_mode
from widgets import gb_settings

"""
Screenman.py

This script manages screen creation and sets rules for adding more.
Also sets up any plugged and unplugged screen.

WARNING - `xbacklight` is outdated. Please install acpilight!
"""

# IS_WAYLAND: bool = qtile.core.name == "wayland"
# IS_XEPHYR: bool = int(os.environ.get("QTILE_XEPHYR", 0)) > 0

# if IS_XEPHYR:
# elif IS_WAYLAND:

bar_settings = dict(
  size=18,
  background = theme["background"],
  #margin = 3,
)

@hook.subscribe.current_screen_change
def reconfScreens() -> None:
  # qtile.current_screen.top.widgets = widget_list
  qtile.cmd_reconfigure_screens()
  return

@hook.subscribe.screen_change
def restart_on_randr(qtile, ev):
	qtile.cmd_restart()

@hook.subscribe.client_killed
def onClientKill(window) -> None:
  return

floating_types = [
    "notification", "toolbar", "splash", "dialog",
    "utility", "menu", "dropdown_menu", "popup_menu", "tooltip",
    "dock",
]

@hook.subscribe.client_new
def set_floating(window):
  if (window.window.get_wm_transient_for()
      or window.window.get_wm_type() in floating_types):
    window.floating = True

# X11
# https://github.com/naelstrof/maim

# Wayland
# https://sr.ht/~emersion/grim/
# https://github.com/emersion/slurp

def screenshot(save=True, copy=False, ft="jpg", select=False):
  def f(qtile):
    path = Path.home() / 'Immagini'
    path /= f'screenshot_{str(int(time() * 100))}.{ft}'
    if select:
      shot = subprocess.run(['maim', '-s'], stdout=subprocess.PIPE)
    else:
      shot = subprocess.run(['maim'], stdout=subprocess.PIPE)

    if save:
      with open(path, 'wb') as sc:
            sc.write(shot.stdout)

    if copy:
      subprocess.run(['xclip', '-selection', 'clipboard', '-t',
                      'image/png'], input=shot.stdout)
  return f

def backlight(action):
    def f(qtile):
        brightness = int(subprocess.run(['xbacklight', '-get'],
                                        stdout=subprocess.PIPE).stdout)
        if brightness != 1 or action != 'dec':
            if (brightness > 49 and action == 'dec') \
                                or (brightness > 39 and action == 'inc'):
                subprocess.run(['xbacklight', f'-{action}', '10',
                                '-fps', '10'])
            else:
                subprocess.run(['xbacklight', f'-{action}', '1'])
    return f

# def proc_id(window): # Returns a string
#     xprop_id_out = check_output(["xprop -id 0x{}".format(window.info()["id"])])
#     proc_id = match(r"_NET_WM_PID.+= ([\d+)", xprop_id_out).group(0)
#     sys.stderr.write(proc_id)
#     return proc_id

def getScreens(groups, ns_screens, ns_specials, wallpapers):
  return [
    Screen(
      top = Bar(
        widget_panel_left + [
          GroupBox(
            visible_groups = [
              group.name for group in groups[i*3:(i+1)*3]
            ] + [group.name for group in groups[-ns_specials:len(groups)]],
            **gb_settings,
          )
        ] + widget_panel_right,
        **bar_settings
      ),
      wallpaper = wallpapers[i],
      wallpaper_mode = "stretch",
    ) for i in range(ns_screens)
  ]