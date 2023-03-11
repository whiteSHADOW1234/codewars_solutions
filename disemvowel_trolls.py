def disemvowel(string_):
    string_ = string_.replace("a","").replace("A","").replace("e","").replace("E","").replace("i","").replace("I","").replace("o","").replace("O","").replace("u","").replace("U","")
    return string_



# Best Solution  O(10*n) -> O(n)
# VOWELS = "aeiouAEIOU"

# def disemvowel(string_):
#     return "".join(char for char in string_ if char not in VOWELS)


def main():
    test_cases = ["This website is for losers LOL!", "a", "abc", "AbcDEFGaB"]
    for test_case in test_cases:
        result = disemvowel(test_case)
        print(f"{test_case}: {result}")

if __name__ == "__main__":
    main()
