import requests
from pathlib import Path

#for wordle

url = "https://wordle-answers-solutions.p.rapidapi.com/today"

headers = {"this is where the key would go, but I deleted it to upload to github."
	
}

response = requests.get(url, headers=headers)
word_lower = response.json()['today'].lower()

print(response.json()['today'])
print(word_lower)

#for dictionary

url_dictionary = f'https://api.dictionaryapi.dev/api/v2/entries/en/{word_lower}'
response2 = requests.get(url_dictionary)
list_for_dict = response2.json()[0]['meanings'][0]['definitions']
print(response2.json()[0]['meanings'][0]['definitions'][0]['definition'])
# dict_def = {}
# dict_def[0]:response2.json()[0]['meanings'][0]['definitions'][0]['definition']
# dict_def[1]:"a"
# print(dict_def)


def definitions(list, definition):
    dict_def = {}
    counter=0
    for i in list:
        dict_def[counter+1]=list[counter][definition]
        counter += 1
    return(dict_def)

dictionary_of_definitions=str((definitions(list_for_dict,'definition')))
html= f'<p>The word of the day is {word_lower}</p><p>These are the following definitions {dictionary_of_definitions}'



file = Path('09_api').joinpath('someexercise.html')
file.write_text(html)

#to see the webpage, you open it with open with browser. 

