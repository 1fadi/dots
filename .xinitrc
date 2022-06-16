#!/bin/sh

# xinitrc runs automatically when you run startx.

### commands that need to be run!

[ -f ~/.xprofile ] && . ~/.xprofile


### urxvt settings

[[ -f ~/.Xresources ]] && xrdb -merge ~/.Xresources

### Wallpaper

#nitrogen --set-zoom ~/Downloads/wall.jpg
# feh --bg-fill ~/Wallpapers/wp6256812-dark-minimalistic-wallpapers.jpg
feh --bg-fill ~/Wallpapers/macWALL.jpg


### window manager

qtile start
