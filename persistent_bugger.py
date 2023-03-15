def persistence(n):
    
    if n < 10:
        return 0
    
    j = 0
    while n >= 10:
        total = 1
        for i in str(n):
            total *= int(i)
        n = total
        j+=1
        
    return j





# A more readable solution
# def persistence(n):
#     """
#     Returns the persistence of n, which is the number of times you need to 
#     multiply the digits of n until you reach a single-digit number.
#     """
#     # If n is a single digit, return 0
#     if n < 10:
#         return 0
    
#     # Convert n to a string to access its digits
#     n_str = str(n)
    
#     # Initialize the number of digits and the iteration counter
#     num_digits = len(n_str)
#     i = 0
    
#     # Multiply the digits of n until we get a single-digit number
#     while num_digits > 1:
#         # Multiply the digits of n and update n_str and num_digits
#         total = 1
#         for digit in n_str:
#             total *= int(digit)
#         n_str = str(total)
#         num_digits = len(n_str)
        
#         # Update the iteration counter
#         i += 1
    
#     # Return the persistence
#     return i


def main():
    """
    Prompts the user to enter a number and calculates its persistence.
    """
    # Prompt the user to enter a number
    n = int(input("Enter a positive integer: "))
    
    # Calculate the persistence of n
    p = persistence(n)
    
    # Display the result
    print(f"The persistence of {n} is {p}.")


if __name__ == '__main__':
    main()