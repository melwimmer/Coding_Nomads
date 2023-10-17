import json

with open("python-301-main/04_web-scraping/films.json", "r") as fin:
    data1 = json.load(fin)

print(len(data1['data']['films']))  # OUTPUT: 21
print(type(data1))  # OUTPUT: <class 'list'>

# print((data1['data']['films']))

allmovies = []
running_time_list = []
print(data1['data']['films'][2]['title'])
print(len(data1['data']['films']))


counter = 0
for i in range(0,len(data1['data']['films'])):
    title = data1['data']['films'][counter]['title']
    director = data1['data']['films'][counter]['director']
    running_time = int(data1['data']['films'][counter]['running_time'])
    td = {}
    td[title] = director
    allmovies.append(td)
    running_time_list.append(running_time)
    counter += 1

    
print(allmovies)
print(running_time_list)

print(max(running_time_list))
