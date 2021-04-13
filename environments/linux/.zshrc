# If you come from bash you might have to change your $PATH.
export PATH=$HOME/bin:/usr/local/bin:$PATH
alias python=python3.6

# Path to your oh-my-zsh installation.
export ZSH="/home/quokka/.oh-my-zsh"

# See https://github.com/ohmyzsh/ohmyzsh/wiki/Themes
ZSH_THEME="robbyrussell"

plugins=(zsh-autosuggestions)

source $ZSH/oh-my-zsh.sh
PROMPT="%F{green}[%*]%f %F{yellow}%m%f %F{blue}%~%f$ "

# User configuration
alias ll='ls -alh'
export CLICOLOR=1
export LSCOLORS=dxfxcxdxbxegedabagacad
unset LESS

bindkey '^g' autosuggest-accept

# Python (pyenv)
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"

# Go
export PATH=$PATH:/usr/local/go/bin

# Node (JS)
export PATH=~/.npm-global/bin:$PATH

