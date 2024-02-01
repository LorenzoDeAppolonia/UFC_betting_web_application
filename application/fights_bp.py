from flask import Blueprint, jsonify, request, make_response
from service.fight_service import FightService
from application.application_helpers.conversions import from_json_to_fight
from exceptions.ufc_betting_error import UfcBettingError

fights_bp = Blueprint('fights', __name__, url_prefix='/fights')


@fights_bp.route('/', methods=['GET', 'POST'])
def fights():
    if request.method == 'GET':
        date_str = request.args.get('date')
        location = request.args.get('location')
        try:
            if date_str:
                fights_list = FightService.get_all_fights_by_date(date_str)
            elif location:
                fights_list = FightService.get_all_fights_by_location(location)
            else:
                fights_list = FightService.get_all_fights()

            if not fights_list:
                response = make_response(jsonify({"error": "No fights found"}), 404)
                return response
            else:
                response = make_response(jsonify(fights_list), 200)
                return response

        except UfcBettingError as e:
            response = make_response(jsonify({'error': str(e)}), 500)
            return response

    elif request.method == 'POST':

        fight_data = request.json
        print(fight_data)
        fight = from_json_to_fight(fight_data)
        try:
            FightService.add_fight(fight)
            response = make_response(jsonify(fight.to_dict()), 201)
            return response
        except UfcBettingError as e:
            response = make_response(jsonify({'error': str(e)}), 500)
            return response

    response = make_response(jsonify({'error': 'Bad Request'}), 400)
    return response


@fights_bp.route('/<int:fight_id>', methods=['GET'])
def get_fight(fight_id):
    if not fight_id:
        response = make_response(jsonify({'error': 'Missing fight_id parameter'}), 400)
        return response

    try:
        fight = FightService.get_fight_statistics(fight_id)

        if fight is None:
            response = make_response(jsonify({f'error': f'Fight with code {fight_id} not found'}), 404)
            return response
        else:
            response = make_response(jsonify(fight), 200)
            return response

    except UfcBettingError as e:
        response = make_response(jsonify({'error': str(e)}), 500)
        return response
