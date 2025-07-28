import tkinter as tk
from tkinter import ttk
import psutil # type: ignore

class TaskDisplay(ttk.Frame):
    def __init__(self, parent, delay = 100, *args, **kwargs):
        """
        """
        super().__init__(parent, *args, **kwargs)

        self.delay = delay
        self.process_headers = ["pid", "name", "status", "cpu_percent", 
                                "memory_info"]

        self.content_frame = ttk.Frame(self)
        self.content_frame.pack(fill=tk.BOTH, expand=True)
        
    def update_tasks(self):
        for element in self.content_frame.winfo_children():
            element.destroy()

        header = ttk.Label(self.content_frame, text="f{'Name':<15} | {'cpu':<6} | {'ram (mb)':<10}")
        header.pack(anchor="w")
        
        for process in psutil.process_iter(self.process_headers):
            try:
                info  = process.info
                name = info['Name'][:15]
                cpu = info['cpu_percent']
                ram = info['memory_info'].rss / (1024 * 1024)
                label = ttk.Label(self.content_frame, text = f"{name:<15} | {cpu:<6.1f} | {ram:<10.1f}")
                label.pack(anchor="w")
                
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        self.after(self.delay, self.update_tasks)