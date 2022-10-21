from tkinter import Menu

from theme import Theme
from file_handler import FileHandler

class AppMenu(Theme, FileHandler):
    
    def create_menu(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)

        file_menu = Menu(menubar, tearoff=False)

        file_menu.add_command(label="Open File(s)", command=self.open_files, underline=0)
        file_menu.add_command(label="Open Folder", command=self.open_folder, underline=0)
        file_menu.add_command(label="Refresh", command=self.refresh, underline=0)
        file_menu.add_command(label="Exit", command=self.root.destroy, underline=1)

        theme_menu = Menu(menubar, tearoff=0)
        theme_menu.add_command(
            label="Dark", command=lambda: self.set_theme("#1D1D1D", "#F0F0F0", "#1C1C1C"), underline=0
        )
        theme_menu.add_command(
            label="Light", command=lambda: self.set_theme("#F0F0F0", "#1D1D1D", "#E0E0E0"), underline=0
        )

        customize_menu = Menu(menubar, tearoff=False)

        customize_menu.add_cascade(label="Theme", menu=theme_menu, underline=0)

        menubar.add_cascade(label="File", menu=file_menu, underline=0)
        menubar.add_cascade(label="Customize", menu=customize_menu, underline=0) 