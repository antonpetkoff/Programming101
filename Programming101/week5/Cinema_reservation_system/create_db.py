import sqlite3


class CreateDB:

    def __init__(self, file_name):
        self.connect = sqlite3.connect(file_name)
        self.cursor = self.connect.cursor()
        self.connect.row_factory = sqlite3.Row

        self._create_movies_table()

    def __del__(self):
        self.connect.close()

    def _create_movies_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS movies(
            id INTEGER PRIMARY KEY, name TEXT, rating REAL);''')

        self.cursor.execute('''INSERT INTO movies(name, rating)
            VALUES("The Hunger Games: Catching Fire", 7.9);''')
        self.cursor.execute('''INSERT INTO movies(name, rating)
            VALUES("Wreck-It Ralph", 7.8);''')
        self.cursor.execute('''INSERT INTO movies(name, rating)
            VALUES("Her", 8.3);''')

        self.connect.commit()


def main():
    movies = CreateDB("cinema.db")

    contents = movies.cursor.execute('''SELECT * from movies;''').fetchall()
    print(contents)


if __name__ == '__main__':
    main()
