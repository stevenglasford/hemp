#! /usr/bin/python

###################
###   Imports   ###
###################
import sys
import time
import subprocess

##########################
###  Control variables ###
##########################
# Next iteration should be able to control more things
#humidity
#temperature
#EC
#PH
#max_water_level
#current_bucket_ID
pumping_time = 300 # allows the pump to run for 5 minutes
soak_time = 900 # allow the roots to soak for about 15 minutes

#########################
###  Board variables  ###
#########################
# need to change to be more generalized it should be able to just plug and play
# currently the ports and serial numbers for the boards are hardcoded.
on  =  ['ykushcmd -s YK24039 -u 1',
        'ykushcmd -s YK24039 -u 2',
        'ykushcmd -s YK24041 -u 1',
        'ykushcmd -s YK24041 -u 2']
off =  ['ykushcmd -s YK24039 -d 1',
        'ykushcmd -s YK24039 -d 2',
        'ykushcmd -s YK24041 -d 1',
        'ykushcmd -s YK24041 -d 2']

# Turn off all buckets at startup
subprocess.call('./off.sh', shell=True)

# Cycle through the buckets turning them on then sleeping
# then turning off, then go to next bucket. Simple.
while True: # Enter infinite loop
	for bucket in range(len(on)): # Enter bucket cycle
		# Turn on the buckets in order
		subprocess.call(on[bucket], shell=True)
		# Sleep for a predetermined amount of time
		time.sleep(pumping_time)
		# Turn off bucket after the predetermined amount of time
		subprocess.call(off[bucket], shell=True)
		# Allow for the roots to properly soak
		time.sleep(soak_time - pumping_time)
