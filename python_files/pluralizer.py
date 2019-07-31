number = int(raw_input("Number: "))
word = raw_input("Word: ")


if bool(word == "tooth") & (number > 1 or number ==0):
    print(str(number)+ " " + word+"teeth")
elif bool(word == "mouse") & (number > 1 or number ==0):
    print(str(number)+ " " + word+"mice")
elif bool(word == "ox") & (number > 1 or number ==0):
    print(str(number)+ " " + word+"oxes")
elif bool(word == "fish") & (number > 1 or number ==0):
    print(str(number)+ " " +word)
elif bool(word[-3:] == "ife") & (number > 1 or number ==0):
    print(str(number)+ " " + word[:-3] + "ives")
elif bool(word[-2:] == "sh") or bool(word[-2:] == "ch") & (number > 1 or number ==0):
    print(str(number) + " " + word + "es")
elif bool(word[-2:] == "us") & (number > 1 or number ==0):
    print(str(number)+ " " + word[:-2] + "i")
elif bool((word[-2:] == "ay" or word[-2:] == "oy" or word[-2:] == "ey" + word[-2:] == "uy")) and (number > 1 or number ==0): #ay/oy/ey/uy
    print(str(number)+ " " + word + "s")

elif bool(word[-1:]) == "y" & (number > 1 or number ==0):
    print(str(number)+ " " + word[:-1] + "ies")
elif number > 1 or number ==0:
    print(str(number)+ " " + word+"s")
else:
    print(str(number)+ " " +word)
