#!/usr/bin/python2

import os
import time

os.system("dialog --infobox 'Encryption & Decryption of Data' 10 40")
time.sleep(1)

def ed():

	os.system("dialog --menu 'Select your choice :' 10 40 5 1 'To Encrypt data of file' 2 'To Decrypt data of file' 3 'Back' 2> /root/Desktop/Project/ch.txt")
	f=open('/root/Desktop/Project/ch.txt' , 'r')
	c=f.read()
	
	if c== '1' :
		os.system("dialog --inputbox 'Enter the location of the file :' 2> /root/Desktop/Project/loc.txt 10 50")
		f=open('/root/Desktop/Project/loc.txt' , 'r')
		r=f.read()
		os.system("dialog --infobox 'The Data has been encrypted..!!' 10 40")
		time.sleep(1)
		os.system("dialog --infobox 'Encrypted data is :' 10 30")
		os.system("openssl base64 -e -in /root/Desktop/Project/data.txt -out /root/Desktop/Project/enc.txt")
		os.system("dialog --textbox /root/Desktop/Project/enc.txt 20 40")
		ed()
	
	if c== '2' :
		os.system("dialog --inputbox 'Enter the location of the file :' 2> /root/Desktop/Project/unloc.txt 10 50")
		f=open('/root/Desktop/Project/unloc.txt' , 'r')
		r=f.read()
		os.system("dialog --infobox 'The Data has been decrypted...!!' 10 40")
		time.sleep(1)
		os.system("dialog --infobox 'Decrypted data is :' 10 30")
		os.system("openssl base64 -d -in /root/Desktop/Project/enc.txt -out /root/Desktop/Project/dec.txt")
		os.system("dialog --textbox /root/Desktop/Project/dec.txt 10 40")
		ed()

	if c== '3' :
		exit()
ed()

raw_input()
		
 
