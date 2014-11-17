import sqlite3
import os


class ManageDB:
    MAX_SPOTS = 100

    def __init__(self, file_name):
        db_exists = os.path.isfile(os.getcwd() + "/" + file_name)

        self.connect = sqlite3.connect(file_name)
        self.connect.row_factory = sqlite3.Row
        self.cursor = self.connect.cursor()

        if not db_exists:
            self.create_tables()
            self.fill_movies()
            self.fill_projections()
            self.fill_reservations()

    def __del__(self):
        self.connect.close()

    def create_tables(self):
        self.cursor.execute('''PRAGMA foreign_keys = ON;''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS movies(
            id INTEGER PRIMARY KEY, name TEXT, rating REAL);''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS projections(
            id INTEGER PRIMARY KEY, movie_id INTEGER,
            type TEXT, date TEXT, time TEXT,
            FOREIGN KEY(movie_id) REFERENCES movies(id));''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS reservations(
            id INTEGER PRIMARY KEY, username TEXT, projections_id INTEGER,
            row INTEGER, col INTEGER,
            FOREIGN KEY(projections_id) REFERENCES projections(id));''')

        self.connect.commit()

    def fill_movies(self):
        movies = [("The Hunger Games: Catching Fire", 7.9),
                  ("Wreck-It Ralph", 7.8),
                  ("Her", 8.3)]
        self.cursor.executemany('''INSERT INTO movies(name, rating)
            VALUES(?,?);''', movies)
        self.connect.commit()

    def fill_projections(self):
        projections = [(1, "3D", "2014-04-01", "19:10"),
                       (1, "2D", "2014-04-01", "19:00"),
                       (1, "4DX", "2014-04-02", "21:00"),
                       (3, "2D", "2014-04-05", "20:20"),
                       (2, "3D", "2014-04-02", "22:00"),
                       (2, "2D", "2014-04-02", "19:30")]
        self.cursor.executemany('''INSERT INTO
            projections(movie_id, type, date, time)
            VALUES(?,?,?,?);''', projections)
        self.connect.commit()

    def fill_reservations(self):
        reservations = [("RadoRado", 1, 2, 1), ("RadoRado", 1, 3, 5),
                        ("RadoRado", 1, 7, 8), ("Ivo", 3, 1, 1),
                        ("Ivo", 3, 1, 2), ("Mysterious", 5, 2, 3),
                        ("Mysterious", 5, 2, 4)]
        self.cursor.executemany('''INSERT INTO
            reservations(username, projections_id, row, col)
            VALUES(?,?,?,?);''', reservations)
        self.connect.commit()

    def get_spots_available(self, proj_id):
        selection = self.cursor.execute('''SELECT * from reservations WHERE
            projections_id = ?;''', (proj_id,)).fetchall()
        return self.MAX_SPOTS - len(selection)

    def show_movies(self):
        movies = self.cursor.execute('''SELECT * from movies;''').fetchall()
        output = "[{}] - {} ({})"
        for movie in movies:
            print(output.format(movie['id'], movie['name'], movie['rating']))

    def show_movie_projections(self, movie_id, date):
        movie = self.cursor.execute('''SELECT name from movies
            WHERE id = ?;''', (movie_id, )).fetchall()

        if date is None:
            print("Projections for movie \'{}\':".format(movie[0][0]))

            selection = self.cursor.execute('''SELECT * from projections WHERE
                movie_id = ? ORDER BY date, time;''', (movie_id,)).fetchall()
            output = "[{}] - {} {} ({}) - {} spots available"
            for item in selection:
                spots = self.get_spots_available(item['id'])
                print(output.format(item['id'], item['date'],
                                    item['time'], item['type'], spots))
        else:
            message = "Projections for movie \'{}\' on date {}:"
            print(message.format(movie[0][0], date))

            selection = self.cursor.execute('''SELECT * from projections WHERE
                movie_id = ? AND date = ?
                ORDER BY date, time;''', (movie_id, date)).fetchall()
            output = "[{}] - {} ({})"
            for item in selection:
                print(output.format(item['id'], item['time'], item['type']))

    def get_taken_seats_for_projection(self, proj_id):
        selection = self.cursor.execute('''SELECT reservations.row,
            reservations.col FROM reservations INNER JOIN projections
            ON  reservations.projections_id = projections.id
            WHERE projections.id = ?;''', (proj_id,)).fetchall()
        return selection

    def print_seats(self, proj_id):
        selection = self.get_taken_seats_for_projection(proj_id)

        seats = ""
        seats += "   1 2 3 4 5 6 7 8 9 10\n"
        for x in range(1, 11):
            seats += str(x) + (" " if x == 10 else "  ")
            for y in range(1, 11):
                seat_taken = False
                for pos in selection:
                    if x == pos["row"] and y == pos["col"]:
                        seat_taken = True
                        break
                if seat_taken:
                    seats += "X "
                else:
                    seats += ". "
            seats += "\n" if x != 10 else ""
        print(seats)

    def add_reservation(self, username, proj_id, row, col):
        self.cursor.execute('''INSERT INTO
            reservations(username, projections_id, row, col)
            VALUES(?, ?, ?, ?)''', (username, proj_id, row, col))
        self.connect.commit()

    def make_reservation(self):
        pass

    def show_reservations(self):
        selection = self.cursor.execute('''SELECT
         * from reservations;''').fetchall()
        for e in selection:
            print(e["id"], e["username"], e["projections_id"],
                  e["row"], e["col"])


def main():
    cinema = ManageDB("cinema.db")
    #cinema.show_movie_projections(3, "2014-04-01")
    cinema.show_reservations()
    cinema.show_movies()


if __name__ == '__main__':
    main()
