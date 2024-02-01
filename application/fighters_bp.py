from flask import Blueprint, jsonify, send_file, request, make_response
from service.fighter_service import FighterService
from service.fight_service import FightService
from application.application_helpers.conversions import from_json_to_fighter
from exceptions.ufc_betting_error import UfcBettingError

fighters_bp = Blueprint('fighters', __name__, url_prefix='/fighters')


@fighters_bp.route('/', methods=['GET', 'POST'])
def fighters():
    if request.method == 'GET':
        name = request.args.get('name')
        stance = request.args.get('stance')
        try:
            if name:
                fighters_list = FighterService.get_all_fighters_by_name(name)
            elif stance:
                fighters_list = FighterService.get_all_fighters_by_stance(stance)
            else:
                fighters_list = FighterService.get_all_fighters()

            response = make_response(jsonify(fighters_list), 200)
            return response
        except UfcBettingError as e:
            response = make_response(jsonify({'error': str(e)}), 500)
            return response

    elif request.method == 'POST':
        try:
            fighter_data = request.json
            fighter = from_json_to_fighter(fighter_data)
            success = FighterService.add_fighter(fighter)
            if success:
                response = make_response(jsonify(fighter.to_dict()), 201)
                return response
            else:
                response = make_response(jsonify({"error": "Failed to add fighter"}), 500)
                return response

        except UfcBettingError as e:
            response = make_response(jsonify({'error': str(e)}), 500)
            return response

    response = make_response(jsonify({'error': 'Bad Request'}), 400)
    return response


@fighters_bp.route('/<int:fighter_id>', methods=['GET', 'DELETE'])
def get_fighter(fighter_id):
    if request.method == 'GET':
        try:
            fighter = FighterService.get_fighter_statistics(fighter_id)

            if fighter is None:
                response = make_response(jsonify({'error': f'Fighter with code {fighter_id} not found'}), 404)
                return response

            response = make_response(jsonify(fighter), 200)
            return response

        except UfcBettingError as e:
            response = make_response(jsonify({'error': str(e)}), 500)
            return response

    elif request.method == 'DELETE':
        try:
            result = FighterService.delete_fighter_by_id(fighter_id)

            if result is None:
                response = make_response(jsonify({"error": "Fighter not found"}), 404)
                return response
            else:
                response = make_response(jsonify({"success": "Fighter deleted"}), 200)
                return response

        except UfcBettingError as e:
            response = make_response(jsonify({'error': str(e)}), 500)
            return response


@fighters_bp.route('/plot/<int:fighter_code>')
def fighter_stats(fighter_code):
    try:
        fighter = FighterService.get_fighter_by_code(fighter_code)

        if fighter is None:
            response = make_response(jsonify({"error": "Fighter not found"}), 404)
            return response
        else:
            record = FightService.get_fighter_record(fighter_code)
            buf = FighterService.generate_plot(record, fighter.name)
            return send_file(buf, mimetype='image/png', as_attachment=False)

    except UfcBettingError as e:
        response = make_response(jsonify({'error': str(e)}), 500)
        return response
