def find_uniq(arr):
    if arr[0] == arr[-1] or arr[0] == arr[1]:
        all = arr[0]
    else:
        return arr[0]
    for i in arr:
        if i != all:
            return i

def main():
    arr = [1, 1, 2, 1, 1, 1]
    unique_value = find_uniq(arr)
    print(f"The unique value is: {unique_value}")

if __name__ == '__main__':
    main()
