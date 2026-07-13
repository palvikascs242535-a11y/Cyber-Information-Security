import tkinter as tk
from tkinter import messagebox

# Function to encrypt text
def encrypt():
    try:
        text = entry.get()
        shift = int(shift_entry.get())

        result = ""

        for char in text:
            if char.isalpha():
                if char.isupper():
                    result += chr((ord(char) - 65 + shift) % 26 + 65)
                else:
                    result += chr((ord(char) - 97 + shift) % 26 + 97)
            else:
                result += char

        output.config(text="Encrypted: " + result)

        # Replace entry with encrypted text
        entry.delete(0, tk.END)
        entry.insert(0, result)

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid shift value.")


# Function to decrypt text
def decrypt():
    try:
        text = entry.get()
        shift = int(shift_entry.get())

        result = ""

        for char in text:
            if char.isalpha():
                if char.isupper():
                    result += chr((ord(char) - 65 - shift) % 26 + 65)
                else:
                    result += chr((ord(char) - 97 - shift) % 26 + 97)
            else:
                result += char

        output.config(text="Decrypted: " + result)

        # Replace entry with decrypted text
        entry.delete(0, tk.END)
        entry.insert(0, result)

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid shift value.")


# Main Window
root = tk.Tk()
root.title("Caesar Cipher")
root.geometry("400x220")
root.resizable(False, False)

# Message
tk.Label(root, text="Enter Message:", font=("Arial", 11)).pack(pady=5)

entry = tk.Entry(root, width=35, font=("Arial", 11))
entry.pack()

# Shift
tk.Label(root, text="Enter Shift Value:", font=("Arial", 11)).pack(pady=5)

shift_entry = tk.Entry(root, width=10, font=("Arial", 11))
shift_entry.pack()

# Buttons
tk.Button(root, text="Encrypt", width=12, command=encrypt).pack(pady=5)

tk.Button(root, text="Decrypt", width=12, command=decrypt).pack(pady=5)

# Output Label
output = tk.Label(root, text="", font=("Arial", 11), fg="blue")
output.pack(pady=10)

root.mainloop()
