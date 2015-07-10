#!/usr/bin/python2


import infog
import nmap
import basic
import arpspoof
import crypto
import os
import time

os.system("dialog --infobox '!!..EtHiC@L H@CkInG..!!' 10 40")
time.sleep(1)

def mainf():

	os.system("dialog --title 'MENU' --menu 'Select your choice' 20 60 6 1 'InFoRm@TiON G@ThErInG' 2 'Sc@NnInG UsInG Nmap' 3 'B@SiC NeTwOrK InFoRm@TiOn' 4 'ArPsPoOfInG' 5 'EnCrYpTiOn & DeCrYpTiOn oF D@T@' 6 'B@Ck' 2> /root/Desktop/Project/wish.txt ")
	f=open('/root/Desktop/Project/wish.txt' , 'r')
	c=f.read()

	if c== '1' :
		infog.mainf()
		mainf()

	if c== '2' :
		nmap.mainf()
		mainf()

	if c== '3' :
		basic.mainf()
		mainf()

	if c== '4' :
		arpspoof.mainf()

	if c== '5' :
		crypto.mainf()
		mainf()

	if c== '6' :
		os.system("dialog --infobox 'ThAnK YoU......' 10 40")
		time.sleep(1)
		exit()

mainf()	
	
