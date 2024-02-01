from db_models.weight_class import WeightClass


class TestWeightClassModel:
    @classmethod
    def test_weight_class_to_dict(cls):

        weight_class = WeightClass(code=3, weight="Bantamweight")

        expected_output = {
            'code': 3,
            'weight': "Bantamweight"
        }

        assert weight_class.to_dict() == expected_output
        assert len(weight_class.to_dict()) == len(expected_output)