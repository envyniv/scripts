# My dotfiles

```
In this repo, I have put,

with the utmost of care, for your prying eyes...

What makes my systems tick, click;

Perhaps even wick(ed).
```

---

Essentially what goes here is crucial to my dream pc setup.

I personally use arch, so you might need to tweak things if you're using a
different distro.

## Features (Real!)
- custom `user-dirs.dirs`
- [Custom python bash prompt](./Config/customprompt.py) (buggy as hell rn)

<details><summary>Configs</summary>

- the bash shell ([.profile](./profile) and [.bashrc](./bashrc))
- [neofetch](./Config/neofetch/config.conf)
- [alacritty](./Config/alacritty/alacritty.yml)
- [micro](./Config/micro/)
- [clight](./Config/clight.conf)
- [dunst](./Config/dunst/dunstrc)
- [mopidy](./Config/mopidy/mopidy.conf)
- [Qtile](./Config/qtile/) (requires [qtile-extras](https://github.com/elParaguayo/qtile-extras)!)
- [rofi](./Config/rofi/)
- [matrixcli](./Config/live-matrixcli-cfg.py)

</details>

- Misc scripts
- - ["live chat > text file" script using matrixcli](./bin/live-chat.sh)
- - simplistic [setup script](./setup.sh)
- - Rofi powermenu lifted from [here](https://github.com/adi1090x/rofi#powermenus) and [edited to fit my needs](./bin/rofi-powermenu)
- - Dumb [script](./bin/nf-dl) that downloads my favourite [Nerd Fonts](https://www.nerdfonts.com/)
- - [Acer Swift 1 V1.08 Suspension Fix](https://wiki.archlinux.org/title/Acer_Swift_1_SF114-34#Suspension)


## TODO
- installed packages backupper and installer
- Dependency installer script?
- Application pausing and resuming (`kill -STOP`/`kill -CONT`)
- Application-specific volume management
- Easier network management (rofi?)
<!-- - More keychords idk -->
- GPU and CPU thermal sensors indicators in topbar
- World domination
- Dynamic-er groups
- Dynamic keybinds
- IME setup
