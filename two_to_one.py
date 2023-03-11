def longest(a1, a2):
    word = a1 + a2
    return ''.join(sorted(set(word), key=str.lower))

# Best Solution Simplified
# def longest(a1, a2):
#     return ''.join(sorted(set(a1 + a2), key=str.casefold))



def main():
    test_cases = [("aretheyhere", "yestheyarehere"), ("loopingisfunbutdangerous", "lessdangerousthancoding"), ("inmanylanguages", "theresapairoffunctions")]
    for test_case in test_cases:
        result = longest(test_case[0], test_case[1])
        print(f"{test_case}: {result}")

if __name__ == "__main__":
    main()