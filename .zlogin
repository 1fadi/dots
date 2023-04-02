#!/bin/zsh

# autostart X server and Qtile in tty1 after login
if [[ "$(tty)" = "/dev/tty1" ]]; then
	if which qtile > /dev/null; then
		pgrep qtile || startx
	fi
fi
