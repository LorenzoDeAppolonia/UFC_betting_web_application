import requests
from .configuration import URL_application
from io import BytesIO


class Fighter:
    def __init__(self, name: str, height: float, reach: float, stance: str, code= None):
        self.__code = code
        self.__name = name
        self.__height = height
        self.__reach = reach
        self.__stance = stance

    @property
    def code(self) -> int:
        return self.__code

    @property
    def name(self) -> str:
        return self.__name

    @property
    def height(self) -> float:
        return self.__height

    @property
    def reach(self) -> float:
        return self.__reach

    @property
    def stance(self) -> str:
        return self.__stance

    def __eq__(self, other):
        if self.code == other.code:
            return True

        return False

    def plot_statistics(self):
        response = requests.get(url=f'{URL_application}/plot/{self.code}')
        if response.status_code == 200:
            image_bytes = BytesIO(response.content)
            with open(f'fighter_{self.code}_stats.png', 'wb') as f:
                f.write(image_bytes.read())
            return True
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return False

    def __str__(self):
        return f"Name: {self.__name} | Code: {self.__code} | Height: {self.__height} | Reach: {self.__reach} | Stance: {self.__stance}"

    def to_dict(self):
        return {
            "code": self.code, "name": self.name, "height": self.height,
            "reach": self.reach, "stance": self.stance
            }



