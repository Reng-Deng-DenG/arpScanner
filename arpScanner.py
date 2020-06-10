from scapy.all import *

scan = 5
broadcast =  'FF:FF:FF:FF:FF:FF'
ipRange = '192.168.47.0/24'
interface =  'wlo1'
ipList = {}
x = 0

while x<scan:

	#srp couche 2
	on, off = srp(Ether(dst=broadcast)/ARP(pdst=ipRange), timeout=2, iface=interface, verbose=0)

	for element in on:
		ip = element[1].psrc# Récupération de l'ip
		mac = element[1].hwsrc# Récupération de la mac address
		ipList[ip] = mac

	x += 1
for ip, mac in ipList.items():
	print('{} {}'.format(ip, mac))
