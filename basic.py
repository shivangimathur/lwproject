#!/usr/bin/python2

import os
import time


def fun():

	os.system("dialog --menu 'Select your choice' 20 60 7 1 'Know your IP address' 2 'Change your IP address' 3 'Know your MAC address' 4 'Change your MAC address' 5 'Know the IP address of router' 6 'Know the speed of your LAN card' 7 'Exit' 20 60 2> /root/Desktop/Project/choice.txt")
	f=open('/root/Desktop/Project/choice.txt' , 'r')
	c=f.read()

	if c== '1' :
		f=open('/root/Desktop/Project/ip.txt' , 'w')
		f.write('Your IP address is : \n')
		f.close()
		os.system("ifconfig | grep Bcast | awk '{print $2}' | cut -c 6-18 >> /root/Desktop/Project/ip.txt")
		os.system("dialog --textbox  /root/Desktop/Project/ip.txt 10 40")
		fun()
		
	if c== '2' :
		f=open('/root/Desktop/Project/ip.txt' , 'w')
		f.write('Your IP addres is : \n') 
		f.close()
		os.system("ifconfig | grep Bcast | awk '{print $2}'| cut -c 6-18 >> /root/Desktop/Project/ip.txt")
		os.system("dialog --textbox /root/Desktop/Project/ip.txt 10 40")
		f=open('/root/Desktop/Project/ip.txt' , 'w')
		f.write("Your new IP address is: \n ")
		f.close()
		os.system("dialog --inputbox 'Enter your new IP address' 10 40 2> /root/Desktop/Project/ipn.txt")
		p=open('/root/Desktop/Project/ipn.txt' , 'r')
		s=p.read()
		os.system("ifconfig eth0 "+s)
		f=open('/root/Desktop/Project/ip.txt' , 'a')
		f.write(s)
		f.close()
		os.system("dialog --textbox /root/Desktop/Project/ip.txt 10 40")
		fun()

	if c== '3' :
		f=open('/root/Desktop/Project/mac.txt' , 'w')
		f.write('Your MAC address is: \n')
		f.close()
		os.system("ifconfig | grep 'eth0' | awk '{print $5}' >> /root/Desktop/Project/mac.txt")
		os.system("dialog --textbox /root/Desktop/Project/mac.txt 10 40")
		fun()

	if c== '4' :
		f=open('/root/Desktop/Project/mac.txt' , 'w')
		f.write('Your current MAC address \n:')
		f.close()
		os.system("ifconfig | grep 'eth0' | awk '{print $5}' >> /root/Desktop/Project/mac.txt")
		os.system("dialog --textbox /root/Desktop/Project/mac.txt 10 40")
		f=open('/root/Desktop/Project/mac.txt' , 'w')
		f.write('Your new MAC address is : \n')
		f.close()
		os.system("dialog --inputbox 'Enter your new MAC address ' 10 40 2> /root/Desktop/Project/macn.txt")
		p=open('/root/Desktop/Project/macn.txt' , 'r')
		s=p.read()
		os.system("ifconfig eth0 hw ether "+s)
		f=open('/root/Desktop/Project/mac.txt' , 'a')
		f.write(s)
		f.close()
		os.system("dialog --textbox /root/Desktop/Project/mac.txt 10 40")
		fun()

	if c== '5' :
		f=open('/root/Desktop/Project/g.txt' , 'w')
		f.write('Address of Router is :\n')
		f.close()
		os.system("route -n | grep 'UG' | awk '{print $2}' >> /root/Desktop/Project/g.txt")
		os.system("dialog --textbox /root/Desktop/Project/g.txt 10 40")	
		fun()

	if c== '6' :
		f=open('/root/Desktop/Project/speed.txt' , 'w')
		f.write('Speed of Lan card is:')
		f.close()
		os.system("ethtool eth0 | grep 'Speed' >> /root/Desktop/Project/speed.txt")
		os.system("dialog --textbox /root/Desktop/Project/speed.txt 10 40")	
		fun()

	if c== '7' :
		exit()		

		
		
fun()	
raw_input()		

