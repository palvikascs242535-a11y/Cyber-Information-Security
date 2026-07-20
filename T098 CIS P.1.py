import math

# Function to find GCD
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to find modular inverse
def mod_inverse(e, phi):
    for d in range(2, phi):
        if (e * d) % phi == 1:
            return d
    return None

# Small prime numbers
p = 17
q = 11

n = p * q
phi = (p - 1) * (q - 1)

e = 7

while gcd(e, phi) != 1:
    e += 2

d = mod_inverse(e, phi)

print("Public Key =", (e, n))
print("Private Key =", (d, n))

message = input("Enter Message: ")

encrypted = [pow(ord(ch), e, n) for ch in message]

print("Encrypted Message:")
print(encrypted)

decrypted = ''.join(chr(pow(ch, d, n)) for ch in encrypted)

print("Decrypted Message:")
print(decrypted)
