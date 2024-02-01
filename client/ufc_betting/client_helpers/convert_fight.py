from ..fight import Fight


def from_json_to_fight(fight_data):
    fight = Fight(

        code=fight_data['code'],

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
