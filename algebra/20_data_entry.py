import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3


def handle_enter_data(event):
    accepted = accept_var.get()

    if accepted == "Accepted":
        firstname = ent_first_name.get()
        lastname = ent_last_name.get()

        if firstname and lastname:
            title = cbx_title.get()
            age = sbx_age.get()
            country = cbx_country.get()

            registration_status = reg_status_var.get()
            num_courses = sbx_num_courses.get()
            num_semesters = sbx_num_semesters.get()

            # Create table (SQLite)
            conn = sqlite3.connect('data.db')
            table_create_query = '''CREATE TABLE IF NOT EXISTS Student
                                    (firstname TEXT, lastname TEXT, title TEXT, age INT, country TEXT)
                                    '''
            conn.execute(table_create_query)

            data_insert_query = '''INSERT INTO Student
                                    (firstname, lastname, title, age, country)
                                    VALUES (?,?,?,?,?)'''
            data_insert_tuple = (firstname, lastname, title, age, country)
            cursor = conn.cursor()
            cursor.execute(data_insert_query, data_insert_tuple)
            conn.commit()
            conn.close()

        else:
            tk.messagebox.showwarning(
                title="WARNING", message="First and last name are required!")
    else:
        tk.messagebox.showwarning(
            title="WARNING", message="You have not accepted the terms")


root = tk.Tk()
root.title("Data Entry Form")

frm = tk.Frame(root)
frm.pack()

# USER INFORMATION FRAME
frm_user_info = tk.LabelFrame(frm, text="User Information")
frm_user_info.grid(row=0, column=0, padx=20, pady=10)

lbl_first_name = tk.Label(frm_user_info, text="First Name")
lbl_first_name.grid(row=0, column=0, padx=10, pady=5)

lbl_last_name = tk.Label(frm_user_info, text="Last Name")
lbl_last_name.grid(row=0, column=1, padx=10, pady=5)

lbl_title = tk.Label(frm_user_info, text="Title")
lbl_title.grid(row=0, column=2, padx=10, pady=5)

ent_first_name = tk.Entry(frm_user_info)
ent_first_name.grid(row=1, column=0, padx=10, pady=5)

ent_last_name = tk.Entry(frm_user_info)
ent_last_name.grid(row=1, column=1, padx=10, pady=5)

cbx_title = ttk.Combobox(frm_user_info, values=["", "Mr.", "Ms.", "Dr."])
cbx_title.grid(row=1, column=2, padx=10, pady=5)

lbl_age = tk.Label(frm_user_info, text="Age")
lbl_age.grid(row=2, column=0, padx=10, pady=5)

sbx_age = tk.Spinbox(frm_user_info, from_=18, to=100)
sbx_age.grid(row=3, column=0, padx=10, pady=5)

lbl_country = tk.Label(frm_user_info, text="Country")
lbl_country.grid(row=2, column=1, padx=10, pady=5)

cbx_country = ttk.Combobox(frm_user_info, values=[
                           "Croatia", "Slovenia", "Germany", "France"])
cbx_country.grid(row=3, column=1, padx=10, pady=5)

# lbl_
# SAVE COURSE INFO
frm_courses = tk.LabelFrame(frm)
frm_courses.grid(row=1, column=0, padx=20, pady=10)

lbl_registered = tk.Label(frm_courses, text='Registration Status')
lbl_registered.grid(row=0, column=0, padx=10, pady=5)

reg_status_var = tk.StringVar(value="Not Registered")
chkbtn_registered = tk.Checkbutton(frm_courses,
                                   text="Currently Registered",
                                   variable=reg_status_var,
                                   onvalue="Registered",
                                   offvalue=" Not Registered")
chkbtn_registered.grid(row=1, column=0, padx=10, pady=5)

lbl_num_courses = tk.Label(frm_courses, text="# Completed Courses").grid(
    row=0, column=1, padx=10, pady=5)

sbx_num_courses = tk.Spinbox(frm_courses, from_=0, to="infinity")
sbx_num_courses.grid(row=1, column=1, padx=10, pady=5)

lbl_num_semesters = tk.Label(frm_courses, text="# Semesters").grid(
    row=0, column=2, padx=10, pady=5)

sbx_num_semesters = tk.Spinbox(frm_courses, from_=0, to=10)
sbx_num_semesters.grid(row=1, column=2, padx=10, pady=5)

frm_terms = tk.LabelFrame(frm, text='Terms & Conditions')
frm_terms.grid(row=2, column=0, sticky="news", padx=20, pady=10)

accept_var = tk.StringVar(value="Not Accepted")

chkbtn_terms = tk.Checkbutton(frm_terms, text="I accept the terms and conditions.",
                              variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")
chkbtn_terms.grid(row=0, column=0)

button = tk.Button(frm, text="Enter Data")
button.grid(row=3, column=0, sticky='news', padx=20, pady=10)
button.bind("<Button-1>", handle_enter_data)

root.mainloop()
