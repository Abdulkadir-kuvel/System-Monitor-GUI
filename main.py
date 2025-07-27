from gui.main_window import MainWindow

if __name__ == "__main__":
    app = MainWindow(lang_code="tr")  # Change "en" to "tr" for Turkish, currently manually.
    app.mainloop()