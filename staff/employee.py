class Employee(object):
    BASE_SALARY = 5000
    employee_number = 0

    def __init__(self, fname, sname, no_of_years):
        self.fname = fname
        self.sname = sname
        self.no_of_years = no_of_years
        Employee.employee_number += 1
        self.employee_number = Employee.employee_number

    '''calculate the base salary plus any bonus
    based on the number of years worked '''

    def calculate_salary(self):
        bonus = 0
        salary = self.BASE_SALARY
        if self.no_of_years < 3:
            bonus = salary * 0.05
        elif self.no_of_years <= 5:
            bonus = salary * 0.1
        elif self.no_of_years > 5:
            bonus = salary * 0.25
        return salary + bonus

    def details(self):
        return " First Name: %s\n Surname: %s\n Years Worked: %s\n Employee Number: %s\n Salary: %s\n " % (
            self.fname, self.sname, self.no_of_years, self.employee_number, self.calculate_salary())
