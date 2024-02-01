from datetime import date

from .client_helpers.convert_fighter import from_json_to_fighter
from .client_helpers.simple_requests import get_fighter_json_by_id, get_weight_class_json_by_id
from .client_helpers.convert_weight_class import from_json_to_weight_class


class Fight:
    def __init__(self, code: int, referee: str, location: str, fight_date: str, age_rc: int, weight_rc: float, win_streak_rc: int,
                 wins_rc: int, losses_rc: int, age_bc: int, weight_bc: float, win_streak_bc: float, wins_bc: int,
                 losses_bc: int, weight_class_code: int, fighter_rc_code: int, fighter_bc_code: int, winner: str):

        self.__code = code
        self.__referee = referee
        self.__location = location
        self.__fight_date = fight_date

        self.__age_rc = age_rc
        self.__weight_rc = weight_rc
        self.__win_streak_rc = win_streak_rc
        self.__wins_rc = wins_rc
        self.__losses_rc = losses_rc

        self.__age_bc = age_bc
        self.__weight_bc = weight_bc
        self.__win_streak_bc = win_streak_bc
        self.__wins_bc = wins_bc
        self.__losses_bc = losses_bc

        self.__weight_class_code = weight_class_code
        self.__fighter_rc_code = fighter_rc_code
        self.__fighter_bc_code = fighter_bc_code
        self.__winner = winner
        self.populate_attributes(fighter_rc_code, fighter_bc_code, weight_class_code)

    def populate_attributes(self, fighter_rc_code, fighter_bc_code, weight_class_code):
        self.__fighter_rc = from_json_to_fighter(get_fighter_json_by_id(fighter_rc_code))
        self.__fighter_bc = from_json_to_fighter(get_fighter_json_by_id(fighter_bc_code))
        self.__weight_class = from_json_to_weight_class(get_weight_class_json_by_id(weight_class_code))

    def __eq__(self, other):
        if self.code == other.code:
            return True
        return False

    def __str__(self):
        return (f"Code: {self.__code} | Referee: {self.__referee} | Location: {self.__location} | "
                f"Fight Date: {self.__fight_date} | Age RC: {self.__age_rc} | Weight RC: {self.__weight_rc} | "
                f"Win Streak RC: {self.__win_streak_rc} | Wins RC: {self.__wins_rc} | Losses RC: {self.__losses_rc} | "
                f"Age BC: {self.__age_bc} | Weight BC: {self.__weight_bc} | Win Streak BC: {self.__win_streak_bc} | "
                f"Wins BC: {self.__wins_bc} | Losses BC: {self.__losses_bc} | Weight Class Code: {self.__weight_class_code} | "
                f"Fighter RC: {self.__fighter_rc.name} | Fighter BC: {self.__fighter_bc.name} | Winner Code: {self.__winner}")

    def to_dict(self):
        return {
            "code": self.__code,
            "referee": self.__referee,
            "location": self.__location,
            "fight_date": self.fight_date,
            "age_rc": self.__age_rc,
            "weight_rc": self.__weight_rc,
            "win_streak_rc": self.__win_streak_rc,
            "wins_rc": self.__wins_rc,
            "losses_rc": self.__losses_rc,
            "age_bc": self.__age_bc,
            "weight_bc": self.__weight_bc,
            "win_streak_bc": self.__win_streak_bc,
            "wins_bc": self.__wins_bc,
            "losses_bc": self.__losses_bc,
            "weight_class_code": self.__weight_class_code,
            "fighter_rc_code": self.__fighter_rc_code,
            "fighter_bc_code": self.__fighter_bc_code,
            "winner": self.__winner
            }

    @property
    def code(self):
        return self.__code

    @property
    def referee(self):
        return self.__referee

    @property
    def location(self):
        return self.__location

    @property
    def fight_date(self):
        return self.__fight_date

    @property
    def age_rc(self):
        return self.__age_rc

    @property
    def weight_rc(self):
        return self.__weight_rc

    @property
    def win_streak_rc(self):
        return self.__win_streak_rc

    @property
    def wins_rc(self):
        return self.__wins_rc

    @property
    def losses_rc(self):
        return self.__losses_rc

    @property
    def age_bc(self):
        return self.__age_bc

    @property
    def weight_bc(self):
        return self.__weight_bc

    @property
    def win_streak_bc(self):
        return self.__win_streak_bc

    @property
    def wins_bc(self):
        return self.__wins_bc

    @property
    def losses_bc(self):
        return self.__losses_bc

    @property
    def weight_class_code(self):
        return self.__weight_class_code

    @property
    def fighter_rc(self):
        return self.__fighter_rc

    @property
    def fighter_bc(self):
        return self.__fighter_bc

    @property
    def winner(self):
        return self.__winner

    @property
    def fighter_rc_code(self):
        return self.__fighter_rc_code

    @property
    def fighter_bc_code(self):
        return self.__fighter_bc_code
