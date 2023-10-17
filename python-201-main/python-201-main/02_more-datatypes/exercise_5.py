users = {"mary": 22, "caroline": 99, "harry": 24}

print(users["mary"])

users['harry'] = 20
print(users['harry'])

users['ludvik'] = 9
print(users['ludvik'])  
print(users)

users.pop('harry')
print(users)

caroline = users.get("caroline")
print(caroline)

users.update({"melanie": 27})
print(users)