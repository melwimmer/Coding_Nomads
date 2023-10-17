filename = "operators.pdf"
extension = False
file = ""
for char in filename:
    if char == ".":
        extension = True
    if extension == True:
        file += char
if file == "pdf":
    print("It's a pdf")



referencia = "Adams, M. R., Moss, M. O., & McClure, P. (2016). Food Microbiology (4th ed.). Royal Society of Chemistry."
ext = False
referencialista1 = ""
for char in referencia:
    if char != "(":
        referencialista1 += char.upper()
    else:
        break 
print(referencialista1) 

referencialista2 = ""
for char in referencia:
    if char == "(":
        ext = True
    if ext == True:
        referencialista2 += char
print(referencialista2)

referencialista = referencialista1 + referencialista2
print(referencialista)
