import scapy.all as scapy

# network_scanner.py
from scapy.all import srp, Ether, ARP, conf

def scan(ip):
    answered, unanswered = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip), timeout=2)
    print(answered.summary())

if __name__ == "__main__":
    conf.verb = 0
    scan("192.168.0.1/24")


conf.verb = 0