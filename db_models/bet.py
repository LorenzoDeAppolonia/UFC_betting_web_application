from __future__ import annotations

from application.db import db
from random import uniform


class Bet(db.Model):
    __tablename__ = 'BET'

    code = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)
    amount = db.Column(db.Float, db.CheckConstraint('amount>=0'))
    date_bet = db.Column(db.Date)
    fight_code = db.Column(db.ForeignKey('FIGHT.code'))
    fight = db.relationship('Fight', foreign_keys=[fight_code])
    winner = db.Column(db.String(50))
    payoff = db.Column(db.Float)

    def to_dict(self) -> dict:
        return {'code': self.code,
                'amount': self.amount,
                'date_bet': self.date_bet.strftime('%Y-%m-%d'),
                'payoff': self.payoff,
                'fight_code': self.fight_code,
                'winner': self.winner
                #'fighter_rc': self.fight.fighter_rc.name,
                #'fighter_bc': self.fight.fighter_bc.name
                }

