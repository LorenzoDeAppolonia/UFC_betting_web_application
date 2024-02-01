from flask import Blueprint, jsonify
from flask import request, make_response
from service.bet_service import BetService
from application.application_helpers.conversions import from_json_to_bet
from exceptions.ufc_betting_error import UfcBettingError

bet_bp = Blueprint('bets', __name__, url_prefix='/bets')


@bet_bp.route('/', methods=['GET', 'POST'])
def bets():
    try:
        if request.method == 'GET':
            bets_list = BetService.get_all_bets()
            response = make_response(jsonify(bets_list), 200)
            return response

        if request.method == 'POST':
            bet_data = request.json
            bet = from_json_to_bet(bet_data)
            BetService.add_bet(bet)
            response = make_response(jsonify(bet.to_dict()), 201)
            return response

    except UfcBettingError as e:
        response = make_response(jsonify({'error': str(e)}), 500)
        return response


@bet_bp.route('/<int:bet_code>', methods=['GET', 'PUT'])
def bet(bet_code):

    if not bet_code:
        response = make_response(jsonify({'error': 'Missing bet_code parameter'}), 400)
        return response

    if request.method == 'GET':
        try:
            bet = BetService.get_bet_statistics(bet_code)

            if bet:
                response = make_response(jsonify(bet), 200)
                return response
            else:
                response = make_response(jsonify({'error': f'Bet with code {bet_code} not found'}), 404)
                return response

        except UfcBettingError as e:

            response = make_response(jsonify({'error': str(e)}), 500)
            return response

    if request.method == 'PUT':
        data = request.json

        try:
            if 'amount' in data:

                BetService.change_bet_amount(code=bet_code, amount=float(data['amount']))

            if 'winner' in data:

                BetService.change_bet_winner(code=bet_code, winner=data['winner'])

            bet = BetService.get_bet_by_code(code=bet_code)
            response = make_response(jsonify(bet.to_dict()), 200)
            return response

        except UfcBettingError as e:

            response = make_response(jsonify({'error': str(e)}), 500)
            return response


@bet_bp.route('/results', methods=['POST'])
def bets_results():
    try:
        if BetService.set_all_bets_results():
            response = make_response(jsonify(BetService.get_all_bets()), 201)
            return response

        response = make_response(jsonify({'error': 'SQLAlchemyError'}), 400)
        return response

    except UfcBettingError as e:
        response = make_response(jsonify({'error': str(e)}), 500)
        return response

