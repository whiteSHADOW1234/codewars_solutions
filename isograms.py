def is_isogram(string):
    low = string.lower()
    if string == "":
        return True
    
    for i in range(0,len(low)):
        for j in range(i+1,len(low)):
            if low[i] == low[j]:
                return False

    return True



# Best Solution with explaination O(n^2) -> O(n)
# def is_isogram(string):
#     """
#     Returns True if the given string is an isogram, i.e. it has no repeating characters.
#     """
#     if not string:
#         # An empty string is considered an isogram
#         return True
    
#     # Convert the string to lowercase to make the comparison case-insensitive
#     string = string.lower()
    
#     # Use a set to keep track of the characters we've seen so far
#     seen_chars = set()
    
#     for char in string:
#         if char in seen_chars:
#             # We've already seen this character, so the string is not an isogram
#             return False
#         seen_chars.add(char)
    
#     # If we made it through the whole string without finding any repeating characters,
#     # then the string is an isogram
#     return True


def main():
    test_cases = ["", "a", "abc", "AbcDEFGaB"]
    for test_case in test_cases:
        result = is_isogram(test_case)
        print(f"{test_case}: {result}")

if __name__ == "__main__":
    main()
