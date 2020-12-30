from tkinter import Tk, Label, Button
from PIL import Image, ImageTk
from os import listdir
from os.path import isfile

class ImageViewer():
    def __init__(self):
        self.current_image_index = 0
        self.image_files = []

        for item in listdir("./images"):
            if isfile(f"./images/{item}"):
                self.image_files.append(item)

        self.root = Tk()
        self.name_label = Label(self.root, text=self.image_files[self.current_image_index], bg="#1D1D1D", fg="#FFFFFF", font=("Arial 18"))
        self.current_image = ImageTk.PhotoImage(Image.open(f"./images/{self.image_files[self.current_image_index]}"))
        self.display = Label(image=self.current_image, width=500, height=300, bg="#1D1D1D")
        self.move_left_button = Button(self.root, text="<", font=("Calibri 20"), bg="#1C1C1C", fg="#FFFFFF", command=self.move_left)
        self.move_right_button = Button(self.root, text=">", font=("Calibri 20"), bg="#1C1C1C", fg="#FFFFFF", command=self.move_right)

    def move_left(self):
        if self.current_image_index != 0:
            self.current_image_index -= 1
            self.name_label.configure(text=self.image_files[self.current_image_index])
            self.current_image = ImageTk.PhotoImage(Image.open(f"./images/{self.image_files[self.current_image_index]}"))
            self.display.configure(image=self.current_image)

    def move_right(self):
        if self.current_image_index != len(self.image_files) - 1:
            self.current_image_index += 1
            self.name_label.configure(text=self.image_files[self.current_image_index])
            self.current_image = ImageTk.PhotoImage(Image.open(f"./images/{self.image_files[self.current_image_index]}"))
            self.display.configure(image=self.current_image)

    def onKeyPress(self, event):
        if event.keycode == 37:
            self.move_left()
        
        if event.keycode == 39:
            self.move_right()

    def render(self):
        self.root.title("Image Viewer")
        self.root.iconbitmap("./favicon.ico")
        self.root.configure(bg="#1D1D1D")
        
        self.name_label.grid(row=0, column=0, columnspan=3)

        self.display.grid(row=1, column=1)

        # Buttons
        self.move_left_button.grid(row=1, column=0)
        self.move_right_button.grid(row=1, column=2)

        self.root.bind("<KeyPress>", self.onKeyPress)
        self.root.mainloop()

ImageViewer().render()