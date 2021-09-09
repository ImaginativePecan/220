"""
Name: Jake Tanner
interest.py

Problem: this program computes the monthly interest charge of a credit card company

Certificate of Authenticity:
I certify that this assignment is entirely  of my own work.
"""


def main():
    annual_interest_rate = eval(input("Enter the annual interest rate: "))
    billing_cycle_days = eval(input("Enter the number of days in the billing cycle: "))
    previous_balance = eval(input("Enter the previous net balance of the account: "))
    payment_amount = eval(input("Enter the payment amount: "))
    payment_date = eval(input("Enter the day of the billing cycle in which the payment was made: "))
    step_one = round(billing_cycle_days, 2) * round(previous_balance, 2)
    step_two = (billing_cycle_days - payment_date) * round(payment_amount, 2)
    step_three = round(step_one, 2) - round(step_two, 2)
    average_daily_balance = round(step_three, 2) / billing_cycle_days
    monthly_interest = ((annual_interest_rate / 100) / 12) * average_daily_balance
    print(round(monthly_interest, 2))


if __name__ == '__main__':
    main()
