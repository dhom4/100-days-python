# caesar cipher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(encrypted_message, shift):
    encrypted_message = ""

    for char in text:
        if char.isalpha():
            if char.islower():
                start_ascii = ord('a')
            else:
                start_ascii = ord('A')
            shifted_char_ascii = ((ord(char) - start_ascii)+ shift) % 26 + start_ascii
            encrypted_message += chr(shifted_char_ascii)
        else:
            # If not an alphabet character, just append it as is
            encrypted_message += char

    print("Encrypted/Decrypted message:", encrypted_message)


def dcrypt(encrypted_message, shift):
    encrypted_message = ""

    for char in text:
        if char.isalpha():
            if char.islower():
                start_ascii = ord('a')
            else:
                start_ascii = ord('A')
            shifted_char_ascii = ((ord(char) - start_ascii)- shift) % 26 + start_ascii
            encrypted_message += chr(shifted_char_ascii)
        else:
            # If not an alphabet character, just append it as is
            encrypted_message += char

    print("Encrypted/Decrypted message:", encrypted_message)

text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
dcrypt(text, shift)
