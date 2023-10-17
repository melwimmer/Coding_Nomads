# Create a sarcastic program that asks a user for their honest opinion,
# then prints the same sentence back to them in aLtErNaTiNg CaPs.

opinion = input("please tell us you honest opinion")

altered_opinion = ""

for n in range(len(opinion)):
    if n %2 == 0:
        altered_opinion += opinion[n].upper()
    else:
        altered_opinion += opinion[n].lower()
print(altered_opinion)


