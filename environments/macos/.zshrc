# If you come from bash you might have to change your $PATH.
export PATH=$HOME/bin:/usr/local/bin:$PATH

# Path to your oh-my-zsh installation.
export ZSH="/Users/quokka/.oh-my-zsh"

# Set name of the theme to load --- if set to "random", it will
# load a random theme each time oh-my-zsh is loaded, in which case,
# to know which specific one was loaded, run: echo $RANDOM_THEME
# See https://github.com/ohmyzsh/ohmyzsh/wiki/Themes
ZSH_THEME="robbyrussell"

plugins=(zsh-autosuggestions)

source $ZSH/oh-my-zsh.sh
PROMPT="%F{green}[%*]%f %F{yellow}%m%f %F{blue}%~%f$ "

# User configuration
###### .bash_profile ######
### cmd
alias ll='ls -alh'
alias rm="rmtrash"   # for mac (please check rmtrash)
alias grep='grep --color=always'
export CLICOLOR=1
export LSCOLORS=dxfxcxdxbxegedabagacad
unset LESS
bindkey '^g' autosuggest-accept

### Go
export GO111MODULE=on
export PATH=$PATH:$HOME/go/bin

### pyenv
# export PATH="/usr/local/opt/m4/bin:$PATH"
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
if command -v pyenv 1>/dev/null 2>&1; then
  eval "$(pyenv init -)"
fi
