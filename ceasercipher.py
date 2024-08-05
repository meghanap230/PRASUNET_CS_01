import tkinter as tk
from tkinter import messagebox

def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            elif char.isupper():
                encrypted_text += chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def on_encrypt():
    message = message_entry.get()
    shift = int(shift_entry.get())
    encrypted_message = caesar_cipher_encrypt(message, shift)
    result_entry.delete(0, tk.END)
    result_entry.insert(0, encrypted_message)

def on_decrypt():
    message = message_entry.get()
    shift = int(shift_entry.get())
    decrypted_message = caesar_cipher_decrypt(message, shift)
    result_entry.delete(0, tk.END)
    result_entry.insert(0, decrypted_message)

# Create the main window
root = tk.Tk()
root.title("Caesar Cipher")

# Create and place the labels, entries, and buttons
message_label = tk.Label(root, text="Message:")
message_label.grid(row=0, column=0, padx=10, pady=10)

message_entry = tk.Entry(root, width=50)
message_entry.grid(row=0, column=1, padx=10, pady=10)

shift_label = tk.Label(root, text="Shift:")
shift_label.grid(row=1, column=0, padx=10, pady=10)

shift_entry = tk.Entry(root, width=50)
shift_entry.grid(row=1, column=1, padx=10, pady=10)

encrypt_button = tk.Button(root, text="Encrypt", command=on_encrypt)
encrypt_button.grid(row=2, column=0, padx=10, pady=10)

decrypt_button = tk.Button(root, text="Decrypt", command=on_decrypt)
decrypt_button.grid(row=2, column=1, padx=10, pady=10)

result_label = tk.Label(root, text="Result:")
result_label.grid(row=3, column=0, padx=10, pady=10)

result_entry = tk.Entry(root, width=50)
result_entry.grid(row=3, column=1, padx=10, pady=10)

# Run the application
root.mainloop()
