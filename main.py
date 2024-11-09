import tkinter as tk, random, string
def generate_password(length, options):
    characters = ''.join(option for option in options if option)
    if not characters:
        raise ValueError("Должен быть выбран хотя бы один тип символов.")
    return ''.join(random.choice(characters) for _ in range(length))
def on_generate():
    length = int(length_entry.get())
    options = [
        uppercase_var.get() * string.ascii_uppercase,
        lowercase_var.get() * string.ascii_lowercase,
        digits_var.get() * string.digits,
        special_chars_var.get() * string.punctuation
    ]
    password_output.config(state='normal')
    password_output.delete(0, tk.END)
    password_output.insert(0, generate_password(length, options))
    password_output.config(state='readonly')
root = tk.Tk()
root.title("Генератор паролей")
tk.Label(root, text="Длина пароля:").grid(row=0, column=0)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1)
uppercase_var = tk.BooleanVar(value=True)
lowercase_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
special_chars_var = tk.BooleanVar(value=True)
for i, (text, var) in enumerate([( "Верхний регистр", uppercase_var),
                                   ("Нижний регистр", lowercase_var),
                                   ("Цифры", digits_var),
                                   ("Специальные символы", special_chars_var)]):
    tk.Checkbutton(root, text=text, variable=var).grid(row=i+1, columnspan=2)

tk.Button(root, text="Сгенерировать пароль", command=on_generate).grid(row=5, columnspan=2)
tk.Label(root, text="Сгенерированный пароль:").grid(row=6, column=0)
password_output = tk.Entry(root, state='readonly')
password_output.grid(row=6, column=1)
root.mainloop()