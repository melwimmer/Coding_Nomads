# Read in the first number from `integers.txt`
# and perform a calculation with it.
# Make sure to catch at least two possible Exceptions (`IOError` and `ValueError`)
# with specific `except` statements, and continue to do the calculation
# only if neither of them applies.

file_name = '/home/meme/python-301-main/python-301-main/05_exceptions/integers.txt'

numbers_text = []


try:
    with open(file_name,"r") as fin:
        contents = fin.readlines()
        number= int(input('give me a number to divide with'))
        division = int(contents[2])/number
        for line in contents:
            numbers_text.append(int(line.rstrip("\n")))
        print(numbers_text)
except IOError:
    print("Your file path is incorrect")
except TypeError:
    print("remember your file is a text file, you need to convert to int.")
except ValueError:
    print('You can only use numbers NO letters')
else:
    print(f'The result of the division is {division}')