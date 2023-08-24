import tkinter as tk
from tkinter import ttk, messagebox
import datetime as dt

root = tk.Tk()
root.title('My smart home')
# root.geometry('700x700')

alarm = tk.BooleanVar()
print(alarm.get())
alarm.set(tk.TRUE)
username = tk.StringVar()
password = tk.StringVar()

login_dict = {'admin': '0000',
              'user1': '0001',
              'user2': '0002'}


def pick_user(event):
    for i in user_listbox.curselection():
        record = user_listbox.get(i)
        username.set(record)
        password.set(login_dict[record])
        print(type(username.get()))
        print(password.get())


def Update_users():
    pass


def login_funct():
    username_text = username_entry.get()
    password_text = password_entry.get()
    if username_text in login_dict and login_dict[username_text] == password_text:
        root.destroy()
        open_main_window()


def open_main_window():
    global user_listbox
    main_window = tk.Tk()
    main_window.title('Settings Notebook')

    main_notebook = ttk.Notebook(main_window)
    main_notebook.pack()

    settings_tab = tk.Frame(main_notebook)
    main_notebook.add(settings_tab, text="Settings")
    # main_notebook.add(lights_tab, text="Lights")

    alarm_chkbox = tk.Checkbutton(settings_tab, text='Alarm', variable=alarm)
    alarm_chkbox.grid(row=0, column=0, sticky='w', pady=5, padx=5)

    lights_chkbox = tk.Checkbutton(settings_tab, text='Svijetla')
    lights_chkbox.grid(row=1, column=0, sticky='w', pady=5, padx=5)

    Klima_chkbox = tk.Checkbutton(settings_tab, text='Klima')
    Klima_chkbox.grid(row=2, column=0, sticky='w', pady=5, padx=5)

    Oven_chkbox = tk.Checkbutton(settings_tab, text='Pećnica')
    Oven_chkbox.grid(row=3, column=0, sticky='w', pady=5, padx=5)

    add_device_btn = tk.Button(settings_tab, text='Add device')
    add_device_btn.grid(row=4, column=0, sticky='w', pady=5, padx=5)

    update_btn = tk.Button(
        settings_tab, text='Update User', command=Update_users)
    update_btn.grid(row=2, column=2)

    user_listbox = tk.Listbox(settings_tab)
    user_listbox.grid(row=0, column=1, rowspan=4)
    user_listbox.bind("<<ListboxSelect>>", pick_user)

    username_ent = tk.Entry(settings_tab, textvariable=username)
    username_ent.grid(row=0, column=2, padx=10, pady=5)

    passwrd_ent = tk.Entry(settings_tab, textvariable=password)
    passwrd_ent.grid(row=1, column=2, padx=10, pady=5)

    for user in login_dict.keys():
        user_listbox.insert(tk.END, user)

    # Alarm is on 22 - 06
    current_time = dt.datetime.now().time()
    if current_time > dt.time(20, 0) or current_time < dt.time(6, 0):
        alarm_chkbox.invoke()
    elif current_time > dt.time(6, 0):
        alarm_chkbox.deselect()


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


root.mainloop()
