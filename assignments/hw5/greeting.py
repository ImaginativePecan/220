"""
Name: Jake Tanner
greeting.py

Problem: this program creates a greeting card using graphics

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


from graphics import GraphWin, Point, Text, Polygon, Oval

import time


def main():
    win = GraphWin('Greeting Card', 500, 500)
    win.setBackground('light blue')

    # displays the message
    begin_text = Text(Point(250, 30), 'Happy Valentine\'s day')
    begin_text.draw(win)

    # waits for user click to start the animation
    ani_text = Text(Point(250, 470), 'Click to start animation')
    ani_text.draw(win)

    # draws shaft
    shaft = Polygon(Point(85, 405), Point(20, 470), Point(30, 480), Point(95, 415))
    shaft.setFill('grey')
    shaft.draw(win)

    # draws arrow
    arrow = Polygon(Point(75, 400), Point(100, 400), Point(100, 425))
    arrow.setFill('black')
    arrow.draw(win)

    # draws first oval for left hump of heart
    l_hump = Oval(Point(340, 100), Point(280, 140))
    l_hump.setOutline('pink')
    l_hump.setFill('pink')
    l_hump.draw(win)

    # draws second oval for right hump of heart
    r_hump = Oval(Point(400, 100), Point(340, 140))
    r_hump.setOutline('pink')
    r_hump.setFill('pink')
    r_hump.draw(win)

    # draws triangle for bottom part of heart
    bottom = Polygon(Point(280, 120), Point(400, 120), Point(340, 250))
    bottom.setOutline('pink')
    bottom.setFill('pink')
    bottom.draw(win)

    # begins animation
    win.getMouse()

    for i in range(400):
        shaft.move(1, -1)
        arrow.move(1, -1)
        time.sleep(0.008)

    begin_text.undraw()
    ani_text.undraw()
    close_text = Text(Point(250, 470), 'Click anywhere to close')
    close_text.draw(win)
    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
