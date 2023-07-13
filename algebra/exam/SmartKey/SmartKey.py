# Parcijalni ispit SmartKey

# Najprije ćemo definirati cijelu hijerarhiju projekta

# Slovo a)
# Prvo imamo praktički prazno korisničko sučelje:
# 1. Kreiramo glavni frame
# 2. Kreiramo tri manja frame-a unutar glavnog frame-a
# 3. Prvi manji frame ima 1 Label i 2 Buttona (raspoređeni
#    su unutar grida 2 X 3)

# Slovo b)
# Button 'Pozvoni' otvara ekran s porukom -> messagebox
# unutar message boxa samo imamo poruku "Zvono je aktivirano!
# Netko će doći otvoriti vrata"

# Slovo c)
# Ponovno ćemo koristiti grid (6 X 9)
# Imat ćemo label 'PIN panel' (nulti redak, kroz sve stupce)

# Imat ćemo 4 entry widgeta u koji će se unositi vrijednosti
# s obzirom na to koji button je kliknut

# Imamo jedan prazan frame

# Imamo jedan veliki frame koji se proteze kroz 5 stupaca i 5 redaka

# Slovo d)
# Ako unesemo pin od admina (provjerit ćemo tako da kad su
# unesena sva 4 broja pin-a, odemo u SQL bazu i pronađemo osobu
# s tim pinom (SELECT * FROM SmartKey WHERE pin= {naš uneseni pin}))

# Ako je admin sustava -> pojavljuje se novi message box s pitanjem
# želi li se ući u administraciju sustava

# Zadnji panel će imati (6 X 4)

# Ponovno imamo label "Upravljanje ključevima"
# Imamo jedan veći frame unutar kojeg je popis osoba s digitalnim
# ključem -> widget Listbox()

# Imamo još 4 frame-a s labelima
# Imamo 3 Entry widgeta
# Imamo jedan Checkbox

# Imamo 3 buttona -> svaki ima neke funkcionalnosti!

# Kreirajmo glavni frame

import tkinter as tk
import sqlite3
import tkinter.messagebox

root = tk.Tk()

root.geometry("650x800")
root.resizable(0, 0)


pin = tk.StringVar()
znak1 = tk.StringVar()
znak2 = tk.StringVar()
znak3 = tk.StringVar()
znak4 = tk.StringVar()
ime = tk.StringVar()
prezime = tk.StringVar()
pin_new = tk.StringVar()
odustani = tk.BooleanVar()
# Prostor za funkcije


def show_frm_1():

    frm_1.grid_columnconfigure(0, weight=1)
    frm_1.grid_columnconfigure(1, weight=1)
    frm_1.grid_columnconfigure(2, weight=1)

    # Kreirajmo label i gumbe za prvi frame
    lbl_frm1 = tk.Label(frm_1, text='Panel s gumbima', font=('Arial', 10))
    lbl_frm1.grid(row=0, column=1, padx=10, pady=10)

    btn_pozvoni = tk.Button(frm_1, text='Pozvoni', font=('Arial', 16))
    btn_pozvoni.grid(row=1, column=0, padx=10, pady=10, sticky='w')

    btn_otkljucaj = tk.Button(frm_1, text='Otkljucaj', font=('Arial', 16))
    btn_otkljucaj.grid(row=1, column=2, padx=10, pady=10, sticky='e')

    btn_pozvoni.bind("<Button-1>", handle_pozvoni)
    btn_otkljucaj.bind("<Button-1>", handle_otkljucaj)


def handle_pozvoni(event):
    tkinter.messagebox.showinfo(
        message='Zvono je aktivirano!\nNetko će doći otvoriti vrata.')


def handle_otkljucaj(event):
    global ent_pin_1, ent_pin_2, ent_pin_3, ent_pin_4

    frm_2.grid_columnconfigure(0, weight=1)
    frm_2.grid_columnconfigure(1, weight=1)
    frm_2.grid_columnconfigure(2, weight=1)
    frm_2.grid_columnconfigure(3, weight=1)
    frm_2.grid_columnconfigure(4, weight=50)

    lbl_pin = tk.Label(frm_2, text="PIN panel").grid(
        row=0, column=0,  columnspan=5, padx=10, pady=10)

    ent_pin_1 = tk.Entry(frm_2, width=5, state="disabled", textvariable=znak1)
    ent_pin_1.grid(row=1, column=0, padx=5, pady=5)
    ent_pin_2 = tk.Entry(frm_2, width=5, state="disabled", textvariable=znak2)
    ent_pin_2.grid(row=1, column=1, padx=5, pady=5)
    ent_pin_3 = tk.Entry(frm_2, width=5, state="disabled", textvariable=znak3)
    ent_pin_3.grid(row=1, column=2, padx=5, pady=5)
    ent_pin_4 = tk.Entry(frm_2, width=5, state="disabled", textvariable=znak4)
    ent_pin_4.grid(row=1, column=3, padx=5, pady=5)

    lbl_status = tk.Label(frm_2, text="Status i poruke", font=(
        'Arial', 10)).grid(row=1, column=4, padx=10, pady=10)
    lbl_status_messages = tk.Label(frm_2, text="Poruka", font=(
        'Arial', 16)).grid(row=2, rowspan=3, column=4, padx=10, pady=10)

    btn_dig_1 = tk.Button(frm_2, text="1", width=4)
    btn_dig_1.grid(row=2, column=0, padx=5, pady=5)
    btn_dig_1.bind("<Button-1>", lambda i: enter_pin("1"))
    btn_dig_2 = tk.Button(frm_2, text="2", width=4)
    btn_dig_2.grid(row=2, column=1, padx=5, pady=5)
    btn_dig_2.bind("<Button-1>", lambda i: enter_pin("2"))
    btn_dig_3 = tk.Button(frm_2, text="3", width=4)
    btn_dig_3.grid(row=2, column=2, padx=5, pady=5)
    btn_dig_3.bind("<Button-1>", lambda i: enter_pin("3"))
    btn_dig_4 = tk.Button(frm_2, text="4", width=4)
    btn_dig_4.grid(row=3, column=0, padx=5, pady=5)
    btn_dig_4.bind("<Button-1>", lambda i: enter_pin("4"))
    btn_dig_5 = tk.Button(frm_2, text="5", width=4)
    btn_dig_5.grid(row=3, column=1, padx=5, pady=5)
    btn_dig_5.bind("<Button-1>", lambda i: enter_pin("5"))
    btn_dig_6 = tk.Button(frm_2, text="6", width=4)
    btn_dig_6.grid(row=3, column=2, padx=5, pady=5)
    btn_dig_6.bind("<Button-1>", lambda i: enter_pin("6"))
    btn_dig_7 = tk.Button(frm_2, text="7", width=4)
    btn_dig_7.grid(row=4, column=0, padx=5, pady=5)
    btn_dig_7.bind("<Button-1>", lambda i: enter_pin("7"))
    btn_dig_8 = tk.Button(frm_2, text="8", width=4)
    btn_dig_8.grid(row=4, column=1, padx=5, pady=5)
    btn_dig_8.bind("<Button-1>", lambda i: enter_pin("8"))
    btn_dig_9 = tk.Button(frm_2, text="9", width=4)
    btn_dig_9.grid(row=4, column=2, padx=5, pady=5)
    btn_dig_9.bind("<Button-1>", lambda i: enter_pin("9"))
    btn_dig_none = tk.Button(frm_2, width=4)
    btn_dig_none.grid(row=5, column=0, padx=5, pady=5)
    btn_dig_0 = tk.Button(frm_2, text="0", width=4)
    btn_dig_0.grid(row=5, column=1, padx=5, pady=5)
    btn_dig_0.bind("<Button-1>", lambda i: enter_pin("0"))
    btn_dig_C = tk.Button(frm_2, text="C", width=4)
    btn_dig_C.grid(row=5, column=2, padx=5, pady=5)
    btn_dig_C.bind("<Button-1>", lambda i: enter_pin("C"))

    # enter_admin_sustav()


def enter_pin(text):
    if text == "C":
        pin.set("")
        znak1.set("")
        znak2.set("")
        znak3.set("")
        znak4.set("")
        return

    if len(pin.get()) == 0:
        znak1.set(text)
        pin.set(znak1.get())
    elif len(pin.get()) == 1:
        znak2.set(text)
        new_pin = pin.get() + znak2.get()
        pin.set(new_pin)
    elif len(pin.get()) == 2:
        znak3.set(text)
        new_pin = pin.get() + znak3.get()
        pin.set(new_pin)
    elif len(pin.get()) == 3:
        znak4.set(text)
        new_pin = pin.get() + znak4.get()
        pin.set(new_pin)
        print_message_enter_admin_system(pin)
        # Nakon što se sve izvrši naša duljina pina će postati 4! Sad želimo preći na novi korak !!


def print_message_enter_admin_system(pin):
    # Želimo se sada povezati na našu SmartKey bazu
    # NAPOMENA: Rekreirajte SQLiteSMartKey.py tako da osim ona tri field, prima još i field aktivan koji je boolean
    conn = sqlite3.connect('SmartKey.db')
    cursor = conn.cursor()

    select_by_pin_query = '''SELECT * FROM Users WHERE pin=?'''
    cursor.execute(select_by_pin_query, (pin.get(),))
    record = cursor.fetchone()

    # Nakon što se spojimo na bazu, EXECUTEamo query, FETCHONEamo rezultat i spremamo u varijablu record
    # probajte isprintati record da vidite u kojem je obliku

    if record == None:
        lbl_greeting_message = tk.Label(frm_2,
                                        text=f'Pogresan PIN!',
                                        font=('Arial', 18))
        lbl_greeting_message.grid(row=2, rowspan=3, column=4, padx=10, pady=10)
        enter_pin("C")
        return

    lbl_greeting_message = tk.Label(frm_2,
                                    text=f'PIN je uspješno unešen.\nDobro došli {record[0]} {record[1]}',
                                    font=('Arial', 18))
    lbl_greeting_message.grid(row=2, rowspan=3, column=4, padx=10, pady=10)

    if record[0] == "Admin":
        answer = tkinter.messagebox.askquestion(title="Ulazak u Admin sustav",
                                                message='Zelite li pokrenuti sustav administracije?')

    if answer == "yes":
        enter_admin_sustav()


def enter_admin_sustav():

    # cbox_aktivan (checkbox widget)

    global ent_ime, ent_prezime, ent_pin, lbox_users

    frm_3.grid_columnconfigure(0, weight=10)
    frm_3.grid_columnconfigure(1, weight=1)
    frm_3.grid_columnconfigure(2, weight=1)
    frm_3.grid_columnconfigure(3, weight=1)

    lbl_admin = tk.Label(frm_3, text="Upravljanje dodijeljenim kljucevima").grid(
        row=0, column=0,  columnspan=4, padx=10, pady=10)

    conn = sqlite3.connect('SmartKey.db')
    cursor = conn.cursor()
    select_all = '''SELECT * FROM Users'''
    cursor.execute(select_all)

    records = cursor.fetchall()

    lbox_users = tk.Listbox(frm_3)
    lbox_users.grid(row=1, column=0, rowspan=4)
    lbox_users.bind("<<ListboxSelect>>", item_selected)

    for record in records:
        lbox_users.insert("end", f"{record[0]} {record[1]}")

    lbl_ime = tk.Label(frm_3, text="Ime")
    lbl_ime.grid(row=1, column=1, sticky="e")
    ent_ime = tk.Entry(frm_3, textvariable=ime)
    ent_ime.grid(row=1, column=2, padx=5, pady=5)

    lbl_prezime = tk.Label(frm_3, text="Prezime")
    lbl_prezime.grid(row=2, column=1, sticky="e")
    ent_prezime = tk.Entry(frm_3, textvariable=prezime)
    ent_prezime.grid(row=2, column=2, padx=5, pady=5)

    lbl_pin = tk.Label(frm_3, text="PIN (4 broja)")
    lbl_pin.grid(row=3, column=1, sticky="e")
    ent_pin = tk.Entry(frm_3, textvariable=pin_new)
    ent_pin.grid(row=3, column=2, padx=5, pady=5)

    lbl_aktivan = tk.Label(frm_3, text="Aktivan")
    lbl_aktivan.grid(row=4, column=1, sticky="e")
    ent_aktivan = tk.Checkbutton(frm_3, variable="")
    ent_aktivan.grid(row=4, column=2, padx=25, pady=5, sticky="w")

    frame_action_buttons = tk.Frame(frm_3)
    frame_action_buttons.grid(row=5, column=2, columnspan=2)

    button_spremi = tk.Button(frame_action_buttons,
                              bd=2, relief=tk.SOLID, text='Spremi')
    button_spremi.bind("<Button-1>", handle_spremi)
    button_spremi.grid(row=5, column=1, padx=10, pady=10, sticky='ew')

    button_odustani = tk.Button(
        frame_action_buttons, bd=2, relief=tk.SOLID, text='Odustani')
    button_odustani.bind("<Button-1>", handle_odustani)
    button_odustani.grid(row=5, column=2, padx=10, pady=10, sticky='ew')

    button_izbrisi = tk.Button(
        frame_action_buttons, bd=2, relief=tk.SOLID, text='Izbrisi')
    button_izbrisi.bind("<Button-1>", handle_izbrisi)
    button_izbrisi.grid(row=5, column=3, padx=10, pady=10, sticky='ew')


def item_selected(event):
    temp = lbox_users.get(lbox_users.curselection())
    temp_list = temp.split()
    ime.set(temp_list[0])
    prezime.set(temp_list[1])

    conn = sqlite3.connect('SmartKey.db')
    cursor = conn.cursor()

    select_by_ime_query = '''SELECT * FROM Users WHERE ime=?'''
    cursor.execute(select_by_ime_query, (ime.get(),))
    record = cursor.fetchone()

    pin_new.set(record[2])

    print(ime.get(), prezime.get(), pin_new.get())


def handle_spremi(event):
    conn = sqlite3.connect('SmartKey.db')
    cursor = conn.cursor()

    update_by_pin_query = '''UPDATE Users
                   SET ime=?,
                       prezime=?,
                       pin=?
                    WHERE pin=?'''

    insert_into_query = '''INSERT INTO Users (ime, prezime, pin)
                       VALUES (?,?,?)'''

    if odustani.get():
        cursor.execute(insert_into_query, (ime.get(),
                       prezime.get(), pin_new.get()))
        lbox_users.insert(item, f"{ime.get()} {prezime.get()}")
    else:
        cursor.execute(update_by_pin_query, (ime.get(),
                       prezime.get(), pin_new.get(), pin_new.get()))
        for item in lbox_users.curselection():
            lbox_users.delete(item)
            lbox_users.insert(item, f"{ime.get()} {prezime.get()}")

    conn.commit()
    cursor.close()

    conn.close()


def handle_odustani(event):
    odustani.set(tk.TRUE)


def handle_izbrisi(event):
    conn = sqlite3.connect('SmartKey.db')
    cursor = conn.cursor()

    temp = lbox_users.get(lbox_users.curselection())
    temp_list = temp.split()
    select_by_ime_query = '''SELECT * FROM Users WHERE ime=?'''
    cursor.execute(select_by_ime_query, (temp_list[0],))
    record = cursor.fetchone()

    delete_from_query = '''DELETE FROM Users WHERE ime=? AND prezime=? AND pin=?'''
    cursor.execute(delete_from_query, (temp_list[0], temp_list[1], record[2]))

    lbox_users.delete(lbox_users.curselection())
    conn.commit()
    cursor.close()

    conn.close()


# MAIN

frm = tk.Frame(root, bd=2, relief=tk.SOLID)
frm.pack(padx=10, pady=10)

# Kreirajmo tri manja okvira
frm_1 = tk.Frame(frm, bd=2, relief=tk.SOLID, width=600, height=110)
frm_1.grid(row=0, column=0, padx=10, pady=10, sticky='news')
frm_1.grid_propagate(0)

show_frm_1()

frm_2 = tk.Frame(frm, bd=2, relief=tk.SOLID, width=600, height=300)
frm_2.grid(row=1, column=0, padx=10, pady=10, sticky='news')
frm_2.grid_propagate(0)

frm_3 = tk.Frame(frm, bd=2, relief=tk.SOLID, width=600, height=300)
frm_3.grid(row=2, column=0, padx=10, pady=10, sticky='news')
frm_3.grid_propagate(0)

# Započni GUI petlju
root.mainloop()
