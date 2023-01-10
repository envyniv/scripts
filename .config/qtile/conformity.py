from os import listdir

def getWPs(userfolder):
    wallpapers = []
    # for wallpaper in listdir(userfolder + "/.local/share/wallpapers"):
        # if wallpaper.endswith(".jpg") or wallpaper.endswith(".png"):
    
    # temporary patchwork
    for wallpaper in range(8):
        wallpapers.append(userfolder + "/.local/share/wallpapers/" + str(wallpaper+1) + ".jpg")
    print(wallpapers)
    return wallpapers

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

    accent     ='#9a5eb3',
    unfocused  ='#503040',
)

font_settings = dict(
    sans = "Ubuntu Nerd Font",
    monospace = "mononoki Nerd Font",
    pt = 14,

)

widget_defaults = dict(
    font=font_settings["sans"],
    foreground=theme["text_light"],
    background=theme["background"],
    fontsize=font_settings["pt"],
    padding=4,
)

extension_defaults = widget_defaults.copy()

icns = "Papirus-Dark"