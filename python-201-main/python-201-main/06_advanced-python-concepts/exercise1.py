listcomp = [x*2 for x in range(5)]
setcomp = {x*2 for x in range(5)}
dictcomp = {k: v*2 for (k, v) in {"a": 1, "b": 2}.items()}

print(listcomp)
print(setcomp)
print(dictcomp)

dict_1 = {"a": 1, "b": 2}
dict_2 = {k: v*2 for (k, v) in dict_1.items()}
print(dict_2)