#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# aliases
if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi

if ! shopt -oq posix; then
  if [ -f /usr/share/bash-completion/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
  elif [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
  fi
fi

if [[ "$(tty)" = "/dev/tty1" ]]; then
	if which qtile > /dev/null; then
		pgrep qtile || startx
	fi
fi

# my own written scripts
export PATH="$PATH:/home/fadi/scripts/global/"

# prompt
PS1='\u@\h \W\$ '

set -o vi
HISTTIMEFORMAT="%F %T "
HISTCONTROL=ignoreboth

shopt -s checkwinsize

