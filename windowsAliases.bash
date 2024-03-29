alias declutter="python ~/scripts/declutter-windows.py"
alias style="~/scripts/style.sh"
alias run="~/scripts/run.py"
alias c="clear && pwd && echo && ls"
alias ll='ls -alF'
alias l='ls -CF'
alias la="ls -a"
alias ncsussh="ssh immoghul@remote.eos.ncsu.edu"
alias rpissh="ssh pi@ibrahimpi.local"
alias grendel="ssh -Y immoghul@grendel.ece.ncsu.edu"
alias wheather="resize -s 42 125 && curl wttr.in"

case "$OSTYPE" in
  linux*)   PS1="\u \w %  " ;;
  darwin*)  PS1="%B%F{256}%n%f%b %U%1~%u %#  🚨🚩" ;; 
  *)        echo "unknown: $OSTYPE" ;;
esac
if [[ "$TERM" = xterm ]] ; then
    if [[ "$OSTYPE" = darwin* ]] ; then
        PS1='%2~$ '
    fi
    if [[ "$OSTYPE" = linux* ]] ; then
        PS1='\u$ '
    fi
fi
