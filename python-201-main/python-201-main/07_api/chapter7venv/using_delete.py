#The DELETE request is also capable of sending information to the server like a POST or PUT request. 
#To make a DELETE request to the API you have been working on, you do not need to send any information in the body of the request.

#As with PUT, you can specify the user you want to delete by utilizing path variables. 
#For example, to delete the user with id 50 you will add the id to the URL as a path variable:

# import requests

# base_url = "http://demo.codingnomads.co:8080/tasks_api/users"
# response = requests.delete(base_url + "/50")
# print(response.status_code)