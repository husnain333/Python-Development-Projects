import secrets
import string
import tkinter as tk
from tkinter import messagebox

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        master.title("Password Generator")

        # Labels and Entry for password criteria
        tk.Label(master, text="Password Length:").grid(row=0, column=0, sticky="e")
        self.length_entry = tk.Entry(master)
        self.length_entry.grid(row=0, column=1)

        self.uppercase_var = tk.IntVar()
        tk.Checkbutton(master, text="Include Uppercase", variable=self.uppercase_var).grid(row=1, column=0, columnspan=2, sticky="w")

        self.digits_var = tk.IntVar()
        tk.Checkbutton(master, text="Include Digits", variable=self.digits_var).grid(row=2, column=0, columnspan=2, sticky="w")

        self.special_chars_var = tk.IntVar()
        tk.Checkbutton(master, text="Include Special Characters", variable=self.special_chars_var).grid(row=3, column=0, columnspan=2, sticky="w")

        # Button to generate password
        tk.Button(master, text="Generate Password", command=self.generate_password).grid(row=4, column=0, columnspan=2)

        # Display area for generated password
        self.password_display = tk.Text(master, height=3, width=30)
        self.password_display.grid(row=5, column=0, columnspan=2)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            uppercase = bool(self.uppercase_var.get())
            digits = bool(self.digits_var.get())
            special_chars = bool(self.special_chars_var.get())

            characters = string.ascii_lowercase
            if uppercase:
                characters += string.ascii_uppercase
            if digits:
                characters += string.digits
            if special_chars:
                characters += string.punctuation

            password = ''.join(secrets.choice(characters) for _ in range(length))
            self.password_display.delete("1.0", tk.END)  # Clear previous content
            self.password_display.insert(tk.END, password)

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid password length.")

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
