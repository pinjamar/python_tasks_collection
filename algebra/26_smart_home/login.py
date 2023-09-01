import tkinter as tk

login_dict = {'Antonio': '0000',
              'Katja': '0001',
              'Dominik': '0002',
              'Lara': '9999'}


def login_funct():
    username_text = username_entry.get()
    password_text = password_entry.get()
    if username_text in login_dict and login_dict[username_text] == password_text:
        root.destroy()


def login(grad):
    global root, username_entry, password_entry

    root = tk.Tk()
    root.title('My Smart Home')
    username_label = tk.Label(text='Username: ')
    username_label.pack()

    username_entry = tk.Entry(root)
    username_entry.pack(padx=10, pady=5)

    password_label = tk.Label(text='Password: ')
    password_label.pack()

    password_entry = tk.Entry(root, show='*')
    password_entry.pack(padx=10, pady=5)

    login_btn = tk.Button(root, text='Login', command=login_funct)
    login_btn.pack(pady=10)

    status_msg = tk.Label(
        root, text=f'Temperatura u Splitu je {grad.temp} °C. Dobrodošli! ')
    status_msg.pack(padx=10, pady=15)

    root.mainloop()
