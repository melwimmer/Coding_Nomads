# Use a built-in Python module to tell you the current date and time.
# Research online, so you can print it in a readable manner.

# import datetime
# print(datetime.date.today.strftime("%m/%d/%Y"))

import datetime

# dd/mm/YY
d1 = datetime.date.today().strftime("%d/%m/%Y")
print(d1)

from datetime import datetime

# datetime object containing current date and time
# now = datetime.now()
 
# print("now =", now)

# dd/mm/YY H:M:S
dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)