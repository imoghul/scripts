if [ "$(uname)" == "Darwin" ]; then
     PS1="%B%F{256}%n%f%b %U%1~%u %#  🚨🚩"
elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
     PS1="\u \w %  🚨🚩"
alias declutter="python3 ~/scripts/declutter.py"
alias style="~/scripts/style.sh"
alias run="~/scripts/run.py"
alias c="clear && pwd && echo && ls"
alias ll='ls -alF'
alias l='ls -CF'
alias la="ls -a"
alias ncsussh="ssh immoghul@remote.eos.ncsu.edu"
alias rpissh="ssh pi@ibrahimpi.local"
