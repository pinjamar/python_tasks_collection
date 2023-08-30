import tkinter as tk
from SQLiteSmartHome_repo import *
import sqlite3
from tkinter import messagebox
import datetime as dt

conn = sqlite3.connect('MySmartHome.db')
cursor = conn.cursor()

def add_obligation():
    user = user_entry.get()
    start_datetime = start_entry.get()
    end_datetime = end_entry.get()
    task = task_entry.get()

    if user and start_datetime and end_datetime and task:
        cursor.execute(insert_into_obligations_query, (user, start_datetime, end_datetime, task))
        conn.commit()
        clear_entries()
        messagebox.showinfo('Success', 'Obligation Added Successfully')
    else:
        messagebox.showerror('Error', 'Please fill in all fields')
    
    refresh_obligations()

def refresh_obligations():
    obligation_lstbox.delete(0, tk.END)
    cursor.execute(select_obligations_by_username, ('Antonio',))
    records = cursor.fetchall()
    date_format = '%Y-%m-%d %H:%M:%S'
    for obligation in records:
        start_datetime_obj = dt.datetime.strptime(obligation[1], date_format)
        end_datetime_obj = dt.datetime.strptime(obligation[2], date_format)
        obligation_lstbox.insert(tk.END, f'{obligation[0]} - {start_datetime_obj.date()} - {start_datetime_obj.time()} - {end_datetime_obj.time()} - {obligation[3]}')
    
    print(obligation[1])
    print(type(obligation[1]))

def clear_entries():
    user_entry.delete(0, tk.END)
    start_entry.delete(0, tk.END)
    end_entry.delete(0, tk.END)
    task_entry.delete(0, tk.END)

def obligations_tab(notebook):
    global user_entry, start_entry, end_entry, task_entry, obligation_lstbox

    obligations_tab = tk.Frame(notebook)
    notebook.add(obligations_tab, text = 'Obligations')

    user_label = tk.Label(obligations_tab, text = 'User: ')
    user_label.pack()

    user_entry = tk.Entry(obligations_tab)
    user_entry.pack()

    start_label = tk.Label(obligations_tab, text = 'Start Datetime: ')
    start_label.pack()

    start_entry = tk.Entry(obligations_tab)
    start_entry.pack()

    end_label = tk.Label(obligations_tab, text = 'End Datetime: ')
    end_label.pack()

    end_entry = tk.Entry(obligations_tab)
    end_entry.pack()

    task_label = tk.Label(obligations_tab, text = 'Task Name: ')
    task_label.pack()

    task_entry = tk.Entry(obligations_tab)
    task_entry.pack()

    # Create buttons
    add_button = tk.Button(obligations_tab, text = 'Add Obligation', command = add_obligation)
    add_button.pack(pady=5)

    clear_button = tk.Button(obligations_tab, text = 'Clear Entries', command=clear_entries)
    clear_button.pack(pady=5)

    # Create listbox
    obligation_lstbox = tk.Listbox(obligations_tab, width= 70)
    refresh_obligations()
    obligation_lstbox.pack(pady=5)

