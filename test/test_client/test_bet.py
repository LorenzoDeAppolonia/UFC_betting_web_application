import datetime


class TestBet:

    @classmethod
    def test_bet_initialization(cls, bet_example):
        assert bet_example.code is None
        assert bet_example.amount == 51.5
        assert bet_example.date_bet == '2024-01-10'
        assert bet_example.fight_code == 19064
        assert bet_example.winner == 'Red'
        assert bet_example.payoff is None

    # @classmethod
    # def test_bet_equality(cls, bet_example, other_bet_example):
    #     assert bet_example.code == other_bet_example.code
    #
    # @classmethod
    # def test_bet_inequality(cls, bet_example, other_bet_example_2):
    #     assert bet_example.code != other_bet_example_2.code

    @classmethod
    def test_bet_str(cls, bet_example):
        output_string = "Code: None | Amount: 51.5 | Payoff: None | Date: 2024-01-10 | Fight code: 19064 | Winner: Red"
        assert str(bet_example) == output_string

    @classmethod
    def test_to_dict(cls, bet_example):
        expected_dict = {
            "amount": bet_example.amount,
            "date_bet": bet_example.date_bet,
            "fight_code": bet_example.fight_code,
            "winner": bet_example.winner,

        }

        assert bet_example.to_dict() == expected_dict
        assert len(bet_example.to_dict()) == len(expected_dict)
