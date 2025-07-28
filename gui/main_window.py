import tkinter as tk
from tkinter  import ttk, Menu
from logic.lang import Translator
# from gui.system_display import SystemDisplay
from logic.theme import THEME
from gui.sidebar import Sidebar
from gui.graph_display import GraphDisplay
from gui.task_display import TaskDisplay
import sys
import psutil  # type: ignore

class MainWindow(tk.Tk):
    def __init__(self, lang_code="en"):
        """
        Initialize the main window.
        """
        super().__init__()

        self.protocol("WM_DELETE_WINDOW", self.destroy_app)

        self.translator = Translator(lang_code)

        self.title(self.translator.t("title"))
        self.geometry("800x600")
        self.configure(bg=THEME["bg"])

        self.style = ttk.Style(self)
        self.style.theme_use("default")
        self.style.configure("TLabel", font=THEME["font"], 
                             background=THEME["bg"], foreground=THEME["fg"])


        self.container = ttk.Frame(self)
        self.sidebar = Sidebar(self.container, self.on_selection)
        self.graph = GraphDisplay(self.container)

        self.task_display = TaskDisplay(self.container)

        menubar = Menu(self)
        menubar.add_command(label=self.translator.t("tasks"), command=self.show_tasks)
        menubar.add_command(label=self.translator.t("graphics"), command=self.show_graphics)
        self.config(menu=menubar)


        self.show_tasks()
        # label = ttk.Label(self, text=self.translator.t("welcome"), font=THEME["title_font"], background=THEME["bg"], foreground=THEME["fg"])
        # label.pack(pady=20)


    def show_tasks(self):
        """
        Show the system display.
        """
        self.hide_views()

        self.container.pack()
        self.task_display.pack(expand=True)                
        
        pass

    def show_graphics(self):
        """
        Show the graphics display.
        """
        self.hide_views()

        self.container.pack(fill=tk.BOTH, expand=True)
        self.sidebar.pack(side="left", fill=tk.Y)
        self.graph.pack(side="left", fill="both", expand=True)

    def hide_views(self):
        self.sidebar.pack_forget()
        self.graph.pack_forget()
        self.task_display.pack_forget()

    def on_selection(self, data_type):
        """
        Handle sidebar selection changes.
        :param data_type: Type of data selected (cpu, ram, disk, net).
        """
        self.graph.set_metric(data_type)

    def destroy_app(self):
        """
        Destroy the application.
        """
        self.destroy()
        sys.exit()