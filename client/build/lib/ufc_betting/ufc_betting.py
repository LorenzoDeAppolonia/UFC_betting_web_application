import requests
from .client_helpers.convert_fight import from_json_to_fight
from .client_helpers.convert_fighter import from_json_to_fighter
from .client_helpers.convert_bet import from_json_to_bet
from .configuration import URL_application
from .bet import Bet
from .fight import Fight
from .client_helpers.error_handler import handle_error
from .fighter import Fighter
import json


class UFCBetting:

    @staticmethod
    def get_all_fights():
        response = requests.get(url=f'{URL_application}/fights/')

        if response.status_code == 200:
            json_list = response.json()
            fight_list = [from_json_to_fight(el) for el in json_list]
            return fight_list

        return handle_error(response)

    @staticmethod
    def get_fights_by_date(date):
        response = requests.get(url=f'{URL_application}/fights/', params={'date': date})

        if response.status_code == 200:
            json_list = response.json()
            fight_list = [from_json_to_fight(el) for el in json_list]
            return fight_list

        return handle_error(response)

    @staticmethod
    def get_fights_by_location(location: str):
        response = requests.get(url=f'{URL_application}/fights/', params={'location': location})
        if response.status_code == 200:
            json_list = response.json()
            fight_list = [from_json_to_fight(el) for el in json_list]
            return fight_list

        return handle_error(response)

    @staticmethod
    def get_fight_by_id(id: int):
        response = requests.get(url=f'{URL_application}/fights/{id}')
        if response.status_code == 200:
            json = response.json()
            fight = from_json_to_fight(json)
            return fight

        return handle_error(response)

    @staticmethod
    def add_fight(fight: Fight):
        fight_dict = fight.to_dict()
        response = requests.post(url=f'{URL_application}/fights/', json=fight_dict)
        if response.status_code == 201:
            return True

        handle_error(response)

    # ===================================================================================================
    #                        FIGHTERS

    @staticmethod
    def get_all_fighters():
        response = requests.get(url=f'{URL_application}/fighters/')
        if response.status_code == 200:
            json_list = response.json()
            fighters_list = [from_json_to_fighter(el) for el in json_list]
            return fighters_list

        handle_error(response)

    @staticmethod
    def get_fighters_by_name(name: str):
        response = requests.get(url=f'{URL_application}/fighters/', params={'name': name})
        if response.status_code == 200:
            json_list = response.json()
            fighters_list = [from_json_to_fighter(el) for el in json_list]
            return fighters_list

        return handle_error(response)

    @staticmethod
    def get_fighters_by_stance(stance: str):
        response = requests.get(url=f'{URL_application}/fighters/', params={'stance': stance})
        if response.status_code == 200:
            json_list = response.json()
            fighters_list = [from_json_to_fighter(el) for el in json_list]
            return fighters_list

        return handle_error(response)

    @staticmethod
    def add_fighter(fighter: Fighter):
        fighter_dict = fighter.to_dict()
        response = requests.post(url=f'{URL_application}/fighters/', json=fighter_dict)
        if response.status_code == 201:
            return True

        handle_error(response)

    @staticmethod
    def delete_fighter(fighter: Fighter):
        response = requests.delete(url=f'{URL_application}/fighters/{int(fighter.code)}')
        if response.status_code == 200:
            return True

        handle_error(response)

    # ===================================================================================================
    #                        BETS

    @staticmethod
    def place_bet(bet: Bet):
        bet_dict = bet.to_dict()
        response = requests.post(url=f'{URL_application}/bets/', json=bet_dict)
        if response.status_code == 201:
            return True

        handle_error(response)

    @staticmethod
    def end_event():
        response = requests.post(url=f'{URL_application}/bets/results')
        if response.status_code == 201:
            return True

        handle_error(response)

    @staticmethod
    def get_all_bets():
        response = requests.get(url=f'{URL_application}/bets/')
        if response.status_code == 200:
            json_list = response.json()
            bets_list = [from_json_to_bet(el) for el in json_list]
            return bets_list

        handle_error(response)

    @staticmethod
    def get_bet_by_code(code: int):
        response = requests.get(url=f'{URL_application}/bets/{code}')
        if response.status_code == 200:
            json = response.json()
            bet = from_json_to_bet(json)
            return bet

        return handle_error(response)


