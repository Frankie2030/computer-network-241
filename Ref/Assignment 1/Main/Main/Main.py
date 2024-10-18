import socket
import threading
import time
import os
import xml.etree.ElementTree as ET
import sys
from p2pnetwork.node import Node

MAX_CONNECTIONS=5

class Server:
    def __init__(self, host, port):
        self.lock=threading.Lock()  # mutual exclusive
        self.server_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((SERVER_HOST, SERVER_PORT))
        

class Client:
    def __init__(self, host, port):
        self.host=host
        self.port=port
        self.connections=MAX_CONNECTIONS
        
class Tracker:
    # def __init__(self):
        
    # def request_tracker():
        
    def parse_metainfo(self, data):
        if not data.strip().startswith('<root>'):
            data = '<root>' + data + '</root>'  # Add a single root element
        root = ET.fromstring(data)
        packets = []
        for child in root:
            packet = {}
            packet['request'] = child.tag
            ip_port_data = child.text.split('|')
            packet['ip'] = ip_port_data[0]
            packet['port'] = ip_port_data[1]
            packet['data'] = ip_port_data[2] if len(ip_port_data) > 2 else ''
            packets.append(packet)
        return packets
        
    # def respone(): #return peers có file  
        

class Peer:
    def __init__(self, host,port):
        self.host=host
        self.port=port
        self.max_connections=5
        self.peer_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #socket.socket.connect()
        #self.id=socket.socket.
        print("Host name: ", host)
        print("Port number: ", port)    
        
    # def Download():
    
    # def Upload():
        