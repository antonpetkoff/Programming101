from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()


class Movie(Base):
    __tablename__ = "movie"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    rating = Column(Float)

    def __str__(self):
        return "[{}] - {} ({})".format(self.id, self.name, self.rating)

    def __repr__(self):
        print(str(self))
