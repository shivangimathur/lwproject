#!/usr/bin/python2

import os
import time

os.system("dialog --infobox '        Welcome To The Network Mapper       ' 10 40")
time.sleep(1)

def n() :
	
	os.system('dialog --menu "Select your choice " 20 60 9 1 "Network Scanning" 2 "Specific Port scan" 2 "Excluding any host from scanning" 3 "To find if a host is protected 	by a firewall or not" 4 "To show open ports of a host" 5 "Quick Traceroute" 6 "Intense scanning" 7 "OS scanning" 			8 "Exit" 2> /root/Desktop/choice.txt')
	f=open('/root/Desktop/choice.txt' , 'r')
	c=f.read()
 
	if c== '1' : 
		os.system("dialog --inputbox 'Enter IP address to be scanned ' 10 40 2> /root/Desktop/ip.txt")
		f=open('/root/Desktop/ip.txt' , 'r')
		r=f.read()
		s=r+"/24"
		os.system("dialog --infobox 'Please wait....' 10 40")
		os.system("nmap "+s+" >/root/Desktop/result.txt")
		os.system("dialog --textbox /root/Desktop/result.txt 20 80")
		n()

		
	if c== '2' :	
		os.system("dialog --inputbox 'Enter IP address ' 10 40 2> /root/Desktop/ip.txt ")
		os.system("dialog --inputbox 'Enter port no. to be scanned ' 10 40 2> /root/Desktop/pt.txt ")
		os.system("dialog --infobox 'Please wait....' 10 40")
		time.sleep(2)
		f=open('/root/Desktop/ip.txt' , 'r')
		r=f.read()
		g=open('/root/Desktop/pt.txt' , 'r')
		s=g.read()
		os.system("nmap -p "+s+" "+r+" > /root/Desktop/ip1.txt")
		os.system('dialog --textbox /root/Desktop/ip1.txt 10 60')
		n()

	if c== '3' :
	
		os.system("dialog --inputbox 'Enter ip address ' 10 40 2> /root/Desktop/ip.txt ")
		os.system("dialog --inputbox 'Enter ip address of host you don't want to scan' 10 50 2> /root/Desktop/ip1.txt")
		os.system("dialog --infobox 'Please wait....' 10 40")
		time.sleep(2)
		f=open('/root/Desktop/ip.txt' , 'r')
		r=f.read()
		s=r+"/24"
		g=open('/root/Desktop/ip1.txt' , 'r')
		h=g.read()
		os.system("nmap "+s+" --exclude "+h+" >/root/Desktop/ip1.txt")
		os.system("dialog --textbox /root/Desktop/ip1.txt 10 40")
		n()

	if c== '4' :
		os.system("dialog --inputbox 'Enter the IP address you want to test for..? ' 10 50 2> /root/Desktop/ip.txt")
		os.system("dialog --infobox 'Please wait...' 10 40")
		f=open('/root/Desktop/ip.txt' , 'r')
		r=f.read() 								
		os.system("nmap -sA "+r+" > /root/Desktop/result.txt")
		os.system("cat /root/Desktop/result.txt | grep 'filtered' > /root/Desktop/final.txt")
		os.system("dialog --textbox /root/Desktop/final.txt 20 60")
		n()
		
	if c== '5' :
		os.system("dialog --inputbox 'Enter the IP address' 10 50 2> /root/Desktop/ip.txt")
		os.system("dialog --infobox 'Please wait..' 10 50")
		f=open('/root/Desktop/ip.txt' , 'r')
		r=f.read()
		os.system("nmap --open "+r+" > /root/Desktop/ip.txt")
		os.system("dialog --textbox /root/Desktop/ip.txt 10 50")				
		n()		
	
	if c== '6' :
		os.system("dialog --inputbox 'Enter IP address' 10 50 2> /root/Desktop/ip.txt")
		os.system("dialog --infobox 'Please wait....' 10 50")
		f=open('/root/Desktop/ip.txt' , 'r')
		r=f.read()
		os.system("nmap --sn --traceroute "+r+" > /root/Desktop/result.txt")
		os.system("dialog --textbox /root/Desktop/result.txt 10 50")
		n()
			                                                         
	if c== '7' : 
		os.system("dialog --inputbox 'Enter IP address' 10 50 2> /root/Desktop/ip.txt")
		os.system("dialog --infobox 'Please wait....' 10 50")
		f=open('root/Desktop/ip.txt' , 'r')
		r=f.read()
		os.system("nmap -T4 -A -v -Pn "+r+" > /root/Desktop/result.txt")
		os.system("dialog --textbox /root/Desktop/result.txt 10 50")
		n()

	if c== '8' :
		os.system("dialog --inputbox 'Enter IP address ' 10 50 2> /root/Desktop/ip.txt")
		os.system("dialog --infobox 'Please wait....' 10 50")
		f=open('/root/Desktop/ip.txt' , 'r')
		r=f.read()
		os.system("nmap -sS -O "+r+" > /root/Desktop/result.txt")
		os.system("cat /root/Desktop/result.txt | grep 'Running' > /root/Desktop/final.txt")	
		os.system("dialog --textbox /root/Desktop/final.txt 10 50")
		n()

	if c== '9' : 
		exit()                                                       
	

n()
raw_input()
