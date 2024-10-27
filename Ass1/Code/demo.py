import tkinter as tk
from tkinter import ttk

class TorrentClientUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Torrent Client")
        
        # Torrent list
        self.torrent_frame = tk.Frame(root)
        self.torrent_frame.pack(pady=10)
        tk.Label(self.torrent_frame, text="Active Torrents").grid(row=0, column=0)
        
        # Listbox to show torrents
        self.torrent_list = tk.Listbox(self.torrent_frame, width=50, height=10)
        self.torrent_list.grid(row=1, column=0)
        
        # Peer stats
        self.peer_frame = tk.Frame(root)
        self.peer_frame.pack(pady=10)
        tk.Label(self.peer_frame, text="Peer Connections").grid(row=0, column=0)
        
        # Treeview to display peers and their status
        self.peer_tree = ttk.Treeview(self.peer_frame, columns=("IP", "Port", "Status"), show='headings')
        self.peer_tree.grid(row=1, column=0)
        self.peer_tree.heading("IP", text="IP")
        self.peer_tree.heading("Port", text="Port")
        self.peer_tree.heading("Status", text="Status")
        
        # Statistics
        self.stats_frame = tk.Frame(root)
        self.stats_frame.pack(pady=10)
        tk.Label(self.stats_frame, text="Download/Upload Statistics").grid(row=0, column=0)
        
        # Progress bar for download progress
        self.progress = ttk.Progressbar(self.stats_frame, orient="horizontal", length=400, mode="determinate")
        self.progress.grid(row=1, column=0)
        self.progress["value"] = 0  # Initial progress
        
        # Control buttons
        self.control_frame = tk.Frame(root)
        self.control_frame.pack(pady=10)
        self.start_button = tk.Button(self.control_frame, text="Start Download", command=self.start_download)
        self.start_button.grid(row=0, column=0, padx=5)
        self.stop_button = tk.Button(self.control_frame, text="Stop Download", command=self.stop_download)
        self.stop_button.grid(row=0, column=1, padx=5)
        
    def start_download(self):
        # Placeholder for starting download logic
        print("Download started...")
        
    def stop_download(self):
        # Placeholder for stopping download logic
        print("Download stopped...")
        
root = tk.Tk()
app = TorrentClientUI(root)
root.mainloop()
