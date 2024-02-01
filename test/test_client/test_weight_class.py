class TestClientWeightClass:

    @classmethod
    def test_weight_class_id(cls, weight_class_example):
        assert weight_class_example.code == 3

    @classmethod
    def test_weight_class_category(cls, weight_class_example):
        assert weight_class_example.weight == "Heavyweight"

    @classmethod
    def test_fighter_equality(cls, weight_class_example, other_weight_class_example):
        assert weight_class_example.code == other_weight_class_example.code

    @classmethod
    def test_fighter_inequality(cls, weight_class_example, other_weight_class_example_2):
        assert weight_class_example.code != other_weight_class_example_2.code

    @classmethod
    def test_weight_class_str(cls, weight_class_example):
        output_string = "Code: 3 | Weight: Heavyweight"
        assert str(weight_class_example) == output_string

    @classmethod
    def test_to_dict(cls, weight_class_example):
        expected_dict = {
            "code": weight_class_example.code,
            "weight": weight_class_example.weight,
        }

        assert weight_class_example.to_dict() == expected_dict
        assert len(weight_class_example.to_dict()) == len(expected_dict)
