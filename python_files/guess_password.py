password = "There's a panda on my bottle"
keep_guessing = True

while keep_guessing:
    guess = raw_input("What is your guess? ")
    if guess == password:
        keep_guessing = False
    else:
        print("please try again!")
print("Success")
