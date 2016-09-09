import socket
from struct import *

class Packet:
    def __init__(self, packet):
        packet = packet[0]
        eth_length = 14
        eth_header = packet[:eth_length]
        eth = unpack('!6s6sH', eth_header)
        eth_protocol = socket.ntohs(eth[2])
        
        if eth_protocol == 8:
            ip_header = unpack('!BBHHHBBH4s4s', packet[eth_length:20+eth_length])
            
            ihl = (ip_header[0] >> 4) & 0xF
            iph_length = ihl * 4
            self.protocol = ip_header[6]
            self.source_addr = socket.inet_ntoa(ip_header[8])
            self.dest_addr = socket.inet_ntoa(ip_header[9])
            l = iph_length + eth_length
            self.data_size = 0
            self.throwaway = False
        
            #tcp
            if self.protocol == 6:
                tcph = unpack('!HHLLBBHHH', packet[l:l+20])
                tcp_length = tcph[4] >> 4
                self.data_size = len(packet) - (l + tcp_length * 4)

            #icmp
            elif self.protocol == 1:
                self.data_size = len(packet) - (l + 4)

            #udp
            elif self.protocol == 17:
                self.data_size = len(packet) - (l + 8)
                
        else:
            self.throwaway = True
