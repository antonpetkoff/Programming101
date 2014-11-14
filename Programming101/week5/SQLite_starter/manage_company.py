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
        selection = self.cursor.execute('''SELECT id, name, position
            FROM employees''')
        for row in selection:
            print("{} - {} - {}".format(row["id"], row["name"], row["position"]))

    def monthly_spending(self):
        sum_monthly = self.cursor.execute('''SELECT SUM(monthly_salary)
            AS sum FROM employees''')
        output = "The company is spending ${} every month!"
        print(output.format(sum_monthly.fetchone()["sum"]))

    def yearly_spending(self):
        sum_monthly = self.cursor.execute('''SELECT SUM(monthly_salary)
            AS sum FROM employees''')
        month = sum_monthly.fetchone()["sum"]
        sum_yearly = self.cursor.execute('''SELECT SUM(yearly_bonus)
            AS sum FROM employees''')
        year = sum_yearly.fetchone()["sum"]
        output = "The company is spending ${} every year!"
        print(output.format(12 * month + year))

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

    def delete_employee(self, id):
        get_ids = self.cursor.execute('''SELECT id FROM employees''').fetchall()
        ids_list = [int(x[0]) for x in get_ids]
        if int(id) in ids_list:
            self.cursor.execute('''DELETE FROM employees WHERE ID = ?''', (id,))
            self.connect.commit()
        else:
            raise ValueError("delete_employee(): No such id: {}".format(id))

    def update_employee(self, id):
        get_ids = self.cursor.execute('''SELECT id FROM employees''').fetchall()
        ids_list = [int(x[0]) for x in get_ids]
        if int(id) in ids_list:
            name = input("name> ")
            monthly_salary = input("monthly_salary> ")
            yearly_bonus = input("yearly_bonus> ")
            position = input("position> ")

            self.cursor.execute('''UPDATE employees SET name = ?,
                monthly_salary = ?, yearly_bonus = ?, position = ?
                WHERE id = ?;''', (name, monthly_salary, yearly_bonus, position, id))

            self.connect.commit()
        else:
            raise ValueError("update_employee(): No such id: {}".format(id))

    @staticmethod
    def loop(manager):
        while True:
            command = input("command (enter \"quit\" to exit)> ")

            if command == "list_employees":
                manager.list_employees()
            elif command == "monthly_spending":
                manager.monthly_spending()
            elif command == "yearly_spending":
                manager.yearly_spending()
            elif command == "add_employee":
                manager.add_employee()
            elif command.find("delete_employee") != -1:
                args = command.split(" ")
                manager.delete_employee(args[1])
            elif command.find("update_employee") != -1:
                args = command.split(" ")
                manager.update_employee(args[1])
            elif command == "quit":
                print("Bye!")
                break
            else:
                print("Invalid command!")


def main():
    manager = CompanyManager("company.db")
    CompanyManager.loop(manager)

if __name__ == '__main__':
    main()
