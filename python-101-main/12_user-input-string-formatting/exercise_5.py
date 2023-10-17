condition = True
while condition == True:
  prompt = input('say something: ')
  if prompt == 'quit':
    condition = False
  print(prompt[::-1])
print("bye!! (it's tiuq, btw. ;)")

prompt = None
while prompt != 'quit':
  prompt = input('say something: ')
  print(prompt[::-1])
print("bye!! (it's tiuq, btw. ;)")