#!/usr/bin/python2

import os
import time

os.system("dialog --infobox  'QR code Generator' 10 40")
time.sleep(1)

os.system("dialog --inputbox 'Enter the location of the image : ' 10 40 2> /root/Desktop/Project/img.txt")
f=open('/root/Desktop/Project/img.txt' , 'r')
r=f.read()
os.system("qrencode -s 16*16 -o "+r+" > /root/Desktop/Project/qcode.txt")
os.system("dialog --textbox /root/Desktop/Project/qcode.txt 20 80")

