class TestFighterClass:

    @classmethod
    def test_fighter_to_dict(cls, fighter_example):

        fighter_dict = fighter_example.to_dict()
        output_dict = {
            "code": 20,
            "name": "Daniel Corcks",
            "height": 165.1,
            "reach": 172.3,
            "stance": "Orthodox"
        }
        assert fighter_dict == output_dict
        assert len(fighter_dict) == len(output_dict)

    @classmethod
    def test_fighter_eq(cls, fighter_example, fighter_example_2):

        fighter_1 = fighter_example
        fighter_12 = fighter_example
        # fighter_3 = fighter_example_2

        # Test equality: fighter1 and fighter2 should be equal
        assert fighter_1 == fighter_12, "Fighter instances with same attributes should be equal"

        # Test inequality: fighter1 and fighter3 should not be equal
        # assert fighter_1 != fighter_3, "Fighter instances with different attributes should not be equal"






