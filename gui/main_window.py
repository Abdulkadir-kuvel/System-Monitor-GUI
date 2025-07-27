import tkinter as tk
from tkinter  import ttk
from logic.lang import Translator

class MainWindow(tk.Tk):
    def __init__(self, lang_code="en"):
        """
        Initialize the main window.
        """
        super().__init__()

        self.translator = Translator(lang_code)

        self.title(self.translator.t("title"))
        self.geometry("800x600")

        self.configure(bg="#777777")
        label = ttk.Label(self, text=self.translator.t("welcome"), font = "Verdana 12", background="#777777", foreground="white")
        label.pack(pady=20)

        start_button = ttk.Button(self, text=self.translator.t("show_data"), command=self.show_data)
        start_button.pack()

    def show_data(self):
        # Placeholder for the data display logic
        print("Data display logic goes here.")