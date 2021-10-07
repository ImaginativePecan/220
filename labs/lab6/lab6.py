"""
Name: Jake Tanner
lab6.py
"""


def name_reverse():
    name = input("Please enter your name: ")
    name = name.split()
    print(name[1] + ', ' + name[0])


def company_name():
    domain = input("Please enter the three part website domain: ")
    domain = domain.split('.')
    print(domain[1])


def initial():
    name = eval(input("Please enter how many student names you will enter: "))
    for i in range(name):
        first_name = input("Please enter the first name of student " + str(i + 1) + ": ")
        last_name = input("Please enter " + first_name + "\'s last name: ")
        print(first_name + "\'s initials are: " + first_name[0] + last_name[0])


def names():
    all_names = input("Please enter the list of names separated by a comma followed by a space: ")
    all_names = all_names.split(", ")
    for name in all_names:
        individual_name = name.split()
        print("The initials for the names entered are: " + individual_name[0][0] + individual_name[1][0])


def thirds():
    num_sentences = eval(input("How many sentences will there be entered: "))
    for i in range(num_sentences):
        sentence = input("Please enter the sentence: ")
        print(sentence[2::3])


def word_average():
    sentence = input("Please enter the sentence: ")
    accumulator = 0
    sentence = sentence.split()
    for word in sentence:
        accumulator = accumulator + len(word)
    print(accumulator / len(sentence))


def pig_latin():
    sentence = input("Please enter the sentence to be converted: ")
    sentence = sentence.lower()
    sentence = sentence.split()
    for word in sentence:
        print(word[1:] + word[0] + "ay", end=" ")


def main():
    name_reverse()
    company_name()
    initial()
    names()
    thirds()
    word_average()
    pig_latin()


main()
