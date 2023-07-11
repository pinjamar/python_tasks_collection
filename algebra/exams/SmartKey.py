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
# from tkinter import messagebox
# OVDJE DEFINIRAMO GLOBANE VARIJABLE
pin = tk.StringVar()

znak1 = tk.StringVar()
znak2 = tk.StringVar()
znak3 = tk.StringVar()
znak4 = tk.StringVar()

odustani = tk.BooleanVar()

# UVIJEK PRVO GLAVNI PROZOR!!!
root = tk.Tk()

# Prostor za funkcije
def handle_pozvoni(event):
    pass
    # TODO
    # hint MessageBox koji nosi neki info text: 'Zvono je aktivirano!\nNetko će doći otvoriti vrata.

def handle_otkljucaj(event):
    pass
    # global ent_pin1,....

    # TODO
    # PARENT WIDGETIMA: frm_2

    # lbl_pin = ....

    # ent_pin1, ent_pin2, ent_pin3, ent_pin4 -> textvariable = znak1, 2, 3, 4
    # HINT: moraju imati state='disabled' da ne može pisati direktno u njih

    # btn_0 .... btn_9 -> povezao sam ih s funkcijom enter_pin(text) # text = text u definiciji buttona
    # btn_c -> samo obriše cijelu do tad uneseni pin - kad se stisne samo treb pin.set(''), pobrisati text iz entry widgeta

    # frm_empty - dodate mu debljinu bordera, relief ...

    # frm_status_messages unutar kojeg ide lbl_status_messages

def enter_pin(text):
    if len(pin.get()) == 0: 
        znak1.set(text) # unutar buttona ćemo imati command = enter_pin(text) -> '1' ako kliknemo na btn_1
        pin.set(znak1.get())
    elif len(pin.get()) == 1:
        znak2.set(text)
        new_pin = pin.get() + znak2.get()
        pin.set(new_pin)
    elif len(pin.get()) == 2:
        # TODO
        pass
    elif len(pin.get()) == 3:
        # TODO
        pass
        
        # Nakon što se sve izvrši naša duljina pina će postati 4! Sad želimo preći na novi korak !!
        print_message_enter_admin_system(pin)
    
def print_message_enter_admin_system(pin):
    # Želimo se sada povezati na našu SmartKey bazu
    # NAPOMENA: Rekreirajte SQLiteSMartKey.py tako da osim ona tri field, prima još i field aktivan koji je boolean
    conn = sqlite3.connect('SmartKey.db')

    # TODO
    select_by_pin_query = '' 
    # Sada se samo vodite vašim SQLiteSmartKey primjerima (HINT: vrijednost pina pin.get())

    # Nakon što se spojimo na bazu, EXECUTEamo query, FETCHONEamo rezultat i spremamo u varijablu record
    # probajte isprintati record da vidite u kojem je obliku

    # TODO
    # record = ....

    lbl_greeting_message = tk.Label(frm_status_messages,
                                    text = f'PIN je uspješno unešen.\nDobro došli {record[0]} {record[1]}',
                                    font = ('Segoe UI', 18))
    lbl_greeting_message.pack()

    if record[0] == "admin":
        answer = tk.messagebox.askquestion(title="Ulazak u Admin sustav", 
                                           message = 'Zelite li pokrenuti sustav administracije?')
    
    if answer == #TODO
        enter_admin_sustav()

def enter_admin_sustav():
    # AKO ŽELITE KORISTITI WIDGETE IZ OVE FUNKCIJE 
    # OBAVEZNO DODATI IME WIDGETA U GLOBAL
    # TODO
    # global ime_widgeta

    # lbl_kljucevi

    # frm_lista_ljudi
    # lbl_lista_ljudi
    # listbox_popis_osoba

    # frm_ime
    # lbl_ime

    # frm_prezime
    # lbl_prezime

    # frm_pin
    # lbl_pin

    # frm_aktivan
    # lbl_aktivan

    # ent_ime
    # ent_prezime
    # ent_pin
    # cbox_aktivan (checkbox widget)

    frame_action_buttons = tk.Frame()
    frame_action_buttons.grid_columnconfigure(0, weight=1)
    frame_action_buttons.grid_columnconfigure(1, weight=1)
    frame_action_buttons.grid_columnconfigure(2, weight=1)
    frame_action_buttons.grid(row=5, column=2, columnspan=2)

    button_spremi = tk.Button(frame_action_buttons, bd=2, relief=tk.SOLID, text='Spremi')
    button_spremi.bind("<Button-1>", handle_spremi)
    button_spremi.grid(row=0, column=0, padx=10, pady=10, sticky='ew')

    button_odustani = tk.Button(frame_action_buttons, bd=2, relief=tk.SOLID, text='Odustani')
    button_odustani.bind("<Button-1>", handle_odustani)
    button_odustani.grid(row=0, column=1, padx=10, pady=10, sticky='ew')

    button_izbrisi = tk.Button(frame_action_buttons, bd=2, relief=tk.SOLID, text='Izbrisi')
    button_izbrisi.bind("<Button-1>", handle_izbrisi)
    button_izbrisi.grid(row=0, column=2, padx=10, pady=10, sticky='ew')

def handle_spremi(event):
    conn = sqlite3.connect('SmartKey.db')
    cursor = conn.cursor()

    if odustani.get():
        cursor.execute(insert_into_query) # Insertati ćemo zapis koji ćemo dohvatiti u ovisnosti o kliku na ime i prezime u
                                          # select boxu
        # Onda koristimo insert naredbu
    else:
        cursor.execute(update_query)
        # Ovdje koristimo update naredbu
    
    conn.commit()
    cursor.close()

    conn.close()

def handle_odustani(event):
    odustani.set(tk.TRUE)

def handle_izbrisi(event):
    #TODO
    pass


# Kreirajmo glavni frame s nekom vidljivom granicom
frm = tk.Frame(root, bd=2, relief=tk.SOLID)
frm.pack(padx=10, pady=10)

# Kreirajmo tri manja okvira
frm_1 = tk.Frame(frm, bd=2, relief=tk.SOLID, width=600, height=135)
frm_1.grid_columnconfigure(0, weight=1)
frm_1.grid_columnconfigure(1, weight=1)
frm_1.grid_columnconfigure(2, weight=1)
frm_1.grid(row=0, column=0, padx=10, pady=10, sticky='news')

frm_2 = tk.Frame(frm, bd=2, relief=tk.SOLID, width=600, height=300)
frm_2.grid(row=1, column=0, padx=10, pady=10)

frm_3 = tk.Frame(frm, bd=2, relief=tk.SOLID, width=600, height=300)
frm_3.grid(row=2, column=0, padx=10, pady=10)

# Kreirajmo label i gumbe za prvi frame
lbl_frm1 = tk.Label(frm_1, text='Panel s gumbima', font=('Arial', 10))
lbl_frm1.grid(row=0, column=1, padx=10, pady=10)

btn_pozvoni = tk.Button(frm_1, text = 'Pozvoni', font=('Arial', 16))
btn_pozvoni.grid(row=1, column=0, padx=10, pady=10, sticky='w')

btn_otkljucaj = tk.Button(frm_1, text = 'Otkljucaj', font=('Arial', 16))
btn_otkljucaj.grid(row=1, column=2, padx=10, pady=10, sticky='e')

btn_pozvoni.bind("<Button-1>", handle_pozvoni)
btn_otkljucaj.bind("<Button-1>", handle_otkljucaj)

# Započni GUI petlju
root.mainloop()
