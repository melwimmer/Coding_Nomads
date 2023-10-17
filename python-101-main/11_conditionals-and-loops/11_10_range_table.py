# Read up on `range()` and additional options for `print()`.
# Then use a loop to print the following table to the console:
#
# 0 1 2 3 4 5 6 7 8 9
# 10 11 12 13 14 15 16 17 18 19
# 20 21 22 23 24 25 26 27 28 29
# 30 31 32 33 34 35 36 37 38 39
# 40 41 42 43 44 45 46 47 48 49


#Split the lists?

# This one works, but it's not exactly the best one, and not exactly the same. 

# r= range(0,50)

# m = []
# n = []
# x = []
# y = []
# z = []
# for i in r: 
#     if i < 10:
#         m.append(i) 
#     elif i < 20:
#         n.append(i)
#     elif i < 30:
#         x.append(i)
#     elif i <40:
#         y.append(i)
#     else:
#         z.append(i)
# print(m, n, x, y, z, sep ='\n')


#This one works, but not the best!

# r= range(0,50)

# a = ''
# b = ''
# c = ''
# d = ''
# e = ''

# for i in r: 
#     if i < 10:
#         a += str(i)
#         a += ' ' 
#     elif i < 20:
#         b += str(i)
#         b += ' '  
#     elif i < 30:
#         c += str(i)
#         c += ' ' 
#     elif i <40:
#         d += str(i)
#         d += ' ' 
#     else:
#         e += str(i)
#         e += ' ' 

# print(a, b, c, d, e, sep = '\n')

# This one is the best solution!!!
a=''
for i in range(0,50):
  if i % 10!=0:
      a += str(i)
      a += " "
  else:
        a += '\n'
        a += str(i)
        a += " "

print(a)

#Another method, not my code, but someone elses:

# for x in range (0, 50):
#     print(x,end = " ")
#     if x % 10 == 9:
#         print(end ="\n")

for x in range (0, 50):
    print(x, end =" ")
    if x % 10 == 9:
        print(end ="\n")







         
        

  


        
