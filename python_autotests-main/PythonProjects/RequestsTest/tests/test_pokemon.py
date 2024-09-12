import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TRAINER_ID = '4519'

def test_get_trainers_status_code():
    response = requests.get(url=f'{URL}/trainers')
    assert response.status_code == 200



def test_get_trainers_my_id():
    response_my_id = requests.get(url=f'{URL}/trainers', params= {'trainer_id' : TRAINER_ID})
    assert response_my_id.json()["data"][0]["trainer_name"] == "Leroy"
