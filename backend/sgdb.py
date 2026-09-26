import requests

from backend import configparser
from configuration.constants import API_HEADER

def get_header():
    header  = API_HEADER
    header['Authorization'] = header['Authorization'].format(token = configparser.get_config('API','token'))
    print(header)
    return header
def search_game(term:str):

    res = requests.get(f'https://www.steamgriddb.com/api/v2/search/autocomplete/{term}',headers=get_header())

    return res.json()

def get_icon_url(game_id:int):
    res = requests.get(f'https://www.steamgriddb.com/api/v2/icons/game/{game_id}',headers=get_header())
    return res.json()

def get_coverart_url(game_id:int):
    res = requests.get(f'https://www.steamgriddb.com/api/v2/grids/game/{game_id}',headers=get_header())
    return res.json()

def get_banner_url(game_id:int):
    res = requests.get(f'https://www.steamgriddb.com/api/v2/heroes/game/{game_id}',headers=get_header())
    return res.json()

if __name__ == '__main__':
    #print(search_game('mario'))
    #print(get_icon(10))
    #print(get_coverart(10))
    print(get_banner_url(10))
