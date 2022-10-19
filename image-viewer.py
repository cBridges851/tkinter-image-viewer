from renderer import Renderer
from menu import AppMenu
from tkinter import Tk, Label, Button
from PIL import Image, ImageTk

class ImageViewer(Renderer, AppMenu):
    def __init__(self):
        
        default_directory = "./images"
        self.current_image_index = 0
        self.image_files = []
        self.blank_img = Image.new("RGBA", (500, 300), (0, 0, 0, 0))
        self.img_dir = default_directory
        self.open_mode = "folder"
        
        self.root = Tk()
        self.root.geometry("800x600+500+250")                  # window_Width x window_Height + x_Position on screen + y_Position on screen (Unit: Pixel)
        self.root.resizable(height=False,width=False)
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
        

if __name__ == '__main__':
    ImageViewer().render()