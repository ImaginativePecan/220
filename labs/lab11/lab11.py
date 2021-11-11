"""
Name: Jake Tanner
lab11.py
"""


import random


def read_word(file):
    word_list = []
    infile = open(file, 'r')
    for _ in range(10):
        line = infile.readline()
        word = line.split('\n')
        word_list.append(word[0])

    return word_list


def pick_word(w_list):
    secret_word = random.choice(w_list)

    return str(secret_word)


def guess_word(file):
    word = pick_word(read_word(file))
    print(word)
    letters = []
    for c in word:
        letters += c
    print(letters)

    num_blanks = len(word)
    blanks = ''
    for i in range(num_blanks):
        blanks += '_ '

    blanks_list = blanks.split()
    print(blanks)

    x = 0
    wrong_guess = []
    while x < 7:
        if game_over(''.join(blanks_list), word):
            break
        else:
            # print('you have 7 guesses left')
            player_input = input('choose a letter to guess: ')
            while len(player_input) > 1:
                print('please only enter one character at a time')
                break
            guess = player_input.lower()
            pos = 0
            found = False
            for i in letters:
                if guess == letters[pos]:
                    blanks_list[pos] = guess
                    found = True
                if not found and len(letters)-1 == pos and not guess == letters[pos]:
                    wrong_guess.append(guess)
                    x += 1

                pos += 1

            guess_left = 7 - x
            print('incorrect answers: ' + ', '.join(wrong_guess))
            print('you have ' + str(guess_left) + ' guesses left')
            print(' '.join(blanks_list))
            print()
            if guess_left == 0:
                print('sorry, you lost')


def game_over(original, answer):
    if ''.join(original) == answer:
        print('Congratulations, you won!')
        return True

    if not ' '.join(original) == answer:
        return False


def play_game(file):
    print('welcome to hangman!')
    start = input('press any key to start')
    guess_word(file)


def main():
    play_game('words.txt')


main()
