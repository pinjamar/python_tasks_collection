# Import tkinter modul
import tkinter as tk

# DIO ZA FUNKCIJE

# Kod kreiranja GUI-a UVIJEK gradimo hijerarhijsku strukturu elemenata
# Prvi element najčešće nazivamo root kao korijen hijerarhije
# Svaki element MORA imati parent element, IZNIMKA je root koji ima Tk()

root = tk.Tk()

# Dodajmo par postavki uz pocetni prozr (Naslov, Širina X Visina prozora)
root.title('Algebra - Python Developer')
root.geometry('600x400')

# DIO ZA DODAVANJE DRUGIH ELEMENATA GUI-a
# Ovdje dodajemo druge elemente grafičkog sučelja

# Kada smo dodali sve element u GUI pokrećemo "glavnu petlju", odnosno glavni prozor
root.mainloop()