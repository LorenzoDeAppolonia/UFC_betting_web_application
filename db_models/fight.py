from application.db import db
from .weight_class import WeightClass


class Fight(db.Model):
    __tablename__ = 'FIGHT'

    code = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    referee = db.Column(db.String(50))
    location = db.Column(db.String(50))
    fight_date = db.Column(db.Date)

    age_rc = db.Column(db.Integer)
    weight_rc = db.Column(db.Float)
    win_streak_rc = db.Column(db.Integer)
    wins_rc = db.Column(db.Integer)
    losses_rc = db.Column(db.Integer)

    age_bc = db.Column(db.Integer)
    weight_bc = db.Column(db.Float)
    win_streak_bc = db.Column(db.Integer)
    wins_bc = db.Column(db.Integer)
    losses_bc = db.Column(db.Integer)

    weight_class_code = db.Column(db.ForeignKey('WEIGHT_CLASS.code'))
    # weight_class= Mapped['WeightClass'] = relationship('WeightClass')
    weight_class = db.relationship('WeightClass')

    fighter_rc_code = db.Column(db.Integer, db.ForeignKey('FIGHTER.code'))
    fighter_rc = db.relationship('Fighter', foreign_keys=[fighter_rc_code], backref=db.backref('fights_as_rc', cascade="all, delete-orphan"))

    fighter_bc_code = db.Column(db.Integer, db.ForeignKey('FIGHTER.code'))
    fighter_bc = db.relationship('Fighter', foreign_keys=[fighter_bc_code], backref=db.backref('fights_as_bc', cascade="all, delete-orphan"))

    winner = db.Column(type_=db.String(50))

    def to_dict(self):
        return {
                f"code": self.code, "referee": self.referee, "location": self.location, "fight_date": self.fight_date.strftime('%Y-%m-%d'),
                "fighter_rc_code": self.fighter_rc_code, "fighter_bc_code": self.fighter_bc_code,
                "age_rc": self.age_rc, "weight_rc": self.weight_rc, "win_streak_rc": self.win_streak_rc,
                "wins_rc": self.wins_rc, "losses_rc": self.losses_rc, "age_bc": self.age_bc,
                "weight_bc": self.weight_bc, "win_streak_bc": self.win_streak_bc,
                "wins_bc": self.wins_bc, "losses_bc": self.losses_bc, "weight_class_code": self.weight_class_code,
                "winner": self.winner
        }
    
    def get_fight_information(self) -> dict:
        return {'code': self.code, 'referee': self.referee, 'location': self.location, 'date': self.fight_date,
                'winner': self.winner}


