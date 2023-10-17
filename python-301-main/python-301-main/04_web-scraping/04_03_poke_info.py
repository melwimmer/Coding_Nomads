from bs4 import BeautifulSoup
import json
import requests


# Use the Pokemon API at https://pokeapi.co/ to assemble a team of your
# six favorite Pokémon.
# Your task is to fetch information about six Pokémon through the
# necessary API calls and include the information in your local script.
# This information should include at least:
# - name
# - number
# - types
#
# You can improve on your project even more by writing the data to a small
# `.html` page which allows you to also display the sprites of each Pokémon.
# Check out the guides they provide: https://pokeapi-how.appspot.com/page5

import json
import requests


list_of_pokemon = ['pikachu', 'charmander', 'ponyta', 'bulbasaur', 'ditto', 'squirtle', 'eevee']
for i in list_of_pokemon:
    # response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{i}")
    # data = response.json()

    # with open(f"python-301-main/04_web-scraping/pokemon_{i}.json", "w") as fout:
    #     json.dump(data, fout)

    with open(f"python-301-main/04_web-scraping/pokemon_{i}.json", "r") as fin:
        data1 = json.load(fin)

    # print(data1)
    print(i)
   
    p_name = data1["forms"][0]['name']
    p_number = data1["id"]
    p_types = data1["types"][0]['type']['name']
    print(f'The name of this pokemon is {p_name}')
    print(f'The number of this pokemon is {p_number}')
    print(f'The type of this pokemon is {p_types}')
