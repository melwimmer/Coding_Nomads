import requests


url = "http://demo.codingnomads.co:8080/tasks_api/users/{id}"
body ={
    "first_name": "Miow Miow", 
    "last name": "Cat",
    "email": "kittens@aresocute.com"
}

response = requests.put(url, json=body)
print(response.status_code)