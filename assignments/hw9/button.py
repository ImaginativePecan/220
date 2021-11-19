from graphics import *
from random import *


class Button:
    def __init__(self, shape, label):
        self.shape = shape
        self.text = label

    def get_label(self):
        return str(self.text)

    def draw(self, win):
        self.shape.draw(win)
        button_loc = self.shape.getCenter()
        self.text = Text(Point(button_loc.getX(), button_loc.getY()), self.get_label())
        self.text.draw(win)

    def undraw(self):
        return self.shape.undraw(), self.text.undraw()

    def is_clicked(self, point):
        x, y = point.getX(), point.getY()
        button_loc = self.shape.getCenter()
        if button_loc.getX() + 50 >= x >= button_loc.getX() - 50 and \
                button_loc.getY() + 25 >= y >= button_loc.getY() - 25:
            return True
        return False

    def color_button(self, color):
        self.shape.setFill(color)

    def set_label(self, label):
        pass
