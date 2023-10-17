import requests


url = "http://demo.codingnomads.co:8080/tasks_api/users"
body ={
    "first_name": "Miow Miow", 
    "last name": "Cat",
    "email": "kittens@aresocute.com"
}

response = requests.post(url, json=body)
print(response.status_code)