from tkinter import Image
from PIL import ImageTk
from Image_Viewer.orchestrator import Orchestrator
from Image_Viewer.theme import Theme

class Renderer(Orchestrator):
    def render(self):
        self.root.title("Chrispy Image Viewer")
        self.root.tk.call("wm", "iconphoto", self.root._w, ImageTk.PhotoImage(file="Image_Viewer/favicon.ico"))
        themeObj=Theme()
        print(themeObj.themes[themeObj.currentTheme])
        self.set_theme(**themeObj.themes[themeObj.currentTheme])

        self.name_label.place(relx=0,rely=0,relheight=0.05,relwidth=1)
        self.display.place(relx=0.175,rely=0.2,relheight=0.5,relwidth=0.625)

        # Buttons
        self.move_left_button.place(relx=0,rely=0.45,relheight=0.1,relwidth=0.1)
        self.move_right_button.place(relx=0.9,rely=0.45,relheight=0.1,relwidth=0.1)

        self.root.bind("<KeyPress>", self.onKeyPress)
        self.root.mainloop()