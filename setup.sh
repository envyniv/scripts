#/usr/bin/env bash
WHEREAMI=$(dirname $(realpath $0))

yesorno() {
	while true; do
		read -p "$* [y/n]: " yn
		case $yn in
			[yY]*) return 0;;
			[nN]*) return 1;;
		esac
	done
}

filecheck() {
	message="found in ~; Overwrite?"
	# if file exists, prompts deletion
	# if deletion refused, backups file and concats it with the .file equivalent
	if [[ -f "~/.$*" ]]; then
		if [ yesorno "$* $message" ]; then
			rm "~/.$*"
			ln "$WHEREAMI/$*" > "~/.$*"
		else
			echo "Alright. backing up and concat-ing instead."
			cp "~/.$*" "~/.$*.bck"
			cat "~/.$*" "$WHEREAMI/$*" "~/.$*"
		fi
	else
		ln "$WHEREAMI/$*" "~/.$*"
	fi
}

foldercheck() {
	message="found in local share. Overwrite?"
	if [[ -d "~/.local/share/$*" ]]; then
		if [ yesorno "$* $message" ]; then
			rm "~/.local/share/$*"
			ln -s "$WHEREAMI/$*" "~/.local/share/$*"
		else
			echo "Alright. no local share folders will be overwritten, then."
		fi
	else
		ln -s "$WHEREAMI/$*" "~/.local/share/$*"
	fi
}

filecheck bashrc

filecheck profile
echo "export PATH=\$PATH:~/.local/bin:$WHEREAMI/bin" >> ~/.profile

# foldercheck wallpapers
# foldercheck fonts
foldercheck icons
foldercheck themes

ln -s "$WHEREAMI/Config" ~/Config

# ln $WHEREAMI/user-dirs.dirs ~/.config/user-dirs.dirs


