"""Exercise01 - Chardle - A cute step toward Wordle."""

__author__: str = "730401052"

guess_word: str = input("Enter a 5-character word: ")
if len(guess_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
guess_letter: str = input("Enter a single character: ")
if len(guess_letter) != 1: 
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + guess_letter + " in " + guess_word)

if guess_letter == guess_word[0]:
    print(guess_letter + " found at index 0")

if guess_letter == guess_word[1]:
    print(guess_letter + " found at index 1")

if guess_letter == guess_word[2]:
    print(guess_letter + " found at index 2")

if guess_letter == guess_word[3]:
    print(guess_letter + " found at index 3")

if guess_letter == guess_word[4]:
    print(guess_letter + " found at index 4")

count: int = 0

if guess_letter == guess_word[0]:
    count = count + 1 
    if guess_letter == guess_word[1]: 
        count = count + 1 
        if guess_letter == guess_word[2]:
            count = count + 1
            if guess_letter == guess_word[3]: 
                count = count + 1 
                if guess_letter == guess_word[4]: 
                    count = count + 1 
if count == 0: 
    if guess_letter == guess_word[1]:
        count = count + 1 
        if guess_letter == guess_word[2]: 
            count = count + 1 
            if guess_letter == guess_word[3]:
                count = count + 1
                if guess_letter == guess_word[4]: 
                    count = count + 1 
                    if guess_letter == guess_word[0]: 
                        count = count + 1 
if count == 0: 
    if guess_letter == guess_word[2]:
        count = count + 1 
        if guess_letter == guess_word[3]: 
            count = count + 1 
            if guess_letter == guess_word[4]:
                count = count + 1
                if guess_letter == guess_word[0]: 
                    count = count + 1 
                    if guess_letter == guess_word[1]: 
                        count = count + 1 
if count == 0: 
    if guess_letter == guess_word[3]:
        count = count + 1 
        if guess_letter == guess_word[4]: 
            count = count + 1 
            if guess_letter == guess_word[1]:
                count = count + 1
                if guess_letter == guess_word[2]: 
                    count = count + 1 
                    if guess_letter == guess_word[0]: 
                        count = count + 1 
if count == 0: 
    if guess_letter == guess_word[4]:
        count = count + 1 
        if guess_letter == guess_word[0]: 
            count = count + 1 
            if guess_letter == guess_word[1]:
                count = count + 1
                if guess_letter == guess_word[2]: 
                    count = count + 1 
                    if guess_letter == guess_word[3]: 
                        count = count + 1 
if count == 1: 
    print("1 instance of " + guess_letter + " found in " + guess_word)

if count == 2: 
    print("2 instances of " + guess_letter + " found in " + guess_word)

if count == 3: 
    print("3 instances of " + guess_letter + " found in " + guess_word)

if count == 4: 
    print("4 instances of " + guess_letter + " found in " + guess_word)

if count == 5: 
    print("5 instances of " + guess_letter + " found in " + guess_word)

if count == 0: 
    print("No instances of " + guess_letter + " found in " + guess_word)