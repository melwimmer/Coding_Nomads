# Write a script that takes in a string from the user.
# Using the `split()` method, create a list of all the words in the string
# and print back the most common word in the text.
from collections import Counter


Text =''' Jellyfish and sea jellies are the informal common names given to the medusa-phase of certain gelatinous members of the subphylum Medusozoa, a major part of the phylum Cnidaria. Jellyfish are mainly free-swimming marine animals with umbrella-shaped bells and trailing tentacles, although a few are anchored to the seabed by stalks rather than being mobile. The bell can pulsate to provide propulsion for highly efficient locomotion. The tentacles are armed with stinging cells and may be used to capture prey and defend against predators. Jellyfish have a complex life cycle; the medusa is normally the sexual phase, which produces planula larvae that disperse widely and enter a sedentary polyp phase before reaching sexual maturity.''' #input("tell me a story")

Listtext = Text.split()
# print(Listtext)

print(Counter(Listtext).most_common(1))






