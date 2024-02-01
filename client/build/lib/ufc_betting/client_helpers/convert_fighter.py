from ..fighter import Fighter


def from_json_to_fighter(fighter_data):

    fighter = Fighter(

        code=fighter_data['code'],

        name=fighter_data['name'],

        height=fighter_data['height'],

        reach=fighter_data['reach'],

        stance=fighter_data['stance']

    )

    return fighter
