"""
Name: Jake Tanner
weighted_average.py

Problem: calculates the weighted average and outputs to a file from an input file with grades and names

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def weighted_average(in_file_name, out_file_name):
    # open both files
    infile = open(in_file_name, 'r')
    outfile = open(out_file_name, 'w+')

    # stores the total average
    total_average = 0
    total_grades = 0
    for line in infile:
        # get the names
        line_l = line.split(':')
        # print(line_l)
        name = line_l[0] + '\'s average: '

        # get the weights and grades
        g_and_w_l = line_l[1]
        g_and_w_l = g_and_w_l.split()
        weights = g_and_w_l[0::2]
        grades = g_and_w_l[1::2]

        # calculate average
        average = 0
        x = 0
        total_weight = 0
        for i in range(len(grades)):
            grade = int(grades[x])
            weight = int(weights[x])
            total_weight += weight
            points = (grade * weight) / 100
            average += points
            x = x + 1

        if total_weight == 100:
            outfile.write(name + str(round(average, 1)) + '\n')
            total_average += average
            total_grades += 1
        elif total_weight > 100:
            outfile.write(name + 'Error: The weights are more than 100. \n')
        elif total_weight < 100:
            outfile.write(name + 'Error: The weights are less than 100. \n')
        else:
            outfile.write('something went wrong \n')
    total_average = round(total_average / total_grades, 1)
    outfile.write('Class average: ' + str(total_average))


def main():
    weighted_average('grades.txt', 'avg.txt')


if __name__ == '__main__':
    main()
