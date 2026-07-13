import tkinter as tk
from tkinter import messagebox


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
    rail = [['\n' for _ in range(len(cipher))] for _ in range(key)]

    direction = None
    row = 0
    col = 0

    # Mark the zig-zag path
    for _ in range(len(cipher)):
        if row == 0:
            direction = 1
        elif row == key - 1:
            direction = -1

        rail[row][col] = '*'
        col += 1
        row += direction

    # Fill the marked positions
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if rail[i][j] == '*' and index < len(cipher):
                rail[i][j] = cipher[index]
                index += 1

    # Read the original text
    result = []
    row = 0
    col = 0

    for _ in range(len(cipher)):
        if row == 0:
            direction = 1
        elif row == key - 1:
            direction = -1

        result.append(rail[row][col])
        col += 1
        row += direction

    return ''.join(result)


def enc():
    try:
        text = msg.get()
        key = int(key_entry.get())

        if key < 2:
            messagebox.showerror("Error", "Key must be greater than 1.")
            return

        cipher = encrypt(text, key)

        out.config(text="Encrypted: " + cipher)

        msg.delete(0, tk.END)
        msg.insert(0, cipher)

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid key.")


def dec():
    try:
        text = msg.get()
        key = int(key_entry.get())

        if key < 2:
            messagebox.showerror("Error", "Key must be greater than 1.")
            return

        plain = decrypt(text, key)

        out.config(text="Decrypted: " + plain)

        msg.delete(0, tk.END)
        msg.insert(0, plain)

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid key.")


root = tk.Tk()
root.title("Rail Fence Cipher")
root.geometry("400x220")
root.resizable(False, False)

tk.Label(root, text="Enter Message:", font=("Arial", 11)).pack(pady=5)

msg = tk.Entry(root, width=35, font=("Arial", 11))
msg.pack()

tk.Label(root, text="Enter Key:", font=("Arial", 11)).pack(pady=5)

key_entry = tk.Entry(root, width=10, font=("Arial", 11))
key_entry.pack()

tk.Button(root, text="Encrypt", width=12, command=enc).pack(pady=5)

tk.Button(root, text="Decrypt", width=12, command=dec).pack(pady=5)

out = tk.Label(root, text="", font=("Arial", 11), fg="blue")
out.pack(pady=10)

root.mainloop()
