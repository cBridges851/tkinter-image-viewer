from tkinter import Tk, Label, Button, Menu, filedialog
from PIL import Image, ImageTk
from os import listdir
from os.path import isfile


class ImageViewer:
    def __init__(self):

        default_directory = "./images"
        self.current_image_index = 0
        self.image_files = []
        self.blank_img = Image.new("RGBA", (500, 300), (0, 0, 0, 0))
        self.img_dir = default_directory

        self.root = Tk()
        self.name_label = Label(self.root, text="No image found", bg="#1D1D1D", fg="#FFFFFF", font=("Arial 18"))
        self.current_image = ImageTk.PhotoImage(self.blank_img)
        self.display = Label(image=self.current_image, width=500, height=300, bg="#1D1D1D")
        self.move_left_button = Button(
            self.root, text="<", font=("Calibri 20"), bg="#1C1C1C", fg="#FFFFFF", command=self.move_left
        )
        self.move_right_button = Button(
            self.root, text=">", font=("Calibri 20"), bg="#1C1C1C", fg="#FFFFFF", command=self.move_right
        )

        self.create_menu()
        self.refresh()

    def move_left(self):
        if self.current_image_index != 0:
            self.current_image_index -= 1
            self.display_image()

    def move_right(self):
        if self.current_image_index != len(self.image_files) - 1:
            self.current_image_index += 1
            self.display_image()

    def onKeyPress(self, event):
        if event.keycode == 37:
            self.move_left()

        if event.keycode == 39:
            self.move_right()

    def render(self):
        self.root.title("Chrispy Image Viewer")
        self.root.iconbitmap("./favicon.ico")
        self.root.configure(bg="#1D1D1D")

        self.name_label.grid(row=0, column=0, columnspan=3)

        self.display.grid(row=1, column=1)

        # Buttons
        self.move_left_button.grid(row=1, column=0)
        self.move_right_button.grid(row=1, column=2)

        self.root.bind("<KeyPress>", self.onKeyPress)
        self.root.mainloop()

    def create_menu(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)

        file_menu = Menu(menubar, tearoff=False)
        file_menu.add_command(label="Open File(s)", command=self.open_files)
        file_menu.add_command(label="Open Folder", command=self.open_folder, underline=0)
        file_menu.add_command(label="Refresh", command=self.refresh, underline=0)
        file_menu.add_command(label="Exit", command=self.root.destroy, underline=1)
        menubar.add_cascade(label="File", menu=file_menu, underline=0)

    def open_files(self):
        files = filedialog.askopenfilenames(
            filetypes=(
                ("all files accepted", ["*.png", ".jpg", ".ico", ".gif", ".jpeg"]),
                ("png files", "*.png"),
                ("jpg files", "*.jpg"),
                ("jpeg files", "*.jpeg"),
                ("gif files", "*.gif"),
                ("ico files", "*.ico"),
            )
        )
        self.image_files = []
        self.image_files.append(*files)
        self.display_image()

    def open_folder(self):
        new_dir = filedialog.askdirectory()

        if new_dir != "":
            self.img_dir = new_dir
            self.find_images(self.img_dir)

    def refresh(self):
        self.find_images(self.img_dir)

    def find_images(self, dir):

        self.image_files = []
        self.current_image_index = 0

        for item in listdir(dir):
            if isfile(f"{dir}/{item}"):
                if item.lower().endswith((".png", ".jpg", ".jpeg", ".ico", ".gif")):
                    self.image_files.append(f"{dir}/{item}")

        self.display_image()

    def display_image(self):

        try:
            self.name_label.configure(text=self.image_files[self.current_image_index])
            new_img = Image.open(f"{self.image_files[self.current_image_index]}")
            self.current_image = ImageTk.PhotoImage(self.resize_image(new_img))
            self.display.configure(image=self.current_image)

        except OSError as e:
            self.name_label.configure(text=e)
            self.current_image = ImageTk.PhotoImage(self.blank_img)
            self.display.configure(image=self.current_image)

        except IndexError:
            self.name_label.configure(text="No image files found")
            self.current_image = ImageTk.PhotoImage(self.blank_img)
            self.display.configure(image=self.current_image)

    def resize_image(self, image):

        # Use the original aspect ratio of the image to resize
        if image.height > 300:
            aspect_ratio = image.width / image.height
            new_width = aspect_ratio * 300
            return image.resize((int(new_width), 300), Image.Resampling.LANCZOS)

        if image.width > 500:
            aspect_ratio = image.width / image.height
            new_height = 500 * aspect_ratio
            return image.resize((500, int(new_height)), Image.Resampling.LANCZOS)

        return image


ImageViewer().render()
