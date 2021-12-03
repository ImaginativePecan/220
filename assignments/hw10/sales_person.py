"""
Name: Jake Tanner
sales_person.py

Problem: creates a class for an individual sales person

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


class SalesPerson:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.sales = []

    def get_id(self):
        return int(self.employee_id)

    def get_name(self):
        return str(self.name)

    def set_name(self, name):
        self.name = name

    def enter_sale(self, sale):
        self.sales.append(float(sale))

    def total_sales(self):
        total_sales = 0
        for sale in self.sales:
            total_sales += sale
        return total_sales

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        if self.total_sales() >= quota:
            return True
        else:
            return False

    def compare_to(self, other):
        if other > self.total_sales():
            return int(-1)
        elif other == self.total_sales():
            return int(0)
        elif other < self.total_sales():
            return int(1)

    def __str__(self):
        return str(self.employee_id) + '-' + self.name + ': ' + str(self.total_sales())
