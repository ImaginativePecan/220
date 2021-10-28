"""
Name: Jake Tanner
lab9.py
"""

from graphics import *
import math


def addTens(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] + 10


def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2


def sumList(nums):
    total_sum = 0
    for i in range(len(nums)):
        total_sum += nums[i]
    return total_sum


def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = float(strList[i])


def writeSumofSquares():
    in_file_name = input('Please enter the name of the file to get the values from: ')
    infile = open(in_file_name, 'r')
    outfile = open('sum_of_squares_output.txt', 'w+')
    for line in infile:
        interested_line = line.split()
        toNumbers(interested_line)
        squareEach(interested_line)
        total_sum = sumList(interested_line)
        outfile.write('Sum = ' + str(total_sum) + '\n')


def starter():
    weight = eval(input('Please enter the weight of the wrestler: '))
    wins = eval(input('Please enter the number of wins the wrestler has: '))
    if 150 <= weight < 160 and wins >= 5:
        print('The wrestler is a starter')
    elif weight > 199 or wins > 20:
        print('The wrestler is a starter')
    else:
        print('The wrestler is not a starter')


def leapYear(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def circleOverlap():
    win = GraphWin('Circle Overlap', 400, 400)
    p1 = win.getMouse()
    p2 = win.getMouse()
    radius1 = math.sqrt((p2.getX() - p1.getX()) ** 2 + (p2.getY() - p1.getY()) ** 2)
    circle1 = Circle(p1, radius1)
    circle1.draw(win)

    p3 = win.getMouse()
    p4 = win.getMouse()
    radius2 = math.sqrt((p4.getX() - p3.getX()) ** 2 + (p4.getY() - p3.getY()) ** 2)
    circle2 = Circle(p3, radius2)
    circle2.draw(win)

    distance = math.sqrt((p3.getX() - p1.getX()) ** 2 + (p3.getY() - p1.getY()) ** 2)
    if distance <= radius1 + radius2:
        print('The circles overlap')
    else:
        print('The circles do not overlap')

    win.getMouse()
    win.close()


def main():
    addTens([5, 2, -3])
    squareEach([3, 5.7, 2])
    sumList([3, 5.7, 2])
    toNumbers(['3', '5.7', '2'])
    writeSumofSquares()
    starter()
    leapYear(2008)
    circleOverlap()


main()
