# This sets colors to use on screens based on the screen's background image
wallpapers = [
    "~/.local/share/wallpapers/4K NO Logo Pl 1951.png",
    "~/.local/share/wallpapers/planet-purple-space-art.jpg",
    "~/.local/share/wallpapers/Plasma_K022_4K_Winter.png",
]
wp_mode = "fill"

theme = dict(
    foreground ='#CFCCD6',
    background ='#101010',
    text_light ="#e5e5e5",
    text_dark  ='#222222',
    dull       ='#495068',

    cpu        ='#0043aa',
    ram        ='#457459',
    storage    ='#bb5500',
    updates    ='#673489',
    uptime     ="#235476",
    clipboard  ='#3e3e73',

    wlan       ="#44ccbb",
    batteryhigh='#90dd02',
    batterylow ='#dd0202',
    backlight  ='#eeee55',
    volume     ="#dd7090",
    clock      ='#bb99ff',

    # Accent colors will vary depending on screen wallpaper
    accent     ='#9a5eb3',
    unfocused  ='#503040',
)

font_settings = dict(
    typeface = "Ubuntu Nerd Font",
    pt = 14,

)

widget_defaults = dict(
    font=font_settings["typeface"],
    foreground=theme["text_light"],
    background=theme["background"],
    fontsize=font_settings["pt"],
    padding=4,
)

extension_defaults = widget_defaults.copy()

icns = "Papirus-Dark"