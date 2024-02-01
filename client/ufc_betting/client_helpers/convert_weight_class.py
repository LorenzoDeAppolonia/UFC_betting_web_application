from ..weight_class import WeightClass


def from_json_to_weight_class(weight_class_data):
    weight_class = WeightClass(

        code=weight_class_data['code'],

        weight=weight_class_data['weight']

    )

    return weight_class
