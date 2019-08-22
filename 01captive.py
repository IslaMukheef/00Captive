###	Note  you need to install scapy ###
###	      pip install scapy		###
###	scapy works only with python 2  ###

import subprocess
import os
import time
import scapy.all as scapy
subprocess.call("ifconfig")
interface = raw_input("interface > ") 


while True:
	f = raw_input("enter range \nexmple:  1/24 or 100/124 >")
	if len(f) == 4:
		break
	if len(f) == 3:
		break
	if len(f) == 7:
		break
	else:
		print("exmple:  1/24 or 100/124")

address = "192.168.1."+f
def scan(ip):
	arp_packet = scapy.ARP(pdst=ip)
	broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	arp_broadcast_packet = broadcast_packet/arp_packet
	answered_list = scapy.srp(arp_broadcast_packet, timeout=1, verbose=False)[0]
	client_list = []
	for ip_mac in answered_list:
		client_dict = {"ip": ip_mac[1].psrc, "mac": ip_mac[1].hwsrc}
		client_list.append(client_dict)	
	print("IPs\t\tMACs\n---------------------------------------------------")
	for client in client_list:
		 print(client["ip"]+"\t"+client["mac"])
scan(address)
while True:
	
	new_mac=raw_input("New MAC ? > ")
	if len(new_mac) == 17:
		break
	else:
		print("Try again >")
subprocess.call(["ifconfig",interface,"down"])
subprocess.call(["ifconfig",interface,"hw","ether",new_mac])
subprocess.call(["ifconfig",interface,"up"])
print("check if you still on the network")
time.sleep(2)
subprocess.call(["ping","-I",interface,"www.google.com","-c3"])

	
	
