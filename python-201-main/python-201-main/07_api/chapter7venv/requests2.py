import requests
from pprint import pprint
url = "http://demo.codingnomads.co:8080/tasks_api/users"
response= requests.get(url)
print(response.status_code)


# url2 = "http://demo.codingnomads.co:8080/tasks_api/tasks?userId=380&complete=true"
# response2= requests.get(url2)
# data = (response2.json())



response3= requests.get(url)
data = (response3.json())
pprint(data["data"][0])


# param = {"id": 381}



# response3= requests.get("http://demo.codingnomads.co:8080/tasks_api/users").json()["data"]
# # pprint(response3.json()["data"])

# for i in response3:
#     # if i[0]:
#     #     pprint(i)
#     if i['id'] == 381:
#         pprint(i)

