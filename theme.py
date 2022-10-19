class Theme:
    
    def set_theme(self, background, foreground, buttonBackground):
            self.root.configure(bg=background)
            self.name_label.configure(bg=background, fg=foreground)
            self.display.configure(bg=background)
            self.move_left_button.configure(bg=buttonBackground, fg=foreground)
            self.move_right_button.configure(bg=buttonBackground, fg=foreground)