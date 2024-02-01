import pytest
from db_models.fighter import Fighter
from db_models.fight import Fight
import datetime


@pytest.fixture
def fight_example():

    date_def = datetime.date(2019, 2, 13)
    fight = Fight(code=1, referee="Loris", location="Las Vegas, USA",
                  fight_date=date_def, age_rc=32, weight_rc=75.2,
                  win_streak_rc=2, wins_rc=8, losses_rc=2, age_bc=28,
                  weight_bc=73.4, win_streak_bc=3, wins_bc=12, losses_bc=3,
                  weight_class_code=3, fighter_rc_code=13, fighter_bc_code=194,
                  winner="Red")
    return fight


@pytest.fixture
def fighter_example():
    fighter = Fighter(code=20, name="Daniel Corcks", height=165.1, reach=172.3, stance="Orthodox")
    return fighter


@pytest.fixture
def fighter_example_2():
    fighter_2 = Fighter(code=20, name="Daniel Corcks", height=165.1, reach=172.3, stance="Orthodox")
    return fighter_2


