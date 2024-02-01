class WeightClass:
    def __init__(self, code: int, weight: str):
        self.__code = code
        self.__weight = weight

    @property
    def code(self) -> int:
        return self.__code

    @property
    def weight(self) -> str:
        return self.__weight

    def __str__(self):
        return f"Code: {self.__code} | Weight: {self.__weight}"

    def __eq__(self, other):
        if self.code == other.code:
            return True

        return False

    def to_dict(self):
        return {
            "code": self.code, "weight": self.weight
            }
