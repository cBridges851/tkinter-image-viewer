from os.path import isfile, abspath, join, basename
from tkinter import filedialog
from os import listdir, pardir

from Image_Viewer.image_handler import ImageHandler

class FileHandler(ImageHandler):

    def open_files(self):
        files = filedialog.askopenfilenames(
            filetypes=(
                ("All files accepted", ["*.png", "*.jpg", "*.jpeg", "*.ico", "*.gif"]),
                ("JPEG", ["*.jpg", "*.jpeg"]),
                ("GIF", "*.gif"),
                ("PNG", "*.png"),
                ("ICO", "*.ico"),
            )
        )

        if len(files) == 0:  # User cancelled
            return
        self.image_files = []
        self.img_dir = abspath(join(files[0], pardir))
        for file in files:
            self.image_files.append(basename(file))
        self.open_mode = "files"
        self.display_image()

    def open_folder(self):
        new_dir = filedialog.askdirectory()

        if new_dir != "":
            self.open_mode = "folder"
            self.img_dir = new_dir
            self.find_images(self.img_dir)
            
    def refresh(self):
        if self.open_mode == "files":
            self.display_image()
        else:
            self.find_images(self.img_dir)
            
    def find_images(self, dir):

        self.image_files = []
        self.current_image_index = 0

        for item in listdir(dir):
            if isfile(f"{dir}/{item}"):
                if item.lower().endswith((".png", ".jpg", ".jpeg", ".ico", ".gif")):
                    self.image_files.append(item)

        self.display_image()