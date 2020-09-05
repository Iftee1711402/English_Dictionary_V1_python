import json
from difflib import get_close_matches

# data = json.load(open("English_dictionary_V1/data.json"))
data = json.load(open("data.json"))


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]

    elif len(get_close_matches(word, data.keys())) > 0:
        y_or_n = input(f"\nDid you mean '{get_close_matches(word, data.keys())[0]}' instead? [y/n]: ")

        if y_or_n == "Y" or y_or_n == "y":
            return data[get_close_matches(word, data.keys())[0]]
            
        elif y_or_n == "N" or y_or_n == "n":
            return "The word does not exist."
            
        else:
            return "we didn't understand your entry"
            
    else:
        return "The word does not exist."
        
    
def driver_function():
    word = input("\nenter word: " + "\n")

    choice = True
    while choice != False:

        output = translate(word)

        if type(output) == list:
            for item in output:
                print(f"\n{item}")
        else:
            print(f"\n{output}")

        choice = input("\n\nwould you like to find meaning of another word? [y/n]: ")
        if choice == "Y" or choice == "y":
            return driver_function()
        elif choice == "n" or choice == "n":
            print("alright, that'll be all, goodbye!")
            return
            


driver_function()