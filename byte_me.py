import sys

def total_bytes(object):
    return sys.getsizeof(object)


def main():
    test_cases = ["hello", 123, '[":)", 1]', "?"*12345]
    for test_case in test_cases:
        result = total_bytes(test_case)
        print(f"{test_case}: {result} bytes")

if __name__ == "__main__":
    main()