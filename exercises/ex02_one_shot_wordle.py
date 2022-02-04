"""A one shot attempt at wordle!"""

__author__: str = "730401052"

secret: str = "python"
guess_word: str = input(f"What is your {len(secret)}-letter guess? ")

while len(guess_word) != len(secret): 
    guess_word = input(f"That was not {len(secret)} letters! Try again: ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

check: int = 0 
result: str = ""

while check < len(secret): 
    if guess_word[check] == secret[check]: 
        result = result + GREEN_BOX
    else: 
        same_character: bool = False
        alternate: int = 0
        while not same_character and alternate < len(secret): 
            if guess_word[check] == secret[alternate]:
                same_character = True 
            else: 
                alternate = alternate + 1 
        if same_character is True: 
            result = result + YELLOW_BOX
        else: 
            result = result + WHITE_BOX

    check = check + 1

print(result)

if guess_word == secret: 
    print("Woo! You got it!")
else: 
    print("Not quite. Play again soon!")