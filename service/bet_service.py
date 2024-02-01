from typing import List
from sqlalchemy.exc import SQLAlchemyError
from db_models.bet import Bet
from application.db import db
from random import uniform
from exceptions.ufc_betting_error import UfcBettingError

class BetService:

    @staticmethod
    def get_bet_by_code(code: int) -> Bet | None:
        try:
            bet = Bet.query.filter_by(code=code).one_or_none()
            return bet

        except SQLAlchemyError as e:
            raise UfcBettingError(str(e))

    @staticmethod
    def get_bet_statistics(code: int) -> dict | None:
        try:
            bet = BetService.get_bet_by_code(code)
            if bet:
                return bet.to_dict()

        except SQLAlchemyError as e:
            raise UfcBettingError(str(e))

    @staticmethod
    def get_all_bets() -> List[Bet] | None:

        try:
            bets = Bet.query.distinct().all()
            bets_list = [bet.to_dict() for bet in bets]
            return bets_list

        except SQLAlchemyError as e:
            raise UfcBettingError(str(e))

    @staticmethod
    def add_bet(bet: Bet):
        try:
            db.session.add(bet)
            db.session.commit()
            return True
        except SQLAlchemyError as e:
            db.session.rollback()
            raise UfcBettingError(str(e))

    @staticmethod
    def set_all_bets_results() -> object:
        try:
            all_bets = Bet.query.all()
            for bet in all_bets:

                if bet.payoff is None:

                    if bet.winner == bet.fight.winner:
                        winning_odds = uniform(1, 5)
                        new_payoff = bet.amount * winning_odds
                        bet.payoff = new_payoff
                    else:
                        bet.payoff = 0

            db.session.commit()
            return True

        except SQLAlchemyError as e:
            raise UfcBettingError(str(e))

    @staticmethod
    def change_bet_amount(code, amount: float):
        try:
            bet_to_change = BetService.get_bet_by_code(code=code)
            bet_to_change.amount = amount
            db.session.commit()

        except SQLAlchemyError as e:
            raise UfcBettingError(str(e))

    @staticmethod
    def change_bet_winner(code: int, winner: str):

        try:
            bet = BetService.get_bet_by_code(code=code)
            bet.winner = winner
            db.session.commit()

        except SQLAlchemyError as e:
            db.session.rollback()
            raise UfcBettingError(str(e))
