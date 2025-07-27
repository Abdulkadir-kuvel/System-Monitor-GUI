import tkinter as tk
from tkinter import ttk
from logic.system_stats import (get_cpu_usage,
                                get_ram_usage,
                                get_disk_usage,
                                get_network_usage)

class SystemDisplay(ttk.Frame):
    def __init__(self, parent, update_interval = 1000):
        """
        Initialize the system display frame.
        """
        super().__init__(parent)

        self.update_interval = update_interval
        self.system_label = ttk.Label(self, text="", font=("Courier", 14))
        self.system_label.pack(padx=10, pady=10)

        self.update_stats()

    def update_stats(self):
        cpu = get_cpu_usage()
        ram = get_ram_usage()
        disk = get_disk_usage()
        network = get_network_usage()

        self.system_label.config(text=f"CPU: {cpu:.1f}% | RAM: {ram:.1f}% | DISK: {disk:.1f}% | "
                                       f"NET: {network['bytes_sent'] / 1024:.1f} KB sent, "
                                       f"{network['bytes_recv'] / 1024:.1f} KB received")
        
        self.after(self.update_interval, self.update_stats)