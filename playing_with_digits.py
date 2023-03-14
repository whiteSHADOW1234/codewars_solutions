
# Brute force solution
import math

def dig_pow(n, p):
    test = n
    total = 0
    digit = len(str(n))
    largest_pow = digit + p - 1
    for i in range(digit):
        val = n % 10
        n = n // 10
        total += math.pow(val, largest_pow)
        largest_pow -= 1
    
    if int(total) % test == 0:
        return total // test

    return -1



# more elegant solution
# def dig_pow(n, p):
#     """
#     Calculates the k value that satisfies the following condition:
#     If we take all the digits of n, raise them to consecutive powers starting with p, 
#     and add the results, we get a multiple of n. The k value is the exponent to which
#     each digit is raised.
#     """
#     digits = [int(d) for d in str(n)]
#     total = sum(d ** (p+i) for i, d in enumerate(digits))
#     if total % n == 0:
#         return total // n
#     else:
#         return -1



if __name__ == '__main__':
    n = 46288
    p = 3
    k = dig_pow(n, p)
    if k == -1:
        print("No k value satisfies the condition.")
    else:
        print(f"The k value that satisfies the condition is {k}.")
