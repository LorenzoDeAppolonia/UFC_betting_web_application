from ..bet import Bet


def from_json_to_bet(bet_data):
    bet = Bet(code=bet_data['code'],
              amount=bet_data['amount'],
              date_bet=bet_data['date_bet'],
              fight_id=bet_data['fight_code'],
              winner=bet_data['winner'],
              payoff=bet_data['payoff']
              )

    return bet
