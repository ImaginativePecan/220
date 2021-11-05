"""
Name: Jake Tanner
bumper.py

Problem: create a simulation of bumper cars using graphics objects

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


from random import randint
from graphics import *
import time
import math


win = GraphWin('Bumper', 600, 400)
win_x = 600
win_y = 400


def get_random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    rgb = color_rgb(r, b, g)
    return rgb


one_pos_x = 400
one_pos_y = 200
# creates and draws first ball
ball_one = Circle(Point(one_pos_x, one_pos_y), 60)
ball_one.setFill(get_random_color())
ball_one.setOutline(get_random_color())
ball_one.draw(win)
ball_one.getCenter()
radius_one = ball_one.getRadius()

two_pos_x = 200
two_pos_y = 200
# creates and draws second ball
ball_two = Circle(Point(two_pos_x, two_pos_y), 60)
ball_two.setFill(get_random_color())
ball_two.setOutline(get_random_color())
ball_two.draw(win)
ball_two.getCenter()
radius_two = ball_two.getRadius()


def get_random(move_amount):
    return randint(-move_amount, move_amount)


def balls_move():
    ball_one_x_acc = one_pos_x
    mov_x = get_random(5)
    ball_one_y_acc = one_pos_y
    mov_y = get_random(5)

    while 60 <= ball_one_x_acc <= 340 and 60 <= ball_one_y_acc <= 540:
        ball_one.move(mov_x, -mov_y)
        time.sleep(0.001)
        ball_one_x_acc += mov_x
        ball_one_y_acc -= mov_y
        if hit_horizontal(ball_one_x_acc, win_x - radius_one):
            ball_one.move(-mov_x, -mov_y)
            time.sleep(0.01)
            ball_one_x_acc -= mov_x
            ball_one_y_acc -= mov_y
        if hit_horizontal(ball_one_x_acc, win_x - radius_one):
            ball_one.move(mov_x, -mov_y)
            time.sleep(0.01)
            ball_one_x_acc += mov_x
            ball_one_y_acc -= mov_y
        if hit_vertical(ball_one_y_acc, win_y - radius_one):
            ball_one.move(mov_x, mov_y)
            time.sleep(0.01)
            ball_one_x_acc += mov_x
            ball_one_y_acc += mov_y
        if hit_vertical(ball_one_y_acc, win_y - radius_one):
            ball_one.move(mov_x, -mov_y)
            time.sleep(0.01)
            ball_one_x_acc += mov_x
            ball_one_y_acc -= mov_y

    ball_two_x_acc = two_pos_x
    mov_x = get_random(5)

    ball_two_y_acc = two_pos_y
    mov_y = get_random(5)

    while 60 <= ball_two_x_acc and ball_two_y_acc <= 540:
        ball_two.move(mov_x, -mov_y)
        time.sleep(0.001)
        ball_two_x_acc += mov_x
        ball_two_y_acc -= mov_y
        if hit_horizontal(ball_two_x_acc, win_x - radius_two):
            ball_two.move(-mov_x, -mov_y)
            time.sleep(0.01)
            ball_two_x_acc -= mov_x
            ball_two_y_acc -= mov_y
        if hit_horizontal(ball_two_x_acc, radius_two):
            ball_two.move(mov_x, -mov_y)
            time.sleep(0.01)
            ball_two_x_acc += mov_x
            ball_two_y_acc -= mov_y
        if hit_vertical(ball_two_y_acc, win_y - radius_two):
            ball_two.move(mov_x, mov_y)
            time.sleep(0.01)
            ball_two_x_acc += mov_x
            ball_two_y_acc += mov_y
        if hit_vertical(ball_two_y_acc, radius_two):
            ball_two.move(mov_x, -mov_y)
            time.sleep(0.01)
            ball_two_x_acc += mov_x
            ball_two_y_acc -= mov_y

    if did_collide(ball_one, ball_two):
        if ball_one.move(mov_x, mov_y) and ball_two.move(-mov_x, -mov_y):
            ball_one.move(-mov_x, -mov_y)
            time.sleep(0.01)
            ball_one_x_acc -= mov_x
            ball_one_y_acc -= mov_y

            ball_two.move(mov_x, mov_y)
            time.sleep(0.01)
            ball_two_x_acc += mov_x
            ball_two_y_acc += mov_y

        elif ball_one.move(-mov_x, mov_y) and ball_two.move(-mov_x, -mov_y):
            ball_one.move(mov_x, -mov_y)
            time.sleep(0.01)
            ball_one_x_acc += mov_x
            ball_one_y_acc -= mov_y

            ball_two.move(mov_x, mov_y)
            time.sleep(0.01)
            ball_two_x_acc += mov_x
            ball_two_y_acc += mov_y

        elif ball_one.move(-mov_x, -mov_y) and ball_two.move(-mov_x, -mov_y):
            ball_one.move(mov_x, mov_y)
            time.sleep(0.01)
            ball_one_x_acc += mov_x
            ball_one_y_acc += mov_y

            ball_two.move(mov_x, mov_y)
            time.sleep(0.01)
            ball_two_x_acc += mov_x
            ball_two_y_acc += mov_y

        elif ball_one.move(mov_x, mov_y) and ball_two.move(mov_x, -mov_y):
            ball_one.move(mov_x, mov_y)
            time.sleep(0.01)
            ball_one_x_acc += mov_x
            ball_one_y_acc += mov_y

            ball_two.move(-mov_x, mov_y)
            time.sleep(0.01)
            ball_two_x_acc -= mov_x
            ball_two_y_acc += mov_y

        elif ball_one.move(mov_x, mov_y) and ball_two.move(-mov_x, mov_y):
            ball_one.move(mov_x, mov_y)
            time.sleep(0.01)
            ball_one_x_acc += mov_x
            ball_one_y_acc += mov_y

            ball_two.move(mov_x, -mov_y)
            time.sleep(0.01)
            ball_two_x_acc += mov_x
            ball_two_y_acc -= mov_y

        elif ball_one.move(mov_x, mov_y) and ball_two.move(mov_x, mov_y):
            ball_one.move(-mov_x, -mov_y)
            time.sleep(0.01)
            ball_one_x_acc -= mov_x
            ball_one_y_acc -= mov_y

            ball_two.move(-mov_x, -mov_y)
            time.sleep(0.01)
            ball_two_x_acc -= mov_x
            ball_two_y_acc -= mov_y


def hit_horizontal(ball, win_d):
    if ball == win_d and win_d >= 340:
        print('hit right')
        return True
    elif ball == win_d and win_d <= 60:
        print('hit left')
        return True
    else:
        return False


def hit_vertical(ball, win_d):
    if ball == win_d and win_d >= 540:
        print('hit bottom')
        return True
    elif ball == win_d and win_d <= 60:
        print('hit top')
        return True
    else:
        return False


def did_collide(one_ball, two_ball):
    ball_one_center = one_ball.getCenter()
    b_o_c_x = ball_one_center.getX()
    b_o_c_y = ball_one_center.getY()

    ball_two_center = two_ball.getCenter()
    b_t_c_x = ball_two_center.getX()
    b_t_c_y = ball_two_center.getY()

    balls_dx = abs(b_t_c_x - b_o_c_x)
    balls_dy = abs(b_o_c_y - b_t_c_y)
    ball_distance = math.sqrt(int((balls_dx + balls_dy)) ** 2)

    if ball_distance > radius_one + radius_two:
        return False
    else:
        return True


def close():
    # prompts user to close window and closes the window
    close_msg = Text(Point(300, 375), 'Click anywhere to close')
    close_msg.draw(win)
    win.getMouse()
    win.close()


def main():
    balls_move()
    close()


if __name__ == '__main__':
    main()
