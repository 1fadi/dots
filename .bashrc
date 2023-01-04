#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return


# source aliases
if [ -d ~/.bashrc.d ]; then
	for rc in ~/.bashrc.d/*.bashrc; do
		if [ -f "$rc" ]; then
			. "$rc"
		fi
	done
fi

if ! shopt -oq posix; then
  if [ -f /usr/share/bash-completion/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
  elif [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
  fi
fi

# auto start x server and qtile in tty1 after boot
if [[ "$(tty)" = "/dev/tty1" ]]; then
	if which qtile > /dev/null; then
		pgrep qtile || startx
	fi
fi


export PATH="$PATH:/$HOME/.local/bin/scripts/global/"
export PATH="$PATH:/$HOME/.local/bin/"
export PATH="$PATH:/$HOME/scripts/bin/"

# default programs
export EDITOR="vim"
export PICVIEW="feh"
export TERM="xterm-256color"
export BROWSER="qutebrowser"
export FILE="less"


# prompt
PS1='\u@\h \W\$ '

set -o vi
HISTTIMEFORMAT="%F %T "
HISTCONTROL=ignoreboth

shopt -s checkwinsize
