from db_models.fight import Fight
from db_models.fighter import Fighter
from db_models.weight_class import WeightClass
from db_models.bet import Bet


def from_json_to_fight(fight_data):

    fight = Fight(

        referee=fight_data['referee'],
        location=fight_data['location'],
        fight_date=fight_data['fight_date'],

        age_rc=fight_data['age_rc'],
        weight_rc=fight_data['weight_rc'],
        win_streak_rc=fight_data['win_streak_rc'],
        wins_rc=fight_data['wins_rc'],
        losses_rc=fight_data['losses_rc'],

        age_bc=fight_data['age_bc'],
        weight_bc=fight_data['weight_bc'],
        win_streak_bc=fight_data['win_streak_bc'],
        wins_bc=fight_data['wins_bc'],
        losses_bc=fight_data['losses_bc'],

        weight_class_code=fight_data['weight_class_code'],
        fighter_rc_code=fight_data['fighter_rc_code'],
        fighter_bc_code=fight_data['fighter_bc_code'],
        winner=fight_data['winner']
    )
    return fight


def from_json_to_fighter(fighter_data):
    fighter = Fighter(
        name=fighter_data['name'],
        height=fighter_data['height'],
        reach=fighter_data['reach'],
        stance=fighter_data['stance']
    )
    return fighter


def from_json_to_weight_class(weight_class_data):
    weight_class = WeightClass(
        weight=weight_class_data['weight']
    )

    return weight_class


def from_json_to_bet(bet_data):
    bet = Bet(
        amount=bet_data['amount'],
        date_bet=bet_data['date_bet'],
        fight_code=bet_data['fight_code'],
        winner=bet_data['winner'],
        payoff=None,
    )
    return bet
