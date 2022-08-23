import argparse
from socket import timeout
import scapy.all as scapy

class ARPPing():
    
    def __init__(self):
        print("ARPPing is started...")

    
    def get_user_input(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-i','--ipaddress',type=str,help="You should enter an ip address.")
        args = parser.parse_args()

        if args.ipaddress != None:
            return args
        else:
            print("Enter an ip address with -i parameter")


    def arp_request(self,ip):

        arp_request_packet = scapy.ARP(pdst=ip)
        broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        combined_packet = broadcast_packet / arp_request_packet

        #ans: answered list, unans: unanswered list
        ans, unans = scapy.srp(combined_packet, timeout=2)
        ans.summary()


if __name__ == "__main__":
    try:
        arp_ping = ARPPing()
        user_input = arp_ping.get_user_input()
        arp_ping.arp_request(user_input.ipaddress)

    except PermissionError:
        print("You should be root!")

