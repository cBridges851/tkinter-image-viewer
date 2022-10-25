from tkinter import Menu

from Image_Viewer.theme import Theme
from Image_Viewer.file_handler import FileHandler
from Image_Viewer.themes_enum import Themes
class AppMenu(Theme, FileHandler):
    def __init__(self):
        Theme.__init__(self)
        
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
            label="Dark", command=lambda:self.change_theme(Themes.DARK), underline=0
        )
        theme_menu.add_command(
            label="Light", command=lambda:self.change_theme(Themes.LIGHT), underline=0
        )

        customize_menu = Menu(menubar, tearoff=False)

        customize_menu.add_cascade(label="Theme", menu=theme_menu, underline=0)

        menubar.add_cascade(label="File", menu=file_menu, underline=0)
        menubar.add_cascade(label="Customize", menu=customize_menu, underline=0) 