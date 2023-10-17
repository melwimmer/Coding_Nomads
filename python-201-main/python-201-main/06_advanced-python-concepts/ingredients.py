def prepare(ingredient):
    return f"cooked {ingredient}"

carrot = "carrot"
salt = "salt"
potato = "potato"

#Esto se usa para evitar que cuando importo un archivo, que se imprima el resultado de las papas. Como lo hice en soup.py
if __name__ == "__main__": #if you run this program directly instead of importing it as a module, do the following:
    print(prepare(potato))
