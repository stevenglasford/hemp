#/bin/bash

# This file is for your cron tab

# This shell file should be added to your cron.d `crontab -e`
# It should look like the following at the end of the file
	# `@reboot ./home/pi/hemp/off.sh`

# Turn off system
./off.sh;
# sleep for a second
sleep 5s;
# Turn on system
python on.py
