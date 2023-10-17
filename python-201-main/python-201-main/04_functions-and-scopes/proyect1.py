def titlecase(text):
    sentence = ""
    for word in text.split():
        capword= word.capitalize()
        sentence += capword + " "
    return(sentence)

print(titlecase("hola soy meme"))


