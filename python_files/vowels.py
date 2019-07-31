word = raw_input("Word: ")
i=0
for vowel in word:
    if vowel == "a" or vowel == "e" or vowel == "i" or vowel == "o" or vowel == "u":
        i=i+1
print(i)
