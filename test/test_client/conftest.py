import pytest
from client.ufc_betting.fight import Fight
from client.ufc_betting.fighter import Fighter
from client.ufc_betting.weight_class import WeightClass
from client.ufc_betting.bet import Bet
import datetime


@pytest.fixture
def fight_example():
    fight = Fight(code=2, referee='Lui Castro', location='Las Vegas, USA', fight_date='2024-01-01', age_rc=30,
                  weight_rc=75.2, win_streak_rc=5, wins_rc=10, losses_rc=2, age_bc=28, weight_bc=73.8,
                  win_streak_bc=4, wins_bc=8, losses_bc=3, weight_class_code=3, fighter_rc_code=2,
                  fighter_bc_code=1, winner="Red")
    return fight


@pytest.fixture
def fight_example_2():
    fight = Fight(code=3, referee='Lui Castro', location='Las Vegas, USA', fight_date='2024-01-01', age_rc=30,
                  weight_rc=75.2, win_streak_rc=5, wins_rc=10, losses_rc=2, age_bc=28, weight_bc=73.8,
                  win_streak_bc=4, wins_bc=8, losses_bc=3, weight_class_code=3, fighter_rc_code=2,
                  fighter_bc_code=1, winner="Red")
    return fight


@pytest.fixture
def fight_example_3():
    fight = Fight(code=2, referee='Lorenzo de Appolonia', location='Las Vegas, USA', fight_date='2024-01-01', age_rc=20,
                  weight_rc=75.2, win_streak_rc=5, wins_rc=10, losses_rc=2, age_bc=28, weight_bc=73.8,
                  win_streak_bc=4, wins_bc=8, losses_bc=3, weight_class_code=3, fighter_rc_code=2,
                  fighter_bc_code=1, winner="Red")

    return fight


@pytest.fixture
def fighter_example():
    fighter = Fighter(code=1, name='John Jons', height=192.1, reach=198.2, stance='Orthodox')
    return fighter


@pytest.fixture
def other_example():
    other_fighter = Fighter(code=1, name='Big Boss', height=182.1, reach=195.2, stance='Southpaw')
    return other_fighter


@pytest.fixture
def other_example_2():
    other_fighter_2 = Fighter(code=2, name='Big Boss', height=183.4, reach=195.2, stance='Southpaw')
    return other_fighter_2


@pytest.fixture
def weight_class_example():
    weight_class = WeightClass(code=3, weight="Heavyweight")
    return weight_class


@pytest.fixture
def other_weight_class_example():
    other_weight_class = WeightClass(code=3, weight="Heavyweight")
    return other_weight_class


@pytest.fixture
def other_weight_class_example_2():
    other_weight_class_2 = WeightClass(code=2, weight="Heavyweight")
    return other_weight_class_2


@pytest.fixture
def bet_example():
    bet = Bet(amount=51.5, date_bet='2024-01-10', fight_id=19064, winner='Red')
    return bet


@pytest.fixture
def other_bet_example():
    other_bet = Bet(amount=51.5, date_bet='2024-01-10', fight_id=19064, winner='Red')
    return other_bet


@pytest.fixture
def other_bet_example_2():
    other_bet_2 = Bet(amount=51.5, date_bet='2024-01-10', fight_id=19064, winner='Blue')
    return other_bet_2
