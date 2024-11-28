# 2.SemesterProjektPython
SUUUUP BITHCES

# Dependencies
## Update system
sudo apt update
sudo apt upgrade

## Install pip3
sudo apt-get install python3-pip

## Install Flask
pip3 install flask

## Install PySerial
sudo pip3 install pyserial

## Boot script
file path: root/etc/rc.local

```
#!/bin/sh -e
#
# rc.local
#
# This script is executed at the end of each multiuser runlevel.
# Make sure that the script will "exit 0" on success or any other
# value on error.
#
# In order to enable or disable this script just change the execution
# bits.
#
# By default this script does nothing.

# Print the IP address
_IP=$(hostname -I) || true
if [ "$_IP" ]; then
  printf "My IP address is %s\n" "$_IP"
fi

sudo python3 /home/rpi/2.SemesterProjektPython/server.py&
exit 0
```
