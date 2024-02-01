import datetime


class TestFightClass:

    @classmethod
    def test_fight_to_dict(cls, fight_example):
        date_def = datetime.date(2019, 2, 13)
        fight = fight_example

        # Call to_dict method
        fight_dict = fight.to_dict()
        print(fight_dict)

        expected_output = {
            "code": 1, "referee": "Loris", "location": "Las Vegas, USA", "fight_date": date_def.strftime('%Y-%m-%d'),
            "age_rc": 32, "weight_rc": 75.2, "win_streak_rc": 2,
            "wins_rc": 8, "losses_rc": 2, "age_bc": 28, "weight_bc": 73.4, "win_streak_bc": 3,
            "wins_bc": 12, "losses_bc": 3, "weight_class_code": 3, "fighter_rc_code": 13, "fighter_bc_code": 194,
            "winner": "Red"
        }

        assert fight_dict == expected_output
        assert len(fight_dict) == len(expected_output)

    @classmethod
    def test_fight_get_fight_information(cls, fight_example):
        default_date = datetime.date(2019, 2, 13)

        fight = fight_example

        fight_info = fight.get_fight_information()

        desired_result = {
            'code': 1,
            'referee': "Loris",
            'location': "Las Vegas, USA",
            'date': default_date,
            'winner': "Red"
        }

        assert fight_info == desired_result
        assert len(fight_info) == len(desired_result)
