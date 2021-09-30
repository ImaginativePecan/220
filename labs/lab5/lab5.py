"""
Name: <your name goes here – first and last>
<ProgramName>.py
"""

import math
from graphics import *


def target():
    win_width = 500
    win_height = 500
    win = GraphWin("Archery Target", win_width, win_height)

    # Add code here to get the dimensions and draw the target
    circ_w = Circle(Point(250, 250), 250)
    circ_w.setFill("white")
    circ_w.draw(win)

    circ_b = Circle(Point(250, 250), 200)
    circ_b.setFill("black")
    circ_b.draw(win)

    circ_bl = Circle(Point(250, 250), 150)
    circ_bl.setFill("blue")
    circ_bl.draw(win)

    circ_r = Circle(Point(250, 250), 100)
    circ_r.setFill("red")
    circ_r.draw(win)

    circ_y = Circle(Point(250, 250), 50)
    circ_y.setFill("yellow")
    circ_y.draw(win)

    message = Text(Point(250, 25), "Click to close")
    message.draw(win)

    # Wait for another click to exit
    win.getMouse()
    win.close()


def triangle():
    win_width = 500
    win_height = 500
    win = GraphWin("Draw a Triangle", win_width, win_height)

    message = Text(Point(250, 25), "Click on three points")
    message.draw(win)

    p1 = win.getMouse()
    p2 = win.getMouse()
    p3 = win.getMouse()
    triangle = Polygon(p1, p2, p3)
    triangle.setFill("blue")
    triangle.draw(win)

    p1_x = p1.getX()
    p1_y = p1.getY()

    p2_x = p2.getX()
    p2_y = p2.getY()

    p3_x = p3.getX()
    p3_y = p3.getY()

    dx12 = abs(p2_x - p1_x)
    dy12 = abs(p2_y - p1_y)

    dx13 = abs(p3_x - p1_x)
    dy13 = abs(p3_y - p1_y)

    dx23 = abs(p3_x - p2_x)
    dy23 = abs(p3_y - p2_y)

    l_12 = math.sqrt(int((dx12 + dy12)) ** 2)
    l_13 = math.sqrt(int((dx13 + dy13)) ** 2)
    l_23 = math.sqrt(int((dx23 + dy23)) ** 2)

    perimeter = int(l_12 + l_13 + l_23)
    s = perimeter / 2

    a1 = int(s-l_12)
    a2 = int(s-l_13)
    a3 = int(s-l_23)
    inside = s * a1 * a2 * a3
    area = math.sqrt(inside)

    p_message = Text(Point(250, 450), "The perimeter is: " + str(perimeter))
    a_message = Text(Point(250, 470), "The area is: " + str(round(area, 2)))
    p_message.draw(win)
    a_message.draw(win)

    win.getMouse()
    win.close()


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    red_box = Entry(Point((win_width / 2), ((win_height / 2) + 40)), 5)
    green_box = Entry(Point((win_width / 2), ((win_height / 2) + 70)), 5)
    blue_box = Entry(Point((win_width / 2), ((win_height / 2) + 100)), 5)

    red_box.draw(win)
    green_box.draw(win)
    blue_box.draw(win)

    for i in range(5):
        win.getMouse()
        red = int(red_box.getText())
        green = int(green_box.getText())
        blue = int(blue_box.getText())
        color = color_rgb(red, green, blue)
        shape.setFill(color)

    # Wait for another click to exit
    win.getMouse()
    win.close()


def process_string():
    s = input("Please enter your string: ")
    print(s[0])
    print(s[-1])
    print(s[2: 6])
    print((s[0] + s[-1]))
    print((s[:3] * 10))
    for c in s:
        print(c, end=" ")
    print()
    print(len(s))


def list_processing():
    pt = Point(5, 10)
    values = [5, "hi ", 2.5, "there", pt, "7.2"]

    x = values[1] + values[3]
    print(x)

    x = int(values[0] + values[2])
    print(x)

    x = values[1] * 5
    print(x)

    x = values[2: 5]
    print(x)

    x = [values[2], values[4], values[0]]
    print(x)

    x = values[0] + values[2] + float(values[5])
    print(x)

    x = len(values)
    print(x)


def another_series():
    num = eval(input("Please enter the number of terms: "))
    acc = 0
    for i in range(num):
        y = 2 + 2 * (i % 3)
        print(y, end=" ")
        acc = acc + y
    print()
    print("Sum =", acc)


def main():
    target()
    triangle()
    color_shape()
    process_string()
    list_processing()
    another_series()


main()
