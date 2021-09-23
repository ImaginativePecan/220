"""
Name: Jake Tanner
lab4.py
"""

import math
from graphics import *


def squares():
    """  <---  You can use tripled quotes to write a multi-line comment....

    Modify the following function to:

    Draw squares (20 X 20) instead of circles. Make sure that the center of the square
    is at the point where the user clicks. Make the window 400 by 400.

    Have each successive click draw an additional square on the screen (rather
    than just moving the existing one).

    Display a message on the window "Click again to quit" after the loop, and
    wait for a final click before closing the window.
    """

    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to move square")
    instructions.draw(win)

    # builds a circle
    shape = Rectangle(Point(50, 50), Point(70, 70))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to create new squares
    for i in range(num_clicks):
        p = win.getMouse()
        shape = Rectangle(Point(p.getX() - 10, p.getY() - 10), Point(p.getX() + 10, p.getY() + 10))
        shape.setOutline("red")
        shape.setFill("red")
        shape.draw(win)

    # removes instructions to draw, and then changes to ending instructions
    instructions.undraw()
    instructions.setText("Click to Close")
    instructions.draw(win)

    win.getMouse()
    win.close()


def rectangle():
    """
    This program displays information about a rectangle drawn by the user.
    Input: Two mouse clicks for the opposite corners of a rectangle.
    Output: Draw the rectangle.
         Display the perimeter and area of the rectangle.
    Formulas: area = (length)(width)   and    perimeter = 2(length+width)
    """

    # creates a window
    win = GraphWin("Rectangle", 400, 400)

    # sets variables as window size
    height_win = 400
    width_win = 400

    # displays prompt for user to click
    inst_pt = Point(width_win / 2, height_win - 30)
    input_text = Text(inst_pt, "Please click two different points to create a rectangle")
    input_text.draw(win)

    # creates rectangle with user input for corners
    p1 = win.getMouse()
    p2 = win.getMouse()
    rect = Rectangle(p1, p2)
    rect.setOutline("black")
    rect.setFill("green")
    rect.draw(win)

    # removes prompt message
    input_text.undraw()

    # calculates length and width of rectangle
    length = abs(p2.getY() - p1.getY())
    width = abs(p2.getX() - p1.getX())

    # calculates and displays perimeter
    perimeter = 2 * (length * width)
    inst_pt = Point(width_win / 2, height_win - 50)
    perimeter_text = Text(inst_pt, "The perimeter is " + str(perimeter))
    perimeter_text.draw(win)

    # calculates and displays area
    area = length * width
    inst_pt = Point(width_win / 2, height_win - 30)
    area_text = Text(inst_pt, "The area is " + str(area))
    area_text.draw(win)

    # displays message to close window
    inst_pt = Point(width_win / 2, height_win - 10)
    close_text = Text(inst_pt, "Please click to close window")
    close_text.draw(win)

    # closes window
    win.getMouse()
    win.close()


def circle():

    # creates a window
    win = GraphWin("Circle", 400, 400)

    # sets variables as window size
    height_win = 400
    width_win = 400

    # displays prompt for user to click
    inst_pt = Point(width_win / 2, height_win - 30)
    input_text = Text(inst_pt, "Please click two different points to create a circle")
    input_text.draw(win)

    # gets user clicks and position values
    p1 = win.getMouse()
    p2 = win.getMouse()
    x1 = p1.getX()
    x2 = p2.getX()
    y1 = p1.getY()
    y2 = p2.getY()

    # removes prompt message
    input_text.undraw()

    # calculates the radius using the distance formula
    radius = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))

    # draws the circle using the points clicked by user
    circ = Circle(p1, radius)
    circ.draw(win)
    circ.setOutline("black")
    circ.setFill("blue")

    # displays the radius
    inst_pt = Point(width_win / 2, height_win - 30)
    radius_text = Text(inst_pt, "The radius of the circle is " + str(radius))
    radius_text.draw(win)

    # displays message to close window
    inst_pt = Point(width_win / 2, height_win - 10)
    close_text = Text(inst_pt, "Please click to close window")
    close_text.draw(win)

    # closes window
    win.getMouse()
    win.close()


def pi2():

    # asks user for how number of terms
    num_terms = eval(input("Please enter the number of terms to sum: "))

    # calculates sum of terms
    accumulator = 0
    for i in range(num_terms):
        numerator = 4 * ((-1) ** i)
        denominator = 1 + (2 * i)
        accumulator = accumulator + (numerator / denominator)

    # outputs the sum for the amount of terms
    final_value = math.pi - accumulator
    print("The final value for " + str(num_terms) + " is " + str(final_value))


def main():
    squares()
    rectangle()
    circle()
    pi2()


if __name__ == '__main__':
    main()
