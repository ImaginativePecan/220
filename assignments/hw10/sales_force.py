"""
Name: Jake Tanner
sales_force.py

Problem: creates a class for the total sales force

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from hw10.sales_person import SalesPerson


class SalesForce:
    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        infile = open(file_name, 'r')
        for line in infile:
            line = line.split('\n')
            self.sales_people.append(line[0])

    def quota_report(self, quota):
        report = []
        for item in self.sales_people:
            employee_report = []
            employee_info = item.split(',')
            employee_report.append(employee_info[:1])
            employee = SalesPerson(employee_info[0], employee_info[1])
            for sale in range(employee_info[2:]):
                employee.enter_sale(sale)
            employee_report.append(employee.total_sales())
            employee_report.append(employee.met_quota(quota))
            report.append(employee_report)
        return report

    def top_seller(self):
        top_seller = []
        s = 0
        s_list = []
        for i in range(len(self.sales_people)):
            if s <= self.sales_people[i]:
                if s == self.sales_people[i]:
                    s_list.append(self.sales_people)
                    s = self.sales_people[i]
                else:
                    s = self.sales_people[i]
        s_list.append(s)
        top_seller.append(s_list)

    def individual_sales(self, employee_id):
        for i in self.sales_people:
            if int(employee_id) == SalesPerson.get_id(i):
                return SalesPerson.__str__(i)
        else:
            return None

