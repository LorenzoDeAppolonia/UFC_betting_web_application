import datetime
from typing import List, Type
from db_models.fight import Fight
from application.db import db
from sqlalchemy.exc import SQLAlchemyError
from exceptions.ufc_betting_error import UfcBettingError


class FightService:

    @staticmethod
    def get_fight_by_code(code: int) -> Fight | None | bool:
        try:
            fight = Fight.query.filter_by(code=code).one_or_none()
            return fight

        except SQLAlchemyError as e:
            raise UfcBettingError(str(e))

    @staticmethod
    def get_fight_statistics(code: int) -> dict | None | bool:
        try:
            fight = FightService.get_fight_by_code(code)
            return fight.to_dict() if fight else None

        except SQLAlchemyError as e:
            raise UfcBettingError(str(e))

    @staticmethod
    def get_all_fights() -> List[Type[Fight]] | bool:
        try:
            fights = Fight.query.distinct().all()
            return [fight.to_dict() for fight in fights]

        except SQLAlchemyError as e:
            raise UfcBettingError(str(e))

    @staticmethod
    def get_all_fights_by_location(location: str) -> List[Type[Fight]] | bool:
        try:
            fights = Fight.query.filter_by(location=location).distinct().all()
            return [fight.to_dict() for fight in fights]

        except SQLAlchemyError as e:
            raise UfcBettingError(str(e))

    @staticmethod
    def get_all_fights_by_date(date: datetime) -> List[Type[Fight]] | bool:
        try:
            fights = Fight.query.filter_by(fight_date=date).distinct().all()
            return [fight.to_dict() for fight in fights]

        except SQLAlchemyError as e:
            raise UfcBettingError(str(e))

    @staticmethod
    def get_all_fights_by_weight_class(weight_class_code: int) -> List[Type[Fight]] | bool:
        try:
            fights = Fight.query.filter_by(weight_class_code=weight_class_code).distinct().all()
            return [fight.to_dict() for fight in fights]

        except SQLAlchemyError as e:
            raise UfcBettingError(str(e))

    @staticmethod
    def add_fight(fight: Fight) -> bool:
        try:
            db.session.add(fight)
            db.session.commit()
            return True

        except SQLAlchemyError as e:
            db.session.rollback()
            raise UfcBettingError(str(e))

    @staticmethod
    def get_fighter_record(fighter_code: int) -> dict | None | bool:
        try:
            red_wins = Fight.query.filter_by(fighter_rc_code=fighter_code, winner='red').count()
            blue_wins = Fight.query.filter_by(fighter_bc_code=fighter_code, winner='blue').count()
            wins = red_wins + blue_wins

            red_losses = Fight.query.filter_by(fighter_rc_code=fighter_code, winner='blue').count()
            blue_losses = Fight.query.filter_by(fighter_bc_code=fighter_code, winner='red').count()
            losses = red_losses + blue_losses

            total_fights = Fight.query.filter((Fight.fighter_rc_code == fighter_code) | (Fight.fighter_bc_code == fighter_code)).count()

            draws = total_fights - wins - losses

            return {'wins': wins, 'losses': losses, 'draws': draws}

        except SQLAlchemyError as e:
            raise UfcBettingError(str(e))

