import random

word = str(raw_input("What would you like to reverse "))

def reverse(word):
    length = len(word)
    reversed_word = ""
    while length > 0:
        reversed_word = reversed_word + word[length-1]
        length -= 1
    return reversed_word

print(reverse(word))


def sum_to_n(number):
    sum =0
    for i in range(number+1):
        sum +=i
    return sum

print(sum_to_n(5))

def is_triangle(s1, s2, s3):
    if s1 + s2 < s3:
        return False
    if s2 + s3 < s1:
        return False
    if s1 + s3 < s2:
        return False
    return True

print is_triangle(10, 15, 30)

def roll_dice(num):
    sum = 0
    while num > 0:
        sum += random.randint(1, 6)
        num -=1
    return sum

print(roll_dice(2))

def is_prime(num):
    count = 2
    while count < num:
        if num % count == 0:
            return True
        count += 1
    return False

print(is_prime(12))


def snake_case(word):
    snaked = ""
    splitted = word.split(" ")
    splitted = word.lower()
    for char in splitted:
        snaked += char + "_"
    return snaked

print(snake_case("CamelCased word"))

prompt = raw_input("Tell me a question: ")

def get_number_input(prompt):
    isNum = True
    number = raw_input(prompt)
    askAgain = True
    while isNum == True:
        try:
           int(number)
           askAgain = True
        except ValueError:
            askAgain = False

        if askAgain == False:
            number = raw_input("That is not a number!")
        else:
                print("That is a number!!")
                isNum = False


get_number_input(prompt)
