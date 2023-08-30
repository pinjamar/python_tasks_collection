import tkinter as tk
import datetime as dt
from tkinter import ttk

lights = [{
    'name':'Dnevna soba',
    'is_on': True},
    {
        'name': 'Kupaonica',
        'is_on': False
    }
    ]
 
def refresh_lights():
    lights_lbox.delete(0,tk.END)
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
        if current_time > dt.time(22,0):
            selected_light['is_on'] = False
            refresh_lights()
 
    # threading.Timer(5, auto_light_ctrl).start()

def lights_tab(notebook):
    global lights_rule_cbox, lights_lbox
    #Lights tab
    lights_tab = tk.Frame(notebook)
    notebook.add(lights_tab, text="Lights")
 
    lights_lbl = tk.Label(lights_tab, text='Svijetla: ', font=('Arial', 15))
    lights_lbl.pack()
 
    lights_lbox = tk.Listbox(lights_tab)
    refresh_lights()
    lights_lbox.pack()
 
    on_off_btn = tk.Button(lights_tab, text='ON/OFF', command= toggle_lights)
    on_off_btn.pack(pady=10)
 
    lights_rule_cbox = ttk.Combobox(lights_tab, values = ['Ugasi nakon 22h'])
    lights_rule_cbox.pack(pady=10)
 
    rule_apply_btn = tk.Button(lights_tab, text = 'Primjeni pravilo', command=auto_light_ctrl)
    rule_apply_btn.pack(pady=5)