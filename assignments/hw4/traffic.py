"""
Name: Jake Tanner
traffic.py

Problem: Calculate the average amount of cars on roads for the Department of Transportation

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def main():
    # gets input for number of roads
    roads_s = eval(input("How many roads were surveyed? "))
    num_cars = 0
    car_day = 0
    for i in range(1, roads_s + 1):
        # gets input for number of days for each road
        days = eval(input("How many days was road " + str(i) + " surveyed? "))
        for x in range(1, days + 1):
            # gets input for how many cars on the road
            cars = eval(input("    How many cars traveled on day " + str(x) + "? "))
            num_cars = num_cars + cars
            car_day = car_day + cars
            average = car_day / days
        car_day = 0

        print("Road", i, "average vehicles per day: ", average)

    # gets the total amount of cars
    print("Total number of vehicles traveled on all roads: ", num_cars)

    # calculates the average of all the cars
    total_average = num_cars / roads_s
    print("Average number of vehicles per road: ", round(total_average, 2))


if __name__ == '__main__':
    main()
