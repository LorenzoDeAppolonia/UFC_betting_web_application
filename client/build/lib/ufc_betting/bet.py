from datetime import date
import requests

from client.ufc_betting.client_helpers.error_handler import handle_error
from client.ufc_betting.configuration import URL_application


class Bet:
    def __init__(self, amount: float, date_bet: str, fight_id: int, winner: str, code=None, payoff=None):

        self.__code = code
        self.__amount = amount
        self.__date_bet = date_bet
        self.__fight_id = fight_id
        self.__winner = winner
        self.__payoff = payoff

    @property
    def code(self) -> int:
        return self.__code

    @property
    def amount(self) -> float:
        return self.__amount

    @amount.setter
    def amount(self, value):
        if int(value) > 0:
            response = requests.put(url=f'{URL_application}/bets/{self.code}', json={'amount': str(value)})
            if response.status_code != 200:
                handle_error(response)

            self.__winner = value

    @property
    def date_bet(self) -> str:
        return self.__date_bet

    @property
    def fight_code(self) -> int:
        return self.__fight_id

    @property
    def winner(self):
        return self.__winner

    @winner.setter
    def winner(self, value: str):
        if value in ['Red', 'Blue']:
            response = requests.put(url=f'{URL_application}/bets/{self.code}', json={'winner': str(value)})
            if response.status_code != 200:
                handle_error(response)

            self.__winner = value

    @property
    def payoff(self) -> float:
        return self.__payoff

    def __eq__(self, other):
        if self.code == other.code:
            return True

        return False

    def __str__(self):
        return f"Code: {self.code} | Amount: {self.amount} | Payoff: {self.payoff} | Date: {self.date_bet} | Fight code: {self.fight_code} | Winner: {self.__winner}"

    def to_dict(self) -> dict:
        return {'amount': float(self.amount),  'date_bet': self.date_bet,  'fight_code': int(self.fight_code), 'winner': self.__winner}