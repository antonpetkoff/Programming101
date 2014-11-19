from movie import Movie
from projection import Projection
from reservation import Reservation

from connection import Base
from connection import engine
from sqlalchemy.orm import Session


class Cinema:
    def __init__(self):
        Base.metadata.create_all(engine)
        self.session = Session(bind=engine)

    def add_movie(self, name, rating):
        self.session.add(Movie(name=name, rating=rating))
        self.session.commit()

    def add_projection(self, movie_id, type, date, time):
        self.session.add(
            Projection(movie_id=movie_id, type=type, date=date, time=time))
        self.session.commit()

    def add_reservation(self, user, proj_id, row, col):
        r = Reservation(username=user, projection_id=proj_id, row=row, col=col)
        self.session.add(r)
        self.session.commit()


def main():
    cinema = Cinema()
    cinema.add_movie("Dingo", 2.1)

if __name__ == '__main__':
    main()
