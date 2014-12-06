from connection import Base
from connection import engine
from sqlalchemy.orm import Session
from player import Player


class DBManager:
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

    def update_score(self, name, score):
        player = self.session.query(Player).\
            filter(Player.name == name).first()
        player.score = score
        self.session.commit()

    def get_highscores(self):
        highscores = self.session.query(Player).\
            order_by(Player.score.desc()).all()

        if len(highscores) == 0:
            return 'There aren\'t any players!'

        limit = min(len(highscores), 10)
        msg = 'This is the current top10:\n\n'

        for i in range(0, limit):
            msg += '{}. {}\n'.format(i + 1, highscores[i])

        return msg[:-1]

    def is_score_better(self, name, score):
        player = self.session.query(Player).\
            filter(Player.name == name).first()
        return score > player.score
