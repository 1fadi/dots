#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

if [[ "$(tty)" = "/dev/tty1" ]]; then
	pgrep qtile || startx
fi

PS1='[\u@\h \W]\$ '

set -o vi
HISTTIMEFORMAT="%F %T "
HISTCONTROL=ignoredups

# aliases
alias vi="vim"
alias ls="ls --color=auto"
alias ll="ls -lh"
alias la="ls -lha"
alias l="ls -CF"
alias fox="firefox --private-window"
alias cp="cp -v"
alias rm="rm -v"
alias mv="mv -v"
alias mkdir="mkdir -pv"
alias grep="grep --color=auto"
alias dir="dir --color=auto"
