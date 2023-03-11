def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    return False


# Best Solution Simplified
# def is_triangle(a, b, c):
#     return a + b > c and a + c > b and b + c > a


def main():
    test_cases = [(1, 2, 2), (7, 2, 2), (1, 2, 3), (1, 3, 2), (3, 1, 2), (5, 1, 2), (1, 2, 5), (2, 5, 1), (4, 2, 3), (5, 1, 5), (2, 2, 2), (-1, 2, 3), (1, -2, 3), (1, 2, -3), (0, 2, 3)]
    for test_case in test_cases:
        result = is_triangle(test_case[0], test_case[1], test_case[2])
        print(f"{test_case}: {result}")
    
if __name__ == "__main__":
    main()