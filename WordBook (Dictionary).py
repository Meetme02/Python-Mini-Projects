import json
from difflib import get_close_matches

elements=json.load(open("wordbook.json"))

def findmeaning(word):
    if word.lower() in elements:
        return elements[word.lower()]
    elif word.upper() in elements:
        return elements[word.upper()]
    elif word.title() in elements:
        return elements[word.title()]
    
    elif word.upper() in elements:
        return elements[word]
    elif len(get_close_matches(word,elements.keys()))> 0:
        closematches=(get_close_matches(word,elements.keys())[0])
        user_decision = input("Are you looking for %s instead? [Y/N] " %closematches)

        if user_decision == 'Y' or user_decision == 'y':
            return elements[get_close_matches(word,elements.keys())[0]]
        elif user_decision == "N" or user_decision == "n":
            return "I can't find your word. I'm Sorry."
        else:
            return "Sorry! I cant find your word."
    else:
        return "I can't find this word. Please look for spelling mistakes."
    
word= input("Type your word here: ")
output= findmeaning(word)

if type(output)== list:
    for i in output:
        print(i)
else:
    print(output)