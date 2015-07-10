#!usr/bin/python2

import os
import time

time.sleep(1)

os.system("dialog --inputbox 'Enter the name of the websites :' 10 40 2> /root/Desktop/webn.txt")
os.system("dialog --infobox 'Please wait...' 20 30")
f=open('/root/Desktop/webn.txt' , 'r')
r=f.read()
os.system("whois "+r+" >/root/Desktop/result.txt")
os.system("dialog --textbox /root/Desktop/result.txt 20 70")

raw_input() 
