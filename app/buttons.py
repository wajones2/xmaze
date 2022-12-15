

class Buttons:
    def __init__(self):
        pass

    def button_labels(self):
        self.A_BUTTON = 0
        self.B_BUTTON = 1
        self.X_BUTTON = 2
        self.Y_BUTTON = 3
        self.LB_BUTTON = 4
        self.RB_BUTTON = 5
        self.LTS_BUTTON = 6
        self.RTS_BUTTON = 7
        self.MENU_BUTTON = 8
        self.XBOX_BUTTON = 9
        self.START_BUTTON = 10

xm_btns = Buttons()
xm_btns.button_labels()

# event.button == 0     'A'
# event.button == 1     'B'
# event.button == 2     'X' 
# event.button == 3     'Y'
# event.button == 4      Left Bumper
# event.button == 5      Right Bumper
# event.button == 6    Left Thumstick
# event.button == 7    Right Thumstick
# event.button == 8     'Menu'
# event.button == 9     Xbox Button
# event.button == 10    'Start'
