export FUNCNEST=100 # forkbomb killer
export HISTFILESIZE=5000
export HISTFILE=$HOME/.bash_history
export HISTSIZE=500

# if [ "$TERM" = "linux" ]; then
# fi

function pyPrompt() {
	$XDG_CONFIG_HOME/customprompt.py $?
}

alias ls="lsd"
alias ll="lsd -la"
alias la='ls -a'
alias lt='ls --tree'

export PROMPT_COMMAND="shopt -s checkwinsize"
export PS1="\[\n\$(pyPrompt) \]"
