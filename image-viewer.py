from tkinter import Tk, Label, Button, Menu, filedialog
from PIL import Image, ImageTk
from os import listdir
from os.path import isfile

class ImageViewer():
    def __init__(self):
                     
        self.current_image_index = 0
        self.image_files = []
        self.blank_img = Image.new('RGBA',(500,300),(0,0,0,0)) # Blank Image to display if no other images are found   
        self.img_dir = "./images" # Directory to search images in -- by default is the ./images folder

        # Tkinter elements setup
        self.root = Tk()
        self.name_label = Label(self.root, text="No image found", bg="#1D1D1D", fg="#FFFFFF", font=("Arial 18"))
        self.current_image = ImageTk.PhotoImage(self.blank_img)
        self.display = Label(image=self.current_image, width=500, height=300, bg="#1D1D1D")
        self.move_left_button = Button(self.root, text="<", font=("Calibri 20"), bg="#1C1C1C", fg="#FFFFFF", command=self.move_left)
        self.move_right_button = Button(self.root, text=">", font=("Calibri 20"), bg="#1C1C1C", fg="#FFFFFF", command=self.move_right)
                
        # Menu creation
        self.create_menu()
        
        # Refresh the current directory and display images
        self.refresh()
        

    def move_left(self):
        if self.current_image_index != 0 and len(self.image_files) != 0:
            self.current_image_index -= 1
            self.display_image()

    def move_right(self):
        if self.current_image_index != len(self.image_files) - 1 and len(self.image_files) != 0:
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
        
    # Menu creation
    def create_menu(self):
        menubar = Menu(self.root) # Create the main Menu bar
        self.root.config(menu=menubar) # Attach the Menu bar to the main root window
        
        file_menu = Menu(menubar, tearoff=False) # Create the 'File' sub menu
        file_menu.add_command(label='Open Folder', command=self.open_folder, underline=0) # Open Folder
        file_menu.add_command(label='Refresh', command=self.refresh, underline=0) # Refresh the current folder
        file_menu.add_command(label='Exit', command=self.root.destroy, underline=1) # Add the Exit button to the File menu
        menubar.add_cascade(label='File', menu=file_menu, underline=0) # Display the File button on the menu bar
    
    # Open the explorer and choose a new folder    
    def open_folder(self):
        self.img_dir = filedialog.askdirectory()
        self.find_images(self.img_dir)
    
    # Refresh the current directory, incase images have been added or removed
    def refresh(self):
        self.find_images(self.img_dir)
    
    # Find images in input directory and append to image_files list    
    def find_images(self, dir):
        
        # Clear current list of images and reset index
        self.image_files = []
        self.current_image_index = 0
        
        for item in listdir(dir):
            if isfile(f"{dir}/{item}"):
                # Only add image items with the following extensions
                if(item.lower().endswith(('.png', '.jpg', '.jpeg', '.ico', '.gif', '.svg'))):
                    self.image_files.append(item)
                
        # Display
        self.display_image()

    # Display image at the current index
    def display_image(self):
        
        try:
            self.name_label.configure(text=self.image_files[self.current_image_index]) # Update the Label
            new_img = Image.open(f"{self.img_dir}/{self.image_files[self.current_image_index]}") # Open the image
            self.current_image = ImageTk.PhotoImage(self.resize_image(new_img)) # Resize and load the image
            self.display.configure(image=self.current_image) # Display the image
            
        except:            
            # No images were found - so change the label and display a blank image
            self.name_label.configure(text="No image found")
            self.current_image = ImageTk.PhotoImage(self.blank_img)
            self.display.configure(image=self.current_image)
    
    # Resize the images for display
    # Currently fixes the height to 300 pixels and adjusts the width, keeping the original aspect ratio to avoid stretching the image
    def resize_image(self, image):
        aspect_ratio = image.width / image.height
        new_width = aspect_ratio * 300
        return image.resize((int(new_width), 300), Image.Resampling.LANCZOS)

ImageViewer().render()