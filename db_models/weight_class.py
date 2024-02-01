from __future__ import annotations


from application.db import db


class WeightClass(db.Model):
    __tablename__ = 'WEIGHT_CLASS'

    code = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    weight = db.Column(db.String(50))

    def to_dict(self):
        return {'code': self.code, 'weight': self.weight}