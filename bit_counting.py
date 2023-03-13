def count_bits(n):
    return bin(n).count('1')

def main():
    # Example usage:
    num = 42
    bit_count = count_bits(num)
    print(f"The number of 1 bits in {num} is {bit_count}.")

if __name__ == '__main__':
    main()
