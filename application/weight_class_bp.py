from flask import Blueprint, jsonify, make_response
from service.weight_class_service import WeightClassService
from exceptions.ufc_betting_error import UfcBettingError

weight_class_bp = Blueprint('weight-classes', __name__, url_prefix='/weight-classes')


@weight_class_bp.route('/')
def weight_classes():
    try:
        result = WeightClassService.get_all_weight_classes()

        if result is None:
            response = make_response(jsonify({"error": "No weight classes found"}), 404)
            return response

        response = make_response(jsonify(result), 200)
        return response

    except UfcBettingError as e:
        response = make_response(jsonify({'error': str(e)}), 500)
        return response


@weight_class_bp.route('/<int:code>')
def get_weight_class_by_code(code):
    try:
        weight_class = WeightClassService.get_weight_class_statistics(code)
        if weight_class is None:
            response = make_response(jsonify({"error": f"Weight class with code {code} not found"}), 404)
            return response
        response = make_response(jsonify(weight_class), 200)
        return response

    except UfcBettingError as e:
        response = make_response(jsonify({'error': str(e)}), 500)
        return response
