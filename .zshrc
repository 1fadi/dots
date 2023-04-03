export PATH=$HOME/bin:/usr/local/bin:$HOME/scripts/bin:$PATH
export ZSH="$HOME/.oh-my-zsh"

# See https://github.com/ohmyzsh/ohmyzsh/wiki/Themes
ZSH_THEME="clean"

zstyle ':omz:update' mode reminder  # just remind me to update when it's time
zstyle ':omz:update' frequency 14

ENABLE_CORRECTION="false"

plugins=(
	git
	zsh-autosuggestions
)

source $ZSH/oh-my-zsh.sh

export MANPATH="/usr/local/man:$MANPATH"

# Preferred editor for local and remote sessions
# if [[ -n $SSH_CONNECTION ]]; then
#   export EDITOR='vim'
# else
#   export EDITOR='mvim'
# fi

source $HOME/.aliases
