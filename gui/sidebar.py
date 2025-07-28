import tkinter as tk
from tkinter import ttk

class Sidebar(ttk.Frame):
    def __init__(self, parent, on_selection, *args, **kwargs):
        """
        Initialize the sidebar frame.
        :param parent: The parent widget.
        :param on_selection: Callback function for selection changes.
        """
        super().__init__(parent, *args, **kwargs)

        self.on_selection = on_selection

        self.sidebar_label = ttk.Label(self, text="Sidebar", font=("Arial", 16))
        self.sidebar_label.pack(pady=10)

        self.buttons_frame = ttk.Frame(self)
        self.buttons_frame.pack(pady=10)

        self.create_buttons()

    def create_buttons(self):
        """
        Create buttons for the sidebar.
        """
        self.cpu_button = ttk.Button(self.buttons_frame, text="CPU", 
                                     command=lambda: self.select("cpu"))
        self.cpu_button.pack(fill=tk.X, padx=10, pady=5)

        self.ram_button = ttk.Button(self.buttons_frame, text="RAM", 
                                     command=lambda: self.select("ram"))
        self.ram_button.pack(fill=tk.X, padx=10, pady=5)

        self.disk_button = ttk.Button(self.buttons_frame, text="DISK", 
                                      command=lambda: self.select("disk"))
        self.disk_button.pack(fill=tk.X, padx=10, pady=5)

        self.net_button = ttk.Button(self.buttons_frame, text="NET", 
                                     command=lambda: self.select("net"))
        self.net_button.pack(fill=tk.X, padx=10, pady=5)

    def select(self, data_type):
        self.on_selection(data_type)