grade_level = raw_input('What grade are you in? ')
isValue = True
try:
   val = int(grade_level)
except ValueError:
    isValue = False

if isValue == True:
    if grade_level == "k":
        print("You are in kindergarten")
    elif int(grade_level) <= 5 & int(grade_level) >0:
        print("youre in elementry school")
    elif int(grade_level) <= 8:
        print("youre in elementry school")
    elif int(grade_level) <= 12:
        print("youre in elementry school")
    elif int(grade_level) <= 0  & int(grade_level) > 12:
        print('That is not a grade')
else:
    print("error: not a number")
