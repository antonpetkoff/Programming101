from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class Movie(Base):
    __tablename__ = "projection"
    id = Column(Integer, primary_key=True)
    type = Column(String)
    date = Column(String)
    time = Column(String)
    movie_id = Column(Integer, ForeignKey("movie.id"))
    movie_id = relationship("Movie", backref="movies")

    def __str__(self):
        return "[{}] - {} {} ({})".format(self.id, self.name, self.rating)

    def __repr__(self):
        print(str(self))
