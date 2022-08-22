#!/bin/sh

# xinitrc runs automatically when you run startx.

[ -f ~/.xprofile ] && . ~/.xprofile
[[ -f ~/.Xresources ]] && xrdb -merge ~/.Xresources

#feh --bg-fill ~/Wallpapers/616159.jpg

qtile start
