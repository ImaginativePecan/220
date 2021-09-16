"""
Name: Jake Tanner
lab3.py
"""


def main():

    # Problem 1: Finding an average
    def average():
        print("This function calculates the average of your grades")
        print()

        num_grades = eval(input("Please enter the number of grades: "))
        hw_num = 1
        total = 0

        for i in range(1, num_grades + 1):
            hw_grade = eval(input("Please enter your grade on HW#" + str(hw_num) + ": "))
            total = total + hw_grade
            hw_num = hw_num + 1
        hw_average = total / num_grades

        print(round(hw_average, 2))

    average()

    print()
    print()

    # Problem 2: I work hard for the money!
    def tip_jar():
        print("This function calculates the total amount of tips in the tip jar")
        print()

        accumulator = 0
        for i in range(5):
            amount = eval(input("Please enter the amount of your donation: $"))
            print()
            accumulator = accumulator + amount

        print()
        print("The total amount of tips in the tip jar is: $" + str(accumulator))

    tip_jar()

    print()
    print()

    # Problem 3: Compute a square root
    def newton():
        print("This function approximates a square root using Sir Issac Newton's method")
        print()

        x = eval(input("Please enter the number you would like to approximate the square root of: "))
        print()
        refine_times = eval(input("Please enter the amount of times you would like to approximate the number: "))
        approximation = x / 2

        for i in range(refine_times):
            approximation = (approximation + (x / approximation)) / 2

        print()
        print("The result is: ", approximation)

    newton()

    print()
    print()

    # Problem 4: Output a sequence
    def sequence():
        print("This function outputs a sequence of numbers")
        print()

        iterations = eval(input("Please enter the amount of numbers in the sequence: "))
        for i in range(1, iterations + 1):
            y = 1 + (i // 2 * 2)
            print(y, end=" ")

    sequence()

    print()
    print()

    # Problem 5: Computing pi
    def pi():
        print("This function approximates the value of pi using the Wallis formula")
        print()

        accumulator = 1
        print("Hint: The more terms will get the value closer to pi")
        terms = eval(input("Please enter the number of terms in the series: "))

        for i in range(terms):
            numerator = 2 + ((i // 2) * 2)
            denominator = 1 + (((i + 1) // 2) * 2)
            accumulator = accumulator * (numerator / denominator)

        print()
        print("The value after", terms, "is:", (accumulator * 2))

    pi()


if __name__ == '__main__':
    main()
