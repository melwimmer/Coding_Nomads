secret = "2349H30023388281E3299371l1l3094842O0333322883"
solution = ""

for char in secret:
    if char.isalpha():
        solution += char

#print(solution)

secret = "2349H30023388281E3299371l1l3094842O0333322883"
solution = ""

for char in secret:
    if char.isdigit():
        solution += char

#print(solution)

secret = "2349H30023388281E3299371l1l3094842O0333322883"
solution = ""

for char in secret:
    if char.isalpha():
        solution += char
        solution = solution.lower()
    
#print(solution)

secret = "2349H30023388281E3299371l1l3094842O0333322883"
solution = ""

for char in secret:
    if char.isalpha():
        solution += char
        solution = solution.lower()
solution_upper = solution[0:5:2].upper()
solution_lower = solution[1:5:2].lower()
#print(solution)
#print(solution_upper)
#print(solution_lower)

solution = "HELLO"
#print(solution)
alt_solution = ""

for char in solution:
    if char in solution[::2]:
        alt_solution += char.upper()
    elif char in solution[1::2]:
        alt_solution += char.lower()
    
print(alt_solution)
   
