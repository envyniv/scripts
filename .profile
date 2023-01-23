# Here are all env vars to be set on login

## Uniform look for Qt and GTK
export GTK_THEME="Atom One Dark"
export GTK2_RC_FILES="~/.themes/AtomOneDarkTheme-main/gtk-2.0/gtkrc"
export QT_QPA_PLATFORMTHEME=gtk2


## Avoid SDL going insane
export SDL_VIDEO_MINIMIZE_ON_FOCUS_LOSS=0


## XDG DIRS
export XDG_CONFIG_HOME=$HOME/Config
export XDG_DOWNLOAD_DIR=$HOME/Downloads
export XDG_TEMPLATES_DIR=$HOME/Templates
export XDG_PUBLICSHARE_DIR=$HOME/Public
export XDG_DOCUMENTS_DIR=$HOME/Documents
export XDG_MUSIC_DIR=$HOME/Sound/Music
export XDG_PICTURES_DIR=$HOME/Images
export XDG_VIDEOS_DIR=$HOME/Video
export XDG_DESKTOP_DIR=$XDG_DOCUMENTS_DIR/Shared
# xdg-user-dirs-update --set CONFIG ~/Config
# xdg-user-dirs-update --set DOWNLOAD ~/Downloads
# xdg-user-dirs-update --set TEMPLATES ~/Templates
# xdg-user-dirs-update --set PUBLICSHARE ~/Public
# xdg-user-dirs-update --set DOCUMENTS ~/Documents
# xdg-user-dirs-update --set Music ~/Sound/Music
# xdg-user-dirs-update --set PUBLICSHARE ~/Public
# xdg-user-dirs-update --set PUBLICSHARE ~/Public
# xdg-user-dirs-update --set PUBLICSHARE ~/Public
