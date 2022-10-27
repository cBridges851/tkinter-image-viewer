from operator import itemgetter
from renderer import Renderer
from menu import AppMenu
from tkinter import Tk, Label, Button
from PIL import Image, ImageTk
import json


class ImageViewer(Renderer, AppMenu):
    def __init__(self):
        # Import configuration.json file, reads it and store data in variables
        f = open("./configuration.json", "r")
        configuration = json.load(f)
        blank_image, name_label, display, move_left_button, move_right_button = itemgetter(
            "blank_image", "name_label", "display", "move_left_button", "move_right_button")(configuration)

        default_directory = "./images"
        self.current_image_index = 0
        self.image_files = []
        # Hardcoded data has been changed by data from the config file
        # Eval method is used to transform string into tuple, which is the data type required by the image constructor
        self.blank_img = Image.new(
            blank_image["type"], eval(blank_image["size"]), eval(blank_image["color"]))
        self.img_dir = default_directory
        self.open_mode = "folder"

        self.root = Tk()
        # window_Width x window_Height + x_Position on screen + y_Position on screen (Unit: Pixel)
        self.root.geometry("800x600+500+250")
        self.root.resizable(height=False, width=False)
        self.name_label = Label(
            self.root, text=name_label["text"], bg=name_label["bg"], fg=name_label["fg"], font=(name_label["font"]))
        self.current_image = ImageTk.PhotoImage(self.blank_img)
        self.display = Label(image=self.current_image,
                             width=display["width"], height=display["height"], bg=display["bg"])
        self.move_left_button = Button(
            self.root, text=move_left_button["text"], font=(
                move_left_button["font"]), bg=move_left_button["bg"], fg=move_left_button["fg"], command=self.move_left
        )
        self.move_right_button = Button(
            self.root, text=move_right_button["text"], font=(
                move_right_button["font"]), bg=move_right_button["bg"], fg=move_right_button["fg"], command=self.move_right
        )

        self.create_menu()
        self.refresh()


if __name__ == '__main__':
    ImageViewer().render()
