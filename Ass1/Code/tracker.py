# tracker.py
import socket
import json
import threading

# Set up tracker server
tracker_host = 'localhost'
tracker_port = 8000
tracker_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tracker_socket.bind((tracker_host, tracker_port))
tracker_socket.listen()

# Dictionary to track peers and their files
peer_registry = {}

def handle_peer_connection(conn, addr):
    """Handles incoming connections from peers."""
    try:
        data = conn.recv(1024).decode()
        if data:
            request = json.loads(data)
            
            if request['type'] == 'register':
                peer_id = request['peer_id']
                file_list = request['files']
                peer_registry[peer_id] = {'address': addr, 'files': file_list}
                response = {'status': 'registered'}
                print(f"Registered peer {peer_id} with files: {file_list}")

            elif request['type'] == 'request':
                file_name = request['file_name']
                peers_with_file = [peer for peer, info in peer_registry.items() if file_name in info['files']]
                response = {'peers': peers_with_file}
                print(f"Peer requested file '{file_name}', peers with file: {peers_with_file}")

            else:
                response = {'error': 'Unknown request type'}
            
            conn.send(json.dumps(response).encode())
    finally:
        conn.close()

print("Tracker is running and waiting for connections...")
while True:
    conn, addr = tracker_socket.accept()
    threading.Thread(target=handle_peer_connection, args=(conn, addr)).start()
