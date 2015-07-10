#!/usr/bin/python2

import os
import time

os.system("dialog --infobox 'UsEr M@N@GeMeNt' 10 40")
time.sleep(1)

def user() :
	os.system("dialog --infobox 'Select your choice' 20 60 5 1 'Add User' 2 'Switch to another user' 3 'Delete a user account' 4 'To know the Hostname' 5 'Back' 2> /root/Desktop/Project/ch1.txt")
	f=open('/root/Desktop/Project/ch1.txt' , 'r')
	c=f.read()

	if c== '1' :
		os.system
