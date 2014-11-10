from create_company import CompanyCreator
import os
import sqlite3


class CompanyManager:

    def __init__(self, file_name):
        if not os.path.isfile(os.getcwd() + "/" + file_name):
            CompanyCreator(file_name)
        self.connect = sqlite3.connect(file_name)
        self.connect.row_factory = sqlite3.Row
        self.cursor = self.connect.cursor()

    def list_employees(self):
        selection = self.cursor.execute('''SELECT name, position
            FROM employees''')
        for row in selection:
            print("{} - {}".format(row["name"], row["position"]))

    def monthly_spending(self):
        sum_monthly = self.cursor.execute('''SELECT SUM(monthly_salary)
            AS sum FROM employees''')
        print(sum_monthly.fetchone()["sum"])

    def yearly_spending(self):
        sum_monthly = self.cursor.execute('''SELECT SUM(monthly_salary)
            AS sum FROM employees''')
        month = sum_monthly.fetchone()["sum"]
        sum_yearly = self.cursor.execute('''SELECT SUM(yearly_bonus)
            AS sum FROM employees''')
        year = sum_yearly.fetchone()["sum"]
        print(12 * month + year)

    def add_employee(self):
        name = input("name> ")
        monthly_salary = input("monthly_salary> ")
        yearly_bonus = input("yearly_bonus> ")
        position = input("position> ")

        self.cursor.execute('''INSERT INTO
            employees(name, monthly_salary, yearly_bonus, position)
            VALUES(?, ?, ?, ?);''',
            (name, monthly_salary, yearly_bonus, position))

        self.connect.commit()

        # result = self.cursor.execute('''SELECT * FROM employees''').fetchall()
        # print([list(x) for x in result])


def main():
    manager = CompanyManager("company.db")
    #manager.list_employees()
    #manager.monthly_spending()
    #manager.yearly_spending()
    #manager.add_employee()
    manager.list_employees()

if __name__ == '__main__':
    main()
