from tkinter import Tk, Label, Button
from PIL import Image, ImageTk

root = Tk()
root.title("Image Viewer")
root.iconbitmap("./favicon.ico")
root.configure(bg="#1D1D1D")

name_label = Label(root, text="Image1.png", bg="#1D1D1D", fg="#FFFFFF", font=("Arial 18"))
name_label.grid(row=0, column=0, columnspan=3)

# Label for Display
placeholder = ImageTk.PhotoImage(Image.open("./images/image1.png"))
display = Label(image=placeholder, width=500, height=300, bg="#1D1D1D")
display.grid(row=1, column=1)

# Buttons
def move_left():
    print("Move left")

def move_right():
    print("Move right")
move_left_button = Button(root, text="<", font=("Calibri 20"), bg="#1C1C1C", fg="#FFFFFF")
move_left_button.grid(row=1, column=0)
move_right_button = Button(root, text=">", font=("Calibri 20"), bg="#1C1C1C", fg="#FFFFFF")
move_right_button.grid(row=1, column=2)

root.mainloop()