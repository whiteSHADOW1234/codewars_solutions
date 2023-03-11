# return masked string
def maskify(cc):
    length = len(cc)
    if length <= 4:
        return cc
    else:
        return '#'*(length-4) + cc[-4]+ cc[-3] + cc[-2] + cc[-1]
    

# Best Solution Simplified
# def maskify(cc):
#     if len(cc) <= 4:
#         return cc
#     else:
#         return '#'*(len(cc)-4) + cc[-4:]


def main():
    test_cases = ["4556364607935616", "64607935616", "1", "Skippy", "Nananananananananananananananana Batman!"]
    for test_case in test_cases:
        result = maskify(test_case)
        print(f"{test_case}: {result}")

if __name__ == "__main__":
    main()