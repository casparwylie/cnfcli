# cnf-cli
https://pypi.org/project/cnfcli/

CLI tool based on command-not-found.com, providing installation suggestions for any command,
and detect's OS to choose and install the tool automatically. 

## Installation

`pip3 install cnfcli`

## Usage

`-bash: lsof: command not found`

:(

`$ cnf lsof`
will recommend installations for the command `lsof` based on your OS.
```$ cnf lsof
Found `brew install lsof`

Would you like to install it? [Y/n]
```

Or, failing to find a good match, it will display all results:

```
Debian: apt-get install lsof
Ubuntu: apt-get install lsof
Alpine: apk add lsof
Arch: pacman -S lsof
Kali: apt-get install lsof
CentOS: yum install lsof
Fedora: dnf install lsof

Sorry, couldn't work out which to use.
```
