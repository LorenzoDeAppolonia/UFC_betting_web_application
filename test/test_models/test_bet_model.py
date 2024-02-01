from db_models.bet import Bet
import datetime


class MockFight:
    def __init__(self, fighter_rc, fighter_bc):
        self.fighter_rc = fighter_rc
        self.fighter_bc = fighter_bc


class MockFighter:
    def __init__(self, name):
        self.name = name


class TestBetModel:

    def test_to_dict(self):

        bet = Bet(
            code=123,
            amount=50.0,
            date_bet=datetime.date(2024, 1, 9),
            fight_code=1,
            winner='Red',
            payoff=100.0
        )

        # Assuming Fight and Fighter have a name attribute
        bet.fight = MockFight(fighter_rc=MockFighter(name='Fighter RC'),
                              fighter_bc=MockFighter(name='Fighter BC'))

        # Expected output
        expected_output = {
            'code': 123,
            'amount': 50.0,
            'date_bet': datetime.date(2024, 1, 9).strftime('%Y-%m-%d'),
            'payoff': 100.0,
            'fight_code': 1,
            'winner': 'Red'
        }

        assert bet.to_dict() == expected_output
        assert len(bet.to_dict()) == len(expected_output)
