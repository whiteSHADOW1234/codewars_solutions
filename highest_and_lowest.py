def high_and_low(numbers):
    num_split = numbers.split()
    num_int = []
    
    for i in num_split:
        num_int.append(int(i))
        
    min = num_int[0]
    max = num_int[0]
    for i in num_int:
        if min > i:
            min = i
        elif max < i:
            max = i
    numbers = str(max) + " " + str(min)
    return numbers


# Best Solution Simplier
# def high_and_low(numbers):
#     num_int = [int(i) for i in numbers.split()]
#     num_min = min(num_int)
#     num_max = max(num_int)
#     return f"{num_max} {num_min}"


def main():
    test_cases = ["1 2 3", "8 3 -5 42 -1 0 0 -9 4 7 4 -4"]
    for test_case in test_cases:
        result = high_and_low(test_case)
        print(f"{test_case}: {result}")

if __name__ == "__main__":
    main()