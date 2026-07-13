def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


message = input("Enter Message : ")
shift = int(input("Enter Shift Value : "))

encrypted = encrypt(message, shift)
print("Encrypted Message :", encrypted)

decrypted = decrypt(encrypted, shift)
print("Decrypted Message :", decrypted)
