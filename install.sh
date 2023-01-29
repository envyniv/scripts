#/usr/bin/env bash

WHEREAMI=$(dirname $(realpath $0))
# echo $WHEREAMI

# bashrc
if [[ -f ~/.bashrc ]]; then
	cp ~/.bashrc ~/.bashrc.bck
fi

cat ~/.bashrc $WHEREAMI/bashrc > ~/.bashrc

## print new bashrc
# cat ~/.bashrc


# profile
if [[ -f ~/.profile ]]; then
	cp ~/.profile ~/.profile.bck
fi

cat ~/.profile $WHEREAMI/profile > ~/.profile
echo "export PATH=\$PATH:~/.local/bin:$WHEREAMI/bin" >> ~/.profile

## print new profile on screen
# cat ~/.profile


ln -s $WHEREAMI/wallpapers ~/.wallpapers
ln -s $WHEREAMI/themes ~/.themes
ln -s $WHEREAMI/fonts ~/.fonts

ln -s $WHEREAMI/Config ~/Config

ln $WHEREAMI/user-dirs.dirs ~/.config/user-dirs.dirs


