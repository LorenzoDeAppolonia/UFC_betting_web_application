from typing import List, Type
from sqlalchemy.exc import SQLAlchemyError
from db_models.fighter import Fighter
from application.db import db
import matplotlib.pyplot as plt
from io import BytesIO
import matplotlib
from sqlalchemy.orm.exc import NoResultFound
from exceptions.ufc_betting_error import UfcBettingError
matplotlib.use('Agg')


class FighterService:

    @staticmethod
    def get_fighter_statistics(code: int) -> dict | None | bool:
        try:
            fighter = FighterService.get_fighter_by_code(code)
            return fighter.to_dict() if fighter else None

        except SQLAlchemyError as e:
            raise UfcBettingError(str(e))

    @staticmethod
    def get_fighter_by_code(code: int) -> Fighter | None | bool:
        try:
            fighter = Fighter.query.filter_by(code=code).one_or_none()
            return fighter

        except SQLAlchemyError as e:
            raise UfcBettingError(str(e))

    @staticmethod
    def get_all_fighters() -> List[Type[Fighter]] | bool:
        try:
            fighters = Fighter.query.distinct().all()
            return [fighter.to_dict() for fighter in fighters]

        except SQLAlchemyError as e:
            raise UfcBettingError(str(e))

    @staticmethod
    def get_all_fighters_by_name(name: str) -> List[Type[Fighter]] | bool:
        try:
            fighters = Fighter.query.filter_by(name=name).distinct().all()
            return [fighter.to_dict() for fighter in fighters]

        except SQLAlchemyError as e:
            raise UfcBettingError(str(e))

    @staticmethod
    def get_all_fighters_by_weight(weight: float) -> List[Type[Fighter]] | bool:
        try:
            fighters = Fighter.query.filter_by(weight=weight).distinct().all()
            return [fighter.to_dict() for fighter in fighters]

        except SQLAlchemyError as e:
            raise UfcBettingError(str(e))

    @staticmethod
    def get_all_fighters_by_stance(stance: str) -> List[Type[Fighter]] | bool:
        try:
            fighters = Fighter.query.filter_by(stance=stance).distinct().all()
            return [fighter.to_dict() for fighter in fighters]

        except SQLAlchemyError as e:
            raise UfcBettingError(str(e))

    @staticmethod
    def get_all_fighters_by_age(age: int) -> List[Type[Fighter]] | bool:
        try:
            fighters = Fighter.query.filter_by(age=age).distinct().all()
            return [fighter.to_dict() for fighter in fighters]

        except SQLAlchemyError as e:
            raise UfcBettingError(str(e))

    @staticmethod
    def add_fighter(fighter: Fighter) -> bool:
        try:
            db.session.add(fighter)
            db.session.commit()
            return True

        except SQLAlchemyError as e:
            db.session.rollback()
            raise UfcBettingError(str(e))

    @staticmethod
    def delete_fighter_by_id(fighter_code) -> None | bool:
        try:
            fighter = FighterService.get_fighter_by_code(fighter_code)
            if fighter:
                db.session.delete(fighter)
                db.session.commit()
                return True
            return None

        except SQLAlchemyError as e:
            db.session.rollback()
            raise UfcBettingError(str(e))

    @staticmethod
    def generate_plot(record: dict, fighter_name: str) -> BytesIO:
        wins = record.get('wins', 0)
        losses = record.get('losses', 0)
        draws = record.get('draws', 0)

        labels = ['Wins', 'Losses', 'Draws']
        values = [wins, losses, draws]

        plt.figure(figsize=(10, 6))
        plt.bar(labels, values, color=['green', 'red', 'blue'])
        plt.title(f'Fighter Record: {fighter_name}', fontsize=14)
        plt.xlabel('Record Type', fontsize=12)
        plt.ylabel('Count', fontsize=12)
        buf = BytesIO()
        plt.savefig(buf, format='png', bbox_inches='tight')
        buf.seek(0)
        plt.close()

        return buf

