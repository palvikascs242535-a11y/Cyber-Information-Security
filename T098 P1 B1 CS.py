def encrypt(text, key):
    rail = [''] * key
    direction = 1
    row = 0

    for ch in text:
        rail[row] += ch

        if row == 0:
            direction = 1
        elif row == key - 1:
            direction = -1

        row += direction

    return ''.join(rail)


def decrypt(cipher, key):
    rail = [['\n' for i in range(len(cipher))] for j in range(key)]

    direction = None
    row = 0
    col = 0

    for i in range(len(cipher)):
        if row == 0:
            direction = 1
        if row == key - 1:
            direction = -1

        rail[row][col] = '*'
        col += 1
        row += direction

    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if rail[i][j] == '*' and index < len(cipher):
                rail[i][j] = cipher[index]
                index += 1

    result = []
    row = 0
    col = 0

    for i in range(len(cipher)):
        if row == 0:
            direction = 1
        if row == key - 1:
            direction = -1

        result.append(rail[row][col])
        col += 1
        row += direction

    return "".join(result)


text = input("Enter Message : ")
key = int(input("Enter Key : "))

cipher = encrypt(text, key)
print("Encrypted :", cipher)

plain = decrypt(cipher, key)
print("Decrypted :", plain)
