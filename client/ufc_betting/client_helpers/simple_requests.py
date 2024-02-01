import requests

# TODO MAKE SERVICE CLASS
def get_fighter_json_by_id(id: str):
    json = requests.get(url=f"http://localhost:5000/fighters/{id}").json()
    return json


def get_fight_json_by_id(id: str):
    json = requests.get(url=f"http://localhost:5000/fights/{id}").json()
    return json


def get_weight_class_json_by_id(id: str):
    json = requests.get(url=f"http://localhost:5000/weight-classes/{id}").json()
    return json
