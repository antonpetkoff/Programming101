from connection import Base
from connection import engine
from sqlalchemy.orm import Session
from player import Player

# generates questions
# updates players DB
# highscores function


class DoYouEvenMath:
    def __init__(self):
        Base.metadata.create_all(engine)
        self.session = Session(bind=engine)

    def player_exists(self):
        pass

    def add_player(self):
        pass

    def update_score(self):
        pass

    def get_highscores(self):
        pass
