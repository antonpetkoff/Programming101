import sqlite3


class CreateCompany:

    def __init__(self):
        self.connect = sqlite3.connect("company.db")
        self.connect.row_factory = sqlite3.Row
        self.cursor = self.connect.cursor()
        self._fill_db()

        # result = self.cursor.execute('''SELECT * FROM employees''').fetchall()
        # print([list(x) for x in result])

    def _fill_db(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS employees(
            id INTEGER PRIMARY KEY, name TEXT, monthly_salary INTEGER,
            yearly_bonus INTEGER, position TEXT);''')

        self.cursor.execute('''INSERT INTO
            employees(name, monthly_salary, yearly_bonus, position)
            VALUES("Ivan Ivanov", 5000, 10000, "Software Developer");''')

        self.cursor.execute('''INSERT INTO
            employees(name, monthly_salary, yearly_bonus, position)
            VALUES("Rado Rado", 500, 0, "Technical Support Intern");''')

        self.cursor.execute('''INSERT INTO
            employees(name, monthly_salary, yearly_bonus, position)
            VALUES("Ivo Ivo", 10000, 100000, "CEO");''')

        self.cursor.execute('''INSERT INTO
            employees(name, monthly_salary, yearly_bonus, position)
            VALUES("Petar Petrov", 3000, 1000, "Marketing Manager");''')

        self.cursor.execute('''INSERT INTO
            employees(name, monthly_salary, yearly_bonus, position)
            VALUES("Maria Georgieva", 8000, 10000, "CEO");''')

    def list_employees(self):
        data = self.cursor.execute('''SELECT name, position FROM employees''')
        for row in data:
            print("{} - {}".format(row["name"], row["position"]))

    def monthly_spending(self):
        s = self.cursor.execute('''SELECT SUM(monthly_salary) FROM employees''')
        print(list(s.fetchone())[0])


def main():
    db = CreateCompany()
    #db.list_employees()
    db.monthly_spending()


if __name__ == '__main__':
    main()
