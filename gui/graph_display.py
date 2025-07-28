import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg # type: ignore
import matplotlib.pyplot as plt # type: ignore
from logic.system_stats import (get_cpu_usage, get_ram_usage, 
                                get_disk_usage, get_network_usage)

class GraphDisplay(ttk.Frame):
    def __init__(self, parent, delay=100, *args, **kwargs):
        """
        Initialize the graph display frame.
        :param parent: The parent widget.
        :param data_type: Type of data to display (cpu, ram, disk, net).
        """
        super().__init__(parent, *args, **kwargs)
        
        self.delay = delay
        self.cpu_data = []
        self.ram_data = []
        self.disk_data = []
        self.network_data = []
        self.metric = "cpu"
        
        self.fig, self.ax = plt.subplots(figsize = (4, 3))
        self.line, = self.ax.plot([], [], color = "#4191e0") # one element tuple

        self.ax.set_ylim(0, 100)
        # self.ax.set_xlim(0, 10)
        self.ax.set_title("Live Graph")
        self.ax.set_xlabel("Time")
        self.ax.set_ylabel("% Usage")

        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        self.update_graph()

    def update_graph(self):
        """
        Update the graph with new data.
        """
        self.cpu_data.append(get_cpu_usage())
        self.ram_data.append(get_ram_usage())
        self.disk_data.append(get_disk_usage())
        self.network_data.append(get_network_usage()['bytes_recv'] / 1024)  # Convert to KB 

        if len(self.cpu_data) > 100:
            self.cpu_data.pop(0)
            self.ram_data.pop(0)
            self.disk_data.pop(0)
            self.network_data.pop(0)

        if self.metric == "cpu":
            data = self.cpu_data
        elif self.metric == "ram":
            data = self.ram_data
        elif self.metric == "disk":
            data = self.disk_data
        else:
            data = self.network_data

        self.line.set_data(range(len(data)), data)
        self.ax.set_xlim(0, 100)
        self.canvas.draw()
        self.after(self.delay, self.update_graph)

    def set_metric(self, metric):
        """
        Set the metric to display.
        :param metric: Type of data to display (cpu, ram, disk, net).
        """
        if metric in ["cpu", "ram", "disk", "net"]:
            self.metric = metric