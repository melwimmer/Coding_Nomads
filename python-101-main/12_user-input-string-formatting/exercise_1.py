user_response = input("What is your name? ")

print(user_response.upper())
print(user_response[::2])

response = "" 

for i in range(len(user_response)):
    if i % 2: 
        response += user_response[i].upper()
    else:
        response += user_response[i].lower()

print(response)

user_number = input("Write a number you want analized ")
print(int(user_number)**2)
