#
# ~/.bash_profile
#

[[ -f ~/.bashrc ]] && . ~/.bashrc
export GPG_TTY=$(tty)

# auto start x server and qtile in tty1 after boot
if [[ "$(tty)" = "/dev/tty1" ]]; then
	if which qtile > /dev/null; then
		pgrep qtile || startx
	fi
fi



