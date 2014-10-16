
class Employee(object):

    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

class HourlyEmployee(Employee):

    def __init__(self, name, hourly_wage):
        super().__init__(name)
        self.hourly_wage = hourly_wage

    def weeklyPay(self, hours):
        if hours > 40:
            return 40 * self.hourly_wage
            + (hours - 40) * self.hourly_wage * 1.5
        else:
            return hours * self.hourly_wage

class SalariedEmployee(Employee):

    def __init__(self, name, annual_salary):
        super().__init__(name)
        self.annual_salary = annual_salary

    def weeklyPay(self, hours):
        return self.annual_salary / 52.0   # 52.177457

class Manager(SalariedEmployee):

    def __init__(self, name, annual_salary, weekly_bonus):
        super().__init__(name, annual_salary)
        self.weekly_bonus = weekly_bonus

    def weeklyPay(self, hours):
        return self.annual_salary / 52.0 + self.weekly_bonus


def main():
    staff = []
    staff.append(HourlyEmployee("Morgan, Harry", 30.0))
    staff.append(SalariedEmployee("Lin, Sally", 52000.0))
    staff.append(Manager("Smith, Mary", 104000.0, 50.0))
    for employee in staff :
        hours = int(input("Hours worked by " + employee.getName() + ": "))
        pay = employee.weeklyPay(hours)
        print("Salary: %.2f" % pay)

if __name__ == '__main__':
    main()
