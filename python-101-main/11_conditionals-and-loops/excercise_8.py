s = input("File Name? ")
v = " "
for i in range(len(s)):
    if i % 2:
        v += s[i].upper()
    else:
        v += s[i].lower()
print(v) 

     

    #print(i)
#print(s[1])