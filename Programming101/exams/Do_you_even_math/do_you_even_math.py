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

    def player_exists(self, name):
        select = self.session.query(Player).filter(Player.name == name).all()
        return len(select) == 1

    def add_player(self, name):
        if self.player_exists(name):
            return

        self.session.add(Player(name=name, score=0))
        self.session.commit()

    def update_score(self):
        pass

    def get_highscores(self):
        pass


def main():
    db = DoYouEvenMath()
    db.add_player("Dingo")
    print(db.player_exists("Dingo"))
    print(db.player_exists("asd"))

if __name__ == '__main__':
    main()
