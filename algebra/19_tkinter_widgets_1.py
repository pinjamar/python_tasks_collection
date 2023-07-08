# Import tkinter modul
import tkinter as tk

# DIO ZA FUNKCIJE
def click():
    print('Gumb "button_click" je kliknut')

root = tk.Tk()

root.title('Algebra - Python Developer')
root.geometry('600x400')

# Dodajmo element Button kojem ćemo kao prvi argument
button = tk.Button(root, text = "GUMBIC", relief = tk.FLAT)

# MORAMO definirati kako će naš "button" biti pozicioniran unutar svojeg PARENT elementa
# Kada smo dodali sve element u GUI pokrećemo "glavnu petlju", odnosno glavni prozor
button.pack()

# Kreirajmo novi gumb koji će ispisati poruku u konzoli da smo kliknuli na gumb
# Najprije ćemo definirati funkciju koja će biti pozvana kad kliknemo na gumb

button_click = tk.Button(root, text = 'Klikni me!', command = click)#.pack(padx = 10, pady = 10)
button_click.pack(padx = 50, pady = 50)
# Padx i pady sluze za odvajanje elemenata po x odnosno y osi

# Kreirajmo varijablu u koju ćemo pohraniti fotografiju
btn_image = tk.PhotoImage(file='python.gif')

button_image = tk.Button(root,
                         text = "Gumbek sa slicicom",
                         image = btn_image,
                         compound = tk.LEFT,
                         relief=tk.FLAT,
                         state = tk.DISABLED).pack(padx=10, pady=10)

root.mainloop()
