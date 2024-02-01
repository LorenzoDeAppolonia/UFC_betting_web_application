from client.ufc_betting.client_helpers.convert_weight_class import from_json_to_weight_class
from client.ufc_betting.weight_class import WeightClass
from client.ufc_betting.fighter import Fighter
from client.ufc_betting.client_helpers.convert_fighter import from_json_to_fighter
from client.ufc_betting.fight import Fight
from client.ufc_betting.client_helpers.convert_fight import from_json_to_fight


def test_from_json_to_weight_class():
    # Mock data
    mock_json = {
        'code': 1,
        'weight': 'Heavyweight'
    }

    weight_class_instance = from_json_to_weight_class(mock_json)

    assert isinstance(weight_class_instance, WeightClass)
    assert weight_class_instance.code == mock_json['code']
    assert weight_class_instance.weight == mock_json['weight']


def test_from_json_to_fighter():
    mock_json = {
        'code': 100,
        'name': 'John Doe',
        'height': 180,
        'reach': 74,
        'stance': 'Orthodox'
    }

    fighter_instance = from_json_to_fighter(mock_json)
    assert isinstance(fighter_instance, Fighter)
    assert fighter_instance.code == mock_json['code']
    assert fighter_instance.name == mock_json['name']
    assert fighter_instance.height == mock_json['height']
    assert fighter_instance.reach == mock_json['reach']
    assert fighter_instance.stance == mock_json['stance']


def test_from_json_to_fight():
    # Mock data
    mock_json = {
        'code': 200,
        'referee': 'Joe Smith',
        'location': 'Las Vegas',
        'fight_date': '2024-01-01',
        'age_rc': 32,
        'weight_rc': 205,
        'win_streak_rc': 3,
        'wins_rc': 15,
        'losses_rc': 2,
        'age_bc': 30,
        'weight_bc': 205,
        'win_streak_bc': 4,
        'wins_bc': 18,
        'losses_bc': 1,
        'weight_class_code': 5,
        'fighter_rc_code': 101,
        'fighter_bc_code': 102,
        'winner': 'Red'
    }

    fight_instance = from_json_to_fight(mock_json)

    # Assertions
    assert isinstance(fight_instance, Fight), "The returned object should be an instance of Fight"
    assert fight_instance.code == mock_json['code']
    assert fight_instance.referee == mock_json['referee']
    assert fight_instance.location == mock_json['location']
    assert fight_instance.fight_date == mock_json['fight_date']
    assert fight_instance.age_rc == mock_json['age_rc']
    assert fight_instance.weight_rc == mock_json['weight_rc']
    assert fight_instance.win_streak_rc == mock_json['win_streak_rc']
    assert fight_instance.wins_rc == mock_json['wins_rc']
    assert fight_instance.losses_rc == mock_json['losses_rc']
    assert fight_instance.age_bc == mock_json['age_bc']
    assert fight_instance.weight_bc == mock_json['weight_bc']
    assert fight_instance.win_streak_bc == mock_json['win_streak_bc']
    assert fight_instance.wins_bc == mock_json['wins_bc']
    assert fight_instance.losses_bc == mock_json['losses_bc']
    assert fight_instance.weight_class_code == mock_json['weight_class_code']
    assert fight_instance.fighter_rc_code == mock_json['fighter_rc_code']
    assert fight_instance.fighter_bc_code == mock_json['fighter_bc_code']
    assert fight_instance.winner == mock_json['winner']

