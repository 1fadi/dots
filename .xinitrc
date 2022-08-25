#!/bin/sh

# xinitrc runs automatically when you run startx.

[ -f ~/.xprofile ] && . ~/.xprofile
[[ -f ~/.Xresources ]] && xrdb -merge ~/.Xresources

if [ -f ~/.fehbg ]; then
	. ~/.fehbg
fi

qtile start
