#
# ~/.bashrc
#

export PATH=$PATH:~/.local/bin
export QT_STYLE_OVERRIDE=kvantum
export SDL_VIDEO_MINIMIZE_ON_FOCUS_LOSS=0
export FLATPAK_ENABLE_SDK_EXT=jdk,python,llvm15

alias ls='lsd'
alias ll='lsd -lav --ignore=..'   # show long listing of all except ".."
alias l='lsd -lav --ignore=.?*'   # show long listing but no hidden dotfiles except "."

[[ -z "$FUNCNEST" ]] && export FUNCNEST=100          # limits recursive functions, see 'man bash'

## Use the up and down arrow keys for finding a command in history
## (you can write some initial letters of the command first).
bind '"\e[A":history-search-backward'
bind '"\e[B":history-search-forward'

alias blog="~/scripts/blog.sh"

if [ -f ~/.config/synth-shell/synth-shell-prompt.sh ] && [ -n "$( echo $- | grep i )" ]; then
	source ~/.config/synth-shell/synth-shell-prompt.sh
fi

neofetch
