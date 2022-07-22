#!/bin/bash
# Turns off all of the board outputs for my yepkit boards

## TODO: make more general, currently only able to turn off my personal boards
##       need to make more general in the event that I want to expand capacity.

ykushcmd -s YK24041 -d 1
ykushcmd -s YK24041 -d 2
ykushcmd -s YK24041 -d 3
ykushcmd -s YK24039 -d 1
ykushcmd -s YK24039 -d 2
ykushcmd -s YK24039 -d 3
