import tkinter as tk
from tkinter import messagebox

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    for d in range(2, phi):
        if (e * d) % phi == 1:
            return d
    return None

p = 17
q = 11

n = p * q
phi = (p - 1) * (q - 1)

e = 7

while gcd(e, phi) != 1:
    e += 2

d = mod_inverse(e, phi)

def encrypt():

    text = entry.get()

    if text == "":
        messagebox.showerror("Error", "Enter Message")
        return

    encrypted = [pow(ord(ch), e, n) for ch in text]

    result.delete(0, tk.END)
    result.insert(0, str(encrypted))


def decrypt():

    try:
        nums = eval(result.get())
        decrypted = ''.join(chr(pow(ch, d, n)) for ch in nums)
        messagebox.showinfo("Decrypted Message", decrypted)

    except:
        messagebox.showerror("Error", "Invalid Cipher")


root = tk.Tk()
root.title("RSA Encryption and Decryption")
root.geometry("450x250")

tk.Label(root, text="Enter Message").pack(pady=5)

entry = tk.Entry(root, width=40)
entry.pack()

tk.Button(root, text="Encrypt", command=encrypt).pack(pady=5)

tk.Label(root, text="Encrypted Message").pack()

result = tk.Entry(root, width=40)
result.pack()

tk.Button(root, text="Decrypt", command=decrypt).pack(pady=5)

root.mainloop()
