# Letter Frequency

# Work out the frequency of letters in "Old Marley was as dead as a door-nail"

phrase = "Old Marley was as dead as a door-nail"
phrase = phrase.replace(" ", "")
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

for letter in alphabet:
    freq = 0
    for char in phrase:
        if letter == char:
            freq = freq + 1
    if freq != 0:
        print(str(letter) + " = " + str(freq))

print(str(len(phrase)))