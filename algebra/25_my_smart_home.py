import tkinter as tk
from tkinter import ttk, messagebox
import datetime as dt
import threading

root = tk.Tk()
root.title('My smart home')
# root.geometry('700x700')


login_dict = {'admin': '0000',
              'user1': '0001',
              'user2': '0002'}

devices_list = ['Alarm', 'Svijetla', 'Klima', 'Pećnica']

lights = [{
    'name': 'Dnevna soba',
    'is_on': True},
    {
        'name': 'Kupaonica',
        'is_on': False
}
]

# def automatic_alarm():
#     #Alarm is on 22 - 06
#     current_time = dt.datetime.now().time()
#     if current_time < dt.time(18,22):
#         alarm_chkbox.invoke()
#     elif current_time > dt.time(18, 22):
#         alarm_chkbox.deselect()
#     # threading.Timer(5, automatic_alarm).start()


def refresh_lights():
    lights_lbox.delete(0, tk.END)
    for light in lights:
        status = '𝗢𝗡' if light['is_on'] else '𝗢𝗙𝗙'
        lights_lbox.insert(tk.END, f'{light["name"]} - {status}')


def toggle_lights():
    selected_index = lights_lbox.curselection()[0]
    lights[selected_index]['is_on'] = not lights[selected_index]['is_on']
    refresh_lights()


def auto_light_ctrl():
    selected_rule = lights_rule_cbox.get()
    selected_light_index = lights_lbox.curselection()[0]
    selected_light = lights[selected_light_index]
    if selected_rule == 'Ugasi nakon 22h':
        current_time = dt.datetime.now().time()
        if current_time > dt.time(22, 0):
            selected_light['is_on'] = False
            refresh_lights()

    # threading.Timer(5, auto_light_ctrl).start()


def pick_user(event):
    for i in user_listbox.curselection():
        record = user_listbox.get(i)
        username.set(record)
        password.set(login_dict[record])


def Update_users():
    updated_username = username.get()
    # print(updated_username)
    updated_password = password.get()
    # print(updated_password)

    for i in user_listbox.curselection():
        print(i)
        record = user_listbox.get(i)
        user_listbox.delete(i)
        user_listbox.insert(i, updated_username)
        login_dict.pop(record)
        login_dict[updated_username] = updated_password


def login_funct():
    username_text = username_entry.get()
    password_text = password_entry.get()
    if username_text in login_dict and login_dict[username_text] == password_text:
        root.destroy()
        open_main_window()


def open_main_window():
    global user_listbox, username, password, lights_lbox, lights_rule_cbox
    main_window = tk.Tk()
    main_window.title('Settings Notebook')

    main_notebook = ttk.Notebook(main_window)
    main_notebook.pack()

    username = tk.StringVar()
    password = tk.StringVar()

    # Settings tab
    settings_tab = tk.Frame(main_notebook)
    main_notebook.add(settings_tab, text="Settings")

    device_listbox = tk.Listbox(settings_tab)
    device_listbox.grid(row=0, column=0, sticky='w', padx=5, pady=5, rowspan=2)
    for device in devices_list:
        device_listbox.insert(tk.END, device)

    add_device_btn = tk.Button(settings_tab, text='Add device')
    add_device_btn.grid(row=2, column=0, sticky='w', pady=5, padx=5)

    update_btn = tk.Button(
        settings_tab, text='Update User', command=Update_users)
    update_btn.grid(row=4, column=1)

    user_listbox = tk.Listbox(settings_tab)
    user_listbox.grid(row=0, column=1, rowspan=2)
    user_listbox.bind("<<ListboxSelect>>", pick_user)

    username_ent = tk.Entry(settings_tab, textvariable=username)
    username_ent.grid(row=2, column=1, padx=10, pady=5)

    passwrd_ent = tk.Entry(settings_tab, textvariable=password)
    passwrd_ent.grid(row=3, column=1, padx=10)

    for user in login_dict.keys():
        user_listbox.insert(tk.END, user)

    # Lights tab
    lights_tab = tk.Frame(main_notebook)
    main_notebook.add(lights_tab, text="Lights")

    lights_lbl = tk.Label(lights_tab, text='Svijetla: ', font=('Arial', 15))
    lights_lbl.pack()

    lights_lbox = tk.Listbox(lights_tab)
    refresh_lights()
    lights_lbox.pack()

    on_off_btn = tk.Button(lights_tab, text='ON/OFF', command=toggle_lights)
    on_off_btn.pack(pady=10)

    lights_rule_cbox = ttk.Combobox(lights_tab, values=['Ugasi nakon 22h'])
    lights_rule_cbox.pack(pady=10)

    rule_apply_btn = tk.Button(
        lights_tab, text='Primjeni pravilo', command=auto_light_ctrl)
    rule_apply_btn.pack(pady=5)
    # automatic_alarm()
    main_window.mainloop()


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
