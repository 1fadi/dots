#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

if [[ "$(tty)" = "/dev/tty1" ]]; then
	pgrep qtile || startx
fi


alias ls='ls --color=auto'
PS1='[\u@\h \W]\$ '

set -o vi
HISTTIMEFORMAT="%F %T "
HISTCONTROL=ignoredups



# ls aliases
alias ll="ls -lh"
alias la="ls -lha"
alias l="ls -CF"


alias sus="systemctl suspend"
