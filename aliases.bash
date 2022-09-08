alias declutter="~/scripts/declutter-cron"
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
alias recompileURxvt="xrdb ~/.Xresources"
alias backlight="~/scripts/kbdbacklight.sh"
alias brightness="xrandr --output $(xrandr -q | grep ' connected' | head -n 1 | cut -d ' ' -f1) --brightness"
case "$(which zsh)" in
  *bash*)   PS1="\u \w %  " ;;
  *zsh*)  PROMPT="%B%F{256}%n%f%b %U%1~%u %# " ;;
  *)        echo "unknown: $0" ;;
esac
if [[ "$TERM" = xterm ]] ; then
    if [[ "$OSTYPE" = darwin* ]] ; then
        PS1='%2~$ '
    fi
    if [[ "$OSTYPE" = linux* ]] ; then
        PS1='\u$ '
    fi
fi
