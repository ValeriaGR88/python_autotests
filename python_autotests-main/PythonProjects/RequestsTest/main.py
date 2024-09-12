import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '17fd8a694d0a0da24d98f14104a464e6'
HEADER = {'Content-Type' : 'application/json',
          'trainer_token' : TOKEN}

BODY_ADD_POKEMON = {
    "name": "generate",
    "photo_id": 5
}

response_add_pokemon = requests.post(url=f'{URL}/pokemons', headers = HEADER, json = BODY_ADD_POKEMON)
print(response_add_pokemon.json())

POKEMON_ID = response_add_pokemon.json()['id']

BODY_PUT_POKEMON = {
    "pokemon_id": POKEMON_ID,
    "name": "New Name",
    "photo_id": 3
}


response_put_pokemon = requests.put(url=f'{URL}/pokemons', headers = HEADER, json = BODY_PUT_POKEMON)
print(response_put_pokemon.json())

BODY_ADD_POKEBALL = {
    "pokemon_id": POKEMON_ID   
}

response_add_pokeball = requests.post(url=f'{URL}/trainers/add_pokeball', headers = HEADER, json = BODY_ADD_POKEBALL)