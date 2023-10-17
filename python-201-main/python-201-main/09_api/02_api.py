# Collect the name from your player
# Check whether it meets the length requirements for the API call
# Ping the Uzby API to create a new random name for your player,
#   using the length of their given name as input
# Inform the player about their in-game name

import requests
player_name_good = False


while player_name_good == False:
    player_name = input("Please tell us us your first name ")
    length = len(player_name)
    if length >= 40:
        print("your name is too long. please type a name that has 2-40 chars")
    elif length <2:
        print("your name is too short. please type a name that has 2-40 chars")
    else:
        url = f"https://uzby.com/api.php?min={2}&max={length}"

        response = requests.get(url)
        print(f'Your player name is {response.text}')
        player_name_good = True
        break