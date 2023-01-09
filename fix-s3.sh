#!/bin/bash

# password=`kdialog --title "Admin Password" --password "To fix suspension, Admin access is needed."`
# if [ $? != 0 ]; then
#   echo "Suspension fix cancelled." >> $log
#   break
# fi
# echo $password | sudo systemctl enable ./fix-s3.sh >> $log

# if [ "$EUID" -ne 0 ]
#  then echo "${0##*/}: Please run as root."
#  exit
# fi

sudo sh -c "echo RP05 > /proc/acpi/wakeup"
