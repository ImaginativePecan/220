"""
Name: Jake Tanner
lab12.py
"""

from random import randint


def find_and_remove_first(list, value):
    try:
        i = list.index(value)
        print(list)
        list[i] = 'Jake'
        print(list)

    except:
        pass


def read_data(filename):
    file = open(filename, 'r')
    data = file.read()
    data = data.split()
    i = 0
    while i < len(data):
        data[i] = int(data[i])
        i += 1
    return data


def is_in_linear(search_val, values):
    i = 0
    while i < len(values):
        if search_val == i:
            return True
        i += 1

    return False


def good_input():
    x = eval(input('enter a value between 1 and 20:'))
    while not(1 <= x <= 20):
        x = eval(input('enter a value between 1 and 20: '))
    return x


def num_digits():
    num = eval(input('enter a number: '))
    while num >= 1:
        digits = 0
        while num > 0:
            num //= 10
            digits += 1
        print('There were ' + str(digits) + ' digits')


def hi_lo_game():
    num = randint(1, 100)
    print(num)
    guesses = 0
    print('you have seven guesses')
    guess = eval(input('take your first guess: '))
    while guess != num and guesses != 7:
        guesses += 1
        if num < guess:
            print('too high')

        elif num > guess:
            print('too low')

        if guess != num and guesses != 7:
            guess = eval(input('take your next guess: '))
        if guess == num:
            print('You picked the correct answer,', str(num), 'in', str(guesses + 1), 'guesses')
        elif guesses == 7:
            print('sorry you lost, the actual number was:', num)


def main():
    find_and_remove_first(['1', 3, 53, 'name', 'hawk', 0], 3)
    print(read_data('numbers.txt'))
    print(is_in_linear(3, ['1', 3, 53, 'name', 'hawk', 0]))
    good_input()
    num_digits()
    hi_lo_game()


main()
