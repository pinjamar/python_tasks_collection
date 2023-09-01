import tkinter as tk
from tkinter import ttk, messagebox
import datetime as dt
import threading
from settings_module import *
from lights_module import *
from login import *
from weather_module import *
from obligations_module import *
from Meteo import podaci, grad


def open_main_window():
    global user_listbox, username, password, lights_lbox, lights_rule_cbox
    main_window = tk.Tk()
    main_window.title('Settings Notebook')

    main_notebook = ttk.Notebook(main_window)
    main_notebook.pack()

    settings(main_notebook)
    lights_tab(main_notebook)
    obligations_tab(main_notebook)
    weather_tab(main_notebook)

    main_window.mainloop()


gradovi = podaci()
split = gradovi[33]

login(split)
open_main_window()
