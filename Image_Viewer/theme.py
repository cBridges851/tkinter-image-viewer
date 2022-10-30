import json


class Theme:
    def __init__(self):
        self.themes = self.read_theme()
        self.current_theme = self.read_custom_settings()["lastTheme"]

    def set_theme(self, background, foreground, buttonBackground):
        self.root.configure(bg=background)
        self.name_label.configure(bg=background, fg=foreground)
        self.display.configure(bg=background)
        self.move_left_button.configure(bg=buttonBackground, fg=foreground)
        self.move_right_button.configure(bg=buttonBackground, fg=foreground)

    def read_theme(self):
        with open('Image_Viewer/themes.json', 'r') as openfile:
            json_object = json.load(openfile)
            return json_object

    def read_custom_settings(self):
        with open('Image_Viewer/customSettings.json', 'r') as openfile:
            json_object = json.load(openfile)
            return json_object

    def write_last_theme(self):
        custom_settings = self.read_custom_settings()
        custom_settings["lastTheme"] = self.current_theme
        json_object = json.dumps(custom_settings, indent=4)
        with open('Image_Viewer/customSettings.json', 'w') as openfile:
            openfile.write(json_object)

    def change_theme(self, theme):
        self.set_theme(**self.themes[theme.value])
        self.current_theme = theme.value
        self.write_last_theme()
