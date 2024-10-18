import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os
from peer import Peer

class BitTorrentGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Peer")
        
        self.peer = Peer()

        # List of files
        self.file_list = []
        
        # Main frame
        self.main_frame = ttk.Frame(root)
        self.main_frame.pack(padx=10, pady=10, fill='both', expand=True)

        # Original Files Frame
        self.original_frame = ttk.LabelFrame(self.main_frame, text="Original Files")
        self.original_frame.pack(side='left', padx=10, pady=10, fill='both', expand=True)

        # Original File Tree
        self.original_file_tree = ttk.Treeview(self.original_frame, columns=("Name", "Size"), show="headings")
        self.original_file_tree.heading("#0", text="File ID")
        self.original_file_tree.heading("Name", text="File Name")
        self.original_file_tree.heading("Size", text="File Size")
        self.original_file_tree.pack(fill='both', expand=True)

        # Received Files Frame
        self.received_frame = ttk.LabelFrame(self.main_frame, text="Received Files")
        self.received_frame.pack(side='left', padx=10, pady=10, fill='both', expand=True)

        # Received File Tree
        self.received_file_tree = ttk.Treeview(self.received_frame, columns=("Name", "Size"), show="headings")
        self.received_file_tree.heading("#0", text="File ID")
        self.received_file_tree.heading("Name", text="File Name")
        self.received_file_tree.heading("Size", text="File Size")
        self.received_file_tree.pack(fill='both', expand=True)

        # Log Messages Frame
        self.log_frame = ttk.LabelFrame(self.main_frame, text="Log Messages")
        self.log_frame.pack(side='right', padx=10, pady=10, fill='both', expand=True)

        # Text widget to display messages
        self.log_text = tk.Text(self.log_frame, height=10, width=50)
        self.log_text.pack(fill='both', expand=True, padx=10, pady=10)

        # Control Buttons Frame
        self.control_frame = ttk.Frame(root)
        self.control_frame.pack(side='bottom', pady=10)

        # Transfer File Button
        self.transfer_button = ttk.Button(self.control_frame, text="Start", command=self.transfer_file)
        self.transfer_button.grid(row=0, column=0, padx=5)

        # Stop Transfer Button
        self.stop_button = ttk.Button(self.control_frame, text="Request and Download", command=self.stop_transfer)
        self.stop_button.grid(row=0, column=1, padx=5)

        # Remove File Button
        self.remove_button = ttk.Button(self.control_frame, text="Update", command=self.remove_file)
        self.remove_button.grid(row=0, column=2, padx=5)

        # Add File Button
        self.add_button = ttk.Button(self.control_frame, text="Stop", command=self.add_file)
        self.add_button.grid(row=0, column=3, padx=5)

        # Quit Button
        self.quit_button = ttk.Button(self.control_frame, text="Quit", command=root.quit)
        self.quit_button.grid(row=0, column=4, padx=5)

    def transfer_file(self):
        # Simulate action when transfer file button is clicked
        selected_items = self.original_file_tree.selection()
        for item in selected_items:
            file_id = self.original_file_tree.item(item, "text")
            file_name = self.original_file_tree.item(item, "values")[0]
            # Display message on GUI
            message = f"Transferring file: ID={file_id}, Name={file_name}\n"
            self.log_text.insert(tk.END, message)

    def stop_transfer(self):
        # Simulate action when stop transfer button is clicked
        message = "Stopping file transfer\n"
        self.log_text.insert(tk.END, message)

    def remove_file(self):
        # Simulate action when remove file button is clicked
        selected_items = self.original_file_tree.selection()
        for item in selected_items:
            file_id = self.original_file_tree.item(item, "text")
            file_name = self.original_file_tree.item(item, "values")[0]
            # Display message on GUI
            message = f"Removing file: ID={file_id}, Name={file_name}\n"
            self.log_text.insert(tk.END, message)
            # Delete file from list
            self.original_file_tree.delete(item)

    def add_file(self):
        # Add a file to the list
        file_path = filedialog.askopenfilename()
        file_stat = os.stat(file_path)
        if file_path:
            file_name = file_path.split("/")[-1]  # Get file name from path
            file_size = file_stat.st_size  # You can get the actual file size here
            file_id = file_stat.st_ino
            self.file_list.append({"id": file_id, "name": file_name, "size": file_size})
            self.original_file_tree.insert("", "end", text=file_id, values=(file_name, file_size))
            # Display message on GUI
            message = f"Adding file: ID={file_id}, Name={file_name}\n"
            self.log_text.insert(tk.END, message)

    def receive_file(self, file_name, file_size):
        # Add the received file to the received file tree
        self.received_file_tree.insert("", "end", values=(file_name, file_size))
        # Display message on GUI
        message = f"Received file: Name={file_name}, Size={file_size}\n"
        self.log_text.insert(tk.END, message)

def main():
    root = tk.Tk()
    app = BitTorrentGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
