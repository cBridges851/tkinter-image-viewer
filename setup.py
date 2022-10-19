from tkinter import Tk, Label
from PIL import Image, ImageTk

class Setup:
    def __init__(self):
        default_directory = "./images"
        self.current_image_index = 0
        self.image_files = []
        self.blank_img = Image.new("RGBA", (500, 300), (0, 0, 0, 0))
        self.img_dir = default_directory
        self.open_mode = "folder"