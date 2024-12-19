import tkinter as tk
import random
import string


class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Генератор паролей")

        self.include_lowercase = tk.BooleanVar(value=True)
        self.include_digits = tk.BooleanVar(value=True)
        self.include_special = tk.BooleanVar(value=True)

        self.password_length = tk.IntVar(value=12)

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Длина пароля:").pack()
        tk.Entry(self.root, textvariable=self.password_length).pack()

        tk.Checkbutton(self.root, text="Включить буквы нижнего регистра (a-z)", variable=self.include_lowercase).pack()

        tk.Checkbutton(self.root, text="Включить цифры (0-9)", variable=self.include_digits).pack()

        tk.Checkbutton(self.root, text="Включить спецсимволы (! @ # $ %)", variable=self.include_special).pack()

        tk.Button(self.root, text="Сгенерировать пароль", command=self.generate_password).pack()

        self.password_output = tk.Entry(self.root, width=50)
        self.password_output.pack()

    def generate_password(self):

        characters = ""
        if self.include_lowercase.get():
            characters += string.ascii_lowercase
        if self.include_digits.get():
            characters += string.digits
        if self.include_special.get():
            characters += "!@#$%"

        if not characters:
            self.password_output.delete(0, tk.END)
            self.password_output.insert(0, "Выберите хотя бы один тип символов.")
            return

        password = ''.join(random.choice(characters) for _ in range(self.password_length.get()))

        self.password_output.delete(0, tk.END)
        self.password_output.insert(0, password)


if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
