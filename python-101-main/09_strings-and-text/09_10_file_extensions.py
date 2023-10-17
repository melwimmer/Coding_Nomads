# Use a Python string method to prove which of the following files
# are .pdf files, and which aren't.
# Call the method on each file string and print() Python's response.

file_1 = "operators.pdf"
file_2 = "snowfall.jpg"
file_3 = "uncle-joes-wedding.doc"
file_4 = "invitation.pdf"

def pdf_function (file):
    print(file.endswith('pdf'))

pdf_function(file_1)
pdf_function(file_2)
pdf_function(file_3)
pdf_function(file_4)
