import os
import requests


class APIRequester:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint=''):
        try:
            response = requests.get(self.base_url + endpoint)
            response.raise_for_status()
            return response
        except requests.RequestException:
            pass


class SWRequester(APIRequester):
    def __init__(self):
        super().__init__('https://swapi.dev/api/')

    def get_sw_categories(self):
        response = self.get()
        if response:
            return list(response.json().keys())
        return []


def get_sw_info(self, sw_type):
    return self.get(sw_type)


def save_sw_data():
    requester = SWRequester()
    categories = requester.get_sw_categories()
    os.makedirs("data", exist_ok=True)

    for category in categories:
        data = requester.get_sw_info(category)
        with open(f'data/{category}.txt', 'w', encoding='utf-8') as file:
            file.write(data)
