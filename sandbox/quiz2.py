"""."""


def main() -> None: 
    inventory: dict[str, int] = {"bread": 5, "chips": 1, "milk": 10}
    buy: dict[str, int] = {"bread": 5, "chips": 2, "milk": 7}
    grocery_list(inventory, buy)


if __name__ == "__main__":
    main()


def odd_and_even(a: list[int]) -> list[int]:
    """."""
    i: int = 0 
    result: list[int] = []
    for item in a: 
        if i % 2 == 0:
            if item % 2 != 0: 
                result.append(item)
        i += 1

    return result


def vowels_and_threes(a: str) -> str:
    result: str = ""
    vowel: list[str] = ["a", "e", "i", "o", "u"]
    # is_vowel: bool = False
    i: int = 0
    while i < len(a): 
        # is_vowel = False
        # j: int = 0
        # # while j < len(a):
        # #     if vowel[j] == a[i]:
        # #         is_vowel = True
        # #     j += 1 
        if i % 3 == 0 and a[i] in vowel: 
            result += ""
        elif i % 3 == 0: 
            result += a[i]
        elif a[i] in vowel: 
            result += a[i]
        i += 1
    return result


def average_grades(grades: dict[str, list[int]]) -> dict[str, float]:
    """maps each students grades to their average."""
    average: dict[str, float] = dict()
    for students in grades: 
        total: int = 0 
        for all in grades[students]: 
            total += all
        average[students] = total / len(grades[students])
    return average


def grocery_list(a: dict[str, int], b: dict[str, int]) -> list[str]:
    result: list[str] = []
    for key in b:
        if b[key] >= a[key]:
            result.append(key)
    return result