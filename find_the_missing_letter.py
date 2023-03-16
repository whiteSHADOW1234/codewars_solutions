def find_missing_letter(chars):
    check = chars[0]
    for i in chars:
        if ord(check) != ord(i):
            return check
        check = chr(ord(check)+1)

def main():
    chars = ['a', 'b', 'c', 'e']
    missing_char = find_missing_letter(chars)
    print(f"The missing character is: {missing_char}")

if __name__ == '__main__':
    main()
