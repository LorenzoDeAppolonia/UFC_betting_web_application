
class TestFight:

    @classmethod
    def test_fight_initialization_and_properties(cls, fight_example, fighter_example, weight_class_example):
        assert fight_example.code == 2
        assert fight_example.referee == 'Lui Castro'
        assert fight_example.location == 'Las Vegas, USA'
        assert fight_example.fight_date == '2024-01-01'
        assert fight_example.age_rc == 30
        assert fight_example.weight_rc == 75.2
        assert fight_example.win_streak_rc == 5
        assert fight_example.wins_rc == 10
        assert fight_example.losses_rc == 2
        assert fight_example.age_bc == 28
        assert fight_example.weight_bc == 73.8
        assert fight_example.win_streak_bc == 4
        assert fight_example.wins_bc == 8
        assert fight_example.losses_bc == 3
        assert fight_example.weight_class_code == 3
        assert fight_example.fighter_rc.name == "Gustavo Lopez"
        assert fight_example.fighter_bc.name == "Adrian Yanez"
        assert fight_example.winner == "Red"

    @classmethod
    def test_eq(cls, fight_example, fight_example_3):
        assert fight_example == fight_example_3

    @classmethod
    def test_eq_negative(cls, fight_example, fight_example_2):
        assert fight_example != fight_example_2

    @classmethod
    def test_str(cls, fight_example):
        expected_output = (
            f"Code: {fight_example.code} | Referee: {fight_example.referee} | Location: {fight_example.location} | "
            f"Fight Date: {fight_example.fight_date} | Age RC: {fight_example.age_rc} | Weight RC: {fight_example.weight_rc} | "
            f"Win Streak RC: {fight_example.win_streak_rc} | Wins RC: {fight_example.wins_rc} | Losses RC: {fight_example.losses_rc} | "
            f"Age BC: {fight_example.age_bc} | Weight BC: {fight_example.weight_bc} | Win Streak BC: {fight_example.win_streak_bc} | "
            f"Wins BC: {fight_example.wins_bc} | Losses BC: {fight_example.losses_bc} | Weight Class Code: {fight_example.weight_class_code} | "
            f"Fighter RC: {fight_example.fighter_rc.name} | Fighter BC: {fight_example.fighter_bc.name} | Winner Code: {fight_example.winner}")

        assert str(fight_example) == expected_output

    @classmethod
    def test_to_dict(cls, fight_example):
        expected_dict = {
            "code": fight_example.code,
            "referee": fight_example.referee,
            "location": fight_example.location,
            "fight_date": fight_example.fight_date,
            "age_rc": fight_example.age_rc,
            "weight_rc": fight_example.weight_rc,
            "win_streak_rc": fight_example.win_streak_rc,
            "wins_rc": fight_example.wins_rc,
            "losses_rc": fight_example.losses_rc,
            "age_bc": fight_example.age_bc,
            "weight_bc": fight_example.weight_bc,
            "win_streak_bc": fight_example.win_streak_bc,
            "wins_bc": fight_example.wins_bc,
            "losses_bc": fight_example.losses_bc,
            "weight_class_code": fight_example.weight_class_code,
            "winner": fight_example.winner,
            'fighter_bc_code': fight_example.fighter_bc_code,
            'fighter_rc_code': fight_example.fighter_rc_code,
        }

        assert fight_example.to_dict() == expected_dict
        assert len(fight_example.to_dict()) == len(expected_dict)
