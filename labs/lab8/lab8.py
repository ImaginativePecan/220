"""
Name: Jake Tanner
lab8.py
"""


from encryption import encode, encode_better


def number_words(in_file_name, out_file_name):
    infile = open(in_file_name, 'r')
    outfile = open(out_file_name, 'w+')
    i = 1
    for line in infile:
        words = line.split()
        for word in words:
            outfile.write(str(i) + ' ' + word + '\n')
            i += 1


def hourly_wages(in_file_name, out_file_name):
    infile = open(in_file_name, 'r')
    outfile = open(out_file_name, 'w+')
    for line in infile:
        parts = line.split()
        wage = float(parts[2])
        pay = wage * int(parts[3])
        raised_pay = pay * 1.65
        outfile.write(parts[0] + ' ' + parts[1] + ' ' + str(raised_pay) + '\n')


def calc_check_sum(isbn) -> int:
    accumulator = 0
    for i in range(10):
        position = 10 - i
        accumulator += (position * int(isbn[i]))
    return accumulator


def send_message(file, friend):
    infile = open(file, 'r')
    outfile = open(friend + '.txt', 'w+')
    for line in infile:
        outfile.write(line)


def send_safe_message(file, friend, key):
    infile = open(file, 'r')
    outfile = open(friend + '_safe.txt', 'w+')
    accumulator = ' '
    for line in infile:
        accumulator += line
    outfile.write(str(encode(accumulator, key)))


def send_uncrackable_message(file, friend, pad):
    infile = open(file, 'r')
    outfile = open(friend + '_uncrackable.txt', 'w+')
    pad_file = open(pad, 'r')
    key = pad_file.read()
    accumulator = ' '
    for line in infile:
        accumulator += line

    outfile.write(str(encode_better(accumulator, key)))


def main():
    # add other function calls here
    number_words('walrus.txt', 'walrus_output.txt')
    hourly_wages('hourly_wages.txt', 'hourly_wages_output.txt')
    print(calc_check_sum('0072946520'))
    send_message('message.txt', 'bob')
    send_safe_message('secret_message.txt', 'bob', 3)
    send_uncrackable_message('safest_message.txt', 'bob', 'pad.txt')


main()
