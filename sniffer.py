from Tkinter import *
from packet import Packet
from ball import Ball
import socket, sys

class Sniffer:
    def __init__(self, canvas, max_x, max_y):
        self.canvas = canvas
        try:
            self.socket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
        except socket.error , msg:
            print 'Socket could not be created. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
            sys.exit()
        self.subnet = self.get_my_subnet()
        self.max_x = max_x
        self.max_y = max_y
        self.run = True

    def sniff(self):
        while self.run:
            packet = self.socket.recvfrom(65565)
            packet = Packet(packet)
            if not packet.throwaway:
                if self.get_subnet(packet.dest_addr) == self.subnet:
                    direction = 'INCOMING'
                else: direction = 'OUTGOING'
                Ball(
                    self.canvas,
                    packet.protocol,
                    packet.data_size,
                    self.max_x,
                    self.max_y,
                    direction
                )

    def get_my_subnet(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        return self.get_subnet(s.getsockname()[0])

    def get_subnet(self, ip):
        sub = ip.rpartition('.')
        return sub[0]
