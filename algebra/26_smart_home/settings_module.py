import tkinter as tk

devices_list = ['Alarm', 'Svijetla', 'Klima', 'Pećnica']

login_dict = {'Antonio':'0000',
              'Katja':'0001',
              'Dominik':'0002',
              'Lara': '9999'}

def pick_user(event):
    for i in user_listbox.curselection():
        record = user_listbox.get(i)
        username.set(record)
        password.set(login_dict[record])
 
def update_users():
    updated_username = username.get()
    updated_password = password.get()
 
    for i in user_listbox.curselection():
        print(i)
        record = user_listbox.get(i)
        user_listbox.delete(i)
        user_listbox.insert(i, updated_username)
        login_dict.pop(record)
        login_dict[updated_username] = updated_password

def settings(notebook):
    global username, password, user_listbox
    username = tk.StringVar()
    password = tk.StringVar()
 
    #Settings tab
    settings_tab = tk.Frame(notebook)
    notebook.add(settings_tab, text="Settings")
 
    device_listbox = tk.Listbox(settings_tab)
    device_listbox.grid(row=0, column=0, sticky='w', padx=5, pady=5, rowspan=2)
    for device in devices_list:
        device_listbox.insert(tk.END, device)
 
    add_device_btn = tk.Button(settings_tab,text='Add device')
    add_device_btn.grid(row=2, column=0, sticky='w', pady=5, padx=5)
 
    update_btn = tk.Button(settings_tab, text='Update User', command=update_users)
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
