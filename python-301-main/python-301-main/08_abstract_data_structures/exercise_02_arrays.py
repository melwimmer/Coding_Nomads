import array
a = array.array('i', [0, 0, 0, 0, 0])


# 'i' for integers
# 'f' for floating point numbers
# 'u' for Unicode characters
# 'b' signed char

# access the element at index 2
print(a[2])  # 0

# modify the element at index 2
a[2] = 10
print(a[2])  # 10

a.append(20)
print(a)  # array('i', [0, 0, 10, 0, 0, 20])

a.insert(3, 30)
print(a)  # array('i', [0, 0, 10, 30, 0, 0, 20])



# Create an array of integers
a1 = array.array('i', [10, 20, 30, 40, 50])

# Remove and return the last element from the array
last = a1.pop()
print(last)  # 50
print(a1)  # array('i', [10, 20, 30, 40])

# Remove and return the element at index 2
middle = a1.pop(2)
print(middle)  # 30
print(a1)  # array('i', [10, 20, 40])