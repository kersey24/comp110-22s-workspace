def main() -> None: 
    # inventory: dict[str, int] = {"bread": 5, "chips": 1, "milk": 10}
    # buy: dict[str, int] = {"bread": 5, "chips": 1, "milk": 10, "kiwi": 1}
    # print(grocery_list(inventory, buy))
    a: list[str] = ["apple", "orange", "banana"]
    b: str = 'a'
    print(last(a, b))


def grocery_list(a: dict[str, int], b: dict[str, int]) -> list[str]:
    result: list[str] = []
    for key in b:
        if b[key] <= a[key]:
            result.append(key)
    return result


def last(a: list[str], b: str) -> list[str]:
    result: list[str] = []
    i: int = 0 
    while i < len(a):
        current: str = a[i]
        if b == current[len(current) - 1]:
            result.append(current)
        i += 1
    return result


if __name__ == "__main__":
    main()
