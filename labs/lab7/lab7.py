"""
Name: Jake Tanner
lab7.py
"""

import math


# This function converts an integer into a dollar amount
def cash_conversion():
    integer = eval(input('Please enter the integer value: '))
    print('$' + '{:.2f}'.format(integer))


def encode():
    message = input('Please enter the message you wish to encode: ')
    key = eval(input('Please enter your key value: '))
    accumulator = ' '
    for c in message:
        i = ord(c)
        i += key
        c = chr(i)
        accumulator += c
    print(accumulator)


def sphere_area(radius):
    area = 4 * math.pi * (radius ** 2)
    return area


def sphere_volume(radius):
    volume = (4/3) * math.pi * (radius ** 3)
    return volume


def sum_n(n):
    total = 0
    for i in range(n):
        total += i
    return total


def sum_n_cubes(n):
    total_c = 0
    for i in range(n):
        total_c += (i ** 3)
    return total_c


def encode_better():
    message = input('Please enter the message you wish to encode: ')
    key = (input('Please enter the key: '))
    accumulator = ' '
    for i in range(len(message)):
        c = message[i]
        k = key[i % len(key)]
        c = ord(c)
        k = ord(k) - 97
        i = c
        i += k
        c = chr(i)
        accumulator += c
    print(accumulator)


def main():
    # add function calls here
    cash_conversion()
    encode()
    print(sphere_area(2))
    print(sphere_volume(4))
    print(sum_n(6))
    print(sum_n_cubes(8))
    encode_better()


main()
