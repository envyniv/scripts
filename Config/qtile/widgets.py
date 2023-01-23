import os

from libqtile.lazy import lazy
# from libqtile import widget
from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration

from conformity import theme, icns
# from screenman import backlight
# from keybinds import kb_layouts
kb_layouts = ["it"]

# method to convert ISO 3166 to flag emojis 
from flag import flag

"""
Widgets

This is where I set up all my widgets for reuse
"""

bklghtpath = '/sys/class/backlight'

updates = widget.CheckUpdates(
    background = theme["updates"],

    display_format = "{updates} \ufbae",
    initial_text = "\uf254",
    no_update_string = "\ue63f",

    decorations=[PowerLineDecoration()]

    # custom_command
    # execute
)

clipboard = widget.Clipboard(
    background = theme["clipboard"],
    blacklist = [
        "keepassxc",
        "KeePassXC",
        ],
    blacklist_text = '\uf023',
    fmt = "\uf64c {}",
    timeout = None,
    mouse_callbacks = {
        "Button1":lazy.spawn("rofi-greenclip"),
    },
    decorations=[PowerLineDecoration()]

)

# battery = widget.Battery(
#     foreground = theme["batteryhigh"],
#     low_foreground = theme["batterylow"],
#     background=theme["text_dark"],

#     charge_char="\uf583",
#     discharge_char="\uf578",
#     empty_char="\uf58d",
#     full_char="\uf582",
#     unknown_char="\uf590",

#     show_short_text = False,
#     update_interval = 5,

#     format='{percent:2.0%} {char} ',
#     notify_below = 15,
#     # decorations = powerline,
# )

ram = widget.Memory(
    background=theme["ram"],
    format='\uebd5 {MemUsed:.0f}{mm}',
    decorations=[PowerLineDecoration()]
)

storage = widget.DF(
    background = theme["storage"],
    visible_on_warn = False,
    format="\ueb29 {uf}{m}",
    decorations=[PowerLineDecoration()]
)

"""
This is kind of a hack. We're not actually using PulseAudio stuff but goddamn we want the system to believe it!
"""

# wlan = widget.Wlan(
#     format="\ufaa8 ",
#     disconnected_message = '\ufaa9 ',
#     # foreground=colours[5],
#     background = theme["wlan"],
#     foreground = theme["text_dark"],
#     update_interval=5,
# )
widget_panel_left = [
    widget.CPU(
        background = theme["cpu"],
        format = '\ueabe {load_percent}%',
        decorations=[PowerLineDecoration()]
    ),
    ram, storage, updates, #uptime,
    clipboard,

    widget.Chord(
        background = theme["text_dark"],
        decorations = [PowerLineDecoration(path="forward_slash")]
    ),
                    
    widget.Spacer(),
]

def backlightWidget():
  if len(os.listdir(bklghtpath)):
      return [
        widget.Backlight(
            backlight_name = os.listdir(bklghtpath)[0],
            background = theme["backlight"],
            foreground = theme["text_dark"],
            format = "{percent:2.0%} \uf5df ",
            decorations = [
                PowerLineDecoration(path = "rounded_right")
            ]
            # mouse_callbacks = {
            #     "Button1":lazy.function(backlight("dec")),
            #     "Button3":lazy.function(backlight("inc")),
            # }
        )
      ]
  return []

widget_panel_right = [
    widget.Spacer(decorations=[PowerLineDecoration(path="rounded_right")]),

    widget.StatusNotifier(
        decorations=[PowerLineDecoration(
            path=[ (0,0), (1,0), (1,.2), (.5,.2), (.5,.8), (1,.8), (1,1), (0,1)
            ]
        )],
        icon_theme = icns,
        background = theme["text_dark"],
    ),
    #battery,
    widget.UPowerWidget(
        foreground = theme["batteryhigh"],
        low_foreground = theme["batterylow"],
        background=theme["dull"],
        border_charge_colour = theme["batteryhigh"],
        border_colour = theme["batteryhigh"],
        border_critical_colour = theme["batterylow"],
        fill_charge = theme["batteryhigh"],
        fill_critical = theme["batterylow"],
        fill_low = theme["batterylow"],
        fill_normal = theme["batteryhigh"],
        text_charging = '{percentage:.0f}% {ttf}',
        text_discharging =  '{percentage:.0f}%',
        margin = 10,

        decorations = [
            PowerLineDecoration(path = "back_slash") # for whatever reason this doesn't worh with "rounded_right"
        ]
    ),
    widget.WiFiIcon(
        background = theme["wlan"],
        foreground = theme["text_dark"],
        active_colour = theme["text_dark"],
        inactive_colour = theme["dull"],

        decorations = [
            PowerLineDecoration(path = "forward_slash")
        ]
    ),
    
    ] + backlightWidget() + [
    widget.PulseVolume(
        # emoji = True,
        fmt = "{} \ufa7d ",
        background = theme["volume"],
        foreground=theme["text_dark"],
        update_interval = 0.01,
        mute_command = "pw-volume mute toggle",
        get_volume_command = "echo $(pw-volume status | jq '.percentage')%", # this doesn't seem to work
        decorations = [
            PowerLineDecoration(path = "rounded_left")
        ]
    ),
    widget.KeyboardLayout(
        # https://flag.readthedocs.io/en/latest/
        configured_keyboards = kb_layouts,
        mouse_callbacks = {
            "Button1": lazy.widget["keyboardlayout"].next_keyboard(),
            
        },
        display_map = {
            str(i):flag(i.split()[0]) for i in kb_layouts
        },
        decorations = [
            PowerLineDecoration(path = "rounded_right")
        ]
    ),
    widget.Clock(
        background=theme["clock"],
        foreground=theme["text_dark"],
        format="%d/%m/%y %H:%M \uf5ef",
    ),
]

gb_settings = dict(
        center_aligned = True,
        disable_drag = True,
        use_mouse_wheel = True,

        background                  = theme["text_dark"],
        active                      = theme["text_light"],
        inactive                    = theme["dull"],
        highlight_color             = theme["dull"],
        urgent_border               = theme["batterylow"],
        urgent_text                 = theme["text_light"],
        other_current_screen_border = theme["dull"],
        other_screen_border         = theme["dull"],
        this_current_screen_border  = theme["accent"],
        this_screen_border          = theme["accent"],

        margin = 3,
        
        urgent_alert_method = "block",
        highlight_method = "line",
        # visible_groups to be changed depending on screen number and available groups
)
