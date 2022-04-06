#!/bin/bash
# Turns on all of the board outputs for my yepkit boards
# Restarting all of the boards has the same effect (turning on)

## TODO: make more general, currently only able to turn on my personal boards
##       need to make more general in the event that I want to expand capacity.

ykushcmd -s YK24041 -u 1
ykushcmd -s YK24041 -u 2
ykushcmd -s YK24041 -u 3
ykushcmd -s YK24039 -u 1
ykushcmd -s YK24039 -u 2
ykushcmd -s YK24039 -u 3
