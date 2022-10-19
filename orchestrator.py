from navigator import Navigator

class Orchestrator(Navigator):
    
    def onKeyPress(self, event):
        if event.keycode == 37:
            self.move_left()

        if event.keycode == 39:
            self.move_right()