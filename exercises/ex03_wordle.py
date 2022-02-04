"""Exercise 3, structured wordle."""

__author__: str = "730401052"


def contains_char(word_search: str, char_search: str) -> bool:
    """Searches first parameter for character given in second parameter."""
    assert len(char_search) == 1
    i: int = 0
    while i < len(word_search):  # searching indices for character
        if word_search[i] == char_search:
            return True 
        else: 
            i = i + 1 
    return False


def emojified(guess: str, secret: str) -> str: 
    """Codifies guess into emoji string of correct, correct but misplace, and incorrect answers."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    i: int = 0
    result: str = ""
    while i < len(secret):  # searching indices of secret for emoji output
        if contains_char(secret, guess[i]) is True:
            if guess[i] == secret[i]: 
                result += GREEN_BOX 
            else: 
                same_character: bool = False
                alternate: int = 0
                while not same_character and alternate < len(secret): 
                    if guess[i] == secret[alternate]:
                        same_character = True 
                    else: 
                        alternate = alternate + 1 
                if same_character is True: 
                    result = result + YELLOW_BOX
        else:
            result += WHITE_BOX
        i += 1

    return result


def input_guess(guess_length: int) -> str: 
    """Input a guess of specified length."""
    guess_word: str = input(f"Enter a {guess_length} character word: ")
    while len(guess_word) != guess_length:
        guess_word = input(f"That wasn't {guess_length} chars! Try again: ")
    return guess_word  # this will be the users guess 


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    turn: int = 1
    win: bool = False  # false until the user wins 
    while not win and turn < 7:
        print(f"=== Turn {turn}/6 ===") 
        guess: str = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret: 
            win = True
        else: 
            turn += 1
    if win is True:  # outputs of win/lose
        print(f"You won in {turn}/6 turns!")
    else: 
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()