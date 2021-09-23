"""
Name: Jake Tanner
mean.py

Problem: this program computes several different means

Certificate of Authenticity:
I certify that this assignment is entirely  of my own work.
"""

import math

# What will the program do?
#
# The program should calculate the mean of x amount of numbers using three different methods
#
# What will be the inputs and outputs?
#
# The user will input the amount of numbers to take the mean of, the numbers to take the mean
# and the program will output the mean of those numbers, using 3 different methods
#
# What is a step-by-step list of what the program must do, aka an algorithm?
#
# 1) ask how many values and store as variable
# 2) function to ask values 1 by 1
# 3) store the values using variables for each mean calculation
# 4) equation to calculate rms average
# 5) equation to calculate harmonic mean
# 6) equation to calculate geometric mean
# 7) print out all the means


def main():

    # gets all the values from the user
    num_values = eval(input("Please enter the amount of values to calculate the mean for: "))
    rms_total = 0
    harmonic_total = 0
    geometric_total = 1
    for i in range(1, num_values + 1):
        values = eval(input("Please enter value " + str(i) + ": "))
        rms_total = rms_total + (values ** 2)
        harmonic_total = harmonic_total + (1 / values)
        geometric_total = geometric_total * values

    # calculates the rms average
    rms_average = math.sqrt(rms_total / num_values)

    # calculates the harmonic mean
    harmonic_mean = (num_values / harmonic_total)

    # calculates the geometric mean
    geometric_mean = geometric_total ** (1 / num_values)

    # prints the rms average
    print(round(rms_average, 3))

    # prints the harmonic mean
    print(round(harmonic_mean, 3))

    # prints the geometric mean
    print(round(geometric_mean, 3))


if __name__ == '__main__':
    main()
