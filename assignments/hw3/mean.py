"""
Name: Jake Tanner
mean.py

Problem: this program computes several different means

Certificate of Authenticity:
I certify that this assignment is entirely  of my own work.
"""

"""
What will the program do?
The program should calculate the mean of x amount of numbers using three different methods

What will be the inputs and outputs?
The user will input numbers to take the mean and the program will output the mean
of those numbers, using 3 different methods

What is a step-by-step list of what the program must do, aka an algorithm?
ask how many values and store as variable
function to ask values 1 by 1
add all the values together and store as variable
function to calculate rms average
function to calculate harmonic mean
function to calculate geometric mean
print out all the means
"""

def main():
    num_values = eval(input("Please enter the amount of values to calculate the mean for: "))
    total = 0
    for values in range(1, num_values + 1):
        sum_values = eval(input("Please enter value " + str(values) + ": "))
        total = total + sum_values
        values = values + 1
    print(total / num_values)


if __name__ == '__main__':
    main()
