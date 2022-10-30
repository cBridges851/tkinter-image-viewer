from operator import itemgetter
from tkinter import Menu

from Image_Viewer.theme import Theme
from Image_Viewer.file_handler import FileHandler
from Image_Viewer.themes_enum import Themes
import json


class AppMenu(Theme, FileHandler):
    def __init__(self):
        Theme.__init__(self)
        
    def create_menu(self):
        f = open('./lang/en-GB.json', "r")
        configuration = json.load(f)
        open_file, open_folder, refresh, exit, dark, light, file, theme, customize = itemgetter(
            "open_file", "open_folder", "refresh", "exit", "dark", "light", "file", "theme", "customize")(configuration["labels"])
        menubar = Menu(self.root)
        self.root.config(menu=menubar)

        file_menu = Menu(menubar, tearoff=False)

        file_menu.add_command(
            label=open_file, command=self.open_files, underline=0)
        file_menu.add_command(
            label=open_folder, command=self.open_folder, underline=0)
        file_menu.add_command(label=refresh, command=self.refresh, underline=0)
        file_menu.add_command(
            label=exit, command=self.root.destroy, underline=1)

        theme_menu = Menu(menubar, tearoff=0)
        theme_menu.add_command(
            label=dark, command=lambda:self.change_theme(Themes.DARK), underline=0
        )
        theme_menu.add_command(
            label=light, command=lambda:self.change_theme(Themes.LIGHT), underline=0
        )

        customize_menu = Menu(menubar, tearoff=False)

        customize_menu.add_cascade(label=theme, menu=theme_menu, underline=0)

        menubar.add_cascade(label=file, menu=file_menu, underline=0)
        menubar.add_cascade(label=customize,
                            menu=customize_menu, underline=0)
