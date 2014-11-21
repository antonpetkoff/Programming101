from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from connection import Base


class Reservation(Base):
    __tablename__ = "reservation"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    row = Column(Integer)
    col = Column(Integer)

    projection_id = Column(Integer, ForeignKey("projection.id"))
    projection = relationship("Projection", backref="reservations")

    def __str__(self):
        return "[{}] {} sitting @ ({},{})"\
            .format(self.id, self.username, self.row, self.col)

    def __repr__(self):
        return self.__str__()
