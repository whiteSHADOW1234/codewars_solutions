# Brute Force ROT13
def rot13(message):
    store = ""
    for i in range(len(message)):
        if (ord(message[i]) - 13) - ord('a') < 0 and ord(message[i]) >=  ord('a') and ord(message[i]) <=  ord('z'):
            store += chr(ord('z') - abs((ord(message[i]) - 13) - ord('a')) + 1)
        elif (ord(message[i]) - 13) - ord('A') < 0 and ord(message[i]) >=  ord('A') and ord(message[i]) <=  ord('Z'):
            store += chr(ord('Z') - abs((ord(message[i]) - 13) - ord('A')) + 1)
        elif (ord(message[i]) >=  ord('a') and ord(message[i]) <=  ord('z')) or (ord(message[i]) >=  ord('A') and ord(message[i]) <=  ord('Z')):
            store += chr(ord(message[i]) - 13)
        else:
            store += message[i]

    return store


# A more elegant solution
# def rot13(message):
#     new_string = ""
#     for char in message:
#         if char.islower():
#             new_string += chr((ord(char) - 97 + 13) % 26 + 97)
#         elif char.isupper():
#             new_string += chr((ord(char) - 65 + 13) % 26 + 65)
#         else:
#             new_string += char
#     return new_string



if __name__ == '__main__':
    message = "hello world"
    encrypted_message = rot13(message)
    print(f"Encrypted message: {encrypted_message}")
    decrypted_message = rot13(encrypted_message)
    print(f"Decrypted message: {decrypted_message}")
