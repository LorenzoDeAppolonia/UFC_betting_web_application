class TestFighter:

    @classmethod
    def test_fighter_id(cls, fighter_example):
        assert fighter_example.code == 1

    @classmethod
    def test_fighter_name(cls, fighter_example):
        assert fighter_example.name == 'John Jons'

    @classmethod
    def test_fighter_height(cls, fighter_example):
        assert fighter_example.height == 192.1

    @classmethod
    def test_fighter_reach(cls, fighter_example):
        assert fighter_example.reach == 198.2

    @classmethod
    def test_fighter_stance(cls, fighter_example):
        assert fighter_example.stance == 'Orthodox'

    @classmethod
    def test_fighter_equality(cls, fighter_example, other_example):
        assert fighter_example.code == other_example.code

    @classmethod
    def test_fighter_inequality(cls, fighter_example, other_example_2):
        assert fighter_example.code != other_example_2.code

    @classmethod
    def test_fighter_str(cls, fighter_example):
        expected_string = "Name: John Jons | Code: 1 | Height: 192.1 | Reach: 198.2 | Stance: Orthodox"
        assert str(fighter_example) == expected_string

    @classmethod
    def test_to_dict(cls, fighter_example):
        expected_dict = {
            "code": fighter_example.code,
            "name": fighter_example.name,
            "height": fighter_example.height,
            "reach": fighter_example.reach,
            "stance": fighter_example.stance,
        }

        assert fighter_example.to_dict() == expected_dict
        assert len(fighter_example.to_dict()) == len(expected_dict)
