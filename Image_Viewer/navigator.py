from Image_Viewer.image_handler import ImageHandler

class Navigator(ImageHandler):
    def move_left(self):
        if self.current_image_index != 0:
            self.current_image_index -= 1
            self.display_image()

    def move_right(self):
        if self.current_image_index != len(self.image_files) - 1:
            self.current_image_index += 1
            self.display_image()