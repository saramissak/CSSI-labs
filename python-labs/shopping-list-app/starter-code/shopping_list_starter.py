#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

choice = ""

print("Welcome to the shopping list app!")

shopping_list = []

while choice.lower() != "e":
    print("Please choose your action from the following list:")
    print("a. Add an item to the list")
    print("b. Remove an item from the list")
    print("c. Check to see if an item is on the list")
    print("d. Show all items on the list")
    print("e. exit")


    choice = raw_input("Enter your choice [a|b|c|d|e]:")

    # Your code below! Handle the cases when the user chooses a, b, c, d, or e

    if choice.lower() == 'a':
        added = raw_input("What would you like to add? ")
        if added in shopping_list:
            print("that is already on the list")
        else:
            splitted = added.split(",")
            for item in splitted:
                shopping_list.append(item.strip(" "))

    elif choice.lower() == 'b':
        removed_item = raw_input("What would you like to remove? (enter item name) ")
        if removed_item in shopping_list:
            you_sure = raw_input("Are you sure you want to remove this item? ")
            if you_sure == "yes":
                shopping_list.remove(removed_item)
        else:
            print("That is not on the list")
    elif choice.lower() == 'c':
        looking_for = raw_input("What item are you looking for? (enter item name) ")
        inList = False
        for item in shopping_list:
            if looking_for == item:
                inList = True
                print("That item is in the list!")
        if inList == False:
            print("this item is not in the list")
            want_to_add = raw_input("Would you like to add it to the list? ")
            if want_to_add == "yes":
                shopping_list.append(looking_for)
    elif choice.lower() == 'd':
        print(shopping_list)
    elif choice.lower() == 'e':
        break
    else:
        print("That is not a valid choice. Please try again! ")
