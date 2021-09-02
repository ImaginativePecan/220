"""
Name: Jake Tanner
lab1.py

Problem: This function calculates the area of a rectangle
"""


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)


calc_rec_area()


"""
This function calculates the volume of an object
"""


def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("Volume =", volume)


calc_volume()


"""
This function calculates the shooting percentage for basketball
"""


def shooting_percentage():
    shots_attempted = eval(input("Enter how many shots were attempted: "))
    shots_made = eval(input("Enter how many shots were made: "))
    shooting_percentage_decimal = shots_made / shots_attempted
    shooting_percentage = shooting_percentage_decimal * 100
    print("Your shooting percentage =", shooting_percentage, "%")


shooting_percentage()


"""
This function calculates the total cost of coffee ordered
"""


def coffee():
    coffee_per_pound = 10.5
    shipping_per_pound = 0.86
    cost_per_order = 1.5
    order_amount = eval(input("Enter how many pounds of coffee were purchased: "))
    total_cost = (order_amount * coffee_per_pound) + (order_amount * shipping_per_pound) + cost_per_order
    print("The total cost for the order is: $", total_cost)


coffee()

"""
This function converts kilometers to miles
"""


def kilometers_to_miles():
    kilometers = eval(input("Enter the amount of Kilometers traveled: "))
    miles = kilometers / 1.60934
    print("The corresponding amount of miles is: ", miles)


kilometers_to_miles()
