# Print out every prime number between 1 and 1000.

# numero que no es divisible entre ningun otro n[umero excepto el mismo]
# m = [2,]

# for number in range(2,100):
#     for n in range (2,100):
#         number + 1
#         if number % n == 0:
#             print(number, n)

#if # is not divisible by 2, 3, 5, 7 it will give a decimal, if it gives a decimal it's prime, so add it to the list and exclude it. 
# if # divisible by 


# m = [2]
# for i in m:
#     m.append(i)
#     print(i)
# #         if (number % i) != 0:
# #             m.append(i)

# # print(m)

m = [2]
for number in range(2,1000):
    for i in m:
        if (number % i) == 0:
            break
    else:
            m.append(number)
print(m)



# for number in range(2,10):
#        for i in range(2,number):
#            if (number % i) == 0:
#                break
#        else:
#            print(number)
