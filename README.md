# cnf-cli
https://pypi.org/project/cnfcli/

CLI tool based on command-not-found.com, providing installation suggestions for any command.

## Installation

`pip3 install cnfcli`

## Usage

E.g `$ cnf lsof`
will recommend installations for the command `lsof` based on your OS.
```$ cnf lsof
Found `brew install lsof`

Would you like to install it? [Y/n]
```

Or, failing to find a good match, it will display all results:

```
Debian: apt-get install file
Ubuntu: apt-get install file
Alpine: apk add file
Arch: pacman -S file
Kali: apt-get install file
CentOS: yum install file
Fedora: dnf install file

Sorry, couldn't work out which to use.
```
