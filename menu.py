from operator import itemgetter
from tkinter import Menu

from theme import Theme
from file_handler import FileHandler
import json


class AppMenu(Theme, FileHandler):

    def create_menu(self):
        f = open('./lang/en-GB.json', "r")
        configuration = json.load(f)
        open_file, open_folder, refresh, exit, dark, light = itemgetter(
            "open_file", "open_folder", "refresh", "exit", "dark", "light")(configuration["labels"])
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
            label=dark, command=lambda: self.set_theme("#1D1D1D", "#F0F0F0", "#1C1C1C"), underline=0
        )
        theme_menu.add_command(
            label=light, command=lambda: self.set_theme("#F0F0F0", "#1D1D1D", "#E0E0E0"), underline=0
        )

        customize_menu = Menu(menubar, tearoff=False)

        customize_menu.add_cascade(label="Theme", menu=theme_menu, underline=0)

        menubar.add_cascade(label="File", menu=file_menu, underline=0)
        menubar.add_cascade(label="Customize",
                            menu=customize_menu, underline=0)
