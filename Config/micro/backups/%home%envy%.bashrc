export FUNCNEST=100 # forkbomb killer
export HISTFILESIZE=5000
export HISTSIZE=500

# if [ "$TERM" = "linux" ]; then
# fi

function matchCOLOR {
	echo ""
}

function resultPrompt {
	if [ $? = 0 ]; then
		echo -e "\e[0;32m  \e[0m"
	else
		echo -e "\e[0;31m  \e[0m"
	fi
	echo ""
}

function userPrompt {
	echo "$USER"
}

# get current branch in git repo
function parse_git_branch {
	BRANCH=`git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/\1/'`
	if [ ! "${BRANCH}" == "" ]
	then
		STAT=`parse_git_dirty`
		echo "[${BRANCH}${STAT}]"
	else
		echo ""
	fi
}

function pwdPrompt {
	echo "$PWD"
	parse_git_branch
}

# get current status of git repo
function parse_git_dirty {
	status=`git status 2>&1 | tee`
	dirty=`echo -n "${status}" 2> /dev/null | grep "modified:" &> /dev/null; echo "$?"`
	untracked=`echo -n "${status}" 2> /dev/null | grep "Untracked files" &> /dev/null; echo "$?"`
	ahead=`echo -n "${status}" 2> /dev/null | grep "Your branch is ahead of" &> /dev/null; echo "$?"`
	newfile=`echo -n "${status}" 2> /dev/null | grep "new file:" &> /dev/null; echo "$?"`
	renamed=`echo -n "${status}" 2> /dev/null | grep "renamed:" &> /dev/null; echo "$?"`
	deleted=`echo -n "${status}" 2> /dev/null | grep "deleted:" &> /dev/null; echo "$?"`
	bits=''
	if [ "${renamed}" == "0" ]; then
		bits=">${bits}"
	fi
	if [ "${ahead}" == "0" ]; then
		bits="*${bits}"
	fi
	if [ "${newfile}" == "0" ]; then
		bits="+${bits}"
	fi
	if [ "${untracked}" == "0" ]; then
		bits="?${bits}"
	fi
	if [ "${deleted}" == "0" ]; then
		bits="x${bits}"
	fi
	if [ "${dirty}" == "0" ]; then
		bits="!${bits}"
	fi
	if [ ! "${bits}" == "" ]; then
		echo " ${bits}"
	else
		echo ""
	fi
}

export PS1="\`resultPrompt\` \`userPrompt\` \`pwdPrompt\` \\$ "
export PS2="\e[1;30 .. \e[0m"

# export PS1="\[\e[45m\]\u\[\e[m\] \[\e[42m\]\W\[\e[m\]\`parse_git_branch\` @\A \[\e[33m\]\\$\[\e[m\] "
