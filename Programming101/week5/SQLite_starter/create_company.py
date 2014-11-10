import sqlite3


class CompanyCreator:

    def __init__(self, file_name):
        self.connect = sqlite3.connect(file_name)
        self.cursor = self.connect.cursor()
        self._fill_db()

    def __del__(self):
        self.connect.close()

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

        self.connect.commit()
