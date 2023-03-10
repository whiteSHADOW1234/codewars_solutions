def get_sum(a,b):
    min_num = 0
    max_num = 0
    if a < b:
        min_num = a
        max_num = b
    elif b < a:
        min_num = b
        max_num = a
    elif a == b:
        return a
    val = 0
    for i in range(min_num, max_num+1):
        val += i
    return val



# Best Solution Time Complexity: O(n) -> O(1), Space Complexity: O(1) -> O(1)
# def get_sum(a, b):
#     if a == b:
#         return a
    
#     if a > b:
#         a, b = b, a

#     # formula for the sum of an arithmetic sequence
#     return (b - a + 1) * (a + b) // 2



def main():
    test_cases = [(0,1), (0,-1)]
    for a, b in test_cases:
        result = get_sum(a, b)
        print(f"The sum of numbers between {a} and {b} is {result}.")

if __name__ == "__main__":
    main()