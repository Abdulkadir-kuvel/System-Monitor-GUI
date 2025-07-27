import tkinter as tk
from tkinter  import ttk
from logic.lang import Translator
from gui.system_display import SystemDisplay
from logic.theme import THEME

class MainWindow(tk.Tk):
    def __init__(self, lang_code="en"):
        """
        Initialize the main window.
        """
        super().__init__()

        self.translator = Translator(lang_code)

        self.title(self.translator.t("title"))
        self.geometry("800x600")
        self.configure(bg=THEME["bg"])

        self.style = ttk.Style(self)
        self.style.theme_use("default")
        self.style.configure("TLabel", font=THEME["font"], 
                             background=THEME["bg"], foreground=THEME["fg"])


        label = ttk.Label(self, text=self.translator.t("welcome"), font=THEME["title_font"], background=THEME["bg"], foreground=THEME["fg"])
        label.pack(pady=20)

        self.sys_display = SystemDisplay(self)
        self.sys_display.pack(pady=10)

        