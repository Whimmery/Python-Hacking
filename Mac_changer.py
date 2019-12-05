#!/usr/bin/env python

import_subprocess
#This will import a subprocess module. 
#A subprocess lets you make commands for different OS command like a Linux command and activate in python code


subprocess.call("ifconfig", shell=True)
#each subprocess module can come with its own specific command
#this subprocess is using the call command to use linux's "ifconfig" to look at mac addresses
