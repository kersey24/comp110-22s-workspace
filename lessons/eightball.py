"""An oracle that predicts the future."""

from random import randint

input("Ask a yes/no question: ")

response: int = randint(0, 3)

if response == 0: 
    print("Most definetly")
elif response == 1: 
    print("Highly likely")
elif response == 2:
    print("Ask again later")
else: 
    response == 3
    print("No way, not a chance")


def repeat(word: str, x: int) -> str: 
    new_word: str = ""
    i: int = 0 
    while i < len(word): 
        y: int = 0 
        while y < x: 
            new_word += word[i]
            y += 1 
        i += 1 
    return new_word


def indices_word(word: str, char: str) -> str:
    new_word: str = ""
    i: int = 0 
    while i < len(word): 
        if word[i] == char:
            new_word += str(i)
        i += 1 
    return new_word