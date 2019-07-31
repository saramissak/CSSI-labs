some_list = []
dictionary = {
    "strawberry": "red thing",
    "banana": "yes"
}

dictionary["banana"] = "Yellow thing"
dictionary["potato"] = "underground thing"
dictionary["blueberry"] = "blue things"
print(dictionary)

fruit = raw_input("What fruit do you want to know about? ")
if fruit not in dictionary:
    print("not in list")
else:
    print(dictionary[fruit])
