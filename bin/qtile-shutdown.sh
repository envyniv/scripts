#!/usr/bin/env bash

scriptdir="$( dirname -- "$BASH_SOURCE"; )";

pacman -Qmq > "$scriptdir/../local"
pacman -Qnq > "$scriptdir/../native"

#should do flatpak next
