"""
Widget  Variable    Example
Label   lbl         lbl_name
Button  btn         btn_pozvoni
Entry   ent         ent_age
Text    txt         txt_note
"""

import random as rnd
import tkinter as tk

root = tk.Tk()
root.title('Algebra - Python Developer | Password Generator')

# Globalne Varijable
slova_var = tk.BooleanVar()
brojevi_var = tk.BooleanVar()
znakovi_var = tk.BooleanVar()
prikazi_lozinku = tk.StringVar()
prikazi_lozinku.set('prikazi')
lozinka_var = tk.StringVar()

# DIO ZA FUNKCIJE


def set_prikaz_lozinke():
    if prikazi_lozinku.get() == 'prikazi':
        ent_lozinka.config(show="")
    else:
        ent_lozinka.config(show="*")


def set_duzina_lozinke(value):
    duzina_lozinke.set(int(value))


def generiraj_lozinku():
    # od 33 do 47 i 58 do 64 i 91 do 96     posebni znakovi
    # od 65 do 90 i 97 do 122               slova
    # od 48 do 57                           brojevi
    broj_znakova = duzina_lozinke.get()
    lozinka = ''
    for znak in range(broj_znakova):
        if slova_var.get():
            kompleksnost = rnd.choice([(65, 90), (97, 122)])
        elif brojevi_var.get():
            kompleksnost = rnd.choice([(48, 57)])
        elif znakovi_var.get():
            kompleksnost = rnd.choice([(33, 47), (58, 64), (91, 96)])
        else:
            kompleksnost = rnd.choice([(33, 122)])

        random_broj = rnd.randint(kompleksnost[0], kompleksnost[-1])
        znak = chr(random_broj)
        lozinka += znak

    lozinka_var.set(str(lozinka))


def kopiraj_lozinku():
    root.clipboard_clear()
    root.clipboard_append(lozinka_var.get())


def resetiraj_lozinku():
    lozinka_var.set('')


# DIO ZA DODAVANJE DRUGIH ELEMENATA GUI-a

frm_postavke = tk.Frame(root).grid(column=0, columnspan=3, row=0, rowspan=3)

# labelFrame - Postavke
lbl_frm_postavke = tk.LabelFrame(frm_postavke, text='Postavke')
lbl_frm_postavke.grid(column=0, columnspan=3, row=0,
                      rowspan=3, padx=10, pady=10)

# Checkboxes
ch_box_slova = tk.Checkbutton(lbl_frm_postavke,
                              text='Samo slova',
                              variable=slova_var).grid(row=0, column=0)

ch_box_brojevi = tk.Checkbutton(lbl_frm_postavke,
                                text='Samo brojevi',
                                variable=brojevi_var).grid(row=0, column=1)

ch_box_znakovi = tk.Checkbutton(lbl_frm_postavke,
                                text='Samo posebni znakovi',
                                variable=znakovi_var).grid(row=0, column=2)
# Radiobuttons
rb_prikazi_lozinku = tk.Radiobutton(lbl_frm_postavke,
                                    text='Prikazi generiranu lozinku',
                                    variable=prikazi_lozinku,
                                    command=set_prikaz_lozinke,
                                    value='prikazi'
                                    ).grid(column=0, row=1)

rb_sakrij_lozinku = tk.Radiobutton(lbl_frm_postavke,
                                   text='Sakrij generiranu lozinku',
                                   variable=prikazi_lozinku,
                                   command=set_prikaz_lozinke,
                                   value='sakrij'
                                   ).grid(column=2, row=1)

# Klizac za duzinu zaporke
duzina_lozinke = tk.IntVar()
duzina_lozinke.set(10)
scl_duzina = tk.Scale(lbl_frm_postavke,
                      orient='horizontal',
                      variable=duzina_lozinke,
                      length=300,
                      from_=8,
                      to=40,
                      command=set_duzina_lozinke)
scl_duzina.grid(column=0, columnspan=3, row=2)

# Gumbi
frm_action_buttons = tk.Frame(root).grid(
    column=0, columnspan=3, row=3, padx=10, pady=20)
# Generiraj Button
btn_generiraj = tk.Button(
    frm_action_buttons, text='Generiraj lozinku', command=generiraj_lozinku)
btn_generiraj.grid(column=0, row=3)
# Copy Button
btn_kopiraj = tk.Button(
    frm_action_buttons, text='Kopiraj lozinku', command=kopiraj_lozinku)
btn_kopiraj.grid(column=1, row=3)
# Reset Button
btn_resetiraj = tk.Button(
    frm_action_buttons, text='Resetiraj lozinku', command=resetiraj_lozinku)
btn_resetiraj.grid(column=2, row=3)

# Frame Display Generated Password
frm_display_gen_password = tk.Frame(root).grid(
    column=0, columnspan=3, row=4, rowspan=2, padx=10, pady=10)
# Label Display
lbl_password = tk.Label(frm_display_gen_password,
                        text='Generirana lozinka', font=('Segoe UI', 14))
lbl_password.grid(column=0, columnspan=3, row=4)
# Entry Display
ent_lozinka = tk.Entry(frm_display_gen_password,
                       textvariable=lozinka_var,
                       justify='center',
                       font=('Segoe', 16),
                       width=30,
                       background='systembuttonface',
                       bd=0)
ent_lozinka.grid(column=0, columnspan=3, row=5, padx=15, pady=10)

root.mainloop()
