"""
Name: Jake Tanner
three_door_game.py

Problem: create a game in which the user picks between 3 doors

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from hw9.button import Button
from graphics import *
from random import *


def td_game():
    win = GraphWin('3 Door Game', 600, 600)
    button_one = Button(Rectangle(Point(100, 300), Point(200, 350)), 'Door 1')
    button_two = Button(Rectangle(Point(250, 300), Point(350, 350)), 'Door 2')
    button_three = Button(Rectangle(Point(400, 300), Point(500, 350)), 'Door 3')

    button_one.draw(win)
    button_two.draw(win)
    button_three.draw(win)

    headline = Text(Point(300, 100), 'I have a secret door')
    headline.draw(win)

    def door_selection():
        d = randint(1, 3)
        return d

    def selection():
        point = win.getMouse()
        while not(button_one.is_clicked(point) or button_two.is_clicked(point) or button_three.is_clicked(point)):
            try_again = Text(Point(300, 500), 'please select a door')
            try_again.draw(win)
            point = win.getMouse()
            try_again.undraw()

        # winning cases
        if button_one.is_clicked(point) and door_selection() == 1:
            button_one.color_button('green')
            you_win = Text(Point(300, 500), 'You win!')
            you_win.draw(win)
        elif button_two.is_clicked(point) and door_selection() == 2:
            button_two.color_button('green')
            you_win = Text(Point(300, 500), 'You win!')
            you_win.draw(win)
        elif button_three.is_clicked(point) and door_selection() == 3:
            button_three.color_button('green')
            you_win = Text(Point(300, 500), 'You win!')
            you_win.draw(win)

        # losing cases
        elif button_one.is_clicked(point) and (door_selection() == 2 or door_selection() == 3):
            button_one.color_button('red')
            you_lose = Text(Point(300, 450), 'You lose')
            you_lose.draw(win)
            if door_selection() == 2:
                right_door = Text(Point(300, 500), 'The correct door was Door 2')
                button_two.color_button('green')
                right_door.draw(win)
            if door_selection() == 3:
                right_door = Text(Point(300, 500), 'The correct door was Door 3')
                button_three.color_button('green')
                right_door.draw(win)
        elif button_two.is_clicked(point) and (door_selection() == 1 or door_selection() == 3):
            button_two.color_button('red')
            you_lose = Text(Point(300, 450), 'You lose')
            you_lose.draw(win)
            if door_selection() == 1:
                right_door = Text(Point(300, 500), 'The correct door was Door 1')
                button_one.color_button('green')
                right_door.draw(win)
            if door_selection() == 3:
                right_door = Text(Point(300, 500), 'The correct door was Door 3')
                button_three.color_button('green')
                right_door.draw(win)
        elif button_three.is_clicked(point) and (door_selection() == 1 or door_selection() == 2):
            button_three.color_button('red')
            you_lose = Text(Point(300, 450), 'You lose')
            you_lose.draw(win)
            if door_selection() == 1:
                right_door = Text(Point(300, 500), 'The correct door was Door 1')
                button_one.color_button('green')
                right_door.draw(win)
            if door_selection() == 2:
                right_door = Text(Point(300, 500), 'The correct door was Door 2')
                button_two.color_button('green')
                right_door.draw(win)

    selection()
    win.getMouse()
    win.close()


def main():
    td_game()


if __name__ == '__main__':
    main()
