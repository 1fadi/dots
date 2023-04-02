#!/bin/sh

# xinitrc runs automatically when you run startx.

[ -f ~/.xprofile ] && . ~/.xprofile
[ -f ~/.Xresources ] && xrdb -merge ~/.Xresources

[ -f ~/.fehbg ] && . ~/.fehbg # restore wallpaper

qtile start
