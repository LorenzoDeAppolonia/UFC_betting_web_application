from __future__ import annotations
from application.db import db


class Fighter(db.Model):
    __tablename__ = 'FIGHTER'

    code = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    name = db.Column(db.String(50))
    height = db.Column(db.Float)
    reach = db.Column(db.Float)
    stance = db.Column(db.String(50))

    def to_dict(self):
        return {
            "code": self.code, "name": self.name, "height": self.height,
            "reach": self.reach, "stance": self.stance
            }

    def __eq__(self, other):
        if self.name == other.name and self.height == other.height and self.reach == other.reach and self.stance == other.stance:
            return True
        return False
