"""

Name: Jake Tanner
lab2.py

"""


import math


def sum_of_threes():
    u_bound = eval(input("Please enter the upper bound: "))
    accumulator = 0
    for i in range(0, u_bound + 1, 3):
        accumulator = accumulator + i
    print(accumulator)


sum_of_threes()


def multiplication_table():
    for height in range(1, 11):
        for length in range(1, 11):
            print(height * length, end=" ")
        print()


multiplication_table()


def triangle_area():
    side_a = eval(input("Please enter the length of side A: "))
    side_b = eval(input("Please enter the length of side B: "))
    side_c = eval(input("Please enter the length of side C: "))
    s = (side_a + side_b + side_c) / 2
    area = s * (s - side_c) * (s - side_b) * (s - side_a)
    area = math.sqrt(area)
    print("The area of the triangle is:", area)


triangle_area()


def sumSquares():
    lower_bound = eval(input("Please enter a lower bound: "))
    upper_bound = eval(input("Please enter an upper bound: "))
    accumulator = 0
    for i in range(lower_bound, upper_bound + 1):
        accumulator = accumulator + i ** 2
    print(accumulator)


sumSquares()


def power():
    accumulator = 1
    base = eval(input("Please enter the base number: "))
    base_power = eval(input("Please enter the power: "))
    for i in range(base_power):
        accumulator = accumulator * base
    print(base, "^", base_power, "=", accumulator)


power()
