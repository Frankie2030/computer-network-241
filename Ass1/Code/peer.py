import socket
import json
import threading
import tkinter as tk
from tkinter import ttk

tracker_host = 'localhost'
tracker_port = 8000
peer_id = input("Enter peer ID: ")
files = input("Enter files to share (comma-separated): ").split(',')

class TorrentClientUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Torrent Client")
        
        self.torrent_list_frame = tk.Frame(root)
        self.torrent_list_frame.pack(pady=10)
        tk.Label(self.torrent_list_frame, text="Active Torrents").grid(row=0, column=0)
        
        self.torrent_list = tk.Listbox(self.torrent_list_frame, width=50, height=10)
        self.torrent_list.grid(row=1, column=0)
        
        self.peer_frame = tk.Frame(root)
        self.peer_frame.pack(pady=10)
        tk.Label(self.peer_frame, text="Peer Connections").grid(row=0, column=0)
        
        self.peer_tree = ttk.Treeview(self.peer_frame, columns=("IP", "Port", "Status"), show='headings')
        self.peer_tree.grid(row=1, column=0)
        self.peer_tree.heading("IP", text="IP")
        self.peer_tree.heading("Port", text="Port")
        self.peer_tree.heading("Status", text="Status")
        
        self.stats_frame = tk.Frame(root)
        self.stats_frame.pack(pady=10)
        tk.Label(self.stats_frame, text="Download/Upload Statistics").grid(row=0, column=0)
        
        self.progress = ttk.Progressbar(self.stats_frame, orient="horizontal", length=400, mode="determinate")
        self.progress.grid(row=1, column=0)
        self.progress["value"] = 0
        
        self.control_frame = tk.Frame(root)
        self.control_frame.pack(pady=10)
        self.start_button = tk.Button(self.control_frame, text="Start Download", command=self.start_download)
        self.start_button.grid(row=0, column=0, padx=5)
        self.stop_button = tk.Button(self.control_frame, text="Stop Download", command=self.stop_download)
        self.stop_button.grid(row=0, column=1, padx=5)

    def start_download(self):
        file_name = input("Enter the file name to download: ")
        request_file(file_name)
        
    def stop_download(self):
        print("Download stopped...")
        
def register_with_tracker():
    """Registers the peer with the tracker."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as peer_socket:
        peer_socket.connect((tracker_host, tracker_port))
        register_request = {
            'type': 'register',
            'peer_id': peer_id,
            'files': files
        }
        peer_socket.send(json.dumps(register_request).encode())
        response = peer_socket.recv(1024).decode()
        print("Tracker response:", json.loads(response))

def request_file(file_name):
    """Requests a file from the tracker."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as peer_socket:
        peer_socket.connect((tracker_host, tracker_port))
        file_request = {
            'type': 'request',
            'file_name': file_name
        }
        peer_socket.send(json.dumps(file_request).encode())
        response = peer_socket.recv(1024).decode()
        peers = json.loads(response).get('peers', [])
        print(f"Peers with file '{file_name}':", peers)

def handle_peer_connection(conn):
    """Handles incoming peer connections for file uploads."""
    try:
        data = conn.recv(1024).decode()
        if data:
            print(f"Received data: {data}")
    finally:
        conn.close()

def start_peer_server():
    """Starts the peer server for accepting incoming connections."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 0))
    server_socket.listen()
    print(f"Peer {peer_id} is ready on {server_socket.getsockname()}")

    while True:
        conn, addr = server_socket.accept()
        threading.Thread(target=handle_peer_connection, args=(conn,)).start()

root = tk.Tk()
app = TorrentClientUI(root)
register_with_tracker()
threading.Thread(target=start_peer_server, daemon=True).start()
root.mainloop()
