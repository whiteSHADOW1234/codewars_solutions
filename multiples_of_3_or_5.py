def solution(number):
    total = 0
    for i in range(0,number):
        if int(i%3) == 0 or int(i%5) == 0:
            total += i
    return total



# Alternative solution
# def solution(number):
#     # Calculate the sum of all multiples of 3 and 5 below 'number'
#     sum_of_multiples = sum([i for i in range(number) if i % 3 == 0 or i % 5 == 0])
    
#     return sum_of_multiples


if __name__ == '__main__':
    # Replace '10' with the value you want to test
    result = solution(10)
    print(result)
    
